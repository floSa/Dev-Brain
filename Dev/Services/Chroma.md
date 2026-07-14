---
galaxie: dev
type: service
nom: Chroma
alias: [chromadb, chroma-core]
pitch: "Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG."
categorie: database/vector
licence_type: open-source
hosted: both
maturite: production
langage: Rust
scaling: single-node
alternatives: ["[[Dev/Services/LanceDB|LanceDB]]", "[[Dev/Services/Faiss|Faiss]]", "[[Dev/Services/hnswlib|hnswlib]]", "[[Dev/Services/Annoy|Annoy]]", "[[Dev/Services/ScaNN|ScaNN]]"]
remplace_par: []
status: actif
tags: [vector-db, rag, embedded]
url_docs: https://docs.trychroma.com
url_repo: https://github.com/chroma-core/chroma
---

# Chroma

## Pourquoi

Base vectorielle « batteries incluses » pensée pour le RAG. Contrairement aux index ANN nus (Faiss, hnswlib…), elle gère **collections, métadonnées, filtrage et persistance** avec une API minimale. S'utilise embarquée (in-process, comme SQLite) ou en mode client/serveur. Cœur réécrit en Rust, API Python/JS en façade. Open-source (Apache 2.0) ; Chroma Cloud offre une version managée serverless.

## Quand l'utiliser

- Prototype RAG : indexer des documents avec métadonnées et requêter en quelques lignes.
- Petit à moyen volume, du notebook à un service modeste, sans déployer d'infra.
- Besoin de collections + filtrage métadonnées sans gérer soi-même un index brut.
- Passage progressif du mode embarqué au mode serveur sans changer d'API.

## Quand NE PAS l'utiliser

- Gros volumes / haute concurrence / production exigeante → un serveur dédié : [[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/Weaviate|Weaviate]], [[Dev/Services/Milvus|Milvus]].
- Du Postgres déjà en place → [[Dev/Services/pgvector|pgvector]] ; zéro infra managé → [[Dev/Services/Pinecone|Pinecone]].
- Besoin seulement d'un index ANN brut dans un pipeline → [[Dev/Services/Faiss|Faiss]] ou [[Dev/Services/hnswlib|hnswlib]].

## Déploiement & coût

- Self-host gratuit (Apache 2.0) : `pip install chromadb`, mode embarqué (persistance sur disque) ou serveur via Docker.
- Managé : Chroma Cloud, serverless, payant à l'usage.
- Index ANN sous-jacent HNSW ; single-node côté OSS.

## Pièges

- Pensée pour le prototypage : monte mal en charge sur de très gros corpus / forte concurrence.
- Le mode embarqué garde tout local → pas de partage multi-instances sans passer au mode serveur.
- API en évolution rapide : des ruptures ont eu lieu entre versions, épingler la version.
- Cohérence métrique / modèle d'embedding à surveiller comme pour tout vector store.

## Alternatives

- [[Dev/Services/LanceDB|LanceDB]] — Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer.
- [[Dev/Services/Faiss|Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[Dev/Services/hnswlib|hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[Dev/Services/Annoy|Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[Dev/Services/ScaNN|ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- Doc : https://docs.trychroma.com
