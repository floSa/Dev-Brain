---
role: brique
nom: MinIO
alias: [minio]
pitch: "Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Ceph]]", "[[SeaweedFS]]", "[[Garage]]", "[[AWS S3]]", "[[Cloudflare R2]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://min.io/docs/minio/linux/index.html
url_repo: https://github.com/minio/minio
---

# MinIO

<!-- AUTO:BANDEAU:START -->
> Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | dépôt archivé · 2026-04-25 |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur de stockage objet **S3-compatible** écrit en **Go**, pensé pour être posé sur ses
propres machines : un seul binaire expose l'API S3, et l'on obtient « son S3 » en local ou dans
son cloud. En mode distribué, la tolérance aux pannes de disque et de nœud passe par de
l'**erasure coding**, sans RAID. C'est le moyen courant d'avoir l'API S3 sans AWS, et son usage
le plus fréquent n'est même pas la production : un conteneur MinIO sert de S3 de développement
et de CI. Deux décisions de l'éditeur, prises en 2025, pèsent aujourd'hui plus lourd que la
technique — le retrait de la console d'administration de l'édition libre, et l'arrêt des
binaires précompilés (cf. *Écarter si*).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Émuler S3 en local ou en CI : un conteneur remplace AWS pour développer et tester | Depuis 2025, la Community Edition est distribuée **en sources uniquement** : plus de binaire précompilé officiel, il faut builder (`go install`) ou passer par une image tierce |
| Stockage objet souverain ou air-gappé : données sur site, hors cloud public | La **console web d'administration** est retirée de la Community Edition — policies, réplication et supervision passent par la CLI `mc` ou par l'offre payante |
| Backend S3 d'autres briques (lakehouse, registres d'artefacts, sauvegardes) sans dépendre d'AWS | L'**AGPLv3** est un copyleft réseau : exposer un service bâti sur MinIO peut imposer de publier le code lié — à valider juridiquement |
| Volume distribué tolérant aux pannes par erasure coding sur plusieurs nœuds | Aucune envie d'opérer disques, nœuds et mises à jour → managé [[AWS S3]] ou [[Cloudflare R2]] |
| | Compatibilité S3 large mais **partielle** : certains cas limites d'AWS ne sont pas couverts, tester ses intégrations |
| | Erasure coding et quorum à dimensionner : un cluster sous-dimensionné perd en disponibilité |

## Mise en œuvre

- Installation — build depuis les sources (`go install`) ou image de conteneur ; plus de binaire officiel précompilé côté libre depuis 2025
- Point d'entrée — l'API S3, et la CLI `mc` pour l'administration
- Prérequis — plusieurs nœuds et un nombre de disques cohérent avec le schéma d'erasure coding visé
- Exécution — self-hébergé, du mono-nœud au cluster distribué
- Coût — gratuit sous AGPLv3 pour le cœur. L'offre commerciale **AIStor** (ex-Enterprise) porte la console d'admin, le support et les fonctions avancées, à licence annuelle élevée

## Écosystème

### Alternatives

- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Ressources

- Documentation — https://min.io/docs/minio/linux/index.html
- Dépôt — https://github.com/minio/minio

## Voir aussi

- [[Stockage]] — le hub du domaine
