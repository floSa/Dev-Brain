---
galaxie: dev
type: service
nom: Weaviate
alias: [weaviate]
pitch: "Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé."
categorie: database/vector
licence_type: open-source
hosted: both
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Dev/Services/Qdrant|Qdrant]]", "[[Dev/Services/pgvector|pgvector]]", "[[Dev/Services/Milvus|Milvus]]", "[[Dev/Services/Pinecone|Pinecone]]"]
remplace_par: []
status: actif
tags: [vector-db, rag, hybrid-search]
url_docs: https://weaviate.io/developers/weaviate
url_repo: https://github.com/weaviate/weaviate
---

# Weaviate

## Pourquoi

Base vectorielle open-source en Go, pensée pour la production. Modules de vectorisation intégrés (la base peut produire elle-même les embeddings), recherche hybride dense+BM25 native, multi-tenancy de première classe.

## Quand l'utiliser

- Multi-tenancy fort : un namespace isolé par client.
- Déléguer l'embedding à la base via ses modules, plutôt que le gérer côté application.
- Recherche hybride (sémantique + mots-clés) avec fusion de scores.
- Besoin d'un managé clé en main (Weaviate Cloud) ou d'un self-host qui scale horizontalement.

## Quand NE PAS l'utiliser

- Tout contrôler côté application (embedding maison, schéma minimal) → [[Dev/Services/Qdrant|Qdrant]].
- Du Postgres déjà en place et volume modéré → [[Dev/Services/pgvector|pgvector]].
- POC jetable de quelques milliers de vecteurs → un index [[Dev/Services/Faiss|Faiss]] en mémoire suffit.

## Déploiement & coût

- Self-host : Docker / Kubernetes ; scaling distribué (sharding + réplication).
- Managé : Weaviate Cloud (serverless ou cluster dédié), facturation à l'usage.
- Coût dominé par la RAM de l'index HNSW ; la quantification réduit l'empreinte.

## Pièges

- Schéma à définir (classes, properties, vectorizer) ; changer de vectorizer impose une recréation.
- Breaking changes entre versions majeures — lire les changelogs avant montée de version.
- Retours d'expérience détaillés : `Dev/REX/REX - Weaviate.md`.

## Alternatives

- [[Dev/Services/Qdrant|Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[Dev/Services/pgvector|pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Dev/Services/Milvus|Milvus]] — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).
- [[Dev/Services/Pinecone|Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- `Dev/REX/REX - Weaviate.md` — retours d'expérience
- Doc : https://weaviate.io/developers/weaviate
