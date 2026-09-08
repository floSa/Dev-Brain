---
role: brique
nom: Garage
alias: [garage]
pitch: "Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3."
categorie: storage/objet
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Rust
scaling: distributed
alternatives: ["[[MinIO]]", "[[SeaweedFS]]", "[[Ceph]]", "[[AWS S3]]", "[[Cloudflare R2]]"]
complements: []
tags: [object-storage, s3-compatible]
url_docs: https://garagehq.deuxfleurs.fr/documentation/
url_repo: https://git.deuxfleurs.fr/Deuxfleurs/garage
---

# Garage

<!-- AUTO:BANDEAU:START -->
> Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Rust | open-source | self-hébergé · distribué | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Stockage objet **S3-compatible** écrit en **Rust** par le collectif **Deuxfleurs**, conçu pour
l'auto-hébergement **géo-distribué** à petite et moyenne échelle. Sa particularité est
l'hypothèse de départ : des nœuds répartis sur plusieurs sites physiques, sur du matériel
**hétérogène** aux capacités disque inégales, reliés par un réseau ordinaire — et le cluster
doit rester disponible quand des serveurs tombent. Pour tenir cela, il renonce au consensus
lourd type Raft sur les données et s'appuie sur des **CRDT**, dans la lignée de Dynamo : la
cohérence est *à terme*, jamais transactionnelle. Le résultat est un binaire léger, simple à
exploiter, pensé pour tourner hors datacenter. En production chez Deuxfleurs depuis 2020.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Auto-héberger du S3 réparti sur **plusieurs sites**, avec réplication géographique | Très haute performance ou très gros volumes mono-site : la cible annoncée est la petite et moyenne échelle → [[MinIO]], [[SeaweedFS]] |
| Matériel modeste et hétérogène, faible empreinte RAM/CPU, tolérance aux pannes de nœud | Besoin de bloc ou de fichier en plus de l'objet → [[Ceph]] |
| Backend S3 de services auto-hébergés : sauvegardes, médias, sites statiques | Aucune envie d'opérer l'infra → managé [[AWS S3]] ou [[Cloudflare R2]] |
| | L'**AGPLv3** est un copyleft réseau : à valider avant toute intégration dans un produit fermé |
| | Cohérence **à terme** par CRDT : aucune garantie transactionnelle |
| | Compatibilité S3 sur un **sous-ensemble** de l'API — vérifier les fonctions réellement utilisées |

## Mise en œuvre

- Installation — un binaire Rust unique, ou une image de conteneur
- Point d'entrée — l'API S3 ; configuration par fichier TOML et commande `garage`
- Prérequis — plusieurs nœuds pour que la réplication ait un sens ; peu de RAM et de CPU par nœud
- Exécution — self-hébergé, distribué, explicitement pensé pour tourner **hors datacenter** ; scaling horizontal par ajout de nœuds, facteur de réplication configurable (souvent x3) entre zones
- Coût — gratuit, AGPLv3 ; le coût est le matériel, et la contrainte est la licence

## Écosystème

### Alternatives

- [[MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Ressources

- Documentation — https://garagehq.deuxfleurs.fr/documentation/
- Dépôt — https://git.deuxfleurs.fr/Deuxfleurs/garage

## Voir aussi

- [[Stockage]] — le hub du domaine
