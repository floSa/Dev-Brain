---
galaxie: dev
type: service
nom: pgvector
alias: [pgvector, pg-vector]
pitch: "Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place."
categorie: database/vector
licence_type: open-source
hosted: both
maturite: production
langage: C
scaling: single-node
alternatives: ["[[Dev/Services/Weaviate|Weaviate]]", "[[Dev/Services/Qdrant|Qdrant]]", "[[Dev/Services/Milvus|Milvus]]", "[[Dev/Services/Pinecone|Pinecone]]"]
remplace_par: []
status: actif
tags: [vector-db, rag, postgres]
url_docs: https://github.com/pgvector/pgvector#readme
url_repo: https://github.com/pgvector/pgvector
---

# pgvector

## Pourquoi

Extension Postgres qui ajoute un type `vector` et des opérateurs de similarité (`<->`, `<#>`, `<=>`). Le vector search vit dans Postgres : pas de service séparé, pas de double écriture, transactions ACID et jointures SQL gratuites. Le choix pragmatique quand du Postgres est déjà là.

## Quand l'utiliser

- Postgres déjà présent dans le projet.
- Volume modéré (de l'ordre de quelques dizaines de millions de vecteurs).
- Filtrage relationnel important (jointures SQL avec les autres tables).
- Une seule source de vérité ; cohérence transactionnelle entre données métier et embeddings.

## Quand NE PAS l'utiliser

- Très grande échelle ou très haut débit → [[Dev/Services/Qdrant|Qdrant]].
- Recherche hybride avancée clé en main → [[Dev/Services/Weaviate|Weaviate]].
- Aucun Postgres dans le projet : en installer un juste pour ça est rarement gagnant.

## Déploiement & coût

- Self-host : extension à activer sur une instance Postgres existante (`CREATE EXTENSION vector`).
- Managé : disponible sur la plupart des Postgres managés (RDS, Cloud SQL, Supabase…).
- Pas de coût d'infra supplémentaire ; scaling lié à Postgres (vertical + réplicas lecture).

## Pièges

- Index HNSW (meilleur rappel) vs IVFFlat (construction plus rapide) : choisir selon le besoin.
- `maintenance_work_mem` à augmenter pour la création d'index, sinon très lent.
- Filtrage + ANN : pre-filter exact (lent sur gros volumes) vs post-filter (perte de rappel) — vérifier les plans de requête.
- Retours d'expérience détaillés : `Dev/REX/REX - pgvector.md`.

## Alternatives

- [[Dev/Services/Weaviate|Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[Dev/Services/Qdrant|Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[Dev/Services/Milvus|Milvus]] — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).
- [[Dev/Services/Pinecone|Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- `Dev/REX/REX - pgvector.md` — retours d'expérience
- Doc : https://github.com/pgvector/pgvector#readme
