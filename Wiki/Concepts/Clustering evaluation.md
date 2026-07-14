---
galaxie: wiki
type: concept
nom: Clustering evaluation
alias: [Évaluation du clustering, évaluation de clustering, silhouette, indice de silhouette, ARI, Adjusted Rand Index, NMI, AMI, Davies-Bouldin, Calinski-Harabasz, DBCV]
categorie: concept/ml
domaines: [data-sci]
tags: [model-evaluation, clustering, unsupervised]
---

# Clustering evaluation

## Aperçu

- Mesurer la qualité d'un partitionnement sans cible : problème mal posé, car il n'existe pas de vérité terrain en non supervisé.
- Deux familles : indices **internes** (cohésion/séparation calculées sur les seules données) et indices **externes** (comparaison à des étiquettes de référence, quand on en dispose).

## Concepts clés

### Indices internes
- **Silhouette** $\in[-1,1]$ : cohésion vs séparation par point, moyennée. **Davies-Bouldin** (plus bas = mieux) et **Calinski-Harabasz** (ratio dispersion inter/intra, plus haut = mieux) complètent. Servent aussi à choisir le nombre de clusters.

### Indices externes
- Comparent la partition à un étiquetage connu. **ARI** (Rand ajusté du hasard, $\in[-1,1]$), **NMI/AMI** (information mutuelle normalisée), homogénéité / complétude / V-measure. Tous corrigés ou normalisés pour être interprétables.

### Choisir le nombre de clusters
- Balayer $K$ et lire silhouette, coude de l'inertie, gap statistic, ou BIC pour les modèles probabilistes ([[Gaussian Mixture Models (GMM)]]).

### Stabilité
- Re-clusteriser sur des ré-échantillons : une partition robuste varie peu. Complément utile aux indices ponctuels.

## Les maths, simplement

- Silhouette d'un point : $s=\dfrac{b-a}{\max(a,b)}$, où $a$ = distance moyenne intra-cluster et $b$ = distance moyenne au cluster voisin le plus proche.
- $\text{ARI}=\dfrac{\text{RI}-\mathbb{E}[\text{RI}]}{\max(\text{RI})-\mathbb{E}[\text{RI}]}$ : indice de Rand corrigé du hasard (0 = hasard, 1 = partitions identiques).
- Calinski-Harabasz $=\dfrac{\operatorname{tr}(B_k)}{\operatorname{tr}(W_k)}\cdot\dfrac{n-k}{k-1}$ (dispersion inter-clusters sur intra-clusters).

## En pratique

- Sans étiquettes : indices internes + stabilité + **interprétabilité métier** des groupes, qui reste le juge final.
- Avec étiquettes de référence : préférer ARI ou AMI (corrigés du hasard) à un Rand brut ou à une exactitude — insensibles à la permutation des labels.
- La silhouette favorise les clusters convexes/sphériques : trompeuse pour [[DBSCAN]] / [[HDBSCAN]] (densité, formes arbitraires) → utiliser plutôt DBCV.
- Évaluer dans l'espace où le clustering a un sens (après [[Réduction de dimension]] si la grande dimension écrase les distances).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.metrics — silhouette_score, davies_bouldin_score, calinski_harabasz_score, adjusted_rand_score, adjusted_mutual_info_score]].

## Approches voisines & alternatives

- [[Clustering]] — la page chapeau ; celle-ci en est le volet évaluation.
- [[K-Means]], [[Classification hiérarchique (CAH)]], [[DBSCAN]], [[HDBSCAN]], [[Gaussian Mixture Models (GMM)]] — méthodes dont on mesure ici la qualité.
- [[Validation croisée]] — la stabilité par ré-échantillonnage en est l'analogue non supervisé.

## Pour aller plus loin

- Rousseeuw (1987) — *Silhouettes: a graphical aid to the interpretation and validation of cluster analysis*.
- Hubert & Arabie (1985) — *Comparing partitions* (Adjusted Rand Index).
- Moulavi et al. (2014) — *Density-Based Clustering Validation* (DBCV).
