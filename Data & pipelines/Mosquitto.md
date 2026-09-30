---
role: brique
nom: Mosquitto
alias: [mosquitto, Eclipse Mosquitto, mosquitto-broker]
pitch: "Broker MQTT 3.1, 3.1.1 et 5.0 léger, écrit en C, sans clustering natif : bridges, TLS avec certificats clients, ACL et plugin Dynamic Security, plugin Sparkplug-aware non validé par le TCK ; EPL-2.0 ou EDL-1.0 sous la fondation Eclipse."
categorie: data/industrie
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: C
scaling: single-node
alternatives: ["[[EMQX]]", "[[NATS]]", "[[RabbitMQ]]"]
complements: []
tags: [mqtt, message-broker, iiot, self-hosted]
url_docs: https://mosquitto.org/documentation/
url_repo: https://github.com/eclipse-mosquitto/mosquitto
---

# Mosquitto

<!-- AUTO:BANDEAU:START -->
> Broker MQTT 3.1, 3.1.1 et 5.0 léger, écrit en C, sans clustering natif : bridges, TLS avec certificats clients, ACL et plugin Dynamic Security, plugin Sparkplug-aware non validé par le TCK ; EPL-2.0 ou EDL-1.0 sous la fondation Eclipse.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Broker **MQTT** du projet Eclipse, écrit en C : des clients publient sur des topics, le broker
route vers les abonnés. Il parle MQTT 3.1, 3.1.1 et 5.0 (l'option `accept_protocol_versions` limite
les versions par écouteur), en TCP, TLS et WebSocket. Il fait **un seul nœud** : la doc de
configuration ne décrit aucun clustering, et un échange de 2014 sur la liste de diffusion du
projet dit que le *bridge* (le pont qui relaie des topics vers un autre broker) n'est pas une
solution de répartition de charge. C'est le broker qu'on met en bordure, sur un petit matériel,
ou en tête d'une cellule d'atelier.

Relevé le 2026-09-30 : dernière release **v2.1.2** du 2026-02-09 (2.1.0 le 2026-01-29), environ
11 200 étoiles, dernier commit du 2026-09-03. La version 2.1 apporte un WebSocket intégré sans
libwebsockets, le protocole PROXY, le plugin `persist-sqlite` et un plugin `sparkplug-aware`.
Le journal des changements de `master` annonce une 2.1.3 non publiée : **aucune release depuis
sept mois et demi**, à rapprocher du fait que les 20 derniers commits (15 juin au 3 septembre)
sont tous du même auteur.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un nœud suffit : une cellule d'atelier, une passerelle en bordure, un Raspberry Pi | Des centaines de milliers de connexions à répartir sur plusieurs nœuds, ou une haute disponibilité : [[EMQX]] (le cluster y exige une licence, voir *Licence*) |
| La licence doit être sans condition : EPL-2.0 ou EDL-1.0 (BSD-3-Clause), aucun palier payant dans le dépôt | Une administration en interface graphique, une intégration de données vers Kafka ou une base sans écrire de passerelle : [[EMQX]], ou un outil de flux devant Mosquitto |
| Un bridge vers un broker central, pour que l'atelier pousse vers le site sans qu'aucune connexion n'entre | Un support Sparkplug B validé : le plugin est livré avec la 2.1 mais sa documentation dit qu'il n'est pas testé avec le TCK officiel |
| Les clients sont des automates ou des passerelles qui ne demandent que MQTT, avec une empreinte de quelques mégaoctets | Une authentification par annuaire ou OIDC des clients : la doc officielle n'en décrit pas ; MySQL, JWT et Redis passent par un plugin tiers, `mosquitto-go-auth` |

## Mise en œuvre

- Installation — paquets des distributions, compilation depuis les sources, ou image Docker officielle `eclipse-mosquitto` (architectures 386, amd64, arm/v6, arm64/v8, ppc64le, s390x, ce qui couvre un Raspberry Pi) ; près de 685 millions de téléchargements constatés le 2026-09-30
- Point d'entrée — MQTT sur le port 1883 (TLS : 8883, ports enregistrés à l'IANA), WebSocket dans un écouteur distinct, fichier `mosquitto.conf`, outils `mosquitto_pub` et `mosquitto_sub` ; l'arbre de topics `$SYS` donne l'état du broker (clients, messages, mémoire)
- Prérequis — TLS en 1.2 ou 1.3 (`tls_version`), `require_certificate` et `use_identity_as_username` pour que le nom du certificat client devienne l'identité ; les connexions anonymes sont refusées par défaut depuis la 2.0 ; un fichier de mots de passe et un fichier ACL (`topic read|write|readwrite|deny`) pour commencer, le plugin **Dynamic Security** (rôles, groupes, clients, administrable à chaud par `$CONTROL/dynamic-security/v1`, livré avec la distribution depuis la 2.0) pour aller plus loin
- Exécution — self-hébergé ; persistance par le plugin `persist-sqlite` (la persistance intégrée dans `mosquitto.db` est déconseillée dans le manuel) ; pas d'endpoint Prometheus natif dans la doc lue, la supervision passe par `$SYS`
- Coût — gratuit ; la page du projet annonce un exécutable d'environ 120 ko et 3 Mo de mémoire pour 1 000 clients connectés, et des essais à 100 000 clients, chiffres anciens sans date de mesure

## Licence et gouvernance

- **EPL-2.0 OR EDL-1.0** (identifiant SPDX `EPL-2.0 OR BSD-3-Clause`), lu dans le fichier `LICENSE.txt` de `master` le 2026-09-30. Copyleft faible au niveau du fichier, sans palier payant dans le dépôt : **aucune fonction de sécurité, de clustering ou d'administration n'est réservée à une édition** dans ce qui est publié.
- **Projet Eclipse Foundation** (état « Mature »), dont la page du site indique un développement porté par **Cedalo** ; le mainteneur est Roger Light. Cedalo vend une édition « Pro Mosquitto » : son contenu exact n'a pas été relevé, et rien n'établit qu'un plugin payant soit le même code que celui du dépôt libre.
- Aucun changement de propriétaire ni de licence trouvé. **Le risque est la concentration** : un seul auteur sur les 20 derniers commits, et sept mois sans release.

## Limites à connaître

- **Pas de clustering** : la haute disponibilité se fait côté client (reconnexion vers un second broker) ou par bridges, sans état partagé. Les messages retenus et les sessions persistantes vivent sur un seul nœud.
- **Sparkplug B, pas de validation officielle** : le README du plugin `sparkplug-aware` dit qu'il implémente les exigences de « conscience » de la spécification 3.0 et qu'il n'est pas testé avec le TCK officiel. Mosquitto ne figure pas dans la liste des logiciels « Sparkplug Compatible » de l'Eclipse, et une demande de 2023 sur le dépôt de la spécification dit que le TCK ne peut valider que HiveMQ. La spécification n'exige du broker que QoS 0 et 1, le retain et les messages de dernière volonté (chapitre *Conformance*) : la lecture qui en découle, non vérifiée par un test, est qu'un broker qui tient ces trois points sert de transport ; ce qui manque est le label, pas une fonction connue.
- **Fichiers de mots de passe et d'ACL en voie de retrait** : la 2.1 dépréciait `password_file` et `acl_file` au profit des plugins `password-file` et `acl-file`, avec retrait prévu en 3.0. Une configuration écrite à l'ancienne marche encore, elle émet un avertissement.
- **Pas d'OAuth ni de LDAP dans la doc officielle** : les bases externes passent par un plugin tiers.
- **Une limite de système d'exploitation** : le manuel donne 2 048 ou 8 192 connexions sous Windows ; ailleurs la limite est celle des descripteurs de fichiers.

## Écosystème

### Alternatives

- [[EMQX]] — Broker MQTT 3.x et 5.0 en Erlang : cluster natif, règles et intégrations de données (Kafka, bases), authentification LDAP, JWT ou X.509, Prometheus natif ; BSL 1.1 depuis la 5.9 (source-available : un seul nœud gratuit en production, le cluster exige une licence commerciale). — le cluster, l'administration graphique et les intégrations de données, au prix d'une licence BSL.
- [[NATS]] — Serveur de messagerie en un seul binaire Go : pub/sub et requête/réponse en mémoire (Core NATS), persistance avec rejeu, key-value et object store (JetStream), MQTT 3.1.1 natif ; serveur Apache-2.0 sous la CNCF. — un seul bus pour les services et pour les capteurs MQTT 3.1.1, sans Sparkplug B ni MQTT 5.
- [[RabbitMQ]] — Broker de messages à routage riche (exchanges, files, quorum queues Raft, streams en journal), AMQP 0-9-1 et 1.0 natifs, MQTT et STOMP par plugins ; MPL-2.0, copyright Broadcom, support communautaire limité à la dernière série. — déjà déployé pour les files de travail, il accepte MQTT par plugin, sans QoS 2 ni abonnements partagés.

### Compléments

Aucun complément déclaré : la passerelle vers une base de séries temporelles se fait par un outil de flux, voir le hub du dossier.

## Ressources

- Documentation — https://mosquitto.org/documentation/
- Dépôt — https://github.com/eclipse-mosquitto/mosquitto
- Documentation — https://projects.eclipse.org/projects/iot.mosquitto

## Voir aussi

- [[Data & pipelines]] — le hub du domaine
- [[Comparatif - Brokers MQTT]] — ce qui départage Mosquitto et EMQX, et les deux brokers écartés
- [[Architecture pilotée par les événements]] — la notion : file contre journal, garanties de livraison
