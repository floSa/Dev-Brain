---
galaxie: dev
type: service
nom: hnswlib
alias: [hnsw, nmslib-hnswlib]
pitch: "Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app."
categorie: database/vector
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Dev/Services/Faiss|Faiss]]", "[[Dev/Services/Annoy|Annoy]]", "[[Dev/Services/ScaNN|ScaNN]]", "[[Dev/Services/Chroma|Chroma]]"]
remplace_par: []
status: actif
tags: [vector-db, ann, embedded, in-memory]
url_docs: https://pypi.org/project/hnswlib/
url_repo: https://github.com/nmslib/hnswlib
---

# hnswlib

## Pourquoi

Implémentation header-only en C++ (bindings Python, R) de l'algorithme **HNSW** (graphe navigable hiérarchique), issue de nmslib. Aucune dépendance hors C++11. Construction incrémentale, suppression d'éléments, faible empreinte mémoire. Licence Apache 2.0. C'est le HNSW « nu » que plusieurs moteurs ont embarqué.

## Quand l'utiliser

- Recherche ANN purement HNSW, rapide à intégrer et sans dépendances lourdes.
- Index incrémental (ajouts au fil de l'eau) directement en mémoire.
- Embarquer l'ANN dans une app C++ ou Python sans tirer une lib massive.
- Cas où HNSW suffit et où l'on veut contrôler `M`, `ef_construction`, `ef`.

## Quand NE PAS l'utiliser

- Besoin de persistance robuste, filtrage métadonnées, CRUD, API ou scaling → un serveur : [[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/Weaviate|Weaviate]], [[Dev/Services/Milvus|Milvus]].
- Du Postgres déjà en place → [[Dev/Services/pgvector|pgvector]].
- Besoin de plusieurs familles d'index (IVF, PQ, GPU) → [[Dev/Services/Faiss|Faiss]].
- Prototype RAG clé en main → [[Dev/Services/Chroma|Chroma]].

## Déploiement & coût

- Gratuit, open-source (Apache 2.0). `pip install hnswlib`.
- In-process, single-node. Persistance via `save_index` / `load_index`.
- Pas de GPU : CPU uniquement.

## Pièges

- Taille maximale de l'index fixée à l'initialisation (`max_elements`) ; dépassement → `resize_index` explicite.
- `ef` à la requête arbitre rappel vs latence ; trop bas = rappel qui chute silencieusement.
- Pas de filtrage métadonnées natif riche (filtre par callback seulement) ni de stockage des payloads.
- HNSW = forte consommation RAM (le graphe entier en mémoire).

## Alternatives

- [[Dev/Services/Faiss|Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[Dev/Services/Annoy|Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[Dev/Services/ScaNN|ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.
- [[Dev/Services/Chroma|Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Index ANN — internes]] — internes de l'index HNSW (réglages `M`, `ef`).
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- Doc : https://pypi.org/project/hnswlib/
