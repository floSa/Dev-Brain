---
role: hub
nom: Stockage
alias: [stockage, storage]
pitch: Ranger des fichiers en masse et les servir par le réseau — le sol sur lequel reposent les lakehouses et les artefacts de modèle.
domaines: [data-eng, mlops, infra-ops]
tags: [object-storage, s3-compatible, self-hosted]
---

# Stockage

> Ranger des fichiers en masse et les servir par le réseau — le sol sur lequel reposent les lakehouses et les artefacts de modèle.

## Ce qu'il faut comprendre

- Le stockage **objet** est la seule famille peuplée ici, et ce n'est pas un hasard : c'est celle sur laquelle repose tout le reste de la pile data moderne. Un lakehouse, un registre de modèles, un cache de features sont des conventions posées sur des objets.
- Un objet n'est pas un fichier. Pas d'arborescence réelle (le `/` est dans la clé), pas d'écriture partielle, pas de renommage atomique. C'est ce qui rend le stockage objet extensible à l'infini et ce qui oblige les formats de table (Delta, Iceberg) à réinventer la transaction par-dessus.
- **L'API S3 est le vrai standard**, et c'est la propriété qui compte au moment de choisir : toute brique compatible S3 est interchangeable côté code. La décision porte donc sur l'exploitation et le coût, pas sur l'intégration.
- Détail par brique : [[Stockage objet]].

## Choisir

- Sur AWS → [[AWS S3]]. Beaucoup d'égress → [[Cloudflare R2]], qui ne le facture pas.
- Un serveur objet self-hébergé, simple à installer et compatible S3 → [[MinIO]].
- Très petite infrastructure, plusieurs sites, faible bande passante → [[Garage]].
- Des milliards de petits fichiers → [[SeaweedFS]].
- Un cluster de stockage unifié bloc + fichier + objet, avec l'équipe pour l'exploiter → [[Ceph]].

<!-- AUTO:START -->
### Sous-domaines
- [[Stockage objet]]
<!-- AUTO:END -->
