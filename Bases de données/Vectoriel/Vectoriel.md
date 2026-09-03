---
role: hub
nom: Vectoriel
pitch: Stocker des embeddings et retrouver les plus proches voisins par recherche approchée (ANN).
domaines: [data-eng, ai-eng]
---

# Vectoriel

> Stocker des embeddings et retrouver les plus proches voisins par recherche approchée (ANN).

## Ce qu'il faut comprendre

- Une base vectorielle indexe des **embeddings** et répond « les $k$ plus proches » au lieu de « les lignes qui valent X ». La recherche est **approchée** : on échange un peu de rappel contre des ordres de grandeur de vitesse.
- Deux natures de briques cohabitent ici, et on les confond souvent. Une **bibliothèque d'index** ([[Faiss]], [[hnswlib]], [[Annoy]], [[ScaNN]]) fournit l'algorithme et rien d'autre : ni persistance, ni filtrage, ni API. Une **base** ([[Qdrant]], [[Milvus]], [[Weaviate]], [[Chroma]], [[LanceDB]], [[Pinecone]]) ajoute le stockage, les métadonnées et le service.
- Le **filtrage par métadonnées** est le vrai discriminant en production : filtrer *pendant* la recherche ou *après* ne donne pas les mêmes résultats à $k$ fixé.
- Deux notions tiennent la théorie du dossier, à deux étages. [[Bases de données vectorielles]] décrit ce qu'un moteur fait — embeddings, ANN, filtrage, métadonnées ; [[Index ANN — internes]] décrit ce qui tourne dessous — HNSW, IVF, PQ et leurs réglages. Lire la première pour choisir une brique, la seconde pour régler celle qu'on a choisie.

## Choisir

- Du Postgres déjà en place → [[pgvector]], et la question est réglée : une extension, pas une base de plus à exploiter.
- Prototype ou notebook → [[Chroma]] ou [[LanceDB]], embarqués, rien à héberger.
- Production self-hébergée avec filtrage exigeant → [[Qdrant]]. Gros volumes distribués → [[Milvus]]. Recherche hybride dense + BM25 → [[Weaviate]].
- Zéro infra à gérer, budget disponible → [[Pinecone]], managé et propriétaire.
- Besoin de l'index seul, à embarquer dans une application → [[Faiss]] ou [[hnswlib]].

<!-- AUTO:START -->
### Notions
- [[Bases de données vectorielles]] — domaines : data-eng, ai-eng
- [[Index ANN — internes]] — domaines : data-eng, ai-eng

### Briques
- [[Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.
- [[Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[LanceDB]] — Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer.
- [[Milvus]] — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).
- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.
- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.
- [[Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.

### Comparatifs
- [[Comparatif - Bases vectorielles]]
<!-- AUTO:END -->
