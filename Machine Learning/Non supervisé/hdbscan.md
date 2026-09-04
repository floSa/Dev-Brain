---
role: brique
nom: hdbscan
alias: [HDBSCAN library, scikit-learn-contrib hdbscan]
pitch: "Implémentation de référence de HDBSCAN — clustering par densité hiérarchique qui découvre le nombre de clusters, gère les densités hétérogènes et isole le bruit, avec un seul paramètre intuitif (taille minimale de cluster)."
categorie: ml/non-supervise
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Scikit-Learn]]"]
complements: ["[[umap-learn]]"]
tags: [clustering, unsupervised]
url_docs: https://hdbscan.readthedocs.io/
url_repo: https://github.com/scikit-learn-contrib/hdbscan
---

# hdbscan

<!-- AUTO:BANDEAU:START -->
> Implémentation de référence de HDBSCAN — clustering par densité hiérarchique qui découvre le nombre de clusters, gère les densités hétérogènes et isole le bruit, avec un seul paramètre intuitif (taille minimale de cluster).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation de référence de l'algorithme HDBSCAN, sous scikit-learn-contrib et maintenue
par les auteurs de la méthode. Clustering par **densité hiérarchique** : elle explore tous les
seuils de densité et extrait les clusters les plus stables, là où DBSCAN en fixe un seul,
`eps`. Elle découvre le nombre de clusters, gère des densités hétérogènes, étiquette le bruit
et n'expose qu'un paramètre vraiment interprétable, `min_cluster_size`. En prime : l'arbre
condensé, des probabilités d'appartenance et un score d'outlier (GLOSH). Le bruit sort en
`label = -1` — ce n'est pas une classe, et son traitement en aval est à prévoir.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Clustering exploratoire quand le nombre de clusters est inconnu et que les groupes ont des densités différentes | `min_samples` est décalé de 1 entre la lib `hdbscan` et `sklearn.cluster.HDBSCAN` : à paramètres « identiques », les résultats diffèrent |
| En aval d'une réduction de dimension non linéaire, dans le pipeline UMAP → HDBSCAN | Coûteux en mémoire et en temps sur de grands jeux en haute dimension, la hiérarchie complète étant construite |
| Extras absents de scikit-learn : `approximate_predict`, arbre condensé, soft clustering, score GLOSH | Une version maintenue dans une seule dépendance suffit → `sklearn.cluster.HDBSCAN` de [[Scikit-Learn]], depuis la 1.3 |
| Détecter le bruit et les outliers en même temps que les clusters | Clusters convexes de tailles comparables, nombre connu d'avance → [[K-Means]] ; un seul seuil de densité global suffit → [[DBSCAN]] |

## Mise en œuvre

- Installation — `uv add hdbscan` ; cœur Cython, wheels Linux, macOS et Windows
- Point d'entrée — l'API scikit-learn : `fit`, puis `labels_`, `probabilities_` et `outlier_scores_`
- Prérequis — NumPy et scikit-learn ; en très haute dimension, une réduction préalable, la distance euclidienne y perdant son sens
- Exécution — single-node, en mémoire ; rien à héberger
- Coût — BSD-3-Clause, gratuit

## Écosystème

### Alternatives

- [[Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

### Compléments

- [[umap-learn]] — Réduction de dimension non linéaire par apprentissage de variété (UMAP) — projette en 2-3D pour la visualisation ou en k dimensions pour le pré-traitement, en préservant mieux la structure globale que t-SNE et bien plus vite. — la réduction de dimension en amont du pipeline UMAP → HDBSCAN

## Ressources

- Documentation — https://hdbscan.readthedocs.io/
- Dépôt — https://github.com/scikit-learn-contrib/hdbscan

## Voir aussi

- [[Clustering hiérarchique par densité]] — la notion implémentée
- [[Clustering]] — le cadre
- [[Non supervisé]] — le hub du dossier ; hdbscan n'entre dans aucune des deux vues de comparatif, filtrées sur la détection d'anomalies et la réduction de dimension
