---
role: brique
nom: Pinecone
alias: [pinecone]
pitch: "Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire."
categorie: database/vecteur
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: Rust
scaling: serverless
alternatives: ["[[Weaviate]]", "[[Qdrant]]", "[[pgvector]]", "[[Milvus]]"]
complements: []
tags: [vector-db, semantic-search, rag]
url_docs: https://docs.pinecone.io
url_repo: 
---

# Pinecone

## Pourquoi

Base vectorielle entièrement managée, pionnière du secteur. Architecture serverless : les vecteurs vivent sur de l'object storage (S3) découplé du calcul, un pool élastique de processeurs sert les requêtes. Moteur propriétaire en Rust. Aucune infra à provisionner ni opérer — on écrit, on requête, le reste est invisible.

## Quand l'utiliser

- Zéro ops voulu : pas d'instance à dimensionner, pas de cluster à exploiter.
- Scaling automatique du stockage et du débit sans intervention.
- Multi-tenant fort : un namespace isolé par client, haute disponibilité sous SLA.
- Brique managée de bout en bout : Pinecone Inference (embeddings + reranking hébergés), Assistant pour le RAG/agent clé en main.

## Quand NE PAS l'utiliser

- Self-host, souveraineté ou refus de dépendre d'un SaaS → [[Qdrant]], [[Weaviate]] ou [[Milvus]].
- Open-source exigé / contrôle bas niveau de l'index → mêmes alternatives.
- Du Postgres déjà en place et volume modéré → [[pgvector]].
- POC jetable de quelques milliers de vecteurs → un index [[Faiss]] en mémoire suffit.

## Déploiement & coût

- 100 % managé : pas de self-host classique (BYOC en preview fait tourner le data plane dans le cloud du client).
- Serverless multi-cloud (AWS, GCP, Azure) ; facturation à l'usage (stockage + lectures/écritures), pas de nœud à payer à vide.
- Charges de lecture intensives : Dedicated Read Nodes (DRN) pour des performances prévisibles.

## Pièges

- Lock-in propriétaire : pas de dépôt, pas de migration triviale, métrique figée à la création de l'index.
- Coût serverless à surveiller sur gros débit de lecture — modèle à l'usage qui peut surprendre.
- Pas de réglage fin des paramètres d'index (HNSW & co) : la base décide.

## Alternatives

- [[Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Milvus]] — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- Doc : https://docs.pinecone.io
