---
role: brique
nom: RustFS
alias: [rustfs, rust fs]
pitch: "Stockage objet S3-compatible en Rust sous Apache 2.0, qui vise la succession de MinIO : versioning, Object Lock, réplication et mode distribué au catalogue, mais en version stable depuis le 2026-09-16 seulement et avec des failles IAM encore publiées chaque mois."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: beta
langage: Rust
scaling: distributed
alternatives: ["[[MinIO]]", "[[SeaweedFS]]", "[[Garage]]", "[[Ceph]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://docs.rustfs.com/
url_repo: https://github.com/rustfs/rustfs
---

# RustFS

<!-- AUTO:BANDEAU:START -->
> Stockage objet S3-compatible en Rust sous Apache 2.0, qui vise la succession de MinIO : versioning, Object Lock, réplication et mode distribué au catalogue, mais en version stable depuis le 2026-09-16 seulement et avec des failles IAM encore publiées chaque mois.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Rust | open-source | self-hébergé · distribué | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur de stockage objet **S3-compatible** écrit en **Rust**, édité par RustFS, Inc. et publié
sous **Apache 2.0**, sans clause restrictive. Son positionnement est explicite : reprendre la
place que MinIO laisse vacante depuis l'archivage de son dépôt communautaire (cf. [[MinIO]]).
Le README annonce un système « distribué » pour les lacs de données et les charges d'IA, avec
un seul binaire, une console web, des charts Helm, et un catalogue de fonctions large :
versioning, **Object Lock (WORM)**, protection contre la corruption silencieuse (bitrot),
chiffrement côté serveur avec un KMS intégré, réplication de buckets et de sites, cycle de vie
(ILM), IAM et politiques, SSO OIDC, en plus de protocoles annexes (Swift, SFTP, FTPS, WebDAV).
Deux fonctions restent marquées **Preview** par le projet : S3 Tables (API REST Iceberg) et la
**compatibilité avec les disques MinIO**, donc la reprise en place d'un cluster MinIO existant.
La frontière de l'outil n'est pas le catalogue, c'est l'âge : sa première version date de
juillet 2025, et la version stable de septembre 2026.

*Constat du 2026-09-30 :* version **1.0.0**, publiée le **2026-09-16** ; environ **34,2 k
étoiles** GitHub. Chronologie lue dans les releases du dépôt : première alpha le 2025-07-02,
première bêta le 2026-04-29, première version candidate le 2026-08-08, stable le 2026-09-16.
Des préversions `1.0.1-preview` ont déjà suivi.

## Maturité — à lire avant d'adopter

La fiche est classée **bêta**, par prudence, alors que le projet se déclare prêt pour la
production depuis le 2026-09-16. Les raisons :

- **Deux semaines de version stable.** L'annonce de la 1.0.0 dit que la capacité centrale, l'objet, est stable et utilisable en production. Elle ne donne ni limite connue ni guide de migration depuis la bêta (source : https://rustfs.com/blog/announcing-rustfs-1-0-0-ga/, 2026-09-16). Les sources antérieures à la 1.0 disaient « alpha, ne pas utiliser en production » ; elles sont dépassées, mais elles datent de quelques mois.
- **Avis de sécurité nombreux.** L'API GitHub du dépôt liste **35 avis** publiés entre le 2025-12-30 et le 2026-09-08 (lue le 2026-09-30). Plusieurs sont critiques ou élevés et touchent exactement ce qui compte pour un stockage souverain : création de comptes de service sous root par un import IAM (2026-05-09), secret HMAC par défaut pour les appels entre nœuds (2026-05-09), contournement de l'Object Lock quand les métadonnées d'un bucket sont illisibles (2026-08-09). Le dernier, du 2026-09-08, vise la 1.0.0-beta.12. Le dépôt corrige vite ; la densité de failles d'authentification montre que la surface est encore en cours de durcissement.
- **Aucune évaluation indépendante postérieure à la version stable** n'a été trouvée.

Ce n'est pas un défaut de licence : c'est l'inverse de MinIO, dont le code est ancien et
l'éditeur parti. Ici, le code est jeune et l'éditeur actif.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un successeur **Apache 2.0** à MinIO est voulu, sans copyleft réseau et avec console, Object Lock et réplication dans l'édition libre | La donnée est critique et l'outil doit avoir fait ses preuves : quinze mois de préversions, deux semaines de version stable → [[Ceph]] ou [[SeaweedFS]] |
| Pilote ou préproduction on-prem pour évaluer un remplaçant de MinIO sur ses propres charges | Reprise en place d'un cluster MinIO existant : la compatibilité avec les disques MinIO est encore en Preview |
| Besoin de WORM et de versioning, que [[Garage]] n'offre pas | Conformité ou audit de sécurité exigeant : 35 avis publiés en neuf mois, à relire un par un |
| Objets de petite taille en volume, si les chiffres du projet se confirment sur son matériel | Les chiffres de performance disponibles viennent du projet (2,3× MinIO sur des objets de 4 Ko) ou d'un essai individuel dont les politiques de durabilité diffèrent entre systèmes : rien d'indépendant |
| | Support commercial en production : l'offre existe (RustFS, Inc., aide à la migration depuis MinIO) mais sans prix public |

## Mise en œuvre

- Installation — binaire unique ou image de conteneur ; charts Helm pour Kubernetes
- Point d'entrée — l'API S3, la console web, et l'interface de gestion des utilisateurs, politiques et réplication
- Prérequis — à dimensionner selon la documentation du projet ; le mode distribué est annoncé disponible, sans détail technique dans l'annonce de la 1.0.0
- Exécution — self-hébergé, du mono-nœud au cluster distribué
- Coût — gratuit sous Apache 2.0 ; support entreprise et aide à la migration sur devis

## Écosystème

### Alternatives

- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.

## Ressources

- Documentation — https://docs.rustfs.com/
- Dépôt — https://github.com/rustfs/rustfs
- Article — https://rustfs.com/blog/announcing-rustfs-1-0-0-ga/

## Voir aussi

- [[Stockage]] — le hub du domaine
