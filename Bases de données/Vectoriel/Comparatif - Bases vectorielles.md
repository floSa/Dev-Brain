---
role: comparatif
nom: Comparatif - Bases vectorielles
categorie: database/vecteur
tags: [vector-db]
---

# Comparatif - Bases vectorielles

> On tranche sur : serveur ou index embarqué, self-host ou managé, filtrage pendant la recherche, volume.

![[Comparatif - Bases vectorielles.base]]

## Ce qui départage

- [[Qdrant]] — le filtrage payload s'applique **pendant** la recherche, pas après.
- [[Weaviate]] — la base produit elle-même les embeddings via ses modules, et fusionne dense + BM25 nativement.
- [[Milvus]] — stockage et calcul découplés, scalables séparément : le seul dimensionné pour le milliard de vecteurs.
- [[Pinecone]] — 100 % managé et propriétaire : aucun paramètre d'index à régler, la base décide.
- [[pgvector]] — pas de service séparé ni de double écriture : ACID et jointures SQL avec les tables métier.
- [[LanceDB]] — embarquée sur le format colonnaire Lance : vecteurs et données multimodales dans la même table, sur stockage objet.
- [[Chroma]] — embarquée elle aussi, mais textuelle : collections, métadonnées et persistance en API minimale, et elle monte mal en charge.
- [[Faiss]] — pas un serveur : index en mémoire in-process, sans métadonnées ni filtrage, mais le plus large choix de familles d'index et le GPU.
- [[hnswlib]] — HNSW nu, header-only, sans dépendance hors C++11, index incrémental.
- [[ScaNN]] — quantification anisotrope pour le produit scalaire (MIPS), au prix d'une optimisation x86/AVX.
- [[Annoy]] — index mmap partageable entre process, mais immuable après `build()` et en mode maintenance.
