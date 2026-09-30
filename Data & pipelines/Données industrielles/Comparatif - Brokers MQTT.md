---
role: comparatif
nom: Comparatif - Brokers MQTT
categorie: data/industrie
tags: [mqtt, message-broker]
---

# Comparatif - Brokers MQTT

> On tranche sur : le nombre de nœuds (un seul ou un cluster), la licence — dont une qui n'est pas libre —, l'authentification des clients, le support réel de Sparkplug B, l'empreinte sur du matériel modeste et l'exploitation en atelier.

![[Comparatif - Brokers MQTT.base]]

## Ce qui départage

- [[Mosquitto]] — le **nœud léger** : un seul serveur en C, MQTT 3.1, 3.1.1 et 5.0, des bridges pour relier l'atelier à un broker central, TLS avec le nom du certificat client pour identité, ACL et plugin Dynamic Security, EPL-2.0 ou EDL-1.0 sans palier payant. Le prix : aucun clustering, aucune release depuis sept mois et demi, un seul auteur sur les derniers commits, et un plugin Sparkplug non validé par le TCK.
- [[EMQX]] — le **broker clusterisable** : cluster natif, règles et intégrations de données (Kafka, bases), authentification par annuaire, JWT, SCRAM ou Kerberos, Prometheus natif, Operator Kubernetes. Le prix : la **BSL 1.1** depuis la 5.9, source-available, où un seul nœud est gratuit en production et où le cluster exige une licence commerciale ; une licence qui exclut la fourniture « hosted or embedded » à des tiers.

**Critère par critère**

**Versions de MQTT.** [[Mosquitto]] : 3.1, 3.1.1 et 5.0, limitables par écouteur. [[EMQX]] : 3.x et 5.0, plus MQTT sur QUIC et les passerelles MQTT-SN, CoAP, LwM2M et OCPP.

**Clustering.** [[Mosquitto]] : non, un nœud ; les bridges relaient des topics mais ne répartissent pas la charge. [[EMQX]] : natif (nœuds *core* et *replicant*), 100 millions de connexions annoncés par cluster, latence réseau de cluster à tenir sous 10 ms ; **la licence commerciale est exigée** dès le deuxième nœud.

**TLS et authentification.** Les deux gèrent TLS mutuel et l'identité par certificat client. [[Mosquitto]] : fichier de mots de passe, ACL, plugin Dynamic Security, bases externes par plugin tiers ; pas d'annuaire ni d'OIDC dans la doc officielle. [[EMQX]] : base intégrée, SQL, MongoDB, Redis, LDAP, HTTP, JWT, PSK, SCRAM, Kerberos, plus CRL et OCSP ; l'OIDC ne sert qu'au SSO du tableau de bord, pas à l'authentification des clients MQTT.

**Sparkplug B.** Aucun des deux n'est dans la liste « Sparkplug Compatible » de l'Eclipse (elle cite Cirrus Link Chariot, HiveMQ CE et Professional, NanoMQ, SIOTH). [[Mosquitto]] livre depuis la 2.1 un plugin `sparkplug-aware` dont le README dit qu'il n'est pas testé avec le TCK officiel ; le TCK, d'après une demande de 2023 sur le dépôt de la spécification, ne peut valider que HiveMQ. [[EMQX]] offre les fonctions de règle `spb_encode` et `spb_decode` (alias gérés depuis la 6.0.2) et la doc est muette sur le rôle « aware ». La spécification n'exige du broker que QoS 0 et 1, le retain et les messages de dernière volonté : les deux les tiennent.

**Empreinte.** [[Mosquitto]] : environ 120 ko d'exécutable et 3 Mo de mémoire pour 1 000 clients, d'après la page du projet (chiffres anciens) ; image Docker pour arm/v6 et arm64. [[EMQX]] : plus lourd, Erlang/OTP ; la doc 5.1 donnait un minimum d'un cœur et 512 Mo pour 100 000 connexions, la doc actuelle n'en donne plus ; images amd64 et arm64. Aucune mesure indépendante sur Raspberry Pi n'a été relevée pour l'un ni l'autre.

**Exploitation.** [[Mosquitto]] : un fichier de configuration, `$SYS` pour l'état, pas d'endpoint Prometheus natif. [[EMQX]] : tableau de bord et API REST, Prometheus natif, Operator et chart Helm, persistance sur RocksDB.

**Licence.** [[Mosquitto]] : EPL-2.0 OR EDL-1.0 (SPDX `EPL-2.0 OR BSD-3-Clause`), aucune fonction réservée. [[EMQX]] : BSL 1.1, conversion en Apache-2.0 quatre ans après chaque version ; **ce n'est pas une licence libre** : un nœud seul, sans fourniture à des tiers, est gratuit ; un cluster, non. La dernière ligne Apache-2.0 est la 5.8.x.

**Gouvernance.** [[Mosquitto]] : fondation Eclipse, Cedalo à la manœuvre d'après le site, un mainteneur principal. [[EMQX]] : EMQ Technologies, un seul éditeur au cœur.

**Les brokers déjà dans le brain qui parlent MQTT** (sans fiche MQTT dédiée) :

- [[NATS]] — **MQTT 3.1.1 natif**, QoS 0, 1 et 2, JetStream obligatoire, serveur 2.10 ou plus ; MQTT 5 refusé, Sparkplug B hors du périmètre documenté. Sept des huit derniers avis de sécurité du dépôt, dans un relevé du 2026-06-29, touchaient MQTT ou JWT.
- [[RabbitMQ]] — **MQTT 3.1, 3.1.1 et 5.0 par le plugin `rabbitmq_mqtt`** livré avec la distribution (MQTT 5 depuis la 3.13.0 du 2024-02-22), mais **sans QoS 2, sans abonnements partagés**, et des messages retenus locaux à chaque nœud, non répliqués.
- [[Kafka]] — **aucun MQTT natif** : il faut un broker MQTT devant, et un pont. [[EMQX]] en embarque un ; le proxy MQTT de Confluent est déprécié depuis Confluent Platform 7.9, et le connecteur source MQTT de Confluent est sous licence commerciale après un essai de 30 jours ; Stream Reactor (Lenses.io) fournit des connecteurs source et sink sous Apache-2.0.
- [[Redpanda]] — pas de MQTT natif ; son composant `mqtt` lit un broker externe : c'est une passerelle.

**Pas de fiche ici**, faute d'être éprouvé pour l'on-prem industriel ou faute de rentrer dans le plafond du lot :

- **HiveMQ Community Edition** — Apache-2.0, dernière release 2026.5 (2026-05-27), la seule des quatre candidats listée « Sparkplug Compatible » par l'Eclipse. Écartée : le clustering, le Control Center et toutes les *Enterprise Extensions* (Security, Bridge, Kafka, bases de données) sont absents de l'édition communautaire ; 91 des 100 derniers commits sont ceux d'un robot de mise à jour des dépendances, le wiki recommande 4 Go et 4 cœurs en production, un utilisateur rapporte sur Raspberry Pi une erreur RocksDB contournée par la persistance en mémoire. À reprendre si un broker Sparkplug listé est exigé.
- **VerneMQ** — code Apache-2.0, cluster natif et gratuit, activité réelle (2.2.1 du 2026-09-17, un mainteneur principal, Octavo Labs). Écarté : les **binaires et images Docker officiels sont sous EULA**, avec abonnement annuel pour un usage commercial, donc un usage gratuit passe par la compilation ; aucune image arm64 officielle ; aucune documentation Sparkplug.
- **NanoMQ** — cité par la liste Sparkplug de l'Eclipse, non évalué.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Données industrielles]] — le hub du dossier.
- [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — la notion : Sparkplug B, pourquoi un broker, sécurité d'un réseau d'atelier.
- [[Comparatif - Brokers de messages]] — les brokers génériques : journal, file, binaire unique.
- [[Architecture pilotée par les événements]] — événement contre commande, file contre journal, garanties de livraison.
