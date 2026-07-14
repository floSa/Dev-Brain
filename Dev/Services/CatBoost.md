---
galaxie: dev
type: service
nom: CatBoost
alias: [catboost, Categorical Boosting]
pitch: "Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Dev/Services/XGBoost|XGBoost]]", "[[Dev/Services/LightGBM|LightGBM]]", "[[Dev/Services/Scikit-Learn|Scikit-Learn]]"]
remplace_par: []
status: actif
tags: [supervised, tree-based, ensemble, boosting]
url_docs: https://catboost.ai/docs/
url_repo: https://github.com/catboost/catboost
---

# CatBoost

## Pourquoi

Implémentation C++ du [[Gradient Boosting (GBDT)]] par Yandex. Deux partis pris la distinguent : la **gestion native des variables catégorielles** par *ordered target encoding* (encodage par la cible calculé sur un ordre de permutation, qui évite la fuite de cible), et des **arbres symétriques** (oblivious trees : même test partout à un niveau donné), rapides à l'inférence et régularisants. Bon résultat « out of the box », avec peu de réglage.

## Quand l'utiliser

- Jeux tabulaires riches en **variables catégorielles** (haute cardinalité) — ni one-hot ni encodage manuel.
- Besoin d'un modèle solide **sans tuning lourd** (défauts raisonnables).
- Inférence rapide recherchée (arbres symétriques) ; entraînement GPU efficace.
- Interprétabilité : valeurs SHAP intégrées.

## Quand NE PAS l'utiliser

- Données purement numériques où la vitesse d'entraînement prime → [[Dev/Services/LightGBM|LightGBM]].
- Écosystème distribué Spark / Dask / Ray déjà en place → [[Dev/Services/XGBoost|XGBoost]] (intégrations plus matures).
- Besoin modeste sans dépendance dédiée → `HistGradientBoosting` de [[Dev/Services/Scikit-Learn|Scikit-Learn]].

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), `uv add catboost` ; rien à héberger.
- Cœur C++ ; CPU multi-thread et **GPU** (entraînement très optimisé). Bindings Python, R, Java.
- Entraînement distribué possible, mais le terrain de prédilection reste la machine unique (CPU / GPU).

## Pièges

- Déclarer les colonnes catégorielles (`cat_features`) — sinon traitées comme numériques, on perd l'atout principal.
- Plus lent que LightGBM sur données purement numériques.
- Mémoire et temps qui montent avec le nombre de permutations et la cardinalité catégorielle.

## Alternatives

- [[Dev/Services/XGBoost|XGBoost]] — Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires.
- [[Dev/Services/LightGBM|LightGBM]] — Gradient boosting Microsoft optimisé vitesse et mémoire : croissance des arbres par feuille (leaf-wise) et binning histogramme, taillé pour les gros volumes.
- [[Dev/Services/Scikit-Learn|Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

## Liens

- Concept implémenté : [[Gradient Boosting (GBDT)]] — sur la brique de base [[Arbres de décision]]
- [[Comparatif - Boosting]] — comparatif des libs de boosting
- Doc : https://catboost.ai/docs/
