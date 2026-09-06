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

<!-- AUTO:BANDEAU:START -->
> Transfert de fichiers de machine à machine par phrase de passe : chiffrement de bout en bout via PAKE, relais public ou auto-hébergé, reprise sur interruption, un seul binaire.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Envoyer un fichier d'une machine à une autre sans compte, sans clé SSH préalable, sans
service tiers dépositaire du contenu : `croc send fichier` affiche une phrase de passe,
`croc <phrase>` sur l'autre machine récupère le fichier. Le mécanisme repose sur **PAKE**
— *password-authenticated key exchange* : la phrase, courte, sert à dériver de part et
d'autre une clé de session forte sans jamais transiter. Le chiffrement est de bout en
bout, donc le relais qui achemine les octets ne voit que du chiffré ; la connexion est
tentée en direct entre pairs, avec repli sur relais si le réseau l'impose, et un transfert
interrompu se reprend. Toute la sécurité tient à la phrase et à son canal de
transmission : interceptée avant la réception, elle suffit à voler le fichier — le premier
arrivé gagne.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Déplacer une fois un jeu de données, un modèle entraîné ou une archive entre poste de dev et serveur, sans monter de tuyau permanent | Synchronisation récurrente ou différentielle de dossiers : ce n'est pas un synchroniseur — `rsync`, Syncthing (hors brain) |
| Sortir un artefact d'une machine cliente où l'on n'a ni droits d'installation durables ni accès SFTP | Copie vers un stockage objet ou entre fournisseurs : `rclone`, ou un client S3 → [[MinIO]] |
| Transférer entre deux réseaux séparés, en interposant son propre relais dans une zone joignable des deux côtés | Transfert automatisé dans un pipeline : le modèle repose sur une phrase échangée hors bande, mal adapté à l'ordonnancement |
| Dépanner : un binaire téléchargeable, rien à configurer, utilisable dans les deux sens | Archivage ou distribution à plusieurs destinataires : le modèle est point à point |
| | Transfert réglementé exigeant une preuve d'audit : la clarté du protocole ne remplace pas l'audit externe indépendant, qui n'existe pas |
| | Contexte où le relais public est inacceptable : le contenu reste chiffré, mais les métadonnées — adresses, volume, horodatage — sont visibles du relais, et c'est la valeur par défaut |

## Mise en œuvre

- Installation — binaires Windows, macOS, Linux et FreeBSD, plus Homebrew, Scoop, Chocolatey, pacman, apt, apk, image Docker, `go install`, et applications Android sur F-Droid. Un client web existe sur `getcroc.com`, compatible avec la ligne de commande ; les interfaces graphiques référencées dans le dépôt sont des projets tiers non officiels
- Point d'entrée — CLI : `croc send <fichier>` d'un côté, `croc <phrase>` de l'autre. La phrase se passe par la variable d'environnement (`CROC_SECRET=<phrase> croc`), **jamais en argument** — un argument fuite par la liste des processus, CVE-2023-43621, sous Linux et macOS
- Prérequis — aucun : un binaire unique, sans dépendance. Pour un relais à soi, `croc relay` et les ports TCP 9009 à 9013 (deux au minimum, personnalisables par `--ports`), protégés par un mot de passe de relais
- Exécution — de pair à pair quand le réseau le permet, sinon par relais : public par défaut, ou le sien via `--relay hote:9009` et `--pass`, ou les variables `CROC_RELAY` et `CROC_PASS`. Un relais auto-hébergé expose une surface réseau, à filtrer
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- *Aucune alternative déclarée : première entrée en `network/transfert`. Hors brain : `magic-wormhole` (même principe PAKE, écosystème Python), `rsync` sur SSH (la référence pour la synchronisation, mais suppose un accès SSH), Syncthing (synchronisation continue), `rclone` (stockages objet) — tous pointés dans le tableau ci-dessus.*

## Ressources

- Documentation — https://github.com/schollz/croc
- Dépôt — https://github.com/schollz/croc
- Site — https://getcroc.com

## Voir aussi

- [[Réseau]] — le hub du domaine
- [[Sniffnet]] — pour vérifier vers quel relais un transfert part réellement
