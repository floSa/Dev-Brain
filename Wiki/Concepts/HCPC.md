---
galaxie: wiki
type: concept
nom: HCPC
alias: [Classification hiérarchique sur composantes principales, Hierarchical Clustering on Principal Components]
categorie: concept/stats
domaines: [data-sci]
tags: [clustering, factor-analysis, unsupervised]
---

# HCPC

## Aperçu

- Hierarchical Clustering on Principal Components : enchaîne une méthode factorielle puis une classification des individus sur les composantes retenues.
- Combine projection (débruitage), classification ascendante hiérarchique (CAH) et consolidation k-means.

## Concepts clés

### Pourquoi classer sur les composantes
- Garder les premiers axes débruite et stabilise le clustering (les derniers axes = bruit).
- Distances calculées dans un espace réduit et décorrélé.

### Les trois étapes
- Méthode factorielle ([[PCA]], [[MCA]], [[FAMD]], [[MFA]]) → coordonnées des individus.
- [[Classification hiérarchique (CAH)|CAH]] (souvent critère de Ward) sur ces coordonnées → arbre (dendrogramme).
- Découpe au saut d'inertie le plus net, puis consolidation par k-means.

### Description automatique des classes
- Chaque classe est caractérisée par les variables (quanti : valeurs-tests ; quali : modalités sur-représentées) et par des individus parangons / spécifiques.

## Les maths, simplement

- Ward minimise la perte d'inertie inter-classe à chaque fusion : agréger les deux classes dont la fusion augmente le moins l'inertie intra.
- Niveau de coupe choisi là où le gain d'inertie inter marque un saut (plus forte décroissance relative).
- Le k-means final réaffecte les individus mal classés autour des barycentres.

## En pratique

- Pipeline de référence de l'analyse exploratoire « à la française » (FactoMineR).
- Garder assez d'axes pour l'information utile, pas trop pour éviter le bruit.
- Pur quantitatif sans réduction → un k-means direct suffit parfois.
- Outils : `FactoMineR::HCPC` (R) ; en Python, enchaîner `prince` / `sklearn` + `scipy.cluster.hierarchy` + `KMeans`.

## Approches voisines & alternatives

- [[Réduction de dimension]] — la famille en amont.
- [[PCA]], [[MCA]], [[FAMD]], [[MFA]] — les méthodes factorielles qui alimentent HCPC.
- [[Classification hiérarchique (CAH)]] — la brique de clustering au cœur de HCPC, ici appliquée aux composantes.
- [[Clustering]] — le cadre général ; alternatives directes : [[K-Means|k-means]] seul, [[DBSCAN]], [[Gaussian Mixture Models (GMM)|mélanges gaussiens]].

## Pour aller plus loin

- Husson, Josse, Pagès — *Principal component methods – hierarchical clustering – partitional clustering* (FactoMineR).
