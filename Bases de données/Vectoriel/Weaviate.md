---
role: brique
nom: Weaviate
alias: [weaviate]
pitch: "Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé."
categorie: database/vecteur
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Qdrant]]", "[[pgvector]]", "[[Milvus]]", "[[Pinecone]]"]
complements: []
tags: [vector-db, rag, hybrid-search]
url_docs: https://weaviate.io/developers/weaviate
url_repo: https://github.com/weaviate/weaviate
---

# Weaviate

<!-- AUTO:BANDEAU:START -->
> Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Go | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base vectorielle écrite en Go, taillée pour un usage exploité au long cours. Elle embarque des
**modules de vectorisation** : la base produit elle-même les embeddings, au lieu de les
recevoir tout faits. La recherche hybride dense + BM25 est native, avec fusion des scores, et
la multi-tenancy est de première classe — un namespace isolé par client. En contrepartie, le
modèle est explicite : classes, propriétés et vectorizer se déclarent avant d'écrire.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Multi-tenancy forte : un namespace isolé par client | Schéma à définir (classes, propriétés, vectorizer), et changer de vectorizer impose une recréation |
| Déléguer l'embedding à la base via ses modules, plutôt que le gérer côté application | Ruptures entre versions majeures : lire les changelogs avant toute montée de version |
| Recherche hybride, sémantique et mots-clés, avec fusion de scores | |
| Managé clé en main, ou self-host qui scale horizontalement | |

## Mise en œuvre

- Installation — Docker, ou Kubernetes pour le mode distribué
- Point d'entrée — le service ; le schéma se déclare avant la première écriture
- Prérequis — RAM dimensionnée sur l'index HNSW ; la quantification réduit l'empreinte
- Exécution — self-hébergé avec sharding et réplication, ou managé sur Weaviate Cloud (serverless ou cluster dédié)
- Coût — gratuit en self-host, le coût réel étant celui de la RAM ; Weaviate Cloud facturé à l'usage

## Écosystème

### Alternatives

- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Milvus]] — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).
- [[Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.

## Ressources

- Documentation — https://weaviate.io/developers/weaviate

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
