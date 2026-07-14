---
galaxie: dev
type: service
nom: Scikit-Learn
alias: [sklearn, scikit-learn]
pitch: "Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/XGBoost|XGBoost]]", "[[Dev/Services/LightGBM|LightGBM]]", "[[Dev/Services/CatBoost|CatBoost]]", "[[Dev/Services/Featuretools|Featuretools]]", "[[Dev/Services/category_encoders|category_encoders]]", "[[Dev/Services/Optuna|Optuna]]", "[[Dev/Services/hdbscan|hdbscan]]", "[[Dev/Services/umap-learn|umap-learn]]"]
remplace_par: []
status: actif
tags: [supervised, unsupervised, dimensionality-reduction, model-evaluation]
url_docs: https://scikit-learn.org/stable/
url_repo: https://github.com/scikit-learn/scikit-learn
---

# Scikit-Learn

## Pourquoi

Bibliothèque de **machine learning généraliste** sur données tabulaires en mémoire, au-dessus de NumPy/SciPy. Sa force est une **API uniforme** : tout objet est un estimateur avec `fit` / `predict` (ou `transform`), composable via `Pipeline` et réglable via `GridSearchCV`. Une seule grammaire couvre supervisé, non supervisé, réduction de dimension, préparation des données et évaluation. C'est le socle ML de l'écosystème Python — d'autres libs (dont [[Dev/Services/Prince|Prince]]) en empruntent l'API.

## Quand l'utiliser

- **Supervisé** : module `linear_model` ([[Régression linéaire]], [[Régression logistique]], variantes à [[Régularisation]] Ridge/Lasso/ElasticNet), SVM, arbres, module `ensemble` ([[Random Forest]], [[Gradient Boosting (GBDT)]], bagging, voting/stacking), k-NN.
- **Non supervisé** : module `cluster` — [[Clustering]] ([[K-Means|k-means]], [[DBSCAN]] / [[Wiki/Concepts/HDBSCAN|HDBSCAN]], [[Classification hiérarchique (CAH)|agglomératif]], [[Gaussian Mixture Models (GMM)|mélanges gaussiens]]) et **décomposition** — module `sklearn.decomposition` : [[Wiki/Concepts/PCA|PCA]], `KernelPCA` (non-linéaire), `FastICA` (sources indépendantes), `NMF` (facteurs positifs). Famille élargie : [[Réduction de dimension]].
- **Preprocessing & pipelines** : module `preprocessing` — [[Mise à l'échelle|scaling]], [[Encodage des variables catégorielles|encodage]], imputation — composé via `ColumnTransformer` / `Pipeline` (un seul `fit` train → `transform` test, anti-fuite) ; tri des variables par `feature_selection` → [[Sélection de variables]].
- **Model selection & métriques** : module `model_selection` — [[Validation croisée]] et recherche d'hyperparamètres (`GridSearchCV`, `RandomizedSearchCV` → [[Optimisation d'hyperparamètres]]) ; module `metrics` riche (accuracy, F1, RMSE, silhouette… et [[ROC-AUC & courbe PR]]).

## Quand NE PAS l'utiliser

- Réseaux de neurones / entraînement GPU → [[Dev/Services/PyTorch|PyTorch]], [[Dev/Services/TensorFlow|TensorFlow]], [[Dev/Services/JAX|JAX]].
- Gradient boosting state-of-the-art sur gros volumes → [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/CatBoost|CatBoost]].
- Analyse factorielle descriptive façon FactoMineR (CA, MCA, FAMD, contributions, cos²) → [[Dev/Services/Prince|Prince]], [[Dev/Services/Fanalysis|Fanalysis]].
- Inférence statistique avec p-values, IC et diagnostics → [[Dev/Services/statsmodels|statsmodels]], [[Dev/Services/scipy.stats|scipy.stats]].

## Déploiement & coût

- Bibliothèque Python (`uv add scikit-learn`), au-dessus de NumPy/SciPy ; rien à héberger.
- Single-node, calcul en mémoire (parallélisme CPU via `n_jobs` ; pas de GPU natif, support Array API émergent).
- BSD-3-Clause, gratuit.

## Pièges

- **Fuite de données** : `fit` (et `fit_transform`) sur le train uniquement, `transform` sur le test — passer par un `Pipeline` pour le garantir dans la validation croisée.
- PCA et modèles à distance/régularisation sont **sensibles à l'échelle** : standardiser avant (dans le pipeline).
- Tout reste en mémoire single-node : sur de très gros volumes, échantillonner ou changer d'outil.

## Alternatives

Pour le gradient boosting en particulier — sklearn embarque `HistGradientBoosting`, mais les libs dédiées vont plus loin :

- [[Dev/Services/XGBoost|XGBoost]] — Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires.
- [[Dev/Services/LightGBM|LightGBM]] — Gradient boosting Microsoft optimisé vitesse et mémoire : croissance des arbres par feuille (leaf-wise) et binning histogramme, taillé pour les gros volumes.
- [[Dev/Services/CatBoost|CatBoost]] — Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning.

Pour la préparation des données et le réglage — sklearn couvre l'essentiel, des libs spécialisées vont plus loin :

- [[Dev/Services/Featuretools|Featuretools]] — Ingénierie de features automatisée par Deep Feature Synthesis : empile des primitives d'agrégation et de transformation sur des données relationnelles/temporelles pour générer des centaines de variables.
- [[Dev/Services/category_encoders|category_encoders]] — Encodeurs catégoriels compatibles scikit-learn — Target, Weight of Evidence, James-Stein, CatBoost, hashing — pour les variables à forte cardinalité.
- [[Dev/Services/Optuna|Optuna]] — Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable.

Pour le clustering par densité et la réduction de dimension non linéaire — sklearn les embarque, mais les libs des auteurs vont plus loin :

- [[Dev/Services/hdbscan|hdbscan]] — Implémentation de référence de HDBSCAN — clustering par densité hiérarchique qui découvre le nombre de clusters, gère les densités hétérogènes et isole le bruit, avec un seul paramètre intuitif (taille minimale de cluster).
- [[Dev/Services/umap-learn|umap-learn]] — Réduction de dimension non linéaire par apprentissage de variété (UMAP) — projette en 2-3D pour la visualisation ou en k dimensions pour le pré-traitement, en préservant mieux la structure globale que t-SNE et bien plus vite.

Pour le deep learning / l'entraînement GPU : [[Dev/Services/PyTorch|PyTorch]], [[Dev/Services/TensorFlow|TensorFlow]], [[Dev/Services/JAX|JAX]].

## Liens

- Concepts implémentés, par module :
    - `linear_model` : [[Régression linéaire]], [[Régression logistique]], [[Régularisation]]
    - `ensemble` : [[Random Forest]], [[Gradient Boosting (GBDT)]]
    - `cluster` : [[Clustering]] — [[K-Means]], [[Classification hiérarchique (CAH)|CAH]], [[DBSCAN]] / [[Wiki/Concepts/HDBSCAN|HDBSCAN]], [[Gaussian Mixture Models (GMM)|GMM]]
    - `decomposition` : [[Wiki/Concepts/PCA|PCA]], [[Réduction de dimension]]
    - `preprocessing` : [[Mise à l'échelle]], [[Encodage des variables catégorielles]]
    - `feature_selection` : [[Sélection de variables]]
    - `model_selection` : [[Validation croisée]], [[Optimisation d'hyperparamètres]]
    - `metrics` : [[ROC-AUC & courbe PR]]
- [[Dev/Services/Prince|Prince]] — analyse factorielle sur l'API scikit-learn
- [[Dev/Patterns/Comparatif - Réduction de dimension]] — PCA / t-SNE (sklearn) vs UMAP / PaCMAP.
- Doc : https://scikit-learn.org/stable/
