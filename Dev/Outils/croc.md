---
role: brique
nom: croc
alias: [croc, schollz/croc]
pitch: "Transfert de fichiers de machine à machine par phrase de passe : chiffrement de bout en bout via PAKE, relais public ou auto-hébergé, reprise sur interruption, un seul binaire."
categorie: network/transfert
famille: cli
domaines: [infra-ops]
licence_type: open-source
os: "Windows, macOS, Linux, FreeBSD, Android"
langage: Go
alternatives: []
complements: []
tags: [file-transfer, networking, cryptography, cli, self-hosted]
url_docs: https://github.com/schollz/croc
url_repo: https://github.com/schollz/croc
---

# croc

## Pourquoi

Envoyer un fichier d'une machine à une autre sans compte, sans clé SSH préalable, sans service tiers dépositaire du contenu. `croc send fichier` affiche une phrase de passe ; `croc <phrase>` sur l'autre machine récupère le fichier. Écrit en Go, licence MIT, distribué en binaire unique sans dépendance.

Le mécanisme repose sur **PAKE** (password-authenticated key exchange) : la phrase de passe, courte, sert à dériver de part et d'autre une clé de session forte sans jamais transiter. Le chiffrement est de bout en bout, donc le relais qui achemine les octets ne voit que du chiffré. La connexion est tentée en direct entre pairs, avec repli sur relais si le réseau l'impose. Une reprise est possible sur transfert interrompu.

L'intérêt en contexte on-prem : deux machines sur deux réseaux qui ne se voient pas, sans VPN, sans partage monté, sans droit d'ouvrir un port. Et surtout — le relais s'auto-héberge, ce qui permet de garder tout le trafic dans le périmètre du client.

## Quand l'utiliser

- Déplacer un jeu de données, un modèle entraîné ou une archive entre poste de dev et serveur, une fois, sans monter de tuyau permanent.
- Sortir un artefact d'une machine cliente où l'on n'a ni droits d'installation durables ni accès SFTP.
- Transférer entre deux réseaux séparés, en interposant son propre relais dans une zone joignable des deux côtés.
- Dépanner : un binaire téléchargeable, rien à configurer, utilisable dans les deux sens.

## Quand NE PAS l'utiliser

- Synchronisation récurrente ou différentielle de dossiers : ce n'est pas un synchroniseur → `rsync`, Syncthing.
- Copie vers un stockage objet ou entre fournisseurs : `rclone`, ou un client S3 vers [[Dev/Services/MinIO|MinIO]].
- Transfert automatisé dans un pipeline : le modèle repose sur une phrase de passe échangée hors bande, mal adapté à l'ordonnancement.
- Contexte où le relais public est inacceptable sans configuration explicite : il faut alors imposer son propre relais, pas se contenter des valeurs par défaut.
- Archivage ou distribution à plusieurs destinataires : le modèle est point à point.

## Installation & plateformes

Binaires publiés pour Windows, macOS, Linux et FreeBSD, plus paquets Homebrew, Scoop, Chocolatey, pacman, apt, apk, image Docker, `go install`, et applications Android sur F-Droid. Un client web existe sur `getcroc.com`, compatible avec la ligne de commande.

Relais auto-hébergé : `croc relay`, qui écoute par défaut sur les ports TCP 9009 à 9013 (au minimum deux ports requis, personnalisables via `--ports`). En conteneur : publier la même plage et fixer un mot de passe de relais par `CROC_PASS`. Les pairs s'y raccrochent par `--relay hote:9009` (et `--pass`), ou via les variables `CROC_RELAY` et `CROC_PASS`.

## Pièges

- **Phrase de passe en argument de ligne de commande = fuite par la liste des processus** (CVE-2023-43621, Linux et macOS). Passer par la variable d'environnement : `CROC_SECRET=<phrase> croc`.
- Par défaut, le trafic peut emprunter un relais public tiers. Le contenu reste chiffré, mais les métadonnées (adresses, volume, horodatage) sont visibles du relais : dans un cadre client, imposer son propre relais.
- La sécurité tient entièrement à la phrase de passe et à son canal de transmission. Une phrase interceptée avant la réception permet un vol de fichier — le premier arrivé gagne.
- Ports 9009-9013 en écoute : un relais auto-hébergé expose une surface réseau, à filtrer et à protéger par mot de passe.
- L'absence d'audit externe indépendant n'est pas comblée par la clarté du protocole : ne pas en faire la brique de conformité d'un transfert réglementé.
- Les interfaces graphiques référencées dans le dépôt sont des projets tiers non officiels.

## Alternatives

Champ vide, faute de fiche réciproque : `croc` est la première entrée en `network/transfer`. Comparables hors brain : `magic-wormhole` (même principe PAKE, écosystème Python), `rsync` sur SSH (référence pour la synchronisation, mais suppose un accès SSH), Syncthing (synchronisation continue, pas envoi ponctuel), `rclone` (stockages objet).

## Liens

- [[Dev/Services/MinIO|MinIO]] — quand le besoin devient un dépôt d'artefacts durable plutôt qu'un transfert ponctuel
- [[Dev/Outils/Sniffnet|Sniffnet]] — pour vérifier vers quel relais un transfert part réellement
- Site : https://getcroc.com
- Repo : https://github.com/schollz/croc
