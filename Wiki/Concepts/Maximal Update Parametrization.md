---
role: notion
nom: Maximal Update Parametrization
alias: [µP, muP, mu-P, µTransfer, muTransfer, transfert d'hyperparamètres, hyperparameter transfer, Tensor Programs, u-µP]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [learning-rate, scaling-laws, hyperparameter-tuning, optimization, deep-learning]
---

# Maximal Update Parametrization

## Aperçu

- Règle de paramétrisation (initialisation + taux d'apprentissage **par couche**, en fonction de la largeur du réseau) qui rend les **dynamiques d'entraînement invariantes à l'échelle** : un réseau de largeur 256 et un réseau de largeur 8192 s'entraînent « de la même façon ».
- Conséquence pratique, et c'est tout l'intérêt : le **meilleur taux d'apprentissage trouvé sur un petit modèle proxy reste optimal sur le grand**. C'est le **µTransfer** — on cherche les hyperparamètres là où c'est bon marché, on les applique là où c'est ruineux.
- Réponse à un problème très concret : sans µP, l'optimum de LR se **déplace** quand on grossit le modèle. Chaque changement d'échelle redemande une recherche, ou pire, on hérite d'un LR devenu trop grand (divergence) ou trop petit (couches gelées de fait).

## Concepts clés

### Le problème : ce qui casse quand on élargit

- Sous la paramétrisation standard (init en $1/\sqrt{\text{fan\_in}}$, un LR global unique), la **taille des mises à jour** ne se comporte pas de la même façon dans toutes les couches quand la largeur augmente.
- Deux régimes dégénérés encadrent l'espace :
  - LR trop grand pour l'échelle → les activations explosent, l'entraînement diverge ;
  - LR trop petit → les couches internes **n'apprennent essentiellement rien** (le réseau se comporte comme un modèle à noyau : seule la dernière couche bouge). C'est le régime « NTK », stable mais sans apprentissage de features.
- Entre les deux existe un **unique** régime où toutes les couches apprennent à un rythme comparable, quelle que soit la largeur : c'est celui que µP vise, d'où le nom *maximal update* — la plus grande mise à jour qui reste stable.

### La règle : chaque type de paramètre a son échelle

- µP classe les paramètres par nature — **entrée / embeddings**, **couches cachées**, **sortie / readout** — et prescrit pour chaque classe comment l'initialisation **et** le LR doivent varier avec la largeur.
- L'intuition en une phrase : ce qui doit rester constant à travers les échelles, c'est l'**amplitude du changement des activations** à chaque pas, pas l'amplitude des poids. On ajuste donc les poids et les pas pour que l'effet observable soit invariant.
- Point souvent mal compris : µP n'est **pas** « diviser le LR par la largeur ». C'est un jeu de règles différenciées par type de couche — appliquer un seul facteur global rate l'objectif.
- Le cadre théorique est celui des *Tensor Programs* (Yang et al.), qui étudie les limites de réseaux à largeur infinie. µP est la paramétrisation où cette limite est un régime d'**apprentissage de features** non trivial.

### µTransfer : le protocole

1. Fixer l'architecture cible, en dériver un **proxy étroit** (même profondeur, même données, largeur réduite d'un ordre de grandeur).
2. Chercher les hyperparamètres sur le proxy — LR, warmup, échelle d'init, éventuellement paramètres d'[[Adam optimizer|Adam]].
3. **Transférer** au modèle cible via les règles µP, sans nouvelle recherche.
- Ce qui transfère bien : LR, échelle d'initialisation, échelle de sortie. Ce qui transfère mal ou pas : tout ce qui dépend du **budget de tokens** ou de la **taille de batch** — le calendrier de LR, la taille de batch optimale, la longueur du warmup restent à traiter à part. µP est un résultat sur la **largeur**, étendu à la profondeur par des travaux ultérieurs, pas une invariance universelle.

### Où ça se joue en 2026

- µP est passé du statut de curiosité théorique à celui d'outillage standard des gros pré-entraînements : c'est ce qui rend défendable de dépenser un budget de recherche d'hyperparamètres sur un modèle 100× plus petit que la cible.
- Prolongements notables : **u-µP** (unit-scaled µP) qui combine µP et *unit scaling* pour bien se marier avec la [[Mixed precision|basse précision]], et l'extension à la **profondeur** (Tensor Programs VI).

## Les maths, simplement

- Objectif formel : que $\Delta h_\ell$, le changement d'activation de la couche $\ell$ après un pas d'optimisation, soit d'ordre $\Theta(1)$ — indépendant de la largeur $d$. Ni $\Theta(d)$ (explosion), ni $\Theta(1/d)$ (couche inerte).
- Pour une couche cachée $W \in \mathbb{R}^{d \times d}$, l'initialisation se prend en variance $\propto 1/d$ (donc $\sigma \propto 1/\sqrt{d}$, comme d'habitude), mais le **LR** doit décroître avec $d$ pour compenser le fait qu'une mise à jour agrège $d$ termes corrélés. L'exposant exact dépend de l'optimiseur : sous Adam, le LR des couches cachées se met à l'échelle en $\propto 1/d$.
- La couche de **sortie** suit une règle différente (souvent une multiplication du logit par $1/d$ ou un LR distinct), parce qu'elle projette vers une dimension **fixe** : elle ne subit pas la même agrégation.
- Vérification empirique classique : tracer la perte en fonction du LR pour plusieurs largeurs. En paramétrisation standard, les courbes en U ont leur **minimum qui glisse** vers la gauche quand la largeur croît. Sous µP, les minima **se superposent** — c'est la signature visuelle du transfert, et le test à faire avant de croire à son implémentation.

## En pratique

- Le bénéfice est proportionnel à l'écart d'échelle : sur un fine-tuning ou un modèle de quelques dizaines de millions de paramètres, µP ne rapporte pas le coût de son implémentation. Sur un pré-entraînement multi-milliards, il rembourse un budget de tuning entier.
- La mise en œuvre est **piégeuse** : il faut classer correctement chaque paramètre (embeddings, biais, normalisations, readout, poids attachés) et l'oubli d'une classe suffit à casser le transfert sans erreur visible. Le test de superposition des courbes en U est donc obligatoire, jamais optionnel.
- La bibliothèque de référence est `mup` (Microsoft) ; les grosses piles d'entraînement modernes intègrent leurs propres variantes.
- Complémentaire des [[Scaling laws|lois d'échelle]], pas redondant : les lois d'échelle disent **quelle taille** entraîner pour un budget ; µP dit **avec quels hyperparamètres** l'entraîner sans les rechercher à l'échelle cible.
- Piège de raisonnement : µP ne rend pas l'entraînement meilleur en soi. Il rend le réglage **transférable**. Une équipe qui a déjà un LR bien réglé pour son échéquier de tailles n'en tirera rien de spectaculaire.

## Approches voisines & alternatives

- [[Learning rate schedules]] — µP fixe l'**échelle** du LR selon la largeur ; le calendrier (warmup, cosine, decay) reste un problème distinct qui ne transfère pas automatiquement.
- [[Optimisation d'hyperparamètres]] — µTransfer déplace la recherche vers un proxy bon marché au lieu de l'améliorer ; les deux se combinent.
- [[Scaling laws]] — l'autre moitié de la question d'échelle : combien de paramètres et de tokens pour un budget donné.
- [[Adam optimizer]] — les exposants µP dépendent de l'optimiseur ; les règles usuelles sont énoncées pour Adam / AdamW.
- [[Gradient descent]] — µP est une réponse au conditionnement de la descente quand la dimension change.
- [[Loss landscape and saddle points]] — même famille de préoccupation : stabilité et conditionnement de l'entraînement profond.
- [[Mixed precision]] — l'interaction avec la basse précision motive u-µP (unit scaling).
- [[Attention Residuals]] — autre levier sur la stabilité en profondeur, côté **architecture** plutôt que paramétrisation.
- Alternative pragmatique : **règles empiriques de mise à l'échelle du LR** (heuristiques en $1/\sqrt{d}$, LR ∝ batch size) — moins fondées, sans garantie de transfert, mais sans coût d'implémentation.

## Pour aller plus loin

- Yang & Hu (2021) — *Tensor Programs IV: Feature Learning in Infinite-Width Neural Networks* (le fondement théorique).
- Yang et al. (2022) — *Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer* (le papier µTransfer).
- Yang et al. (2023) — *Tensor Programs VI: Feature Learning in Infinite-Depth Neural Networks* (arXiv 2310.02244 — extension à la profondeur).
- Blake et al. (2024) — *u-µP: The Unit-Scaled Maximal Update Parametrization* (arXiv 2407.17465).
- Dépôt `microsoft/mup` — implémentation de référence et outils de vérification du transfert.
