---
galaxie: dev
type: service
nom: Annoy
alias: [annoy, approximate-nearest-neighbors-oh-yeah]
pitch: "Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance."
categorie: database/vector
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Dev/Services/hnswlib|hnswlib]]", "[[Dev/Services/Faiss|Faiss]]", "[[Dev/Services/ScaNN|ScaNN]]", "[[Dev/Services/Chroma|Chroma]]"]
remplace_par: []
status: actif
tags: [vector-db, ann, embedded]
url_docs: https://pypi.org/project/annoy/
url_repo: https://github.com/spotify/annoy
---

# Annoy

## Pourquoi

*Approximate Nearest Neighbors Oh Yeah* — bibliothèque C++ (bindings Python) de Spotify, à base de **forêts d'arbres aléatoires**. Particularité : l'index est un fichier **mmap** partageable entre process et chargeable sans tout mettre en RAM. Licence Apache 2.0. A longtemps servi Discover Weekly ; Spotify recommande désormais Voyager (basé sur HNSW) pour les nouveaux usages — Annoy reste maintenu mais figé.

## Quand l'utiliser

- Index **statique** construit une fois puis chargé en lecture seule par plusieurs process (mmap).
- Empreinte mémoire serrée : le fichier sur disque évite de tout charger.
- Besoin simple, dépendances minimales, API très réduite.

## Quand NE PAS l'utiliser

- Nouveau projet cherchant le meilleur débit/rappel → [[Dev/Services/hnswlib|hnswlib]] (base de Voyager) ou [[Dev/Services/ScaNN|ScaNN]].
- Index **mutable** (ajouts/suppressions fréquents) : Annoy fige l'index après `build()`.
- Besoin de persistance riche, filtrage, CRUD, API → un serveur : [[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/Weaviate|Weaviate]], [[Dev/Services/Milvus|Milvus]].
- Prototype RAG clé en main → [[Dev/Services/Chroma|Chroma]].

## Déploiement & coût

- Gratuit, open-source (Apache 2.0). `pip install annoy`.
- In-process, single-node, CPU uniquement. Persistance native via le fichier mmap.

## Pièges

- Index **immuable** : il faut le reconstruire entièrement pour ajouter des vecteurs.
- Précision en retrait par rapport à HNSW/ScaNN à temps égal (état de l'art dépassé).
- Le nombre d'arbres arbitre taille/précision : trop peu = rappel faible.
- Projet en maintenance : ne pas en faire un choix par défaut pour du neuf.

## Alternatives

- [[Dev/Services/hnswlib|hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[Dev/Services/Faiss|Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[Dev/Services/ScaNN|ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.
- [[Dev/Services/Chroma|Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- Doc : https://pypi.org/project/annoy/
