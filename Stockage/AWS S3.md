---
role: brique
nom: AWS S3
alias: [s3, amazon s3, aws-s3]
pitch: "Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS."
categorie: storage/objet
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: serverless
alternatives: ["[[MinIO]]", "[[Ceph]]", "[[SeaweedFS]]", "[[Garage]]", "[[Cloudflare R2]]"]
complements: []
tags: [object-storage]
url_docs: https://docs.aws.amazon.com/s3/
url_repo: 
---

# AWS S3

<!-- AUTO:BANDEAU:START -->
> Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Amazon Simple Storage Service : le stockage objet qui a défini la catégorie, et dont l'API est
devenue le **standard de fait** que toutes les autres briques du dossier réimplémentent. Les
données vivent dans des *buckets*, adressées par clé, sans hiérarchie de fichiers réelle. La
donnée est répliquée sur au moins trois zones de disponibilité, ce qui donne les **onze neuf**
de durabilité annoncés, et la capacité est fournie sans provisionnement. Le service est au
centre de l'écosystème AWS — Lambda, Athena, Glue, CloudFront — au point d'être souvent le
point de gravité d'une architecture data sur ce cloud. Sa cohérence est forte en lecture après
écriture depuis 2020 ; le *listing*, lui, reste à raisonner sur gros volumes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Déjà sur AWS : intégration native avec IAM, Lambda, Athena et le reste du lakehouse | Trafic sortant élevé : l'**egress** est facturé par paliers au-delà de 100 Go/mois, et une charge de lecture intensive coûte plus cher que le stockage → [[Cloudflare R2]] |
| Stockage durable de gros volumes non structurés : sauvegardes, data lake, artefacts, médias | Souveraineté, air-gap ou refus du cloud public → [[MinIO]], même API en auto-hébergé |
| Optimiser le coût par classe de stockage selon la fréquence d'accès (Standard, Intelligent-Tiering, Glacier) | Petit besoin local ou tests : dépendre d'un compte AWS est disproportionné → [[MinIO]] en conteneur |
| Attendre les fonctions avancées : versioning, lifecycle, réplication inter-régions, chiffrement, Object Lock | Lock-in : la donnée est facile à écrire, coûteuse à exfiltrer — frais de sortie plus réécriture des intégrations |
| | Politiques IAM et de bucket complexes : un bucket public par erreur reste une cause classique de fuite |

## Mise en œuvre

- Installation — aucune : un compte AWS et un bucket suffisent
- Point d'entrée — l'API S3, via SDK (`boto3`), la CLI `aws s3` ou tout outil S3-compatible
- Prérequis — un compte AWS et des politiques IAM correctement écrites
- Exécution — 100 % managé, serverless : aucun serveur à opérer, scaling automatique du stockage et du débit
- Coût — à l'usage : stockage au Go-mois (≈ 0,023 $/Go-mois en Standard), opérations PUT/GET, et **egress** internet facturé — le poste qui surprend. Le free tier a été revu en juillet 2025 : les nouveaux comptes reçoivent des crédits (≈ 200 $ sur 6 mois) au lieu des 5 Go gratuits à vie

## Écosystème

### Alternatives

- [[MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Ressources

- Documentation — https://docs.aws.amazon.com/s3/

## Voir aussi

- [[Stockage]] — le hub du domaine
