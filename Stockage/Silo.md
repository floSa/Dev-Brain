---
role: brique
nom: Silo
alias: [silo, pgsty silo, pgsty/silo, pgsty/minio]
pitch: "Fork communautaire de MinIO publié par Pigsty sous AGPL-3.0, avec console web, binaires, paquets et images Docker (`pgsty/silo`, ex-`pgsty/minio`, renommé le 2026-08-06) : un pont de migration pour une installation MinIO existante, mais un seul mainteneur (94 % des commits sur six mois), donc pas un choix pour une nouvelle installation."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: beta
langage: Go
scaling: distributed
alternatives: ["[[MinIO]]", "[[RustFS]]", "[[SeaweedFS]]", "[[Garage]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://silo.pgsty.com/docs/
url_repo: https://github.com/pgsty/silo
---

# Silo

<!-- AUTO:BANDEAU:START -->
> Fork communautaire de MinIO publié par Pigsty sous AGPL-3.0, avec console web, binaires, paquets et images Docker (`pgsty/silo`, ex-`pgsty/minio`, renommé le 2026-08-06) : un pont de migration pour une installation MinIO existante, mais un seul mainteneur (94 % des commits sur six mois), donc pas un choix pour une nouvelle installation.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur de stockage objet **S3-compatible** à héberger soi-même, écrit en **Go** : un **fork
communautaire de MinIO**, publié par Pigsty (une distribution PostgreSQL). Il reprend
le code de MinIO et rend ce que l'éditeur a cessé de distribuer : la console web complète, les
binaires, les paquets RPM, DEB et APK, et les images Docker (`pgsty/silo`, standard et sans
distribution). Il garde le format des données, les variables `MINIO_*` et les routes `/minio/*` :
une installation MinIO existante peut le reprendre sur place, par le guide de migration du projet.
Le dépôt s'appelait `pgsty/minio` ; il a été **renommé `pgsty/silo` le 2026-08-06**, avec le
binaire, le paquet et l'image.

**Un seul mainteneur.** Sur les six derniers mois, un auteur signe 540 des 573 commits (94 %), et
les quatorze autres auteurs se partagent le reste. Pigsty l'exploite en production pour la
sauvegarde de ses clusters PostgreSQL (source : le README), mais le projet repose sur une personne
et une petite structure. C'est un **pont de migration** pour qui a déjà MinIO, pas un choix pour
une nouvelle installation. L'AGPL-3.0 permet à n'importe qui de reprendre le code si le projet
s'arrête ; le manifeste du projet affirme qu'il n'y aura ni CLA ni changement de licence.

*Constat du 2026-10-30 :* version **RELEASE.2026-10-26T00-00-00Z** (publiée le 2026-10-26, console
embarquée v2.5.1), environ **4,4 k étoiles** GitHub, licence **AGPL-3.0** lue dans le fichier
`LICENSE` du dépôt (le README précise « AGPL-3.0-or-later »). L'image `pgsty/silo` de Docker Hub
compte environ 2,6 millions de téléchargements (lu le 2026-10-30).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une installation [[MinIO]] tourne déjà et doit rester à jour : même format de données, même console, correctifs de sécurité publiés | **Nouvelle installation de production** : un seul mainteneur (94 % des commits), la continuité ne tient pas à une équipe → [[SeaweedFS]], [[RustFS]] ou [[Garage]] |
| Des images, des paquets et des binaires sont voulus à la place d'une compilation depuis les sources | Un projet qui doit survivre à son mainteneur sans plan de reprise : le dépôt peut être forké (AGPL), mais personne d'autre n'y contribue aujourd'hui |
| La console web de MinIO doit rester disponible (policies, réplication, supervision) | **Copyleft réseau** : l'AGPL-3.0 peut imposer de publier le code lié à un service exposé — à valider avant un produit fermé |
| Le périmètre « correctifs de bugs et de CVE, pas de fonction nouvelle » suffit | Des fonctions neuves attendues : le projet maintient une ligne de MinIO, il ne la fait pas évoluer |
| | Compatibilité avec le MinIO d'origine seulement « au mieux » : la pile supportée est `silo` + `silo-console` + `mc` + `silo-pkg` |

## Mise en œuvre

- Installation — image `pgsty/silo` (amd64 et arm64), binaires des releases GitHub (Linux, macOS, Windows), paquets RPM, DEB et APK, chart Helm ; chaque release publie ses sommes de contrôle, ses SBOM et des manifestes signés
- Point d'entrée — l'API S3 sur le port 9000, la console web sur le port 9001, le client `mcli` (le `mc` du fork) pour l'administration
- Prérequis — comme MinIO : disques et nœuds cohérents avec le schéma d'erasure coding visé ; reprise d'un MinIO existant par le service systemd et l'utilisateur d'origine, d'après le guide de migration
- Exécution — self-hébergé, du mono-nœud au cluster distribué
- Coût — gratuit sous AGPL-3.0 ; le manifeste du projet exclut de mettre une fonction existante derrière un paiement

## Écosystème

### Alternatives

- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire.
- [[RustFS]] — Stockage objet S3-compatible en Rust sous Apache 2.0, qui vise la succession de MinIO : versioning, Object Lock, réplication et mode distribué au catalogue, mais en version stable depuis le 2026-09-16 seulement et avec des failles IAM encore publiées chaque mois.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.

## Ressources

- Documentation — https://silo.pgsty.com/docs/
- Dépôt — https://github.com/pgsty/silo
- Documentation — https://silo.pgsty.com/compatibility/migration/ (guide de migration depuis MinIO)

## Voir aussi

- [[Stockage]] — le hub du domaine
- [[Stockage objet et API S3]] — la notion : ce que l'API S3 fixe, ce qu'elle laisse à chaque implémentation, et comment choisir un backend on-prem
- [[Comparatif - Stockage objet]] — ce qui départage les briques du dossier
