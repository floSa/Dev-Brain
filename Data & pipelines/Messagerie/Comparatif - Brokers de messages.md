---
role: comparatif
nom: Comparatif - Brokers de messages
categorie: data/messagerie
tags: [message-broker, task-queue]
---

# Comparatif - Brokers de messages

> On tranche sur : le modèle (journal conservé ou file consommée), l'ordre et le rejeu, ce que le broker garantit à la livraison, l'exploitation minimale sur site, l'empreinte, les clients Python et la licence — dont une qui n'est pas open source.

![[Comparatif - Brokers de messages.base]]

## Ce qui départage

- [[Kafka]] — le **journal** : messages conservés et relus par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés avec, Apache-2.0. Le prix : trois contrôleurs KRaft en production, des disques dédiés, une supervision à brancher soi-même (JMX, pas d'endpoint Prometheus), et un éditeur associé, Confluent, passé sous IBM.
- [[Redpanda]] — le **journal sans JVM** : le protocole Kafka dans un binaire C++, un endpoint Prometheus natif, un opérateur Kubernetes officiel. Le prix : une licence **BSL 1.1**, source-available, dont les fonctions d'exploitation d'un cluster critique (audit, RBAC, tiered storage, rééquilibrage continu) sont Enterprise, et un seul éditeur au cœur.
- [[NATS]] — le **binaire léger** : Core NATS en mémoire et JetStream persistant dans le même serveur, des *leaf nodes* pour les sites distants, MQTT 3.1.1 natif, Apache-2.0 sous la CNCF. Le prix : pas d'écosystème d'intégration comparable à Kafka Connect, une supervision Prometheus par exporter, et un financeur dominant (Synadia, 97 % des contributions au serveur selon lui).
- [[RabbitMQ]] — la **file avec routage** : exchanges, quorum queues, priorités, AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins, plugin Prometheus livré, streams pour le rejeu. Le prix : un propriétaire, Broadcom, dont la politique de support ne couvre gratuitement que la dernière série mineure, donc une montée de version tous les quelques mois.

**Critère par critère**

**Modèle.** [[Kafka]] et [[Redpanda]] : journal partitionné et répliqué, conservé selon une rétention ou compacté par clé. [[NATS]] : Core NATS (mémoire, au plus une fois) et JetStream (streams sur fichier ou en mémoire, consumers en tirage ou en poussée). [[RabbitMQ]] : exchanges (`direct`, `fanout`, `topic`, `headers`) vers des files où le message est retiré à l'acquittement, plus des streams en journal.

**Ordre et rejeu.** [[Kafka]] et [[Redpanda]] : ordre par partition, rejeu en reculant l'offset. [[NATS]] : rejeu par consumer JetStream ; le consommateur ordonné se reconstruit sur un trou mais n'a pas d'ack. [[RabbitMQ]] : FIFO par canal, mais plusieurs consommateurs actifs peuvent désordonner à la redélivrance (file à consommateur actif unique, ou stream, pour l'ordre) ; les streams se relisent par offset, position ou horodatage.

**Garanties de livraison.** [[Kafka]] : producteur idempotent et transactions, exactly-once dans le périmètre Kafka. [[Redpanda]] : idem, mais la partie serveur du KIP-890 n'est pas implémentée et les clients Kafka 4.x retombent sur l'ancien protocole transactionnel. [[NATS]] : au moins une fois avec JetStream, déduplication par `Nats-Msg-Id` sur deux minutes par défaut, double ack. [[RabbitMQ]] : au moins une fois par acquittement ; le dead-lettering au moins une fois n'existe que sur les quorum queues. Voir [[Architecture pilotée par les événements]] pour ce que « exactement une fois » veut dire.

**Débit et latence.** Aucune mesure indépendante n'a été relevée, et aucun chiffre officiel de latence pour les quatre. La seule revendication chiffrée lue vient de la page de comparaison de la doc de RabbitMQ, écrite par son équipe : plus de 4 millions de messages par seconde sur un stream avec regroupement, « comparable à Kafka ». À mesurer sur son matériel.

**Exploitation minimale on-prem.** [[NATS]] : un nœud suffit ; trois serveurs pour la haute disponibilité de JetStream. [[Kafka]] : un nœud pour développer, trois contrôleurs KRaft en production (le mode combiné broker et contrôleur est déconseillé en environnement critique par la doc). [[RabbitMQ]] : un nœud pour des files classiques, trois pour des quorum queues. [[Redpanda]] : trois brokers recommandés, un nœud dédié par broker, le mode développement est celui par défaut.

**Empreinte.** [[NATS]] : moins de 20 Mo de mémoire pour le serveur seul, d'après son site. [[Redpanda]] : 2 Go de mémoire par cœur et 2 Mo par réplica de partition. [[Kafka]] : la doc donne une règle plutôt qu'un plancher, mémoire de l'ordre du débit d'écriture multiplié par 30 secondes, et un exemple à 24 Go. [[RabbitMQ]] : un plafond mémoire à environ 60 % de la RAM par défaut ; les quorum queues coûtent au moins 1 Mo par 30 000 messages.

**Clients Python.** [[Kafka]] : `confluent-kafka` 2.15.1 (librdkafka), `kafka-python` 3.0.11, `aiokafka` 0.14.0. [[Redpanda]] : les mêmes, validés par l'éditeur. [[NATS]] : `nats-py` 2.16.0, asyncio. [[RabbitMQ]] : `pika` 1.4.4, `aio-pika` 10.1.0 (mainteneur individuel), `kombu`, et `rstream` pour les streams.

**Protocoles industriels.** [[NATS]] parle MQTT 3.1.1 nativement (QoS 0, 1 et 2, JetStream requis) ; [[RabbitMQ]] parle MQTT 3.1, 3.1.1 et 5.0 par plugin, sans QoS 2 ni abonnements partagés ; [[Kafka]] et [[Redpanda]] ne parlent pas MQTT (Redpanda Connect a un composant qui lit un broker MQTT : c'est une passerelle). Pour un broker dont le sujet est MQTT, voir [[Comparatif - Brokers MQTT]] et le dossier [[Données industrielles]] : MQTT et OPC UA forment un bloc à part.

**Licence.** [[Kafka]] et [[NATS]] : Apache-2.0. [[RabbitMQ]] : MPL-2.0, copyright Broadcom. [[Redpanda]] : **BSL 1.1** pour le cœur — l'usage interne d'une entreprise n'est pas visé, mais offrir Redpanda comme service à des tiers est interdit, et une ESN qui héberge un cluster pour ses clients est un cas à faire valider — et licence commerciale pour les fonctions Enterprise, avec des montées de version majeure bloquées si elles sont actives sans licence.

**Gouvernance.** [[Kafka]] : Apache Software Foundation ; Confluent a été racheté par IBM (finalisé le 2026-03-17) sans effet documenté sur le projet. [[NATS]] : CNCF, après le litige de 2025 avec Synadia, clos sans changement de licence. [[RabbitMQ]] : Broadcom. [[Redpanda]] : Redpanda Data, seule à écrire le cœur.

**La file de tâches n'est pas dans ce tableau.** [[Celery]] ne s'oppose pas aux brokers, il en emploie un : RabbitMQ et Redis sont ses brokers stables, Kafka reste expérimental chez lui. Sa vue est à part. Les alternatives Python sans fiche (RQ, Huey, Dramatiq, arq, Taskiq) sont relevées dans sa fiche.

**Pas de fiche ici**, faute d'être éprouvé pour l'on-prem ou faute de rentrer dans le plafond :

- **Apache Pulsar** — vivant (4.2.4 du 2026-08-03, commits quotidiens, Apache-2.0), mais la doc officielle demande au moins six machines en production (métadonnées, brokers, bookies), le mode autonome est réservé au développement, le pont Kafka KoP est archivé (2024-01-24) et MoP et AoP dépendent d'un seul éditeur. Disproportionné pour du on-prem solo ou en petite équipe.
- **NATS Streaming** — l'ancien étage de persistance de NATS, déprécié, dépôt archivé le 2025-12-31 : JetStream le remplace.
- **[[Redis]]** — sert aussi de file et de broker léger, mais sa fiche le range comme stockage clé-valeur ; il reste un broker possible de [[Celery]].
- **Une table [[Postgres]] avec `SKIP LOCKED`** — pas un outil, une option : voir [[Architecture pilotée par les événements]], *Quand un broker est inutile*.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Messagerie]] — le hub du dossier.
- [[Architecture pilotée par les événements]] — événement contre commande, file contre journal, garanties de livraison.
- [[Stream processing]] — traiter le flux une fois transporté.
- [[Change Data Capture (CDC)]] — produire un flux depuis le journal d'une base.
