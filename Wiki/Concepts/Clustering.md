---
galaxie: wiki
type: concept
nom: Clustering
alias: [Partitionnement, Partitionnement non supervisé, Cluster analysis, Analyse de clusters, Regroupement]
categorie: concept/ml
domaines: [data-sci]
tags: [clustering, unsupervised]
---

# Clustering

## Aperçu

- Famille de méthodes **non supervisées** : regrouper les observations en sous-ensembles (*clusters*) homogènes, sans variable cible ni étiquettes connues.
- Objectif : maximiser la similarité intra-cluster et la séparation inter-cluster, selon une notion de distance choisie. Sert à explorer, segmenter, débruiter, détecter des anomalies.

## Concepts clés

### Distance et similarité
- Tout repose sur une mesure de proximité (euclidienne, cosinus, Manhattan…). Le choix de la distance définit ce qu'est un « groupe ».
- Sensible à l'échelle des variables : standardiser avant, sauf méthode invariante.

### Quatre grandes familles
- **Partition** : découpe en $K$ groupes en optimisant un critère global → [[K-Means]]. Rapide, mais $K$ fixé d'avance et clusters convexes.
- **Hiérarchique** : construit un arbre de fusions/divisions, coupé a posteriori → [[Classification hiérarchique (CAH)]]. Pas de $K$ imposé, lecture par dendrogramme.
- **Densité** : un cluster = une zone dense séparée par du vide → [[DBSCAN]], [[HDBSCAN]]. Formes arbitraires, détection du bruit, $K$ découvert.
- **Probabiliste / modèle** : les données sont un mélange de lois → [[Gaussian Mixture Models (GMM)]]. Affectation souple (probabilités), clusters ellipsoïdaux.

### Affectation dure vs souple
- Dure : chaque point appartient à un seul cluster (K-Means, DBSCAN).
- Souple : chaque point a une probabilité d'appartenance à chaque cluster (GMM).

### Combien de clusters ?
- Question centrale et mal posée (pas de vérité terrain). Heuristiques : coude de l'inertie, score de **silhouette**, gap statistic, BIC/AIC (modèles probabilistes), lecture du dendrogramme.

## Les maths, simplement

- Inertie intra-cluster (à minimiser pour une partition) : $W = \sum_{k=1}^{K} \sum_{x \in C_k} \lVert x - \mu_k \rVert^2$, où $\mu_k$ est le centre du cluster $C_k$. C'est la dispersion résiduelle après regroupement.
- Silhouette d'un point : $s = \dfrac{b - a}{\max(a, b)} \in [-1, 1]$, où $a$ = distance moyenne aux points de son cluster et $b$ = distance moyenne au cluster voisin le plus proche. Proche de 1 = bien classé.

## En pratique

- **Standardiser** les variables avant toute méthode à distance (sinon la variable de plus grande amplitude domine).
- Aucune méthode n'est universelle : forme des clusters, présence de bruit, volume et dimension dictent le choix.
- En grande dimension, les distances se concentrent (*curse of dimensionality*) — réduire d'abord ([[Réduction de dimension]], [[PCA]]) stabilise le clustering.
- Le résultat n'a pas de « vérité » : valider par la silhouette, la stabilité (re-runs, ré-échantillons) et surtout l'interprétabilité métier des groupes.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.cluster]] (KMeans, DBSCAN, AgglomerativeClustering, HDBSCAN), `sklearn.mixture` (GaussianMixture), `scipy.cluster.hierarchy`.

## Approches voisines & alternatives

- [[K-Means]] — partition en $K$ groupes minimisant l'inertie intra-classe ; rapide, baseline.
- [[Classification hiérarchique (CAH)]] — hiérarchie de fusions visualisée par dendrogramme ; pas de $K$ imposé.
- [[DBSCAN]] — clustering par densité ; formes arbitraires et détection du bruit.
- [[HDBSCAN]] — extension hiérarchique de DBSCAN, sans seuil de densité global.
- [[Gaussian Mixture Models (GMM)]] — mélange probabiliste de gaussiennes ; affectation souple.
- [[Mise à l'échelle]] — préalable obligé des méthodes à distance (sinon la variable de plus grande amplitude domine).
- [[Réduction de dimension]] — souvent en amont, pour débruiter avant de classer (cf. [[HCPC]]).

## Pour aller plus loin

- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 14 (Cluster Analysis).
- Documentation scikit-learn — *Clustering* : tableau comparatif des méthodes et de leurs hypothèses.
