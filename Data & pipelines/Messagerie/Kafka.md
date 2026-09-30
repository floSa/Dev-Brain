---
role: brique
nom: Kafka
alias: [kafka, Apache Kafka, Kafka Connect, Kafka Streams]
pitch: "Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0)."
categorie: data/messagerie
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Redpanda]]", "[[RabbitMQ]]", "[[NATS]]"]
complements: ["[[Debezium]]", "[[Flink]]", "[[Kestra]]", "[[OpenLineage]]", "[[OpenMetadata]]", "[[DataHub]]", "[[EMQX]]"]
tags: [message-broker, streaming, distributed, self-hosted]
url_docs: https://kafka.apache.org/documentation/
url_repo: https://github.com/apache/kafka
---

# Kafka

<!-- AUTO:BANDEAU:START -->
> Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de **journal d'événements distribué**. Les messages s'écrivent à la suite dans des
*topics* découpés en partitions, répliqués sur plusieurs brokers, et sont **conservés** selon une
rétention (durée, taille, ou compaction par clé) au lieu d'être supprimés à la lecture. Chaque
consommateur suit sa position (*offset*) par partition ; un groupe de consommateurs se répartit
les partitions, et relire le passé revient à reculer un offset. Le projet livre **Kafka
Connect** (connecteurs entre Kafka et d'autres systèmes) et **Kafka Streams** (traitement de flux
en bibliothèque Java). Depuis la 4.0 (2025-03-18), ZooKeeper n'existe plus : le quorum de
métadonnées est **KRaft**, porté par les contrôleurs de Kafka eux-mêmes.

Relevé le 2026-09-30 : ligne courante **4.3** (4.3.1 du 2026-06-25) ; la 4.2.2, correctif de la
ligne précédente, date du 2026-09-29. Apache-2.0, environ 33 900 étoiles, dernier commit du
2026-09-30. Cadence annoncée : trois versions par an.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un journal durable et rejouable : plusieurs consommateurs indépendants relisent les mêmes événements, et un nouveau consommateur repart du début | Une file de tâches — un message est un travail à faire, avec priorités, routage et relance : [[RabbitMQ]], ou [[Celery]] par-dessus un broker. Les *share groups* de la 4.2 (files, KIP-932) comblent une partie de l'écart |
| Un débit élevé avec ordre par clé : le partitionnement répartit la charge, l'ordre est tenu dans chaque partition | Un volume modeste et personne pour exploiter un cluster : [[NATS]] tient dans un seul binaire, et une table [[Postgres]] suffit parfois (voir la notion) |
| Un écosystème d'intégration : Kafka Connect (la capture de changements de [[Debezium]] s'y déploie « le plus souvent »), Kafka Streams, et le connecteur officiel de [[Flink]] | Un binaire unique sans JVM, avec le même protocole côté client : [[Redpanda]], au prix d'une licence BSL |
| Des garanties transactionnelles à l'intérieur de Kafka : producteur idempotent, transactions, exactly-once de Kafka Streams | Des capteurs qui parlent MQTT : Kafka n'a aucun protocole MQTT natif, une passerelle s'impose |

## Mise en œuvre

- Installation — image `apache/kafka` ou archive de la distribution ; un seul nœud suffit pour développer (`docker run -p 9092:9092 apache/kafka:latest`), plusieurs en production
- Point d'entrée — protocole binaire propre à Kafka (port 9092) et scripts en ligne de commande de la distribution. Clients Python : **confluent-kafka** 2.15.1 (2026-09-10, Apache-2.0, au-dessus de librdkafka, « recommandé pour la production » d'après son README), **kafka-python** 3.0.11 (2026-08-16) et **aiokafka** 0.14.0 (asyncio, 2026-04-29). Le dépôt kafka-python-ng est archivé depuis le 2025-07-11
- Prérequis — Java 17 pour les brokers, Connect et les outils (Java 11 pour les clients) ; 3 ou 5 contrôleurs KRaft en production (3 tolèrent une panne, 5 en tolèrent deux) ; le mode combiné broker + contrôleur est plus simple mais déconseillé en environnement critique par la doc ; disques dédiés, le débit disque étant le goulot
- Exécution — self-hébergé ; sur Kubernetes, l'opérateur usuel est Strimzi (Apache-2.0, projet CNCF *incubating*), qui n'est **pas** un projet Apache. Des offres managées existent (Confluent) ; supervision : métriques exposées en JMX ; la page de supervision de la documentation ne mentionne ni Prometheus ni OpenTelemetry, il faut donc un exporter JMX à côté. La télémétrie des clients au format OTLP est décrite dans le KIP-714
- Coût — gratuit ; l'exploitation est le prix : contrôleurs, disques, dimensionnement mémoire (la doc donne « débit d'écriture × 30 s » comme règle)

## Licence et gouvernance

- **Apache-2.0**, projet de premier niveau de l'Apache Software Foundation, dirigé par un PMC. Aucune fonction du dépôt n'est réservée à une édition payante.
- **Rachat de Confluent par IBM** : finalisé le 2026-03-17 (31 $ par action, environ 11 Md$ de valeur d'entreprise). Le communiqué d'IBM ne dit rien de la licence ni de la gouvernance de Kafka ; le projet reste sous l'ASF et sous Apache-2.0, et l'effet du rachat sur son orientation n'est documenté par aucune source primaire lue.
- **Ce qui n'est pas dans le projet** : le Schema Registry le plus répandu est celui de Confluent, sous **Confluent Community License** (les modules `client-*` et `avro-*` sont en Apache-2.0). Cette licence interdit d'offrir le logiciel comme service concurrent de celui de Confluent ; l'usage interne est libre.

## Limites à connaître

- **Exactly-once = périmètre Kafka.** La garantie vaut de Kafka vers Kafka (Kafka Streams en `exactly_once_v2`, ou producteur transactionnel plus consommateur en `read_committed`). Vers une base ou une API, Kafka reste en au moins une fois : le consommateur doit être idempotent.
- **L'ordre n'existe que par partition**, et le nombre de partitions borne le parallélisme d'un groupe : une partition est lue par un seul consommateur du groupe à la fois.
- **Pas de file de lettres mortes dans le broker.** Kafka Connect en offre une pour ses connecteurs de sortie (`errors.deadletterqueue.topic.name`, KIP-298), vide par défaut.
- **ZooKeeper est retiré** : toute grappe existante doit migrer vers KRaft avant la 4.x, la 3.9 étant recommandée comme étape.
- **Le connecteur Flink prend du retard** : le dernier (5.0.0, 2026-06-02) cible Flink 2.1 et 2.2, et la documentation de Flink 2.3 dit qu'aucun connecteur n'existe encore pour cette version.
- **« Plus de 80 % du Fortune 100 »** est l'affirmation de la page d'accueil du projet, sans source citée : à lire comme un ordre de grandeur, pas une mesure.

## Écosystème

### Alternatives

- [[Redpanda]] — Broker compatible avec le protocole Kafka, en un seul binaire C++ sans JVM ni ZooKeeper ; cœur sous licence BSL 1.1 (source-available : offrir Redpanda comme service de streaming ou de file est interdit) et fonctions Enterprise (audit, RBAC, tiered storage, rééquilibrage continu) sous licence commerciale. — même protocole côté client et un seul binaire sans JVM, mais licence BSL et fonctions d'exploitation (audit, RBAC, tiered storage, rééquilibrage continu) réservées à l'édition payante.
- [[RabbitMQ]] — Broker de messages à routage riche (exchanges, files, quorum queues Raft, streams en journal), AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins ; MPL-2.0, copyright Broadcom, support communautaire limité à la dernière série. — ses streams offrent un journal rejouable, mais son point fort reste la file avec routage, priorités et acquittements ; la doc de RabbitMQ renvoie elle-même vers Kafka pour la compaction de log, le stockage hiérarchisé et l'écosystème Flink.
- [[NATS]] — Serveur de messagerie en un seul binaire Go : pub/sub et requête/réponse en mémoire (Core NATS), persistance avec rejeu, key-value et object store (JetStream), MQTT 3.1.1 natif ; serveur Apache-2.0 sous la CNCF. — JetStream apporte persistance et rejeu dans un binaire unique, sans Kafka Connect ni Kafka Streams.

### Compléments

- [[Debezium]] — Capture de changements (CDC) par le journal de transactions : événements par ligne (avant/après) depuis Postgres, MySQL, MariaDB, SQL Server, Oracle et MongoDB, via Kafka Connect, un serveur autonome sans Kafka ou un moteur Java embarqué (Apache-2.0). — Kafka Connect est le mode de déploiement le plus courant de Debezium (« most commonly », d'après sa doc d'architecture) : les connecteurs Debezium y tournent.
- [[Flink]] — Moteur de traitement de flux stateful et distribué : exactly-once par checkpointing, sémantique d'event-time avec watermarks, API DataStream / Table / SQL et PyFlink ; traitement unifié flux et batch. — connecteur officiel Kafka pour Flink (5.0.0, pour Flink 2.1 et 2.2 ; aucun connecteur encore pour Flink 2.3), avec écriture exactly-once par les transactions Kafka.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches. — plugin Kafka de Kestra : tâches Produce et Consume, déclencheurs à l'interrogation ou en temps réel ; Kafka comme backend de Kestra est réservé à l'édition Enterprise.
- [[OpenLineage]] — Spécification ouverte d'événements de lignage — jobs, runs, jeux de données et facettes, dont le lignage colonne — avec des clients Python, Java et Go et des intégrations Spark, Flink, dbt et Airflow ; un standard qu'un catalogue consomme, pas un catalogue (Apache-2.0, LF AI & Data). — transport d'événements de lignage côté client (`openlineage-python[kafka]`).
- [[OpenMetadata]] — Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate). — connecteur de messagerie listé ; canal de réception du connecteur OpenLineage. Le serveur n'en dépend pas.
- [[DataHub]] — Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud). — composant obligatoire : bus des événements de métadonnées, avec un registre de schémas.
- [[EMQX]] — Broker MQTT 3.x et 5.0 en Erlang : cluster natif, règles et intégrations de données (Kafka, bases), authentification LDAP, JWT ou X.509, Prometheus natif ; BSL 1.1 depuis la 5.9 (source-available : un seul nœud gratuit en production, le cluster exige une licence commerciale). — pont Kafka intégré à EMQX : les messages MQTT des capteurs sont produits vers Kafka, qui n'a aucun protocole MQTT natif.

## Ressources

- Documentation — https://kafka.apache.org/documentation/
- Dépôt — https://github.com/apache/kafka
- Documentation — https://kafka.apache.org/community/downloads/ (téléchargements et versions)

## Voir aussi

- [[Messagerie]] — le hub du dossier
- [[Comparatif - Brokers de messages]] — ce qui départage Kafka, Redpanda, NATS et RabbitMQ, et la vue à part de Celery
- [[Architecture pilotée par les événements]] — la notion : file contre journal, garanties de livraison, idempotence
