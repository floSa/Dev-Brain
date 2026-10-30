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
alternatives: ["[[Silo]]", "[[Apache Ozone]]", "[[RustFS]]", "[[Ceph]]", "[[SeaweedFS]]", "[[Garage]]", "[[AWS S3]]", "[[Cloudflare R2]]"]
complements: ["[[Delta Lake]]", "[[lakeFS]]", "[[DVC]]", "[[RAGFlow]]", "[[Trino]]"]
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

Serveur de stockage objet **S3-compatible** écrit en **Go**, à héberger soi-même : un binaire
expose l'API S3, et la tolérance aux pannes passe par de l'**erasure coding**, sans RAID. Il a
été le moyen courant d'avoir « son S3 » sans AWS, et son usage le plus fréquent était un S3 de
développement et de CI en conteneur. La fiche est classée **abandonnée** et reste au brain comme
**repère** : sa chute est la raison du comparatif du dossier. Pourquoi : l'éditeur a retiré en
2025 la console d'administration, puis les binaires et les images, puis la maintenance ; le dépôt
est **archivé**, et ses images ont disparu de Docker Hub en septembre 2026. Le README du projet dit
lui-même que toute production bâtie sur des binaires compilés depuis les sources l'est « à ses
propres risques ». **Où aller** : [[Silo]] si une installation MinIO existe et doit rester à jour ;
[[SeaweedFS]], [[RustFS]] ou [[Garage]] pour une nouvelle installation (voir le
[[Comparatif - Stockage objet]]).

*Constat du 2026-10-30 :* dépôt `minio/minio` archivé en lecture seule (dernier push le
2026-04-24, bannière « THIS REPOSITORY IS NO LONGER MAINTAINED ») ; environ **61,3 k étoiles** ;
licence **AGPL-3.0** ; dernière release `RELEASE.2025-10-15T17-29-55Z`, publiée le 2025-10-16 (un
correctif d'élévation de privilèges sur les session policies des comptes de service et de STS).
Aucune release depuis, aucun correctif de sécurité officiel à attendre.

## Chronologie — comment l'édition libre s'est arrêtée

- **Mai 2025** — la console web d'administration est retirée de la Community Edition : il ne reste qu'un navigateur d'objets, le reste passe par `mc` (source : Blocks & Files, 2025-06-19).
- **Octobre 2025** — plus de binaires ni d'images Docker officiels côté libre (source : It's FOSS ; le README confirme : « distributed as source code only »).
- **2025-12-03** — le README annonce un projet « en maintenance » qui n'accepte plus de changements ; les correctifs de sécurité critiques sont examinés « au cas par cas ».
- **2025-12-23** — trois paliers AIStor : *Free* (licence propriétaire, **mononœud uniquement**), *Enterprise Lite* (multinœud, moins de 400 TiB) et *Enterprise* ; prix non publics.
- **2026-02-12** — le README devient « THIS REPOSITORY IS NO LONGER MAINTAINED » et renvoie vers AIStor.
- **2026-04-24** — dernier push, dépôt archivé (les sources donnent le 24 ou le 25 avril : bannière GitHub, It's FOSS).
- **2026-08-06** — le fork de Pigsty devient [[Silo]] (le dépôt `pgsty/minio` est renommé `pgsty/silo`).
- **2026-09-11** — les dépôts `minio/minio` et `minio/mc` disparaissent de **Docker Hub**. Preuves : le ticket `xtdb/xtdb#6061` du 2026-09-11 (« withdrawn from Docker Hub », l'API répond 404) et `milvus-io/milvus#53430` du 2026-09-14 (le `docker compose` de développement ne démarre plus). Lu le 2026-10-30 : l'API de Docker Hub répond toujours 404 pour les deux dépôts, et `dl.min.io` répond **410** pour les binaires du serveur et du client. Pour `quay.io/minio/minio`, l'API répond comme pour un dépôt qui n'existe pas (401, alors que `quay.io/minio/operator` répond 200) : retiré ou privé, la sortie ne tranche pas. Aucune annonce de l'éditeur trouvée.

## Où aller

- **Une installation MinIO existe** → [[Silo]] : même code, même format de données, console, binaires, paquets et images. Un seul mainteneur : un pont de migration, pas une destination.
- **Une nouvelle installation** → [[SeaweedFS]] (le plus de recul, couverture S3 large), [[RustFS]] (le plus proche des habitudes MinIO, à réévaluer), [[Garage]] (petit cluster réparti), [[Ceph]] pour du bloc et du fichier en plus.
- **AIStor**, l'offre de l'éditeur : *Free* est mononœud et propriétaire, le multinœud est payant sur devis. Hors périmètre du brain (pas de page pour un logiciel fermé).
- OpenMaxIO, fork de la console seule, est inactif depuis juin 2025 : ce n'est pas une suite.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Garder une installation existante le temps de migrer : les binaires déjà déployés continuent de tourner | **Toute nouvelle installation** : dépôt archivé, plus de release depuis octobre 2025, plus de correctif de sécurité officiel → [[SeaweedFS]], [[RustFS]], [[Garage]] |
| Un S3 de développement ou de CI sur une image figée que l'on a déjà en cache, là où une faille n'expose aucune donnée réelle | Il faut **récupérer l'image ou le binaire** : `minio/minio` et `minio/mc` ont disparu de Docker Hub, et `dl.min.io` répond 410 |
| Rester sur la base de code MinIO avec des correctifs : [[Silo]] | La **console web d'administration** : retirée de l'édition libre |
| | L'**AGPLv3** est un copyleft réseau : exposer un service bâti sur MinIO peut imposer de publier le code lié |

## Mise en œuvre

- Installation — build depuis les sources (`go install`) ; plus de binaire ni d'image officiels côté libre, et les images ont quitté Docker Hub en septembre 2026
- Point d'entrée — l'API S3, et la CLI `mc` pour l'administration
- Prérequis — plusieurs nœuds et un nombre de disques cohérent avec le schéma d'erasure coding visé ; parité EC:3 ou plus en production d'après la documentation de l'éditeur
- Exécution — self-hébergé, du mono-nœud au cluster distribué
- Coût — gratuit sous AGPLv3, sans maintenance ; la suite **AIStor** est propriétaire

## Écosystème

### Alternatives

- [[Silo]] — Fork communautaire de MinIO publié par Pigsty sous AGPL-3.0, avec console web, binaires, paquets et images Docker (`pgsty/silo`, ex-`pgsty/minio`, renommé le 2026-08-06) : un pont de migration pour une installation MinIO existante, mais un seul mainteneur (94 % des commits sur six mois), donc pas un choix pour une nouvelle installation.
- [[Apache Ozone]] — Stockage objet distribué d'Apache (Apache 2.0) pour les très gros volumes analytiques sur site : espace de noms à milliards d'objets, accès S3 et système de fichiers Hadoop, erasure coding et cohérence forte par Raft, mais une douzaine de machines au minimum et un S3 sans versioning, Object Lock ni politiques de bucket.
- [[RustFS]] — Stockage objet S3-compatible en Rust sous Apache 2.0, qui vise la succession de MinIO : versioning, Object Lock, réplication et mode distribué au catalogue, mais en version stable depuis le 2026-09-16 seulement et avec des failles IAM encore publiées chaque mois.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

### Compléments

- [[Delta Lake]] — Format de table ouvert pour le lakehouse, sous la Linux Foundation : un journal de transactions `_delta_log` au-dessus de fichiers Parquet, ACID, time travel, MERGE, évolution de schéma et Change Data Feed ; implémentations Spark, Rust (delta-rs) et Delta Kernel en Apache-2.0, avec des fonctions d'optimisation propres à Databricks hors de l'open source. — stockage S3-compatible décrit par la documentation de delta-rs (`aws_conditional_put`) et cité parmi les intégrations communautaires de Delta.
- [[lakeFS]] — Versionnage d'un dépôt d'objets à la manière de Git — branches, commits, merges atomiques, retour en arrière, hooks — au-dessus d'un stockage S3-compatible, sans copier les données ; serveur Go avec PostgreSQL, sous licence BSL 1.1 depuis la v1.87.0 (usage interne non modifié), édition libre limitée à un utilisateur. — exemple de configuration de la page d'installation sur site de lakeFS (`force_path_style: true`).
- [[DVC]] — Versionnage de données et de modèles en ligne de commande, posé sur Git : des pointeurs `.dvc` dans le dépôt, le contenu dans un cache adressé par le hash et des remotes (S3 compatible, SSH, NAS), plus des pipelines reproductibles par `dvc repro` ; Apache-2.0, projet racheté par lakeFS en novembre 2025. — remote S3-compatible cité par la documentation de DVC.
- [[RAGFlow]] — Moteur RAG clé en main (Apache-2.0, InfiniFlow) — parsing de documents par mise en page (DeepDoc, OCR, tables), chunking par modèles, recherche hybride avec reranking, GraphRAG, agents et serveur MCP ; lourd : un moteur de documents, MySQL, MinIO et un cache.
- [[Trino]] — Moteur de requête SQL distribué et fédéré, séparé du stockage : une requête interactive joint des tables Iceberg, Delta ou Hive et des bases (PostgreSQL, MySQL…) sans rien stocker lui-même ; Apache-2.0, coordinateur et workers en Java. — moteur SQL sur les tables du stockage objet ; MinIO est testé pour l'exchange manager.

## Ressources

- Documentation — https://min.io/docs/minio/linux/index.html
- Dépôt — https://github.com/minio/minio (archivé)
- Article — https://www.min.io/blog/introducing-new-subscription-tiers-for-minio-aistor-free-enterprise-lite-and-enterprise

## Voir aussi

- [[Stockage]] — le hub du domaine
- [[Stockage objet et API S3]] — la notion : ce que l'API S3 fixe, ce qu'elle laisse à chaque implémentation, et comment choisir un backend on-prem
- [[Comparatif - Stockage objet]] — ce qui départage les briques du dossier
