---
role: hub
nom: Stockage objet
alias: [stockage objet, object storage, s3]
pitch: Servir des objets par une API S3 — la brique de base des lakehouses, des registres de modèles et des sauvegardes.
domaines: [data-eng, mlops, infra-ops]
tags: [object-storage, s3-compatible, self-hosted]
---

# Stockage objet

> Servir des objets par une API S3 — la brique de base des lakehouses, des registres de modèles et des sauvegardes.

## Ce qu'il faut comprendre

- Six briques, une seule interface : toutes parlent **S3**. Le code applicatif ne les distingue pas, ce qui déplace entièrement la décision vers l'exploitation — qui héberge, à quel coût, avec quelle équipe.
- Trois natures se cachent derrière l'interface commune, et elles n'ont pas les mêmes contraintes. Un **service managé** ([[AWS S3]], [[Cloudflare R2]]) ne demande aucune exploitation mais facture le stockage, les requêtes et parfois la sortie. Un **serveur objet** ([[MinIO]], [[Garage]], [[SeaweedFS]]) est un binaire qu'on installe et qu'on sauvegarde soi-même. Un **système de stockage distribué** ([[Ceph]]) est une infrastructure à part entière, avec l'équipe qui va avec.
- Le poste de coût qui surprend n'est pas le stockage mais l'**égress** : sortir la donnée du fournisseur. C'est l'argument central de [[Cloudflare R2]], qui ne le facture pas, et une raison fréquente de rapatrier en on-prem.
- La forme des objets décide plus qu'on ne croit. **Beaucoup de petits fichiers** est le cas qui met en difficulté la plupart des moteurs — d'où [[SeaweedFS]], conçu pour ça. **Peu de gros fichiers** convient à tout le monde.

## Choisir

- Déjà sur AWS → [[AWS S3]], et la question ne se pose pas.
- Beaucoup de lectures depuis l'extérieur → [[Cloudflare R2]], pour l'égress gratuit.
- Un serveur S3 self-hébergé à mettre en route vite, en dev comme en prod → [[MinIO]].
- Plusieurs petits sites, liens lents, matériel hétérogène → [[Garage]].
- Des milliards de petits objets → [[SeaweedFS]].
- Un besoin de stockage unifié bloc + fichier + objet à l'échelle du datacenter → [[Ceph]].

<!-- AUTO:START -->
### Briques
- [[AWS S3]] — Stockage objet de référence d'AWS : durabilité 11 neuf, scaling quasi illimité et écosystème intégré, mais egress facturé et dépendance au cloud AWS.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde.
- [[Cloudflare R2]] — Stockage objet managé S3-compatible sans frais d'egress : sortie de données gratuite et intégration native avec Cloudflare Workers.
- [[Garage]] — Stockage objet S3-compatible léger en Rust conçu pour l'auto-hébergement géo-distribué sur matériel hétérogène : résilient, sans coordination lourde (CRDT), sous AGPLv3.
- [[MinIO]] — Stockage objet S3-compatible auto-hébergé écrit en Go : haute performance, erasure coding distribué, sous licence AGPLv3.
- [[SeaweedFS]] — Stockage objet S3-compatible distribué en Go (inspiré de Haystack) optimisé pour des milliards de petits fichiers en accès O(1), sous licence permissive Apache 2.0.
<!-- AUTO:END -->
