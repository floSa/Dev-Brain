---
galaxie: dev
type: service
nom: MinIO
alias: [minio]
pitch: "Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3."
categorie: storage
licence_type: open-source
hosted: self
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Dev/Services/Ceph|Ceph]]", "[[Dev/Services/SeaweedFS|SeaweedFS]]", "[[Dev/Services/Garage|Garage]]", "[[Dev/Services/AWS S3|AWS S3]]", "[[Dev/Services/Cloudflare R2|Cloudflare R2]]"]
remplace_par: []
status: actif
tags: [object-storage, s3-compatible]
url_docs: https://min.io/docs/minio/linux/index.html
url_repo: https://github.com/minio/minio
---

# MinIO

## Pourquoi

Serveur de stockage objet **S3-compatible**, écrit en **Go**, pensé pour être auto-hébergé. Un seul binaire expose l'API S3 : on déploie son propre « S3 » sur ses machines, en local ou dans son cloud. Mode distribué avec **erasure coding** (tolérance aux pannes de disques/nœuds sans RAID) et haute performance. C'est le moyen courant d'avoir l'API S3 sans AWS — en dev (un conteneur émule S3) comme en prod souveraine.

## Quand l'utiliser

- Émuler S3 en local / CI : un conteneur MinIO remplace AWS pour développer et tester sans compte cloud.
- Stockage objet souverain ou air-gappé : données sur site, hors cloud public.
- Backend S3 d'autres briques (lakehouse, registres d'artefacts, sauvegardes) sans dépendre d'AWS.
- Volume distribué tolérant aux pannes via erasure coding sur plusieurs nœuds.

## Quand NE PAS l'utiliser

- Aucune envie d'opérer l'infra (disques, nœuds, mises à jour) → [[Dev/Services/AWS S3|AWS S3]] ou [[Dev/Services/Cloudflare R2|Cloudflare R2]] (managés).
- Besoin de la console web d'administration : depuis 2025, elle est retirée de la Community Edition (réservée à l'offre commerciale AIStor).
- Pas d'équipe pour gérer la conformité AGPLv3 et le build depuis les sources (voir Pièges).

## Déploiement & coût

- Self-host gratuit sous **AGPLv3** : binaire unique ou conteneur, du mono-nœud au cluster distribué (erasure coding).
- Depuis 2025, la Community Edition est distribuée **en sources uniquement** — plus de binaires précompilés officiels pour la version libre ; il faut builder (`go install`) ou utiliser une image tierce.
- Offre commerciale **AIStor** (ex-Enterprise) pour la console d'admin, le support et les fonctions avancées — licence annuelle élevée.

## Pièges

- **AGPLv3** : licence copyleft réseau. Exposer un service bâti sur MinIO peut imposer de publier le code lié — à valider juridiquement avant tout produit fermé.
- 2025 : retrait de la Web UI d'administration et arrêt des binaires précompilés côté Community — gérer policies, réplication et monitoring se fait désormais en CLI (`mc`) ou via l'offre payante.
- Compatibilité S3 large mais **partielle** : certaines API/edge cases AWS ne sont pas couverts — tester ses intégrations.
- Erasure coding et quorum à dimensionner correctement : un cluster sous-dimensionné perd en disponibilité.

## Alternatives

- [[Dev/Services/Ceph|Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[Dev/Services/SeaweedFS|SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Dev/Services/Garage|Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[Dev/Services/AWS S3|AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Dev/Services/Cloudflare R2|Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Liens

- [[Dev/Services/AWS S3|AWS S3]] — la référence S3 que MinIO réimplémente en auto-hébergé
- [[Dev/Services/Cloudflare R2|Cloudflare R2]] — autre alternative S3-compatible, managée
- Doc : https://min.io/docs/minio/linux/index.html
