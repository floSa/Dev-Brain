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

## Pourquoi

Base vectorielle distribuée, conçue pour les très gros volumes (milliards de vecteurs). Architecture découplée stockage/calcul, choix large d'index (HNSW, IVF, DiskANN), parallélisme massif. Le poids lourd quand l'échelle dépasse ce qu'un nœud unique encaisse.

## Quand l'utiliser

- Très gros volumes (centaines de millions à milliards de vecteurs).
- Besoin de scaler horizontalement le stockage et le calcul indépendamment.
- Choix fin de l'index selon le compromis mémoire / rappel / latence (DiskANN pour tenir sur disque).
- Équipe prête à opérer une infra distribuée (etcd, object storage, message queue).

## Quand NE PAS l'utiliser

- Volume modéré ou self-host simple → [[Qdrant]] (un binaire, bien plus léger).
- Déléguer l'embedding et le schéma à la base → [[Weaviate]].
- Du Postgres déjà en place → [[pgvector]].

## Déploiement & coût

- Self-host : mode standalone (Docker) pour tester, mode cluster (Kubernetes + etcd + object storage + Pulsar/Kafka) en production.
- Managé : Zilliz Cloud.
- Coût opérationnel non négligeable en cluster : plusieurs composants à exploiter.

## Pièges

- Stack distribuée lourde : ne pas partir en cluster pour un petit volume.
- Cohérence éventuelle (consistency levels) à comprendre selon le cas d'usage.
- Métrique et type d'index figés par collection.

## Alternatives

- [[Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- Doc : https://milvus.io/docs
