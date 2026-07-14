---
galaxie: wiki
type: concept
nom: Versionnage de données
alias: [data versioning, versionnage de données, DVC, lakeFS, time travel, data lineage]
categorie: concept/data
domaines: [data-eng, mlops]
tags: [data-versioning]
---

# Versionnage de données

## Aperçu

- Appliquer aux **jeux de données** la discipline du versionnage de code : capturer des états nommés et immuables, pouvoir y revenir, comparer, et relier un résultat à la donnée exacte qui l'a produit.
- Brique de **reproductibilité** : un run d'[[ELT vs ETL & idempotence|ELT]] ou un entraînement de modèle devient rejouable à l'identique parce que sa donnée d'entrée est figée et adressable.

## Concepts clés

### Snapshot vs versionnage logique
- **Snapshot** : copie complète d'un état à un instant T. Simple, mais coûteux en stockage si répété.
- **Versionnage par contenu** : on adresse les données par hash et on ne stocke que les deltas — un « commit » référence des fichiers partagés entre versions (modèle Git appliqué aux données).

### Versionnage de fichiers — DVC
- **DVC** versionne des fichiers/dossiers de données *à côté* de Git : Git suit de petits fichiers `.dvc` (pointeurs + hash), le gros volume vit dans un *remote* (S3, GCS…).
- Couple données, code et pipeline : un `dvc repro` rejoue les étapes dont les entrées ont changé. Ancré **MLOps** — relier dataset ↔ modèle ↔ métrique pour la reproductibilité d'expériences.

### Versionnage de dépôt de données — lakeFS
- **lakeFS** apporte une sémantique **Git** (branch / commit / merge) au-dessus d'un **object store** entier (S3, GCS, Azure), sans copier la donnée.
- Permet d'isoler une transformation sur une *branche*, de la valider, puis de *merger* atomiquement en production ; ou de revenir à un commit antérieur du lac. Ancré **data-eng** (échelle lac de données).

### Time travel des formats de table
- Les formats lakehouse (Delta Lake, Apache Iceberg, Hudi) embarquent un versionnage par snapshots : requêter une table « telle qu'au commit N » ou rollback. Versionnage intégré au moteur, sans outil externe.

## En pratique

- Choisir l'échelle : **DVC** pour versionner des datasets liés à des expériences ML (Git-centric, fichiers) ; **lakeFS** pour du versionnage transactionnel à l'échelle d'un lac (branches sur object store) ; le **time travel** d'un format de table quand on est déjà sur lakehouse.
- Épingler la version d'entrée dans le pipeline : un backfill ou un rerun ([[ELT vs ETL & idempotence]]) reproductible suppose une donnée d'entrée adressable et figée.
- Lier au suivi d'expériences : versionner la donnée **et** journaliser quel commit a produit quel modèle/quelle métrique (lineage).
- Distinguer du versionnage de **structure** : faire évoluer le schéma relève des [[Migrations de schéma]] ; ici on version le **contenu**.
- Pièges : confondre versionnage de données et simple sauvegarde ; faire exploser le stockage avec des snapshots redondants ; ne pas figer la version d'entrée et croire un run « reproductible ».

## Approches voisines & alternatives

- [[ELT vs ETL & idempotence]] — un rerun/backfill reproductible s'appuie sur une entrée versionnée.
- [[Change Data Capture (CDC)]] — figer des états cohérents en aval d'un flux continu.
- [[Migrations de schéma]] — versionner la structure, pas le contenu.
- [[Contrats de données & qualité]] — un contrat respecté rend une version exploitable en confiance.
- [[Notebooks-as-code]] — versionner le **code** des notebooks ; pendant côté code de la reproductibilité.

## Pour aller plus loin

- Outils non encore fichés : **DVC** (Git-centric, MLOps), **lakeFS** (Git sur object store), Git LFS, Delta Lake / Iceberg (time travel) — candidats `Dev/Services/` (`data/versioning`).
- Notion connexe : *data lineage* — tracer la donnée de la source au livrable.
