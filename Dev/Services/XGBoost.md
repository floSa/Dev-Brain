---
galaxie: dev
type: service
nom: XGBoost
alias: [xgboost, eXtreme Gradient Boosting]
pitch: "Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Dev/Services/LightGBM|LightGBM]]", "[[Dev/Services/CatBoost|CatBoost]]", "[[Dev/Services/Scikit-Learn|Scikit-Learn]]"]
remplace_par: []
status: actif
tags: [supervised, tree-based, ensemble, boosting, distributed]
url_docs: https://xgboost.readthedocs.io/
url_repo: https://github.com/dmlc/xgboost
---

# XGBoost

## Pourquoi

Implémentation C++ du [[Gradient Boosting (GBDT)]] devenue la référence. Apporte au boosting classique une **régularisation explicite** (L1/L2 sur les poids des feuilles), un algorithme par **histogrammes** rapide, la gestion native des valeurs manquantes, et surtout un **passage à l'échelle distribué** (Spark, Dask, Ray, Flink). C'est l'outil qui a popularisé le GBDT en compétition (Kaggle).

## Quand l'utiliser

- Données **tabulaires** structurées, classification ou régression — souvent le meilleur modèle hors deep learning.
- Besoin de distribuer l'entraînement sur cluster (Spark / Dask / Ray) ou sur GPU.
- Intégration dans un écosystème large : bindings Python, R, Java, Scala, Julia.
- Réglage fin recherché : nombreux hyperparamètres, contrôle complet de la régularisation.

## Quand NE PAS l'utiliser

- Vitesse d'entraînement prioritaire sur très gros volumes → [[Dev/Services/LightGBM|LightGBM]] (leaf-wise plus rapide).
- Beaucoup de variables **catégorielles** à fort cardinal → [[Dev/Services/CatBoost|CatBoost]] (encodage natif).
- Besoin modeste sans dépendance dédiée → le `HistGradientBoosting` de [[Dev/Services/Scikit-Learn|Scikit-Learn]] suffit.
- Données non tabulaires (images, texte, séquences) → réseaux de neurones.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), `uv add xgboost` ; rien à héberger.
- Cœur C++ ; entraînement CPU multi-thread ou GPU (CUDA).
- Distribué via Spark, Dask, Ray, Flink pour les volumes qui dépassent une machine.

## Pièges

- Croissance **level-wise** par défaut : plus robuste mais plus lente que le leaf-wise de LightGBM.
- Sans réglage conjoint de `n_estimators` / `learning_rate` / `max_depth` (+ early stopping), surapprentissage facile.
- Deux API distinctes : « sklearn » (`XGBClassifier`) et native (`xgb.train` + `DMatrix`) — ne pas les mélanger.

## Alternatives

- [[Dev/Services/LightGBM|LightGBM]] — Gradient boosting Microsoft optimisé vitesse et mémoire : croissance des arbres par feuille (leaf-wise) et binning histogramme, taillé pour les gros volumes.
- [[Dev/Services/CatBoost|CatBoost]] — Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning.
- [[Dev/Services/Scikit-Learn|Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

## Liens

- Concept implémenté : [[Gradient Boosting (GBDT)]] — sur la brique de base [[Arbres de décision]]
- [[Comparatif - Boosting]] — comparatif des libs de boosting
- Doc : https://xgboost.readthedocs.io/
