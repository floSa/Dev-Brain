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

<!-- AUTO:BANDEAU:START -->
> Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production |
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

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Charge à **très grand nombre de petits fichiers** — images, vignettes, fragments — où S3 et MinIO peinent | Besoin d'un stockage unifié objet + bloc + fichier d'entreprise → [[Ceph]] |
| Vouloir une licence **permissive** sans copyleft, face à l'AGPLv3 de [[MinIO]] et [[Garage]] | Préférence pour l'écosystème et l'outillage S3 les plus standardisés → [[MinIO]] |
| S3 *et* système de fichiers (Filer, montage FUSE) sur la même brique | Aucune envie d'opérer l'infra → managé [[AWS S3]] ou [[Cloudflare R2]] |
| Scaling horizontal simple et faible latence en lecture | Compatibilité S3 sur un **sous-ensemble** de l'API : tester ses intégrations |
| | Architecture multi-composants — master, volume, filer, s3 — à comprendre avant la production |
| | Le **metadata store** du Filer (LevelDB, Redis, SQL…) conditionne perf et exploitation : ce choix n'est pas un détail |
| | Moins d'outillage tiers que MinIO autour de l'API S3 |

## Mise en œuvre

- Installation — un binaire `weed` unique, ou une image de conteneur
- Point d'entrée — l'API S3, l'API HTTP du blob store, ou le Filer et son montage FUSE
- Prérequis — décider des rôles à lancer (master, volume, filer, s3) et du metadata store du Filer
- Exécution — self-hébergé, distribué : scaling horizontal par ajout de serveurs volume, erasure coding pour la durabilité
- Coût — gratuit, Apache 2.0 pour le cœur ; une offre **SeaweedFS Enterprise** couvre support et fonctions avancées

## Écosystème

### Alternatives

- [[MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Ressources

- Documentation — https://github.com/seaweedfs/seaweedfs/wiki
- Dépôt — https://github.com/seaweedfs/seaweedfs

## Voir aussi

- [[Stockage]] — le hub du domaine
