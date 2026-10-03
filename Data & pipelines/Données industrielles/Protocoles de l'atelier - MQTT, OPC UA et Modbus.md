---
role: notion
nom: Protocoles de l'atelier - MQTT, OPC UA et Modbus
alias: ["Protocoles de l'atelier : MQTT, OPC UA et Modbus", protocoles industriels, MQTT, OPC UA, Modbus, Sparkplug B, ISA-95, modèle de Purdue, Unified Namespace]
categorie: data/industrie
domaines: [data-eng, infra-ops]
tags: [mqtt, opc-ua, iiot, networking]
---

# Protocoles de l'atelier - MQTT, OPC UA et Modbus

## Aperçu

- Trois protocoles portent la donnée d'atelier, et ils ne se remplacent pas : **Modbus** lit des registres sur un automate, **OPC UA** décrit et expose les données d'une machine, **MQTT** transporte des messages entre producteurs et consommateurs par un broker. Sparkplug B est une couche au-dessus de MQTT.
- Ce que cette page apporte : ce que chacun fait, où il se place dans la pyramide ISA-95, pourquoi un broker MQTT s'intercale, comment sécuriser le réseau, et le trajet du capteur jusqu'à la base de séries temporelles. Les briques sont dans le dossier : [[Mosquitto]], [[EMQX]], [[Node-RED]], [[asyncua]].

## Concepts clés

### MQTT : publier et s'abonner par un broker

- **Publication/abonnement** : un client publie sur un *topic* hiérarchique, le broker route vers les abonnés ; `+` remplace un niveau, `#` tous les niveaux suivants. MQTT 3.1.1 est une norme OASIS du 29 octobre 2014 (aussi ISO/IEC 20922:2016) ; MQTT 5.0, une norme OASIS du 7 mars 2019. Ports enregistrés : 1883, et **8883 pour TLS**, que la spécification recommande.
- **QoS** : 0 au plus une fois, 1 au moins une fois (doublons possibles), 2 exactement une fois. **Retain** : le broker garde le dernier message d'un topic pour les abonnés futurs. **Will** : message que le broker publie si un client disparaît sans se déconnecter.
- **MQTT 5** apporte des codes de raison, des abonnements partagés (répartir la charge entre abonnés), des propriétés utilisateur et une expiration de session.
- **Aucun modèle de données** : le contenu du message est libre. C'est la force de MQTT et sa limite : deux fabricants publieront deux formats.

### OPC UA : un modèle d'information, en client-serveur ou en pub/sub

- **Architecture orientée services**, indépendante de la plateforme, sortie en 2008 : un serveur expose un **espace d'adressage** (nœuds, variables, méthodes, types) qu'un client parcourt, lit et abonne. La partie 14 (pub/sub, version 1.05.06 d'octobre 2025) ajoute un mode sans client-serveur, par UDP ou par un broker (MQTT, Kafka, AMQP).
- **Transports** client-serveur : `opc.tcp`, HTTPS, WebSockets ; encodages binaire, XML ou JSON. Ports IANA : 4840 (TCP et UDP) et 4843 (TLS).
- **Specifications compagnons** : des modèles d'information par secteur, publiés par l'OPC Foundation avec des associations : EUROMAP 77 (presses à injecter vers MES, remplace EUROMAP 63), MTConnect (2019), OPC UA for Machinery (VDMA), PackML.
- **Sécurité intégrée** : trois modes (None, Sign, SignAndEncrypt), des politiques de sécurité, des certificats X.509 pour les applications, des jetons d'utilisateur (anonyme, nom et mot de passe, certificat, jeton délivré). Les certificats s'échangent et se font confiance à la main ou par un serveur de gestion.
- **Licence de la spécification** : téléchargeable sans adhésion depuis l'annonce du 14 avril 2015, mais sous un contrat d'usage (v1.14, 2017) qui interdit la copie et la redistribution. Ce n'est pas du libre.
- **Pub/sub OPC UA sur MQTT** : topic `<préfixe>/<encodage>/<type>/<éditeur>/...`, encodage `json` ou `uadp`, et retain activé pour les messages de métadonnées, d'état et de connexion, pas pour les données.

### Modbus : des registres, sans sécurité

- **Modèle de données** : quatre tables, *discrete inputs* (1 bit, lecture seule), *coils* (1 bit, lecture-écriture), *input registers* (16 bits, lecture seule), *holding registers* (16 bits, lecture-écriture). Fonctions courantes : 01, 02, 03, 04 pour lire, 05, 06, 15, 16 pour écrire. Spécification V1.1b3 du 26 avril 2012 ; unité de données limitée à 253 octets.
- **Deux liaisons** : série RS-485 (un seul maître, 247 esclaves au plus) et **Modbus/TCP** sur le port 502. La spec série parle de maître et d'esclaves, la couche applicative de client et de serveur.
- **Aucune sécurité native** : ni chiffrement ni authentification, ce que l'ANSSI range parmi les protocoles sans mécanisme de sécurité. **Modbus/TCP Security** (TLS 1.2 ou plus, authentification mutuelle par certificats X.509, port 802, v36 du 2021-07-30) existe ; sa présence sur les automates en service est un fait à constater sur site.
- **Toujours très présent** : dans son rapport 2024, Censys le cite comme le service le plus observé parmi les systèmes industriels exposés à Internet.

### Sparkplug B : donner un sens à MQTT

- Spécification de la fondation Eclipse, **3.0** (site : 2022-10-21 ; PDF : 2022-11-16 ; release GitHub : 2022-12-23), normalisée ISO/IEC 20237:2023. Aucune 4.0 publiée.
- Elle fixe le **topic** `spBv1.0/<groupe>/<type>/<nœud>[/<appareil>]`, les types de message (NBIRTH, NDEATH, DBIRTH, DDEATH, NDATA, DDATA, NCMD, DCMD) et un **payload Protobuf** avec horodatage, types et métadonnées. Le message de mort du nœud est un *Will* en QoS 1 ; l'application hôte déclare son état sur `spBv1.0/STATE/<hôte>`.
- **Rôles** : le *nœud de bordure* (passerelle vers automates et capteurs), l'*application hôte primaire* (le consommateur qui doit être en ligne), le *serveur MQTT* (le broker). Un nœud de bordure attend que l'hôte primaire soit en ligne avant de publier ses messages de naissance.
- **Ce qu'elle exige du broker** : QoS 0 et 1, le retain, les messages Will. Un broker « Aware » stocke en plus les messages de naissance. Le support réel varie : voir [[Comparatif - Brokers MQTT]].
- **Critiques** : les blogs d'éditeurs (HiveMQ, 2024 ; FlowFuse, 2026) relèvent la rigidité du topic, le QoS 0 des données et un payload Protobuf illisible sans décodeur. Ce sont des sources d'éditeurs ; l'affirmation de l'un d'eux qu'il n'y aurait pas de retain est inexacte, puisque l'état est retenu.

### La pyramide ISA-95 et le modèle de Purdue

- ISA-95 range le système d'une usine en niveaux : 0 le procédé physique, 1 capteurs et contrôle de base, 2 supervision, 3 gestion des opérations (MES), 4 planification d'entreprise (ERP). C'est un modèle **fonctionnel** ; le modèle de Purdue en est l'architecture **réseau** de référence. La page de l'ISA place les automates au niveau 2 et SCADA au niveau 3, alors que le découpage usuel de Purdue met l'automate au niveau 1 et la supervision au niveau 2 : toujours citer le découpage retenu.
- **Où placer les protocoles** : aucune source ouverte n'en donne un placement officiel. La lecture courante, sans source normative : Modbus vit aux niveaux 0 à 2, OPC UA aux niveaux 1 à 3, MQTT en haut du niveau 3 ou en zone démilitarisée. Le « niveau 3.5 » est un usage, pas un terme du NIST.
- **Limites du modèle** : le NIST (SP 800-82 Rev. 3, 2023) écrit que l'IIoT peut obliger à déplacer les frontières ou à exposer plus d'interfaces ; un article de 2023 note qu'une « autoroute de données » court-circuite les niveaux et que le cloud est hors du modèle d'origine.

### Pourquoi passer par un broker MQTT

- **Découpler** : un automate ou une passerelle publie une fois, N consommateurs (historien, supervision, pipeline de données, [[Architecture pilotée par les événements|architecture événementielle]]) s'abonnent sans que le producteur les connaisse.
- **Sens de la connexion** : le producteur ouvre une connexion **sortante** vers le broker. C'est ce que recommande le guide conjoint du NCSC et de la CISA (janvier 2026) : toute connexion avec l'environnement de production industrielle doit être initiée depuis l'intérieur ; le broker se place en zone démilitarisée, et l'IT vient y lire.
- **État** : le retain, les sessions persistantes et le Will donnent au consommateur l'état courant et la disparition d'un producteur, sans interroger chaque automate (déduction à partir de la spécification).
- **Ce que le broker ne fait pas** : il ne modélise rien (c'est le rôle d'OPC UA ou de Sparkplug), et une session persistante ne protège que le lien client-broker, pas la livraison de bout en bout.

### Sécurité d'un réseau d'atelier

- **Zones et conduits** (IEC 62443-3-2, 2020) : regrouper les actifs qui partagent des exigences de sécurité en zones, et ne laisser passer que des conduits contrôlés. L'ANSSI (ANSSI-PA-108, version 2 du 2025-11-27) décline des flux unidirectionnels par classe : pare-feu, passerelle unidirectionnelle, puis diode qualifiée.
- **Le NCSC, la CISA et leurs partenaires** (2026-01-14) : les protocoles industriels restent dans des segments isolés ; l'échange OT vers IT passe par la zone démilitarisée en OPC UA sur TLS, MQTT sur TLS ou HTTPS. Le NIST demande de ne laisser passer que des flux entre niveaux adjacents.
- **TLS et certificats clients** : chaque client a son certificat, dont le nom sert d'identité et de clé de droits (ACL par topic, par nœud de bordure, comme les exemples de la spécification Sparkplug). La **rotation** des certificats n'est décrite par aucune des sources relevées : garder le même nom à chaque rotation est une précaution déduite du lien nom-ACL. Voir [[Reverse proxy et TLS]] pour la terminaison.
- **Exposition réelle** : plus de 145 000 systèmes industriels exposés à Internet selon Censys (2024), plus de 600 000 brokers MQTT indexés par Shodan selon Airbus (juin 2024), sans taux d'authentification.
- **Sécurité d'OPC UA** : l'étude du BSI (2017, menée par TÜV SÜD Rail, sur la spécification 1.02 et la pile de référence) ne trouvait « aucune erreur systématique » et relevait quatre faiblesses de l'implémentation de référence ; elle ne couvre pas le pub/sub. Elle recommande Sign ou SignAndEncrypt et d'interdire l'utilisateur anonyme.

### Du capteur à la base de séries temporelles

- **Chaîne type** : capteur ou automate, puis Modbus ou OPC UA vers une passerelle ([[Node-RED]], [[asyncua]]), puis MQTT vers un broker ([[Mosquitto]] en bordure, [[EMQX]] au centre), puis un consommateur qui écrit dans [[InfluxDB]] ou [[TimescaleDB]] (cf. [[Comparatif - Bases temporelles]]). [[Kafka]] ou [[NATS]] peuvent prendre le relais pour le reste du système d'information.
- **Unified Namespace (UNS)** : espace de noms unique où tous les systèmes publient leurs données. Le terme est popularisé par Walker Reynolds ; une critique de 2025 lui reproche l'accent sur les outils plutôt que la gouvernance et des hiérarchies ISA-95 trop simples, et HiveMQ note qu'un broker seul n'est pas un UNS.
- **Horodatage à la source** : OPC UA demande un `sourceTimestamp` en UTC aussi proche que possible de la source, relayé sans changement ; Sparkplug demande UTC et une horloge exacte. Sans horodatage dans le message, l'horodatage est celui du collecteur.
- **Qualité** : un StatusCode OPC UA est Good, Uncertain ou Bad ; une valeur « incertaine » n'est pas à jeter avant d'avoir lu son usage.
- **Bande morte et échantillonnage** : un abonnement OPC UA filtre par bande morte absolue ou en pourcentage et par intervalle d'échantillonnage, avec une file bornée ; écrire « à chaque changement » évite d'inonder le réseau.
- **Tempêtes de reconnexion** : le guide client d'EMQX Cloud donne une reprise à 1 s, doublée à chaque échec jusqu'à 120 s, avec 10 à 30 % d'aléa.
- **Insertion idempotente** : avec QoS 1, des doublons arrivent ; un billet de TigerData propose un index unique sur (horodatage, appareil, métrique) pour rendre l'insertion rejouable. Les unités et la rétention n'ont pas de source ouverte relevée.

## En pratique

- **Commencer par le sens des flux** : qui ouvre la connexion, depuis quelle zone, vers quel broker. Le choix du protocole vient après.
- **Un broker par site, un broker central** : [[Mosquitto]] en bordure avec un bridge sortant vers le broker central ; [[EMQX]] ou un autre si la centralisation exige un cluster. Un seul nœud, sous licence libre, tient souvent un atelier.
- **Ne pas exposer Modbus** : port 502 ouvert sur Internet, c'est l'erreur la plus documentée. Le placer derrière une passerelle qui parle MQTT ou OPC UA sur TLS.
- **Protéger l'éditeur d'une passerelle** : Node-RED est ouvert par défaut (voir sa fiche).
- **Mesurer avant de promettre** : aucun chiffre indépendant de débit ou de latence n'a été relevé pour les brokers ; à mesurer sur le matériel cible.

## Approches voisines & alternatives

- [[Architecture pilotée par les événements]] — événement, file, journal, garanties de livraison, idempotence : le vocabulaire des messages une fois qu'ils sont sur le bus.
- [[Comparatif - Brokers de messages]] — Kafka, Redpanda, NATS, RabbitMQ ; [[NATS]] et [[RabbitMQ]] parlent MQTT avec des bornes (NATS : 3.1.1 seul ; RabbitMQ : sans QoS 2).
- [[Stream processing]] — traiter le flux une fois transporté.
- [[Maintenance prédictive et RUL]] et [[Time series anomaly detection]] — ce que l'on fait des séries une fois stockées.
- [[Apache NiFi]] — l'ingestion de fichiers et de protocoles, hors du périmètre d'atelier.
- Voir aussi : [[Telegraf]], [[open62541]].
- Plateformes d'éditeur qui collectent ces protocoles : Siemens Insights Hub, Cognite Data Fusion (extracteur OPC UA).

## Pour aller plus loin

- Spécification MQTT 5.0 (OASIS) — https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html
- Spécification Sparkplug 3.0 (Eclipse) — https://sparkplug.eclipse.org/specification/version/3.0/documents/sparkplug-specification-3.0.0.pdf
- OPC UA, partie 14 (pub/sub) — https://reference.opcfoundation.org/Core/Part14/v105/docs/
- NIST SP 800-82 Rev. 3 — https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
- Secure connectivity principles for OT (NCSC, CISA et autres, 2026-01-14) — https://www.ncsc.gov.uk/sites/default/files/documents/ncsc-secure-connectivity-for-operational-technology.pdf
- ANSSI, « La cybersécurité des systèmes industriels — mesures détaillées » — https://messervices.cyber.gouv.fr/documents-guides/Guide_Systemes_industriels__Mesures_detaillees_v2.pdf
- BSI, « OPC UA Security Analysis » (2017) — https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/Studies/OPCUA/OPCUA.pdf
- Modbus/TCP Security v36 — https://www.modbus.org/docs/MB-TCP-Security-v36_2021-07-30.pdf
- Hub du dossier — [[Données industrielles]]
