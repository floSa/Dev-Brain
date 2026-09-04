---
role: brique
nom: Pinecone
alias: [pinecone]
pitch: "Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire."
categorie: database/vecteur
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
langage: Rust
scaling: serverless
alternatives: ["[[Weaviate]]", "[[Qdrant]]", "[[pgvector]]", "[[Milvus]]"]
complements: []
tags: [vector-db, semantic-search, rag]
url_docs: https://docs.pinecone.io
url_repo: 
---

# Pinecone

<!-- AUTO:BANDEAU:START -->
> Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base vectorielle pionnière du secteur, servie comme un service et rien d'autre. L'architecture
est serverless : les vecteurs vivent sur du stockage objet, découplé du calcul, et un pool
élastique de processeurs sert les requêtes. Autour du magasin de vecteurs, l'éditeur fournit
Pinecone Inference — embeddings et reranking hébergés — et Assistant, un RAG clé en main. On
écrit, on requête ; tout le reste est invisible, y compris les réglages.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Zéro ops voulu : ni instance à dimensionner, ni cluster à exploiter | Aucun paramètre d'index exposé : impossible d'arbitrer soi-même rappel contre latence |
| Scaling automatique du stockage et du débit, sans intervention | Enfermement : pas de dépôt, pas de migration triviale, et la métrique est figée à la création de l'index |
| Multi-tenant fort : un namespace isolé par client, haute disponibilité sous SLA | Facturation à l'usage : un gros débit de lecture peut surprendre |
| Chaîne managée de bout en bout — Inference pour les embeddings et le reranking, Assistant pour le RAG | |

## Mise en œuvre

- Installation — rien à installer : le service est provisionné côté éditeur
- Point d'entrée — le service, appelé depuis un client ; l'index se crée côté éditeur, métrique comprise
- Prérequis — un des clouds servis : AWS, GCP ou Azure
- Exécution — 100 % managé ; pas de self-host classique, le BYOC en préversion faisant tourner le data plane dans le cloud du client
- Coût — à l'usage (stockage, lectures et écritures), aucun nœud payé à vide ; Dedicated Read Nodes pour un débit de lecture prévisible

## Écosystème

### Alternatives

- [[Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Milvus]] — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).

## Ressources

- Documentation — https://docs.pinecone.io

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
