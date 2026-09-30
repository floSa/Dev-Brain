---
role: brique
nom: MinIO
alias: [minio]
pitch: "Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: deprecated
langage: Go
scaling: distributed
alternatives: ["[[Apache Ozone]]", "[[RustFS]]", "[[Ceph]]", "[[SeaweedFS]]", "[[Garage]]", "[[AWS S3]]", "[[Cloudflare R2]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://min.io/docs/minio/linux/index.html
url_repo: https://github.com/minio/minio
---

# MinIO

<!-- AUTO:BANDEAU:START -->
> Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | deprecated | dépôt archivé · 2026-04-25 |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur de stockage objet **S3-compatible** écrit en **Go**, pensé pour être posé sur ses
propres machines : un seul binaire expose l'API S3, et l'on obtient « son S3 » en local ou dans
son cloud. En mode distribué, la tolérance aux pannes de disque et de nœud passe par de
l'**erasure coding**, sans RAID. C'est le moyen courant d'avoir l'API S3 sans AWS, et son usage
le plus fréquent n'est même pas la production : un conteneur MinIO sert de S3 de développement
et de CI. Les décisions de l'éditeur, prises entre 2025 et 2026, pèsent aujourd'hui plus lourd
que la technique : l'édition libre a perdu sa console d'administration, puis ses binaires, puis
sa maintenance, et le dépôt est **archivé**. La fiche est donc classée **abandonnée** : c'est
le critère qui écarte une brique des propositions automatiques, et le README du projet dit
lui-même que toute production bâtie sur des binaires compilés depuis les sources l'est « à ses
propres risques ».

*Constat du 2026-09-30 :* dépôt `minio/minio` archivé par son propriétaire le **2026-04-25**
(bannière GitHub, lecture seule) ; environ **61,3 k étoiles** ; dernière release
`RELEASE.2025-10-15T17-29-55Z`, publiée le 2025-10-16 — un correctif d'élévation de privilèges
par contournement des session policies des comptes de service et de STS. Aucune release
depuis, et aucun correctif de sécurité officiel à attendre.

## Chronologie — comment l'édition libre s'est arrêtée

- **Mai 2025** — la console web d'administration est retirée de la Community Edition : il ne reste qu'un navigateur d'objets, le reste passe par `mc` (source : Blocks & Files, 2025-06-19).
- **Octobre 2025** — plus de binaires ni d'images Docker officiels (source : It's FOSS ; le README actuel confirme : « distributed as source code only »).
- **2025-12-03** — le README annonce un projet « en maintenance » qui n'accepte plus de changements : ni fonction, ni amélioration, ni pull request ; les correctifs de sécurité critiques sont examinés « au cas par cas » (commit `27742d46`).
- **2025-12-23** — l'éditeur annonce trois paliers AIStor : *Free* (licence propriétaire qui limite la redistribution, **mononœud uniquement**), *Enterprise Lite* (multinœud, moins de 400 TiB) et *Enterprise*. Les prix ne sont pas publics.
- **2026-02-12** — le README devient « THIS REPOSITORY IS NO LONGER MAINTAINED » et renvoie vers AIStor (commit `7aac2a2c`).
- **2026-04-25** — dépôt archivé. Les sources divergent sur la date (It's FOSS la place au 25 avril, un billet de Pigsty au 12 février, date du dernier commit de README) ; la bannière GitHub lue ce jour donne le 25 avril.

## Forks et suites

- **AIStor** — l'offre de l'éditeur. *Free* n'est pas une option de cluster : mononœud, licence propriétaire. Le multinœud est payant, sur devis.
- **`pgsty/minio`** — fork communautaire de Pigsty, **AGPL-3.0**, créé le 2025-10-25, environ 3,6 k étoiles, dernière release le 2026-09-16. Il rétablit la console, les binaires, les images et les paquets RPM/DEB. Périmètre annoncé : correctifs de bugs et de CVE, pas de fonction nouvelle. Il est maintenu par une petite structure, non affiliée à MinIO Inc. (source : billet de son mainteneur, partie prenante).
- **OpenMaxIO** — fork de la console seule, inactif depuis juin 2025 : pas une suite.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Maintenir une installation existante le temps de migrer : les binaires déjà déployés continuent de tourner | **Toute nouvelle installation de production** : dépôt archivé, aucune release depuis octobre 2025, plus de correctif de sécurité officiel → [[RustFS]], [[SeaweedFS]], [[Ceph]] |
| S3 de développement ou de CI avec une image figée, là où une faille n'expose aucune donnée réelle | Il faut **compiler soi-même** : la Community Edition est distribuée en sources uniquement, sans binaire ni image officiels |
| Rester sur la base de code MinIO avec des correctifs de sécurité : le fork `pgsty/minio` existe, à évaluer comme dépendance (petite structure, périmètre limité aux correctifs) | La **console web d'administration** est retirée de l'édition libre — policies, réplication et supervision passent par la CLI `mc` ou par l'offre payante |
| | L'**AGPLv3** est un copyleft réseau : exposer un service bâti sur MinIO peut imposer de publier le code lié — à valider juridiquement |
| | AIStor, la suite de l'éditeur : *Free* est mononœud et propriétaire, le multinœud est payant, sur devis |
| | Aucune envie d'opérer disques, nœuds et mises à jour → managé [[AWS S3]] ou [[Cloudflare R2]] |
| | Compatibilité S3 large mais **partielle** : certains cas limites d'AWS ne sont pas couverts, tester ses intégrations |
| | Erasure coding et quorum à dimensionner : un cluster sous-dimensionné perd en disponibilité |

## Mise en œuvre

- Installation — build depuis les sources (`go install`) ; plus de binaire ni d'image officiels côté libre depuis octobre 2025 (le fork `pgsty/minio` en fournit)
- Point d'entrée — l'API S3, et la CLI `mc` pour l'administration
- Prérequis — plusieurs nœuds et un nombre de disques cohérent avec le schéma d'erasure coding visé : ensembles de 2 à 16 disques (jusqu'à 32 par réglage), parité EC:3 ou plus en production d'après la documentation de l'éditeur, par exemple EC:4 sur 16 disques pour 75 % d'espace utile
- Exécution — self-hébergé, du mono-nœud au cluster distribué
- Coût — gratuit sous AGPLv3 pour le cœur, sans maintenance. **AIStor** (ex-Enterprise) porte la console d'admin, le support et les fonctions avancées : *Free* mononœud et propriétaire, *Enterprise Lite* sous 400 TiB, *Enterprise* avec support 24/7, sur devis

## Écosystème

### Alternatives

- [[Apache Ozone]] — Stockage objet distribué d'Apache (Apache 2.0) pour les très gros volumes analytiques sur site : espace de noms à milliards d'objets, accès S3 et système de fichiers Hadoop, erasure coding et cohérence forte par Raft, mais une douzaine de machines au minimum et un S3 sans versioning, Object Lock ni politiques de bucket.
- [[RustFS]] — Stockage objet S3-compatible en Rust sous Apache 2.0, qui vise la succession de MinIO : versioning, Object Lock, réplication et mode distribué au catalogue, mais en version stable depuis le 2026-09-16 seulement et avec des failles IAM encore publiées chaque mois.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Ressources

- Documentation — https://min.io/docs/minio/linux/index.html
- Dépôt — https://github.com/minio/minio (archivé)
- Dépôt — https://github.com/pgsty/minio (fork communautaire)
- Article — https://www.min.io/blog/introducing-new-subscription-tiers-for-minio-aistor-free-enterprise-lite-and-enterprise

## Voir aussi

- [[Stockage]] — le hub du domaine
