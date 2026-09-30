---
role: brique
nom: asyncua
alias: [opcua-asyncio, FreeOpcUa, asyncua OPC UA]
pitch: "Bibliothèque Python asynchrone, client et serveur OPC UA : lecture, écriture, abonnements, méthodes, historique, chiffrement X.509 et import de NodeSet XML ; LGPL-3.0, noyau de mainteneurs réduit, alarmes serveur non implémentées et pub/sub minimal."
categorie: data/industrie
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Node-RED]]"]
complements: []
tags: [opc-ua, iiot, data-ingestion]
url_docs: https://opcua-asyncio.readthedocs.io/
url_repo: https://github.com/FreeOpcUa/opcua-asyncio
---

# asyncua

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python asynchrone, client et serveur OPC UA : lecture, écriture, abonnements, méthodes, historique, chiffrement X.509 et import de NodeSet XML ; LGPL-3.0, noyau de mainteneurs réduit, alarmes serveur non implémentées et pub/sub minimal.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation **OPC UA en Python pur**, sur `asyncio`, du projet FreeOpcUa. Elle offre un **client** (connexion,
navigation dans l'espace d'adressage, lecture et écriture, abonnements aux changements de donnée et
aux événements, appel de méthodes, lecture d'historique) et un **serveur** (mêmes services, historique
des changements et des événements, chiffrement, gestion de certificats, structures personnalisées).
Un wrapper synchrone (`asyncua.sync`) et des outils en ligne de commande (`uals`, `uaread`,
`uasubscribe`, `uahistoryread`) sont fournis. Les politiques de sécurité comptent None, Basic128Rsa15,
Basic256, Basic256Sha256, Aes128Sha256RsaOaep et Aes256Sha256RsaPss ; les jetons d'utilisateur sont
anonyme, nom et mot de passe, ou certificat X.509.

Relevé le 2026-09-30 : **v2.0.1** du 2026-06-29 (2.0 le 2026-06-05), environ 1 500 étoiles, dernier
commit du 2026-09-16. PyPI annonce Python 3.10 à 3.13 et le statut *Beta* ; les notes de la 2.0
mentionnent aussi 3.14, que PyPI ne classe pas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Collecter des variables d'un automate ou d'un serveur OPC UA depuis du code Python : un pipeline, un notebook, un service | Un serveur embarqué sur microcontrôleur, en C : open62541 (MPL-2.0, sans fiche ici) |
| Publier ensuite vers un broker MQTT ou une base : la bibliothèque ne connaît que OPC UA, le reste est du Python ordinaire | Les équipes d'atelier doivent lire et modifier le flux sans écrire de code : [[Node-RED]] |
| Un serveur OPC UA de test ou de simulation, rapide à écrire, pour développer sans automate | Une passerelle Java à embarquer ou à faire certifier : Eclipse Milo (EPL-2.0, sans fiche ici) |
| Charger un modèle d'information depuis un fichier NodeSet2 XML | Les alarmes et conditions côté serveur : le README les liste comme non implémentées |

## Mise en œuvre

- Installation — `pip install asyncua` ; dépendances `cryptography`, `pyopenssl`, `aiosqlite`, `anyio` ; Python 3.10 minimum
- Point d'entrée — `async with Client(url=...) as client`, puis `client.nodes.root.get_child("0:Objects/2:MyObject/2:MyVariable")` et `await var.read_value()`, d'après l'exemple officiel `client-minimal.py` ; pour les abonnements, `client.create_subscription(500)` puis `subscribe_data_change(nodes)`, et `auto_reconnect=True` à la connexion depuis la 2.0.1
- Prérequis — pour le chiffrement, `set_security(SecurityPolicyBasic256Sha256, certificate=..., private_key=..., server_certificate=...)` ; un `CertificateValidator` avec `TrustStore` est fourni
- Exécution — aucune : c'est une bibliothèque, pas un service ; le démarrage d'un serveur sur un Raspberry Pi prend environ 3,5 s avec le cache de l'espace d'adressage, contre 125 s sans
- Coût — gratuit ; aucune certification OPC Foundation trouvée, le README cite des serveurs testés (Prosys, Kepware, Beckhoff, WinCC, B&R)

## Licence et gouvernance

- **LGPL-3.0**, dans le fichier `COPYING` (le chemin `LICENSE` répond 404) ; PyPI affiche « LGPLv3+ », GitHub « LGPL-3.0 » seule. **Lecture, sans valeur juridique** : utiliser `asyncua` comme dépendance `pip` d'un code fermé est en général compatible avec la LGPL, à condition de fournir la notice et les sources de ses propres modifications de la bibliothèque, et de laisser l'utilisateur la remplacer. Le point sensible est l'**embarqué figé** (PyInstaller, Nuitka, une image où la bibliothèque n'est plus remplaçable) : à valider avec un juriste avant de livrer chez un client.
- **Gouvernance** : organisation GitHub « FreeOpcUa », ni fondation ni société mainteneur trouvée. Environ 226 contributeurs au total, mais `oroulet` signe 1 096 commits et n'apparaît pas dans les 20 derniers, menés par trois ou quatre contributeurs extérieurs (20 commits en sept semaines). Aucun changement de propriétaire trouvé.

## Limites à connaître

- **Un README en retard sur les notes de version** : il classe encore la reconnexion automatique du client parmi les fonctions « peut-être » non implémentées, alors que les notes de la 2.0 l'annoncent et que l'exemple officiel l'emploie. Il annonce aussi Python 3.14 sans classifieur PyPI. Se fier aux notes et aux exemples, et tester.
- **Serveur : des fonctions absentes** : alarmes, vues, restauration de session, WebSocket et XML ne sont pas implémentés selon le README ; le modèle d'utilisateur est basique (un seul utilisateur en écriture). Le pub/sub est annoncé en « MVP » dans les notes de la 2.0.
- **Pas d'empreinte mémoire ni de profil Nano ou Micro documentés** : la bibliothèque est du Python, elle suppose un interpréteur. Sur microcontrôleur, une pile C comme open62541 est un autre choix.
- **Pas de passerelle prête à l'emploi** : aucun exemple officiel n'illustre la publication vers MQTT ou une base. Ce montage est courant, il est à écrire.
- **Adoption** : environ 710 000 téléchargements PyPI en septembre 2026 hors miroirs, environ 740 dépôts dépendants sur GitHub (exemples : Conpot, MyEMS). Aucun produit industriel qui l'embarque n'a été trouvé.

## Écosystème

### Alternatives

- [[Node-RED]] — Éditeur visuel de flux dans le navigateur, sur un runtime Node.js : nœuds MQTT, HTTP, TCP, WebSocket et Function livrés, des milliers de nœuds communautaires (OPC UA, Modbus, S7) sans revue de sécurité ; Apache-2.0 sous l'OpenJS Foundation, éditeur non protégé par défaut. — le même besoin, par un flux visuel que lisent les automaticiens, plutôt que par du code Python versionné.
- voisin : **open62541** (MPL-2.0, C, v1.5.8 du 2026-09-06, environ 3 200 étoiles) — pile C client et serveur, profil *Micro Embedded Device Server*, serveur exemple certifié profil *Standard Server 2017* ; o6 Automation emploie les contributeurs principaux, sans double licence commerciale, seulement du support ; sans fiche dans le brain.
- voisin : **Eclipse Milo** (EPL-2.0, Java, v1.1.7 du 2026-09-09, environ 1 400 étoiles) — pile Java client et serveur de la fondation Eclipse, sur laquelle Ignition est bâti d'après son mainteneur ; 32 contributeurs, dont un signe presque tout ; sans fiche dans le brain.
- voisin : **node-opcua** (MIT, Node.js) — le pub/sub et le serveur de découverte (GDS) y sont un module commercial de Sterfive ; sans fiche dans le brain.

### Compléments

Aucun complément déclaré : la publication vers un broker ou une base de séries se fait en Python ordinaire, voir le hub du dossier.

## Ressources

- Documentation — https://opcua-asyncio.readthedocs.io/
- Dépôt — https://github.com/FreeOpcUa/opcua-asyncio

## Voir aussi

- [[Données industrielles]] — le hub du dossier
- [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]] — la notion : le modèle d'information et la sécurité d'OPC UA, Modbus, MQTT, Sparkplug B
- [[Comparatif - Brokers MQTT]] — les brokers où publier ce qu'on lit en OPC UA
