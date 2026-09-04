---
role: brique
nom: Optuna
alias: [optuna, TPESampler]
pitch: "Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable."
categorie: ml/hyperopt
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Scikit-Learn]]", "[[Hyperopt]]", "[[Ray Tune]]"]
complements: []
tags: [hyperparameter-tuning, bayesian, distributed]
url_docs: https://optuna.readthedocs.io/
url_repo: https://github.com/optuna/optuna
---

# Optuna

<!-- AUTO:BANDEAU:START -->
> Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'**optimisation d'hyperparamètres** au design *define-by-run* : l'espace de
recherche se déclare dynamiquement dans le code (`trial.suggest_float`, `suggest_int`,
`suggest_categorical`), ce qui autorise les espaces conditionnels et les boucles. Le moteur
combine **recherche bayésienne** — TPE par défaut, GP, CMA-ES — et **pruning**, l'arrêt précoce
des essais non prometteurs par MedianPruner, HyperbandPruner ou SuccessiveHalving. Le pruning
suppose une métrique **rapportée par étapes** (`trial.report` puis `should_prune`) : un
entraînement opaque en un seul bloc n'en bénéficie pas. La parallélisation passe par un
**storage partagé** (SQLite, PostgreSQL, MySQL) — sans lui, une étude vit en mémoire et meurt
avec le process. Maintenu par Preferred Networks.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Réglage coûteux où chaque entraînement est lourd : la recherche bayésienne converge en moins d'essais qu'une grille | Sans **storage persistant**, une étude en mémoire est perdue à la fin du process |
| Espace de recherche **conditionnel** ou irrégulier, mal exprimé par un produit cartésien | Le **pruning** exige une métrique rapportée par étapes : inapplicable à un entraînement opaque en un bloc |
| Élaguer tôt les essais ratés — deep learning, GBDT avec early stopping | Les plages d'échelle doivent être déclarées en **log** (`log=True`) pour les taux d'apprentissage et la régularisation, sinon l'échantillonnage est inefficace |
| Campagne distribuée sur plusieurs workers partageant un storage | Petit espace, quelques combinaisons : `GridSearchCV` / `RandomizedSearchCV` de [[Scikit-Learn]] suffisent |
| Intégrations prêtes : scikit-learn, [[XGBoost]], [[LightGBM]], [[PyTorch]] |  |

## Mise en œuvre

- Installation — `uv add optuna` ; `optuna-dashboard` en option pour le suivi en temps réel
- Point d'entrée — API Python *define-by-run* : une fonction objectif recevant un `trial`, puis `study.optimize`
- Prérequis — un storage (SQLite, PostgreSQL, MySQL) dès qu'on veut persister ou distribuer
- Exécution — single-node par défaut ; distribué en pointant plusieurs workers sur un storage commun
- Coût — gratuit, MIT, rien à héberger

## Écosystème

### Alternatives

- [[Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.
- [[Hyperopt]] — Optimisation d'hyperparamètres distribuée historique : recherche TPE (Parzen) sur espaces conditionnels, parallélisable via MongoDB/Spark ; mature mais peu maintenu.
- [[Ray Tune]] — Optimisation d'hyperparamètres distribuée sur Ray : schedulers à arrêt précoce (ASHA, PBT, HyperBand) et intégration des moteurs de recherche (Optuna, Hyperopt) à l'échelle du cluster.

## Ressources

- Documentation — https://optuna.readthedocs.io/
- Dépôt — https://github.com/optuna/optuna

## Voir aussi

- [[Optimisation d'hyperparamètres]] — la notion qu'il implémente
- [[Validation croisée]] — d'où vient le score qu'il optimise
- [[Comparatif - Optimisation d'hyperparamètres]] — ce qui départage les moteurs de réglage
