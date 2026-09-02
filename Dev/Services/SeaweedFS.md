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
alternatives: ["[[MinIO]]", "[[Ceph]]", "[[Garage]]", "[[AWS S3]]", "[[Cloudflare R2]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://github.com/seaweedfs/seaweedfs/wiki
url_repo: https://github.com/seaweedfs/seaweedfs
---

# SeaweedFS

## Pourquoi

Système de stockage distribué en **Go** inspiré du papier **Haystack** de Facebook, optimisé pour stocker **des milliards de petits fichiers** avec un accès disque en **O(1)** (environ 40 octets de métadonnées par fichier, une seule lecture disque pour servir). Le cœur est un blob store ; un **Filer** optionnel ajoute répertoires, attributs POSIX et métadonnées, et la couche **S3** expose une API compatible. Erasure coding (idées de *f4*) pour le stockage « tiède ». Sous licence permissive **Apache 2.0** — souvent présenté comme l'alternative à MinIO sans le risque d'une bascule de licence.

## Quand l'utiliser

- Charges à **très grand nombre de petits fichiers** (images, vignettes, fragments) où S3/MinIO peinent.
- Besoin d'une licence **permissive** (Apache 2.0) sans copyleft → vs l'AGPLv3 de [[MinIO]] et [[Garage]].
- S3 *et* système de fichiers (Filer, montage FUSE) sur la même brique.
- Scaling horizontal simple, faible latence en lecture.

## Quand NE PAS l'utiliser

- Besoin de stockage unifié objet + bloc + fichier d'entreprise → [[Ceph]].
- Préférence pour l'écosystème et l'outillage S3 les plus standardisés → [[MinIO]].
- Aucune envie d'opérer l'infra → managé [[AWS S3]] ou [[Cloudflare R2]].

## Déploiement & coût

- Open-source **Apache 2.0**, self-host gratuit ; binaire `weed` unique (rôles master / volume / filer / s3).
- Offre commerciale **SeaweedFS Enterprise** (support, fonctions avancées) ; le cœur reste Apache 2.0.
- Scaling horizontal par ajout de serveurs volume ; erasure coding pour la durabilité.

## Pièges

- Compatibilité S3 sur un **sous-ensemble** de l'API : tester ses intégrations.
- Architecture multi-composants (master / volume / filer / s3) à comprendre avant la prod.
- Le choix du **metadata store** du Filer (LevelDB, Redis, SQL…) conditionne perf et exploitation.
- Moins d'outillage tiers que MinIO autour de l'API S3.

## Alternatives

- [[MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Liens

- [[MinIO]] — alternative S3 auto-hébergée, licence AGPLv3 vs Apache 2.0 ici
- [[Ceph]] — alternative lourde pour stockage unifié à grande échelle
- Doc : https://github.com/seaweedfs/seaweedfs/wiki
