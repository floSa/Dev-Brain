---
role: brique
nom: EMQX
alias: [emqx, EMQX Enterprise, EMQX Broker, EMQ X]
pitch: "Broker MQTT 3.x et 5.0 en Erlang : cluster natif, règles et intégrations de données (Kafka, bases), authentification LDAP, JWT ou X.509, Prometheus natif ; BSL 1.1 depuis la 5.9 (source-available : un seul nœud gratuit en production, le cluster exige une licence commerciale)."
categorie: data/industrie
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: Erlang
scaling: distributed
alternatives: ["[[Mosquitto]]", "[[NATS]]", "[[RabbitMQ]]"]
complements: ["[[Prometheus]]", "[[Kubernetes]]", "[[Kafka]]", "[[InfluxDB]]", "[[TimescaleDB]]"]
tags: [mqtt, message-broker, iiot, distributed, self-hosted]
url_docs: https://docs.emqx.com/en/emqx/latest/
url_repo: https://github.com/emqx/emqx
---

# EMQX

<!-- AUTO:BANDEAU:START -->
> Broker MQTT 3.x et 5.0 en Erlang : cluster natif, règles et intégrations de données (Kafka, bases), authentification LDAP, JWT ou X.509, Prometheus natif ; BSL 1.1 depuis la 5.9 (source-available : un seul nœud gratuit en production, le cluster exige une licence commerciale).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Erlang | source-available | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Broker **MQTT** écrit en Erlang/OTP par EMQ Technologies : MQTT 3.x et 5.0, y compris sur QUIC, plus
des passerelles CoAP, LwM2M, MQTT-SN et OCPP. Sa particularité est le **cluster natif** (architecture
Mria, des nœuds *core* qui portent l'état et des nœuds *replicant* qui portent les connexions), avec
pour cibles annoncées 1,5 million de connexions par nœud et 100 millions par cluster. Autour du
broker : un moteur de règles, des ponts MQTT, et des intégrations de données vers Kafka et des bases
(InfluxDB, TimescaleDB, PostgreSQL, ClickHouse : une page de doc chacune).

Relevé le 2026-09-30 : plusieurs lignes vivent en parallèle. **6.3.1** (étiquetée LTS, 2026-09-18),
**6.1.5** et **6.0.4** (2026-09-29), **5.10.5** (2026-09-17) ; 6.3.0 date du 2026-09-03 et 6.0.0 du
2025-09-30. Environ 16 800 étoiles, dernier commit du jour, 137 contributeurs, mais un seul auteur
signe 82 des 100 derniers commits.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un cluster de brokers est nécessaire et un budget de licence est acquis : connexions nombreuses, haute disponibilité | Un seul nœud suffit et la licence doit rester sans condition : [[Mosquitto]] |
| Les messages doivent finir dans Kafka, une base de séries ou PostgreSQL sans écrire la passerelle : règles et intégrations de données intégrées | Une intégration dans un produit ou une solution livrés à des tiers : la BSL exclut l'usage « hosted or embedded », à faire valider par un juriste, typiquement pour une ESN |
| MQTT 5, QUIC, mTLS, LDAP, JWT, SCRAM ou Kerberos pour authentifier les clients | Un matériel très modeste : la doc actuelle ne donne aucun minimum, et la seule mention (doc 5.1) date d'avant la BSL |
| Une supervision Prometheus native et des images Docker et Kubernetes officielles | Une licence strictement libre : seule la ligne 5.8.x reste sous Apache-2.0, et sa dernière release date du 2025-12-31 |

## Mise en œuvre

- Installation — paquets Linux (Ubuntu 22.04 et 24.04, Debian 11 à 13, amd64 et arm64), image Docker `emqx/emqx` (amd64 et arm64 ; 47 millions de téléchargements constatés le 2026-09-30) ou `emqx/emqx-enterprise`, Operator et chart Helm sur Kubernetes
- Point d'entrée — MQTT sur 1883 (TLS 8883), WebSocket sur 8083 et 8084, tableau de bord web et API REST `/api/v5/`, règles en SQL-like ; Erlang/OTP 27 pour la 5.9, 28 à partir de la 6.1
- Prérequis — un nœud seul tourne sous la licence **Community** livrée par défaut ; un cluster de plusieurs nœuds exige un fichier de licence chargé ; l'essai de 15 jours (10 000 sessions) n'est pas valable en production. Sécurité : TLS mutuel, certificats X.509, vérification CRL et OCSP, authentification par base intégrée, MySQL, PostgreSQL, MongoDB, Redis, LDAP, HTTP, JWT, PSK, SCRAM ou Kerberos ; autorisation par fichier ACL, base ou LDAP
- Exécution — self-hébergé, ou service managé EMQX Cloud ; persistance durable sur RocksDB, environ 1,5 ko par session annoncés ; Prometheus en pull ou par Pushgateway, plus OpenTelemetry (depuis la 6.3.0 le scrape demande une authentification par défaut)
- Coût — **un nœud gratuit en production**, un cluster sous licence commerciale ; pas de prix public relevé

## Licence et gouvernance

- **BSL 1.1**, lue dans le fichier `LICENSE` de `master` le 2026-09-30 : *Licensed Work* « EMQX Version 5.9.0 or later », *Licensor* EMQ Technologies, *Change License* **Apache-2.0** quatre ans après la publication de chaque version (une 5.9.0 de mai 2025 passerait donc vers mai 2029 : déduction, aucune page officielle ne donne les dates).
- **Ce que l'autorisation d'usage permet** : la production sur **un seul nœud**, à condition de ne pas fournir le logiciel à des tiers « on a hosted or embedded basis » (en service, ou intégré dans un produit ou une solution offerts à des tiers) ; les établissements d'enseignement et les organisations à but non lucratif, sans restriction hors profit commercial. **Un cluster de plusieurs nœuds exige une licence commerciale** : la FAQ officielle et le README le disent, le texte de la BSL ne mentionne ni nombre de connexions ni taille de nœud.
- **Le passage d'Apache-2.0 à BSL** s'est fait à la version **5.9.0**, entre avril et mai 2025 : commit du fichier `LICENSE` le 2025-04-10, tag `e5.9.0` le 2025-05-02, annonces des 6 et 7 mai, image Docker le 16 mai. Les sources n'en donnent pas une date unique. Depuis la 5.9, les éditions « Community » et « Enterprise » sont une seule base de code sous une seule licence ; aucun nouveau changement de licence depuis.
- **Dernière ligne encore Apache-2.0** : la 5.8.x (dernière release **5.8.9**, 2025-12-31), le fichier `LICENSE` de ce tag étant Apache-2.0 par défaut avec des dossiers Enterprise en BSL. Une fin de support en février 2026 a été lue dans un résumé de discussion, non recoupée.
- **Gouvernance** : EMQ Technologies écrit l'essentiel du code, clients commerciaux cités sur le site (SAIC Volkswagen, Swire Coca-Cola, Geely) ; aucun changement de propriétaire trouvé.

## Limites à connaître

- **La licence est la première limite** : la BSL n'est pas une licence libre. Pour une ESN qui héberge ou intègre le broker chez ses clients, le cas est à faire valider avant le premier déploiement.
- **Une documentation en retard sur la licence** : la page de cluster dit encore « limit the cluster size to three nodes in the open-source edition », périmée depuis la fusion des éditions ; la doc courante s'intitule « Enterprise » ; les fonctions qui exigent une licence payante (dont le SSO du tableau de bord, par LDAP, SAML ou OIDC) ne sont pas détaillées par la FAQ.
- **Un défaut signalé sur le nœud seul** : le ticket n° 17600 du 2026-06-16 rapporte, en 6.2.1, un plantage au démarrage d'un nœud unique avec une licence à nœud unique, fermé « not planned » d'après un résumé ; la cause et un éventuel correctif n'ont pas été relevés. À tester sur la version visée.
- **Sparkplug B : des fonctions de règle, pas de label** : `spb_encode` et `spb_decode`, avec un état par session client pour les alias depuis la 6.0.2. EMQX ne figure pas dans la liste « Sparkplug Compatible » de l'Eclipse, et la doc ne parle ni de *Primary Host* ni de stockage des messages de naissance.
- **Matériel modeste non documenté** : la doc 5.1 annonçait un minimum d'un cœur et 512 Mo pour 100 000 connexions ; la doc actuelle ne donne plus de minimum. Aucune mesure sur Raspberry Pi n'a été trouvée.
- **Un nombre de mainteneurs réduit** : sept auteurs sur les 100 derniers commits, dont un pour 82.

## Écosystème

### Alternatives

- [[Mosquitto]] — Broker MQTT 3.1, 3.1.1 et 5.0 léger, écrit en C, sans clustering natif : bridges, TLS avec certificats clients, ACL et plugin Dynamic Security, plugin Sparkplug-aware non validé par le TCK ; EPL-2.0 ou EDL-1.0 sous la fondation Eclipse. — un nœud léger sous licence libre, sans cluster ni administration graphique.
- [[NATS]] — Serveur de messagerie en un seul binaire Go : pub/sub et requête/réponse en mémoire (Core NATS), persistance avec rejeu, key-value et object store (JetStream), MQTT 3.1.1 natif ; serveur Apache-2.0 sous la CNCF. — un seul bus pour les services et les capteurs MQTT 3.1.1, sans MQTT 5 ni Sparkplug B, sous Apache-2.0.
- [[RabbitMQ]] — Broker de messages à routage riche (exchanges, files, quorum queues Raft, streams en journal), AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins ; MPL-2.0, copyright Broadcom, support communautaire limité à la dernière série. — déjà déployé pour les files de travail, MQTT par plugin sans QoS 2 ni abonnements partagés.

### Compléments

- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — EMQX expose ses métriques au format Prometheus, en pull ou par Pushgateway.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — Operator et chart Helm officiels pour déployer un cluster EMQX.
- [[Kafka]] — Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0). — pont Kafka intégré : les messages MQTT sont produits vers Kafka, ou consommés depuis Kafka.
- [[InfluxDB]] — SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles. — intégration de données documentée : les messages MQTT arrivent dans InfluxDB sans passerelle séparée.
- [[TimescaleDB]] — Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres. — intégration de données documentée vers Timescale.

## Ressources

- Documentation — https://docs.emqx.com/en/emqx/latest/
- Dépôt — https://github.com/emqx/emqx
- Article — https://www.emqx.com/en/content/license-faq

## Voir aussi

- [[Data & pipelines]] — le hub du domaine
- [[Comparatif - Brokers MQTT]] — ce qui départage Mosquitto et EMQX, et les deux brokers écartés
- [[Architecture pilotée par les événements]] — la notion : file contre journal, garanties de livraison
