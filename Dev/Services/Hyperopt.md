---
galaxie: dev
type: service
nom: Hyperopt
alias: [hyperopt, TPE, tree-structured Parzen estimator]
pitch: "Optimisation d'hyperparamètres distribuée historique : recherche TPE (Parzen) sur espaces conditionnels, parallélisable via MongoDB/Spark ; mature mais peu maintenu."
categorie: ml/hyperopt
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Optuna|Optuna]]", "[[Dev/Services/Ray Tune|Ray Tune]]"]
remplace_par: []
status: actif
tags: [hyperparameter-tuning, bayesian, distributed]
url_docs: http://hyperopt.github.io/hyperopt/
url_repo: https://github.com/hyperopt/hyperopt
---

# Hyperopt

## Pourquoi

Bibliothèque **historique** d'optimisation d'hyperparamètres en Python, qui a popularisé l'algorithme **TPE** (*tree-structured Parzen estimator*) : une approche bayésienne qui modélise la densité des bons vs mauvais essais plutôt que la fonction objectif directement. Décrit des **espaces de recherche** déclaratifs, y compris **conditionnels** (`hp.choice`, `hp.uniform`, `hp.loguniform`), et parallélise les essais via un backend **MongoDB** ou **Spark** (`SparkTrials`). Encore très présente (intégrée à Spark/Databricks, Freqtrade…), mais le projet est **peu actif** : dernière release 0.2.7 (~2021), pas de nouvelle version depuis.

## Quand l'utiliser

- Codebase ou tutoriels **déjà bâtis sur Hyperopt** (Spark / Databricks, Freqtrade) : l'API est stable et éprouvée.
- Besoin de **TPE** sur des espaces de recherche **conditionnels** simples à déclarer.
- Parallélisation des essais via un cluster **Spark** existant (`SparkTrials`) ou MongoDB.

## Quand NE PAS l'utiliser

- Nouveau projet : préférer [[Dev/Services/Optuna|Optuna]] (API define-by-run, pruning, dashboard, maintenance active) — successeur de facto.
- HPO **distribué à grande échelle** avec schedulers avancés → [[Dev/Services/Ray Tune|Ray Tune]].
- Petit espace, quelques combinaisons → `GridSearchCV` / `RandomizedSearchCV` de [[Dev/Services/Scikit-Learn|Scikit-Learn]].
- Besoin de support actif / corrections récentes : le projet est quasi en sommeil.

## Déploiement & coût

- Bibliothèque open-source (BSD), `uv add hyperopt` ; rien à héberger pour l'usage local.
- Single-node par défaut ; **distribué** via un backend MongoDB (`MongoTrials`) ou via [[Dev/Services/Spark|Spark]] (`SparkTrials`).
- Coût = l'infra de parallélisation éventuelle ; la bibliothèque est gratuite.

## Pièges

- **Peu maintenu** : pas de release depuis ~2021, friction d'installation avec les versions récentes de Python/NumPy.
- `hp.choice` renvoie un **index**, pas la valeur : erreur classique au moment de relire le meilleur essai (`space_eval` pour récupérer la config réelle).
- Le backend **MongoDB** pour le distribué est lourd à opérer ; `SparkTrials` est souvent préférable.
- Pas de pruning intra-essai comme [[Dev/Services/Optuna|Optuna]] : l'arrêt précoce n'est pas natif.

## Alternatives

- [[Dev/Services/Optuna|Optuna]] — Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable.
- [[Dev/Services/Ray Tune|Ray Tune]] — Optimisation d'hyperparamètres distribuée sur Ray : schedulers à arrêt précoce (ASHA, PBT, HyperBand) et intégration des moteurs de recherche (Optuna, Hyperopt) à l'échelle du cluster.

## Liens

- Concept implémenté : [[Optimisation d'hyperparamètres]]
- [[Comparatif - Optimisation d'hyperparamètres]] — comparatif de la catégorie
- Peut être orchestré en distribué par [[Dev/Services/Ray Tune|Ray Tune]] ou [[Dev/Services/Spark|Spark]].
- Doc : http://hyperopt.github.io/hyperopt/
