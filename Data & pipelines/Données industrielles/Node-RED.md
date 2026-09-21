---
role: brique
nom: Node-RED
alias: [node-red, NodeRED, Node RED, FlowFuse, FlowForge]
pitch: "Éditeur visuel de flux dans le navigateur, sur un runtime Node.js : nœuds MQTT, HTTP, TCP, WebSocket et Function livrés, des milliers de nœuds communautaires (OPC UA, Modbus, S7) sans revue de sécurité ; Apache-2.0 sous l'OpenJS Foundation, éditeur non protégé par défaut."
categorie: data/industrie
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: JavaScript
scaling: single-node
alternatives: ["[[asyncua]]"]
complements: ["[[Mosquitto]]", "[[EMQX]]", "[[Docker Compose]]", "[[Authentik]]"]
tags: [low-code, iiot, data-ingestion, self-hosted]
url_docs: https://nodered.org/docs/
url_repo: https://github.com/node-red/node-red
---

# Node-RED

<!-- AUTO:BANDEAU:START -->
> Éditeur visuel de flux dans le navigateur, sur un runtime Node.js : nœuds MQTT, HTTP, TCP, WebSocket et Function livrés, des milliers de nœuds communautaires (OPC UA, Modbus, S7) sans revue de sécurité ; Apache-2.0 sous l'OpenJS Foundation, éditeur non protégé par défaut.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme JavaScript | open-source | self-hébergé ou managé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de **programmation par flux** : on assemble dans un éditeur web des nœuds (entrée, traitement,
sortie) reliés par des fils, et un runtime Node.js les exécute. Les flux sont stockés en JSON
(`flows.json`). Le cœur livre des nœuds réseau (MQTT, HTTP, TCP, WebSocket), de traitement
(Function en JavaScript, Switch, Change, Template) et d'analyse de formats. Tout le reste vient de
**nœuds communautaires** installés par npm, dont les connecteurs industriels (OPC UA, Modbus, Siemens
S7). En atelier, il sert de passerelle : lire un automate, republier sur un broker MQTT, écrire dans
une base.

Relevé le 2026-09-30 : **5.0.7** du 2026-09-08 (la 5.0.0 date du 2026-06-09) et une **4.1.15** du
2026-09-09 sur la branche 4.x ; environ 23 700 étoiles, 239 contributeurs, dernier commit du
2026-09-18. La 5.x exige Node.js 22.9 ou plus et **abandonne les ARM 32 bits** (Raspberry Pi 3b et
plus anciens, Pi Zero).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Relier vite un automate, un broker et une base par un flux visible, sans écrire de code : le cas d'une passerelle d'atelier | Une collecte de métriques pure, configurée par fichier et sans état à héberger : un agent comme Telegraf (MIT, sans fiche ici) |
| L'équipe d'atelier (automaticiens) doit lire et modifier le flux elle-même | Un lecteur OPC UA écrit, testé et versionné comme du code Python : [[asyncua]] |
| Une passerelle en bordure en 64 bits (Raspberry Pi, images Docker amd64 et arm64) | Un Raspberry Pi 3b ou un Pi Zero : la 5.x ne supporte plus l'ARM 32 bits |
| Un besoin de transformer un message à la volée (JavaScript dans un nœud Function) | Un éditeur exposé sans être protégé : il est **ouvert par défaut**, voir *Limites* |

## Mise en œuvre

- Installation — `npm install -g node-red`, image Docker `nodered/node-red` (tags `latest`, `latest-24`, architectures amd64 et arm64, Node 24 ; plus de 324 millions de téléchargements constatés le 2026-09-30), script d'installation pour Raspberry Pi ; la doc officielle fournit un exemple Docker Compose
- Point d'entrée — éditeur sur le port 1880, API d'administration HTTP, nœuds `http in` pour exposer des points d'entrée, dossier utilisateur `~/.node-red` ou `/data` en conteneur
- Prérequis — Node.js 22.9 minimum pour la 5.x (la doc recommande 24, et déconseille les versions impaires) ; **`adminAuth` à configurer** ; `credentialSecret` à fixer une fois pour toutes (il chiffre les secrets de `flows_cred.json`, le changer les rend illisibles)
- Exécution — self-hébergé, ou FlowFuse Cloud ; un runtime par instance, la haute disponibilité et la gestion de flotte sont des offres FlowFuse ; la doc donne `--max-old-space-size=256` pour un Raspberry Pi, sans empreinte mémoire officielle (un mainteneur répondait en 2020 qu'une instance de 512 Mo suffirait très probablement à 65 capteurs émettant toutes les cinq minutes)
- Coût — gratuit ; FlowFuse vend Edge, Hub et Fleet, sur devis

## Licence et gouvernance

- **Apache-2.0**, lu dans le fichier `LICENSE` le 2026-09-30 (« Copyright OpenJS Foundation and other contributors »). Node-RED est né chez IBM en 2013, fondateur de la JS Foundation en 2016, puis de l'OpenJS Foundation (2019), où il est un projet **At-Large**. Gouvernance méritocratique ; la doc note que le petit cercle de *committers* est aussi le cercle de décision.
- **FlowFuse** est le sponsor actif (IBM et Hitachi l'ont été) : société fondée en 2021 par Nick O'Leary, co-créateur de Node-RED, qui en est le CTO et dirige toujours le projet libre. Aucun changement de licence ni de gouvernance trouvé. **Ce qui est payant** est à côté du cœur : le dépôt de FlowFuse est Apache-2.0 sauf le dossier `forge/ee/`, sous licence « FlowForge » (usage en production avec un abonnement) ; l'offre ajoute Git, haute disponibilité, journal d'audit, RBAC, SSO, flotte d'appareils.
- **Un point de dépendance** : les commits de release récents sont du même mainteneur principal, dirigeant de l'éditeur adossé. La doc ne liste pas l'employeur des autres mainteneurs.

## Limites à connaître

- **L'éditeur n'est pas protégé par défaut** : la doc l'écrit, « anyone who can access its IP address can access the editor and deploy changes », et limite cela à un réseau de confiance. Protéger passe par `adminAuth` (utilisateurs avec mot de passe bcrypt, permissions, ou une stratégie Passport), HTTPS, et `httpNodeAuth` pour les routes HTTP. `disableEditor: true` ne coupe pas l'API d'administration ; il faut `httpAdminRoot: false`.
- **Des produits d'atelier livrés avec Node-RED sans authentification ont eu des CVE** : CVE-2025-41656, score 10,0, publiée le 2025-07-01, affecte selon la NVD un automate Pilz. Le défaut vient de la configuration livrée, pas du cœur de Node-RED, qui n'a que **deux avis publiés** au dépôt, tous deux de 2021.
- **Les nœuds communautaires ne sont pas revus** : la doc du projet le dit, un mainteneur écrivait en 2022 que le catalogue ne fait aucune vérification ; dans l'enquête de décembre 2025, 32 % des utilisateurs en production citent la sécurité des nœuds tiers. `externalModules` permet de limiter l'installation de paquets par liste autorisée.
- **Un nœud Function lit les secrets déchiffrés** : quiconque accède à l'éditeur peut les lire (fil du forum officiel sans réponse de mainteneur). Il n'existe pas de page officielle sur le risque des nœuds Function et Exec.
- **Les nœuds industriels sont d'inégale fraîcheur** (relevé du 2026-09-30) : `node-red-contrib-opcua` (de Mika Karaila, Apache-2.0, 0.2.355 du 2026-08-26, bâti sur `node-opcua`) et `node-red-contrib-modbus` (BSD-3-Clause, 5.60.2 du 2026-08-14) sont actifs ; `node-red-contrib-s7` est en **GPL-3.0** (3.1.3 du 2026-01-15) ; `node-red-contrib-iiot-opcua` est à 4.1.2 depuis 2022-12-14 ; `node-red-contrib-influxdb` est à 0.7.0 depuis 2023-12-30, avec un support d'InfluxDB 3 non trouvé. `node-red-dashboard` est déprécié : `@flowfuse/node-red-dashboard` (Apache-2.0, 1.32.0 du 2026-09-24) le remplace.
- **Pas de SSO documenté côté Node-RED** : la page officielle de sécurité ne parle pas d'OIDC ; c'est la doc d'[[Authentik]], en support communautaire, qui décrit l'intégration par `passport-openidconnect`. Pour Keycloak, aucune doc officielle n'a été trouvée. Même constat pour Traefik, Caddy et Nginx : aucune page officielle de Node-RED, seulement une FAQ du forum.

## Écosystème

### Alternatives

- [[asyncua]] — Bibliothèque Python asynchrone, client et serveur OPC UA : lecture, écriture, abonnements, méthodes, historique, chiffrement X.509 et import de NodeSet XML ; LGPL-3.0, noyau de mainteneurs réduit, alarmes serveur non implémentées et pub/sub minimal. — le même besoin de lire un serveur OPC UA, mais en code Python versionné plutôt qu'en flux visuel.
- voisin : **Telegraf** (MIT, InfluxData, v1.40.1 du 2026-09-21) — agent de collecte configuré en TOML, avec `inputs.opcua`, `inputs.modbus` et `inputs.mqtt_consumer` ; sans fiche dans le brain.
- voisin : [[n8n]] — automatisation de workflows entre applications SaaS, pas de protocoles d'atelier ; d'autres catégories, autre licence (source-available).

### Compléments

- [[Mosquitto]] — Broker MQTT 3.1, 3.1.1 et 5.0 léger, écrit en C, sans clustering natif : bridges, TLS avec certificats clients, ACL et plugin Dynamic Security, plugin Sparkplug-aware non validé par le TCK ; EPL-2.0 ou EDL-1.0 sous la fondation Eclipse. — le broker le plus courant à côté de Node-RED, qui parle MQTT par ses nœuds du cœur.
- [[EMQX]] — Broker MQTT 3.x et 5.0 en Erlang : cluster natif, règles et intégrations de données (Kafka, bases), authentification LDAP, JWT ou X.509, Prometheus natif ; BSL 1.1 depuis la 5.9 (source-available : un seul nœud gratuit en production, le cluster exige une licence commerciale). — un broker clusterisable, que Node-RED lit et écrit comme n'importe quel broker MQTT.
- [[Docker Compose]] — Décrit une pile multi-conteneurs dans un fichier compose.yaml et la lance d'une commande (Apache-2.0, Go) — sur un seul hôte : ni multi-nœuds, ni autoscaling. — la doc de Node-RED fournit un exemple `docker-compose-node-red.yml`.
- [[Authentik]] — Fournisseur d'identité à flux configurables : OIDC, SAML, LDAP, SCIM, RADIUS et proxy avec forward auth pour Traefik, Caddy et Nginx, sur PostgreSQL seul (MIT, Python, Authentik Security) — audit renforcé, PAM, mTLS et synchronisation Entra ou Google sont réservés à l'édition Enterprise, 5 $ par utilisateur et par mois. — page d'intégration « Node-RED » dans la doc d'Authentik (support communautaire), par `passport-openidconnect`.

## Ressources

- Documentation — https://nodered.org/docs/
- Dépôt — https://github.com/node-red/node-red
- Documentation — https://nodered.org/docs/user-guide/runtime/securing-node-red

## Voir aussi

- [[Données industrielles]] — le hub du dossier
- [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — la notion : MQTT, OPC UA, Modbus, Sparkplug B, pyramide ISA-95
- [[Comparatif - Brokers MQTT]] — les brokers à mettre derrière un flux Node-RED
