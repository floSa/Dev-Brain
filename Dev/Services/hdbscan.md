---
galaxie: dev
type: service
nom: hdbscan
alias: [HDBSCAN library, scikit-learn-contrib hdbscan]
pitch: "Implémentation de référence de HDBSCAN — clustering par densité hiérarchique qui découvre le nombre de clusters, gère les densités hétérogènes et isole le bruit, avec un seul paramètre intuitif (taille minimale de cluster)."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Scikit-Learn|Scikit-Learn]]"]
remplace_par: []
status: actif
tags: [clustering, unsupervised]
url_docs: https://hdbscan.readthedocs.io/
url_repo: https://github.com/scikit-learn-contrib/hdbscan
---

# hdbscan

## Pourquoi

Implémentation de référence de l'algorithme [[Wiki/Concepts/HDBSCAN|HDBSCAN]] (scikit-learn-contrib), maintenue par les auteurs de la méthode. Clustering par **densité hiérarchique** : explore tous les seuils de densité et extrait les clusters les plus stables, là où DBSCAN fixe un seul `eps`. Découvre le nombre de clusters, gère des densités hétérogènes, étiquette le bruit, et n'expose qu'un paramètre vraiment interprétable — `min_cluster_size`. Fournit en bonus l'arbre condensé, des probabilités d'appartenance et un score d'outlier (GLOSH). API compatible scikit-learn (`fit` / `labels_`).

## Quand l'utiliser

- Clustering exploratoire quand le **nombre de clusters est inconnu** et que les groupes ont des densités différentes.
- En aval d'une réduction de dimension non linéaire (pipeline classique [[Dev/Services/umap-learn|UMAP]] → hdbscan).
- Besoin des extras absents de sklearn : `approximate_predict`, arbre condensé, soft clustering, score d'outlier GLOSH.
- Détection de bruit / outliers en même temps que le clustering.

## Quand NE PAS l'utiliser

- Une version maintenue dans une seule dépendance suffit → `sklearn.cluster.HDBSCAN` de [[Dev/Services/Scikit-Learn|Scikit-Learn]] (depuis la 1.3).
- Clusters convexes de tailles comparables, nombre connu d'avance → [[K-Means]] (plus simple, plus rapide).
- Un seul seuil de densité global suffit → [[DBSCAN]] (moins coûteux en calcul).

## Déploiement & coût

- Bibliothèque Python (`uv add hdbscan`), cœur Cython ; wheels pour Linux/macOS/Windows. Rien à héberger.
- Single-node, en mémoire ; complexité supérieure à DBSCAN (construction de la hiérarchie complète).
- BSD-3-Clause, gratuit.

## Pièges

- `min_samples` est **décalé de 1** entre la lib `hdbscan` et `sklearn.cluster.HDBSCAN` : à paramètres « identiques », les résultats diffèrent.
- Coûteux en mémoire et en temps sur de grands jeux en haute dimension : réduire la dimension avant ([[Dev/Services/umap-learn|UMAP]] / PCA).
- La distance euclidienne perd son sens en très haute dimension : projeter d'abord.
- Le bruit (`label = -1`) n'est pas une classe : prévoir son traitement en aval.

## Alternatives

- [[Dev/Services/Scikit-Learn|Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

## Liens

- Concept implémenté : [[Wiki/Concepts/HDBSCAN|HDBSCAN]] — dans le cadre [[Clustering]], extension de [[DBSCAN]].
- Pipeline fréquent : [[Dev/Services/umap-learn|umap-learn]] (réduction) → hdbscan (clustering).
- Doc : https://hdbscan.readthedocs.io/
