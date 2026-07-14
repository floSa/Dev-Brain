---
galaxie: dev
type: service
nom: Optuna
alias: [optuna, TPESampler]
pitch: "Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable."
categorie: ml/hyperopt
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Scikit-Learn|Scikit-Learn]]", "[[Dev/Services/Hyperopt|Hyperopt]]", "[[Dev/Services/Ray Tune|Ray Tune]]"]
remplace_par: []
status: actif
tags: [hyperparameter-tuning, bayesian, distributed]
url_docs: https://optuna.readthedocs.io/
url_repo: https://github.com/optuna/optuna
---

# Optuna

## Pourquoi

Framework d'**optimisation d'hyperparamètres** au design *define-by-run* : l'espace de recherche se déclare dynamiquement dans le code (`trial.suggest_float`, `suggest_int`, `suggest_categorical`), ce qui autorise des espaces conditionnels et des boucles. Le moteur combine **recherche bayésienne** (TPE par défaut, GP, CMA-ES) et **pruning** — l'arrêt précoce des essais non prometteurs (MedianPruner, HyperbandPruner, SuccessiveHalving) — pour économiser le budget. Parallélisation native via un **storage partagé** (RDB) et suivi visuel (`optuna-dashboard`). Maintenu par Preferred Networks.

## Quand l'utiliser

- Réglage coûteux où chaque entraînement est lourd : la recherche bayésienne converge en moins d'essais qu'une grille.
- Espace de recherche **conditionnel** ou irrégulier, mal exprimé par un produit cartésien.
- Besoin d'**élaguer** tôt les essais ratés (deep learning, GBDT avec early stopping).
- Campagne **distribuée** sur plusieurs workers/nœuds partageant un storage.
- Intégrations prêtes : scikit-learn, [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/PyTorch|PyTorch]].

## Quand NE PAS l'utiliser

- Petit espace, quelques combinaisons → `GridSearchCV` / `RandomizedSearchCV` de [[Dev/Services/Scikit-Learn|Scikit-Learn]] suffisent.
- Orchestration distribuée lourde sur cluster (schedulers ASHA/PBT) → [[Dev/Services/Ray Tune|Ray Tune]] (qui sait d'ailleurs piloter Optuna comme moteur de recherche).

## Déploiement & coût

- Bibliothèque Python open-source (MIT), `uv add optuna` ; rien à héberger pour l'usage local.
- Single-node par défaut ; **distribué** en pointant plusieurs workers sur un storage commun (SQLite/PostgreSQL/MySQL).
- Dashboard optionnel (`optuna-dashboard`) pour le suivi en temps réel.

## Pièges

- Sans **storage persistant**, une étude (`study`) en mémoire est perdue à la fin du process.
- Le pruning suppose une métrique **rapportée par étapes** (`trial.report` + `should_prune`) : inapplicable à un entraînement opaque en un bloc.
- Définir les plages d'échelle en **log** (`log=True`) pour les taux d'apprentissage / régularisation, sinon l'échantillonnage est inefficace.

## Alternatives

- [[Dev/Services/Scikit-Learn|Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.
- [[Dev/Services/Hyperopt|Hyperopt]] — Optimisation d'hyperparamètres distribuée historique : recherche TPE (Parzen) sur espaces conditionnels, parallélisable via MongoDB/Spark ; mature mais peu maintenu.
- [[Dev/Services/Ray Tune|Ray Tune]] — Optimisation d'hyperparamètres distribuée sur Ray : schedulers à arrêt précoce (ASHA, PBT, HyperBand) et intégration des moteurs de recherche (Optuna, Hyperopt) à l'échelle du cluster.

## Liens

- Concept implémenté : [[Optimisation d'hyperparamètres]]
- Score optimisé fourni par : [[Validation croisée]]
- [[Comparatif - Optimisation d'hyperparamètres]] — comparatif de la catégorie
- Doc : https://optuna.readthedocs.io/
