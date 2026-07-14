---
galaxie: wiki
type: concept
nom: HDBSCAN
alias: [Hierarchical DBSCAN, Hierarchical Density-Based Spatial Clustering]
categorie: concept/ml
domaines: [data-sci]
tags: [clustering, unsupervised]
---

# HDBSCAN

## Aperçu

- Extension **hiérarchique** de [[DBSCAN]] : au lieu d'un rayon `eps` global, explore tous les seuils de densité et en extrait les clusters les plus **stables**.
- Gère les clusters de **densités différentes** (le talon d'Achille de DBSCAN) et ne demande qu'un paramètre intuitif : la taille minimale d'un cluster.

## Concepts clés

### Pourquoi « hiérarchique »
- DBSCAN fixe un seul `eps`, donc une seule densité de coupure. HDBSCAN construit la hiérarchie complète des clusters à toutes les densités (équivaut à balayer `eps`), puis condense l'arbre et garde les branches stables.

### Distance d'atteignabilité mutuelle
- Repondère les distances pour écarter les points isolés des zones denses (`core distance` = distance au $k$-ième voisin), rendant la hiérarchie robuste au bruit.

### Extraction des clusters stables
- Sur l'arbre condensé, chaque cluster candidat a une **persistance** (durée de vie sur l'axe de densité). On retient ceux qui persistent le plus → pas de seuil de densité global à régler.

### Paramètres
- `min_cluster_size` : plus petit groupe admis comme cluster (le levier principal, interprétable). `min_samples` : conservatisme vis-à-vis du bruit. Les points non retenus restent étiquetés bruit, comme DBSCAN.

## Les maths, simplement

- Distance d'atteignabilité mutuelle : $d_{\text{mreach}}(a,b) = \max\big(\text{core}_k(a),\ \text{core}_k(b),\ d(a,b)\big)$, où $\text{core}_k$ est la distance au $k$-ième voisin. Elle « éloigne » les points en zone peu dense.
- Les clusters sont les composantes du candidat le plus **persistant** dans la hiérarchie construite sur cette distance — sélection par stabilité, sans `eps` fixe.

## En pratique

- À préférer à [[DBSCAN]] dès que les clusters n'ont pas tous la même densité, ou quand régler `eps` est pénible.
- `min_cluster_size` est plus facile à fixer qu'un `eps` : c'est une taille de groupe, pas une échelle de distance.
- Plus coûteux que DBSCAN, mais fournit en bonus une hiérarchie, des scores d'appartenance et un score d'outlier (GLOSH).
- Très utilisé en aval d'une réduction de dimension non linéaire (ex. [[Dev/Services/umap-learn|UMAP]] → HDBSCAN) pour le clustering exploratoire.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.cluster.HDBSCAN]] (depuis la 1.3) ; lib autonome [[Dev/Services/hdbscan|hdbscan]] (scikit-learn-contrib). Attention : `min_samples` décalé de 1 entre les deux implémentations.

## Approches voisines & alternatives

- [[DBSCAN]] — la méthode dont HDBSCAN est l'extension ; plus simple et un peu plus rapide, mais un seul seuil de densité et un `eps` à régler.
- [[Clustering]] — le cadre général et les autres familles.
- [[Classification hiérarchique (CAH)]] — autre méthode hiérarchique, mais fondée sur un linkage géométrique plutôt que sur la densité.

## Pour aller plus loin

- Campello, Moulavi, Sander (2013) — *Density-Based Clustering Based on Hierarchical Density Estimates*.
- McInnes, Healy, Astels (2017) — *hdbscan: Hierarchical density based clustering* (JOSS), implémentation de référence.
