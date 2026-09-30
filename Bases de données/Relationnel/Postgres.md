---
role: brique
nom: Postgres
alias: [postgres, postgresql, pg]
pitch: "SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne."
categorie: database/relationnel
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: C
scaling: single-node
alternatives: ["[[MySQL]]", "[[MariaDB]]", "[[SQLite]]", "[[CockroachDB]]", "[[Microsoft SQL Server]]"]
complements: ["[[pgvector]]", "[[pgAdmin]]", "[[TimescaleDB]]", "[[psycopg2]]", "[[Apache AGE]]", "[[dbt Core]]", "[[SQLMesh]]", "[[Great Expectations]]", "[[Soda Core]]", "[[Airbyte]]", "[[dlt]]", "[[Debezium]]", "[[Apache NiFi]]", "[[OpenMetadata]]", "[[DataHub]]"]
tags: [relational, postgres]
url_docs: https://www.postgresql.org/docs/
url_repo: https://github.com/postgres/postgres
---

# Postgres

<!-- AUTO:BANDEAU:START -->
> SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C | open-source | self-hébergé ou managé · mono-nœud | production | à jour · 2026-08-11 |
<!-- AUTO:BANDEAU:END -->

## Définition

SGBD relationnel-objet conforme SQL, bâti sur MVCC : les lecteurs ne bloquent pas les
écrivains, et les transactions ACID tiennent sous charge. Sa particularité est
l'**extensibilité** — types personnalisés, fonctions, langages procéduraux, et des extensions
qui ajoutent un domaine entier au même moteur : PostGIS pour le géospatial, pgvector pour le
vectoriel, TimescaleDB pour les séries. Le type `JSONB` absorbe le semi-structuré sans quitter
le relationnel. C'est le défaut raisonnable pour une base applicative.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Base applicative transactionnelle (OLTP) généraliste | VACUUM et bloat à surveiller sous forte charge d'`UPDATE` / `DELETE` |
| Types riches, `JSONB`, requêtes complexes ou contraintes d'intégrité fortes | Connexions coûteuses : au-delà de quelques centaines, un pooler (PgBouncer) devient obligatoire |
| Tirer parti des extensions : PostGIS, pgvector, TimescaleDB, toutes dans le même moteur | Paramètres par défaut conservateurs (`work_mem`, `shared_buffers`) : sans tuning, les performances restent en deçà |
| Cohérence transactionnelle stricte sur un nœud, avec réplicas en lecture | |

## Mise en œuvre

- Installation — paquet système ou image Docker officielle ; managé partout (RDS, Cloud SQL, Supabase, Neon)
- Point d'entrée — serveur SQL sur le port 5432 ; client `psql`, pilotes standard ([[psycopg2]], [[SQLAlchemy]])
- Prérequis — un serveur à administrer ; les extensions s'installent une par une, par `CREATE EXTENSION`
- Exécution — un primaire plus des réplicas de lecture ; scaling vertical, sharding par l'extension Citus si nécessaire
- Coût — gratuit, licence PostgreSQL permissive ; la dépense est celle du serveur et de son exploitation

## Écosystème

### Alternatives

- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

### Compléments

- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place. — la recherche vectorielle dans la base métier, sans second moteur
- [[pgAdmin]] — Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur. — l'administration et la supervision graphiques du serveur
- [[TimescaleDB]] — Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres. — l'extension qui ajoute les hypertables et les agrégats continus, sans changer de moteur
- [[Apache AGE]] — Extension PostgreSQL qui ajoute un graphe de propriétés interrogé en openCypher depuis SQL (Apache-2.0, projet de premier niveau de l'ASF) — aucune base de plus à opérer, mais pas de bibliothèque d'algorithmes ni de scale-out propre. — l'extension qui ajoute un graphe de propriétés, sans second moteur.
- [[psycopg2]] — Adaptateur PostgreSQL de référence pour Python (LGPL) — implémentation DB-API 2.0 en C au-dessus de libpq, sûre et performante ; figé en fonctionnalités, successeur psycopg 3. — le driver DB-API historique, sous la plupart des accès Python à cette base
- [[dbt Core]] — Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit). — `dbt-postgres` (1.11.0, 2026-07-16), adaptateur `Trusted` maintenu par dbt Labs ; il n'existe pas en dbt v2.
- [[SQLMesh]] — Framework de transformation SQL à environnements virtuels : plan/apply sur des modèles versionnés, lignage au niveau colonne, exécution incrémentale par intervalles suivis et audits (Apache-2.0, Python) ; sous gouvernance Linux Foundation depuis mars 2026 après le rachat de Tobiko par Fivetran. — moteur d'exécution pris en charge (extra `postgres`) et base d'état recommandée (`state_connection`), à côté du moteur de données.
- [[Great Expectations]] — Cadre de validation de données en Python : des Expectations groupées en suites, exécutées par des Checkpoints sur des tables SQL, pandas ou Spark, avec rapports HTML Data Docs (GX Core, Apache-2.0) ; dépôt repris par Fivetran en 2026. — source SQL de la liste de compatibilité officielle de GX (extra `postgresql`).
- [[Soda Core]] — Vérification de la qualité des données par contrats YAML, exécutée en ligne de commande ou en Python sur PostgreSQL, Trino, DuckDB et une quinzaine d'autres sources ; licence Elastic 2.0 depuis la v4 (source-available), historique et alertes réservés à Soda Cloud. — paquet `soda-postgres` : les contrôles s'exécutent en SQL dans la base.
- [[Airbyte]] — Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes. — source en disponibilité générale (`source-postgres` 3.8.5), en curseur, en `xmin` ou en CDC par slot `pgoutput`, et destination en disponibilité générale.
- [[dlt]] — Bibliothèque Python d'ingestion : des générateurs Python deviennent des tables typées chargées dans DuckDB, Postgres, ClickHouse ou des fichiers, avec schéma inféré, état et curseurs incrémentaux stockés dans la destination, sans serveur (Apache-2.0). — destination, et source CDC par `pg_replication` (slot logique `pgoutput`, sans Kafka).
- [[Debezium]] — Capture de changements (CDC) par le journal de transactions : événements par ligne (avant/après) depuis Postgres, MySQL, MariaDB, SQL Server, Oracle et MongoDB, via Kafka Connect, un serveur autonome sans Kafka ou un moteur Java embarqué (Apache-2.0). — source de capture par décodage logique (`wal_level=logical`, `pgoutput`), versions 14 à 18.
- [[Apache NiFi]] — Plateforme de flux de données à interface graphique : des centaines de processeurs (fichiers, SFTP, JDBC, MQTT, syslog, Kafka…) reliés par des files avec contre-pression, provenance de chaque donnée et livraison garantie ; Apache-2.0, JVM, sans broker. — lu et écrit par les processeurs JDBC (`ExecuteSQL`, `QueryDatabaseTable`, `PutDatabaseRecord`).
- [[OpenMetadata]] — Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate). — base possible du serveur (PostgreSQL 15 ou plus) et connecteur de base.
- [[DataHub]] — Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud). — base possible du serveur et source listée en GA.

## Ressources

- Documentation — https://www.postgresql.org/docs/
- Dépôt — https://github.com/postgres/postgres

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases relationnelles]] — ce qui départage les moteurs du dossier
