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
alternatives: ["[[RustFS]]", "[[MinIO]]", "[[SeaweedFS]]", "[[Ceph]]", "[[AWS S3]]", "[[Cloudflare R2]]"]
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
lourd type Raft sur les données et s'appuie sur des **CRDT**, dans la lignée de Dynamo. La
garantie visée est la **lecture après écriture**, obtenue par des quorums (2 réplicas sur 3) et
non par un consensus ; aucune transaction entre plusieurs clés. Le résultat est un binaire léger,
simple à exploiter, pensé pour tourner hors datacenter. En production chez Deuxfleurs depuis 2020.

*Constat du 2026-09-30 :* étiquette **v2.4.1** (commit du 2026-09-07), précédée de v2.4.0 le
2026-09-06 et de v2.3.0 le 2026-04-16 ; la branche 1.x reste maintenue. Le dépôt principal est
sur `git.deuxfleurs.fr` ; le miroir GitHub `deuxfleurs-org/garage` compte environ **4,6 k
étoiles**. Licence **AGPL-3.0**, confirmée sur le miroir. Côté S3, la page officielle de
compatibilité liste les **manques** : pas de versioning (`GetBucketVersioning` répond « non
activé »), **pas d'Object Lock**, donc pas de WORM, pas de politiques de bucket ni d'ACL (Garage
a son propre modèle de droits par clé et par bucket), pas de tagging, de notifications ni de
réplication S3, et un cycle de vie réduit à l'expiration et à l'abandon des multiparts. Il n'y a
**pas d'erasure coding**, par choix de conception : la réplication (facteur 3 par défaut, une
copie par zone) est le seul mécanisme. La cible annoncée est l'auto-hébergement géo-distribué à
petite échelle ; la section « à grande échelle » de sa page de benchmarks est restée vide.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Auto-héberger du S3 réparti sur **plusieurs sites**, avec réplication géographique | Très haute performance ou très gros volumes mono-site : la cible annoncée est la petite et moyenne échelle → [[MinIO]], [[SeaweedFS]] |
| Matériel modeste et hétérogène, faible empreinte RAM/CPU, tolérance aux pannes de nœud | Besoin de bloc ou de fichier en plus de l'objet → [[Ceph]] |
| Backend S3 de services auto-hébergés : sauvegardes, médias, sites statiques | Aucune envie d'opérer l'infra → managé [[AWS S3]] ou [[Cloudflare R2]] |
| | L'**AGPLv3** est un copyleft réseau : à valider avant toute intégration dans un produit fermé |
| | Aucune transaction entre clés ; lecture après écriture par quorum, sans consensus — à éprouver sur ses charges de métadonnées |
| | Compatibilité S3 sur un **sous-ensemble** de l'API — vérifier les fonctions réellement utilisées |

## Mise en œuvre

- Installation — un binaire Rust unique, ou une image de conteneur
- Point d'entrée — l'API S3 ; configuration par fichier TOML et commande `garage`
- Prérequis — plusieurs nœuds pour que la réplication ait un sens ; peu de RAM et de CPU par nœud
- Exécution — self-hébergé, distribué, explicitement pensé pour tourner **hors datacenter** ; scaling horizontal par ajout de nœuds, facteur de réplication configurable (souvent x3) entre zones
- Coût — gratuit, AGPLv3 ; le coût est le matériel, et la contrainte est la licence

## Écosystème

### Alternatives

- [[RustFS]] — Stockage objet S3-compatible en Rust sous Apache 2.0, qui vise la succession de MinIO : versioning, Object Lock, réplication et mode distribué au catalogue, mais en version stable depuis le 2026-09-16 seulement et avec des failles IAM encore publiées chaque mois.
- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.

## Ressources

- Documentation — https://garagehq.deuxfleurs.fr/documentation/
- Dépôt — https://git.deuxfleurs.fr/Deuxfleurs/garage

## Voir aussi

- [[Stockage]] — le hub du domaine
- [[Stockage objet et API S3]] — la notion : ce que l'API S3 fixe, ce qu'elle laisse à chaque implémentation, et comment choisir un backend on-prem
- [[Comparatif - Stockage objet]] — ce qui départage les briques du dossier
