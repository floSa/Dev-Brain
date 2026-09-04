---
role: brique
nom: Qdrant
alias: [qdrant]
pitch: "Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple."
categorie: database/vecteur
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Rust
scaling: distributed
alternatives: ["[[Weaviate]]", "[[pgvector]]", "[[Milvus]]", "[[Pinecone]]"]
complements: []
tags: [vector-db, rag, ann]
url_docs: https://qdrant.tech/documentation/
url_repo: https://github.com/qdrant/qdrant
---

# Qdrant

<!-- AUTO:BANDEAU:START -->
> Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Rust | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base vectorielle écrite en Rust, servie derrière une API REST et gRPC. Elle stocke les
vecteurs avec un *payload* — les métadonnées arbitraires attachées à chaque point — et sait
appliquer un filtre sur ce payload pendant le parcours de l'index, pas après coup sur le
résultat. Les réglages HNSW (`m`, `ef_construct`, `ef`) sont exposés et se règlent selon le
compromis rappel / latence visé ; la quantification scalaire ou binaire réduit la RAM
consommée par l'index. C'est un service à exploiter : il tourne, il se dimensionne, il se
sauvegarde.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| RAG ou recherche sémantique en production, self-hébergée | La métrique de distance est figée à la création de la collection (Cosine, Dot, Euclidean) et le changement est irréversible |
| Filtrage métier critique combiné à la recherche vectorielle (« docs de ce client, score > 0.8 ») | La quantification binaire fait gagner de la mémoire, mais peut coûter du rappel sur de petits embeddings |
| Garder la production des embeddings et la logique métier côté application | Aucun module d'embedding : les vecteurs arrivent déjà calculés, c'est à l'application de les produire |
| Recherche hybride dense + sparse, avec contrôle fin des paramètres HNSW | |

## Mise en œuvre

- Installation — binaire unique, ou image Docker
- Point d'entrée — API REST ou gRPC ; gRPC est le plus rapide des deux
- Prérequis — RAM dimensionnée sur l'index HNSW ; la quantification est le levier pour la réduire
- Exécution — self-hébergé ou managé (Qdrant Cloud) ; le mode distribué, sharding et réplication compris, est dans l'open-source
- Coût — gratuit en self-host ; Qdrant Cloud est payant, et le cluster managé l'est aussi

## Écosystème

### Alternatives

- [[Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Milvus]] — Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).
- [[Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.

## Ressources

- Documentation — https://qdrant.tech/documentation/
- Dépôt — https://github.com/qdrant/qdrant

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Index ANN — internes]] — les réglages HNSW que cette base expose
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
