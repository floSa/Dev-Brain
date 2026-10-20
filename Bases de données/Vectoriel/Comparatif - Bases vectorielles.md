---
role: comparatif
nom: Comparatif - Bases vectorielles
categorie: database/vecteur
tags: [vector-db]
---

# Comparatif - Bases vectorielles

> On tranche sur : serveur ou index embarqué, self-host ou managé, filtrage pendant la recherche, volume, et ce que l'équipe devra exploiter une fois le RAG en production.

![[Comparatif - Bases vectorielles.base]]

## Ce qui départage

- [[Qdrant]] — le filtrage payload s'applique **pendant** la recherche, pas après.
- [[Weaviate]] — la base produit elle-même les embeddings via ses modules, et fusionne dense + BM25 nativement.
- [[Milvus]] — stockage et calcul découplés, scalables séparément : le seul dimensionné pour le milliard de vecteurs.
- [[Pinecone]] — 100 % managé et propriétaire : aucun paramètre d'index à régler, la base décide.
- [[pgvector]] — pas de service séparé ni de double écriture : ACID et jointures SQL avec les tables métier. Le filtre s'applique **après** le parcours de l'index approximatif : avec HNSW et `hnsw.ef_search` à 40 (défaut), un filtre qui garde 10 % des lignes laisse en moyenne **4 résultats** sur 40 candidats (README) ; parades : scans itératifs, index partiels, partitionnement.
- [[LanceDB]] — embarquée sur le format colonnaire Lance : vecteurs et données multimodales dans la même table, sur stockage objet.
- [[Chroma]] — embarquée elle aussi, mais textuelle : collections, métadonnées et persistance en API minimale, et elle monte mal en charge.
- [[Faiss]] — pas un serveur : index en mémoire in-process, sans métadonnées ni filtrage, mais le plus large choix de familles d'index et le GPU.
- [[hnswlib]] — HNSW nu, header-only, sans dépendance hors C++11, index incrémental.
- [[ScaNN]] — quantification anisotrope pour le produit scalaire (MIPS), au prix d'une optimisation x86/AVX.
- [[Annoy]] — index mmap partageable entre process, mais immuable après `build()` et en mode maintenance.
- **Critère d'exploitation, avant la vitesse.** Choisir une base, c'est choisir ce que l'équipe maintiendra : sauvegarde, mise à jour, reconstruction d'index, supervision, incidents, coût. Une base plus rapide qui retrouve moins souvent les bons documents n'est pas un meilleur choix, et aucune mesure indépendante lue ne classe ces bases sur un même protocole (ANN-Benchmarks mesure des index, sans filtre).
  - Déjà sur PostgreSQL et sans problème mesuré de filtrage, de latence ou de volume : rester sur [[pgvector]], dont la sauvegarde et la reprise sont celles de [[Postgres]]. Déjà sur [[Elasticsearch]] ou [[OpenSearch]] : leur recherche vectorielle native d'abord, même logique.
  - Prototype ou petit volume : [[Chroma]], [[LanceDB]], [[Faiss]] (une bibliothèque, ni métadonnées ni serveur).
  - Équipe sans capacité d'exploitation : le service géré [[Pinecone]], au prix de la dépendance : plus de mode local depuis la fin de vie de Pinecone Local (2026-10-07, notes de version), et un découpage qui pèse sur la facture (100 locataires de 1 Go : 1 unité de lecture par requête avec un espace de noms par locataire, 100 avec un seul espace de noms filtré, exemple de la documentation).
  - Filtres d'accès riches ou nombreux locataires : un serveur dont le filtre entre dans le parcours ([[Qdrant]], [[Weaviate]]) ; très gros volumes : [[Milvus]] distribué, au prix d'un cluster à exploiter.
  - Dans tous les cas, tester sur les **mêmes questions métier**, avec les **vrais filtres d'accès**, sur des données qui évoluent, puis comparer passages utiles retrouvés, latence et coût sous charge. Les droits par document sont traités dans [[Droits d'accès dans un RAG]].

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
