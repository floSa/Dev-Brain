---
role: notion
nom: Architecture pilotée par les événements
alias: [event-driven architecture, EDA, architecture événementielle, pub/sub, at-least-once, exactly-once, dead letter queue, outbox pattern, idempotent consumer, contre-pression]
categorie: data/messagerie
domaines: [data-eng]
tags: [event-driven, message-broker, idempotence]
---

# Architecture pilotée par les événements

## Aperçu

- Des composants qui **réagissent à des faits publiés** au lieu de s'appeler les uns les autres : le producteur écrit « la commande 42 a été payée », il ne sait ni qui écoute ni ce qui suit. Le mot recouvre pourtant plusieurs idées distinctes : Fowler (2017) en sépare quatre — *Event Notification*, *Event-Carried State Transfer*, *Event Sourcing* et *CQRS* — et écrit que « le vrai problème est la confusion entre ces patterns ».
- Ce qu'on y gagne : le producteur n'attend plus le consommateur, et on ajoute un consommateur sans toucher au producteur. Ce qu'on y perd : le flux n'est écrit nulle part. Fowler le dit ainsi : il est difficile de voir un tel flux, car il n'est explicite dans aucun texte de programme. Le brain garde le transport dans [[Messagerie]] ; le traitement du flux est dans [[Stream processing]], la lecture du journal d'une base dans [[Change Data Capture (CDC)]] — ni l'un ni l'autre n'est répété ici.

## Concepts clés

### Événement, commande, message

- Les *Enterprise Integration Patterns* (Hohpe et Woolf) distinguent trois messages selon l'**intention**. Une **commande** (*Command Message*) invoque une procédure d'une autre application : l'expéditeur demande une action. Un **événement** (*Event Message*) notifie qu'un fait s'est produit, et son occurrence suffit à dire à l'observateur de réagir ; beaucoup d'événements sont vides. Un **document** (*Document Message*) transfère des données, et le récepteur décide quoi en faire.
- *Message* est l'enveloppe qui transporte les trois. La commande vise un destinataire, l'événement n'en connaît pas : c'est ce qui fait qu'on branche un consommateur de plus sans rien changer.
- Les mêmes pages notent que la livraison garantie compte moins pour un événement fréquent que pour une commande, et que l'expiration d'un message évite de traiter un événement périmé.

### File contre journal

- Une **file** retire le message une fois acquitté : un seul consommateur du lot le reçoit, c'est un travail à distribuer. Une **file de tâches** comme [[Celery]] est bâtie dessus, avec [[RabbitMQ]] ou [[Redis]] pour broker.
- Un **journal** conserve les messages selon une rétention et chaque consommateur suit **sa position** (l'*offset* chez [[Kafka]]) : relire le passé revient à reculer cette position, et plusieurs groupes lisent le même flux indépendamment. C'est le modèle de [[Kafka]] et de [[Redpanda]], des *streams* de [[RabbitMQ]] et de JetStream chez [[NATS]].
- La question qui départage : *le message est-il un travail à faire (file) ou un fait à conserver (journal) ?* Le détail par outil est dans [[Comparatif - Brokers de messages]].

### Garanties de livraison

- La documentation de Kafka définit trois niveaux : **au plus une fois** (des messages peuvent être perdus, jamais redélivrés), **au moins une fois** (jamais perdus, mais possiblement redélivrés), **exactement une fois** (chaque message traité une fois et une seule). Elle prévient que beaucoup de systèmes annoncent l'exactly-once de façon trompeuse.
- Tyler Treat (*You Cannot Have Exactly-Once Delivery*, 2015) argue que la **livraison** exactement une fois est impossible dans un système distribué (problème des deux généraux, résultat FLP), et qu'en pratique on la « simule » : messages idempotents, ou déduplication. Exactly-once en pratique, c'est donc *au moins une fois plus un traitement idempotent*.
- Ce que les outils proposent : Kafka, un producteur idempotent (identifiant de producteur et numéro de séquence) et des transactions, avec un périmètre **Kafka vers Kafka** — pour une autre destination, il faut la « coopération » du système cible. JetStream déduplique à la publication sur l'en-tête `Nats-Msg-Id` (fenêtre de deux minutes par défaut) et offre un double ack ; le Core NATS est au plus une fois. RabbitMQ donne de l'au moins une fois par les acquittements, et sa doc dit que les consommateurs doivent être prêts à recevoir des messages déjà vus. [[Celery]] acquitte par défaut *avant* l'exécution.

### Idempotence des consommateurs

- **Idempotent Consumer** (Chris Richardson) : enregistrer les identifiants de messages traités dans une table, clé `(subscriberId, messageId)` ; l'insertion échoue si le message a déjà été vu et la transaction est annulée. L'insertion et l'effet métier doivent partager la **même transaction**, sinon le trou revient.
- **Transactional Outbox** (Richardson) : écrire l'événement dans une table de la base **dans la même transaction** que la donnée métier, puis un relais le publie. Le relais peut publier deux fois s'il tombe après l'envoi : les consommateurs restent donc idempotents. Le *Outbox Event Router* de [[Debezium]] lit cette table par le journal de la base et route chaque ligne vers un topic, avec un en-tête d'identifiant qui sert à écarter les doublons.
- La rejouabilité d'un traitement par lots est la même propriété : cf. [[ELT vs ETL & idempotence]].

### Ordre et partitions

- Chez [[Kafka]], les messages de même clé vont dans la même partition et un consommateur les lit dans l'ordre d'écriture ; une partition n'est lue que par **un** consommateur du groupe à la fois. L'ordre n'existe donc que **par partition**, et le nombre de partitions borne le parallélisme.
- Chez [[RabbitMQ]], une file est FIFO sur un canal de publication, mais avec plusieurs consommateurs actifs « toute redélivrance peut changer l'ordre » ; pour un ordre strict, la doc oriente vers les streams ou une file à consommateur actif unique.
- Le consommateur *ordonné* de JetStream ([[NATS]]) détecte un trou et se reconstruit, mais il n'a pas d'ack : il ne convient pas à un traitement « exactement une fois ».

### Contre-pression

- Le glossaire du *Reactive Manifesto* : quand un composant n'arrive plus à suivre, le système entier doit réagir de façon sensée. *Reactive Streams* vise à échanger un flux à travers une frontière asynchrone sans forcer le récepteur à mettre en tampon une quantité arbitraire de données.
- Les brokers répondent différemment. Kafka est en **tirage** (*pull*) : un consommateur lent prend du retard puis rattrape, alors qu'en poussée il serait submergé. RabbitMQ borne les messages non acquittés par consommateur (`basic.qos`, le *prefetch*). JetStream borne par `MaxAckPending` et, en tirage, par `batch` et `expires`.
- Le Core NATS fait l'inverse : un abonné trop lent est **déconnecté** par le serveur, qui protège le système et non le consommateur. Cela ne vaut pas pour JetStream.

### Dead letter et message empoisonné

- Le *Dead Letter Channel* des EIP : déplacer un message qu'on ne sait pas livrer vers une file à part, pour l'analyser. Un **message empoisonné** est celui qui fait échouer le consommateur à chaque essai et bloquerait la file sans cela.
- RabbitMQ a un mécanisme natif (*dead letter exchanges*) avec quatre causes : rejet, expiration, longueur de file, limite de redélivrance d'une quorum queue — et seules les quorum queues offrent un dead-lettering au moins une fois. JetStream publie un avis (*advisory*) quand un message atteint `max_deliver` ; en faire une file de rebut est un montage à construire, non une fonction de la doc lue. Kafka n'a **pas** de file de rebut dans le broker : Kafka Connect en propose une pour ses connecteurs de sortie (`errors.deadletterqueue.topic.name`, KIP-298), et une file de rebut pour Kafka Streams est le sujet du KIP-1034, dont la version de livraison n'a pas été vérifiée.

### Quand un broker est inutile

- La documentation de PostgreSQL dit que `SELECT … FOR UPDATE SKIP LOCKED` « peut servir à éviter la contention de verrous avec plusieurs consommateurs qui accèdent à une table en forme de file », tout en donnant une vue incohérente des données, donc « inadaptée à un usage général ». Le patron : `DELETE … USING (SELECT … FOR UPDATE SKIP LOCKED LIMIT n) … RETURNING`, et un `ROLLBACK` remet les éléments dans la file (Christensen, Crunchy Data, 2021).
- Des projets en font une file complète : **pgmq** (licence PostgreSQL, « comme SQS mais sur Postgres », clients dans quatorze langages), **River** (Go, MPL-2.0, insertion transactionnelle avec les autres changements), **Oban** (Elixir, Apache-2.0), **procrastinate** (Python, MIT) et **PgQ** (ISC). L'atout : le travail est inséré **dans la même transaction** que la donnée, ce qui règle l'outbox sans relais.
- `LISTEN/NOTIFY` réveille les consommateurs sans les interroger, mais la doc borne la charge à 8000 octets par défaut, la file de notifications à 8 Go, ne livre qu'au commit et ne conserve rien pour un écouteur déconnecté. Un retour d'exploitation (Recall.ai, 2025, mis à jour en 2026) décrit un verrou global posé au commit qui a sérialisé les transactions ; un correctif du cœur l'aurait levé, ce qui n'a pas été vérifié.
- Un broker se justifie quand il faut **plusieurs groupes de lecteurs indépendants**, un **rejeu** sur une longue rétention, un débit que la base ne doit pas porter, ou des services sur plusieurs sites. Sinon, une table dans la base déjà exploitée est un service de moins.

## En pratique

- Commencer par nommer ce qu'on publie : **commande** (un destinataire, une action attendue) ou **événement** (un fait, aucun destinataire connu). Publier une commande sous forme d'événement cache un couplage.
- Choisir **file ou journal** avant de choisir l'outil, puis lire ses garanties réelles, pas celles de la plaquette.
- Partir d'*au moins une fois* et rendre le consommateur idempotent ; ne compter sur l'exactly-once d'un broker que dans son périmètre (Kafka vers Kafka).
- Choisir la clé de partition selon l'entité dont l'ordre compte, et accepter qu'il n'y a pas d'ordre global.
- Prévoir dès le départ la **file de rebut**, sa supervision et la façon de rejouer ce qu'elle contient.
- Mesurer le **retard** des consommateurs : c'est la première alerte d'une contre-pression mal gérée.
- Pièges : un événement porteur de trop peu d'information force chaque consommateur à rappeler le producteur ; un événement porteur de tout couple les schémas ; un flux implicite se déboguera par le traçage distribué ou pas du tout.

## Approches voisines & alternatives

- [[Stream processing]] — traiter le flux (fenêtres, event-time, état) une fois transporté.
- [[Change Data Capture (CDC)]] — produire les événements depuis le journal d'une base, sans toucher à l'application.
- [[ELT vs ETL & idempotence]] — la propriété qui rend un rejeu sans danger.
- [[Kafka]], [[Redpanda]], [[NATS]] et [[RabbitMQ]] — les brokers ; [[Celery]] — la file de tâches Python.
- [[Temporal]] — l'exécution durable, qui remplace le broker pour un appel dont il faut reprendre l'état exactement.
- [[Postgres]] — la table de file avec `SKIP LOCKED`.
- [[Debezium]] et [[Flink]] — l'outbox lue par le journal, et le traitement de ce qui est publié.
- Voir aussi : [[Données industrielles]], [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]].
- [[Programmation asynchrone en Python]] — la concurrence côté consommateur Python ; [[API REST, GraphQL et gRPC]] — le contraste requête-réponse.

## Pour aller plus loin

- Martin Fowler, *What do you mean by « Event-Driven »?*, 7 février 2017 — https://martinfowler.com/articles/201701-event-driven.html
- Gregor Hohpe et Bobby Woolf, *Enterprise Integration Patterns*, pages *Command Message*, *Event Message*, *Document Message*, *Dead Letter Channel* — https://www.enterpriseintegrationpatterns.com/patterns/messaging/
- Apache Kafka, *Design* — *Message Delivery Semantics* — https://kafka.apache.org/documentation/#design_deliverysemantics ; KIP-98, *Exactly Once Delivery and Transactional Messaging* — https://cwiki.apache.org/confluence/display/KAFKA/KIP-98+-+Exactly+Once+Delivery+and+Transactional+Messaging ; KIP-298, *Error Handling in Connect*
- Tyler Treat, *You Cannot Have Exactly-Once Delivery*, Brave New Geek, 25 mars 2015 — https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/
- Chris Richardson, *Idempotent Consumer* et *Transactional Outbox* — https://microservices.io/patterns/communication-style/idempotent-consumer.html ; https://microservices.io/patterns/data/transactional-outbox.html
- Debezium, *Outbox Event Router* — https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html
- RabbitMQ, *Reliability Guide*, *Dead Letter Exchanges*, *Consumer Prefetch* — https://www.rabbitmq.com/docs/reliability
- PostgreSQL, *SELECT — The Locking Clause* — https://www.postgresql.org/docs/current/sql-select.html ; *NOTIFY* — https://www.postgresql.org/docs/current/sql-notify.html
- David Christensen, *Message Queuing Using Native PostgreSQL*, Crunchy Data, 1er septembre 2021 — https://www.crunchydata.com/blog/message-queuing-using-native-postgresql
- Critiques : Erica Sadun (Temporal), *Event-driven systems and the truth about loosely coupled architectures*, 4 décembre 2024 — https://temporal.io/blog/event-driven-systems-and-the-truth-about-loosely-coupled-architectures (source d'un éditeur concurrent) ; Marcus Kohlberg (Encore), 4 mai 2026 — https://encore.dev/articles/event-driven-architecture (source d'un éditeur)
