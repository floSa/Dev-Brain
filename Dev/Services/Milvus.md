---
galaxie: dev
type: service
nom: Milvus
alias: [milvus]
pitch: "Base vectorielle distribuée costaude, pour gros volumes (multi-index HNSW/IVF/DiskANN)."
categorie: database/vector
licence_type: open-source
hosted: both
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Dev/Services/Weaviate|Weaviate]]", "[[Dev/Services/Qdrant|Qdrant]]", "[[Dev/Services/pgvector|pgvector]]", "[[Dev/Services/Pinecone|Pinecone]]"]
remplace_par: []
status: actif
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

- Volume modéré ou self-host simple → [[Dev/Services/Qdrant|Qdrant]] (un binaire, bien plus léger).
- Déléguer l'embedding et le schéma à la base → [[Dev/Services/Weaviate|Weaviate]].
- Du Postgres déjà en place → [[Dev/Services/pgvector|pgvector]].

## Déploiement & coût

- Self-host : mode standalone (Docker) pour tester, mode cluster (Kubernetes + etcd + object storage + Pulsar/Kafka) en production.
- Managé : Zilliz Cloud.
- Coût opérationnel non négligeable en cluster : plusieurs composants à exploiter.

## Pièges

- Stack distribuée lourde : ne pas partir en cluster pour un petit volume.
- Cohérence éventuelle (consistency levels) à comprendre selon le cas d'usage.
- Métrique et type d'index figés par collection.
- Retours d'expérience détaillés : `Dev/REX/REX - Milvus.md`.

## Alternatives

- [[Dev/Services/Weaviate|Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[Dev/Services/Qdrant|Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[Dev/Services/pgvector|pgvector]] — Extension Postgres qui ajoute le type vector — idéale quand du Postgres est déjà en place.
- [[Dev/Services/Pinecone|Pinecone]] — Base vectorielle 100 % managée et serverless — zéro infra à gérer, scaling automatique, propriétaire.

## Liens

- [[Bases de données vectorielles]] — le concept (Wiki)
- [[Comparatif - Bases vectorielles]] — comparatif des moteurs
- `Dev/REX/REX - Milvus.md` — retours d'expérience
- Doc : https://milvus.io/docs
