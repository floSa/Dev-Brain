---
role: brique
nom: Flink
alias: [flink, Apache Flink]
pitch: "Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch."
categorie: data/streaming
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Java
scaling: distributed
alternatives: []
complements: ["[[Debezium]]", "[[Kafka]]", "[[OpenLineage]]", "[[Delta Lake]]"]
tags: [streaming, distributed]
url_docs: https://nightlies.apache.org/flink/flink-docs-stable/
url_repo: https://github.com/apache/flink
---

# Flink

<!-- AUTO:BANDEAU:START -->
> Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-06-22 |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de traitement de flux **avec état**, distribué. Vrai streaming — un enregistrement à
la fois, pas de micro-batch imposé — reposant sur deux mécanismes qui commandent tout le
reste : l'**event-time** et ses *watermarks*, qui datent un événement par son horodatage
métier et décident quand fermer une fenêtre malgré les retards ; le **checkpointing**, qui
prend un instantané de l'état et rend l'exactly-once possible. Le modèle est unifié flux et
batch, exposé à trois niveaux — DataStream (bas niveau), Table API et SQL (déclaratif),
PyFlink (Python). La version 2.0, sortie en mars 2025, désagrège la gestion d'état sur
système de fichiers distribué.

Relevé le 2026-09-30 : **2.3.0** du 2026-06-25 (opérateurs SQL `FROM_CHANGELOG` et `TO_CHANGELOG`,
contrôle des rafraîchissements de tables matérialisées, sélection adaptative de partitions contre
la contre-pression, système de fichiers S3 natif expérimental), Apache-2.0, environ 26 400
étoiles. La politique de support de la page de téléchargements : la version mineure courante et la
précédente reçoivent les correctifs critiques, et la précédente une dernière version corrective à
la sortie d'une nouvelle mineure.

**Intégration Kafka** : le connecteur officiel (`flink-connector-kafka`, 5.0.0 du 2026-06-02) cible
Flink 2.1 et 2.2 ; la documentation de la version stable dit qu'il n'existe pas encore de
connecteur pour Flink 2.3. La source valide ses offsets à la fin de chaque checkpoint, à titre de
suivi seulement : la reprise repose sur l'état du checkpoint. Le sink offre `NONE`, `AT_LEAST_ONCE`
et `EXACTLY_ONCE` (transactions Kafka, lisibles sans doublon par un consommateur `read_committed`).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Pipelines temps réel à faible latence : détection de fraude, alerting, ETL et analytique en flux, CEP | DAGs batch planifiés et leur lignage → [[Airflow]] ou [[Dagster]], qui sont des orchestrateurs, pas des moteurs de flux |
| Gros traitements stateful en flux — fenêtres, jointures, agrégations — avec exactly-once | Transformations légères couplées à Kafka seul : Kafka Streams, livré avec [[Kafka]], s'opère plus simplement |
| Justesse en event-time sur des flux désordonnés ou avec données tardives | Analytique batch sur fichiers → [[Spark]] ou [[DuckDB]] |
| SQL continu sur des flux (Table API, Flink SQL) | Petite échelle sans besoin temps réel : le moteur est surdimensionné, et son exploitation est le vrai coût |
| | L'état est le point dur : tuning RocksDB, backpressure, taille et fréquence des checkpoints |
| | Event-time et watermarks mal réglés produisent des erreurs silencieuses sur les données tardives |

## Mise en œuvre

- Installation — distribution Apache ; cluster JobManager + TaskManagers sur Kubernetes, YARN ou standalone
- Point d'entrée — API DataStream, Table API et Flink SQL, ou PyFlink
- Prérequis — une JVM et son tuning mémoire, un state backend (RocksDB, système de fichiers distribué) ; la migration 1.x → 2.0 n'est pas triviale, l'architecture d'état ayant été revue
- Exécution — self-hébergé en cluster, ou managé : Amazon Managed Service for Apache Flink, Ververica, Confluent, Decodable
- Coût — gratuit en self-host, Apache-2.0 ; le coût réel est l'exploitation — état et checkpoints — pas la licence

## Écosystème

### Alternatives

- Aucun autre moteur de flux dans le brain. Concurrents directs hors brain : **Spark Structured Streaming** (micro-batch, écosystème Spark) et **Kafka Streams** (bibliothèque livrée avec [[Kafka]], couplée à lui).

### Compléments

- [[Debezium]] — Capture de changements (CDC) par le journal de transactions : événements par ligne (avant/après) depuis Postgres, MySQL, MariaDB, SQL Server, Oracle et MongoDB, via Kafka Connect, un serveur autonome sans Kafka ou un moteur Java embarqué (Apache-2.0). — les connecteurs Flink CDC de Ververica figurent parmi les intégrations de la page des utilisateurs de Debezium.
- [[Kafka]] — Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0). — source et sink Kafka par le connecteur officiel (5.0.0 pour Flink 2.1 et 2.2, pas encore pour 2.3) ; le sink écrit en exactly-once par les transactions Kafka.
- [[OpenLineage]] — Spécification ouverte d'événements de lignage — jobs, runs, jeux de données et facettes, dont le lignage colonne — avec des clients Python, Java et Go et des intégrations Spark, Flink, dbt et Airflow ; un standard qu'un catalogue consomme, pas un catalogue (Apache-2.0, LF AI & Data). — deux implémentations : Flink 1.x par `JobListener`, avec modification du code et sans Flink SQL ; Flink 2.x par les interfaces natives (FLIP-314), sans modifier le code, avec Flink SQL.
- [[Delta Lake]] — Format de table ouvert pour le lakehouse, sous la Linux Foundation : un journal de transactions `_delta_log` au-dessus de fichiers Parquet, ACID, time travel, MERGE, évolution de schéma et Change Data Feed ; implémentations Spark, Rust (delta-rs) et Delta Kernel en Apache-2.0, avec des fonctions d'optimisation propres à Databricks hors de l'open source. — connecteur de lecture et d'écriture listé par la documentation de Delta ; les notes de la 4.4.0 le disent expérimental.

## Ressources

- Documentation — https://nightlies.apache.org/flink/flink-docs-stable/
- Dépôt — https://github.com/apache/flink

## Voir aussi

- [[Stream processing]] — la notion du dossier : event-time, windowing, watermarks, exactly-once
- [[Apache Iceberg]] — cible d'écriture fréquente pour des tables de lakehouse
