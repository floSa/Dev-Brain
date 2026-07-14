---
galaxie: wiki
type: concept
nom: k-médoïds (PAM)
alias: [k-medoids, PAM, Partitioning Around Medoids, k-médoïdes, CLARA]
categorie: concept/ml
domaines: [data-sci]
tags: [unsupervised, clustering]
---

# k-médoïds (PAM)

## Aperçu

- Variante de [[K-Means]] où le centre de chaque cluster n'est pas une moyenne mais un **médoïde** : un **point réel** du jeu de données, celui qui minimise la somme des dissimilarités aux autres points du cluster.
- Deux conséquences directes : **robustesse aux outliers** (un point réel ne « dérape » pas comme un barycentre) et acceptation d'une **distance/dissimilarité quelconque** (Manhattan, Gower, DTW…), pas seulement la distance euclidienne. Contrepartie : coût de calcul plus élevé.

## Concepts clés

### Médoïde vs centroïde
- Le **centroïde** de K-Means est un point virtuel (la moyenne, possiblement hors nuage). Le **médoïde** est l'observation existante la plus « centrale » du cluster. Il reste donc interprétable comme un représentant concret.

### PAM (Partitioning Around Medoids)
- L'algorithme de référence. Phase **BUILD** : choisir $k$ médoïdes initiaux. Phase **SWAP** : tester l'échange d'un médoïde avec un point non-médoïde, garder l'échange qui fait le plus baisser le coût total ; itérer jusqu'à stabilisation. Optimum **local**, comme K-Means.

### Distance arbitraire
- Comme seul compte un tableau de dissimilarités (et non des coordonnées), PAM s'applique à des données **mixtes** (Gower), des **séries temporelles** (DTW), des chaînes (distance d'édition) — tout ce qui n'a pas de « moyenne » bien définie.

### CLARA — passage à l'échelle
- PAM ne tient pas sur de gros $n$. **CLARA** applique PAM sur plusieurs **échantillons** du jeu et retient le meilleur jeu de médoïdes ; **CLARANS** explore le voisinage de façon randomisée. Variantes modernes : **FastPAM** (accélère la phase SWAP).

## Les maths, simplement

- Objectif minimisé : $\displaystyle \sum_{k=1}^{K}\ \sum_{x \in C_k} d(x, m_k)$, où $m_k$ est le **médoïde** du cluster $C_k$ et $m_k \in C_k$ (point réel), et $d$ une dissimilarité quelconque.
- Différence clé avec K-Means : K-Means minimise $\sum \lVert x-\mu_k\rVert^2$ avec $\mu_k$ la moyenne (sensible aux extrêmes via le carré) ; ici on minimise une somme de distances à un point réel → moins sensible aux outliers et libre du choix de $d$.
- Coût : une itération de PAM est en $O\!\big(k\,(n-k)^2\big)$ (chaque swap candidat réévalue le nuage), bien plus lourd que K-Means.

## En pratique

- **Standardiser** comme pour K-Means quand la distance le requiert (L2, Manhattan).
- $K$ reste fixé d'avance ; mêmes heuristiques de choix qu'en K-Means (silhouette…), cf. [[Clustering evaluation]].
- Privilégier k-médoïds quand : présence d'**outliers**, distance **non euclidienne** imposée par les données, ou besoin d'un **représentant réel** par cluster. Sur gros volumes, passer à CLARA / FastPAM.
- Outils : `sklearn-extra` (`KMedoids`), ou implémentations PAM dédiées (`kmedoids`, `pyclustering`).

## Approches voisines & alternatives

- [[K-Means]] — l'ancêtre par centroïdes : plus rapide et scalable, mais L2 seulement et sensible aux outliers.
- [[Clustering]] — le cadre général et les autres familles (hiérarchique, densité, mélanges).
- [[Clustering evaluation]] — choisir $K$ et juger la partition (silhouette, etc.), indépendamment de l'algorithme.

## Pour aller plus loin

- Kaufman & Rousseeuw (1990) — *Finding Groups in Data* (PAM, CLARA).
- Schubert & Rousseeuw (2019) — *Faster k-Medoids Clustering* (FastPAM).
