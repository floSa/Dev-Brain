---
role: notion
nom: OLTP, OLAP et lakehouse
alias: [OLTP, OLAP, lakehouse, entrepôt de données, data warehouse, data lake, moteur de requête fédéré]
categorie: database/analytique
domaines: [data-eng, data-sci]
tags: [olap, columnar, lakehouse, query-engine, federation]
---

# OLTP, OLAP et lakehouse

## Aperçu

- Deux charges que tout oppose. **OLTP** : beaucoup de petites transactions qui lisent ou écrivent quelques lignes (une commande, un paiement), où la latence et la cohérence comptent. **OLAP** : peu de requêtes qui balaient de gros volumes sur quelques colonnes (chiffre d'affaires par mois et par région), où le débit de lecture compte.
- Les architectures analytiques se sont succédé pour séparer ces charges : l'**entrepôt** (données structurées, chargées dans un moteur qui les possède), le **lac** (fichiers bruts sur stockage bon marché), puis le **lakehouse**, qui garde des fichiers ouverts sur stockage objet et leur ajoute une couche de table transactionnelle.
- Sur site, le choix se ramène à trois formes : un moteur embarqué ([[DuckDB]]), une base colonnes qui possède ses données ([[ClickHouse]]), ou un moteur de requête posé sur un lac ([[Trino]] sur [[Apache Iceberg]]).

## Concepts clés

### Ligne ou colonne
- Un stockage **par lignes** range ensemble les champs d'un enregistrement : lire ou écrire une ligne entière est rapide, balayer une colonne oblige à tout lire. Un stockage **par colonnes** range ensemble les valeurs d'un même champ : une agrégation ne lit que les colonnes utiles, et la compression est bien meilleure.
- Le papier C-Store (Stonebraker et al., VLDB 2005) oppose les architectures optimisées pour l'écriture et celles optimisées pour la lecture, et annonce des résultats préliminaires nettement meilleurs sur un sous-ensemble de TPC-H. Abadi, Madden et Hachem (SIGMOD 2008) montrent qu'**émuler** un column-store dans une base à lignes (partitionnement vertical, index couvrants, vues matérialisées) reste nettement plus lent sur le Star Schema Benchmark : il faut changer le stockage **et** l'exécuteur de requêtes.
- Sur fichier, [[Parquet]] est le format colonnaire de référence ; [[Apache Arrow]] en est l'équivalent en mémoire.

### Entrepôt, lac, lakehouse
- L'**entrepôt** charge les données dans son propre stockage (ETL ou ELT) : performant et gouverné, mais les données sont dans un format que seul le moteur lit. Le **lac** range des fichiers sur stockage objet, lisibles par tout outil, sans transactions ni schéma imposé.
- Le **lakehouse** (Armbrust, Ghodsi, Xin, Zaharia, CIDR 2021) garde des fichiers ouverts ([[Parquet]]) sur stockage objet et pose dessus une **couche de métadonnées transactionnelle** qui dit quels fichiers composent une version de table : [[Delta Lake]] (journal de transactions dans le stockage objet, papier VLDB 2020) ou [[Apache Iceberg]] (fichiers de métadonnées remplacés par échange atomique, lecteurs sans verrou, selon sa spécification). Les performances viennent d'optimisations qui laissent les fichiers intacts : statistiques min/max, cache, organisation des données.
- Le benchmark du papier Lakehouse est interne à Databricks, et les auteurs reconnaissent les limites du design : les transactions ne portent que sur **une table**, et le journal, stocké sur le stockage objet, borne le débit de transactions.

### Moteur de requête séparé du stockage
- L'idée : le moteur **ne possède pas** les données, il les lit en place. Dremel (Google, VLDB 2010) présente l'analyse *in situ* : pas de phase de chargement, que le papier tient pour un frein majeur à l'usage des bases pour l'analytique. Presto (Facebook, ICDE 2019) généralise : une API de **connecteurs** donne accès à HDFS et S3, aux bases relationnelles, au NoSQL et à Kafka, et ses métadonnées sont dans un service séparé du stockage.
- Conséquence pratique : on peut **fédérer** — joindre dans une requête une table de lac et une table d'une base métier — et changer de moteur sans migrer les données. [[Trino]] est le descendant de Presto.
- Prix : un catalogue de tables à héberger (Hive Metastore, JDBC, REST, Nessie), un stockage objet ([[Ceph]], [[SeaweedFS]], [[MinIO]] archivé depuis le 2026-04-25) et une JVM distribuée à exploiter. Un moteur embarqué n'a rien de tout cela.

### Pourquoi ne pas interroger la base de production
- Les requêtes analytiques sont longues et gourmandes en CPU et en I/O, sur une base pensée pour des transactions courtes. La documentation PostgreSQL établit que, grâce au MVCC, la lecture ne bloque jamais l'écriture : le verrouillage n'est donc pas le vrai coût, mais la charge reste sur le primaire, et les anciennes versions de lignes s'accumulent pendant la requête.
- Sur un réplica de lecture, les requêtes en conflit avec le rejeu du journal sont **annulées** passé le délai configuré (`max_standby_streaming_delay`) ; `hot_standby_feedback` évite l'annulation mais peut gonfler les tables du primaire. L'argument est une déduction des mécanismes de [[Postgres]], pas une règle que la documentation énonce.
- Usage courant : copier la donnée vers un stockage analytique (ELT, capture de changements), puis la modéliser. Kleppmann (*Designing Data-Intensive Applications*, chap. 3) développe le même raisonnement ; le chapitre n'a pas pu être relu ici.

## En pratique

- **Choisir selon le volume et le nombre d'utilisateurs, pas selon la mode.** Aucun seuil publié et fiable ne dit « au-delà de N To, passer au cluster » ; il se mesure sur ses propres requêtes. Mühleisen (« The Lost Decade of Small Data? », mai 2025) soutient que le matériel moderne suffit pour l'essentiel des charges : médiane de lecture d'environ 100 Mo par requête sur Redshift ou Snowflake, et un portable de 2012 qui exécute TPC-H à 265 Go avec DuckDB. Chiffres cités par l'éditeur de DuckDB, requêtes à froid, source des chiffres non vérifiée.
- **Un poste ou un serveur, un ou deux analystes** : [[DuckDB]] sur du Parquet. **Données d'événements à fort débit, tableaux de bord sub-seconde, append** : [[ClickHouse]]. **Plusieurs équipes, plusieurs sources, un lac sur stockage objet, des BI** : [[Trino]] sur Iceberg. Les trois peuvent coexister ; ils ne sont pas concurrents sur tous les cas.
- **Formats et échange.** [[Parquet]] pour le fichier, Iceberg ou Delta pour la table, [[Apache Arrow]] pour passer les colonnes d'un moteur à l'autre, [[ADBC]] pour les lire depuis une base.
- **BI.** Une BI ([[Metabase]], [[Apache Superset]]) n'a pas de moteur : elle envoie du SQL à l'un de ces trois. Cf. [[Comparatif - BI auto-hébergée]].
- **Nuances.** Le lakehouse n'est pas accepté sans réserve. Dans « DuckLake » (mai 2025), l'équipe de DuckDB soutient qu'Iceberg et Delta ont été conçus pour se passer de base de données, d'où des métadonnées en fichiers, des catalogues en plus et pas de transactions multi-tables ; elle propose de mettre les métadonnées dans une base SQL. Les auteurs sont partie prenante et reconnaissent que cela déplace la complexité vers un catalogue SQL. Le papier CIDR 2023 (Jain et al.) compare Delta, Hudi et Iceberg et montre des différences mesurées, là où le papier Lakehouse les traite comme équivalents.
- Pièges : copier la base de production vers l'entrepôt sans capture de changements fiable ; confondre format de fichier, format de table et moteur ; croire qu'un lakehouse dispense de modéliser ; installer un cluster pour des données qui tiennent sur un disque.

## Approches voisines & alternatives

- [[Modélisation dimensionnelle]] — comment ranger les tables pour l'analyse, une fois le moteur choisi ; la présente notion ne la reprend pas.
- [[Architecture médaillon]] — les couches de raffinage bronze, silver, gold qui se posent sur un lakehouse.
- [[Partitionnement & layout de données]] — ce qui décide du coût réel de lecture, quel que soit le moteur.
- [[Formats de fichiers et de tables]] — le hub des formats de fichier et de table.
- [[Bases de données]] — le hub du domaine, dont les familles relationnelles, NoSQL et colonnes.
- [[Comparatif - Bases colonnes]] — départage [[DuckDB]], [[ClickHouse]] et [[Trino]].

## Pour aller plus loin

- Armbrust, Ghodsi, Xin, Zaharia, « Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics », CIDR 2021 — https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf
- Stonebraker et al., « C-Store: A Column-oriented DBMS », VLDB 2005 — https://www.vldb.org/conf/2005/papers/p553-stonebraker.pdf
- Abadi, Madden, Hachem, « Column-Stores vs. Row-Stores: How Different Are They Really? », SIGMOD 2008 — https://users.cs.utah.edu/~pandey/courses/cs6530/fall22/papers/rowvcolumn/abadi-sigmod08.pdf
- Melnik et al., « Dremel: Interactive Analysis of Web-Scale Datasets », PVLDB 3(1), VLDB 2010 — https://vldb.org/pvldb/vol3/R29.pdf
- Sethi et al., « Presto: SQL on Everything », ICDE 2019 — https://trino.io/Presto_SQL_on_Everything.pdf
- Armbrust et al., « Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores », PVLDB 13(12), 2020 — https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf
- Spécification Apache Iceberg — https://iceberg.apache.org/spec/
- Jain et al., « Analyzing and Comparing Lakehouse Storage Systems », CIDR 2023 — https://vldb.org/cidrdb/2023/analyzing-and-comparing-lakehouse-storage-systems.html
- Mühleisen, « The Lost Decade of Small Data? », 2025 — https://duckdb.org/2025/05/19/the-lost-decade-of-small-data
- Raasveldt, Mühleisen, « DuckLake: SQL as a Lakehouse Format », 2025 — https://duckdb.org/2025/05/27/ducklake.html
- Documentation PostgreSQL, MVCC et Hot Standby — https://www.postgresql.org/docs/current/mvcc-intro.html, https://www.postgresql.org/docs/current/hot-standby.html
