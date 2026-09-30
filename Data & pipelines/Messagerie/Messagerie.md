---
role: hub
nom: Messagerie
alias: [messaging, brokers de messages]
pitch: Transporter des événements et des tâches entre services sans les interpréter — brokers en journal ou en file, file de tâches Python par-dessus — et savoir ce que chacun garantit à la livraison.
domaines: [data-eng, infra-ops]
tags: [message-broker, task-queue, streaming]
---

# Messagerie

> Transporter des événements et des tâches entre services sans les interpréter — brokers en journal ou en file, file de tâches Python par-dessus — et savoir ce que chacun garantit à la livraison.

## Ce qu'il faut comprendre

- Ce dossier range ce qui **transporte** des messages, pas ce qui les **traite** : fenêtres, état et agrégations relèvent de [[Stream processing]] et de [[Flink]] ; le suivi d'un graphe de tâches relève de l'[[Orchestration]]. [[Debezium]] *produit* un flux depuis une base, il ne le transporte pas.
- **Deux formes de broker, qui ne se remplacent pas toujours.** Un *journal* ([[Kafka]], [[Redpanda]]) conserve les messages et laisse chaque consommateur relire à sa position ; une *file* ([[RabbitMQ]]) retire le message une fois acquitté, et route selon des règles. [[NATS]] tient les deux dans un seul binaire (Core NATS en mémoire, JetStream persistant). Les streams de RabbitMQ et les *share groups* de Kafka 4.2 brouillent la frontière sans l'effacer.
- **[[Celery]] n'est pas un broker** : c'est une file de tâches Python qui *emploie* un broker ([[RabbitMQ]] par défaut, ou [[Redis]]). Il ne se compare pas aux brokers, il s'y branche.
- **Les licences ne sont pas les mêmes, et l'une est restrictive** : [[Kafka]] et [[NATS]] sont en Apache-2.0, [[RabbitMQ]] en MPL-2.0 (copyright Broadcom, support communautaire limité à la dernière série), [[Celery]] en BSD-3-Clause. [[Redpanda]] est sous **BSL 1.1** : source-available, offrir Redpanda comme service de streaming est interdit, et les fonctions d'exploitation d'un cluster critique (audit, RBAC, tiered storage) sont Enterprise.
- **Deux changements de propriétaire à connaître** : Confluent, l'éditeur autour de Kafka, a été racheté par IBM (finalisé le 2026-03-17) sans effet documenté sur le projet Apache ; RabbitMQ appartient à Broadcom depuis le rachat de VMware, avec le resserrement du support qui va avec. NATS a traversé en 2025 un litige entre Synadia et la CNCF, clos sans changement de licence.
- **Exploitation minimale on-prem** : [[NATS]] tient sur un nœud ; [[Kafka]] veut 3 contrôleurs KRaft en production ; [[RabbitMQ]] veut 3 nœuds pour des files répliquées ; [[Redpanda]] recommande 3 brokers dédiés. Un broker de plus est un service de plus à sauvegarder, superviser et mettre à jour.
- **Les protocoles de capteurs industriels sont ailleurs.** [[NATS]] parle MQTT 3.1.1 nativement et [[RabbitMQ]] MQTT par plugin ; [[Kafka]] et [[Redpanda]] ne le parlent pas.

## Choisir

- Un journal rejouable, à gros débit, avec l'écosystème Connect, Streams et [[Flink]] → [[Kafka]].
- Le protocole Kafka sans JVM, si la licence BSL est acceptable → [[Redpanda]].
- Un binaire unique, des sites distants reliés à un site central, des capteurs MQTT 3.1.1 → [[NATS]].
- Des files de travail avec routage, priorités et relance, ou AMQP/MQTT/STOMP → [[RabbitMQ]].
- Sortir un travail long d'une application Python → [[Celery]], avec [[RabbitMQ]] ou [[Redis]] comme broker.
- Capter les changements d'une base vers un broker → [[Debezium]].
- Traiter le flux, pas le transporter → [[Flink]].

<!-- AUTO:START -->
### Briques
- [[Celery]] — File de tâches distribuée pour Python : des workers exécutent des fonctions asynchrones postées sur un broker (RabbitMQ, Redis, SQS), avec relances, planification (Beat) et enchaînements (canvas) ; au moins une fois, BSD-3-Clause.
- [[Kafka]] — Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0).
- [[NATS]] — Serveur de messagerie en un seul binaire Go : pub/sub et requête/réponse en mémoire (Core NATS), persistance avec rejeu, key-value et object store (JetStream), MQTT 3.1.1 natif ; serveur Apache-2.0 sous la CNCF.
- [[RabbitMQ]] — Broker de messages à routage riche (exchanges, files, quorum queues Raft, streams en journal), AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins ; MPL-2.0, copyright Broadcom, support communautaire limité à la dernière série.
- [[Redpanda]] — Broker compatible avec le protocole Kafka, en un seul binaire C++ sans JVM ni ZooKeeper ; cœur sous licence BSL 1.1 (source-available : offrir Redpanda comme service de streaming ou de file est interdit) et fonctions Enterprise (audit, RBAC, tiered storage, rééquilibrage continu) sous licence commerciale.
<!-- AUTO:END -->
