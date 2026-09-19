---
role: brique
nom: Redpanda
alias: [redpanda, Redpanda Data, Redpanda Console, Redpanda Connect]
pitch: "Broker compatible avec le protocole Kafka, en un seul binaire C++ sans JVM ni ZooKeeper ; cœur sous licence BSL 1.1 (source-available : offrir Redpanda comme service de streaming ou de file est interdit) et fonctions Enterprise (audit, RBAC, tiered storage, rééquilibrage continu) sous licence commerciale."
categorie: data/messagerie
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Kafka]]", "[[RabbitMQ]]", "[[NATS]]"]
complements: ["[[Prometheus]]", "[[Grafana]]", "[[Kubernetes]]"]
tags: [message-broker, streaming, distributed, self-hosted]
url_docs: https://docs.redpanda.com/current/
url_repo: https://github.com/redpanda-data/redpanda
---

# Redpanda

<!-- AUTO:BANDEAU:START -->
> Broker compatible avec le protocole Kafka, en un seul binaire C++ sans JVM ni ZooKeeper ; cœur sous licence BSL 1.1 (source-available : offrir Redpanda comme service de streaming ou de file est interdit) et fonctions Enterprise (audit, RBAC, tiered storage, rééquilibrage continu) sous licence commerciale.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C++ | source-available | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Broker de streaming qui parle le **protocole Kafka** : les clients, les outils et les connecteurs
écrits pour [[Kafka]] s'y branchent sans changement. Il est réécrit en C++ sur le modèle
*thread-per-core* de Seastar : un seul binaire, ni JVM ni ZooKeeper, avec un Schema Registry et un
proxy HTTP intégrés. Le journal, les partitions, les offsets et les groupes de consommateurs
sont ceux de Kafka.

Relevé le 2026-09-30 : **v26.2.2** du 2026-08-22, environ 12 600 étoiles, dernier commit de la
branche `dev` lu au 2026-08-20. Console 3.12.0 (2026-09-16), Redpanda Connect 4.111.1
(2026-09-30).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Le protocole Kafka est exigé (clients, Kafka Connect, outils existants) mais l'exploitation d'un cluster JVM avec contrôleurs séparés est de trop | La licence ne peut pas être source-available : [[Kafka]] est en Apache-2.0 |
| Un site où l'on veut peu de composants : un binaire, une console, un outil en ligne de commande (`rpk`) | Les fonctions d'exploitation d'un cluster critique — audit, RBAC, tiered storage, rééquilibrage continu, restauration de cluster — sont attendues gratuites : elles sont Enterprise |
| Des NVMe dédiés et des nœuds à part, dont le débit par cœur compte | L'infrastructure est partagée, sur NFS ou avec peu de cœurs : le moteur suppose des ressources réservées |
| Des métriques Prometheus natives, sans exporter à ajouter | Un usage qui revend Redpanda comme service à des tiers (voir *Licence*) |

## Mise en œuvre

- Installation — paquets et images officiels ; `rpk` pilote le cluster. **Le mode développement est le mode par défaut** : `rpk redpanda mode production` puis `rpk redpanda tune all` avant toute production
- Point d'entrée — l'API Kafka (clients Python validés par Redpanda : kafka-python, confluent-kafka-python), plus la console web et l'API HTTP d'administration
- Prérequis — nœud dédié par broker, 3 brokers au moins recommandés, 4 cœurs physiques, 2 Go de mémoire par cœur et 2 Mo par réplica de partition, XFS ou ext4 (NVMe recommandé), **NFS non supporté** ; RHEL 8 ou plus, Ubuntu 20.04 ou plus
- Exécution — self-hébergé ; opérateur Kubernetes et chart Helm officiels ; supervision : endpoint Prometheus natif sur le port 9644 : `/public_metrics` (préfixe `redpanda_`) est celui à retenir, `/metrics` est un endpoint hérité à forte cardinalité ; `rpk generate grafana-dashboard` produit un tableau de bord. La documentation du broker ne mentionne pas OpenTelemetry
- Coût — gratuit dans l'édition communautaire ; les fonctions Enterprise se paient (voir *Licence*)

## Licence et gouvernance

- **Cœur : BSL 1.1** (Business Source License), dépôt `redpanda-data/redpanda`. Licence *source-available*, pas open source au sens de l'OSI. Ce qu'elle interdit, mot pour mot dans le fichier de licence : utiliser l'œuvre licenciée pour un *Streaming or Queuing Service*, défini comme une offre commerciale qui laisse des tiers (hors employés et sous-traitants individuels) accéder à ses fonctions en déclenchant, directement ou non, la création d'un topic. L'usage interne d'une entreprise n'est pas visé ; **une ESN qui héberge un cluster pour ses clients est un cas à faire valider**.
- **Conversion en Apache-2.0** : le fichier de licence du dépôt dit quatre ans après la date de release de chaque version ; la page de licences de la documentation dit quatre ans après chaque fusion de code. Les deux formulations ne coïncident pas, et la date exacte de conversion d'une version donnée n'a pas été vérifiée.
- **Fonctions Enterprise** (licence commerciale RCL, même binaire) : journal d'audit, RBAC et GBAC, OIDC, Kerberos, FIPS, autorisation du Schema Registry, tiered storage, Cloud Topics, restauration de cluster complet, remote read replicas, rééquilibrage continu, *leader pinning*, topics Iceberg. Un nouveau cluster reçoit un essai de 30 jours, prolongeable de 30 jours ; ensuite les fonctions actives passent en état restreint, et **les montées de version majeure sont bloquées** si des fonctions Enterprise sont actives sans licence. La *rack awareness* n'est pas dans le tableau des fonctions Enterprise de la page officielle.
- **Autour du cœur** : Console et opérateur sont annoncés sous BSL et RCL par leurs README (texte de licence non relu) ; Redpanda Connect (ex-Benthos, racheté en mai 2024) est en Apache-2.0 pour l'essentiel, RCL pour ses fonctions Enterprise.
- **Propriétaire** : Redpanda Data, société éditrice. Elle a racheté Benthos (2024) et Oxla (2025) ; aucun rachat de Redpanda trouvé.

## Limites à connaître

- **Compatibilité Kafka, avec exceptions documentées** : un seul mécanisme SCRAM par utilisateur ; le proxy HTTP ne gère ni topics ni ACL ; le quota `request_percentage` n'est pas supporté ; la partie serveur du KIP-890 n'est pas implémentée, et les clients Kafka 4.x retombent sur l'ancien protocole transactionnel.
- **Pas de MQTT ni d'AMQP natif.** Redpanda Connect a un composant `mqtt` qui lit un broker MQTT externe : c'est une passerelle.
- **Un écart entre l'essai et la production** : le mode développement par défaut n'applique ni le réglage du noyau ni les vérifications de production.
- **Adoption** : « des centaines d'organisations » selon la page presse de l'éditeur, sans détail ; c'est moins que l'ancienneté de Kafka, et l'éditeur reste seul mainteneur du cœur.

## Écosystème

### Alternatives

- [[Kafka]] — Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0). — la référence Apache-2.0 dont Redpanda reprend le protocole : davantage de composants à exploiter, aucune fonction réservée à une édition payante.
- [[RabbitMQ]] — Broker de messages à routage riche (exchanges, files, quorum queues Raft, streams en journal), AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins ; MPL-2.0, copyright Broadcom, support communautaire limité à la dernière série. — routage et files de travail plutôt que journal, sous MPL-2.0.
- [[NATS]] — Serveur de messagerie en un seul binaire Go : pub/sub et requête/réponse en mémoire (Core NATS), persistance avec rejeu, key-value et object store (JetStream), MQTT 3.1.1 natif ; serveur Apache-2.0 sous la CNCF. — un binaire léger sous Apache-2.0, mais un autre protocole : aucun client Kafka ne s'y branche.

### Compléments

- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — endpoint natif sur le port 9644 (`/public_metrics`, préfixe `redpanda_`).
- [[Grafana]] — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud. — `rpk generate grafana-dashboard` produit un tableau de bord depuis les métriques Prometheus.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — opérateur et chart Helm officiels de Redpanda.

## Ressources

- Documentation — https://docs.redpanda.com/current/
- Dépôt — https://github.com/redpanda-data/redpanda
- Documentation — https://docs.redpanda.com/current/get-started/licensing/overview/ (licences)

## Voir aussi

- [[Messagerie]] — le hub du dossier
- [[Comparatif - Brokers de messages]] — ce qui départage Kafka, Redpanda, NATS et RabbitMQ, et la vue à part de Celery
- [[Architecture pilotée par les événements]] — la notion : file contre journal, garanties de livraison, idempotence
