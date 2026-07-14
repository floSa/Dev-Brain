---
type: moc
nom: Bases de données
galaxie: dev
indexe: database/*
---

# Bases de données

<!-- AUTO:START -->
Briques techniques de la catégorie `database/*`.

- [[Dev/Services/ADBC|ADBC]] — Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement des données Arrow.
- [[Dev/Services/Annoy|Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[Dev/Services/Apache Cassandra|Apache Cassandra]] — Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter.
- [[Dev/Services/Chroma|Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.
- [[Dev/Services/ClickHouse|ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence.
- [[Dev/Services/CockroachDB|CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Dev/Services/DuckDB|DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur.
- [[Dev/Services/Elasticsearch|Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle.
- [[Dev/Services/Faiss|Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[Dev/Services/hnswlib|hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[Dev/Services/InfluxDB|InfluxDB]] — SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles.
- [[Dev/Services/LanceDB|LanceDB]] — Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer.
- [[Dev/Services/MariaDB|MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[Dev/Services/Marqo|Marqo]] — Moteur de recherche vectorielle end-to-end (Apache-2.0) qui gère lui-même l'inférence des embeddings texte et image via une seule API — projet open-source déprécié, pivoté vers une plateforme commerciale de recherche e-commerce.
- [[Dev/Services/Microsoft SQL Server|Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.
- [[Dev/Services/Milvus|Milvus]] — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).
- [[Dev/Services/MongoDB|MongoDB]] — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding.
- [[Dev/Services/MySQL|MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[Dev/Services/Nebula Graph|Nebula Graph]] — Base de graphes distribuée pour jeux de données massifs.
- [[Dev/Services/Neo4j|Neo4j]] — SGBD de graphes natif, leader des données connectées : modèle propriété-graphe et requêtes Cypher.
- [[Dev/Services/pgvector|pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Dev/Services/Pinecone|Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.
- [[Dev/Services/Postgres|Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[Dev/Services/psycopg2|psycopg2]] — Adaptateur PostgreSQL de référence pour Python (LGPL) — implémentation DB-API 2.0 en C au-dessus de libpq, sûre et performante ; figé en fonctionnalités, successeur psycopg 3.
- [[Dev/Services/Qdrant|Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[Dev/Services/Redis|Redis]] — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub.
- [[Dev/Services/ScaNN|ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.
- [[Dev/Services/SQLite|SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[Dev/Services/TimescaleDB|TimescaleDB]] — Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres.
- [[Dev/Services/txtai|txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI.
- [[Dev/Services/Vespa|Vespa]] — Plateforme de recherche et de serving IA (Apache-2.0) — combine full-text, recherche vectorielle et ranking par modèles ML dans un même moteur distribué, à l'échelle du milliard de documents et sous 100 ms.
- [[Dev/Services/Weaviate|Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
<!-- AUTO:END -->

## Notes

