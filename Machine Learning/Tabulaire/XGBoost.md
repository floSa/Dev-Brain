---
role: brique
nom: XGBoost
alias: [xgboost, eXtreme Gradient Boosting]
pitch: "Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires."
categorie: ml/tabulaire
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[LightGBM]]", "[[CatBoost]]", "[[Scikit-Learn]]"]
complements: []
tags: [supervised, tree-based, ensemble, boosting, distributed]
url_docs: https://xgboost.readthedocs.io/
url_repo: https://github.com/dmlc/xgboost
---

# XGBoost

<!-- AUTO:BANDEAU:START -->
> Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-15 |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation de référence du gradient boosting sur arbres. Elle ajoute au boosting classique
une régularisation explicite — pénalités L1 et L2 sur les poids des feuilles —, un algorithme
par histogrammes, la gestion native des valeurs manquantes, et un passage à l'échelle
distribué mature : Spark, Dask, Ray, Flink. Les arbres croissent *level-wise*, niveau par
niveau : plus prudent que le *leaf-wise*, donc plus lent, mais c'est celui qui surapprend le
moins sur un petit jeu. Deux API coexistent, l'une compatible scikit-learn (`XGBClassifier`),
l'autre native (`xgb.train` sur `DMatrix`).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Données tabulaires, classification ou régression : souvent le meilleur modèle hors deep learning | Croissance *level-wise* : sensiblement plus lente que le *leaf-wise* sur de très gros volumes |
| Distribuer l'entraînement sur cluster (Spark, Dask, Ray, Flink) ou sur GPU | Sans réglage conjoint de `n_estimators`, `learning_rate` et `max_depth`, plus l'early stopping, le surapprentissage vient vite |
| Écosystème large : bindings Python, R, Java, Scala, Julia | Les deux API — sklearn et native — ne se mélangent pas dans un même code |
| Réglage fin recherché : contrôle complet de la régularisation | Données non tabulaires — images, texte, séquences → [[Apprentissage profond]] |
| | Besoin modeste sans dépendance dédiée → le `HistGradientBoosting` de [[Scikit-Learn]] |

## Mise en œuvre

- Installation — `uv add xgboost`
- Point d'entrée — API Python `XGBClassifier` / `XGBRegressor`, ou l'API native `xgb.train` sur `DMatrix` ; bindings R, Java, Scala, Julia
- Prérequis — aucun : le cœur C++ est précompilé dans les roues
- Exécution — CPU multi-thread ou GPU (CUDA) sur une machine ; distribué via Spark, Dask, Ray, Flink
- Coût — gratuit, Apache-2.0 ; rien à héberger

## Écosystème

### Alternatives

- [[LightGBM]] — Gradient boosting Microsoft optimisé vitesse et mémoire : croissance des arbres par feuille (leaf-wise) et binning histogramme, taillé pour les gros volumes.
- [[CatBoost]] — Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning.
- [[Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

## Ressources

- Documentation — https://xgboost.readthedocs.io/
- Dépôt — https://github.com/dmlc/xgboost

## Voir aussi

- [[Gradient Boosting (GBDT)]] — la notion qu'il implémente
- [[Arbres de décision]] — la brique de base sur laquelle le boosting empile
- [[Comparatif - Boosting]] — ce qui départage les trois implémentations du dossier
