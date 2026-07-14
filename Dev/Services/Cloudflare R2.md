---
galaxie: dev
type: service
nom: Cloudflare R2
alias: [r2, cloudflare-r2]
pitch: "Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers."
categorie: storage
licence_type: proprietary
hosted: managed
maturite: production
langage: 
scaling: serverless
alternatives: ["[[Dev/Services/AWS S3|AWS S3]]", "[[Dev/Services/MinIO|MinIO]]", "[[Dev/Services/Ceph|Ceph]]", "[[Dev/Services/SeaweedFS|SeaweedFS]]", "[[Dev/Services/Garage|Garage]]"]
remplace_par: []
status: actif
tags: [object-storage, s3-compatible]
url_docs: https://developers.cloudflare.com/r2/
url_repo: 
---

# Cloudflare R2

## Pourquoi

Stockage objet managé de Cloudflare, **S3-compatible**, dont l'argument central est l'**absence de frais d'egress** : lire ses données ne coûte rien, quel que soit le volume sorti (API S3, Workers, domaine `r2.dev`). API compatible S3 donc migration outillage quasi transparente, et **intégration native avec Cloudflare Workers** pour servir la donnée au bord du réseau sans infra supplémentaire. Positionné frontalement contre le modèle de facturation d'AWS S3.

## Quand l'utiliser

- Charges à fort trafic sortant : diffusion de médias, assets, datasets publics — l'egress gratuit change l'économie face à S3.
- Déjà dans l'écosystème Cloudflare : Workers, CDN, Pages → R2 s'y branche sans couture.
- Migration depuis S3 avec un minimum de friction : réutiliser les SDK/outils S3 existants en repointant l'endpoint.
- Backend objet d'apps edge / serverless servant beaucoup de lectures.

## Quand NE PAS l'utiliser

- Architecture profondément intégrée à AWS (Athena, Glue, Lambda) → [[Dev/Services/AWS S3|AWS S3]] reste plus naturel.
- Souveraineté / auto-hébergement exigé → [[Dev/Services/MinIO|MinIO]] (sur site, même API).
- Besoin de la palette complète de classes de stockage et services analytiques d'AWS → [[Dev/Services/AWS S3|AWS S3]].

## Déploiement & coût

- 100 % managé, serverless : pas d'infra à opérer, scaling automatique.
- Facturation au **stockage** (Go-mois) + **opérations** (deux classes A/B), avec **egress à 0 $** — c'est la différence structurelle avec S3.
- Palier gratuit mensuel ; classes Standard et Infrequent Access selon la fréquence d'accès.

## Pièges

- Service propriétaire Cloudflare : lock-in écosystème, pas de self-host possible.
- Compatibilité S3 large mais **pas exhaustive** : certaines API/fonctions S3 manquent — vérifier ses dépendances avant migration.
- L'egress gratuit ne supprime pas les coûts d'**opérations** (Class A en écriture surtout) : à modéliser sur charge write-heavy.
- Empreinte régionale et garanties différentes d'AWS : valider latence et conformité selon le cas.

## Alternatives

- [[Dev/Services/AWS S3|AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Dev/Services/MinIO|MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[Dev/Services/Ceph|Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[Dev/Services/SeaweedFS|SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Dev/Services/Garage|Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.

## Liens

- [[Dev/Services/AWS S3|AWS S3]] — la référence S3, dont R2 conteste le modèle d'egress
- [[Dev/Services/MinIO|MinIO]] — alternative S3-compatible auto-hébergée
- Doc : https://developers.cloudflare.com/r2/
