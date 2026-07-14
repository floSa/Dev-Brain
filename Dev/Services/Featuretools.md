---
galaxie: dev
type: service
nom: Featuretools
alias: [featuretools, Deep Feature Synthesis, DFS]
pitch: "Ingénierie de features automatisée par Deep Feature Synthesis : empile des primitives d'agrégation et de transformation sur des données relationnelles/temporelles pour générer des centaines de variables."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Scikit-Learn|Scikit-Learn]]"]
remplace_par: []
status: actif
tags: [feature-engineering]
url_docs: https://featuretools.alteryx.com/
url_repo: https://github.com/alteryx/featuretools
---

# Featuretools

## Pourquoi

Automatise la création de variables (*feature engineering*) sur des données **relationnelles et temporelles** via l'algorithme **Deep Feature Synthesis (DFS)**. À partir d'un `EntitySet` (plusieurs tables liées par des relations parent-enfant), DFS empile des **primitives** — agrégations (`mean`, `count`, `sum`…) et transformations (`day`, `time_since`, `cum_sum`…) — pour dériver automatiquement des centaines de features sans les écrire à la main. Chaque empilement augmente la « profondeur » de la feature.

## Quand l'utiliser

- Données **multi-tables** (clients ↔ transactions ↔ produits) où les variables utiles sont des agrégats inter-tables.
- Données **temporelles** avec besoin de respecter une *cutoff time* (interdire au futur de fuiter dans les agrégats).
- Prototypage rapide : générer un large jeu de candidates puis filtrer par [[Sélection de variables]].
- Industrialiser une logique de FE reproductible (mêmes primitives train et prod).

## Quand NE PAS l'utiliser

- Une seule table plate sans relations → la FE manuelle de [[Dev/Services/Scikit-Learn|Scikit-Learn]] (`ColumnTransformer`) suffit.
- Encodage catégoriel fin (Target, WoE) → [[Dev/Services/category_encoders|category_encoders]].
- Très gros volumes hors mémoire → backends Dask/Spark (support partiel) ou calcul d'agrégats en SQL/Spark en amont.

## Déploiement & coût

- Bibliothèque Python open-source (BSD-3-Clause), `uv add featuretools` ; rien à héberger.
- Calcul en mémoire au-dessus de pandas (single-node) ; backends Dask/Spark pour des EntitySets plus gros.
- Maintenue par Alteryx (ex-Feature Labs).

## Pièges

- DFS produit beaucoup de variables redondantes → sélection / filtrage indispensable en aval.
- Mal régler la *cutoff time* réintroduit la **fuite de données** que l'outil est censé éviter.
- Définir correctement l'`EntitySet` (types logiques des colonnes, relations) conditionne toute la suite.

## Alternatives

- [[Dev/Services/Scikit-Learn|Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

## Liens

- Concept implémenté : [[Ingénierie des caractéristiques]]
- Étape aval : [[Sélection de variables]] · encodage fin : [[Dev/Services/category_encoders|category_encoders]]
- Doc : https://featuretools.alteryx.com/
