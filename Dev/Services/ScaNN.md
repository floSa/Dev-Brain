---
galaxie: dev
type: service
nom: ScaNN
alias: [scann, scalable-nearest-neighbors]
pitch: "Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes."
categorie: database/vector
licence_type: open-source
hosted: self
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Dev/Services/Faiss|Faiss]]", "[[Dev/Services/hnswlib|hnswlib]]", "[[Dev/Services/Annoy|Annoy]]", "[[Dev/Services/Chroma|Chroma]]"]
remplace_par: []
status: actif
tags: [vector-db, ann, embedded, in-memory]
url_docs: https://github.com/google-research/google-research/blob/master/scann/README.md
url_repo: https://github.com/google-research/google-research/tree/master/scann
---

# ScaNN

## Pourquoi

*Scalable Nearest Neighbors* — bibliothèque C++ (API Python, op TensorFlow optionnelle) de Google Research. Sa nouveauté : la **quantification anisotrope**, qui préserve les composantes parallèles des vecteurs (celles qui comptent pour le produit scalaire) et pousse le compromis débit/rappel à l'état de l'art sur du *maximum inner product search*. Open-source (Apache 2.0), optimisée AVX (x86).

## Quand l'utiliser

- Recherche par produit scalaire (MIPS) sur gros volumes où le débit/rappel prime.
- Pipeline Python/TensorFlow recherchant le top de la performance ANN CPU.
- Cas où un bench montre que la quantification anisotrope bat HNSW/IVF.

## Quand NE PAS l'utiliser

- Plateforme non x86 / sans AVX, ou besoin GPU large → [[Dev/Services/Faiss|Faiss]].
- Intégration ultra-simple et incrémentale → [[Dev/Services/hnswlib|hnswlib]].
- Besoin de persistance, filtrage, CRUD, API ou scaling → un serveur : [[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/Weaviate|Weaviate]], [[Dev/Services/Milvus|Milvus]].
- Du Postgres déjà en place → [[Dev/Services/pgvector|pgvector]] ; prototype RAG clé en main → [[Dev/Services/Chroma|Chroma]].

## Déploiement & coût

- Gratuit, open-source (Apache 2.0). `pip install scann` (intégration TensorFlow via `scann[tf]` depuis 1.4.0).
- In-process, single-node, CPU (optimisé AVX). Pas de serveur.

## Pièges

- Construction de l'index plus exigeante à régler (partitionnement + quantification) que HNSW.
- Optimisé x86/AVX : gains moindres voire build difficile hors de cet environnement.
- Écosystème plus restreint que Faiss (moins de tutoriels, support communautaire plus mince).
- Vit dans le monorepo google-research : packaging et cadence moins « produit » qu'une lib dédiée.

## Alternatives

- [[Dev/Services/Faiss|Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[Dev/Services/hnswlib|hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[Dev/Services/Annoy|Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[Dev/Services/Chroma|Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Index ANN — internes]] — internes des index ANN, dont la quantification anisotrope.
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- Doc : https://github.com/google-research/google-research/blob/master/scann/README.md
