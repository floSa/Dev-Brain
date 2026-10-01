---
role: brique
nom: Debezium
alias: [debezium, Debezium Server, Debezium Engine]
pitch: "Capture de changements (CDC) par le journal de transactions : événements par ligne (avant/après) depuis Postgres, MySQL, MariaDB, SQL Server, Oracle et MongoDB, via Kafka Connect, un serveur autonome sans Kafka ou un moteur Java embarqué (Apache-2.0)."
categorie: data/ingestion
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Airbyte]]"]
complements: ["[[Postgres]]", "[[MySQL]]", "[[MariaDB]]", "[[Microsoft SQL Server]]", "[[MongoDB]]", "[[Apache Iceberg]]", "[[Flink]]", "[[NATS]]", "[[RabbitMQ]]", "[[Kafka]]"]
tags: [data-ingestion, cdc, streaming, self-hosted]
url_docs: https://debezium.io/documentation/
url_repo: https://github.com/debezium/debezium
---

# Debezium

<!-- AUTO:BANDEAU:START -->
> Capture de changements (CDC) par le journal de transactions : événements par ligne (avant/après) depuis Postgres, MySQL, MariaDB, SQL Server, Oracle et MongoDB, via Kafka Connect, un serveur autonome sans Kafka ou un moteur Java embarqué (Apache-2.0).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de **capture de changements** : un connecteur lit le journal de transactions d'une base
(WAL logique de Postgres, binlog de MySQL et MariaDB, tables CDC de SQL Server, LogMiner d'Oracle,
change streams de MongoDB) et émet un événement par ligne modifiée, avec l'état avant, l'état après
et le type d'opération. Il se déploie de trois façons : connecteurs **Kafka Connect** (Kafka
obligatoire), **Debezium Server** (processus autonome, sans Kafka) ou **Debezium Engine**
(bibliothèque Java embarquée dans une application).

Relevé le 2026-09-30 : **3.7.0.Final** du 2026-09-29, Apache-2.0 (grammaires ANTLR sous MIT),
environ 13 170 étoiles, dernier commit du 2026-09-28. Le projet a rejoint la Commonhaus Foundation
(annonce du 2024-11-04).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Répliquer une base transactionnelle sans la recharger et capter les suppressions, à faible latence et sans requêter les tables | Une source sans journal accessible ou sans droit de lecture du log : le CDC par interrogation d'une colonne témoin est un repli, pas Debezium |
| Un Kafka déjà en place : les connecteurs Kafka Connect sont le mode historique | Aucun broker et aucune équipe pour l'exploiter : prendre Debezium Server, ou [[Airbyte]] qui embarque la capture |
| Aucun broker : Debezium Server écrit vers Redis, NATS, RabbitMQ Streams (puits `rabbitmqstream`, pas les files AMQP classiques), HTTP ou directement vers une base par le puits JDBC | Charger des API, des fichiers ou des bases sans journal : Debezium ne lit que les journaux de bases |
| Une base Postgres, MySQL, MariaDB, SQL Server, Oracle ou MongoDB dont on contrôle la configuration (`wal_level`, `binlog_format`) | Des transformations lourdes : les SMT de Kafka Connect ne remplacent pas un traitement de flux ([[Flink]]) |

## Mise en œuvre

- Installation — image Docker ou archive de Debezium Server, ou les plugins de connecteurs dans un cluster Kafka Connect ; le moteur embarqué est une dépendance Maven
- Point d'entrée — un fichier `application.properties` (Server) ou un JSON de connecteur posté à l'API de Kafka Connect ; un événement porte `before`, `after`, `op` (`c`, `u`, `d`, `r`) et les métadonnées de la source
- Prérequis — côté source : Postgres en `wal_level=logical` avec slot et `pgoutput` ; MySQL en `binlog_format=ROW` et `binlog_row_image=FULL` ; SQL Server 2016 SP1 ou plus avec CDC activé sur la base et sur chaque table, et SQL Server Agent démarré. Java 21 pour Server, d'après la page de la 3.7
- Exécution — **Kafka Connect** : broker Kafka et service Connect ; **Server** : un seul processus, offsets en fichier, JDBC ou Redis ; **Engine** : dans l'application, livraison au moins une fois, offsets vidés toutes les 60 s par défaut
- Coût — gratuit ; l'exploitation est le prix : un cluster Kafka et des workers Connect, ou Server seul plus la base source ; une édition produit Red Hat existe à côté du code communautaire

## Licence et gouvernance

- **Apache-2.0** (licence du dépôt ; les grammaires ANTLR du module `debezium-ddl-parser` sont sous MIT). Aucune fonction du dépôt communautaire n'est réservée à une édition payante.
- **Restriction propre à Oracle, pas à Debezium** : l'adaptateur XStream demande une licence du produit GoldenGate d'Oracle, et le support du type `JSON` d'Oracle est une fonction premium de GoldenGate. L'adaptateur LogMiner, par défaut, n'en demande pas.
- **Gouvernance** : Red Hat a porté le projet depuis 2015 ; il est passé à la Commonhaus Foundation (annonce du 2024-11-04), et le suivi des tickets a quitté Jira pour GitHub Issues le 2025-12-01. La documentation contient encore une édition produit Red Hat, où Debezium Server est en *Technology Preview*.

## Limites à connaître

- **Livraison au moins une fois** : un événement peut être rejoué après une reprise ; la cible doit appliquer les changements de façon idempotente (upsert par clé). Le puits JDBC de Debezium Server le fait par upsert et propage les suppressions.
- **Le journal est une ressource de la source** : un slot Postgres qui n'avance pas retient le WAL et peut saturer le disque de la base.
- **Connecteurs inégaux** : stables — MongoDB, MariaDB, MySQL, PostgreSQL, SQL Server, Oracle, Db2, Cassandra ; en incubation — Vitess, Spanner, Informix, CockroachDB, YashanDB, Ingres, Milvus, sujets à changements incompatibles.
- **Le puits Iceberg de Debezium Server est communautaire**, hébergé dans un autre dépôt (`memiiso/debezium-server-iceberg`).
- **Debezium ne charge pas** : il produit un flux. Le rechargement initial passe par les modes de snapshot (`initial`, `always`, `incremental`, `blocking`, `no_data`), et la destination reste à construire.

## Écosystème

### Alternatives

- [[Airbyte]] — Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes. — pour répliquer une base dans un entrepôt sans monter soi-même Debezium : son mode CDC couvre Postgres, MySQL, SQL Server et MongoDB, et embarque Debezium pour SQL Server d'après le journal de son connecteur ; la page des utilisateurs de Debezium cite Airbyte.

### Compléments

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — source par décodage logique (`pgoutput`), versions 14 à 18.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web. — source par le binlog, versions 8.0, 8.4 et 9.7.
- [[MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle. — connecteur dédié, classé stable.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche. — source par les tables CDC de SQL Server.
- [[MongoDB]] — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding. — connecteur stable.
- [[Apache Iceberg]] — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB). — cible via le puits communautaire de Debezium Server.
- [[Flink]] — Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch. — Flink CDC figure parmi les intégrations de la page des utilisateurs de Debezium.
- [[NATS]] — Serveur de messagerie en un seul binaire Go : pub/sub et requête/réponse en mémoire (Core NATS), persistance avec rejeu, key-value et object store (JetStream), MQTT 3.1.1 natif ; serveur Apache-2.0 sous la CNCF. — sink de Debezium Server : NATS JetStream.
- [[RabbitMQ]] — Broker de messages à routage riche (exchanges, files, quorum queues Raft, streams en journal), AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins ; MPL-2.0, copyright Broadcom, support communautaire limité à la dernière série. — sink de Debezium Server vers RabbitMQ Streams, pas vers les files AMQP classiques.
- [[Kafka]] — Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0). — mode Kafka Connect, le plus courant : Kafka est obligatoire ; Debezium Server sait aussi écrire vers Kafka.

## Ressources

- Documentation — https://debezium.io/documentation/
- Dépôt — https://github.com/debezium/debezium

## Voir aussi

- [[Ingestion de données]] — le hub du dossier
- [[Comparatif - Ingestion de données]] — ce qui départage Debezium, Airbyte, dlt et Apache NiFi
- [[Change Data Capture (CDC)]] — la notion dont Debezium est l'outil de référence
- [[Ingestion incrémentale et curseurs]] — le repli par curseur quand le journal n'est pas lisible
