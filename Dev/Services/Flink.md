---
galaxie: dev
type: service
nom: Flink
alias: [flink, Apache Flink]
pitch: "Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch."
categorie: data/streaming
licence_type: open-source
hosted: both
maturite: production
langage: Java
scaling: distributed
alternatives: []
remplace_par: []
status: actif
tags: [streaming, distributed]
url_docs: https://nightlies.apache.org/flink/flink-docs-stable/
url_repo: https://github.com/apache/flink
---

# Flink

## Pourquoi

Apache Flink est un moteur de **traitement de flux avec état**, distribué. Vrai streaming (un enregistrement à la fois, pas de micro-batch obligatoire), il gère l'**event-time** et les **watermarks** pour traiter correctement les événements en retard ou désordonnés, et garantit l'**exactly-once** via **checkpointing** + snapshots d'état. Modèle **unifié flux et batch**. Trois niveaux d'API : DataStream (bas niveau), Table API & SQL (déclaratif), et PyFlink (Python). Flink 2.0 (mars 2025) introduit la gestion d'état désagrégée sur système de fichiers distribué. Apache-2.0, JVM.

## Quand l'utiliser

- Pipelines temps réel à faible latence : détection de fraude, alerting, ETL / analytique streaming, CEP.
- Gros traitements **stateful** en flux (fenêtres, jointures, agrégations) avec exactly-once.
- Justesse en **event-time** sur des flux désordonnés ou avec données tardives.
- SQL sur des flux continus (Table API / Flink SQL).

## Quand NE PAS l'utiliser

- DAGs batch planifiés et leur lignage → [[Dev/Services/Airflow|Airflow]] / [[Dev/Services/Dagster|Dagster]] (orchestrateurs, pas moteurs de flux).
- Transformations légères couplées à Kafka uniquement → Kafka Streams (plus simple à opérer).
- Analytique batch sur fichiers → Spark / DuckDB.
- Petite échelle sans besoin temps réel → Flink est surdimensionné.

## Déploiement & coût

- Open-source (Apache-2.0), auto-hébergé : cluster JobManager + TaskManagers sur Kubernetes, YARN ou standalone ; state backends (RocksDB, DFS).
- Managé : Amazon Managed Service for Apache Flink, Ververica, Confluent, Decodable.
- Exploitation **lourde** : la gestion d'état et le tuning des checkpoints sont le vrai coût.

## Pièges

- L'état est le point dur : tuning RocksDB, backpressure, taille / fréquence des checkpoints.
- Event-time et watermarks subtils à régler — sources d'erreurs silencieuses sur données tardives.
- Migration 1.x → 2.0 non triviale (architecture d'état revue).
- Tuning mémoire JVM et opérations cluster exigeants.

## Alternatives

- Pas encore d'autre moteur de flux en brain. Concurrents directs hors brain : **Spark Structured Streaming** (micro-batch, écosystème Spark) et **Kafka Streams** (bibliothèque, couplée à Kafka).

## Liens

- [[Stream processing]] — le concept (Wiki) : event-time, windowing, watermarks, exactly-once.
- [[Dev/Services/Apache Iceberg|Apache Iceberg]] — cible d'écriture fréquente pour des tables de lakehouse.
- Source / sink de flux courant : Apache Kafka.
- Doc : https://nightlies.apache.org/flink/flink-docs-stable/
