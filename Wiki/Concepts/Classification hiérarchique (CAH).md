---
galaxie: wiki
type: concept
nom: Classification hiérarchique (CAH)
alias: [CAH, Classification ascendante hiérarchique, Hierarchical clustering, HAC, Agglomerative clustering, Dendrogramme]
categorie: concept/ml
domaines: [data-sci]
tags: [clustering, unsupervised]
---

# Classification hiérarchique (CAH)

## Aperçu

- Méthode de [[Clustering]] qui construit une **hiérarchie** de clusters emboîtés, visualisée par un **dendrogramme**, sans fixer le nombre de groupes à l'avance.
- Deux sens de construction : **ascendant** (agglomératif — chaque point part seul, on fusionne) ou **descendant** (divisif — tout dans un groupe, on scinde). L'ascendant (CAH) domine en pratique.

## Concepts clés

### Dendrogramme
- Arbre des fusions successives ; la hauteur d'une fusion = distance à laquelle deux groupes se rejoignent. Couper l'arbre à une hauteur donnée produit une partition ; le nombre de clusters se lit a posteriori.

### Critère de liaison (linkage)
- Définit la distance entre deux **groupes** à partir des distances entre points :
  - **single** (saut minimal) : distance des deux points les plus proches — sensible à l'effet de chaîne.
  - **complete** (saut maximal) : des deux points les plus éloignés — clusters compacts.
  - **average** : distance moyenne entre paires.
  - **Ward** : fusionne les deux groupes qui augmentent le moins l'inertie intra-classe — clusters de variance homogène, le choix par défaut le plus courant.

### Coût
- Agglomératif naïf en $O(n^3)$ (ou $O(n^2 \log n)$ avec optimisations), $O(n^2)$ en mémoire — réservé aux jeux de taille modérée.

## Les maths, simplement

- Ward : à chaque étape, fusionner les groupes $A$ et $B$ qui minimisent l'accroissement d'inertie $\Delta(A,B) = \dfrac{|A|\,|B|}{|A|+|B|}\, \lVert \mu_A - \mu_B \rVert^2$.
- La hauteur du dendrogramme croît à chaque fusion (monotonie) ; un **saut** net dans les hauteurs suggère un bon niveau de coupe.

## En pratique

- **Standardiser** avant (distances euclidiennes) ; choisir distance **et** linkage selon la forme attendue des groupes.
- Le dendrogramme aide à choisir le nombre de clusters : couper au plus grand saut d'inertie. Résultat déterministe — pas de relance comme K-Means.
- Coûteux en mémoire/temps : au-delà de quelques dizaines de milliers de points, échantillonner ou passer à K-Means / DBSCAN.
- Combinée à une réduction de dimension en amont, c'est le cœur de [[HCPC]] (CAH sur composantes principales, puis consolidation k-means).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.cluster.AgglomerativeClustering]] ; `scipy.cluster.hierarchy` (`linkage`, `dendrogram`, `fcluster`) pour tracer et couper.

## Approches voisines & alternatives

- [[Clustering]] — le cadre général et les autres familles.
- [[K-Means]] — plus rapide et scalable, mais $K$ imposé et pas de hiérarchie.
- [[HCPC]] — CAH appliquée aux composantes d'une analyse factorielle, avec description automatique des classes.
- [[DBSCAN]] / [[HDBSCAN]] — clusters par densité ; HDBSCAN produit aussi une hiérarchie, mais fondée sur la densité plutôt que sur un linkage géométrique.

## Pour aller plus loin

- Ward (1963) — *Hierarchical Grouping to Optimize an Objective Function*.
- Müllner (2011) — *Modern hierarchical, agglomerative clustering algorithms* (algorithmes efficaces).
