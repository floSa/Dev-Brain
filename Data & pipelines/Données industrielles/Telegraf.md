---
role: brique
nom: Telegraf
alias: [InfluxData Telegraf, agent Telegraf, telegraf.conf]
pitch: "Agent de collecte en Go, binaire statique configuré en TOML : entrées OPC UA (interrogation et abonnements), Modbus, S7 et MQTT, sorties vers InfluxDB, PostgreSQL/TimescaleDB, Prometheus et Kafka ; MIT sous InfluxData, tampon disque encore expérimental."
categorie: data/industrie
famille: cli
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[Node-RED]]"]
complements: ["[[Mosquitto]]", "[[InfluxDB]]", "[[TimescaleDB]]", "[[Prometheus]]"]
tags: [iiot, metrics, data-ingestion, opc-ua, mqtt]
url_docs: https://docs.influxdata.com/telegraf/v1/
url_repo: https://github.com/influxdata/telegraf
---

# Telegraf

<!-- AUTO:BANDEAU:START -->
> Agent de collecte en Go, binaire statique configuré en TOML : entrées OPC UA (interrogation et abonnements), Modbus, S7 et MQTT, sorties vers InfluxDB, PostgreSQL/TimescaleDB, Prometheus et Kafka ; MIT sous InfluxData, tampon disque encore expérimental.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Agent de collecte d'**InfluxData**, écrit en Go. Un binaire statique lit un fichier TOML où l'on déclare
quatre sortes de plug-ins : des **entrées** (`inputs`, qui lisent une source), des **processeurs** et des
**agrégateurs** (qui transforment ou résument au passage) et des **sorties** (`outputs`, qui écrivent vers
une destination). Chaque plug-in peut être déclaré plusieurs fois, et chaque instance tourne
indépendamment. Le nom vient de la pile TICK, mais l'agent n'impose aucune base : les sorties couvrent
InfluxDB, PostgreSQL, Prometheus, Kafka, MQTT, NATS, OpenTelemetry, HTTP et des dizaines d'autres.

Pour l'atelier, ce sont les entrées qui comptent : `inputs.opcua` (interrogation périodique),
`inputs.opcua_listener` (abonnements), `inputs.modbus` (TCP, RTU sur TCP, ASCII, série RS485/RS232),
`inputs.s7comm` (Siemens S7-300 à S7-1500) et `inputs.mqtt_consumer`. Une passerelle d'atelier
s'écrit donc **sans code**, par configuration — là où [[Node-RED]] la dessine en flux et [[asyncua]]
l'écrit en Python.

Relevé le 2026-10-01 : **v1.40.1** du 2026-09-21 (1.40.0 le 2026-09-07), 17 842 étoiles, dernier commit
du 2026-09-30, dépôt créé en 2015 et non archivé. Rythme observé dans le CHANGELOG : une version
mineure environ tous les trois mois, des correctifs toutes les trois à quatre semaines.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Collecter périodiquement des variables OPC UA, des registres Modbus ou des topics MQTT et les écrire dans une base de séries, sans développer | Une logique de flux riche (aiguillage, règles métier, interface pour les automaticiens) : [[Node-RED]] |
| Un seul binaire à poser sur un PC industriel ou une passerelle, sans Node.js ni Python | Lire de l'OPC UA depuis du code Python déjà en place, avec appels de méthodes ou historique : [[asyncua]] |
| Exposer les valeurs à [[Prometheus]] (`outputs.prometheus_client`) ou les pousser vers [[Kafka]], depuis la même configuration | Un serveur OPC UA à héberger, ou un client à embarquer dans un produit en C : [[open62541]] |
| Écrire vers [[TimescaleDB]] avec création automatique des tables (`outputs.postgresql`) | Une coupure réseau longue sans perte tolérée : le tampon par défaut est en mémoire et borné |

## Mise en œuvre

- Installation — binaire statique Go ; paquets officiels pour Debian, Fedora, RHEL, Ubuntu, macOS, Windows et FreeBSD d'après la page des plates-formes ; la liste des architectures n'est pas détaillée à cet endroit
- Point d'entrée — `telegraf --config telegraf.conf` ; `--watch-config` (`notify` ou `poll`, ce dernier imposé sous Windows) ou le signal `SIGHUP` rechargent la configuration
- Prérequis — la source et la destination accessibles ; pour OPC UA chiffré, un certificat client reconnu par le serveur
- Exécution — un démon par machine ; chaque sortie a son propre tampon (`metric_buffer_limit`, 10 000 métriques par défaut d'après `agent.conf`, les plus anciennes écrasées quand il est plein)
- Coût — gratuit ; Telegraf Enterprise est un forfait commercial (limites plus hautes sur Telegraf Controller, haute disponibilité, LDAP, OIDC, audit, support), sans plug-in réservé qui y soit cité

## Licence et gouvernance

- **MIT**, éditeur **InfluxData Inc.** (fichier `LICENSE`, copyright 2015-2025). `docs/LICENSE_OF_DEPENDENCIES.md` liste les licences des dépendances Go sans y faire apparaître de GPL ni de LGPL (recherche de la chaîne « GPL », 0 occurrence, le 2026-10-01).
- **Ce que permet la licence** : utiliser chez un client, embarquer dans un produit livré et le revendre, à condition de conserver la notice MIT. Pas d'obligation de publier ses propres sources. **Lecture, sans valeur juridique.**
- **Édition payante** : Telegraf Enterprise (page de documentation d'InfluxData) ajoute des limites plus hautes sur Telegraf Controller (gratuit jusqu'à 20 configurations et 100 agents), la haute disponibilité du Controller, LDAP, OIDC, la piste d'audit et le support. Ce ne sont pas des plug-ins de l'agent, et aucun plug-in réservé n'est cité sur cette page.
- **Gouvernance** : société, pas de fondation. Aucun changement de propriétaire ni de relicence trouvé, aucun avis de sécurité publié sur le dépôt au 2026-10-01 (absence d'avis, pas preuve d'absence de faille).

## Limites à connaître

- **Tampon par défaut en mémoire.** Un redémarrage perd ce qu'il contient, et un tampon plein écrase les plus anciennes mesures. Le tampon sur disque (`buffer_strategy = "disk"`) existe depuis la v1.32.0 (2024-09-09) mais le CONFIGURATION.md le dit encore *experimental*, et des correctifs de troncature, de performance et de panique l'ont touché jusqu'à la v1.39.2 (2026-07-20). Pour un atelier à réseau coupé, c'est la limite qui décide.
- **OPC UA : la politique la plus forte est Basic256Sha256.** Le README de `inputs.opcua` liste `None`, `Basic128Rsa15`, `Basic256`, `Basic256Sha256` et `auto` ; les politiques Aes128 et Aes256 plus récentes n'y figurent pas, alors qu'[[open62541]] les propose. Sans certificat configuré, un certificat auto-signé temporaire est créé à chaque démarrage et le serveur doit le ré-autoriser.
- **MQTT : pas de réglage de version en entrée.** `inputs.mqtt_consumer` n'expose aucun champ de version de protocole, alors que `outputs.mqtt` accepte 3.1.1 ou 5. À tester contre un broker qui n'accepterait que MQTT 5.
- **Pas de sortie ClickHouse dédiée.** Le répertoire `plugins/outputs` n'en contient pas ; `outputs.sql` embarque un pilote ClickHouse, mais son schéma est figé, une table par type de métrique.
- **Les plug-ins de service** (`opcua_listener`, `mqtt_consumer`) ne répondent pas toujours à `--test` et `--once` ; **aucune empreinte mémoire ni taille de binaire n'est documentée** : à mesurer sur la cible.
- **Cardinalité** : aucune page lue ne la traite. Avec `outputs.postgresql`, un tag ou un champ nouveau ajoute des colonnes ; `create_templates` et `add_column_templates` l'encadrent.

## Écosystème

### Alternatives

- [[Node-RED]] — Éditeur visuel de flux dans le navigateur, sur un runtime Node.js : nœuds MQTT, HTTP, TCP, WebSocket et Function livrés, des milliers de nœuds communautaires (OPC UA, Modbus, S7) sans revue de sécurité ; Apache-2.0 sous l'OpenJS Foundation, éditeur non protégé par défaut. — la même passerelle d'atelier, par un flux visuel que les automaticiens lisent, plutôt que par un fichier TOML sans logique de flux.
- voisin : **Vector** (MPL-2.0, Datadog, Rust) — pipeline de logs et de métriques ; aucune source industrielle (OPC UA, Modbus, S7) n'a été vérifiée ; sans fiche dans le brain.
- voisin : **Grafana Alloy** (Apache-2.0) et **OpenTelemetry Collector** (Apache-2.0) — collecteurs de télémétrie d'infrastructure et d'application ; leurs récepteurs industriels n'ont pas été vérifiés ; sans fiche dans le brain.

### Compléments

- [[Mosquitto]] — Broker MQTT 3.1, 3.1.1 et 5.0 léger, écrit en C, sans clustering natif : bridges, TLS avec certificats clients, ACL et plugin Dynamic Security, plugin Sparkplug-aware non validé par le TCK ; EPL-2.0 ou EDL-1.0 sous la fondation Eclipse. — le broker auquel `inputs.mqtt_consumer` s'abonne, ou vers lequel `outputs.mqtt` publie.
- [[InfluxDB]] — SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles. — la destination historique ; `outputs.influxdb_v3` apparaît dans le CHANGELOG de la v1.38.0.
- [[TimescaleDB]] — Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres. — `outputs.postgresql` crée les tables, avec des exemples d'hypertable et de compression dans son README.
- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — `outputs.prometheus_client` expose les mesures sur `:9273/metrics` pour qu'il vienne les lire.

## Ressources

- Documentation — https://docs.influxdata.com/telegraf/v1/
- Dépôt — https://github.com/influxdata/telegraf

## Voir aussi

- [[Données industrielles]] — le hub du dossier
- [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — la notion : ce que lisent les plug-ins OPC UA, Modbus et MQTT, et le trajet du capteur à la base de séries
- [[Comparatif - Brokers MQTT]] — les brokers auxquels s'abonne `inputs.mqtt_consumer`
- [[Kafka]] — l'autre destination courante (`outputs.kafka`, basé sur Sarama)
