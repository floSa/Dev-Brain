---
galaxie: wiki
type: concept
nom: PGA
alias: [Principal Geodesic Analysis, Analyse géodésique principale]
categorie: concept/stats
domaines: [data-sci]
tags: [dimensionality-reduction, manifold, unsupervised]
---

# PGA

## Aperçu

- Principal Geodesic Analysis : généralisation de la [[PCA]] aux données vivant sur une **variété riemannienne** (formes, tenseurs de diffusion, matrices SPD, rotations).
- Remplace droites et moyennes euclidiennes par géodésiques et moyenne de Fréchet.

## Concepts clés

### Pourquoi pas la PCA standard
- Sur une variété courbe, les combinaisons linéaires sortent de l'espace ; une « moyenne » euclidienne n'est pas un point valide.
- PGA travaille intrinsèquement avec la géométrie de la variété.

### Géodésiques principales
- Une géodésique = plus court chemin local, l'analogue de la droite.
- PGA cherche les géodésiques passant par la moyenne de Fréchet qui captent le plus de variance.

### Linéarisation dans l'espace tangent
- En pratique : projeter les points dans l'espace tangent à la moyenne via le logarithme riemannien $\mathrm{Log}$, y faire une PCA, puis ramener sur la variété via l'exponentielle $\mathrm{Exp}$.

## Les maths, simplement

- Moyenne de Fréchet : $\mu = \arg\min_p \sum_i d(p, x_i)^2$, avec $d$ la distance géodésique.
- Espace tangent en $\mu$ : $v_i = \mathrm{Log}_\mu(x_i)$ ; PCA sur les $v_i$ ; reconstruction par $\mathrm{Exp}_\mu(\cdot)$.
- Exact à courbure nulle ; sinon approximation tangente — d'où des variantes « exactes » (geodesic PCA).

## En pratique

- Domaines : analyse de formes (anatomie), imagerie (tenseurs DTI), vision, robotique (groupes de Lie).
- Suppose de connaître la variété et ses opérations $\mathrm{Exp} / \mathrm{Log}$.
- Le seul du cluster hors tradition « analyse de données » française ; absent de FactoMineR / prince.
- Outils : `geomstats`, `pymanopt` (Python).

## Approches voisines & alternatives

- [[Réduction de dimension]] — la famille ; PGA en est la branche non euclidienne.
- [[PCA]] — le cas plat dont PGA est l'extension.
- t-SNE, UMAP, Isomap, autoencodeurs — autres réductions non linéaires (apprises, non riemanniennes) hors brain.

## Pour aller plus loin

- Fletcher, Lu, Pizer, Joshi (2004), *Principal Geodesic Analysis for the Study of Nonlinear Statistics of Shape*, IEEE TMI.
