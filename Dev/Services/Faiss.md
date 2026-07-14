---
galaxie: dev
type: service
nom: Faiss
alias: [faiss, faiss-cpu, faiss-gpu]
pitch: "Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores."
categorie: database/vector
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Dev/Services/hnswlib|hnswlib]]", "[[Dev/Services/Annoy|Annoy]]", "[[Dev/Services/ScaNN|ScaNN]]", "[[Dev/Services/Chroma|Chroma]]"]
remplace_par: []
status: actif
tags: [vector-db, ann, embedded, in-memory]
url_docs: https://faiss.ai
url_repo: https://github.com/facebookresearch/faiss
---

# Faiss

## Pourquoi

Bibliothèque C++ (bindings Python) de Meta FAIR pour la recherche de similarité et le clustering de vecteurs denses. Pas un serveur : un **index en mémoire** que l'on appelle in-process. Référence du domaine — beaucoup de vector stores l'utilisent en interne. Licence MIT, support GPU (CUDA / ROCm) optionnel.

## Quand l'utiliser

- Recherche ANN à fort volume où la latence et le rappel se règlent finement (IVF, PQ, HNSW, OPQ…).
- Pipeline ML/recherche où l'index vit déjà dans le process Python, sans base externe.
- Besoin de GPU pour indexer/chercher des dizaines de millions de vecteurs.
- Brique bas niveau d'un moteur maison (on gère soi-même persistance et métadonnées).

## Quand NE PAS l'utiliser

- Besoin de persistance, filtrage métadonnées, CRUD, API ou multi-tenant → un serveur : [[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/Weaviate|Weaviate]], [[Dev/Services/Milvus|Milvus]].
- Du Postgres déjà en place → [[Dev/Services/pgvector|pgvector]].
- Zéro infra à gérer → [[Dev/Services/Pinecone|Pinecone]].
- Prototype RAG clé en main (collections + métadonnées sans code) → [[Dev/Services/Chroma|Chroma]].

## Déploiement & coût

- Gratuit, open-source (MIT). `pip install faiss-cpu` ou `faiss-gpu`.
- Tourne dans le process : pas de serveur, pas de réseau. Persistance = sérialiser l'index sur disque soi-même.
- GPU optionnel pour un gain massif sur gros volumes.

## Pièges

- Choix du type d'index non trivial : `IndexFlat` (exact, lent), `IVF` (rapide, à entraîner), `PQ` (compresse, perd du rappel). Mauvais choix = rappel ou latence catastrophiques.
- Les index IVF/PQ demandent un `train()` sur un échantillon représentatif avant d'ajouter.
- Pas de gestion des métadonnées ni de filtrage : à la charge de l'application.
- Suppressions / mises à jour limitées selon le type d'index.

## Alternatives

- [[Dev/Services/hnswlib|hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[Dev/Services/Annoy|Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[Dev/Services/ScaNN|ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.
- [[Dev/Services/Chroma|Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Index ANN — internes]] — internes des index (HNSW, IVF, PQ) que cette lib implémente.
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- Doc : https://faiss.ai
