---
galaxie: dev
type: service
nom: Apache Iceberg
alias: [Iceberg, iceberg]
pitch: "Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB)."
categorie: data/lakehouse
licence_type: open-source
hosted: both
maturite: production
langage: Java
scaling: distributed
alternatives: []
remplace_par: []
status: actif
tags: [lakehouse, olap, schema-evolution]
url_docs: https://iceberg.apache.org/docs/latest/
url_repo: https://github.com/apache/iceberg
---

# Apache Iceberg

## Pourquoi

Apache Iceberg est un **format de table ouvert** (pas un format de fichier) : il ajoute une **sémantique de table** au-dessus de fichiers de données posés sur stockage objet. Les données vivent en **[[Dev/Services/Parquet|Parquet]]** (ou ORC / [[Dev/Services/Avro|Avro]]) ; une arborescence de métadonnées (snapshots, listes de manifests en Avro) décrit l'état de la table. On obtient des **transactions ACID** par isolation de snapshots, le **time travel**, l'**évolution de schéma**, le **partitionnement caché** et l'**évolution de partitionnement**. Indépendant du moteur : lu et écrit par Spark, Trino, [[Dev/Services/Flink|Flink]], Dremio, DuckDB, Snowflake, Databricks. Né chez Netflix, projet Apache de premier rang ; Databricks a racheté Tabular (fondé par les créateurs d'Iceberg) en 2024.

## Quand l'utiliser

- Tables analytiques sur data lake exigeant ACID, écrivains concurrents, time travel.
- Évolution de **schéma** et de **partitionnement** sans réécrire ni casser l'historique.
- Accès **multi-moteurs** au même jeu de données, sans verrouillage propriétaire.
- Remplacement des tables Hive vieillissantes.

## Quand NE PAS l'utiliser

- Un simple fichier sans besoin de sémantique de table → [[Dev/Services/Parquet|Parquet]] seul.
- Upserts / CDC intensifs sur clés primaires en flux → Apache Hudi peut mieux convenir.
- Maison 100 % Databricks/Spark déjà sur Delta Lake → Delta Lake.
- Transactionnel ligne à ligne (OLTP) → base relationnelle ([[Dev/Services/Postgres|Postgres]]).

## Déploiement & coût

- Spécification + bibliothèques (cœur Java, PyIceberg, Rust, Go). Gratuit (Apache-2.0).
- Dépend d'un **catalogue** qui suit les métadonnées : REST catalog, AWS Glue, Hive Metastore, Nessie, Polaris.
- Données sur S3 / MinIO / HDFS ; catalogues managés via AWS Glue, Snowflake, Databricks.
- N'est **pas un moteur** : nécessite Spark / Trino / Flink / DuckDB pour requêter.

## Pièges

- Le catalogue est une **dépendance dure** et un point de migration ; le choisir tôt.
- Snapshots et petits fichiers s'accumulent → maintenance obligatoire (compaction, expiration des snapshots).
- Versions de spec (v1 / v2 / v3) et support moteur **variables** — vérifier la compatibilité.
- La promesse « ouvert » suppose des catalogues interopérables ; en pratique le catalogue peut lier à un fournisseur.

## Alternatives

- Pas encore d'autre format de table en brain. Concurrents directs hors brain : **Delta Lake** (écosystème Databricks / Spark) et **Apache Hudi** (orienté upserts et CDC en flux).

## Liens

- [[Dev/Services/Parquet|Parquet]] — format des fichiers de données sous-jacents.
- [[Dev/Services/Avro|Avro]] — format des fichiers de métadonnées (manifests).
- [[Dev/Services/Flink|Flink]] — moteur de flux capable d'écrire des tables Iceberg.
- Doc : https://iceberg.apache.org/docs/latest/
