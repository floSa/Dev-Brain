---
galaxie: dev
type: service
nom: LanceDB
alias: [lancedb, lance]
pitch: "Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer."
categorie: database/vector
licence_type: open-source
hosted: both
maturite: production
langage: Rust
scaling: single-node
alternatives: ["[[Dev/Services/Chroma|Chroma]]"]
remplace_par: []
status: actif
tags: [vector-db, embedded, multimodal, columnar]
url_docs: https://lancedb.com/documentation/
url_repo: https://github.com/lancedb/lancedb
---

# LanceDB

## Pourquoi

Base vectorielle **embarquée** (in-process, comme SQLite) bâtie sur **Lance**, un format de fichier colonnaire pensé pour l'IA : accès aléatoire rapide, stockage de données profondément imbriquées (texte, images, vidéo, embeddings) dans une même table. Cœur en **Rust**, API Python / TypeScript / Rust. Les données vivent dans des fichiers Lance posés sur le **disque local ou un stockage objet** (S3, GCS) — pas de serveur à exploiter. Au-delà du simple index ANN, c'est un **lakehouse multimodal** : on y stocke et requête vecteurs *et* données brutes côte à côte. Open-source (Apache 2.0) ; LanceDB Cloud / Enterprise pour la version managée.

## Quand l'utiliser

- RAG ou recherche multimodale embarqués, du notebook à un service, sans déployer d'infra.
- Données lourdes et imbriquées (images, audio, vidéo + embeddings) à stocker et requêter ensemble.
- Versionnage des tables et stockage sur S3/GCS, séparation stockage/compute « sans serveur ».
- Feature store / dataset d'entraînement où l'accès aléatoire rapide compte.

## Quand NE PAS l'utiliser

- Très gros volumes, haute concurrence, exploitation distribuée → [[Dev/Services/Milvus|Milvus]] ou [[Dev/Services/Qdrant|Qdrant]] (serveurs dédiés).
- Du Postgres déjà en place et besoin modeste → [[Dev/Services/pgvector|pgvector]] ; zéro infra 100 % managé → [[Dev/Services/Pinecone|Pinecone]].
- Simple prototype RAG textuel sans dimension multimodale → [[Dev/Services/Chroma|Chroma]] suffit ; juste un index ANN brut → [[Dev/Services/Faiss|Faiss]].

## Déploiement & coût

- Self-host gratuit (Apache 2.0) : `pip install lancedb`, mode embarqué, données en fichiers Lance sur disque ou stockage objet (S3/GCS/Azure).
- Managé : LanceDB Cloud (serverless) et LanceDB Enterprise, payants.
- Index ANN : IVF-PQ et HNSW ; single-node côté OSS, l'échelle passe par le stockage objet (compute séparé du stockage).

## Pièges

- Format Lance jeune et en évolution rapide : épingler la version, prévoir les migrations de format.
- Embarqué : pas de partage concurrent multi-écrivains comme un serveur — un seul process écrit proprement.
- Performance liée à la latence du stockage objet (S3) ; un cache local change tout sur les requêtes répétées.
- Métrique de distance et modèle d'embedding à garder cohérents, comme pour tout vector store.

## Alternatives

- [[Dev/Services/Chroma|Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- Doc : https://lancedb.com/documentation/
