---
galaxie: wiki
type: concept
nom: Feature store — concept
alias: [feature store, magasin de features, online store, offline store, point-in-time correctness, train/serve skew]
categorie: concept/ml
domaines: [mlops, data-eng]
tags: [feature-store, feature-engineering]
---

# Feature store — concept

## Aperçu

- Couche qui **centralise, stocke et sert** les features ML afin qu'elles soient identiques à l'entraînement et à l'inférence — la raison d'être d'un feature store est d'éliminer le **train/serve skew**.
- Une même définition de feature alimente deux chemins : historique (offline) pour entraîner, faible latence (online) pour servir.

## Concepts clés

### Offline store vs online store
- **Offline** : grand volume historique (entrepôt, Parquet/S3) — construit les jeux d'entraînement et le scoring batch.
- **Online** : clé-valeur faible latence (Redis, DynamoDB) — sert les features pré-calculées à l'inférence temps réel.
- Le store garantit que la **même logique** remplit les deux ; la divergence entre les deux *est* le skew à éviter.

### Point-in-time correctness
- Pour construire un exemple d'entraînement, ne joindre que les valeurs de feature **connues à l'instant de l'événement** — jamais une valeur future.
- Une jointure naïve « dernière valeur connue » fait fuiter le futur dans le train → [[Data leakage]]. Le point-in-time join est la parade.

### Définition, matérialisation, registry
- **Définition** : la feature est déclarée une fois (source, entité, fenêtre d'agrégation).
- **Matérialisation** : un job calcule et pousse les valeurs vers l'online store, à fraîcheur surveillée.
- **Registry** : catalogue partagé des définitions → réutilisation entre modèles et équipes.

### Ce qu'un feature store n'est pas
- Pas un moteur de calcul : il **stocke et sert**, la transformation reste à des pipelines en amont (cf. [[Dev/Services/Feast|Feast]]).

## En pratique

- Justifié quand il y a **inférence temps réel** + besoin de cohérence train/serve + réutilisation de features entre modèles. Sinon, un pipeline de feature engineering suffit.
- Surveiller la **fraîcheur** de l'online store (un job de matérialisation en retard = features périmées servies).
- Coût opérationnel réel (online + offline + matérialisation) : à n'introduire que lorsqu'il est amorti.

## Approches voisines & alternatives

- [[Dev/Services/Feast|Feast]] — feature store open-source de référence (couche au-dessus de Redis / BigQuery / Snowflake…).
- [[Data leakage]] — ce que le point-in-time correctness empêche (fuite temporelle).
- [[Monitoring de modèle en production]] — surveille le drift des features servies par le store.
- [[Encodage des variables catégorielles]] — transformation en amont dont le store sert le résultat.

## Pour aller plus loin

- Documentation Feast — point-in-time joins, online / offline stores, matérialisation.
- Tecton, Hopsworks, Databricks Feature Store — alternatives managées (hors périmètre OSS).
