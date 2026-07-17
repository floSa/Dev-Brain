---
galaxie: wiki
type: concept
nom: ICA
alias: [Independent Component Analysis, Analyse en composantes indépendantes, ACI, FastICA, Séparation aveugle de sources, Blind source separation]
categorie: concept/ml
domaines: [data-sci]
tags: [dimensionality-reduction, factor-analysis, unsupervised]
---

# ICA

## Aperçu

- Décomposition qui sépare un signal mélangé en **sources statistiquement indépendantes**. Le problème canonique est celui du *cocktail party* : plusieurs micros captent plusieurs voix mélangées, l'ICA reconstitue chaque voix sans rien savoir des locuteurs ni de la salle.
- Sa différence avec la [[PCA]] tient en un mot : la PCA cherche des directions **décorrélées et orthogonales** (ordre 2), l'ICA cherche des directions **indépendantes** — une exigence bien plus forte, qui mobilise les moments d'ordre supérieur.

## Concepts clés

### Décorrélé ≠ indépendant
- Le point qui fonde toute la méthode. La décorrélation ne regarde que la covariance : $\mathbb{E}[xy] = \mathbb{E}[x]\mathbb{E}[y]$. L'indépendance exige que la loi jointe se factorise entièrement : $p(x, y) = p(x)\,p(y)$.
- Deux variables peuvent être parfaitement décorrélées et totalement dépendantes ($y = x^2$ avec $x$ centrée symétrique en est l'exemple type). La PCA se contente du premier, l'ICA vise le second.

### Pourquoi la non-gaussianité est le moteur
- Résultat central, et contre-intuitif : **l'ICA ne fonctionne que si les sources ne sont pas gaussiennes**. Au plus une source gaussienne est tolérée.
- La raison : pour des variables gaussiennes, décorrélation **équivaut** à indépendance. Une fois blanchies, toutes les rotations sont équivalentes et rien ne permet de choisir — le problème n'a pas de solution unique.
- D'où le retournement qui donne l'algorithme : **maximiser la non-gaussianité** des projections revient à trouver les sources. Par le [[Théorème central limite|théorème central limite]], un mélange de sources est *plus* gaussien que chaque source prise à part — donc démélanger, c'est s'éloigner de la gaussienne.

### Ce que l'ICA ne peut pas savoir
- Deux indéterminations structurelles, à connaître avant de sur-interpréter un résultat :
  - **L'ordre** des composantes est arbitraire — il n'y a pas de « première composante » comme en PCA, aucune variance expliquée pour les classer.
  - **L'échelle et le signe** sont indéterminés : multiplier une source par 2 et diviser sa colonne de mélange par 2 donne exactement le même mélange.

### Le blanchiment, étape obligée
- On commence toujours par blanchir les données — c'est-à-dire une [[PCA]] suivie d'une normalisation des variances. Le problème se réduit alors à trouver une **rotation**.
- Autrement dit, l'ICA ne remplace pas la PCA : elle **la prolonge**. PCA pour décorréler, rotation pour rendre indépendant.

### Les hyperparamètres

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `n_components` | Nombre de sources cherchées | Pas de critère objectif (aucune variance expliquée à lire). Le fixer par connaissance du problème |
| `fun` | Mesure de non-gaussianité : `logcosh`, `exp`, `cube` | `logcosh` par défaut, robuste. `exp` si sources très super-gaussiennes ; `cube` sensible aux outliers |
| `whiten` | Blanchiment préalable | À laisser actif — c'est un prérequis, pas une option |
| `max_iter` / `tol` | Convergence | À monter si l'algorithme ne converge pas (avertissement fréquent) |
| `random_state` | Graine | **À fixer** : FastICA part d'une initialisation aléatoire, les résultats varient d'un run à l'autre |

## Les maths, simplement

- Le modèle : $x = A s$, où $s$ sont les sources indépendantes inconnues, $A$ la matrice de mélange inconnue, $x$ ce qu'on observe. On cherche $W \approx A^{-1}$ telle que $\hat{s} = W x$ ait des composantes indépendantes.
- **Négentropie** — la mesure de non-gaussianité : $J(y) = H(y_{\text{gauss}}) - H(y)$, où $H$ est l'[[Shannon entropy|entropie]] et $y_{\text{gauss}}$ une gaussienne de même variance. Elle est nulle si et seulement si $y$ est gaussienne, positive sinon. La gaussienne est la loi d'entropie **maximale** à variance fixée — donc s'en éloigner, c'est baisser l'entropie.
- En pratique la négentropie est incalculable ; FastICA l'approche par $J(y) \approx \big(\mathbb{E}[G(y)] - \mathbb{E}[G(\nu)]\big)^2$, avec $G$ une fonction non quadratique — d'où le paramètre `fun` (`logcosh` : $G(u) = \frac{1}{a}\log\cosh(au)$).
- Formulation équivalente par l'[[Mutual information|information mutuelle]] : minimiser $I(\hat{s}_1, …, \hat{s}_k)$, qui est nulle exactement quand les composantes sont indépendantes. Maximiser la non-gaussianité et minimiser l'information mutuelle sont le même problème.

## En pratique

- **Ne pas l'utiliser pour réduire la dimension.** Sans ordre ni variance expliquée, on ne sait pas quoi garder. Pour réduire, [[PCA]]. L'ICA sert à **séparer**, pas à compresser.
- **Fixer `random_state`** : FastICA est stochastique. Sans graine, deux exécutions donnent des composantes différentes — et l'utilisateur croit à un bug.
- **Terrain naturel : les signaux.** EEG/MEG (retirer les artefacts oculaires est *l'*application canonique), audio, capteurs. Partout où l'hypothèse « mélange linéaire de sources » a un sens physique.
- **Vérifier la non-gaussianité des sources supposées** avant de se lancer. Si elles sont gaussiennes, la méthode ne peut pas fonctionner — ce n'est pas un problème de réglage.
- **Sensible aux outliers**, surtout avec `fun='cube'` (moment d'ordre 4). Nettoyer en amont ([[Détection d'outliers univariée]]).
- **Usage en interprétabilité** : [[Dev/Services/interpreto|interpreto]] propose l'ICA comme méthode de dictionnaire sur les activations, à côté des [[Sparse autoencoders|SAE]] et de la [[NMF]]. Linéaire, instantanée, sans entraînement — la baseline honnête avant de sortir un SAE.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.decomposition.FastICA]] ; [[Dev/Services/scipy.signal|scipy.signal]] pour le prétraitement.

## Approches voisines & alternatives

- [[PCA]] — l'étape préalable (blanchiment) et le contraste central : décorrélation (ordre 2) contre indépendance (ordres supérieurs).
- [[NMF]] — l'autre décomposition « à part » : contrainte de positivité au lieu d'indépendance, et parties additives plutôt que sources.
- [[Réduction de dimension]] — le chapeau ; l'ICA y figure comme le membre qui ne réduit pas vraiment.
- [[Sparse autoencoders]] — le pendant non linéaire et appris, pour démêler des activations.
- [[Mutual information]] — la formulation équivalente du critère.
- [[Shannon entropy]] — d'où vient la négentropie.
- [[Théorème central limite]] — pourquoi un mélange est plus gaussien que ses sources ; le fondement du critère.
- [[Traitement du signal]] — son domaine d'application principal.
- [[Matrix decompositions]] — la famille algébrique.

## Pour aller plus loin

- Hyvärinen & Oja (2000) — *Independent Component Analysis: Algorithms and Applications* : la synthèse de référence, très lisible.
- Comon (1994) — *Independent Component Analysis, a new concept?* : l'article fondateur.
- Documentation scikit-learn — *FastICA on 2D point clouds* et *Blind source separation*, où le contraste avec la PCA est visuel.
