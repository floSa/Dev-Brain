---
role: brique
nom: Trino
alias: [trino, PrestoSQL]
pitch: "Moteur de requête SQL distribué et fédéré, séparé du stockage : une requête interactive joint des tables Iceberg, Delta ou Hive et des bases (PostgreSQL, MySQL…) sans rien stocker lui-même ; Apache-2.0, coordinateur et workers en Java."
categorie: database/analytique
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[DuckDB]]", "[[ClickHouse]]"]
complements: ["[[Apache Iceberg]]", "[[Delta Lake]]", "[[MinIO]]", "[[Apache Superset]]"]
tags: [query-engine, federation, olap, distributed, lakehouse]
url_docs: https://trino.io/docs/current/
url_repo: https://github.com/trinodb/trino
---

# Trino

<!-- AUTO:BANDEAU:START -->
> Moteur de requête SQL distribué et fédéré, séparé du stockage : une requête interactive joint des tables Iceberg, Delta ou Hive et des bases (PostgreSQL, MySQL…) sans rien stocker lui-même ; Apache-2.0, coordinateur et workers en Java.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de requête **SQL distribué**, séparé du stockage : Trino ne possède aucune donnée, il
l'interroge là où elle se trouve, par des **connecteurs** (catalogues). Un même `SELECT` peut
joindre une table Iceberg sur stockage objet, une table PostgreSQL et une collection MongoDB.
Un coordinateur planifie, des workers exécutent en parallèle et en mémoire, le résultat revient
au client (CLI, JDBC, BI). C'est le moteur d'un [[OLTP, OLAP et lakehouse|lakehouse]] : les
fichiers ([[Parquet]]) et le format de table ([[Apache Iceberg]], [[Delta Lake]]) restent
ailleurs. Fork de Presto renommé en décembre 2020, après le départ des fondateurs.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Requêtes interactives sur un lac de fichiers ou de tables Iceberg / Delta, à plusieurs utilisateurs | Un poste ou un serveur suffit : [[DuckDB]] lit les mêmes fichiers sans cluster à opérer |
| Jointure de sources hétérogènes sans les recopier (base métier + lac) | Stockage analytique dédié, ingestion et dashboards sub-seconde → [[ClickHouse]] |
| Stockage objet S3-compatible déjà en place ([[MinIO]]) sans moteur SQL dessus | Charge transactionnelle, petites écritures → [[Postgres]] : Trino n'est pas une base |
| SSO et droits fins sans licence commerciale : OAuth2 / OIDC, LDAP, règles JSON, OPA ou Ranger | Pas de capacité à exploiter une JVM distribuée, un catalogue de tables et un stockage objet |
| Un moteur unique derrière plusieurs BI ([[Apache Superset]], [[Metabase]]) | Base MPP avec stockage propre pour la BI temps réel → Apache Doris ou StarRocks (Apache-2.0, non fichés) |
| | Worker natif C++ (Velox) recherché → PrestoDB, actif (0.299, 2026-08-28, 16,8k étoiles, Java 17) ; Trino a la doc et les connecteurs les plus larges |
| | RBAC géré par interface, audit unifié, cache accéléré, support sous contrat → Starburst Enterprise (payant) |

## Mise en œuvre

- Installation — image Docker officielle `trinodb/trino`, chart Helm officiel ([[Helm]], [[Kubernetes]]), ou archive Linux 64 bits. Constaté le 2026-09-30 : version 483 (2026-07-17), 13,3k étoiles, une version tous les 1 à 3 mois
- Point d'entrée — SQL via la CLI, JDBC ou l'API HTTP ; chaque source se déclare par un fichier de catalogue
- Prérequis — Java 25 (25.0.1 au minimum) ; stockage objet S3-compatible et catalogue de tables : pour Iceberg, JDBC (PostgreSQL recommandé), REST, Nessie, Glue ou Hive Metastore, donc pas de Hive obligatoire ; pour Delta, Hive Metastore ou Glue. Écritures INSERT / UPDATE / DELETE / MERGE sur Iceberg v1 et v2
- Exécution — self-hébergé, distribué : un coordinateur et N workers, heap JVM à 70-85 % de la RAM du nœud ; exécution tolérante aux pannes (`retry-policy` `QUERY` ou `TASK`, exchange manager sur stockage objet pour `TASK`). [[Ceph]] et [[SeaweedFS]] passent par l'API S3, mais la doc ne les nomme pas ; MinIO est testé
- Coût — gratuit, Apache 2.0, sans édition payante dans le dépôt : le payant est chez un tiers (Starburst Enterprise sur site, Galaxy en SaaS seulement). L'ESN peut déployer et livrer Trino librement. Le coût réel est le cluster, le catalogue et le stockage

## Écosystème

### Alternatives

- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — la même lecture de Parquet et d'Iceberg en un seul process, sans cluster : Trino se justifie quand plusieurs utilisateurs ou plusieurs sources partagent le moteur.
- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence. — stockage et moteur intégrés, ingestion à fort débit ; Trino laisse les données où elles sont et les interroge.

### Compléments

- [[Apache Iceberg]] — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB). — format de table lu et écrit par Trino (INSERT, UPDATE, DELETE, MERGE ; spécifications v1 et v2), catalogue JDBC, REST, Nessie, Glue ou Hive.
- [[Delta Lake]] — Format de table ouvert pour le lakehouse, sous la Linux Foundation : un journal de transactions `_delta_log` au-dessus de fichiers Parquet, ACID, time travel, MERGE, évolution de schéma et Change Data Feed ; implémentations Spark, Rust (delta-rs) et Delta Kernel en Apache-2.0, avec des fonctions d'optimisation propres à Databricks hors de l'open source. — connecteur Delta Lake, catalogue Hive Metastore ou Glue uniquement.
- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire. — stockage objet S3-compatible, testé pour l'exchange manager de l'exécution tolérante aux pannes.
- [[Apache Superset]] — BI auto-hébergée Apache-2.0 tournée vers l'exploration : SQL Lab, constructeur de graphiques, tableaux de bord, droits par ligne, alertes et embedding sans édition payante ; exploitation plus lourde (base de métadonnées, Redis, Celery). — BI branchée sur Trino par un dialecte SQLAlchemy : Trino joue le moteur, Superset l'interface.

## Ressources

- Documentation — https://trino.io/docs/current/
- Dépôt — https://github.com/trinodb/trino

## Voir aussi

- [[OLTP, OLAP et lakehouse]] — la notion : pourquoi un moteur séparé du stockage
- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases colonnes]] — ce qui départage les moteurs analytiques du dossier
