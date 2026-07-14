---
galaxie: dev
type: service
nom: Qdrant
alias: [qdrant]
pitch: "Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple."
categorie: database/vector
licence_type: open-source
hosted: both
maturite: production
langage: Rust
scaling: distributed
alternatives: ["[[Dev/Services/Weaviate|Weaviate]]", "[[Dev/Services/pgvector|pgvector]]", "[[Dev/Services/Milvus|Milvus]]", "[[Dev/Services/Pinecone|Pinecone]]"]
remplace_par: []
status: actif
tags: [vector-db, rag, ann]
url_docs: https://qdrant.tech/documentation/
url_repo: https://github.com/qdrant/qdrant
---

# Qdrant

## Pourquoi

Base vectorielle écrite en Rust. Performances élevées, **filtrage payload** puissant (filtres appliqués pendant la recherche, pas après), quantification scalaire/binaire. Le défaut moderne pour un vector store self-hosted sérieux.

## Quand l'utiliser

- RAG / recherche sémantique en production, self-hosted.
- Filtrage métier critique combiné au vector search (« docs de ce client uniquement, score > 0.8 »).
- Garder l'embedding et la logique côté application.
- Hybrid search dense + sparse, avec contrôle fin des paramètres HNSW.

## Quand NE PAS l'utiliser

- Déléguer l'embedding et le schéma à la base → [[Dev/Services/Weaviate|Weaviate]].
- Du Postgres déjà en place et besoin modeste → [[Dev/Services/pgvector|pgvector]].
- POC en RAM dans un script → un index [[Dev/Services/Faiss|Faiss]] direct suffit.

## Déploiement & coût

- Self-host : binaire unique ou Docker ; mode distribué (sharding + réplication) en open-source.
- Managé : Qdrant Cloud ; le mode cluster managé est payant.
- gRPC plus rapide que REST ; quantification pour réduire la RAM.

## Pièges

- Métrique de distance figée à la création de la collection (Cosine / Dot / Euclidean), irréversible.
- Paramètres HNSW (`m`, `ef_construct`, `ef`) à régler selon le compromis rappel / latence.
- Quantification binaire : gain mémoire réel, mais perte de rappel possible sur petits embeddings.
- Retours d'expérience détaillés : `Dev/REX/REX - Qdrant.md`.

## Alternatives

- [[Dev/Services/Weaviate|Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[Dev/Services/pgvector|pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Dev/Services/Milvus|Milvus]] — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).
- [[Dev/Services/Pinecone|Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- `Dev/REX/REX - Qdrant.md` — retours d'expérience
- Doc : https://qdrant.tech/documentation/
