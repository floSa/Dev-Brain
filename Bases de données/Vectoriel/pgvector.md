---
role: brique
nom: pgvector
alias: [pgvector, pg-vector]
pitch: "Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place."
categorie: database/vecteur
famille: extension
licence_type: open-source
maturite: production
langage: C
alternatives: ["[[Weaviate]]", "[[Qdrant]]", "[[Milvus]]", "[[Pinecone]]"]
complements: ["[[Postgres]]", "[[LibreChat]]", "[[Mem0]]", "[[Cognee]]"]
tags: [vector-db, rag, postgres]
url_docs: https://github.com/pgvector/pgvector#readme
url_repo: https://github.com/pgvector/pgvector
---

# pgvector

<!-- AUTO:BANDEAU:START -->
> Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Extension C | open-source | dans le moteur hôte, rien à héberger | production | à jour · 2026-07-29 |
<!-- AUTO:BANDEAU:END -->

## Définition

Extension qui ajoute à Postgres un type `vector` et ses opérateurs de similarité (`<->`,
`<#>`, `<=>`). La recherche vectorielle vit alors dans la base métier : une seule source de
vérité, des transactions ACID et des jointures SQL avec les tables existantes. Deux index sont
disponibles et ne servent pas le même besoin — HNSW donne le meilleur rappel, IVFFlat se
construit plus vite.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Du Postgres est déjà présent dans le projet | Aucun Postgres dans le projet : en installer un pour cela seul est rarement gagnant |
| Volume modéré, de l'ordre de quelques dizaines de millions de vecteurs | `maintenance_work_mem` à relever pour la création d'index, sinon elle est très lente |
| Filtrage relationnel important : jointures SQL avec les autres tables | Filtrage combiné à l'ANN : le pre-filter exact est lent sur gros volumes, le post-filter coûte du rappel — les plans de requête sont à vérifier |
| Une seule source de vérité, cohérence transactionnelle entre données métier et embeddings | |

## Mise en œuvre

- Installation — `CREATE EXTENSION vector` sur une instance Postgres existante
- Point d'entrée — SQL : le type `vector` et les opérateurs `<->`, `<#>`, `<=>`
- Prérequis — un Postgres en place, et `maintenance_work_mem` relevé le temps de créer l'index
- Exécution — dans le moteur Postgres hôte ; disponible sur la plupart des Postgres managés (RDS, Cloud SQL, Supabase)
- Coût — aucun coût d'infrastructure supplémentaire ; le dimensionnement est celui de Postgres, vertical et réplicas de lecture

## Écosystème

### Alternatives

- [[Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[Milvus]] — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).
- [[Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.

### Compléments

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — le moteur hôte, dont l'extension étend le type système
- [[LibreChat]] — Interface de chat auto-hébergée multi-fournisseurs (MIT, rachetée par ClickHouse en novembre 2025) — agents avec MCP et interpréteur de code, artefacts, RAG par service dédié, SSO OIDC, SAML et LDAP, panneau d'administration ; exige MongoDB.
- [[Mem0]] — Couche de mémoire pour agents LLM (Apache-2.0, open-core) — un LLM extrait les faits d'une conversation, rangés par utilisateur, agent ou session dans un vector store, puis retrouvés par recherche ; la mémoire graphe, les webhooks et l'export sont réservés à la plateforme hébergée.
- [[Cognee]] — Moteur de mémoire pour agents (Topoteretes, Apache-2.0) — ingère documents et conversations, en tire un graphe de connaissances et un index vectoriel, puis les interroge ; pile locale SQLite, LanceDB et Kuzu par défaut, accès par jeu de données avec rôles ; version 1.x classée beta.

## Ressources

- Documentation — https://github.com/pgvector/pgvector#readme

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
