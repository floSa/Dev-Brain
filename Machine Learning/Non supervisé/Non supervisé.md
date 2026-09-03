---
role: hub
nom: Non supervisé
alias: [unsupervised]
pitch: Chercher une structure sans cible — regrouper, réduire, repérer l'anormal — sans plus rien qui dise qu'on a raison.
domaines: [data-sci, ml-eng]
tags: [unsupervised, clustering, dimensionality-reduction, anomaly-detection, manifold]
---

# Non supervisé

> Chercher une structure sans cible — regrouper, réduire, repérer l'anormal — sans plus rien qui dise qu'on a raison.

## Ce qu'il faut comprendre

- **Ce qui définit ce dossier n'est pas une technique, c'est une absence.** Il n'y a pas de $y$, donc pas d'erreur à minimiser, donc pas de validation croisée pour trancher. [[Apprentissage non supervisé]] pose le cadre et ses trois usages : regrouper, représenter, repérer l'anormal. Le changement par rapport à [[Socle]] n'est pas l'algorithme, c'est la **nature de la preuve** — et c'est ce qui rend ce dossier plus exigeant, pas plus simple.
- **Regrouper, c'est choisir une hypothèse de forme avant de choisir un algorithme.** [[Clustering]] pose le cadre. [[K-Means]] suppose des groupes sphériques de taille comparable et fixe leur nombre d'avance ; [[k-médoïds (PAM)]] garde la partition mais prend un point réel pour centre, donc encaisse les outliers et accepte une dissimilarité quelconque ; [[DBSCAN]] et [[Clustering hiérarchique par densité]] ne fixent aucun nombre, trouvent des formes arbitraires et laissent le bruit dehors — le second en explorant tous les seuils de densité au lieu d'un seul ; [[Classification hiérarchique (CAH)]] rend un arbre plutôt qu'une partition, donc une décision différée ; [[Gaussian Mixture Models (GMM)]] rend une affectation probabiliste et des groupes ellipsoïdaux.
- **Un partitionnement se juge, et mal.** [[Clustering evaluation]] est la page à lire *avant* d'annoncer un résultat : les indices internes mesurent une cohésion géométrique, pas une pertinence métier, et deux indices peuvent classer deux partitions en sens inverse. C'est le contrôle le plus souvent sauté du dossier.
- **Réduire la dimension sert à deux choses opposées, et les outils ne sont pas interchangeables** : voir, ou alimenter un modèle. [[t-SNE and UMAP]] préservent le voisinage local et servent à regarder — les distances entre amas d'une projection t-SNE ne veulent rien dire ; [[Manifold learning]] est la famille dont elles sont la branche visualisation, et ses autres méthodes (Isomap, LLE, Kernel PCA) rendent des coordonnées réutilisables en aval ; [[ICA]] sépare des sources indépendantes ; [[NMF]] impose la positivité et donne des parties additives, donc interprétables. Les [[embeddings]], au niveau du domaine, sont la version **apprise** du même problème.
- **La frontière avec [[Analyse factorielle]] est réelle, fine, et elle est écrite.** Là-bas on décompose un tableau pour **interpréter les axes** — on regarde le biplot et on nomme les dimensions ; ici on cherche une **représentation utile à une tâche**, et on la juge sur cette tâche. Les deux familles partagent le tag `dimensionality-reduction`, et c'est précisément pour ça que le critère est écrit plutôt que deviné.
- **L'anomalie est un problème de définition avant d'être un problème d'algorithme.** [[Détection d'outliers univariée]] cherche une valeur extrême sur un axe, [[Détection d'outliers multivariée]] une violation de la structure de corrélation — un point normal partout et anormal en conjonction. Les trois détecteurs multivariés traduisent trois hypothèses différentes sur le mot « anormal » : la densité locale ([[Local Outlier Factor]], le seul à capter le contextuel), la facilité d'isolement ([[Isolation Forest]]), l'enveloppe apprise du normal ([[One-Class SVM]]).

## Choisir

- Ne pas savoir combien de groupes il y a → [[DBSCAN]] ou [[Clustering hiérarchique par densité]], puis [[hdbscan]].
- Le savoir, beaucoup de points, une contrainte de temps → [[K-Means]].
- Des outliers dans les données, ou une distance qui n'est pas euclidienne → [[k-médoïds (PAM)]].
- Une appartenance graduée plutôt qu'un vote net → [[Gaussian Mixture Models (GMM)]].
- Décider du nombre de groupes après coup, en regardant → [[Classification hiérarchique (CAH)]].
- Vérifier qu'une partition vaut quelque chose → [[Clustering evaluation]].
- Voir un nuage en deux dimensions → [[umap-learn]] ou [[PaCMAP]], et [[t-SNE and UMAP]] pour lire la projection sans se tromper. Cf. [[Comparatif - Réduction de dimension]], au niveau du domaine.
- Des coordonnées à réutiliser dans un pipeline, pas seulement à regarder → [[Manifold learning]], Kernel PCA en particulier.
- Des signaux mélangés à séparer → [[ICA]] ; des parties additives interprétables sur données positives → [[NMF]].
- Des anomalies sur du tabulaire, sans parier une méthode → [[PyOD]]. Cf. [[Comparatif - Détection d'anomalies]].
- Interpréter des axes plutôt qu'alimenter un modèle → [[Analyse factorielle]], pas ce dossier.

<!-- AUTO:START -->
### Notions
- [[Apprentissage non supervisé]] — domaines : data-sci
- [[Classification hiérarchique (CAH)]] — domaines : data-sci
- [[Clustering]] — domaines : data-sci
- [[Clustering evaluation]] — domaines : data-sci
- [[Clustering hiérarchique par densité]] — domaines : data-sci
- [[DBSCAN]] — domaines : data-sci
- [[Détection d'outliers multivariée]] — domaines : data-sci, ml-eng
- [[Détection d'outliers univariée]] — domaines : data-sci, ml-eng
- [[Gaussian Mixture Models (GMM)]] — domaines : data-sci
- [[ICA]] — domaines : data-sci
- [[Isolation Forest]] — domaines : data-sci, ml-eng
- [[K-Means]] — domaines : data-sci
- [[k-médoïds (PAM)]] — domaines : data-sci
- [[Local Outlier Factor]] — domaines : data-sci, ml-eng
- [[Manifold learning]] — domaines : data-sci
- [[NMF]] — domaines : data-sci
- [[One-Class SVM]] — domaines : data-sci, ml-eng
- [[t-SNE and UMAP]] — domaines : data-sci

### Briques
- [[hdbscan]] — Implémentation de référence de HDBSCAN — clustering par densité hiérarchique qui découvre le nombre de clusters, gère les densités hétérogènes et isole le bruit, avec un seul paramètre intuitif (taille minimale de cluster).
- [[PaCMAP]] — Réduction de dimension préservant structure locale ET globale — projette en 2-3D via des paires mid-near, plus fidèle à la topologie d'ensemble que t-SNE et UMAP, et scalable.
- [[PyOD]] — Boîte à outils Python unifiée pour la détection d'outliers multivariés — 50+ détecteurs (LOF, Isolation Forest, ECOD, COPOD, autoencodeurs…) sous une API scikit-learn, pour comparer les méthodes au lieu d'en parier une.
- [[umap-learn]] — Réduction de dimension non linéaire par apprentissage de variété (UMAP) — projette en 2-3D pour la visualisation ou en k dimensions pour le pré-traitement, en préservant mieux la structure globale que t-SNE et bien plus vite.
<!-- AUTO:END -->

## Notes
