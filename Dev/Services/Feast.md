---
galaxie: dev
type: service
nom: Feast
alias: [feast]
pitch: "Feature store open-source (Python) : définit, matérialise et sert des features ML de façon cohérente entre entraînement (offline store) et inférence temps réel (online store), au-dessus de l'infra existante (Redis, BigQuery, Snowflake, S3…)."
categorie: ml/feature-store
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: []
remplace_par: []
status: actif
tags: [feature-store]
url_docs: https://docs.feast.dev/
url_repo: https://github.com/feast-dev/feast
---

# Feast

## Pourquoi

Feast (Feature Store) est le **feature store open-source** de référence. Il résout le **train/serve skew** : les mêmes définitions de features alimentent l'**offline store** (données historiques pour l'entraînement et le scoring batch) et l'**online store** (faible latence pour l'inférence temps réel), garantissant la cohérence entre les deux. Feast n'est pas une base de données : c'est une **couche d'abstraction** posée au-dessus de l'infra existante (Redis, DynamoDB, BigQuery, Snowflake, Postgres, S3…), avec génération de jeux d'entraînement *point-in-time correct*, matérialisation planifiée et serveur de features. Apache-2.0 ; créé par Willem Pienaar, Tecton en étant le principal contributeur.

## Quand l'utiliser

- Servir les **mêmes features** à l'entraînement et à l'inférence sans divergence.
- Inférence temps réel nécessitant des features pré-calculées à faible latence (online store).
- Réutiliser et partager des définitions de features entre modèles et équipes (registry).
- Génération de jeux d'entraînement **point-in-time correct** (éviter la fuite temporelle).

## Quand NE PAS l'utiliser

- Pas d'inférence temps réel ni de réutilisation de features → un simple pipeline de feature engineering ([[Dev/Services/Featuretools|Featuretools]], requêtes SQL) suffit.
- Besoin d'une plateforme managée clé en main avec transformations à la volée → Tecton (commercial, hors périmètre OSS).
- Volume et équipe modestes : l'infra online+offline ajoute une complexité opérationnelle non amortie.

## Déploiement & coût

- Open-source (Apache-2.0), `uv add feast`. **Self-host** : pas de service managé Feast officiel.
- S'appuie sur l'infra existante : online store ([[Dev/Services/Redis|Redis]], DynamoDB…), offline store (BigQuery, Snowflake, [[Dev/Services/Postgres|Postgres]], Parquet/S3).
- Le registry (métadonnées) et un planificateur de matérialisation sont à opérer.

## Pièges

- Feast **ne calcule pas** les features : la transformation reste à la charge de pipelines en amont (il stocke et sert).
- La matérialisation online doit être ordonnancée et surveillée — la fraîcheur des features est à la charge de l'équipe.
- La cohérence offline/online est visée mais dépend des stores choisis et de leur configuration.

## Alternatives

<!-- seul service de la catégorie ml/feature-store dans le brain pour l'instant -->
- Aucune alternative en catégorie `ml/feature-store` à ce jour. Approche voisine, en amont : [[Dev/Services/Featuretools|Featuretools]] (génération automatique de features).

## Liens

- Concept implémenté : [[Feature store — concept]] (online/offline, point-in-time correctness, train/serve skew).
- Alimente l'inférence servie par : [[Dev/Services/BentoML|BentoML]], [[Dev/Services/KServe|KServe]].
- Stores : [[Dev/Services/Redis|Redis]] (online), [[Dev/Services/Postgres|Postgres]] (offline/registry).
- Doc : https://docs.feast.dev/
