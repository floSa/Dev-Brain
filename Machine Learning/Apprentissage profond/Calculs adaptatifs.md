---
role: notion
nom: Calculs adaptatifs
alias: [adaptive computation, calcul adaptatif, early exit, sortie anticipée, Mixture of Depths, MoD, looped transformers, Mixture of Recursions, MoR, adaptive depth, ponder]
categorie: ml/apprentissage-profond
domaines: [ml-eng, ai-eng]
tags: [inference-optimization, reasoning, transformers, mixture-of-experts, deep-learning]
---

# Calculs adaptatifs

## Aperçu

- Un [[Transformer architectures|Transformer]] standard dépense **exactement le même calcul** pour chaque token : toutes les couches, tout le temps. Prédire « de » après « la maison » coûte autant que résoudre une étape de raisonnement mathématique.
- Les calculs adaptatifs cassent cette uniformité : **allouer la profondeur selon la difficulté**, par token ou par exemple. Le token facile sort tôt (ou saute des couches), le token difficile en consomme plus.
- La famille regroupe trois gestes distincts qu'on confond souvent : **sortir tôt** (early exit), **sauter des couches** (Mixture of Depths), **boucler sur les mêmes couches** (looped transformers). Seul le troisième permet de dépenser *plus* que la profondeur nominale.

## Concepts clés

### Sortie anticipée (early exit)

- Le modèle porte des têtes de prédiction intermédiaires ; dès qu'un critère de confiance est atteint à une couche donnée, on renvoie la prédiction sans traverser le reste de la pile.
- Le critère est le point délicat. L'**entropie** de la distribution prédite est le signal usuel (basse entropie → décision faite), avec un seuil appris plutôt que fixé à la main. Un seuil mal calibré donne soit aucune économie, soit une dégradation silencieuse sur les cas durs.
- Problème pratique majeur en génération autorégressive : si un token sort à la couche 8, les couches 9 à 32 **n'ont pas produit de KV-cache** pour lui. Les tokens suivants qui voudront l'attendre à ces couches trouveront un trou. Les solutions (recalcul paresseux, propagation d'état) rognent le gain — c'est la raison principale pour laquelle l'early exit reste peu déployé en LLM malgré son ancienneté.

### Mixture of Depths — router les tokens à travers la pile

- **MoD** (Raposo et al., 2024) transpose l'idée du [[Mixture of Experts|MoE]] de la largeur vers la profondeur : à chaque couche (ou bloc), un routeur sélectionne les **top-$k$** tokens qui la traversent ; les autres la contournent par le résiduel.
- Différence essentielle avec l'early exit : un token « sauté » à la couche 8 peut **revenir** à la couche 12. Le budget de calcul est fixé à l'avance (le $k$ est statique), donc le coût par lot reste **prévisible** — propriété décisive pour le serving, où l'on ne veut pas de latence à variance libre.
- Prolongement 2025-2026 : **Mixture of Recursions** (MoR) et les variantes à routage appris de la profondeur, qui remplacent le top-$k$ dur par une allocation apprise plus souple.

### Transformers bouclés — dépenser plus que la profondeur

- Au lieu d'empiler $L$ couches distinctes, on **réapplique** un bloc de couches partagées plusieurs fois. Le nombre d'itérations devient un levier de calcul **au moment de l'inférence**, sans changer les poids.
- C'est ce que les autres approches ne permettent pas : un modèle bouclé peut décider de « réfléchir plus » sur une entrée dure, au-delà de son budget nominal. On y greffe naturellement l'early exit (sortie du token quand son entropie chute — cf. Ouro, 2025).
- Le biais inductif est différent : boucler un petit bloc favorise le **raisonnement algorithmique** (appliquer la même règle de façon répétée) plutôt que la mémorisation de motifs profonds. C'est l'argument des architectures HRM / TRM — de petits modèles bouclés qui tiennent tête à de bien plus gros sur des tâches de raisonnement structuré.
- Contrepartie : le travail 2026 sur les *looped language models* montre que boucler **seul** ne passe pas l'échelle — il faut des couches creuses (sparsité) pour que ça tienne.

### Le lien avec le raisonnement

- Il faut distinguer deux échelles d'adaptation, souvent mélangées :
  - **intra-forward** — profondeur variable dans une seule passe (tout ce qui précède) ;
  - **inter-forward** — générer plus de tokens de réflexion, échantillonner plusieurs solutions et voter. C'est le régime des [[Reasoning models|modèles de raisonnement]] et du *test-time compute*.
- Le second a gagné industriellement : il ne demande **aucun changement d'architecture**, juste du post-entraînement et un budget de tokens. Les calculs adaptatifs intra-forward restent en grande partie de la recherche — leur promesse est d'obtenir le même effet sans payer en tokens générés.

## Les maths, simplement

- Coût d'un Transformer standard sur $n$ tokens et $L$ couches : $C = n L c$ où $c$ est le coût d'une couche. Rigide dans les deux facteurs.
- Sous MoD avec une capacité $k$ par couche : $C = k L c$ avec $k < n$. Le taux de sélection $k/n$ (souvent ~12,5 % ou 50 %) est **fixé**, d'où un coût déterministe. À budget de calcul égal, on peut donc financer un modèle **plus profond ou plus large** — c'est là que se trouve le gain de qualité, pas dans l'économie brute.
- Sous early exit avec profondeur $\ell_i$ par token : $C = c \sum_i \ell_i$, espérance $n c \, \mathbb{E}[\ell]$ mais **variance non nulle**. Le p99 de latence, lui, reste gouverné par $L$ : les cas durs paient plein tarif. Un service dimensionné sur son p99 ne gagne donc rien — subtilité qui invalide beaucoup d'annonces d'accélération.
- Modèle bouclé à $T$ itérations d'un bloc de $B$ couches : $C = n T B c$ avec les paramètres de $B$ couches seulement. On **découple le calcul de la taille du modèle** — le pendant exact du MoE, qui découple la taille du calcul, mais dans l'autre sens.

## En pratique

- Rien ici n'est un réglage de déploiement : ce sont des choix d'architecture et d'entraînement. La valeur immédiate du concept est de **savoir lire** une fiche de modèle et anticiper son profil de latence.
- Pour arbitrer un projet réel où le coût d'inférence pose problème, l'ordre d'efficacité est clair : [[Quantization|quantization]] et [[Speculative decoding|décodage spéculatif]] d'abord (gains immédiats, sans réentraînement), [[Routing and cascading|cascade de modèles]] ensuite (un petit modèle traite les cas faciles — c'est du calcul adaptatif au niveau **système**, et ça marche aujourd'hui), architectures adaptatives en dernier.
- Le piège récurrent : une **latence à variance libre**. Un p50 divisé par deux avec un p99 inchangé ne se vend pas en production. Toujours mesurer la queue de distribution.
- Sur GPU, le calcul irrégulier est mal aimé : sauter des couches pour une partie des tokens crée du remplissage et des noyaux moins efficaces. Le gain théorique en FLOP survit rarement intégralement au passage au matériel.

## Approches voisines & alternatives

- [[Mixture of Experts]] — le même geste de sparsité conditionnelle, appliqué à la **largeur** (quels experts) au lieu de la **profondeur** (quelles couches). MoD en est la transposition directe.
- [[Reasoning models]] — l'adaptation de calcul qui a réellement percé, au niveau des tokens générés plutôt que des couches traversées.
- [[Routing and cascading]] — calcul adaptatif au niveau du **système** : escalader du petit modèle vers le gros selon la difficulté. Déployable immédiatement.
- [[Inference optimization]] — le cadre général des leviers de coût d'inférence, où ces techniques viennent en dernier recours.
- [[Transformer architectures]] — l'uniformité de profondeur que ces approches remettent en question.
- [[Speculative decoding]] — orthogonal : accélère le décodage sans toucher au calcul par token.
- [[Scaling laws]] — MoD et le bouclage sont présentés comme des déplacements de la frontière compute ↔ qualité.
- [[Small Language Models]] — approche concurrente : au lieu d'un gros modèle à calcul variable, un petit modèle à calcul fixe.
- [[Pruning]] — réduire le calcul **une fois pour toutes** (statique) au lieu de l'adapter par entrée (dynamique).

## Pour aller plus loin

- Graves (2016) — *Adaptive Computation Time for Recurrent Neural Networks* (l'ancêtre de la famille).
- Schuster et al. (2022) — *Confident Adaptive Language Modeling* (CALM — early exit en génération, et le problème du KV-cache).
- Raposo et al. (2024) — *Mixture-of-Depths: Dynamically allocating compute in transformer-based language models*.
- Bae et al. (2025) — *Mixture-of-Recursions* (profondeur récursive apprise par token).
- *Sparse Layers are Critical to Scaling Looped Language Models* (2026, arXiv 2605.09165) — pourquoi boucler seul ne suffit pas.
