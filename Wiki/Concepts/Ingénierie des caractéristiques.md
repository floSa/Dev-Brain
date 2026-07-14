---
galaxie: wiki
type: concept
nom: Ingénierie des caractéristiques
alias: [Feature engineering, Ingénierie des variables, Feature preprocessing]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [feature-engineering]
---

# Ingénierie des caractéristiques

## Aperçu

- Construire et transformer les variables d'entrée (*features*) d'un modèle à partir des données brutes : imputer, encoder, mettre à l'échelle, combiner, sélectionner.
- Étape souvent plus déterminante que le choix de l'algorithme : un bon jeu de variables fait gagner plus qu'un modèle plus complexe sur des variables mal préparées.

## Concepts clés

### Quatre opérations de base
- **Imputer** les valeurs manquantes → [[Imputation des valeurs manquantes]].
- **Encoder** les variables catégorielles en numérique → [[Encodage des variables catégorielles]].
- **Mettre à l'échelle** les variables numériques → [[Mise à l'échelle]].
- **Sélectionner** les variables utiles → [[Sélection de variables]].

### Création vs sélection vs extraction
- **Création** : dériver de nouvelles variables (ratios, dates décomposées, agrégats, croisements).
- **Sélection** : garder un sous-ensemble des variables existantes, sans les modifier → [[Sélection de variables]].
- **Extraction** : projeter dans un nouvel espace de variables construites → [[Réduction de dimension]], [[PCA]].

### Place dans le pipeline
- Le FE s'intercale entre données brutes et entraînement. L'encapsuler dans un `Pipeline` / `ColumnTransformer` garantit que chaque transformation est *apprise sur le train* puis *appliquée* au test.

### Fuite de données (data leakage)
- Le piège central : ajuster une transformation (moyenne d'imputation, échelle, encodage cible) sur l'ensemble des données — validation comprise — donne un score optimiste irréel.
- Parade : `fit` sur le train seul, dans le pipeline, à l'intérieur de chaque pli de validation croisée.

## Les maths, simplement

- Pas de formule unique : le FE est une composition de transformations $\phi : X \mapsto X'$ apprises sur le jeu d'entraînement, puis appliquées à l'identique en validation et en production.

## En pratique

- Adapter au modèle : les arbres ignorent l'échelle et encaissent l'ordinal ; les modèles linéaires, à distance ou à gradient exigent mise à l'échelle et encodage soigné.
- Toujours `fit_transform` sur le train, `transform` sur le test — jamais l'inverse.
- Garder la traçabilité des transformations (mêmes colonnes, même ordre) entre entraînement et service.
- Outils : [[Dev/Services/Scikit-Learn|scikit-learn]] (`sklearn.pipeline`, `ColumnTransformer`, `sklearn.preprocessing`, `sklearn.impute`, `sklearn.feature_selection`) ; [[Dev/Services/Featuretools|Featuretools]] pour la FE automatisée sur données relationnelles/temporelles.

## Approches voisines & alternatives

- [[Imputation des valeurs manquantes]] — combler les trous avant de modéliser.
- [[Encodage des variables catégorielles]] — passer de la catégorie au numérique.
- [[Mise à l'échelle]] — homogénéiser les amplitudes des variables numériques.
- [[Sélection de variables]] — réduire à un sous-ensemble informatif.
- [[Réduction de dimension]], [[PCA]] — extraction de variables construites, distincte de la sélection.

## Pour aller plus loin

- Kuhn & Johnson — *Feature Engineering and Selection* (2019).
- Documentation scikit-learn — *Preprocessing data*, *Imputation*, *Feature selection*, *Pipelines and composite estimators*.
