---
role: brique
nom: Ceph
alias: [ceph, rados, radosgw, rgw]
pitch: "Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[MinIO]]", "[[SeaweedFS]]", "[[Garage]]", "[[AWS S3]]", "[[Cloudflare R2]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://docs.ceph.com/
url_repo: https://github.com/ceph/ceph
---

# Ceph

<!-- AUTO:BANDEAU:START -->
> Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C++ | open-source | self-hébergé · distribué | production | à jour · 2026-08-18 |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de stockage distribué **unifiée** : un même cluster expose de l'**objet** (API S3 et
Swift par le démon RADOS Gateway), du **bloc** (RBD) et du **fichier** (CephFS), au-dessus de la
couche **RADOS** qui réplique et auto-répare les données sans point de défaillance unique. Elle
est conçue pour l'échelle massive — du péta à l'exaoctet — sur du matériel standard, et se
passe de RAID : la tolérance aux pannes de disque et de nœud est portée par le placement des
objets. L'API S3 n'est donc pas le produit mais une façade parmi trois, ce qui est tout
l'argument : c'est le moyen d'avoir du S3 auto-hébergé quand on veut *aussi* du bloc et du
fichier sur la même infra. Portée par la Ceph Foundation, longtemps chez Red Hat puis IBM.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Stockage unifié objet + bloc + fichier sur un seul cluster (OpenStack, Proxmox, Kubernetes par Rook) | Il ne faut qu'un endpoint S3 simple : le minimum viable est déjà de plusieurs nœuds → [[MinIO]], [[Garage]] |
| Très grande échelle, tolérance aux pannes sans RAID, auto-réparation et rééquilibrage | Pas d'équipe ops dédiée : MON/OSD/PG, rééquilibrage et tuning fin ont une réputation de difficulté méritée |
| Infra souveraine ou sur site où le stockage est un socle partagé entre plusieurs charges | Charge mono-nœud ou petit volume : surdimensionné → [[SeaweedFS]], ou le managé [[AWS S3]] |
| | La performance de radosgw se règle sur gros volumes d'objets — le sharding de l'index de bucket en particulier |
| | Récupération après panne longue si le cluster est sous-dimensionné en capacité ou en réseau |

## Mise en œuvre

- Installation — cephadm, Rook pour Kubernetes, ou une distribution qui l'embarque (Proxmox, IBM/Red Hat Ceph Storage)
- Point d'entrée — trois façades au choix : API S3/Swift par radosgw, bloc par RBD, fichier par CephFS
- Prérequis — plusieurs nœuds et un réseau rapide dès le départ ; une équipe capable d'opérer un système distribué
- Exécution — self-hébergé, distribué : scaling horizontal par ajout d'OSD et de nœuds
- Coût — gratuit, LGPL-2.1 / LGPL-3.0 pour le cœur ; le coût réel est le matériel et l'exploitation. Support commercial par IBM/Red Hat

## Écosystème

### Alternatives

- [[MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Ressources

- Documentation — https://docs.ceph.com/
- Dépôt — https://github.com/ceph/ceph

## Voir aussi

- [[Stockage]] — le hub du domaine
