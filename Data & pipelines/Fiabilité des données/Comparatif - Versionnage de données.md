---
role: comparatif
nom: Comparatif - Versionnage de données
categorie: data/fiabilite
tags: [data-versioning]
---

# Comparatif - Versionnage de données

> On tranche sur : le niveau qu'on versionne (fichiers, dépôt d'objets ou table), la manière dont un état daté se retrouve pour rejouer un entraînement, le lien avec Git, ce qu'il faut héberger — stockage, base, serveur —, le coût d'exploitation, et la licence, dont une a changé en septembre 2026.

![[Comparatif - Versionnage de données.base]]

## Ce qui départage

- [[DVC]] — le versionnage **par Git** : des pointeurs `.dvc` dans le dépôt, le contenu dans un remote quelconque, et des pipelines rejouables par `dvc repro`. Le prix : Git est obligatoire, pas de branches ni de transactions côté stockage, un surcoût sur les très nombreux petits fichiers, et une maintenance minimale depuis le rachat du projet par lakeFS (aucune release depuis mars 2026).
- [[lakeFS]] — le versionnage **d'un dépôt d'objets** : branches, commits, merges atomiques et retour en arrière au-dessus d'un stockage S3-compatible, lu par les outils S3 existants. Le prix : un serveur et PostgreSQL à exploiter, une licence BSL 1.1 depuis la v1.87.0 — usage interne non modifié seulement —, un seul utilisateur en édition libre, et aucun lien avec Git.
- [[Delta Lake]] — le versionnage **d'une table** par un journal de transactions sur Parquet : `VERSION AS OF`, `RESTORE`, `MERGE`, Change Data Feed, lisible sans JVM par `delta-rs`. Le prix : l'historique est borné par `VACUUM` (7 jours par défaut) et par la durée du journal (30 jours), les écritures concurrentes sur S3 demandent un mécanisme de verrou, et des optimisations restent propres à Databricks.
- [[Apache Iceberg]] — le versionnage **d'une table** par des snapshots et un catalogue, lu par plusieurs moteurs (Spark, Trino, Flink, DuckDB). Le prix : un catalogue à choisir et à exploiter, et une expiration des snapshots à planifier, sans quoi le stockage grossit ; le time travel s'arrête aux snapshots conservés.

**Critère par critère**

**Niveau versionné.** [[DVC]] : des fichiers et des dossiers, par leur empreinte. [[lakeFS]] : un dépôt entier d'objets, sans sémantique de ligne ni de schéma — les fichiers Delta ou Iceberg y sont stockés tels quels. [[Delta Lake]] et [[Apache Iceberg]] : une **table**, avec schéma, transactions et requêtes SQL ; le versionnage est un effet du format, pas un outil posé dessus.

**Reproduire un entraînement à partir d'un jeu daté.** [[DVC]] : `git checkout <tag>` puis `dvc pull` restaure le jeu exact, `dvc repro` rejoue le pipeline. [[lakeFS]] : un commit ou un tag désigne l'état, et la lecture passe par `s3://dépôt/<commit>/chemin` ; le lien avec le run d'entraînement se note à la main, par exemple comme paramètre du run [[MLflow]] (intégration documentée par lakeFS). [[Delta Lake]] et [[Apache Iceberg]] : on interroge la table à une version ou à un horodatage, **tant que les snapshots ou les fichiers existent** — un `VACUUM` ou une expiration de snapshots efface la possibilité de revenir, donc la reproductibilité sur plusieurs mois suppose de figer l'état autrement.

**Intégration Git.** [[DVC]] : native et obligatoire ; Git porte la version. [[lakeFS]], [[Delta Lake]], [[Apache Iceberg]] : aucune ; la version vit dans le serveur ou dans la table, et la relier au code est à la charge du pipeline.

**Stockage et hébergement.** [[DVC]] : un remote au choix — dossier réseau, SSH, S3-compatible —, aucun serveur. [[lakeFS]] : un stockage S3-compatible (la documentation cite MinIO, Ceph et NetApp StorageGRID) **et** PostgreSQL 11 ou plus, plus un serveur sans état. [[Delta Lake]] : un stockage et un moteur (Spark, Flink, DuckDB, ou `delta-rs`) ; sur S3, un seul driver d'écriture par défaut, ou un verrou. [[Apache Iceberg]] : un stockage objet, un moteur **et** un catalogue.

**Coût d'exploitation.** [[DVC]] : nul, une commande et un remote. [[lakeFS]] : une base et un serveur à sauvegarder, à monter en version, et à régler par une licence si plus d'un utilisateur. [[Delta Lake]] : la maintenance `OPTIMIZE` et `VACUUM`. [[Apache Iceberg]] : la compaction, l'expiration des snapshots et le catalogue.

**Licence.** [[DVC]] : Apache-2.0, dépôt sous le nom de Treeverse depuis novembre 2025. [[lakeFS]] : **BSL 1.1 depuis la v1.87.0 du 2026-09-22**, production permise pour un usage interne non modifié, conversion en Apache-2.0 quatre ans après chaque version ; les versions jusqu'à la v1.86.0 restent en Apache-2.0 ; une ESN qui héberge lakeFS pour un client n'est pas dans le cas « interne ». [[Delta Lake]] : Apache-2.0, sous la Linux Foundation. [[Apache Iceberg]] : Apache-2.0, sous la fondation Apache.

**On tranche, sur site, dans cet ordre** : un projet ML déjà dans Git, des données de quelques centaines de Gio → [[DVC]] ; des branches de données sur un dépôt d'objets, un seul organisme qui l'exploite → [[lakeFS]] ; des tables et des mises à jour ligne à ligne → [[Delta Lake]] si le socle est Spark, [[Apache Iceberg]] si plusieurs moteurs doivent se partager les tables.

**Pas de fiche ici** :

- **ClearML** — sa suite ajoute la gestion de données versionnées (cf. [[ClearML]]) ; un versionnage qui suit l'outil de suivi d'expériences, sans l'évaluer à part.
- **Apache Hudi** — format de table orienté mises à jour et flux de changements, cité par la fiche d'Apache Iceberg ; hors du brain, non évalué.
- **Git LFS** — cité par la notion [[Versionnage de données]] ; non évalué ici.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Fiabilité des données]] — le hub du dossier.
- [[Versionnage de données]] — les principes : snapshot ou versionnage par contenu, fichiers, dépôt ou table.
- [[Model registry & versioning]] — le pendant côté modèle : la donnée versionnée ici se relie au modèle enregistré là.
- [[Comparatif - Orchestrateurs ML]] — les orchestrateurs versionnent leurs propres artefacts, pas le jeu source.
