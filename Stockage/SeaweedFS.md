---
role: brique
nom: SeaweedFS
alias: [seaweedfs, seaweed, weed]
pitch: "Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[OpenStack Swift]]", "[[Apache Ozone]]", "[[RustFS]]", "[[MinIO]]", "[[Ceph]]", "[[Garage]]", "[[AWS S3]]", "[[Cloudflare R2]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://github.com/seaweedfs/seaweedfs/wiki
url_repo: https://github.com/seaweedfs/seaweedfs
---

# SeaweedFS

<!-- AUTO:BANDEAU:START -->
> Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | à jour · 2026-09-08 |
<!-- AUTO:BANDEAU:END -->

## Définition

Système de stockage distribué en **Go** inspiré du papier **Haystack** de Facebook, dont le
pari porte sur un cas précis : **des milliards de petits fichiers**. Là où une base objet
classique paie une indirection par fichier, SeaweedFS tient environ 40 octets de métadonnées
par fichier et sert une lecture en **une seule opération disque**, donc en O(1). Le cœur est un
blob store ; un **Filer** optionnel ajoute répertoires, attributs POSIX et métadonnées, et une
couche **S3** expose l'API compatible par-dessus. L'erasure coding, repris des idées de *f4*,
couvre le stockage tiède. Sa licence **Apache 2.0** en fait l'alternative que l'on cite quand
le copyleft réseau d'un concurrent pose problème.

*Constat du 2026-09-30 :* version **4.48**, publiée le 2026-09-28, après 47 releases en douze
mois ; environ **35,1 k étoiles** GitHub. Côté S3, le README et le wiki officiel décrivent
aujourd'hui une couverture bien plus large qu'un « sous-ensemble » : **versioning** (sans MFA
Delete), **Object Lock** (rétention et legal hold), cycle de vie, tagging, CORS, **écritures
conditionnelles** (`If-Match`, `If-None-Match`), URL présignées, multipart, IAM avec politiques de
bucket et conditions, chiffrement côté serveur SSE-S3, SSE-KMS et SSE-C. Restent **non
implémentés**, d'après le wiki : les notifications de bucket, la réplication S3 native
(`PutBucketReplication`), l'hébergement de site web, les règles de transition du cycle de vie et
`SelectObjectContent`. La réplication entre clusters existe, mais par le Filer, pas par l'API S3.
L'erasure coding est **Reed-Solomon RS(10,4)** par défaut (14 fragments, surcoût de 1,4×) et
ne s'applique qu'à des volumes passés en lecture seule ; la réplication par volume reste le mode
par défaut. Les chiffres de performance du README (15 708 écritures et 47 019 lectures par
seconde sur un million de fichiers de 1 Ko) viennent d'un portable, et la page de benchmarks du
wiki, non mise à jour depuis 2018, dit elle-même que ces mesures sont trompeuses : le pari des
petits fichiers est une thèse d'architecture, pas un résultat indépendant.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Charge à **très grand nombre de petits fichiers** — images, vignettes, fragments — où S3 et MinIO peinent | Besoin d'un stockage unifié objet + bloc + fichier d'entreprise → [[Ceph]] |
| Vouloir une licence **permissive** sans copyleft, face à l'AGPLv3 de [[MinIO]] et [[Garage]] | Préférence pour l'écosystème et l'outillage S3 les plus standardisés → [[MinIO]] |
| S3 *et* système de fichiers (Filer, montage FUSE) sur la même brique | Aucune envie d'opérer l'infra → managé [[AWS S3]] ou [[Cloudflare R2]] |
| Scaling horizontal simple et faible latence en lecture | Compatibilité S3 large mais avec des **manques déclarés** — notifications de bucket, réplication S3 native, hébergement de site : tester ses intégrations |
| | Architecture multi-composants — master, volume, filer, s3 — à comprendre avant la production |
| | Le **metadata store** du Filer (LevelDB, Redis, SQL…) conditionne perf et exploitation : ce choix n'est pas un détail |
| | Moins d'outillage tiers que MinIO autour de l'API S3 |

## Mise en œuvre

- Installation — un binaire `weed` unique, ou une image de conteneur
- Point d'entrée — l'API S3, l'API HTTP du blob store, ou le Filer et son montage FUSE
- Prérequis — décider des rôles à lancer (master, volume, filer, s3) et du metadata store du Filer
- Exécution — self-hébergé, distribué : scaling horizontal par ajout de serveurs volume, erasure coding pour la durabilité
- Coût — gratuit, Apache 2.0 pour le cœur ; une offre **SeaweedFS Enterprise**, sous licence à clé appliquée à un cluster libre, ajoute l'erasure coding paramétrable (20+4 par exemple), la réparation automatique, la restauration d'objets supprimés, le multi-locataire et le support ; gratuite sous 25 To en dev/test, sinon 2 $/To/mois ou 20 $/To/an (source : seaweedfs.com, 2026-09-30)

## Écosystème

### Alternatives

- [[OpenStack Swift]] — Stockage objet d'OpenStack (Apache 2.0) : proxy, anneau de placement et réplication ou erasure coding, API native Swift plus S3 par middleware ; maintenu mais historique, pertinent dans un parc OpenStack existant, cohérence à terme et sans cycle de vie ni étiquettes S3.
- [[Apache Ozone]] — Stockage objet distribué d'Apache (Apache 2.0) pour les très gros volumes analytiques sur site : espace de noms à milliards d'objets, accès S3 et système de fichiers Hadoop, erasure coding et cohérence forte par Raft, mais une douzaine de machines au minimum et un S3 sans versioning, Object Lock ni politiques de bucket.
- [[RustFS]] — Stockage objet S3-compatible en Rust sous Apache 2.0, qui vise la succession de MinIO : versioning, Object Lock, réplication et mode distribué au catalogue, mais en version stable depuis le 2026-09-16 seulement et avec des failles IAM encore publiées chaque mois.
- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Ressources

- Documentation — https://github.com/seaweedfs/seaweedfs/wiki
- Dépôt — https://github.com/seaweedfs/seaweedfs

## Voir aussi

- [[Stockage]] — le hub du domaine
- [[Stockage objet et API S3]] — la notion : ce que l'API S3 fixe, ce qu'elle laisse à chaque implémentation, et comment choisir un backend on-prem
- [[Comparatif - Stockage objet]] — ce qui départage les briques du dossier
