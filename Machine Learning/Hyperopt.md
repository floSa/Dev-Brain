---
role: brique
nom: Hyperopt
alias: [hyperopt, TPE, tree-structured Parzen estimator]
pitch: "Optimisation d'hyperparamètres distribuée historique : recherche TPE (Parzen) sur espaces conditionnels, parallélisable via MongoDB/Spark ; mature mais peu maintenu."
categorie: ml/hyperopt
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Optuna]]", "[[Ray Tune]]"]
complements: []
tags: [hyperparameter-tuning, bayesian, distributed]
url_docs: http://hyperopt.github.io/hyperopt/
url_repo: https://github.com/hyperopt/hyperopt
---

# Hyperopt

<!-- AUTO:BANDEAU:START -->
> Optimisation d'hyperparamètres distribuée historique : recherche TPE (Parzen) sur espaces conditionnels, parallélisable via MongoDB/Spark ; mature mais peu maintenu.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

La bibliothèque **historique** d'optimisation d'hyperparamètres en Python, celle qui a
popularisé l'algorithme **TPE** (*tree-structured Parzen estimator*) : une approche bayésienne
qui modélise la densité des bons essais contre celle des mauvais, plutôt que la fonction
objectif elle-même. Les espaces de recherche s'y déclarent, y compris **conditionnels**
(`hp.choice`, `hp.uniform`, `hp.loguniform`), et les essais se parallélisent via un backend
MongoDB ou Spark (`SparkTrials`). Une particularité coûte cher à l'usage : `hp.choice` renvoie
un **index**, pas la valeur, et relire le meilleur essai demande `space_eval`. Le projet est
quasi en sommeil — dernière release 0.2.7 vers 2021 — tout en restant très présent, intégré à
Spark/Databricks et à Freqtrade.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Codebase ou tutoriels **déjà bâtis sur Hyperopt** — Spark, Databricks, Freqtrade : l'API est stable et éprouvée | **Peu maintenu** : pas de release depuis 2021, friction d'installation avec les Python et NumPy récents → [[Optuna]], successeur de facto |
| Besoin de **TPE** sur des espaces de recherche conditionnels simples à déclarer | Pas de **pruning intra-essai** : l'arrêt précoce n'est pas natif, tout essai va à son terme → [[Optuna]] |
| Parallélisation des essais via un cluster **Spark** déjà en place (`SparkTrials`) | `hp.choice` renvoie un **index** et non la valeur : erreur classique à la relecture du meilleur essai, `space_eval` obligatoire |
| | Le backend **MongoDB** du mode distribué est lourd à opérer — `SparkTrials` est souvent préférable |
| | Petit espace, quelques combinaisons : `GridSearchCV` / `RandomizedSearchCV` de [[Scikit-Learn]] suffisent |

## Mise en œuvre

- Installation — `uv add hyperopt`
- Point d'entrée — API Python : espace déclaratif (`hp.*`), `fmin` sur la fonction objectif, `space_eval` pour relire le résultat
- Prérequis — pour le distribué, un MongoDB (`MongoTrials`) ou un cluster [[Spark]] (`SparkTrials`)
- Exécution — single-node par défaut ; distribué via l'un des deux backends
- Coût — gratuit, BSD, rien à héberger ; le coût est celui de l'infra de parallélisation éventuelle

## Écosystème

### Alternatives

- [[Optuna]] — Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable.
- [[Ray Tune]] — Optimisation d'hyperparamètres distribuée sur Ray : schedulers à arrêt précoce (ASHA, PBT, HyperBand) et intégration des moteurs de recherche (Optuna, Hyperopt) à l'échelle du cluster.

## Ressources

- Documentation — http://hyperopt.github.io/hyperopt/
- Dépôt — https://github.com/hyperopt/hyperopt

## Voir aussi

- [[Optimisation d'hyperparamètres]] — la notion qu'il implémente
- [[Spark]] — le cluster qui porte `SparkTrials`
- [[Comparatif - Optimisation d'hyperparamètres]] — ce qui départage les moteurs de réglage
