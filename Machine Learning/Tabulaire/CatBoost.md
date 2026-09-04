---
role: brique
nom: CatBoost
alias: [catboost, Categorical Boosting]
pitch: "Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning."
categorie: ml/tabulaire
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[XGBoost]]", "[[LightGBM]]", "[[Scikit-Learn]]"]
complements: []
tags: [supervised, tree-based, ensemble, boosting]
url_docs: https://catboost.ai/docs/
url_repo: https://github.com/catboost/catboost
---

# CatBoost

<!-- AUTO:BANDEAU:START -->
> Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation du gradient boosting par Yandex, que deux partis pris distinguent. Les
variables catégorielles sont traitées nativement par *ordered target encoding* : l'encodage
par la cible est calculé sur un ordre de permutation, ce qui évite la fuite de cible sans
encodage manuel. Les arbres sont *symétriques* — le même test partout à un niveau donné —, ce
qui régularise et rend l'inférence rapide. Le résultat par défaut est bon sans réglage lourd ;
la contrepartie est un entraînement plus lent que LightGBM sur des colonnes purement
numériques.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Jeux riches en variables catégorielles, y compris à forte cardinalité : ni one-hot ni encodage manuel | Colonnes purement numériques : plus lent que les autres implémentations du dossier |
| Modèle solide sans réglage lourd : les défauts sont raisonnables | Colonnes catégorielles non déclarées dans `cat_features` : traitées comme numériques, et l'atout principal est perdu |
| Inférence rapide recherchée (arbres symétriques), entraînement GPU efficace | Mémoire et temps qui montent avec le nombre de permutations et la cardinalité |
| Interprétabilité : valeurs SHAP intégrées | Écosystème distribué déjà en place : les intégrations Spark, Dask et Ray y sont moins matures |

## Mise en œuvre

- Installation — `uv add catboost`
- Point d'entrée — API Python `CatBoostClassifier` / `CatBoostRegressor` avec `cat_features` ; bindings R et Java
- Prérequis — aucun : le cœur C++ est précompilé dans les roues
- Exécution — CPU multi-thread ou GPU sur une machine ; le distribué est possible, mais ce n'est pas son terrain
- Coût — gratuit, Apache-2.0 ; rien à héberger

## Écosystème

### Alternatives

- [[XGBoost]] — Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires.
- [[LightGBM]] — Gradient boosting Microsoft optimisé vitesse et mémoire : croissance des arbres par feuille (leaf-wise) et binning histogramme, taillé pour les gros volumes.
- [[Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

## Ressources

- Documentation — https://catboost.ai/docs/
- Dépôt — https://github.com/catboost/catboost

## Voir aussi

- [[Gradient Boosting (GBDT)]] — la notion qu'il implémente
- [[Arbres de décision]] — la brique de base sur laquelle le boosting empile
- [[Encodage des variables catégorielles]] — la notion que son *ordered target encoding* internalise
- [[Comparatif - Boosting]] — ce qui départage les trois implémentations du dossier
