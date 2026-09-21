---
role: brique
nom: RabbitMQ
alias: [rabbitmq, RabbitMQ Streams, Tanzu RabbitMQ]
pitch: "Broker de messages à routage riche (exchanges, files, quorum queues Raft, streams en journal), AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins ; MPL-2.0, copyright Broadcom, support communautaire limité à la dernière série."
categorie: data/messagerie
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Erlang
scaling: distributed
alternatives: ["[[Kafka]]", "[[Redpanda]]", "[[NATS]]", "[[Mosquitto]]", "[[EMQX]]"]
complements: ["[[Prometheus]]", "[[Grafana]]", "[[Kubernetes]]", "[[Debezium]]", "[[Kestra]]", "[[Celery]]"]
tags: [message-broker, distributed, self-hosted]
url_docs: https://www.rabbitmq.com/docs
url_repo: https://github.com/rabbitmq/rabbitmq-server
---

# RabbitMQ

<!-- AUTO:BANDEAU:START -->
> Broker de messages à routage riche (exchanges, files, quorum queues Raft, streams en journal), AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins ; MPL-2.0, copyright Broadcom, support communautaire limité à la dernière série.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Erlang | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Broker de messages **orienté routage**. Un producteur publie vers un *exchange* (`direct`, `fanout`,
`topic` ou `headers`) qui, selon des règles de liaison, copie le message dans une ou plusieurs
*files* ; les consommateurs y lisent avec des acquittements explicites. Le message est retiré de la
file une fois acquitté : c'est le modèle de la file de travail. Les **streams** ajoutent un
second modèle, un journal en ajout seul à consommation non destructive, relisible par offset, qui
se partitionne en *super streams* (depuis la 3.11). Les files répliquées sont des **quorum queues**
(consensus Raft) ; le miroir des files classiques est retiré depuis la 4.0.

Relevé le 2026-09-30 : **4.3.6** du 2026-09-14 (série 4.3 sortie le 2026-04-23), MPL-2.0,
environ 13 900 étoiles, dernier commit du 2026-09-30, Erlang/OTP 27 au minimum pour les dernières
versions.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un message est un **travail à faire** : file, acquittement, relance, priorités, expiration, livraison différée — ce que la doc de RabbitMQ recommande contre Kafka | Un journal durable à relire par de nombreux groupes de consommateurs, avec compaction, stockage hiérarchisé et écosystème Flink ou Spark : [[Kafka]] (c'est aussi ce que dit la doc de RabbitMQ) |
| Un routage non trivial : diffusion, motifs de sujets, en-têtes, files mortes par échange | Un seul binaire sans Erlang à opérer, ou une flotte de sites distants : [[NATS]] |
| Plusieurs protocoles sur le même broker : AMQP 0-9-1 et 1.0 natifs, MQTT (3.1, 3.1.1, 5.0) et STOMP par plugins | Un usage dont la continuité dépend de correctifs sur une série précise : le support communautaire ne couvre que la dernière série (voir *Licence*) |
| Le broker par défaut de [[Celery]], le plus documenté | Un besoin de fonctions listées comme payantes (FIPS, réplication *warm standby*, audit sur Kubernetes) |

## Mise en œuvre

- Installation — image Docker officielle (maintenue par la « Docker Community », tags 4.3.6, 4.2.9, 4.1.8, 4.0.9), paquets ou Cluster Operator sur Kubernetes. L'image de base active seulement `rabbitmq_prometheus` ; la variante `-management` active l'interface web. MQTT, STOMP et le protocole stream se demandent explicitement
- Point d'entrée — AMQP sur le port 5672. Clients Python : **pika** 1.4.4 (2026-08-06, BSD-3-Clause, le client du tutoriel officiel ; entre la 1.3.2 de 2023-05-05 et la 1.4.0 de 2026-05-06, trois ans sans version), **aio-pika** 10.1.0 (2026-09-27, Apache-2.0, asyncio, mainteneur individuel), **kombu** 5.6.2 (la couche de Celery), **rstream** 1.1.0 (2026-09-09, MIT, communautaire, pour les streams)
- Prérequis — pour une file répliquée : 3 nœuds au moins et un nombre impair de réplicas ; le watermark mémoire par défaut est d'environ 60 % de la RAM. Un nœud unique suffit pour des files classiques non répliquées
- Exécution — self-hébergé ; le **Cluster Operator** Kubernetes est développé par l'équipe RabbitMQ (MPL-2.0, dernier commit du 2026-09-29) ; supervision : plugin `rabbitmq_prometheus` livré avec la distribution (port 15692) et tableaux de bord Grafana officiels ; OpenTelemetry n'est pas mentionné par la page de supervision lue
- Coût — gratuit ; les fonctions commerciales sont dans un produit à part (voir *Licence*)

## Licence et gouvernance

- **MPL-2.0** pour le serveur et les plugins de premier niveau (quelques fichiers en Apache-2.0). La licence est restée MPL-2.0 après le changement de politique de 2024.
- **Propriétaire : Broadcom** (copyright « 2007-2026 Broadcom », via le rachat de VMware). Aucune fondation n'a été trouvée dans les sources lues.
- **Effet du rachat sur le support** — et c'est le point à connaître :
  - depuis le 2024-06-01, le support de l'équipe cœur va aux clients d'une licence commerciale, aux contributeurs actifs et aux utilisateurs qui fournissent un rapport reproductible ; les séries 3.12 et antérieures n'ont plus de correctif communautaire ;
  - depuis la 4.1.0, la série 4.0.x est réservée aux clients payants via le portail Broadcom ; les autres doivent monter en 4.1 ;
  - le fichier `COMMUNITY_SUPPORT.md` du dépôt dit que seule la dernière série mineure reçoit des correctifs pour les non-payants, hors failles critiques, et que l'équipe « n'a aucune obligation de répondre » ;
  - une série ne reçoit donc que **quelques mois** de correctifs communautaires : 4.3 du 2026-04-23 au 2026-11-30, 4.2 close depuis le 2026-07-31. Les binaires et images de la série courante restent publics.
- **Fonctions payantes** (Tanzu RabbitMQ, produit distinct) : support étendu, FIPS 140-2 pour TLS, réplication *warm standby* vers un cluster distant, *shovels* distribués, AMQP 1.0 sur WebSocket, compression intra-cluster, audit sur Kubernetes, « Stream Browser » dans l'interface.

## Limites à connaître

- **L'exploitation on-prem exige de suivre la cadence des séries** : une version qui sort du support communautaire ne reçoit plus de correctif, et la montée de version devient un chantier régulier.
- **Quorum queues : des restrictions** — pas de files non durables ni exclusives, pas de QoS global (donc pas d'autoscale de workers [[Celery]] avec elles), limite de redélivrance à 20 par défaut, priorités disponibles seulement depuis la 4.3. Leur file de lettres mortes offre l'*au moins une fois*, ce que les autres types de files n'offrent pas.
- **La persistance se demande** : publier vers une file durable ne rend pas le message persistant, il faut marquer le message.
- **Les streams ne sont pas Kafka** : une stream est unitaire (le partitionnement passe par les super streams), et le protocole binaire dédié est recommandé pour les performances. La page de comparaison de la doc vient de l'équipe RabbitMQ et le dit : « commencer avec RabbitMQ, ajouter Kafka pour la compaction de log, le stockage hiérarchisé ou Kafka Streams ».
- **MQTT par plugin, avec des bornes écrites** : MQTT 3.1, 3.1.1 et 5.0 (la 5.0 depuis la 3.13.0 du 2024-02-22, « avec limitations »), mais **QoS 2 non supporté**, **abonnements partagés non supportés**, et des messages retenus locaux à chaque nœud, donc non répliqués (en mémoire, ou sur disque dans la limite de 2 Go par hôte virtuel). Relevé dans la page `rabbitmq.com/docs/mqtt` le 2026-09-30. Un client MQTT 5 se connecte sans ces garanties : pour des capteurs, voir [[Comparatif - Brokers MQTT]].

## Écosystème

### Alternatives

- [[Kafka]] — Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0). — le journal partitionné à grand débit, avec compaction et stockage hiérarchisé, quand le message est un fait à conserver plutôt qu'un travail à faire.
- [[Redpanda]] — Broker compatible avec le protocole Kafka, en un seul binaire C++ sans JVM ni ZooKeeper ; cœur sous licence BSL 1.1 (source-available : offrir Redpanda comme service de streaming ou de file est interdit) et fonctions Enterprise (audit, RBAC, tiered storage, rééquilibrage continu) sous licence commerciale. — le protocole Kafka sans JVM, sous licence BSL.
- [[NATS]] — Serveur de messagerie en un seul binaire Go : pub/sub et requête/réponse en mémoire (Core NATS), persistance avec rejeu, key-value et object store (JetStream), MQTT 3.1.1 natif ; serveur Apache-2.0 sous la CNCF. — un binaire unique et un routage par sujets hiérarchiques plutôt que par exchanges et liaisons.
- [[Mosquitto]] — Broker MQTT 3.1, 3.1.1 et 5.0 léger, écrit en C, sans clustering natif : bridges, TLS avec certificats clients, ACL et plugin Dynamic Security, plugin Sparkplug-aware non validé par le TCK ; EPL-2.0 ou EDL-1.0 sous la fondation Eclipse. — un broker dédié à MQTT, quand MQTT est l'usage principal plutôt qu'un plugin d'un broker de files.
- [[EMQX]] — Broker MQTT 3.x et 5.0 en Erlang : cluster natif, règles et intégrations de données (Kafka, bases), authentification LDAP, JWT ou X.509, Prometheus natif ; BSL 1.1 depuis la 5.9 (source-available : un seul nœud gratuit en production, le cluster exige une licence commerciale). — un cluster MQTT natif avec intégrations de données, sous licence BSL, quand MQTT est l'usage principal.

### Compléments

- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — plugin `rabbitmq_prometheus` livré avec la distribution et activé dans l'image Docker de base (port 15692).
- [[Grafana]] — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud. — tableaux de bord officiels de RabbitMQ publiés sur grafana.com, alimentés par le plugin Prometheus.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — Cluster Operator officiel, développé par l'équipe RabbitMQ (MPL-2.0).
- [[Debezium]] — Capture de changements (CDC) par le journal de transactions : événements par ligne (avant/après) depuis Postgres, MySQL, MariaDB, SQL Server, Oracle et MongoDB, via Kafka Connect, un serveur autonome sans Kafka ou un moteur Java embarqué (Apache-2.0). — Debezium Server écrit vers RabbitMQ Streams ; le sink vers les files AMQP classiques n'existe pas.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches. — plugin AMQP de Kestra : Publish, Consume, création de files et d'exchanges, déclencheurs Trigger et RealtimeTrigger.
- [[Celery]] — File de tâches distribuée pour Python : des workers exécutent des fonctions asynchrones postées sur un broker (RabbitMQ, Redis, SQS), avec relances, planification (Beat) et enchaînements (canvas) ; au moins une fois, BSD-3-Clause. — broker par défaut de la doc de Celery ; les quorum queues sont supportées (`x-queue-type: quorum`) mais sans QoS global, donc sans autoscale.

## Ressources

- Documentation — https://www.rabbitmq.com/docs
- Dépôt — https://github.com/rabbitmq/rabbitmq-server
- Article — https://www.rabbitmq.com/blog/2024/05/31/new-community-support-policy
- Documentation — https://www.rabbitmq.com/docs/compare/kafka (comparaison avec Kafka)

## Voir aussi

- [[Messagerie]] — le hub du dossier
- [[Comparatif - Brokers de messages]] — ce qui départage Kafka, Redpanda, NATS et RabbitMQ, et la vue à part de Celery
- [[Architecture pilotée par les événements]] — la notion : file contre journal, garanties de livraison, idempotence
