---
role: brique
nom: Apache Iceberg
alias: [Iceberg, iceberg]
pitch: "Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB)."
categorie: data/format
famille: specification
licence_type: open-source
maturite: production
langage: Java
alternatives: []
complements: []
tags: [lakehouse, olap, schema-evolution]
url_docs: https://iceberg.apache.org/docs/latest/
url_repo: https://github.com/apache/iceberg
---

# Apache Iceberg

<!-- AUTO:BANDEAU:START -->
> Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Spécification Java | open-source | rien à exécuter | production | à jour · 2026-05-20 |
<!-- AUTO:BANDEAU:END -->

## Définition

Format de **table** ouvert, et non format de fichier : il pose une sémantique de table
au-dessus de fichiers déposés sur stockage objet. Les données vivent en Parquet, ORC ou
Avro ; à côté, une arborescence de métadonnées — snapshots, listes de manifests — décrit
l'état de la table à un instant donné. De cette indirection viennent les transactions ACID
par isolation de snapshots, le time travel, l'évolution de schéma, le partitionnement caché
et l'évolution de partitionnement. Iceberg n'exécute rien lui-même : il lui faut un moteur
pour lire ou écrire, et un catalogue pour suivre les métadonnées. Né chez Netflix ;
Databricks a racheté Tabular, fondé par ses créateurs, en 2024.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tables analytiques sur data lake exigeant ACID, écrivains concurrents et time travel | Un simple fichier, sans besoin de sémantique de table → [[Parquet]] seul |
| Faire évoluer schéma **et** partitionnement sans réécrire ni casser l'historique | Upserts et CDC intensifs sur clés primaires en flux : Apache Hudi, hors brain, est taillé pour ça |
| Donner accès au même jeu de données à plusieurs moteurs, sans verrouillage propriétaire | Maison déjà 100 % Databricks / Spark sur Delta Lake : le format de table y est en place |
| Remplacer des tables Hive vieillissantes | Transactionnel ligne à ligne, OLTP → [[Postgres]] |
| | Le catalogue est une dépendance dure et un point de migration ; la promesse « ouvert » suppose des catalogues interopérables, et en pratique il peut lier à un fournisseur |
| | Snapshots et petits fichiers s'accumulent : compaction et expiration des snapshots sont une maintenance obligatoire, pas une option |

## Mise en œuvre

- Installation — bibliothèques par langage : cœur Java, PyIceberg, Rust, Go
- Point d'entrée — aucune API propre : un moteur ([[Spark]], Trino, [[Flink]], [[DuckDB]]) lit et écrit les tables
- Prérequis — un catalogue qui suit les métadonnées (REST catalog, AWS Glue, Hive Metastore, Nessie, Polaris) et un stockage objet (S3, MinIO, HDFS) ; vérifier quelle version de spec (v1 / v2 / v3) le moteur retenu supporte
- Exécution — rien à exécuter en propre : le calcul est celui du moteur, le stockage celui de l'objet
- Coût — gratuit, Apache-2.0 ; les catalogues managés (AWS Glue, Snowflake, Databricks) sont facturés

## Écosystème

### Alternatives

- Aucun autre format de table dans le brain. Concurrents directs hors brain : **Delta Lake** (écosystème Databricks / Spark) et **Apache Hudi** (orienté upserts et CDC en flux).

## Ressources

- Documentation — https://iceberg.apache.org/docs/latest/
- Dépôt — https://github.com/apache/iceberg

## Voir aussi

- [[Partitionnement & layout de données]] — le partitionnement caché et la compaction que ce format automatise
- [[Architecture médaillon]] — le cadre où ces tables s'empilent en bronze / silver / gold
- [[Avro]] — le format des fichiers de métadonnées (manifests)
