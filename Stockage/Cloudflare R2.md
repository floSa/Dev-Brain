---
role: brique
nom: Cloudflare R2
alias: [r2, cloudflare-r2]
pitch: "Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers."
categorie: storage/objet
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: 
scaling: serverless
alternatives: ["[[AWS S3]]", "[[MinIO]]", "[[Ceph]]", "[[SeaweedFS]]", "[[Garage]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://developers.cloudflare.com/r2/
url_repo: 
---

# Cloudflare R2

<!-- AUTO:BANDEAU:START -->
> Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Stockage objet managé de Cloudflare, **S3-compatible**, dont l'argument central tient en un
point de facturation : **l'egress est à zéro**. Lire ses données ne coûte rien, quel que soit
le volume sorti — par l'API S3, par un Worker ou par le domaine `r2.dev`. Le reste suit le
modèle habituel : buckets, clés, classes Standard et Infrequent Access. La compatibilité S3
rend la migration d'outillage quasi transparente, et l'**intégration native avec Cloudflare
Workers** permet de servir la donnée au bord du réseau sans infra supplémentaire. Le
positionnement est frontal : c'est le modèle économique d'AWS S3 qui est visé, pas ses
fonctionnalités.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Fort trafic sortant — diffusion de médias, d'assets, de jeux de données publics : l'egress gratuit change l'économie | Architecture profondément intégrée à AWS (Athena, Glue, Lambda) → [[AWS S3]] reste plus naturel |
| Déjà dans l'écosystème Cloudflare : Workers, CDN, Pages s'y branchent sans couture | Souveraineté ou auto-hébergement exigé : il n'existe pas de self-host → [[MinIO]] |
| Migrer depuis S3 en repointant l'endpoint des SDK et outils existants | Palette complète des classes de stockage et des services analytiques attendue → [[AWS S3]] |
| Backend objet d'applications edge ou serverless dominées par la lecture | La compatibilité S3 est large mais **pas exhaustive** : vérifier ses dépendances avant migration |
| | L'egress gratuit ne supprime pas le coût des **opérations** — la classe A, en écriture, se modélise sur charge write-heavy |
| | Empreinte régionale et garanties différentes d'AWS : latence et conformité à valider cas par cas |

## Mise en œuvre

- Installation — aucune : un compte Cloudflare et un bucket
- Point d'entrée — l'API S3 avec un endpoint R2, un binding Worker, ou le domaine public `r2.dev`
- Prérequis — un compte Cloudflare ; aucune infra
- Exécution — 100 % managé, serverless : scaling automatique, rien à opérer
- Coût — stockage au Go-mois et opérations en deux classes A/B, **egress à 0 $** ; palier gratuit mensuel, classes Standard et Infrequent Access

## Écosystème

### Alternatives

- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.

## Ressources

- Documentation — https://developers.cloudflare.com/r2/

## Voir aussi

- [[Stockage]] — le hub du domaine
