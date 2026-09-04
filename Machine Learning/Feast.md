---
role: brique
nom: Feast
alias: [feast]
pitch: "Feature store open-source (Python) : définit, matérialise et sert des features ML de façon cohérente entre entraînement (offline store) et inférence temps réel (online store), au-dessus de l'infra existante (Redis, BigQuery, Snowflake, S3…)."
categorie: ml/feature-store
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: distributed
alternatives: []
complements: []
tags: [feature-store]
url_docs: https://docs.feast.dev/
url_repo: https://github.com/feast-dev/feast
---

# Feast

<!-- AUTO:BANDEAU:START -->
> Feature store open-source (Python) : définit, matérialise et sert des features ML de façon cohérente entre entraînement (offline store) et inférence temps réel (online store), au-dessus de l'infra existante (Redis, BigQuery, Snowflake, S3…).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | open-source | self-hébergé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Le **feature store** de référence. Il résout le *train/serve skew* : les mêmes
définitions de features alimentent l'**offline store** — données historiques pour
l'entraînement et le scoring batch — et l'**online store** — faible latence pour l'inférence
temps réel —, garantissant la cohérence entre les deux, avec génération de jeux d'entraînement
*point-in-time correct*. Feast n'est **pas une base de données**, et ne **calcule pas** les
features : c'est une couche d'abstraction posée au-dessus de l'infra existante (Redis,
DynamoDB, BigQuery, Snowflake, Postgres, S3), qui stocke et sert ce que des pipelines amont ont
transformé. Créé par Willem Pienaar, Tecton en étant le principal contributeur.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Servir les **mêmes features** à l'entraînement et à l'inférence sans divergence | Feast **ne calcule pas** les features : la transformation reste à la charge de pipelines en amont → [[Featuretools]], ou des requêtes SQL |
| Inférence temps réel nécessitant des features pré-calculées à faible latence | La **matérialisation online** doit être ordonnancée et surveillée : la fraîcheur des features est à la charge de l'équipe |
| Réutiliser et partager des définitions de features entre modèles et équipes, via le registry | Volume et équipe modestes : l'infra online + offline ajoute une complexité opérationnelle non amortie |
| Génération de jeux d'entraînement **point-in-time correct**, pour éviter la fuite temporelle | La cohérence offline/online est **visée**, pas garantie : elle dépend des stores choisis et de leur configuration |
| | Plateforme managée clé en main avec transformations à la volée : il n'existe pas de service managé Feast officiel → Tecton, commercial et hors périmètre OSS |

## Mise en œuvre

- Installation — `uv add feast`
- Point d'entrée — définitions de features en Python, registry de métadonnées, puis serveur de features pour l'online
- Prérequis — un online store ([[Redis]], DynamoDB) et un offline store (BigQuery, Snowflake, [[Postgres]], Parquet/S3) déjà en place
- Exécution — self-hébergé, distribué ; le registry et un planificateur de matérialisation sont à opérer
- Coût — gratuit, Apache-2.0 ; aucun service managé officiel, le coût est celui de l'infra sous-jacente

## Écosystème

### Alternatives

- Aucune fiche du brain n'occupe la catégorie `ml/feature-store` à ce jour.
- Tecton — la plateforme managée par les contributeurs principaux, avec transformations à la volée (pas encore en fiche).

## Ressources

- Documentation — https://docs.feast.dev/
- Dépôt — https://github.com/feast-dev/feast

## Voir aussi

- [[Feature store — concept]] — la notion qu'il implémente : online/offline, point-in-time correctness, train/serve skew
- [[Featuretools]] — l'étage amont : générer les features que Feast se contente de stocker et servir
- [[Redis]] · [[Postgres]] — les stores usuels, online et offline/registry
- [[BentoML]] · [[KServe]] — l'inférence qu'il alimente en features
