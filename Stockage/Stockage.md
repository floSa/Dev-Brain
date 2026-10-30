---
role: hub
nom: Stockage
alias: [stockage, storage, stockage objet, object storage, s3]
pitch: Ranger des fichiers en masse et les servir par le réseau — le sol sur lequel reposent les lakehouses et les artefacts de modèle.
domaines: [data-eng, mlops, infra-ops]
tags: [object-storage, s3-compatible, self-hosted]
---

# Stockage

> Ranger des fichiers en masse et les servir par le réseau — le sol sur lequel reposent les lakehouses et les artefacts de modèle.

## Ce qu'il faut comprendre

- Le stockage **objet** est la seule famille peuplée du domaine, et ce n'est pas un hasard : c'est celle sur laquelle repose tout le reste de la pile data moderne. Un lakehouse, un registre de modèles, un cache de features sont des conventions posées sur des objets.
- Un objet n'est pas un fichier. Pas d'arborescence réelle (le `/` est dans la clé), pas d'écriture partielle, pas de renommage atomique. C'est ce qui rend le stockage objet extensible à l'infini, et ce qui oblige les formats de table (Delta, [[Apache Iceberg|Iceberg]]) à réinventer la transaction par-dessus.
- Douze briques, une seule interface : toutes parlent **S3** (Swift parle aussi son API native). Le code applicatif ne les distingue pas, ce qui déplace la décision vers l'exploitation — qui héberge, à quel coût, avec quelle équipe — et vers ce que l'API ne fixe pas : fonctions réellement couvertes (versioning, Object Lock), état du projet, licence. La notion [[Stockage objet et API S3]] détaille ce contrat, et le [[Comparatif - Stockage objet]] les départage, avec étoiles, licence et console web de chacune.
- Quatre natures se cachent derrière l'interface commune, et elles n'ont pas les mêmes contraintes. Un **service managé** ([[AWS S3]], [[Cloudflare R2]]) ne demande aucune exploitation mais facture le stockage, les requêtes et parfois la sortie. Un **serveur objet** ([[SeaweedFS]], [[RustFS]], [[Garage]], [[Silo]], et [[MinIO]], aujourd'hui abandonné) est un binaire qu'on installe et qu'on sauvegarde soi-même. Un **système de stockage distribué** ([[Ceph]], [[Apache Ozone]], [[OpenStack Swift]]) est une infrastructure à part entière, avec l'équipe qui va avec. Une **passerelle** ([[Versity GW]], [[S3Proxy]]) n'a pas de stockage propre : elle traduit S3 vers des fichiers, Azure, Swift ou SFTP qui existent déjà, et ne se compare pas aux serveurs.
- Le poste de coût qui surprend n'est pas le stockage mais l'**égress** : sortir la donnée du fournisseur. C'est l'argument central de [[Cloudflare R2]], qui ne le facture pas, et une raison fréquente de rapatrier en on-prem.
- La forme des objets décide plus qu'on ne croit. **Beaucoup de petits fichiers** est le cas qui met en difficulté la plupart des moteurs — d'où [[SeaweedFS]], conçu pour ça. **Peu de gros fichiers** convient à tout le monde.

## Choisir

- Déjà sur AWS → [[AWS S3]], et la question ne se pose pas.
- Beaucoup de lectures depuis l'extérieur → [[Cloudflare R2]], pour l'égress gratuit.
- Un serveur S3 self-hébergé pour la production, avec une licence sans copyleft → [[SeaweedFS]] ; son concurrent direct né de l'arrêt de MinIO, [[RustFS]], est à réévaluer dans six mois avant de s'y fier (version stable du 2026-09-16, avis de sécurité encore nombreux).
- Une installation [[MinIO]] existante → la garder le temps de migrer, ou la remplacer par [[Silo]], le fork communautaire qui rend console, binaires et images (un seul mainteneur : un pont, pas une destination). Le dépôt MinIO est archivé et ses images ont quitté Docker Hub en septembre 2026.
- Des données déjà dans un système de fichiers, à servir en S3 → [[Versity GW]] ; traduire S3 vers Azure, Google Cloud, Swift ou SFTP, ou un S3 de test → [[S3Proxy]]. Des passerelles, pas des moteurs.
- Du WORM (Object Lock) sur site → [[SeaweedFS]], [[Ceph]] ou [[RustFS]] ; ni [[Garage]] ni [[Apache Ozone]] ne l'offrent.
- Plusieurs petits sites, liens lents, matériel hétérogène → [[Garage]] (sans console intégrée à ce jour).
- Des milliards de petits objets → [[SeaweedFS]].
- Un besoin de stockage unifié bloc + fichier + objet à l'échelle du datacenter → [[Ceph]].
- De l'analytique Hadoop ou Spark sur des milliards d'objets, sur site → [[Apache Ozone]].
- Un cloud privé OpenStack existant → [[OpenStack Swift]], qui n'est pas un choix de nouvelle installation.

<!-- AUTO:START -->
### Notions
- [[Stockage objet et API S3]] — domaines : data-eng, mlops, infra-ops

### Briques
- [[Apache Ozone]] — Stockage objet distribué d'Apache (Apache 2.0) pour les très gros volumes analytiques sur site : espace de noms à milliards d'objets, accès S3 et système de fichiers Hadoop, erasure coding et cohérence forte par Raft, mais une douzaine de machines au minimum et un S3 sans versioning, Object Lock ni politiques de bucket.
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire.
- [[OpenStack Swift]] — Stockage objet d'OpenStack (Apache 2.0) : proxy, anneau de placement et réplication ou erasure coding, API native Swift plus S3 par middleware ; maintenu mais historique, pertinent dans un parc OpenStack existant, cohérence à terme et sans cycle de vie ni étiquettes S3.
- [[RustFS]] — Stockage objet S3-compatible en Rust sous Apache 2.0, qui vise la succession de MinIO : versioning, Object Lock, réplication et mode distribué au catalogue, mais en version stable depuis le 2026-09-16 seulement et avec des failles IAM encore publiées chaque mois.
- [[S3Proxy]] — Passerelle S3 en Java sous Apache 2.0 qui traduit l'API S3 vers Azure, Google Cloud, OpenStack Swift, SFTP, un autre S3 ou un dossier local, et sert aussi à tester sans AWS : sans stockage propre ni console, avec un seul mainteneur (99 % des commits sur six mois) — une passerelle, pas un moteur.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Silo]] — Fork communautaire de MinIO publié par Pigsty sous AGPL-3.0, avec console web, binaires, paquets et images Docker (`pgsty/silo`, ex-`pgsty/minio`, renommé le 2026-08-06) : un pont de migration pour une installation MinIO existante, mais un seul mainteneur (94 % des commits sur six mois), donc pas un choix pour une nouvelle installation.
- [[Versity GW]] — Passerelle S3 en Go sous Apache 2.0 qui expose un système de fichiers POSIX, ScoutFS ou Azure Blob comme un serveur S3, ou relaie vers un autre serveur S3 : sans état, sans stockage propre, avec une WebGUI optionnelle et un mode S3 sur RDMA — une passerelle, pas un moteur.

### Comparatifs
- [[Comparatif - Stockage objet]]
<!-- AUTO:END -->
