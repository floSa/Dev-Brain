---
role: brique
nom: Milvus
alias: [milvus]
pitch: "Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN)."
categorie: database/vecteur
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Weaviate]]", "[[Qdrant]]", "[[pgvector]]", "[[Pinecone]]"]
complements: []
tags: [vector-db, rag, ann]
url_docs: https://milvus.io/docs
url_repo: https://github.com/milvus-io/milvus
---

# Milvus

<!-- AUTO:BANDEAU:START -->
> Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Go | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base vectorielle distribuée, conçue pour les très gros volumes — jusqu'au milliard de
vecteurs. Son architecture découple le stockage du calcul, qui se dimensionnent alors
séparément, et elle offre un choix large d'index : HNSW, IVF, DiskANN pour tenir sur disque.
En contrepartie, elle expose des **niveaux de cohérence** qu'il faut comprendre avant de
choisir, parce qu'ils décident de ce qu'une lecture voit d'une écriture récente.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Très gros volumes, de la centaine de millions au milliard de vecteurs | Stack distribuée lourde — etcd, stockage objet, file de messages : hors de proportion pour un petit volume |
| Scaler horizontalement le stockage et le calcul indépendamment | Métrique et type d'index figés par collection |
| Choix fin de l'index selon le compromis mémoire / rappel / latence (DiskANN pour tenir sur disque) | Coût opérationnel réel en cluster : plusieurs composants à exploiter, pas un binaire |
| Équipe prête à exploiter une infrastructure distribuée | |

## Mise en œuvre

- Installation — mode standalone via Docker pour tester ; mode cluster sur Kubernetes en production
- Point d'entrée — service interrogé depuis un client ; le type d'index se choisit à la création de la collection
- Prérequis — en cluster : etcd, un stockage objet et Pulsar ou Kafka
- Exécution — self-hébergé (standalone ou cluster) ou managé sur Zilliz Cloud ; distribué
- Coût — gratuit en self-host ; Zilliz Cloud payant ; en cluster, le coût réel est opérationnel

## Écosystème

### Alternatives

- [[Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.

## Ressources

- Documentation — https://milvus.io/docs
- Dépôt — https://github.com/milvus-io/milvus

## Voir aussi

- [[Bases de données vectorielles]] — la notion du dossier
- [[Comparatif - Bases vectorielles]] — ce qui départage les moteurs du dossier
