---
galaxie: wiki
type: concept
nom: DBSCAN
alias: [Density-Based Spatial Clustering, Density-Based Spatial Clustering of Applications with Noise]
categorie: concept/ml
domaines: [data-sci]
tags: [clustering, unsupervised]
---

# DBSCAN

## Aperçu

- Méthode de [[Clustering]] par **densité** : un cluster est une zone dense de points séparée des autres par des régions clairsemées. Découvre des clusters de **formes arbitraires** et isole le **bruit**.
- Deux atouts majeurs : le nombre de clusters n'est pas fixé d'avance, et les points isolés sont étiquetés « bruit » plutôt que forcés dans un groupe.

## Concepts clés

### Deux paramètres
- `eps` ($\varepsilon$) : rayon de voisinage. `min_samples` : nombre minimal de points dans ce rayon pour qualifier une zone de dense.

### Trois types de points
- **Cœur** (*core*) : a au moins `min_samples` voisins dans son rayon `eps`.
- **Bordure** (*border*) : dans le voisinage d'un point cœur, mais pas cœur lui-même.
- **Bruit** (*noise*) : ni l'un ni l'autre — non assigné.

### Propagation par densité
- Les clusters croissent en reliant les points cœur dont les voisinages se chevauchent (densité-atteignabilité). Pas de centroïde, pas d'hypothèse de forme convexe.

## Les maths, simplement

- Point cœur : $\lvert \{ y : \lVert x - y \rVert \le \varepsilon \} \rvert \ge \text{min\_samples}$.
- Un cluster = composante connexe de la relation « densité-atteignable » entre points cœur ; les bordures rejoignent le cluster du cœur qui les atteint, le reste est du bruit. Aucun $K$ à fournir.

## En pratique

- Le couple (`eps`, `min_samples`) est **le** point dur : `eps` trop petit → tout devient du bruit ; trop grand → les clusters fusionnent. Le graphe des distances au $k$-ième voisin (k-distance plot) aide à régler `eps`.
- **Échoue quand la densité varie** fortement d'un cluster à l'autre : un seul `eps` global ne peut convenir à tous → c'est précisément ce que corrige [[HDBSCAN]].
- Souffre de la grande dimension (les distances se concentrent) — réduire d'abord.
- Robuste aux outliers (capturés comme bruit), quasi déterministe (pas de relance aléatoire).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.cluster.DBSCAN]].

## Approches voisines & alternatives

- [[Clustering]] — le cadre général et les autres familles.
- [[HDBSCAN]] — extension hiérarchique : fait varier `eps` et gère les densités hétérogènes, au prix d'un peu plus de calcul.
- [[K-Means]] — plus rapide et scalable, mais clusters convexes, $K$ imposé et aucun bruit isolé.
- [[Classification hiérarchique (CAH)]] — autre approche sans $K$ imposé, mais géométrique (linkage) plutôt que par densité.

## Pour aller plus loin

- Ester, Kriegel, Sander, Xu (1996) — *A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise* (DBSCAN), prix « test of time » SIGKDD 2014.
