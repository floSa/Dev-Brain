---
role: hub
nom: Recherche d'hyperparamètres
alias: []
pitch: Régler un modèle en connaissant le coût d'un essai — grille, hasard, substitut bayésien, arrêt précoce, et les bibliothèques qui les exécutent.
domaines: [data-sci, ml-eng]
tags: [hyperparameter-tuning, bayesian]
---

# Recherche d'hyperparamètres

> Régler un modèle en connaissant le coût d'un essai — grille, hasard, substitut bayésien, arrêt précoce, et les bibliothèques qui les exécutent.

## Ce qu'il faut comprendre

- **Régler un hyperparamètre, c'est optimiser une boîte noire.** Pas de gradient, un score bruité (une [[Validation croisée]]), un essai qui coûte un entraînement. [[Optimisation d'hyperparamètres]] pose le problème et les stratégies de base : grille, hasard, couper tôt les essais sans promesse.
- **Le modèle de substitution est une idée à part entière.** [[Optimisation bayésienne]] détaille comment un substitut (processus gaussien, TPE) et une fonction d'acquisition choisissent l'essai suivant, et où cette idée cesse de payer — dimension élevée, variables catégorielles, budget de quelques dizaines d'essais.
- **Les bibliothèques se distinguent moins par la recherche que par ce qu'elles y ajoutent.** [[Optuna]] déclare l'espace dans le code et coupe les essais ratés ; [[Ray Tune]] n'implémente pas de recherche propre, il enveloppe les autres et apporte le cluster ; [[Hyperopt]] est le TPE historique, peu maintenu. Le détail est dans [[Comparatif - Optimisation d'hyperparamètres]].
- **Ce dossier ne minimise pas une fonction connue.** Descente de gradient, convexité, optimisation sous contrainte vivent dans le domaine Mathématiques ; ici l'objectif est inconnu et coûteux.

## Choisir

- Un défaut sur une machine, avec élagage des essais → [[Optuna]].
- Une recherche à répartir sur un cluster, avec arrêt précoce par scheduler → [[Ray Tune]].
- Un projet existant bâti sur TPE à maintenir → [[Hyperopt]].
- Comprendre quand l'optimisation bayésienne vaut mieux que le hasard → [[Optimisation bayésienne]].
- Comparer les trois sur des critères → [[Comparatif - Optimisation d'hyperparamètres]].

<!-- AUTO:START -->
### Notions
- [[Optimisation d'hyperparamètres]] — domaines : data-sci, ml-eng

### Briques
- [[Hyperopt]] — Optimisation d'hyperparamètres distribuée historique : recherche TPE (Parzen) sur espaces conditionnels, parallélisable via MongoDB/Spark ; mature mais peu maintenu.
- [[Optuna]] — Optimisation d'hyperparamètres define-by-run : recherche bayésienne (TPE, GP) et élagage des essais (Hyperband, median), parallélisable.
- [[Ray Tune]] — Optimisation d'hyperparamètres distribuée sur Ray : schedulers à arrêt précoce (ASHA, PBT, HyperBand) et intégration des moteurs de recherche (Optuna, Hyperopt) à l'échelle du cluster.

### Comparatifs
- [[Comparatif - Optimisation d'hyperparamètres]]
<!-- AUTO:END -->

## Notes
