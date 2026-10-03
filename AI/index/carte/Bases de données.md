# Bases de données — carte

> Généré par `AI/scripts/build_carte.py`. Ne pas éditer à la main.
> 77 pages, chacune avec son chemin et une ligne.
> Couvre : Administration, Bases de graphes, Recherche, Relationnel, Vectoriel.

## Au niveau du dossier
- [[ADBC]] · brique · `Bases de données/ADBC.md` — Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement…
- [[Alembic]] · brique · `Bases de données/Alembic.md` — Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle.
- [[Apache Cassandra]] · brique · `Bases de données/Apache Cassandra.md` — Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter.
- [[ClickHouse]] · brique · `Bases de données/ClickHouse.md` — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence.
- [[DuckDB]] · brique · `Bases de données/DuckDB.md` — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur.
- [[Flyway]] · brique · `Bases de données/Flyway.md` — Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build.
- [[InfluxDB]] · brique · `Bases de données/InfluxDB.md` — SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles.
- [[Liquibase]] · brique · `Bases de données/Liquibase.md` — Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD.
- [[MongoDB]] · brique · `Bases de données/MongoDB.md` — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding.
- [[Prisma]] · brique · `Bases de données/Prisma.md` — ORM TypeScript nouvelle génération : schéma déclaratif, client typé et migrations générées.
- [[psycopg2]] · brique · `Bases de données/psycopg2.md` — Adaptateur PostgreSQL de référence pour Python (LGPL) — implémentation DB-API 2.0 en C au-dessus de libpq, sûre et performante ; figé en fonctionnalités…
- [[Redis]] · brique · `Bases de données/Redis.md` — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub.
- [[SQLAlchemy]] · brique · `Bases de données/SQLAlchemy.md` — Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0.
- [[SQLModel]] · brique · `Bases de données/SQLModel.md` — Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI.
- [[TimescaleDB]] · brique · `Bases de données/TimescaleDB.md` — Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres.
- [[Trino]] · brique · `Bases de données/Trino.md` — Moteur de requête SQL distribué et fédéré, séparé du stockage : une requête interactive joint des tables Iceberg, Delta ou Hive et des bases (PostgreSQL…
- [[Migrations de schéma]] · notion · `Bases de données/Migrations de schéma.md` — Faire évoluer la structure d'une base (tables, colonnes, index, contraintes) de façon contrôlée et reproductible, au même titre que le code.
- [[OLTP, OLAP et lakehouse]] · notion · `Bases de données/OLTP, OLAP et lakehouse.md` — Deux charges que tout oppose.
- [[ORM]] · notion · `Bases de données/ORM.md` — Object-Relational Mapping : faire correspondre des tables relationnelles à des objets/types du langage, pour manipuler la base sans écrire (tout) le SQL à la…
- [[Comparatif - Bases colonnes]] · comparatif · `Bases de données/Comparatif - Bases colonnes.md` — un cluster ou un seul process, qui possède les données, et la tolérance aux écritures en place.
- [[Comparatif - Bases NoSQL]] · comparatif · `Bases de données/Comparatif - Bases NoSQL.md` — ce qu'on stocke — un document, une structure en RAM, ou un flux d'écritures massif.
- [[Comparatif - Bases temporelles]] · comparatif · `Bases de données/Comparatif - Bases temporelles.md` — a-t-on déjà du Postgres, faut-il du SQL standard avec des jointures, et le site a-t-il déjà un historien industriel.
- [[Comparatif - Migrations de schéma]] · comparatif · `Bases de données/Comparatif - Migrations de schéma.md` — du SQL écrit à la main, un format abstrait portable, ou un diff généré depuis l'ORM.
- [[Comparatif - ORM]] · comparatif · `Bases de données/Comparatif - ORM.md` — le langage de la stack, et la quantité de SQL qu'on veut garder sous la main.

## Administration
- [[DataGrip]] · brique · `Bases de données/Administration/DataGrip.md` — IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs.
- [[DBeaver]] · brique · `Bases de données/Administration/DBeaver.md` — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.
- [[HeidiSQL]] · brique · `Bases de données/Administration/HeidiSQL.md` — Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.
- [[MongoDB Compass]] · brique · `Bases de données/Administration/MongoDB Compass.md` — Client graphique officiel de MongoDB : exploration de documents, requêtes visuelles et analyse de schéma.
- [[MySQL Workbench]] · brique · `Bases de données/Administration/MySQL Workbench.md` — Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur.
- [[pgAdmin]] · brique · `Bases de données/Administration/pgAdmin.md` — Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur.
- [[Redis Insight]] · brique · `Bases de données/Administration/Redis Insight.md` — Client graphique officiel de Redis : exploration des clés, profiling et workbench pour modules (JSON, Search).
- [[Comparatif - Clients de bases de données]] · comparatif · `Bases de données/Administration/Comparatif - Clients de bases de données.md` — un seul moteur ou tous, et le poids qu'on accepte sur le poste.

## Bases de graphes
- [[Apache AGE]] · brique · `Bases de données/Bases de graphes/Apache AGE.md` — Extension PostgreSQL qui ajoute un graphe de propriétés interrogé en openCypher depuis SQL (Apache-2.0, projet de premier niveau de l'ASF) — aucune base de…
- [[ArangoDB]] · brique · `Bases de données/Bases de graphes/ArangoDB.md` — Base multi-modèle (documents, graphes, clé-valeur, recherche) interrogée en AQL (C++, BSL 1.1) — cluster complet, mais binaires Community limités à un usage…
- [[Dgraph]] · brique · `Bases de données/Bases de graphes/Dgraph.md` — Base de graphes distribuée en Go (Apache-2.0) — sharding par prédicat, Raft, DQL et GraphQL natif ; reprise par Istari Digital en 2025, sans offre managée ni…
- [[JanusGraph]] · brique · `Bases de données/Bases de graphes/JanusGraph.md` — Couche de graphe Java au-dessus de Cassandra, ScyllaDB ou HBase et d'un index Elasticsearch ou Solr (Apache-2.0, Linux Foundation) — Gremlin, milliards de…
- [[Memgraph]] · brique · `Bases de données/Bases de graphes/Memgraph.md` — Base de graphes en mémoire, compatible Cypher et Bolt (C++, BSL 1.1) — temps réel et flux Kafka, mono-nœud ; haute disponibilité automatique, RBAC et SSO…
- [[Nebula Graph]] · brique · `Bases de données/Bases de graphes/Nebula Graph.md` — Base de graphes distribuée nativement (Apache-2.0, C++, Raft) pour jeux de données massifs — l'édition Community est figée sur la 3.8.0 de mai 2024…
- [[Neo4j]] · brique · `Bases de données/Bases de graphes/Neo4j.md` — SGBD de graphes natif, référence du modèle propriété-graphe et de Cypher — Community en GPLv3 et mono-instance, cluster et sauvegarde en ligne réservés à…
- [[Bases graphe — modèles et langages de requête]] · notion · `Bases de données/Bases de graphes/Bases graphe — modèles et langages de requête.md` — Une base de graphe stocke des entités (nœuds) et des relations (arêtes) et répond à des parcours : trouver les chemins, les voisinages, les motifs.
- [[Comparatif - Bases graphes]] · comparatif · `Bases de données/Bases de graphes/Comparatif - Bases graphes.md` — le graphe tient-il sur un nœud, à quel prix d'exploitation, et sous quelle licence.

## Recherche
- [[Apache Solr]] · brique · `Bases de données/Recherche/Apache Solr.md` — Plateforme de recherche Apache (Apache-2.0) bâtie sur Lucene — full-text, vectoriel et géospatial, distribuée par SolrCloud (réplication, bascule automatique).
- [[bm25s]] · brique · `Bases de données/Recherche/bm25s.md` — Implémentation BM25 ultra-rapide en Python (matrices creuses SciPy) — scores pré-calculés à l'indexation, requêtes en millisecondes, des ordres de grandeur…
- [[Elasticsearch]] · brique · `Bases de données/Recherche/Elasticsearch.md` — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.
- [[Lucene]] · brique · `Bases de données/Recherche/Lucene.md` — Bibliothèque Java de recherche plein texte (Apache-2.0) — le moteur d'indexation sous Elasticsearch et Solr ; index inversé et HNSW natifs, à embarquer dans…
- [[Marqo]] · brique · `Bases de données/Recherche/Marqo.md` — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source…
- [[Meilisearch]] · brique · `Bases de données/Recherche/Meilisearch.md` — Moteur de recherche instantané en Rust — full-text tolérant aux fautes de frappe, sémantique et hybride derrière une API REST ; édition communautaire MIT…
- [[OpenSearch]] · brique · `Bases de données/Recherche/OpenSearch.md` — Moteur de recherche et d'analytique distribué (Apache-2.0) — fork d'Elasticsearch 7.10.2 : full-text, k-NN et recherche hybride, visualisé dans OpenSearch…
- [[rank-bm25]] · brique · `Bases de données/Recherche/rank-bm25.md` — Implémentation Python pure des algorithmes BM25 (Okapi, BM25L, BM25+) pour le classement lexical de documents — minimale, sans index ni dépendance, idéale pour…
- [[txtai]] · brique · `Bases de données/Recherche/txtai.md` — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du…
- [[Typesense]] · brique · `Bases de données/Recherche/Typesense.md` — Moteur de recherche tolérant aux fautes de frappe (GPL-3.0, C++) — index en mémoire pour du search-as-you-type sous 50 ms, avec recherche vectorielle HNSW et…
- [[Vespa]] · brique · `Bases de données/Recherche/Vespa.md` — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à…
- [[Index inversé]] · notion · `Bases de données/Recherche/Index inversé.md` — Structure de données qui associe chaque terme à la liste des documents qui le contiennent.
- [[Recherche sémantique]] · notion · `Bases de données/Recherche/Recherche sémantique.md` — Retrouver des documents par le sens de la requête, non par les mots exacts qu'elle contient.
- [[Recherche vectorielle approximative]] · notion · `Bases de données/Recherche/Recherche vectorielle approximative.md` — Retrouver, dans un moteur de recherche, les $k$ documents dont le vecteur est le plus proche de celui de la requête, en échangeant un peu de rappel contre…
- [[Comparatif - Moteurs de recherche]] · comparatif · `Bases de données/Recherche/Comparatif - Moteurs de recherche.md` — bibliothèque ou moteur déployé, lexical ou sémantique, le ranking dans le serving ou après, et la licence — Apache-2.0, MIT ou copyleft réseau.

## Relationnel
- [[CockroachDB]] · brique · `Bases de données/Relationnel/CockroachDB.md` — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[MariaDB]] · brique · `Bases de données/Relationnel/MariaDB.md` — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[Microsoft SQL Server]] · brique · `Bases de données/Relationnel/Microsoft SQL Server.md` — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.
- [[MySQL]] · brique · `Bases de données/Relationnel/MySQL.md` — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[Postgres]] · brique · `Bases de données/Relationnel/Postgres.md` — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[SQLite]] · brique · `Bases de données/Relationnel/SQLite.md` — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[Comparatif - Bases relationnelles]] · comparatif · `Bases de données/Relationnel/Comparatif - Bases relationnelles.md` — serveur ou fichier embarqué, un nœud ou plusieurs, licence et écosystème.

## Vectoriel
- [[Annoy]] · brique · `Bases de données/Vectoriel/Annoy.md` — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[Chroma]] · brique · `Bases de données/Vectoriel/Chroma.md` — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.
- [[Faiss]] · brique · `Bases de données/Vectoriel/Faiss.md` — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[hnswlib]] · brique · `Bases de données/Vectoriel/hnswlib.md` — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[LanceDB]] · brique · `Bases de données/Vectoriel/LanceDB.md` — Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer.
- [[Milvus]] · brique · `Bases de données/Vectoriel/Milvus.md` — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).
- [[pgvector]] · brique · `Bases de données/Vectoriel/pgvector.md` — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Pinecone]] · brique · `Bases de données/Vectoriel/Pinecone.md` — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.
- [[Qdrant]] · brique · `Bases de données/Vectoriel/Qdrant.md` — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[ScaNN]] · brique · `Bases de données/Vectoriel/ScaNN.md` — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.
- [[Weaviate]] · brique · `Bases de données/Vectoriel/Weaviate.md` — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[Bases de données vectorielles]] · notion · `Bases de données/Vectoriel/Bases de données vectorielles.md` — Stocke des embeddings (vecteurs de flottants) et retrouve les plus proches d'un vecteur requête.
- [[Index ANN — internes]] · notion · `Bases de données/Vectoriel/Index ANN — internes.md` — Comment les index de recherche vectorielle trouvent les plus proches voisins sans comparer la requête à tous les vecteurs : ils échangent un peu de rappel…
- [[Comparatif - Bases vectorielles]] · comparatif · `Bases de données/Vectoriel/Comparatif - Bases vectorielles.md` — serveur ou index embarqué, self-host ou managé, filtrage pendant la recherche, volume.
