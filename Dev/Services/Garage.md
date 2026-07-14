---
galaxie: dev
type: service
nom: Garage
alias: [garage]
pitch: "Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3."
categorie: storage
licence_type: open-source
hosted: self
maturite: production
langage: Rust
scaling: distributed
alternatives: ["[[Dev/Services/MinIO|MinIO]]", "[[Dev/Services/SeaweedFS|SeaweedFS]]", "[[Dev/Services/Ceph|Ceph]]", "[[Dev/Services/AWS S3|AWS S3]]", "[[Dev/Services/Cloudflare R2|Cloudflare R2]]"]
remplace_par: []
status: actif
tags: [object-storage, s3-compatible]
url_docs: https://garagehq.deuxfleurs.fr/documentation/
url_repo: https://git.deuxfleurs.fr/Deuxfleurs/garage
---

# Garage

## Pourquoi

Stockage objet **S3-compatible** écrit en **Rust**, conçu par le collectif **Deuxfleurs** pour l'auto-hébergement **géo-distribué** à petite et moyenne échelle. Sa particularité : viser des nœuds répartis sur plusieurs sites physiques, sur du matériel **hétérogène** (capacités disque inégales), tout en restant disponible quand des serveurs tombent. Pas de consensus lourd type Raft pour les données : il s'appuie sur des **CRDT** (inspiration Dynamo) pour une cohérence à terme. Léger, simple à opérer, résilient — pensé pour tourner *hors datacenter*. En production chez Deuxfleurs depuis 2020.

## Quand l'utiliser

- Auto-héberger du S3 réparti sur **plusieurs sites** avec réplication géographique.
- Matériel modeste et hétérogène, faible empreinte RAM/CPU, tolérance aux pannes de nœud.
- Besoin d'un binaire léger et simple à exploiter plutôt qu'une plateforme lourde → vs [[Dev/Services/Ceph|Ceph]].
- Backend S3 pour services self-hosted (sauvegardes, médias, sites statiques).

## Quand NE PAS l'utiliser

- Très haute performance ou très gros volumes mono-site → [[Dev/Services/MinIO|MinIO]] ou [[Dev/Services/SeaweedFS|SeaweedFS]].
- Besoin de bloc/fichier en plus de l'objet → [[Dev/Services/Ceph|Ceph]].
- Aucune envie d'opérer l'infra → managé [[Dev/Services/AWS S3|AWS S3]] ou [[Dev/Services/Cloudflare R2|Cloudflare R2]].
- Contrainte de licence : l'**AGPLv3** (copyleft réseau) peut être incompatible avec un produit fermé.

## Déploiement & coût

- Open-source **AGPLv3**, self-host gratuit ; binaire unique en Rust, image conteneur disponible.
- Conçu pour tourner **hors datacenter** : faible empreinte, peu de RAM/CPU exigés.
- Scaling horizontal par ajout de nœuds ; facteur de réplication configurable (souvent x3) entre zones.

## Pièges

- **AGPLv3** : copyleft réseau, à valider avant toute intégration dans un produit fermé.
- Cohérence **à terme** (CRDT) : pas de garanties transactionnelles fortes type base SQL.
- Cible explicite petite/moyenne échelle : mauvais choix pour des charges massives.
- Compatibilité S3 sur un **sous-ensemble** de l'API : vérifier les fonctions réellement utilisées.

## Alternatives

- [[Dev/Services/MinIO|MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[Dev/Services/SeaweedFS|SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Dev/Services/Ceph|Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[Dev/Services/AWS S3|AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Dev/Services/Cloudflare R2|Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Liens

- [[Dev/Services/MinIO|MinIO]] — autre S3 auto-hébergé, mono-site plus performant
- [[Dev/Services/Ceph|Ceph]] — alternative lourde quand il faut bloc + fichier
- Doc : https://garagehq.deuxfleurs.fr/documentation/
