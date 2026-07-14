---
galaxie: wiki
type: concept
nom: Manifold learning
alias: [manifold learning, apprentissage de variété, Isomap, LLE, Locally Linear Embedding, Kernel PCA, Laplacian Eigenmaps, spectral embedding]
categorie: concept/stats
domaines: [data-sci]
tags: [dimensionality-reduction, manifold, unsupervised]
---

# Manifold learning

## Aperçu

- Famille de méthodes de **réduction de dimension non linéaire** qui supposent que les données vivent sur une **variété** (manifold) courbe de faible dimension plongée dans l'espace ambiant.
- Objectif : **déplier** cette variété là où les méthodes linéaires ([[PCA]]) échouent — branche non linéaire de la [[Réduction de dimension]].

## Concepts clés

### Hypothèse de variété
- Les données à $p$ dimensions occupent en réalité une surface de dimension $d \ll p$ (exemple canonique : le *rouleau suisse*).
- La distance euclidienne ambiante trompe ; il faut préserver la **géométrie locale** ou les distances **le long** de la variété.

### Isomap
- Construit un graphe de voisinage, calcule les **distances géodésiques** (plus courts chemins sur le graphe), puis applique un MDS classique. Préserve les distances mesurées *sur* la variété.

### LLE — Locally Linear Embedding
- Reconstruit chaque point comme **combinaison linéaire de ses voisins**, puis cherche un plongement basse dimension qui conserve ces poids. Purement local, sans distances globales.

### Kernel PCA
- [[PCA]] dans un espace de variables induit par un **noyau** (RBF, polynomial) : capture des structures non linéaires via le *kernel trick*, sans expliciter la transformation. Sait projeter de nouveaux points (`transform`).

### Laplacian Eigenmaps / spectral embedding
- Vecteurs propres du **Laplacien** du graphe de voisinage ; préserve la proximité locale.

### Lien avec t-SNE / UMAP
- [[t-SNE and UMAP]] sont aussi des méthodes manifold, mais orientées **visualisation** ; Isomap / LLE / Kernel PCA visent en plus des coordonnées exploitables en aval (features, pipeline).

## Les maths, simplement

- Hypothèse : données $\approx f(z)$ avec $z \in \mathbb{R}^d$, $d \ll p$, $f$ lisse.
- **Isomap** remplace la distance euclidienne par la distance géodésique (approchée par plus courts chemins), puis diagonalise la matrice de distances (MDS).
- **Kernel PCA** diagonalise la matrice de Gram centrée $K_{ij} = k(x_i, x_j)$ au lieu de la covariance — la PCA appliquée dans l'espace du noyau.

## En pratique

- Sensibles au **nombre de voisins** (`n_neighbors`) et au bruit ; standardiser, et réduire d'abord par [[PCA]] sur gros volumes (coûteux).
- Kernel PCA pour des **features non linéaires** en pipeline (projette de nouveaux points) ; Isomap / LLE moins naturellement transposables.
- Pour seulement **visualiser** → [[t-SNE and UMAP]].
- Outils : [[Dev/Services/Scikit-Learn|sklearn.manifold]] (`Isomap`, `LocallyLinearEmbedding`, `SpectralEmbedding`) et `sklearn.decomposition.KernelPCA`.

## Approches voisines & alternatives

- [[Réduction de dimension]] — la page chapeau ; le manifold learning en est la branche non linéaire.
- [[PCA]] — le socle linéaire dont Kernel PCA est l'extension à noyau.
- [[t-SNE and UMAP]] — méthodes manifold spécialisées dans la visualisation 2-3D.
- [[PGA]] — composantes principales sur variété **riemannienne** (géométrie connue d'avance, vs apprise ici).

## Pour aller plus loin

- Tenenbaum, de Silva, Langford (2000) — *A Global Geometric Framework for Nonlinear Dimensionality Reduction* (Isomap).
- Roweis & Saul (2000) — *Nonlinear Dimensionality Reduction by Locally Linear Embedding*.
- Schölkopf, Smola, Müller (1998) — *Kernel PCA*.
