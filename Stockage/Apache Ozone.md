---
role: brique
nom: Apache Ozone
alias: [ozone, apache-ozone]
pitch: "Stockage objet distribué d'Apache (Apache 2.0) pour les très gros volumes analytiques sur site : espace de noms à milliards d'objets, accès S3 et système de fichiers Hadoop, erasure coding et cohérence forte par Raft, mais une douzaine de machines au minimum et un S3 sans versioning, Object Lock ni politiques de bucket."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[OpenStack Swift]]", "[[Ceph]]", "[[SeaweedFS]]", "[[MinIO]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://ozone.apache.org/docs/
url_repo: https://github.com/apache/ozone
---

# Apache Ozone

<!-- AUTO:BANDEAU:START -->
> Stockage objet distribué d'Apache (Apache 2.0) pour les très gros volumes analytiques sur site : espace de noms à milliards d'objets, accès S3 et système de fichiers Hadoop, erasure coding et cohérence forte par Raft, mais une douzaine de machines au minimum et un S3 sans versioning, Object Lock ni politiques de bucket.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Système de stockage distribué de la fondation **Apache**, écrit en **Java**, décrit par son
dépôt comme « évolutif, fiable, optimisé pour l'analytique et les charges de stockage objet ».
Il a été conçu pour que des **milliards d'objets** tiennent dans un même espace de noms, ce que
HDFS supporte mal. L'architecture sépare trois rôles : l'**Ozone Manager** (OM) tient l'espace
de noms — volumes, buckets, clés —, le **Storage Container Manager** (SCM) gère la couche
physique des conteneurs de données, et les **Datanodes** stockent. Les métadonnées sont
répliquées par **Ratis**, une implémentation de Raft : le stockage est **fortement cohérent**,
ce qui le distingue des serveurs à cohérence à terme. **Recon** sert à la supervision. On y
accède par une **passerelle S3** et par le système de fichiers Hadoop (**OFS**), donc depuis
Hive, Spark, Flink, Trino ou Iceberg sans HDFS. La frontière de l'outil est son public :
c'est une brique de l'analytique sur site à grande échelle, pas un serveur S3 de remplacement
pour un petit cluster.

*Constat du 2026-09-30 :* version stable **2.2.1**, publiée le 2026-08-27 (la documentation
utilisateur la désigne comme stable) ; la branche précédente continue de recevoir des
correctifs, avec la 2.1.2 le 2026-09-18. La version `latest` de l'API GitHub renvoie cette 2.1.2 :
elle ne désigne pas la version courante. Environ **1,3 k étoiles** GitHub, licence
**Apache 2.0**, dépôt actif (183 pull requests fusionnées entre le 2026-08-30 et le
2026-09-30). Le nombre d'étoiles est modeste parce que le public est celui de l'écosystème
Hadoop, pas celui du S3 généraliste.

## S3 — ce que la passerelle couvre

La page officielle de compatibilité S3 de la version 2.2.1 liste ce qui **est** pris en charge
et ce qui **ne l'est pas**, sans ambiguïté :

- **Pris en charge** — opérations de buckets et d'objets de base, `DeleteObjects`, `CopyObject`, `ListObjectsV2`, étiquettes d'objets, multipart complet, URL présignées.
- **Non pris en charge** — ACL, politiques de bucket, CORS, hébergement de site, **versioning**, **Object Lock**, chiffrement côté serveur S3 (les buckets chiffrés par Ranger KMS existent), S3 Select, **requêtes conditionnelles**, cycle de vie, réplication inter-régions, notifications d'événements.
- **En cours d'arrivée** — la documentation de la prochaine version décrit un cycle de vie partiel (expiration et abandon des multiparts, désactivé par défaut, sans transition). Absent de la version stable.

Pour un usage qui suppose du WORM, du versioning ou des politiques de bucket, la passerelle ne
suffit pas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Très gros volumes analytiques sur site, avec Spark, Hive, Trino ou Iceberg, en remplacement ou en complément de HDFS | Il faut un serveur S3 simple sur quelques machines : le guide de dimensionnement demande 3 nœuds OM et 3 nœuds SCM en haute disponibilité, et au moins 10 Datanodes pour l'erasure coding RS-6-3, 15 pour RS-10-4 → [[SeaweedFS]], [[RustFS]], [[Garage]] |
| Un espace de noms à milliards d'objets, avec cohérence forte par Raft | Le S3 doit être complet : pas de versioning, d'Object Lock, de politiques de bucket ni d'écritures conditionnelles → [[Ceph]], [[SeaweedFS]] |
| Déjà dans l'écosystème Hadoop, avec sécurité Kerberos et Ranger | Pas d'équipe capable d'exploiter un système Java distribué à quatre rôles (OM, SCM, Datanodes, Recon) |
| Erasure coding en 3:2, 6:3 ou 10:4 pour réduire le surcoût de la réplication | Stockage unifié objet, bloc et fichier POSIX → [[Ceph]] |
| | Usage en production attesté surtout en Asie et chez des éditeurs Hadoop : peu de retours indépendants en Europe |

## Mise en œuvre

- Installation — distribution Apache (paquets, images de conteneur), déploiement sur Kubernetes ou sur YARN
- Point d'entrée — la passerelle S3, le système de fichiers OFS de Hadoop, et la CLI `ozone`
- Prérequis — 3 OM et 3 SCM pour la haute disponibilité, un Recon, au moins 10 Datanodes avec erasure coding RS-6-3 ; le guide conseille de ne pas dépasser 400 To bruts par Datanode, des disques NVMe ou SSD pour les métadonnées et les journaux Ratis, et au plus 2:1 de sursouscription réseau
- Exécution — self-hébergé, distribué, sur du matériel standard
- Coût — gratuit sous Apache 2.0 ; support commercial par les distributions qui l'embarquent, dont Cloudera

Les utilisateurs listés par le projet sont Tencent, Cloudera, Shopee, Preferred Networks,
G-Research, Qihoo 360, DiDi, Meituan et China Unicom ; la page ne donne aucun chiffre d'échelle.

## Écosystème

### Alternatives

- [[OpenStack Swift]] — Stockage objet d'OpenStack (Apache 2.0) : proxy, anneau de placement et réplication ou erasure coding, API native Swift plus S3 par middleware ; maintenu mais historique, pertinent dans un parc OpenStack existant, cohérence à terme et sans cycle de vie ni étiquettes S3.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire.

## Ressources

- Documentation — https://ozone.apache.org/docs/
- Dépôt — https://github.com/apache/ozone
- Documentation — https://ozone.apache.org/docs/user-guide/client-interfaces/s3/s3-api
- Documentation — https://ozone.apache.org/docs/administrator-guide/installation/hardware-and-sizing

## Voir aussi

- [[Stockage]] — le hub du domaine
