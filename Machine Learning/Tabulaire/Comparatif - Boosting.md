---
role: comparatif
nom: Comparatif - Boosting
categorie: ml/tabulaire
tags: [boosting, tree-based, ensemble]
---

# Comparatif - Boosting

> On tranche sur : la nature des colonnes — catégorielles ou numériques —, le temps d'entraînement, et la taille du jeu.

![[Comparatif - Boosting.base]]

## Ce qui départage

- [[XGBoost]] — croissance **level-wise**, plus prudente donc plus lente : c'est celui qui surapprend le moins sur un petit jeu, et le seul dont le passage à l'échelle distribué (Spark, Dask, Ray, Flink) est mature.
- [[LightGBM]] — croissance **leaf-wise** plus binning par histogrammes, GOSS et EFB : le plus rapide à entraîner sur gros volumes, au prix d'un surapprentissage rapide qu'il faut borner par `num_leaves`.
- [[CatBoost]] — *ordered target encoding* et arbres symétriques : le seul à absorber les catégorielles à fort cardinal sans encodage manuel, mais plus lent que LightGBM sur des colonnes purement numériques.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
