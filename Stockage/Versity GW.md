---
role: brique
nom: Versity GW
alias: [versity gw, versitygw, versity s3 gateway, versity gateway]
pitch: "Passerelle S3 en Go sous Apache 2.0 qui expose un système de fichiers POSIX, ScoutFS ou Azure Blob comme un serveur S3, ou relaie vers un autre serveur S3 : sans état, sans stockage propre, avec une WebGUI optionnelle et un mode S3 sur RDMA — une passerelle, pas un moteur."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[S3Proxy]]", "[[SeaweedFS]]", "[[RustFS]]", "[[Garage]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://github.com/versity/versitygw/wiki
url_repo: https://github.com/versity/versitygw
---

# Versity GW

<!-- AUTO:BANDEAU:START -->
> Passerelle S3 en Go sous Apache 2.0 qui expose un système de fichiers POSIX, ScoutFS ou Azure Blob comme un serveur S3, ou relaie vers un autre serveur S3 : sans état, sans stockage propre, avec une WebGUI optionnelle et un mode S3 sur RDMA — une passerelle, pas un moteur.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Passerelle S3** écrite en **Go** par Versity Software : un serveur qui parle l'API S3 vers les
clients et traduit chaque requête vers un autre système. Le plus courant est un **système de
fichiers POSIX** (un NAS, un système de fichiers partagé) : une commande suffit pour qu'un
dossier devienne un serveur S3, et les mêmes fichiers restent lisibles en POSIX et en S3. Il sait
aussi parler à ScoutFS (le système de fichiers libre de Versity), à Azure Blob Storage et à
d'autres serveurs S3. La passerelle est **sans état** : plusieurs instances derrière un répartiteur
de charge servent n'importe quelle requête. Elle ne stocke rien et ne protège aucune donnée :
durabilité et capacité sont celles du système en dessous. **Une passerelle, pas un moteur** : elle
ne se compare pas à un serveur de stockage, elle se pose devant un stockage qu'on a déjà.

*Constat du 2026-10-30 :* version **v1.10.0** publiée le 2026-10-22 ; environ **3,1 k étoiles**
GitHub ; licence **Apache 2.0** lue dans le fichier `LICENSE` du dépôt. Sur six mois, 45 auteurs
(54 % des commits pour le premier), un éditeur derrière le projet qui vend du support. Le README
annonce une **WebGUI** de gestion et d'exploration, optionnelle, un hébergement de sites statiques
et l'accès **S3 sur RDMA** (pour le calcul intensif).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des données vivent déjà dans des fichiers (NAS, système de fichiers partagé) et des applications veulent les lire en S3 sans les copier | Un nouveau stockage est à construire : la passerelle n'en fournit pas → [[SeaweedFS]], [[RustFS]] ou [[Garage]] |
| Les mêmes fichiers doivent rester accessibles en POSIX et en S3 | Durabilité attendue de l'outil : elle vient du système de fichiers dessous |
| Un point d'entrée S3 devant un autre serveur S3 ou devant Azure Blob | Réplication entre sites ou erasure coding attendus de l'outil : la passerelle n'en a pas, elle délègue au système dessous |
| Du S3 sur RDMA pour des charges de calcul intensif | Un support commercial exigé : il existe, vendu par Versity, sur contact |

## Mise en œuvre

- Installation — un binaire Go unique (Linux, macOS, BSD, Windows), téléchargé depuis les releases GitHub
- Point d'entrée — l'API S3 ; `versitygw` avec une sous-commande par backend (`posix`, et les autres) ; la WebGUI optionnelle
- Prérequis — un système de fichiers déjà monté et sain ; des comptes IAM (fichier JSON pour les essais, d'après le README)
- Exécution — self-hébergé, instances sans état à multiplier derrière un répartiteur de charge
- Coût — gratuit sous Apache 2.0 ; support entreprise vendu par Versity, sur contact

## Écosystème

### Alternatives

- [[S3Proxy]] — Passerelle S3 en Java sous Apache 2.0 qui traduit l'API S3 vers Azure, Google Cloud, OpenStack Swift, SFTP, un autre S3 ou un dossier local, et sert aussi à tester sans AWS : sans stockage propre ni console, avec un seul mainteneur (99 % des commits sur six mois) — une passerelle, pas un moteur.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[RustFS]] — Stockage objet S3-compatible en Rust sous Apache 2.0, qui vise la succession de MinIO : versioning, Object Lock, réplication et mode distribué au catalogue, mais en version stable depuis le 2026-09-16 seulement et avec des failles IAM encore publiées chaque mois.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.

## Ressources

- Documentation — https://github.com/versity/versitygw/wiki
- Dépôt — https://github.com/versity/versitygw

## Voir aussi

- [[Stockage]] — le hub du domaine
- [[Stockage objet et API S3]] — la notion : ce que l'API S3 fixe, ce qu'elle laisse à chaque implémentation, et comment choisir un backend on-prem
- [[Comparatif - Stockage objet]] — ce qui départage les briques du dossier
