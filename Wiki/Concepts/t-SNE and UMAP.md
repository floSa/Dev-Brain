---
galaxie: wiki
type: concept
nom: t-SNE and UMAP
alias: [t-SNE, UMAP, visualisation haute dimension]
categorie: concept/ml
domaines: [data-sci]
tags: [dimensionality-reduction, manifold, unsupervised]
---

# t-SNE and UMAP

## Aperçu

- Deux méthodes de **réduction de dimension non linéaire**, surtout employées pour **visualiser** en 2-3D des données à haute dimension (embeddings, single-cell, images).
- Préservent le **voisinage local** (qui est proche de qui) plutôt que les distances globales — branche manifold de la [[Réduction de dimension]].

## Concepts clés

### Idée commune
- Modéliser la proximité entre points en haute dimension, puis chercher un agencement en basse dimension qui reproduit ces proximités.

### t-SNE
- Convertit les distances en probabilités de voisinage (gaussienne en haute dimension, **loi de Student** en basse dimension pour éviter l'entassement).
- Hyperparamètre clé : la **perplexity** (~5–50), taille effective du voisinage. Lent, surtout local, sans `transform` natif pour de nouveaux points.

### UMAP
- Fondé sur la topologie des variétés : un graphe de voisinage flou optimisé en basse dimension.
- `n_neighbors` (équilibre local ↔ global), `min_dist` (compacité). Plus **rapide**, préserve mieux la **structure globale**, sait projeter de nouveaux points. Implémentation : [[Dev/Services/umap-learn|umap-learn]].

### Lire une projection
- Les **tailles d'amas** et les **distances entre amas** ne sont **pas** quantitativement fiables.
- Des amas peuvent apparaître ou disparaître selon les réglages : tester plusieurs valeurs, ne pas conclure d'un seul run.

## Les maths, simplement

- t-SNE minimise la divergence de **Kullback-Leibler** entre la distribution des voisinages en haute dimension ($p_{ij}$) et en basse dimension ($q_{ij}$) : $\mathrm{KL}(P\,\Vert\,Q) = \sum_{ij} p_{ij}\log\dfrac{p_{ij}}{q_{ij}}$.
- La queue lourde de la loi de Student en basse dimension ($q_{ij} \propto (1+\lVert y_i - y_j\rVert^2)^{-1}$) laisse de la place aux points éloignés → amas mieux séparés.
- UMAP optimise une entropie croisée entre graphes flous (forces d'attraction / répulsion, descente de gradient stochastique).

## En pratique

- Réduire d'abord par [[PCA]] (ex. 50 dimensions) avant t-SNE : plus rapide et moins bruité.
- UMAP par défaut quand on veut de la vitesse, la structure globale, ou projeter de nouveaux points ; t-SNE reste une référence visuelle.
- Excellents **avant un clustering** par densité ([[HDBSCAN]]) ou pour inspecter des [[embeddings]] ; mauvais choix si l'on veut des axes interprétables ou des distances chiffrées → [[PCA]] et méthodes factorielles.
- Stochastiques : fixer `random_state` ; standardiser les entrées.

## Approches voisines & alternatives

- [[Réduction de dimension]] — la page chapeau ; t-SNE et UMAP en sont la branche non linéaire.
- [[Manifold learning]] — le sous-chapeau manifold (Isomap, LLE, Kernel PCA) ; t-SNE/UMAP en sont les membres orientés visualisation.
- [[PCA]] — l'alternative linéaire, interprétable et à variance chiffrée ; souvent un pré-traitement de t-SNE.
- [[Dev/Services/umap-learn|umap-learn]] — l'implémentation de référence d'UMAP.
- [[Dev/Services/PaCMAP|PaCMAP]] — variante récente qui préserve mieux la structure globale (paires mid-near), alternative à t-SNE et UMAP.
- [[embeddings]] — la donnée que l'on projette le plus souvent.
- [[HDBSCAN]] — clustering fréquent en aval de la projection.

## Pour aller plus loin

- van der Maaten & Hinton (2008) — *Visualizing Data using t-SNE*.
- McInnes, Healy, Melville (2018) — *UMAP: Uniform Manifold Approximation and Projection*.
- *How to Use t-SNE Effectively* (Distill, 2016).
