---
role: brique
nom: Scikit-Learn
alias: [sklearn, scikit-learn]
pitch: "Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques."
categorie: ml/socle
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[XGBoost]]", "[[LightGBM]]", "[[CatBoost]]", "[[Featuretools]]", "[[category_encoders]]", "[[Optuna]]", "[[hdbscan]]", "[[umap-learn]]"]
complements: []
tags: [supervised, unsupervised, dimensionality-reduction, model-evaluation]
url_docs: https://scikit-learn.org/stable/
url_repo: https://github.com/scikit-learn/scikit-learn
---

# Scikit-Learn

<!-- AUTO:BANDEAU:START -->
> Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Le socle du machine learning sur données tabulaires en mémoire, au-dessus de NumPy et SciPy. Sa force n'est pas un algorithme mais une **grammaire uniforme** : tout objet est un estimateur avec `fit` / `predict` (ou `transform`), composable via `Pipeline` et réglable via `GridSearchCV` — une seule interface couvre supervisé, non supervisé, réduction de dimension, préparation des données et évaluation. D'autres bibliothèques en empruntent l'API plutôt que d'en inventer une. Cette grammaire porte aussi la discipline anti-fuite : `fit` et `fit_transform` sur le train uniquement, `transform` sur le test — le `Pipeline` est ce qui le garantit à l'intérieur d'une validation croisée, où l'oubli est invisible. Deuxième réflexe qu'elle n'impose pas : PCA, modèles à distance et modèles régularisés sont **sensibles à l'échelle**, la standardisation se pose donc dans le pipeline, pas après coup.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Supervisé : `linear_model`, SVM, arbres, `ensemble` (forêts, boosting, bagging, voting, stacking), k-NN | Réseaux de neurones ou entraînement GPU → [[PyTorch]], [[TensorFlow]], [[JAX]] |
| Non supervisé : `cluster` et `decomposition`, du k-means au mélange gaussien, de la PCA à la NMF | Gradient boosting à l'état de l'art sur gros volumes → [[XGBoost]], [[LightGBM]], [[CatBoost]] |
| Préparation et pipelines : `preprocessing`, `ColumnTransformer`, `feature_selection` — un seul `fit` sur le train | Analyse factorielle descriptive façon FactoMineR (CA, MCA, FAMD, contributions, cos²) → [[Prince]], [[Fanalysis]] |
| Sélection de modèle et métriques : `model_selection` et un module `metrics` riche | Inférence statistique avec p-values, intervalles de confiance et diagnostics → [[statsmodels]], [[scipy.stats]] |
| Feature engineering, encodage à forte cardinalité, réglage bayésien, densité et variétés — via les libs spécialisées de son écosystème | Volume qui ne tient plus en mémoire sur une machine : échantillonner, ou passer au flux → [[River]] |

## Mise en œuvre

- Installation — `uv add scikit-learn`, au-dessus de NumPy et SciPy
- Point d'entrée — import Python : un estimateur, ou un `Pipeline` qui en compose plusieurs
- Prérequis — aucun ; pas de GPU natif, le support Array API est émergent
- Exécution — single-node, calcul en mémoire, parallélisme CPU par `n_jobs`
- Coût — gratuit, BSD-3-Clause ; rien à héberger

## Écosystème

### Alternatives

- [[XGBoost]] — Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires.
- [[LightGBM]] — Gradient boosting Microsoft optimisé vitesse et mémoire : croissance des arbres par feuille (leaf-wise) et binning histogramme, taillé pour les gros volumes.
- [[CatBoost]] — Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning.
- [[Featuretools]] — Ingénierie de features automatisée par Deep Feature Synthesis : empile des primitives d'agrégation et de transformation sur des données relationnelles/temporelles pour générer des centaines de variables.
- [[category_encoders]] — Encodeurs catégoriels compatibles scikit-learn — Target, Weight of Evidence, James-Stein, CatBoost, hashing — pour les variables à forte cardinalité.
- [[Optuna]] — Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable.
- [[hdbscan]] — Implémentation de référence de HDBSCAN — clustering par densité hiérarchique qui découvre le nombre de clusters, gère les densités hétérogènes et isole le bruit, avec un seul paramètre intuitif (taille minimale de cluster).
- [[umap-learn]] — Réduction de dimension non linéaire par apprentissage de variété (UMAP) — projette en 2-3D pour la visualisation ou en k dimensions pour le pré-traitement, en préservant mieux la structure globale que t-SNE et bien plus vite.

## Ressources

- Documentation — https://scikit-learn.org/stable/
- Dépôt — https://github.com/scikit-learn/scikit-learn

## Voir aussi

- [[Socle]] — le hub du domaine
- `linear_model` — [[Régression linéaire]], [[Régression logistique]], [[Régularisation]]
- `ensemble` — [[Random Forest]], [[Gradient Boosting (GBDT)]]
- `cluster` — [[Clustering]] : [[K-Means]], [[Classification hiérarchique (CAH)|CAH]], [[DBSCAN]], [[Clustering hiérarchique par densité|HDBSCAN]], [[Gaussian Mixture Models (GMM)|GMM]]
- `decomposition` — [[PCA]], [[Réduction de dimension]]
- `preprocessing` — [[Mise à l'échelle]], [[Encodage des variables catégorielles]]
- `feature_selection` — [[Sélection de variables]]
- `model_selection` — [[Validation croisée]], [[Optimisation d'hyperparamètres]]
- `metrics` — [[ROC-AUC & courbe PR]]
- [[Prince]] — l'analyse factorielle écrite sur l'API scikit-learn
- [[Comparatif - Réduction de dimension]] — PCA et t-SNE face à UMAP et PaCMAP
