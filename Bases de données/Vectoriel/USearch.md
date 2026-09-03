---
role: brique
nom: USearch
alias: [usearch, unum-usearch]
pitch: "Moteur ANN header-only en C++ à métriques définies par l'utilisateur — 10+ bindings de langage, aucune dépendance obligatoire."
categorie: database/vecteur
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[hnswlib]]", "[[Faiss]]", "[[Annoy]]", "[[ScaNN]]"]
complements: []
tags: [vector-db, ann, embedded, in-memory]
url_docs: https://unum-cloud.github.io/USearch/
url_repo: https://github.com/unum-cloud/usearch
---

# USearch

## Pourquoi

Implémentation HNSW en C++11 header-only, de la même famille que [[hnswlib]], avec deux
différences qui décident : les **métriques définies par l'utilisateur** (au lieu d'un jeu fixe)
et l'absence de dépendance obligatoire — ni BLAS, ni OpenMP. Une dizaine de bindings de langage
(Python, Rust, Go, Java, JS, C#, Swift, Objective-C, C99) au lieu d'un ou deux.

## Quand l'utiliser

- Embarquer un index ANN dans une application non-Python : c'est là que le nombre de bindings compte.
- Métrique métier non standard (distance sur mesure, objets arbitraires), impossible à exprimer dans un jeu fixe.
- Contrainte de dépendances ou de taille de paquet : aucune dépendance obligatoire, paquet Python sous 1 Mo.
- Indexation de gros volumes où le temps de construction pèse.

## Quand NE PAS l'utiliser

- Besoin de l'écosystème et des variantes d'index les plus larges (IVF, PQ, GPU) → [[Faiss]].
- Simple HNSW en Python, déjà éprouvé et suffisant → [[hnswlib]].
- Il faut de la persistance, du filtrage par métadonnées et une API : une bibliothèque ne les donne pas → [[Qdrant]] ou [[Milvus]].

## Pièges

- Une métrique définie par l'utilisateur contourne les chemins SIMD optimisés : le gain de flexibilité peut coûter le gain de vitesse.
- Header-only signifie compilation chez l'appelant — la portabilité se paie au build, pas au run.
- Les comparaisons de débit publiées viennent de l'éditeur : à rejouer sur ses propres données avant d'en faire un critère.

## Alternatives

- [[hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.

## Liens

- [[Bases de données vectorielles]] — le concept
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- Doc : https://unum-cloud.github.io/USearch/
