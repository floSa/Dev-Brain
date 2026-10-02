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
- **Les licences ne sont pas les mêmes, et l'une est restrictive** : [[Mosquitto]] est en EPL-2.0 ou EDL-1.0, [[Node-RED]] en Apache-2.0, [[asyncua]] en LGPL-3.0 (à lire pour un livrable embarqué figé), [[Telegraf]] en MIT et [[open62541]] en MPL-2.0 (copyleft par fichier : la liaison avec du code fermé, même statique, est permise, mais les correctifs apportés à la bibliothèque elle-même se publient). [[EMQX]] est sous **BSL 1.1** depuis la 5.9 : source-available, un seul nœud gratuit en production, le cluster exige une licence commerciale, et la fourniture « hosted or embedded » à des tiers est exclue.
- **Deux brokers MQTT seulement ont une fiche**, départagés dans [[Comparatif - Brokers MQTT]] : le nœud léger sous licence libre, le cluster sous BSL. Les brokers déjà dans le brain qui parlent MQTT sont cités dans ce comparatif : [[NATS]] (3.1.1 seul) et [[RabbitMQ]] (sans QoS 2) ; [[Kafka]] n'en parle pas.
- **Une passerelle d'atelier est un point d'entrée dans le réseau.** [[Node-RED]] a un éditeur ouvert par défaut, et des produits d'atelier livrés avec lui sans authentification ont eu des CVE : la configuration d'`adminAuth` n'est pas optionnelle.
- **Collecter sans développer, ou compiler son propre serveur** : [[Telegraf]] lit OPC UA, Modbus, S7 et MQTT par configuration TOML et écrit vers [[InfluxDB]], [[TimescaleDB]], [[Prometheus]] ou [[Kafka]] ; [[open62541]] est la pile C à embarquer pour un serveur ou un client OPC UA dans un produit. Le tampon de Telegraf est en mémoire par défaut, le tampon disque reste expérimental : à connaître avant de compter sur lui pendant une coupure de réseau.
- **Des piles OPC UA sans fiche**, faute de place : Eclipse Milo (EPL-2.0, Java), node-opcua (MIT, dont le pub/sub est un module commercial) et Apache PLC4X (Apache-2.0). Leurs points sont dans les fiches [[open62541]] et [[asyncua]].

## Choisir

- Un broker MQTT sur un seul nœud, sous licence libre, sur un petit matériel → [[Mosquitto]].
- Un cluster de brokers MQTT, avec intégrations vers Kafka et bases de séries, et un budget de licence → [[EMQX]].
- Lire un automate ou un serveur OPC UA depuis du code Python → [[asyncua]].
- Collecter des variables OPC UA, des registres Modbus ou des topics MQTT et les écrire dans une base, sans développer → [[Telegraf]].
- Embarquer un serveur ou un client OPC UA dans un équipement ou un produit livré, en C → [[open62541]].
- Relier automate, broker et base par un flux visuel que les automaticiens lisent → [[Node-RED]], avec `adminAuth` configuré.
- Comprendre MQTT, OPC UA, Modbus, Sparkplug B, la pyramide ISA-95 et la sécurité du réseau d'atelier → [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]].
- Stocker les séries une fois arrivées → [[InfluxDB]] ou [[TimescaleDB]], cf. [[Comparatif - Bases temporelles]].
- Une plateforme IoT industrielle clé en main : [[Siemens Insights Hub]] (cloud privé local possible, géré par Siemens) ou [[Cognite Data Fusion]] (cloud seul), propriétaires, cf. [[Comparatif - Offres de maintenance prédictive]].
- Faire tourner un modèle sur le matériel de l'atelier, avec la donnée qu'on vient de collecter → [[Inférence en bordure - modèles sur du matériel d'atelier]], et [[OpenVINO]] ou [[LiteRT]] côté moteurs.

<!-- AUTO:START -->
### Notions
- [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — domaines : data-eng, infra-ops

### Briques
- [[asyncua]] — Bibliothèque Python asynchrone, client et serveur OPC UA : lecture, écriture, abonnements, méthodes, historique, chiffrement X.509 et import de NodeSet XML ; LGPL-3.0, noyau de mainteneurs réduit, alarmes serveur non implémentées et pub/sub minimal.
- [[Cognite Data Fusion]] — Plateforme de données industrielles de Cognite — modèle de données en graphe, extracteurs (OPC UA, PostgreSQL), contextualisation et API REST avec SDK Python ouvert ; service cloud, sans offre sur site décrite dans la documentation consultée.
- [[EMQX]] — Broker MQTT 3.x et 5.0 en Erlang : cluster natif, règles et intégrations de données (Kafka, bases), authentification LDAP, JWT ou X.509, Prometheus natif ; BSL 1.1 depuis la 5.9 (source-available : un seul nœud gratuit en production, le cluster exige une licence commerciale).
- [[Mosquitto]] — Broker MQTT 3.1, 3.1.1 et 5.0 léger, écrit en C, sans clustering natif : bridges, TLS avec certificats clients, ACL et plugin Dynamic Security, plugin Sparkplug-aware non validé par le TCK ; EPL-2.0 ou EDL-1.0 sous la fondation Eclipse.
- [[Node-RED]] — Éditeur visuel de flux dans le navigateur, sur un runtime Node.js : nœuds MQTT, HTTP, TCP, WebSocket et Function livrés, des milliers de nœuds communautaires (OPC UA, Modbus, S7) sans revue de sécurité ; Apache-2.0 sous l'OpenJS Foundation, éditeur non protégé par défaut.
- [[open62541]] — Pile OPC UA client et serveur en C, cœur sans dépendance hors bibliothèque standard, de Linux à FreeRTOS et Zephyr : sécurité X.509 (mbedTLS ou OpenSSL), PubSub UADP et MQTT encore annoncé expérimental, serveur d'exemple certifié (profil Standard 2017, v1.4) ; MPL-2.0, support commercial chez o6 Automation.
- [[Siemens Insights Hub]] — Plateforme IoT industrielle de Siemens (ex-MindSphere) — collecte des données de machines, modèle d'actifs, tableaux de bord, applications low-code (Mendix) et module Predict de prévision et de détection d'anomalies ; en cloud public, en cloud privé virtuel ou en cloud privé local géré par Siemens.
- [[Telegraf]] — Agent de collecte en Go, binaire statique configuré en TOML : entrées OPC UA (interrogation et abonnements), Modbus, S7 et MQTT, sorties vers InfluxDB, PostgreSQL/TimescaleDB, Prometheus et Kafka ; MIT sous InfluxData, tampon disque encore expérimental.

### Comparatifs
- [[Comparatif - Brokers MQTT]]
<!-- AUTO:END -->
