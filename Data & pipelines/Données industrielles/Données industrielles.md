---
role: hub
nom: Données industrielles
alias: [données d'atelier, IIoT, industrial data]
pitch: Amener la donnée de l'atelier jusqu'au système d'information par les protocoles industriels — brokers MQTT, piles OPC UA, outils de flux — et sécuriser le chemin.
domaines: [data-eng, infra-ops]
tags: [mqtt, opc-ua, iiot, message-broker]
---

# Données industrielles

> Amener la donnée de l'atelier jusqu'au système d'information par les protocoles industriels — brokers MQTT, piles OPC UA, outils de flux — et sécuriser le chemin.

## Ce qu'il faut comprendre

- Ce dossier range ce qui parle **les protocoles de l'atelier**, pas ce qui transporte des messages en général : les brokers génériques ([[Kafka]], [[NATS]], [[RabbitMQ]]) sont dans [[Messagerie]], les outils de chargement génériques dans [[Ingestion de données]], la base qui stocke le résultat dans [[Bases de données]] ([[InfluxDB]], [[TimescaleDB]]).
- **Trois protocoles, trois rôles** : Modbus lit des registres, OPC UA expose un modèle d'information, MQTT transporte par un broker. La notion [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] pose le vocabulaire, la pyramide ISA-95, Sparkplug B et la sécurité d'un réseau d'atelier.
- **Les licences ne sont pas les mêmes, et l'une est restrictive** : [[Mosquitto]] est en EPL-2.0 ou EDL-1.0, [[Node-RED]] en Apache-2.0, [[asyncua]] en LGPL-3.0 (à lire pour un livrable embarqué figé). [[EMQX]] est sous **BSL 1.1** depuis la 5.9 : source-available, un seul nœud gratuit en production, le cluster exige une licence commerciale, et la fourniture « hosted or embedded » à des tiers est exclue.
- **Deux brokers MQTT seulement ont une fiche**, départagés dans [[Comparatif - Brokers MQTT]] : le nœud léger sous licence libre, le cluster sous BSL. Les brokers déjà dans le brain qui parlent MQTT sont cités dans ce comparatif : [[NATS]] (3.1.1 seul) et [[RabbitMQ]] (sans QoS 2) ; [[Kafka]] n'en parle pas.
- **Une passerelle d'atelier est un point d'entrée dans le réseau.** [[Node-RED]] a un éditeur ouvert par défaut, et des produits d'atelier livrés avec lui sans authentification ont eu des CVE : la configuration d'`adminAuth` n'est pas optionnelle.
- **Des piles OPC UA sans fiche**, faute de place dans le lot : open62541 (MPL-2.0, C), Eclipse Milo (EPL-2.0, Java), node-opcua (MIT, dont le pub/sub est un module commercial), et Telegraf (MIT), dont les plug-ins lisent OPC UA, Modbus et MQTT. Leurs points sont dans les fiches [[asyncua]] et [[Node-RED]].

## Choisir

- Un broker MQTT sur un seul nœud, sous licence libre, sur un petit matériel → [[Mosquitto]].
- Un cluster de brokers MQTT, avec intégrations vers Kafka et bases de séries, et un budget de licence → [[EMQX]].
- Lire un automate ou un serveur OPC UA depuis du code Python → [[asyncua]].
- Relier automate, broker et base par un flux visuel que les automaticiens lisent → [[Node-RED]], avec `adminAuth` configuré.
- Comprendre MQTT, OPC UA, Modbus, Sparkplug B, la pyramide ISA-95 et la sécurité du réseau d'atelier → [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]].
- Stocker les séries une fois arrivées → [[InfluxDB]] ou [[TimescaleDB]], cf. [[Comparatif - Bases temporelles]].

<!-- AUTO:START -->
### Notions
- [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — domaines : data-eng, infra-ops

### Briques
- [[asyncua]] — Bibliothèque Python asynchrone, client et serveur OPC UA : lecture, écriture, abonnements, méthodes, historique, chiffrement X.509 et import de NodeSet XML ; LGPL-3.0, noyau de mainteneurs réduit, alarmes serveur non implémentées et pub/sub minimal.
- [[EMQX]] — Broker MQTT 3.x et 5.0 en Erlang : cluster natif, règles et intégrations de données (Kafka, bases), authentification LDAP, JWT ou X.509, Prometheus natif ; BSL 1.1 depuis la 5.9 (source-available : un seul nœud gratuit en production, le cluster exige une licence commerciale).
- [[Mosquitto]] — Broker MQTT 3.1, 3.1.1 et 5.0 léger, écrit en C, sans clustering natif : bridges, TLS avec certificats clients, ACL et plugin Dynamic Security, plugin Sparkplug-aware non validé par le TCK ; EPL-2.0 ou EDL-1.0 sous la fondation Eclipse.
- [[Node-RED]] — Éditeur visuel de flux dans le navigateur, sur un runtime Node.js : nœuds MQTT, HTTP, TCP, WebSocket et Function livrés, des milliers de nœuds communautaires (OPC UA, Modbus, S7) sans revue de sécurité ; Apache-2.0 sous l'OpenJS Foundation, éditeur non protégé par défaut.

### Comparatifs
- [[Comparatif - Brokers MQTT]]
<!-- AUTO:END -->
