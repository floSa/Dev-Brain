---
galaxie: wiki
type: concept
nom: Architecture médaillon
alias: [medallion, médaillon, architecture médaillon, bronze silver gold, bronze/silver/gold, multi-hop architecture]
categorie: concept/data
domaines: [data-eng]
tags: [data-modeling, data-pipeline, lakehouse, data-quality]
---

# Architecture médaillon

## Aperçu

- Organise les données d'un lakehouse en **trois couches** de qualité croissante : **Bronze** (brut), **Silver** (nettoyé/conformé), **Gold** (agrégé/métier).
- Chaque couche est une étape de raffinage : on ne réécrit pas la source, on **dérive** la suivante. Le brut reste disponible pour tout re-calculer (multi-hop).

## Concepts clés

### Bronze — données brutes
- Ingestion **telle quelle** depuis les sources (fichiers, [[Change Data Capture (CDC)|CDC]], flux), sans transformation métier.
- Append-only, historisé, idéalement immuable : c'est le filet de sécurité qui rend tout backfill possible.
- Au plus quelques ajouts techniques : horodatage d'ingestion, nom de source, fichier d'origine.

### Silver — données nettoyées & conformées
- Typage, déduplication, résolution des nulls, jointures de conformité, application des [[Contrats de données & qualité|contrats de données]].
- Modèle souvent normalisé / par entité métier : une table par concept (clients, commandes), clés stables.
- C'est la couche « source de vérité » exploitable, sur laquelle s'appuient analystes et features ML.

### Gold — données métier
- Agrégats, tables de faits/dimensions (schéma en étoile), KPIs, datamarts par usage (BI, reporting, feature serving).
- Optimisée pour la lecture : dénormalisée, pré-agrégée, partitionnée pour les requêtes cibles.

### Propagation incrémentale & lineage
- Le flux est unidirectionnel Bronze → Silver → Gold ; chaque couche se recalcule depuis la précédente, pas depuis la source.
- Le raffinage se fait en [[ELT vs ETL & idempotence|ELT]] : transformations versionnées (SQL/dbt), idempotentes, partition par partition.
- Le lineage entre couches rend traçable d'où vient chaque chiffre Gold et permet de rejouer une couche sans toucher les autres.

## En pratique

- Cadre par défaut sur un lakehouse ([[Dev/Services/Apache Iceberg|Apache Iceberg]] / Delta Lake) où chaque couche est un jeu de tables transactionnelles posées sur [[Dev/Services/Parquet|Parquet]].
- Garder Bronze **immuable et exhaustif** : sa valeur est de pouvoir tout re-dériver après un bug de transformation. Ne jamais y appliquer de règle métier.
- Poser les portes de qualité au passage Bronze → Silver : une charge non conforme est rejetée là, pas propagée en Gold. Cf. [[Contrats de données & qualité]].
- Partitionner chaque couche selon ses requêtes ([[Partitionnement & layout de données]]) ; soigner la taille de fichiers, surtout en Bronze alimenté par du flux.
- Pièges : transformer trop tôt (perte du brut), Silver fourre-tout sans modèle clair, Gold qui recalcule depuis la source au lieu de Silver, couches qui se télescopent (écritures croisées).
- Les noms ne sont pas sacrés : 2 couches suffisent parfois (raw / curated) ; au-delà de 3, on duplique souvent sans gagner.

## Approches voisines & alternatives

- [[ELT vs ETL & idempotence]] — le moteur de raffinage entre couches : transformations versionnées et rejouables.
- [[Partitionnement & layout de données]] — comment chaque couche est rangée physiquement.
- [[Contrats de données & qualité]] — les portes posées au passage entre couches.
- [[Versionnage de données]] — snapshots/time travel par couche, pour figer un état reproductible.
- [[Change Data Capture (CDC)]] — alimente fréquemment la couche Bronze.
- Alternative de modélisation : Data Vault (hubs/links/satellites) ou Kimball pur (étoile sans couche brute durable) — autres façons d'organiser le raffinage.

## Pour aller plus loin

- Implémentations de référence : Databricks (origine du terme « medallion »), équivalents sur Iceberg + dbt.
- Format de table sous-jacent : [[Dev/Services/Apache Iceberg|Apache Iceberg]] (ACID, time travel) — service Dev.
- Outil de transformation entre couches : dbt (modèles SQL versionnés) — non encore fiché.
