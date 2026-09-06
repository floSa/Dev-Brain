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

<!-- AUTO:BANDEAU:START -->
> Gradient boosting Microsoft optimisé vitesse et mémoire : croissance des arbres par feuille (leaf-wise) et binning histogramme, taillé pour les gros volumes.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation du gradient boosting créée par Microsoft, maintenue depuis 2026 sous
l'organisation indépendante `lightgbm-org`, avec les mêmes mainteneurs. Elle est réglée pour la
vitesse et la mémoire : arbres en croissance *leaf-wise* — le meilleur découpage d'abord, où
qu'il soit —, binning par histogrammes, et deux astuces signatures, GOSS qui échantillonne
selon le gradient et EFB qui regroupe les variables creuses mutuellement exclusives. C'est
souvent le plus rapide à entraîner sur gros volumes ; c'est aussi celui qui surapprend le plus
vite si `num_leaves` n'est pas borné.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Gros jeux tabulaires où le temps d'entraînement et l'empreinte mémoire comptent | Petits jeux : la croissance *leaf-wise* y surapprend vite |
| Beaucoup de variables, dont des creuses issues du one-hot : EFB les regroupe | `num_leaves` est le levier central, distinct de `max_depth` : trop grand pour la profondeur, on surajuste |
| Variables catégorielles en cardinalité modérée : prise en charge native, sans one-hot | Variables catégorielles à déclarer explicitement (`categorical_feature`), sinon traitées comme numériques |
| Entraînement distribué intégré, ou sur GPU | `min_data_in_leaf` à soigner en même temps, sous peine de feuilles bâties sur quelques points |
| | Besoin modeste sans dépendance dédiée → le `HistGradientBoosting` de [[Scikit-Learn]], inspiré de LightGBM |

## Mise en œuvre

- Installation — `uv add lightgbm`
- Point d'entrée — API Python `LGBMClassifier` / `LGBMRegressor`, ou `lgb.train` sur un `Dataset` ; bindings R et C#
- Prérequis — aucun : le cœur C++ est précompilé dans les roues
- Exécution — CPU multi-thread, GPU, et mode distribué intégré (apprentissage en réseau)
- Coût — gratuit, MIT ; rien à héberger

## Écosystème

### Alternatives

- [[XGBoost]] — Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires.
- [[CatBoost]] — Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning.
- [[Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

## Ressources

- Documentation — https://lightgbm.readthedocs.io/
- Dépôt — https://github.com/lightgbm-org/LightGBM

## Voir aussi

- [[Gradient Boosting (GBDT)]] — la notion qu'il implémente
- [[Arbres de décision]] — la brique de base sur laquelle le boosting empile
- [[Comparatif - Boosting]] — ce qui départage les trois implémentations du dossier
