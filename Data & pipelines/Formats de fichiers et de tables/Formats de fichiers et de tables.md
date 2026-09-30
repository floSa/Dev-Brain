---
role: hub
nom: Formats de fichiers et de tables
alias: [formats de données, formats de table, lakehouse]
pitch: Comment la donnée est rangée sur disque ou sur stockage objet — le format de fichier qui décide de la vitesse de lecture, le format de table posé par-dessus qui apporte transactions et time travel.
domaines: [data-eng, data-sci]
tags: [file-format, lakehouse, schema-evolution, data-versioning, columnar]
---

# Formats de fichiers et de tables

> Comment la donnée est rangée sur disque ou sur stockage objet — le format de fichier qui décide de la vitesse de lecture, le format de table posé par-dessus qui apporte transactions et time travel.

## Ce qu'il faut comprendre

- Le dossier range **deux étages** qu'on confond souvent. Le **format de fichier** dit comment des octets sont disposés : [[Parquet]] par colonnes, rapide en analytique et lent à la ligne ; [[Avro]] par lignes, adapté à l'échange et aux messages. Le **format de table** dit ce que sont des fichiers *ensemble* : [[Apache Iceberg]] et [[Delta Lake]] ajoutent des transactions, un historique et l'évolution de schéma au-dessus de fichiers Parquet, par une couche de métadonnées.
- Un format de table n'exécute rien. Il lui faut un **moteur** pour lire et écrire ([[Spark]], [[Flink]], [[DuckDB]]), un stockage — objet ou système de fichiers — et, selon le cas, un catalogue ([[Apache Iceberg]]) ou un mécanisme d'écriture concurrente sur S3 ([[Delta Lake]]).
- **Le time travel d'un format de table est un effet du format**, pas un outil posé dessus : on interroge la table à une version tant que les snapshots ou les fichiers existent, et la maintenance — expiration de snapshots, `VACUUM` — efface cette possibilité. Figer un état pour rejouer un entraînement des mois plus tard est l'affaire des outils de [[Fiabilité des données]] ([[DVC]], [[lakeFS]]), cf. [[Comparatif - Versionnage de données]].
- Le **partitionnement** et la compaction décident du coût réel de lecture, quel que soit le format : cf. [[Partitionnement & layout de données]].
- Deux formats de table, deux histoires : Iceberg se branche sur plusieurs catalogues (REST, Glue, Hive Metastore, Nessie, Polaris), Delta Lake naît autour de Spark et de Databricks et publie un protocole avec plusieurs implémentations ; le dépôt de Delta Lake porte deux propositions de convergence avec Iceberg, encore au stade de RFC.

## Choisir

- Scans analytiques sur du stockage objet → [[Parquet]].
- Échanger des colonnes en mémoire entre moteurs, sans copie ni conversion → [[Apache Arrow]] (le format en mémoire, pas un format de stockage).
- Échanger des messages ou des enregistrements à schéma versionné → [[Avro]].
- Poser une table transactionnelle sur du Parquet, lue par plusieurs moteurs → [[Apache Iceberg]].
- Poser une table transactionnelle quand le socle est Spark ou Databricks, ou lire sans JVM depuis Python → [[Delta Lake]].
- Comprendre pourquoi une lecture est lente malgré le bon format → [[Partitionnement & layout de données]].
- Figer un état de données pour reproduire un entraînement → [[Comparatif - Versionnage de données]].

<!-- AUTO:START -->
### Notions
- [[Partitionnement & layout de données]] — domaines : data-eng

### Briques
- [[Apache Arrow]] — Format colonnaire en mémoire et bibliothèques multi-langages pour échanger des données entre moteurs sans copie ni conversion : spécification, IPC, Flight, C++ et pyarrow (Apache-2.0).
- [[Apache Iceberg]] — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB).
- [[Avro]] — Format de sérialisation orienté ligne avec schéma JSON embarqué : encodage binaire compact et évolution de schéma (compatibilité ascendante / descendante) ; pivot de l'échange de données et des messages Kafka.
- [[Delta Lake]] — Format de table ouvert pour le lakehouse, sous la Linux Foundation : un journal de transactions `_delta_log` au-dessus de fichiers Parquet, ACID, time travel, MERGE, évolution de schéma et Change Data Feed ; implémentations Spark, Rust (delta-rs) et Delta Kernel en Apache-2.0, avec des fonctions d'optimisation propres à Databricks hors de l'open source.
- [[Parquet]] — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet.
<!-- AUTO:END -->
