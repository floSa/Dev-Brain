---
role: brique
nom: ScaNN
alias: [scann, scalable-nearest-neighbors]
pitch: "Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes."
categorie: database/vecteur
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[Faiss]]", "[[hnswlib]]", "[[Annoy]]", "[[Chroma]]"]
complements: []
tags: [vector-db, ann, embedded, in-memory]
url_docs: https://github.com/google-research/google-research/blob/master/scann/README.md
url_repo: https://github.com/google-research/google-research/tree/master/scann
---

# ScaNN

<!-- AUTO:BANDEAU:START -->
> Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | à jour · 2025-08-29 |
<!-- AUTO:BANDEAU:END -->

## Définition

*Scalable Nearest Neighbors*, de Google Research : une bibliothèque C++ avec une API Python et
une opération TensorFlow optionnelle. Son apport est la **quantification anisotrope**, qui
préserve les composantes parallèles des vecteurs — celles qui pèsent dans le produit scalaire —
et pousse le compromis débit/rappel à l'état de l'art sur le *maximum inner product search*.
Le code est optimisé pour les jeux d'instructions AVX du x86, ce qui explique une bonne part
de ses résultats.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche par produit scalaire (MIPS) sur gros volumes, où le débit à rappel donné prime | Plateforme hors x86 ou sans AVX : gains moindres, voire compilation difficile |
| Pipeline Python ou TensorFlow qui cherche le haut du panier en ANN sur CPU | Construction de l'index plus exigeante à régler — partitionnement et quantification — que HNSW |
| Un bench montre que la quantification anisotrope bat HNSW ou IVF sur le jeu de données | Écosystème restreint : moins de tutoriels et un support communautaire plus mince |
| | Vit dans le monorepo google-research : packaging et cadence moins « produit » qu'une bibliothèque dédiée |

## Mise en œuvre

- Installation — `uv add scann` ; `scann[tf]` pour l'intégration TensorFlow, depuis la 1.4.0
- Point d'entrée — API Python, ou opération TensorFlow optionnelle
- Prérequis — x86 avec AVX ; CPU uniquement
- Exécution — dans le process appelant, single-node ; pas de serveur
- Coût — gratuit, licence Apache 2.0

## Écosystème

### Alternatives

- [[Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

## Ressources

- Documentation — https://github.com/google-research/google-research/blob/master/scann/README.md

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Index ANN — internes]] — les internes des index ANN, dont la quantification anisotrope
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
