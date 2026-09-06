---
role: brique
nom: LanceDB
alias: [lancedb, lance]
pitch: "Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer."
categorie: database/vecteur
famille: paquet
licence_type: open-source
maturite: production
langage: Rust
alternatives: ["[[Chroma]]"]
complements: []
tags: [vector-db, embedded, multimodal, columnar]
url_docs: https://lancedb.com/documentation/
url_repo: https://github.com/lancedb/lancedb
---

# LanceDB

<!-- AUTO:BANDEAU:START -->
> Base vectorielle embarquée et multimodale écrite en Rust sur le format colonnaire Lance — du notebook au lakehouse sur stockage objet, sans serveur à gérer.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Rust | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base vectorielle **embarquée** — in-process, comme SQLite — bâtie sur **Lance**, un format de
fichier colonnaire pensé pour l'IA : accès aléatoire rapide, et données profondément imbriquées
(texte, images, vidéo, embeddings) stockées dans une même table. Le cœur est en Rust, les API
en Python, TypeScript et Rust. Les données vivent dans des fichiers Lance posés sur un disque
local ou un stockage objet, sans serveur à exploiter. C'est plus qu'un index : un lakehouse
multimodal, où vecteurs et données brutes se requêtent côte à côte.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| RAG ou recherche multimodale embarqués, du notebook au service, sans déployer d'infra | Format Lance jeune et en évolution rapide : épingler la version et prévoir les migrations de format |
| Données lourdes et imbriquées — images, audio, vidéo et embeddings — à stocker et requêter ensemble | Embarquée : un seul process écrit proprement, il n'y a pas de multi-écrivains concurrents |
| Versionnage des tables et stockage sur S3 ou GCS, stockage et calcul séparés | Performance suspendue à la latence du stockage objet ; sans cache local, les requêtes répétées la paient |
| Feature store ou dataset d'entraînement où l'accès aléatoire rapide compte | |

## Mise en œuvre

- Installation — `uv add lancedb`
- Point d'entrée — API Python, TypeScript ou Rust, en mode embarqué
- Prérequis — un disque local ou un stockage objet (S3, GCS, Azure) ; comme pour tout magasin de vecteurs, la métrique de distance et le modèle d'embedding doivent rester cohérents entre l'indexation et la requête
- Exécution — dans le process appelant ; single-node côté open-source, l'échelle passant par le stockage objet, calcul séparé du stockage. Index IVF-PQ et HNSW
- Coût — gratuit en self-host (Apache 2.0) ; LanceDB Cloud (serverless) et LanceDB Enterprise, payants

## Écosystème

### Alternatives

- [[Chroma]] — Base vectorielle légère et embarquée, du notebook au serveur — l'option la plus simple pour prototyper un RAG.

## Ressources

- Documentation — https://lancedb.com/documentation/
- Dépôt — https://github.com/lancedb/lancedb

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
