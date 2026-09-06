---
role: brique
nom: Chroma
alias: [chromadb, chroma-core]
pitch: "Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG."
categorie: database/vecteur
famille: paquet
licence_type: open-source
maturite: production
langage: Rust
alternatives: ["[[LanceDB]]", "[[Faiss]]", "[[hnswlib]]", "[[Annoy]]", "[[ScaNN]]"]
complements: []
tags: [vector-db, rag, embedded]
url_docs: https://docs.trychroma.com
url_repo: https://github.com/chroma-core/chroma
---

# Chroma

<!-- AUTO:BANDEAU:START -->
> Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Rust | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base vectorielle « batteries incluses » pensée pour le RAG. Là où un index ANN nu ne fournit
que l'algorithme, elle gère **collections, métadonnées, filtrage et persistance** derrière une
API minimale, avec HNSW comme index sous-jacent. Elle s'utilise embarquée dans le process,
comme SQLite, ou en client/serveur — la même API dans les deux cas, ce qui permet de passer de
l'un à l'autre sans réécrire l'appelant. Le cœur est en Rust, les façades en Python et
JavaScript.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Prototype RAG : indexer des documents avec métadonnées et requêter en quelques lignes | Montée en charge : un très gros corpus ou une forte concurrence la mettent en difficulté |
| Petit à moyen volume, du notebook à un service modeste, sans déployer d'infra | Le mode embarqué garde tout en local : pas de partage entre instances sans passer au mode serveur |
| Collections et filtrage par métadonnées sans gérer soi-même un index brut | API en évolution rapide, avec des ruptures déjà survenues entre versions — épingler la version |
| Passage progressif du mode embarqué au mode serveur sans changer d'API | |

## Mise en œuvre

- Installation — `uv add chromadb`
- Point d'entrée — API Python ou JavaScript ; mode embarqué in-process, ou serveur via Docker
- Prérequis — rien en mode embarqué ; l'index ANN sous-jacent est un HNSW ; comme pour tout magasin de vecteurs, la métrique de distance et le modèle d'embedding doivent rester cohérents entre l'indexation et la requête
- Exécution — embarquée avec persistance sur disque, ou en serveur ; single-node côté open-source
- Coût — gratuit en self-host (Apache 2.0) ; Chroma Cloud, serverless, payant à l'usage

## Écosystème

### Alternatives

- [[LanceDB]] — Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer.
- [[Faiss]] — Bibliothèque ANN de référence (Meta), index en mémoire CPU/GPU — le moteur derrière beaucoup de vector stores.
- [[hnswlib]] — Implémentation HNSW C++/Python header-only — rapide, minimale, faite pour embarquer l'ANN dans une app.
- [[Annoy]] — Bibliothèque ANN de Spotify, index sur disque mmap — simple et stable, désormais en mode maintenance.
- [[ScaNN]] — Bibliothèque ANN de Google à quantification anisotrope — débit/rappel à l'état de l'art sur gros volumes.

## Ressources

- Documentation — https://docs.trychroma.com
- Dépôt — https://github.com/chroma-core/chroma

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
