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
complements: []
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

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Pipelines temps réel à faible latence : détection de fraude, alerting, ETL et analytique en flux, CEP | DAGs batch planifiés et leur lignage → [[Airflow]] ou [[Dagster]], qui sont des orchestrateurs, pas des moteurs de flux |
| Gros traitements stateful en flux — fenêtres, jointures, agrégations — avec exactly-once | Transformations légères couplées à Kafka seul : Kafka Streams, hors brain, s'opère plus simplement |
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

- Aucun autre moteur de flux dans le brain. Concurrents directs hors brain : **Spark Structured Streaming** (micro-batch, écosystème Spark) et **Kafka Streams** (bibliothèque, couplée à Kafka).

## Ressources

- Documentation — https://nightlies.apache.org/flink/flink-docs-stable/
- Dépôt — https://github.com/apache/flink

## Voir aussi

- [[Stream processing]] — la notion du dossier : event-time, windowing, watermarks, exactly-once
- [[Apache Iceberg]] — cible d'écriture fréquente pour des tables de lakehouse
