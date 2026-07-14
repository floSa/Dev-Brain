---
galaxie: dev
type: service
nom: AWS S3
alias: [s3, amazon s3, aws-s3]
pitch: "Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS."
categorie: storage
licence_type: proprietary
hosted: managed
maturite: production
langage: 
scaling: serverless
alternatives: ["[[Dev/Services/MinIO|MinIO]]", "[[Dev/Services/Ceph|Ceph]]", "[[Dev/Services/SeaweedFS|SeaweedFS]]", "[[Dev/Services/Garage|Garage]]", "[[Dev/Services/Cloudflare R2|Cloudflare R2]]"]
remplace_par: []
status: actif
tags: [object-storage]
url_docs: https://docs.aws.amazon.com/s3/
url_repo: 
---

# AWS S3

## Pourquoi

Amazon Simple Storage Service : le stockage objet qui a défini la catégorie et dont l'API est devenue le standard de fait. Les données vivent dans des **buckets**, adressées par clé, sans hiérarchie de fichiers réelle. Conçu pour une **durabilité de 99,999999999 % (11 neuf)** via réplication sur au moins 3 zones de disponibilité, et une capacité **quasi illimitée** sans provisionnement. Au cœur de l'écosystème AWS (Lambda, Athena, Glue, CloudFront) : c'est souvent le point de gravité d'une architecture data sur AWS.

## Quand l'utiliser

- Déjà sur AWS : intégration native avec le reste des services (IAM, Lambda, Athena, lakehouse).
- Stockage durable de gros volumes non structurés : backups, data lake, artefacts, médias.
- Besoin des classes de stockage pour optimiser le coût selon la fréquence d'accès (Standard, Intelligent-Tiering, Glacier).
- Fonctionnalités avancées attendues : versioning, lifecycle, réplication inter-régions, chiffrement, Object Lock.

## Quand NE PAS l'utiliser

- Trafic sortant élevé où l'**egress** pèse sur la facture → [[Dev/Services/Cloudflare R2|Cloudflare R2]] (sortie gratuite).
- Souveraineté, air-gap ou refus du cloud public → [[Dev/Services/MinIO|MinIO]] (auto-hébergé, même API).
- Petit besoin local ou tests → un MinIO en conteneur évite de dépendre d'un compte AWS.

## Déploiement & coût

- 100 % managé : aucun serveur à opérer, scaling automatique du stockage et du débit.
- Facturation à l'usage : stockage au Go-mois (≈ 0,023 $/Go-mois en Standard), **opérations** (PUT/GET) et surtout **egress** internet facturé par paliers au-delà de 100 Go/mois — le poste qui surprend.
- Free tier revu en juillet 2025 : les nouveaux comptes reçoivent des crédits AWS (≈ 200 $ sur 6 mois) au lieu de l'ancien « 5 Go gratuits à vie ».

## Pièges

- L'**egress** est le coût caché : une charge de lecture intensive vers l'extérieur peut coûter plus cher que le stockage lui-même.
- Lock-in cloud : la donnée est facile à écrire, plus coûteuse à exfiltrer (frais de sortie + réécriture des intégrations).
- Politiques IAM/bucket complexes : un bucket public par erreur reste une cause classique de fuite.
- Cohérence forte en lecture-après-écriture depuis 2020, mais le listing reste à raisonner sur gros volumes.

## Alternatives

- [[Dev/Services/MinIO|MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[Dev/Services/Ceph|Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[Dev/Services/SeaweedFS|SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Dev/Services/Garage|Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[Dev/Services/Cloudflare R2|Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Liens

- [[Dev/Services/MinIO|MinIO]] — alternative auto-hébergée implémentant la même API S3
- [[Dev/Services/Cloudflare R2|Cloudflare R2]] — alternative managée sans egress
- Doc : https://docs.aws.amazon.com/s3/
