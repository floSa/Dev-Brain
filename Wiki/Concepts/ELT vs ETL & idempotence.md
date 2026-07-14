---
galaxie: wiki
type: concept
nom: ELT vs ETL & idempotence
alias: [ELT, ETL, idempotence, rejouabilité, backfill, rerun]
categorie: concept/data
domaines: [data-eng]
tags: [data-pipeline, idempotence]
---

# ELT vs ETL & idempotence

## Aperçu

- Deux ordres d'assemblage d'un pipeline de données : **ETL** transforme avant de charger, **ELT** charge brut puis transforme dans la cible.
- L'**idempotence** est la propriété qui rend ces pipelines sûrs à rejouer : un même run relancé produit le même état final, sans doublon ni dérive.

## Concepts clés

### ETL — transform then load
- Extract → Transform → Load : la donnée est nettoyée et mise en forme **avant** d'atterrir dans la cible.
- Pertinent quand la cible est coûteuse ou contrainte (entrepôt cher, schéma strict), ou quand des règles métier/PII doivent s'appliquer en amont.
- Coût : la logique de transformation vit hors de la cible, plus dure à versionner et à rejouer.

### ELT — load then transform
- Extract → Load → Transform : on charge la donnée **brute** dans la cible (entrepôt, lakehouse), puis on transforme en SQL/compute sur place.
- Dominant avec les entrepôts modernes (BigQuery, Snowflake, DuckDB) : le compute scalable de la cible absorbe la transformation, et le brut reste disponible pour re-dériver.
- Les transformations deviennent du code versionné (modèles dbt/SQL), testables et rejouables.

### Idempotence
- Un traitement est idempotent si l'appliquer une fois ou N fois donne le même résultat. C'est ce qui permet de relancer un job en échec sans corrompre les données.
- Mécanismes courants : écriture par `MERGE`/upsert sur clé, `INSERT OVERWRITE` d'une partition entière, `DELETE`+`INSERT` bornés par fenêtre, plutôt qu'un `INSERT` aveugle qui duplique.

### Reruns & backfills
- **Rerun** : rejouer un run échoué — n'est sûr que si l'étape est idempotente.
- **Backfill** : (re)calculer l'historique passé, partition par partition. Le partitionnement temporel rend chaque tranche indépendante et rejouable isolément.
- Clé de design : des étapes **déterministes** et **partitionnées**, où l'unité d'écriture correspond à l'unité de rejeu.

## En pratique

- Par défaut viser l'ELT quand la cible a du compute scalable : on garde le brut, on transforme en code versionné, on rejoue sans réingérer.
- Rendre chaque tâche idempotente avant de se soucier d'orchestration : un [[Dev/Services/Airflow|Airflow]] ou un [[Dev/Services/Dagster|Dagster]] qui relance une étape non idempotente ne fait qu'amplifier le dégât.
- [[Dev/Services/Dagster|Dagster]] (assets partitionnés) matérialise nativement le couple partition ↔ unité de rejeu ; sur [[Dev/Services/Airflow|Airflow]], la même discipline passe par des tâches idempotentes et l'`execution_date`.
- Pièges : `INSERT` non borné qui duplique au rerun, transformation dépendante de l'horloge courante (non déterministe), backfill qui écrase une partition encore en cours d'écriture.
- Adosser des contrôles : voir [[Contrats de données & qualité]] pour bloquer une charge non conforme avant qu'elle ne se propage.

## Approches voisines & alternatives

- [[Change Data Capture (CDC)]] — mode d'extraction incrémental qui alimente l'étape *Load*.
- [[Contrats de données & qualité]] — portes de qualité posées sur les étapes du pipeline.
- [[Versionnage de données]] — snapshots qui rendent un rerun/backfill reproductible.
- [[Migrations de schéma]] — même exigence d'idempotence, côté structure de base.
- Orchestrateurs : [[Dev/Services/Airflow|Airflow]], [[Dev/Services/Dagster|Dagster]] (cf. [[Comparatif - Orchestrateurs data]]).

## Pour aller plus loin

- Transformation ELT en code : dbt (modèles SQL versionnés, tests, matérialisations incrémentales) — service non encore fiché.
- Principe directeur : *functional data engineering* (Maxime Beauchemin) — tâches pures, partitions immuables, rejeu déterministe.
