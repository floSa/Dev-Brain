---
role: hub
nom: Bases de données
alias: [base de données, bdd, database, sgbd, dbms]
pitch: Stocker et interroger de la donnée de façon durable — les familles de moteurs, leurs compromis, et quand basculer de l'une à l'autre.
domaines: [data-eng, data-sci, ai-eng]
tags: [relational, nosql, columnar, timeseries, graph-db, vector-db, search]
---

# Bases de données

> Stocker et interroger de la donnée de façon durable — les familles de moteurs, leurs compromis, et quand basculer de l'une à l'autre.

## Aperçu

- Système qui stocke, organise et restitue des données de façon durable et interrogeable.
- Le choix d'une base = un compromis entre modèle de données, cohérence, échelle et type de charge (OLTP transactionnel vs OLAP analytique).
- Plusieurs **familles** coexistent ; chacune optimise un usage. La connaître évite de plier un problème dans le mauvais modèle.

## Concepts clés

### Relationnel (SQL)
- Données en tables à schéma fixe, reliées par clés ; langage SQL ; transactions **ACID**.
- Le défaut solide pour la majorité des applications. Implémentations Dev : [[Postgres]], [[MySQL]], [[MariaDB]], [[SQLite]], [[Microsoft SQL Server]], et le distribué [[CockroachDB]].

### NoSQL
- Document (JSON, [[MongoDB]]), clé-valeur (cache, [[Redis]]), wide-column ([[Apache Cassandra]]).
- Schéma souple et scale horizontal, au prix d'une cohérence souvent relâchée (`BASE` plutôt qu'ACID).

### Colonne / OLAP
- Stockage orienté colonnes, optimisé pour l'agrégation analytique sur de gros volumes. Implémentations Dev : [[ClickHouse]] (distribué) et [[DuckDB]] (embarqué) ; managé type BigQuery.
- À l'opposé du relationnel ligne-à-ligne pensé pour l'OLTP.

### Graphe
- Nœuds et arêtes typées ; idéal pour les données fortement connectées et le parcours de relations profondes que SQL exprime mal.
- Implémentations Dev : [[Neo4j]] (natif, mono-instance) et le distribué [[Nebula Graph]].

### Vectoriel
- Stocke des embeddings et retrouve les plus proches par recherche ANN. Détail : [[Bases de données vectorielles]].

### Temporel
- Séries temporelles et métriques, optimisé pour l'écriture séquentielle et les fenêtres temporelles. Implémentations Dev : [[TimescaleDB]] (extension Postgres) et [[InfluxDB]] (serveur autonome, métriques + IoT).

### Recherche / full-text
- Indexation de documents pour la recherche plein texte (pertinence, agrégations, logs), souvent en complément d'une base primaire plutôt qu'à sa place. Implémentation Dev : [[Elasticsearch]].

## Les maths, simplement

- Index B-tree : recherche d'une clé en $O(\log n)$ au lieu d'un balayage $O(n)$ — la raison d'être des index.
- Théorème **CAP** : en cas de partition réseau, un système distribué ne tient au plus que 2 des 3 propriétés Cohérence / Disponibilité / tolérance aux Partitions. Le relationnel distribué (NewSQL) privilégie C+P.
- Normalisation : décomposer pour éliminer la redondance (formes normales) ; on dénormalise sciemment pour la lecture analytique.

## En pratique

- Démarrer relationnel par défaut ([[Postgres]]) ; ne changer de famille que sur un besoin avéré (échelle, modèle, charge).
- OLTP (beaucoup de petites transactions) → relationnel ; OLAP (grosses agrégations) → colonne ; relations profondes → graphe ; recherche sémantique → vectoriel.
- Un même projet combine souvent plusieurs familles (polyglot persistence) : relationnel + cache clé-valeur + vectoriel.
- Pièges : choisir NoSQL « pour scaler » sans en avoir besoin ; ignorer le coût de cohérence du distribué ; sous-estimer l'outillage et l'écosystème dans le choix.

## Approches voisines & alternatives

- Implémentations relationnelles (Dev) : [[Postgres]], [[MySQL]], [[MariaDB]], [[SQLite]], [[CockroachDB]], [[Microsoft SQL Server]].
- Implémentations NoSQL (Dev) : [[MongoDB]] (document), [[Redis]] (clé-valeur), [[Apache Cassandra]] (wide-column).
- Implémentations graphe (Dev) : [[Neo4j]], [[Nebula Graph]] (distribué).
- Implémentations colonne / OLAP (Dev) : [[ClickHouse]] (distribué), [[DuckDB]] (embarqué).
- Implémentations temporelles (Dev) : [[TimescaleDB]] (extension Postgres), [[InfluxDB]] (serveur autonome).
- Implémentation recherche / full-text (Dev) : [[Elasticsearch]].
- Sous-famille spécialisée détaillée : [[Bases de données vectorielles]].

### Outillage

- Clients GUI / administration (Wiki) : [[DBeaver]] (universel), [[DataGrip]] (IDE), [[HeidiSQL]] (Windows léger), [[pgAdmin]] (Postgres), [[MySQL Workbench]] (MySQL), [[MongoDB Compass]] (Mongo), [[Redis Insight]] (Redis).
- Évolution du schéma : [[Migrations de schéma]] — outils [[Liquibase]], [[Flyway]].
- Accès aux données typé : [[ORM]] — implémentation [[Prisma]].

## Pour aller plus loin

- Comparatif des moteurs relationnels : [[Comparatif - Bases relationnelles]] (vue Dev).
- Comparatif des moteurs NoSQL : [[Comparatif - Bases NoSQL]] (vue Dev).
- Comparatif des moteurs de graphe : [[Comparatif - Bases graphes]] (vue Dev).
- Comparatif des moteurs colonne / OLAP : [[Comparatif - Bases colonnes]] (vue Dev).
- Comparatif des moteurs temporels : [[Comparatif - Bases temporelles]] (vue Dev).
- Comparatif des clients GUI : [[Comparatif - Clients de bases de données]] (vue Wiki).
- Comparatif des outils de migration : [[Comparatif - Migrations de schéma]] (vue Dev).
- Notions d'outillage : [[Migrations de schéma]], [[ORM]].
- Référence : *Designing Data-Intensive Applications* (M. Kleppmann) pour les compromis cohérence/échelle.

<!-- AUTO:START -->
### Sous-domaines
- [[Administration]] · [[Recherche]] · [[Relationnel]] · [[Vectoriel]]

### Notions
- [[Migrations de schéma]] — domaines : data-eng
- [[ORM]] — domaines : data-eng

### Briques
- [[ADBC]] — Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement des données Arrow.
- [[Alembic]] — Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle.
- [[Apache Cassandra]] — Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter.
- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence.
- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur.
- [[Flyway]] — Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build.
- [[InfluxDB]] — SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles.
- [[Liquibase]] — Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD.
- [[MongoDB]] — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding.
- [[Nebula Graph]] — Base de graphes distribuée pour jeux de données massifs.
- [[Neo4j]] — SGBD de graphes natif, leader des données connectées : modèle propriété-graphe et requêtes Cypher.
- [[Prisma]] — ORM TypeScript nouvelle génération : schéma déclaratif, client typé et migrations générées.
- [[psycopg2]] — Adaptateur PostgreSQL de référence pour Python (LGPL) — implémentation DB-API 2.0 en C au-dessus de libpq, sûre et performante ; figé en fonctionnalités, successeur psycopg 3.
- [[Redis]] — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub.
- [[SQLAlchemy]] — Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0.
- [[SQLModel]] — Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI.
- [[TimescaleDB]] — Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres.

### Comparatifs
- [[Comparatif - Bases NoSQL]]
- [[Comparatif - Bases colonnes]]
- [[Comparatif - Bases graphes]]
- [[Comparatif - Bases temporelles]]
- [[Comparatif - Migrations de schéma]]
- [[Comparatif - ORM]]
<!-- AUTO:END -->
