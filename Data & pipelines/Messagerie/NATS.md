---
role: brique
nom: NATS
alias: [nats, NATS JetStream, JetStream, nats-server]
pitch: "Serveur de messagerie en un seul binaire Go : pub/sub et requête/réponse en mémoire (Core NATS), persistance avec rejeu, key-value et object store (JetStream), MQTT 3.1.1 natif ; serveur Apache-2.0 sous la CNCF."
categorie: data/messagerie
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Kafka]]", "[[Redpanda]]", "[[RabbitMQ]]", "[[Mosquitto]]", "[[EMQX]]"]
complements: ["[[Prometheus]]", "[[Kubernetes]]", "[[Debezium]]", "[[Kestra]]"]
tags: [message-broker, distributed, self-hosted]
url_docs: https://docs.nats.io/
url_repo: https://github.com/nats-io/nats-server
---

# NATS

<!-- AUTO:BANDEAU:START -->
> Serveur de messagerie en un seul binaire Go : pub/sub et requête/réponse en mémoire (Core NATS), persistance avec rejeu, key-value et object store (JetStream), MQTT 3.1.1 natif ; serveur Apache-2.0 sous la CNCF.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Système de messagerie à deux étages, servi par un **seul binaire Go**. **Core NATS** est un bus de
sujets hiérarchiques en mémoire : publication/abonnement, requête/réponse, files d'abonnés, avec
une livraison *au plus une fois* — un message que personne n'écoute est perdu. **JetStream**,
activé dans le même serveur, ajoute la persistance : des *streams* sur fichier ou en mémoire, des
*consumers* en tirage (*pull*) ou en poussée (*push*), la livraison *au moins une fois*, le rejeu,
une rétention par limites, par intérêt ou en file de travail, plus un stockage clé-valeur et un
stockage d'objets répliqués.

Relevé le 2026-09-30 : serveur **v2.15.0** du 2026-09-17 (des candidates 2.15.1 et 2.14.8 datent
du 2026-09-28), Apache-2.0, environ 20 800 étoiles, dernier commit du 2026-09-30. Synadia annonce
des cycles de release de six mois (billet du 2025-05-13). Statut CNCF : *incubating* depuis le
2018-03-15.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Peu de ressources et peu d'exploitation : un binaire, un fichier de configuration, un nœud suffit pour commencer | Un écosystème d'intégration prêt à l'emploi (Connect, Streams, Schema Registry) : [[Kafka]] |
| Des sites distants derrière un pare-feu, reliés à un site central : les *leaf nodes* ouvrent la connexion vers le hub | Un routage fin par files, échanges et priorités : [[RabbitMQ]] |
| Un bus de requête/réponse entre services en plus des événements durables | Un journal partitionné pensé pour conserver et relire de gros volumes, avec ses outils d'exploitation éprouvés : [[Kafka]] |
| Des capteurs MQTT 3.1.1 qui doivent rejoindre le même bus, sans passerelle séparée | MQTT 5 ou Sparkplug B : la version 5 est refusée, Sparkplug B est hors du périmètre documenté |

## Mise en œuvre

- Installation — binaire `nats-server`, image Docker ou chart Helm ; `-js` active JetStream
- Point d'entrée — protocole texte NATS sur le port 4222, WebSocket dans un écouteur distinct. Client Python : **nats-py** 2.16.0 (2026-09-16, Apache-2.0, asyncio, JetStream pris en charge)
- Prérequis — pour la haute disponibilité de JetStream : au moins 3 serveurs, en Raft, avec 3 ou 5 recommandés (le quorum est la moitié plus un). La réplication d'un stream vaut 1 par défaut, ce que la doc juge risqué en production ; un seul nœud reste possible ; sécurité : tLS, mTLS, utilisateur/mot de passe, jetons, NKeys, comptes et JWT décentralisés, *auth callout* : la doc n'en marque aucun comme payant
- Exécution — self-hébergé ; sur Kubernetes, le chart Helm `nats/nats` est officiel, et **NACK** pilote streams, consumers, key-value et object store par ressources personnalisées (CRD) ; supervision : le port de supervision 8222 sert du JSON (`/varz`, `/jsz`, `/healthz`), **sans authentification par défaut**. Il n'y a pas d'endpoint Prometheus natif : la doc passe par `prometheus-nats-exporter` (port 7777) ou `nats-surveyor`, et les tableaux Grafana sont communautaires. OpenTelemetry n'est pas mentionné
- Coût — gratuit ; la mémoire annoncée par le site est inférieure à 20 Mo pour le serveur seul

## Licence et gouvernance

- **Apache-2.0** pour le serveur et les clients, sous l'organisation GitHub `nats-io`, dont le domaine et les dépôts appartiennent à la **CNCF**. Le NATS Streaming historique est déprécié, son dépôt archivé le 2025-12-31.
- **Litige de 2025 entre Synadia et la CNCF**, résolu. En mars-avril 2025, Synadia a exigé le transfert du domaine `nats.io` et des dépôts (la CNCF dit n'avoir jamais reçu les marques, malgré un engagement écrit de 2018). Le 2025-04-25, Synadia a annoncé quitter la gouvernance CNCF et explorer la **BSL** comme licence. Le communiqué commun du 2025-05-01 y met fin : Synadia cède ses deux marques NATS à la **Linux Foundation**, domaine et dépôts restent à la CNCF sous Apache-2.0, et un éventuel fork propriétaire de Synadia devra porter un autre nom. Le 2025-05-13, Synadia a confirmé ne pas forker sous BSL. **La licence n'a jamais changé.**
- **Ce qui reste comme risque** : une dépendance à un financeur dominant. Synadia dit avoir financé environ 97 % des contributions au serveur, et la CNCF affiche un indice de santé du projet de 68/100 (« Fair »).
- **Payant chez Synadia** (produits à part, pas dans le dépôt) : console de contrôle, OIDC, KMS, RBAC, audit, FIPS, connecteurs.

## Limites à connaître

- **Core NATS ne garde rien** : un abonné lent est déconnecté par le serveur plutôt que ralenti, et le message est perdu. La durabilité vient de JetStream, pas du Core.
- **Exactly-once par construction, pas par défaut** : JetStream déduplique à la publication sur l'en-tête `Nats-Msg-Id`, dans une fenêtre de deux minutes par défaut, et propose un double ack côté consommateur. Le consommateur ordonné n'a pas d'ack et ne convient pas à un traitement « exactement une fois ».
- **MQTT, avec des bornes écrites** : version 3.1.1 seule (une connexion v5 reçoit CONNACK 1), JetStream obligatoire, serveur 2.10 ou plus. Les messages venus d'un client NATS arrivent en QoS 0 aux abonnés MQTT ; les sujets contenant espace, tabulation ou retour à la ligne sont rejetés. La doc d'avant la 2.10 disait QoS 2 non supporté, celle d'aujourd'hui le supporte.
- **Des avis de sécurité récents touchent MQTT et JWT** : sept des huit derniers avis de la page du dépôt, dans un relevé du 2026-06-29, dont deux de gravité haute sur MQTT. À lire avant d'exposer le port MQTT.
- **Adoption** : aucun chiffre officiel n'a été trouvé à la source.

## Écosystème

### Alternatives

- [[Kafka]] — Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0). — l'écosystème d'intégration (Connect, Streams) et l'ancienneté d'exploitation d'un journal partitionné, au prix de plusieurs composants.
- [[Redpanda]] — Broker compatible avec le protocole Kafka, en un seul binaire C++ sans JVM ni ZooKeeper ; cœur sous licence BSL 1.1 (source-available : offrir Redpanda comme service de streaming ou de file est interdit) et fonctions Enterprise (audit, RBAC, tiered storage, rééquilibrage continu) sous licence commerciale. — le protocole Kafka pour brancher clients et connecteurs existants, sous licence BSL.
- [[RabbitMQ]] — Broker de messages à routage riche (exchanges, files, quorum queues Raft, streams en journal), AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins ; MPL-2.0, copyright Broadcom, support communautaire limité à la dernière série. — routage par exchanges, files de travail avec acquittement, AMQP 1.0 natif.
- [[Mosquitto]] — Broker MQTT 3.1, 3.1.1 et 5.0 léger, écrit en C, sans clustering natif : bridges, TLS avec certificats clients, ACL et plugin Dynamic Security, plugin Sparkplug-aware non validé par le TCK ; EPL-2.0 ou EDL-1.0 sous la fondation Eclipse. — un broker dédié à MQTT pour un nœud d'atelier, qui accepte MQTT 5.0 là où NATS refuse la version 5, sans JetStream obligatoire.
- [[EMQX]] — Broker MQTT 3.x et 5.0 en Erlang : cluster natif, règles et intégrations de données (Kafka, bases), authentification LDAP, JWT ou X.509, Prometheus natif ; BSL 1.1 depuis la 5.9 (source-available : un seul nœud gratuit en production, le cluster exige une licence commerciale). — un cluster MQTT natif avec MQTT 5 et intégrations de données, au prix d'une licence BSL.

### Compléments

- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — pas d'endpoint natif : `prometheus-nats-exporter` ou `nats-surveyor` traduisent la supervision JSON du port 8222.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — chart Helm officiel `nats/nats` et NACK, qui pilote streams et consumers par CRD.
- [[Debezium]] — Capture de changements (CDC) par le journal de transactions : événements par ligne (avant/après) depuis Postgres, MySQL, MariaDB, SQL Server, Oracle et MongoDB, via Kafka Connect, un serveur autonome sans Kafka ou un moteur Java embarqué (Apache-2.0). — Debezium Server dispose d'un sink NATS JetStream, ce qui évite Kafka.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches. — plugin NATS de Kestra : Produce et Consume sur JetStream, Request, key-value, déclencheurs Trigger et RealtimeTrigger.

## Ressources

- Documentation — https://docs.nats.io/
- Dépôt — https://github.com/nats-io/nats-server
- Article — https://www.cncf.io/announcements/2025/05/01/cncf-and-synadia-align-on-securing-the-future-of-the-nats-io-project/

## Voir aussi

- [[Messagerie]] — le hub du dossier
- [[Comparatif - Brokers de messages]] — ce qui départage Kafka, Redpanda, NATS et RabbitMQ, et la vue à part de Celery
- [[Architecture pilotée par les événements]] — la notion : file contre journal, garanties de livraison, idempotence
