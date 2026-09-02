---
role: brique
nom: LightGBM
alias: [lightgbm, lgbm, Light Gradient Boosting Machine]
pitch: "Gradient boosting Microsoft optimisé vitesse et mémoire : croissance des arbres par feuille (leaf-wise) et binning histogramme, taillé pour les gros volumes."
categorie: ml/tabulaire
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[XGBoost]]", "[[CatBoost]]", "[[Scikit-Learn]]"]
complements: []
tags: [supervised, tree-based, ensemble, boosting, distributed]
url_docs: https://lightgbm.readthedocs.io/
url_repo: https://github.com/lightgbm-org/LightGBM
---

# LightGBM

## Pourquoi

Implémentation C++ du [[Gradient Boosting (GBDT)]] créée par Microsoft (maintenue depuis 2026 sous l'organisation indépendante `lightgbm-org`, mêmes mainteneurs). Optimisée pour la **vitesse** et la **mémoire** : arbres en croissance **leaf-wise** (meilleur découpage d'abord), **binning par histogrammes**, et deux astuces signatures — GOSS (échantillonnage orienté gradient) et EFB (regroupement de variables creuses exclusives). Souvent le plus rapide à entraîner sur gros volumes.

## Quand l'utiliser

- Gros jeux tabulaires où le **temps d'entraînement** et l'empreinte mémoire comptent.
- Beaucoup de variables, dont creuses (one-hot) — EFB les regroupe.
- Variables catégorielles modérées : prise en charge native, sans one-hot.
- Entraînement distribué intégré (apprentissage en réseau) ou sur GPU.

## Quand NE PAS l'utiliser

- Petits jeux de données → le leaf-wise surapprend vite ; [[XGBoost]] (level-wise) est plus prudent.
- Variables catégorielles nombreuses et à fort cardinal → [[CatBoost]] (encodage ordonné anti-fuite).
- Besoin modeste sans dépendance dédiée → `HistGradientBoosting` de [[Scikit-Learn]] (inspiré de LightGBM).

## Déploiement & coût

- Bibliothèque open-source (MIT), `uv add lightgbm` ; rien à héberger.
- Cœur C++ ; CPU multi-thread, GPU, et mode distribué intégré.
- Bindings Python, R, C#.

## Pièges

- Croissance **leaf-wise** = surapprentissage rapide : borner `num_leaves` et `max_depth`, soigner `min_data_in_leaf`.
- `num_leaves` est le levier central (≠ `max_depth`) — trop grand pour la profondeur, on surajuste.
- Variables catégorielles : les déclarer explicitement (`categorical_feature`), sinon traitées comme numériques.

## Alternatives

- [[XGBoost]] — Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires.
- [[CatBoost]] — Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning.
- [[Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

## Liens

- Concept implémenté : [[Gradient Boosting (GBDT)]] — sur la brique de base [[Arbres de décision]]
- [[Comparatif - Boosting]] — comparatif des libs de boosting
- Doc : https://lightgbm.readthedocs.io/
