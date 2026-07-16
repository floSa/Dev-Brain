---
galaxie: wiki
type: concept
nom: Apprentissage non supervisé
alias: [Unsupervised learning, Apprentissage non supervise, Méthodes non supervisées]
categorie: concept/ml
domaines: [data-sci]
tags: [unsupervised, clustering]
---

# Apprentissage non supervisé

## Aperçu

- Famille de méthodes qui cherchent une **structure dans les données sans variable cible** : aucun $y$, aucune bonne réponse connue. On ne prédit pas, on organise.
- Trois usages dominants : **regrouper** ([[Clustering]]), **compresser / représenter** ([[Réduction de dimension]]), **repérer l'anormal** ([[Détection d'outliers multivariée]]).

## Concepts clés

### Ce qui change tout : pas de vérité terrain
- En supervisé, une métrique tranche entre deux modèles. Ici, **rien ne tranche objectivement** : deux partitions différentes peuvent être toutes deux défendables.
- La validation devient interne (silhouette, inertie, BIC), par stabilité (re-runs, ré-échantillons), et surtout **métier** : les groupes trouvés ont-ils un sens pour quelqu'un ? Voir [[Clustering evaluation]].
- Corollaire : un résultat non supervisé se **présente et se discute**, il ne se « valide » pas seul.

### Regrouper
- Partitionner les observations en groupes homogènes : [[K-Means]], [[DBSCAN]], [[HDBSCAN]], [[Classification hiérarchique (CAH)]], [[Gaussian Mixture Models (GMM)]]. Vue d'ensemble et critères de choix : [[Clustering]].

### Représenter et compresser
- Projeter dans un espace de plus faible dimension en préservant l'essentiel : [[PCA]] (linéaire), [[t-SNE and UMAP]] (voisinage local, **visualisation seulement**), [[Manifold learning]], [[SVD]].
- Sur données non structurées, les représentations apprises jouent ce rôle : [[embeddings]].
- Familles factorielles selon le type de variables : [[CA]] (contingence), [[MCA]] (qualitatif), [[FAMD]] (mixte), [[MFA]] (groupes de variables).

### Repérer l'anormal
- Sans étiquettes de fraude / panne, on modélise le « normal » et on mesure l'écart : [[Isolation Forest]], [[Détection d'outliers multivariée]], [[Détection d'outliers univariée]].

### Tout repose sur la distance
- La plupart de ces méthodes ne voient les données qu'à travers une mesure de proximité. Le choix de la distance **est** le choix du modèle.
- Conséquences : **standardiser** est obligatoire ([[Mise à l'échelle]]), et en grande dimension les distances se concentrent au point de perdre leur pouvoir discriminant — réduire d'abord.

## Les maths, simplement

- Inertie intra-cluster, le critère des méthodes de partition : $W = \sum_{k=1}^{K} \sum_{x \in C_k} \lVert x - \mu_k \rVert^2$ — la dispersion qui reste une fois les groupes formés. Elle décroît mécaniquement avec $K$, d'où l'inutilité de la minimiser seule.
- [[PCA]] : chercher les directions $w$ qui maximisent la variance projetée, $\max_{\lVert w \rVert = 1} \operatorname{Var}(Xw)$. La solution est donnée par les vecteurs propres de la matrice de covariance ([[Eigendecomposition]]).
- Le fléau de la dimension : quand $d$ grandit, le rapport entre distance la plus proche et la plus lointaine tend vers 1 — « tout le monde est à la même distance », et le clustering perd son sens.

## En pratique

- **Standardiser d'abord**, systématiquement. Sans cela, la variable exprimée en euros écrase celle exprimée en années ([[Mise à l'échelle]]).
- **Réduire avant de regrouper** en grande dimension : [[PCA]] puis clustering est un enchaînement classique et robuste (cf. [[HCPC]]).
- **[[t-SNE and UMAP]] servent à voir, pas à conclure.** Les distances inter-clusters et les tailles de groupes y sont des artefacts. Ne jamais clusteriser sur des coordonnées t-SNE.
- Ne pas chercher « le bon nombre de clusters » comme s'il existait. Il dépend de la granularité utile au métier, pas d'un optimum mathématique.
- Le non supervisé est souvent une **étape**, pas une finalité : segmenter pour ensuite modéliser, réduire pour ensuite classer, détecter pour ensuite étiqueter — et l'étiquetage ainsi amorcé fait basculer en [[Apprentissage supervisé]].
- Outils : [[Dev/Services/Scikit-Learn|sklearn.cluster / sklearn.decomposition]], [[Dev/Services/umap-learn|umap-learn]], [[Dev/Services/hdbscan|hdbscan]], [[Dev/Services/PyOD|PyOD]] (anomalies), [[Dev/Services/Prince|Prince]] (analyses factorielles).

## Approches voisines & alternatives

- [[Apprentissage supervisé]] — le pendant avec cible : prédire plutôt que structurer.
- [[Clustering]] — le chapeau du regroupement, et ses quatre familles.
- [[Réduction de dimension]] — le chapeau de la compression / représentation.
- [[PCA]] — la méthode linéaire de référence, point de départ par défaut.
- [[Détection d'outliers multivariée]] — repérer l'anormal sans étiquettes.
- [[embeddings]] — représentations apprises, le non supervisé des données non structurées.
- [[Types de données et choix de modèle]] — l'aiguillage : pas de cible, donc quelle méthode.
- [[Reinforcement learning]] — ni cible ni structure : un signal de récompense.

## Pour aller plus loin

- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 14 (Unsupervised Learning).
- Documentation scikit-learn — *Clustering* (tableau des hypothèses par méthode) et *Decomposing signals*.
- Wattenberg, Viégas, Johnson (2016) — *How to Use t-SNE Effectively* (Distill) : pourquoi les cartes trompent.
