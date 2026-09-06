---
role: brique
nom: Featuretools
alias: [featuretools, Deep Feature Synthesis, DFS]
pitch: "Ingénierie de features automatisée par Deep Feature Synthesis : empile des primitives d'agrégation et de transformation sur des données relationnelles/temporelles pour générer des centaines de variables."
categorie: ml/tabulaire
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Scikit-Learn]]"]
complements: ["[[category_encoders]]"]
tags: [feature-engineering]
url_docs: https://featuretools.alteryx.com/
url_repo: https://github.com/alteryx/featuretools
---

# Featuretools

<!-- AUTO:BANDEAU:START -->
> Ingénierie de features automatisée par Deep Feature Synthesis : empile des primitives d'agrégation et de transformation sur des données relationnelles/temporelles pour générer des centaines de variables.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Automatise la création de variables sur des données relationnelles et temporelles par **Deep
Feature Synthesis**. À partir d'un `EntitySet` — plusieurs tables liées par des relations
parent-enfant, avec leurs types logiques —, DFS empile des *primitives* d'agrégation (`mean`,
`count`, `sum`) et de transformation (`day`, `time_since`, `cum_sum`) pour dériver
automatiquement des centaines de variables ; chaque empilement ajoute une « profondeur ». Une
*cutoff time* par entité interdit aux agrégats de puiser dans le futur. Maintenue par Alteryx,
ex-Feature Labs.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Données multi-tables (clients ↔ transactions ↔ produits) où les variables utiles sont des agrégats inter-tables | Une seule table plate, sans relations : un `ColumnTransformer` de [[Scikit-Learn]] écrit à la main suffit |
| Données temporelles à agréger sans laisser le futur fuiter, via la *cutoff time* | *Cutoff time* mal réglée : elle réintroduit exactement la fuite que l'outil est censé éviter → [[Data leakage]] |
| Prototypage : générer un large jeu de candidates, puis filtrer → [[Sélection de variables]] | DFS produit beaucoup de variables redondantes : la sélection en aval n'est pas optionnelle |
| Industrialiser une logique reproductible : mêmes primitives à l'entraînement et en production | `EntitySet` mal défini (types logiques, relations) : toute la suite en dépend |
| | Volumes hors mémoire : les backends Dask et Spark ne sont que partiellement supportés |
| | Encodage catégoriel fin — Target, WoE → [[category_encoders]] |

## Mise en œuvre

- Installation — `uv add featuretools`
- Point d'entrée — API Python : construire un `EntitySet`, puis `featuretools.dfs(...)`
- Prérequis — pandas ; les backends Dask ou Spark pour des EntitySets plus gros
- Exécution — calcul en mémoire, sur une machine
- Coût — gratuit, BSD-3-Clause ; rien à héberger

## Écosystème

### Alternatives

- [[Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

### Compléments

- [[category_encoders]] — Encodeurs catégoriels compatibles scikit-learn — Target, Weight of Evidence, James-Stein, CatBoost, hashing — pour les variables à forte cardinalité. Prend le relais sur les colonnes catégorielles que DFS produit.

## Ressources

- Documentation — https://featuretools.alteryx.com/
- Dépôt — https://github.com/alteryx/featuretools

## Voir aussi

- [[Ingénierie des caractéristiques]] — la notion qu'il automatise
