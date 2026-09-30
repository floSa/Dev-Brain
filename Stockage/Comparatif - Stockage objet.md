---
role: comparatif
nom: Comparatif - Stockage objet
categorie: storage/objet
tags: [object-storage, s3-compatible]
---

# Comparatif - Stockage objet

> On tranche sur : l'état du projet et sa licence d'abord — c'est ce qui a bougé en 2025 et 2026 —, puis l'étendue réelle de l'API S3 (versioning, Object Lock, écritures conditionnelles), le mécanisme de durabilité (erasure coding ou réplication), l'échelle qu'il faut pour commencer, et le public visé (petit cluster, analytique, datacenter).

![[Comparatif - Stockage objet.base]]

## Ce qui départage

**Les références managées** ne sont pas départagées sur l'on-prem : elles fixent ce que l'API doit savoir faire et ce qu'elle coûte.

- [[AWS S3]] — la **référence de l'API** que tous les autres réimplémentent : versioning, Object Lock, cycle de vie, notifications, lecture après écriture forte depuis 2020. Service managé propriétaire, dont l'**egress** est le poste qui surprend. Les nouveautés récentes (S3 Files, S3 Tables, Express One Zone) sont propres à AWS.
- [[Cloudflare R2]] — la référence managée **sans frais d'egress**. Sa page de compatibilité déclare elle-même l'absence de versioning et d'Object Lock S3, remplacé par des « bucket locks » propriétaires.

**Les serveurs auto-hébergés** se départagent ainsi.

- [[MinIO]] — le serveur S3 auto-hébergé qui a servi de référence, aujourd'hui **abandonné** : dépôt archivé le 2026-04-25, plus de release depuis octobre 2025, **AGPLv3**, et une suite commerciale propriétaire (AIStor, dont l'édition gratuite est mononœud). À ne plus choisir pour une nouvelle installation ; il reste à connaître parce qu'une base installée existe, et parce que son arrêt est la raison de ce comparatif.
- [[RustFS]] — le **successeur visé**, en **Apache 2.0** : versioning, Object Lock, réplication et console dans l'édition libre. Mais la version stable date du 2026-09-16 et 35 avis de sécurité ont été publiés depuis décembre 2025, dont des critiques sur l'IAM et l'Object Lock : **pas encore éprouvé**, à réserver à un pilote tant que des retours indépendants manquent.
- [[SeaweedFS]] — **Apache 2.0**, une couverture S3 large (versioning, Object Lock, écritures conditionnelles, SSE) et un pari d'architecture sur les **petits fichiers** et les milliards d'objets. Erasure coding seulement sur les volumes passés en lecture seule ; ni notifications de bucket, ni réplication S3 native. Plusieurs composants à exploiter (master, volume, filer, S3) et un metadata store à choisir.
- [[Garage]] — le choix du **petit cluster géo-distribué** sur matériel modeste (1 Go de RAM suffisent) : réplication en facteur 3 par zone, lecture après écriture par quorum, sans consensus. **AGPL-3.0**, et un S3 volontairement restreint — **ni versioning ni Object Lock**, donc pas de WORM — sans erasure coding.
- [[Ceph]] — le **socle unifié** objet, bloc et fichier, en **LGPL**, avec une couverture S3 documentée large (versioning, cycle de vie, politiques, notifications, Object Lock). Le prix est l'exploitation : trois moniteurs, 4 Gio de RAM par OSD, un réseau rapide, une équipe dédiée. Justifié quand le cluster sert aussi du bloc ou du fichier.
- [[Apache Ozone]] — l'**analytique sur site à très grande échelle** : espace de noms à milliards d'objets, cohérence forte par Raft, accès par S3 et par le système de fichiers Hadoop. Le dimensionnement officiel (3 OM, 3 SCM, au moins 10 Datanodes pour RS-6-3) et un S3 sans versioning, Object Lock ni requêtes conditionnelles le réservent à ce public.
- [[OpenStack Swift]] — la brique **historique** : pertinent dans un cloud privé OpenStack existant ou pour son API native. Cohérence à terme, middleware S3 sans cycle de vie ni étiquettes, et un principal exploitant public (OVHcloud) qui a arrêté de le faire évoluer au profit du S3 natif.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Stockage]] — le hub du dossier.
- [[Stockage objet et API S3]] — la notion : ce que l'API S3 fixe et ce qu'elle laisse à chaque implémentation.
