---
galaxie: dev
type: service
nom: Ceph
alias: [ceph, rados, radosgw, rgw]
pitch: "Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde."
categorie: storage
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Dev/Services/MinIO|MinIO]]", "[[Dev/Services/SeaweedFS|SeaweedFS]]", "[[Dev/Services/Garage|Garage]]", "[[Dev/Services/AWS S3|AWS S3]]", "[[Dev/Services/Cloudflare R2|Cloudflare R2]]"]
remplace_par: []
status: actif
tags: [object-storage, s3-compatible]
url_docs: https://docs.ceph.com/
url_repo: https://github.com/ceph/ceph
---

# Ceph

## Pourquoi

Plateforme de stockage distribué **unifiée** : un même cluster expose du stockage **objet** (API S3 et Swift via le démon RADOS Gateway), **bloc** (RBD) et **fichier** (CephFS), au-dessus de la couche **RADOS** qui réplique et auto-répare les données sans point de défaillance unique. Conçu pour l'échelle massive (péta- à exaoctet) sur matériel standard. L'API S3 arrive via **radosgw** : c'est le moyen d'avoir du S3 auto-hébergé quand on veut *aussi* du bloc et du fichier sur la même infra. Maintenu par la Ceph Foundation (Linux Foundation), longtemps porté par Red Hat puis IBM.

## Quand l'utiliser

- Stockage **unifié** objet + bloc + fichier sur un seul cluster (souvent couplé à OpenStack, Proxmox ou Kubernetes via Rook).
- Très grande échelle, tolérance aux pannes disque/nœud sans RAID, auto-réparation et rééquilibrage.
- Infra souveraine / sur site où le stockage est un socle partagé entre plusieurs charges.
- Équipe ops capable d'opérer un système distribué complexe.

## Quand NE PAS l'utiliser

- Juste besoin d'un endpoint S3 simple → [[Dev/Services/MinIO|MinIO]] ou [[Dev/Services/Garage|Garage]] (bien plus légers).
- Pas d'équipe ops dédiée : Ceph est réputé lourd à déployer et à tuner.
- Charge mono-nœud ou petit volume : surdimensionné → [[Dev/Services/SeaweedFS|SeaweedFS]] ou le managé [[Dev/Services/AWS S3|AWS S3]].

## Déploiement & coût

- 100 % open-source (**LGPL-2.1 / LGPL-3.0**), self-host gratuit ; déploiement via cephadm, Rook (K8s) ou distributions (Proxmox, IBM/Red Hat Ceph Storage pour l'offre commerciale).
- Coût = matériel + exploitation ; pas de licence pour le cœur. Support commercial via IBM/Red Hat.
- Scaling horizontal en ajoutant des OSD/nœuds ; viser plusieurs nœuds et un réseau rapide dès le départ.

## Pièges

- Courbe d'apprentissage et exploitation **réputées difficiles** : MON/OSD/PG, rééquilibrage, tuning fin.
- Surdimensionné pour un simple besoin S3 ; minimum viable = plusieurs nœuds.
- Performance de radosgw à régler sur gros volumes d'objets (sharding de l'index de bucket notamment).
- Récupération après panne longue si le cluster est sous-dimensionné en capacité ou en réseau.

## Alternatives

- [[Dev/Services/MinIO|MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[Dev/Services/SeaweedFS|SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Dev/Services/Garage|Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[Dev/Services/AWS S3|AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Dev/Services/Cloudflare R2|Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Liens

- [[Dev/Services/MinIO|MinIO]] — endpoint S3 simple quand le bloc/fichier n'est pas requis
- [[Dev/Services/AWS S3|AWS S3]] — la référence S3 dont radosgw réimplémente l'API
- Doc : https://docs.ceph.com/
