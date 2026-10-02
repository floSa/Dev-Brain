---
role: comparatif
nom: Comparatif - Optimisation d'hyperparamètres
categorie: ml/hyperopt
tags: [hyperparameter-tuning]
---

# Comparatif - Optimisation d'hyperparamètres

> On tranche sur : une machine ou un cluster, et la façon dont le budget d'essais se coupe.

![[Comparatif - Optimisation d'hyperparamètres.base]]

## Ce qui départage

- [[Optuna]] — *define-by-run* : l'espace se déclare dans le code, boucles et conditions comprises, et le **pruning** coupe l'essai raté en cours de route — mais il exige une métrique rapportée par étapes, donc un entraînement qui n'est pas opaque.
- [[Ray Tune]] — n'implémente aucune recherche : il **enveloppe** Optuna, Hyperopt ou BayesOpt et leur ajoute le cluster, les schedulers (ASHA, HyperBand, PBT) et la reprise sur panne par checkpoint. On hérite de [[Ray]] avec.
- [[Hyperopt]] — le TPE historique, avec `SparkTrials` pour un cluster Spark déjà là ; pas de release depuis 2021, pas de pruning intra-essai, et `hp.choice` rend un **index** et non la valeur.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
