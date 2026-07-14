---
galaxie: wiki
type: concept
nom: K-Means
alias: [K-means, kmeans, K-moyennes, Lloyd, k-means++]
categorie: concept/ml
domaines: [data-sci]
tags: [clustering, unsupervised]
---

# K-Means

## Aperçu

- Méthode de [[Clustering]] par **partition** : répartit les observations en $K$ clusters en minimisant l'inertie intra-classe (somme des carrés des distances aux centres).
- Algorithme simple, rapide, scalable — la baseline du clustering. En contrepartie : $K$ fixé d'avance et clusters supposés sphériques et de taille comparable.

## Concepts clés

### Centres (centroïdes)
- Chaque cluster est résumé par son barycentre $\mu_k$. Un point est affecté au centre le plus proche (affectation dure ; les frontières forment un diagramme de Voronoï).

### Algorithme de Lloyd
- Boucle à deux temps jusqu'à stabilisation : (1) **affecter** chaque point au centre le plus proche ; (2) **recalculer** chaque centre comme moyenne de ses points. Converge vers un minimum **local**.

### Initialisation (k-means++)
- Le résultat dépend des centres initiaux. `k-means++` les tire éloignés les uns des autres → convergence plus rapide et solutions plus stables que l'aléatoire pur. En pratique, plusieurs relances (`n_init`), on garde la meilleure inertie.

### Choix de K
- $K$ n'est pas appris. Heuristiques : coude de l'inertie, score de silhouette, gap statistic.

## Les maths, simplement

- Objectif minimisé : $\displaystyle \min_{C_1,\dots,C_K} \sum_{k=1}^{K} \sum_{x \in C_k} \lVert x - \mu_k \rVert^2$, avec $\mu_k = \frac{1}{|C_k|}\sum_{x \in C_k} x$.
- L'étape d'affectation et l'étape de mise à jour font chacune décroître ce critère → convergence garantie, mais vers un optimum local (d'où les relances).

## En pratique

- **Standardiser** impérativement : K-Means raisonne en distance euclidienne, une variable à forte amplitude écrase les autres.
- Échoue sur clusters allongés, de densités ou tailles très différentes, ou non convexes — la distance au centre ne capture que des blobs ronds.
- Sensible aux **outliers** (ils tirent les centres) ; pas de notion de bruit, tout point est classé.
- `MiniBatchKMeans` pour les gros volumes (mises à jour sur mini-lots, plus rapide, légèrement moins précis).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.cluster.KMeans / MiniBatchKMeans]].

## Approches voisines & alternatives

- [[Clustering]] — le cadre général et les autres familles.
- [[Gaussian Mixture Models (GMM)]] — généralisation probabiliste : K-Means en est le cas limite (covariance sphérique, affectation dure). Gère les clusters ellipsoïdaux et l'affectation souple.
- [[Classification hiérarchique (CAH)]] — quand $K$ n'est pas connu d'avance ou qu'une hiérarchie a du sens.
- [[DBSCAN]] — pour des formes arbitraires et un nombre de clusters découvert, avec gestion du bruit.
- [[k-médoïds (PAM)]] — centre = un point réel (médoïde) au lieu de la moyenne : robuste aux outliers et compatible avec une distance arbitraire (Manhattan, Gower, DTW), au prix d'un coût plus élevé.

## Pour aller plus loin

- Lloyd (1982) — *Least squares quantization in PCM* ; MacQueen (1967) — *Some methods for classification and analysis of multivariate observations*.
- Arthur & Vassilvitskii (2007) — *k-means++: The Advantages of Careful Seeding*.
