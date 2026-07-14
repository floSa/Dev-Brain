---
galaxie: dev
type: service
nom: Haystack
alias: [haystack, deepset-haystack, farm-haystack]
pitch: "Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/LangChain|LangChain]]", "[[Dev/Services/LlamaIndex|LlamaIndex]]", "[[Dev/Services/DSPy|DSPy]]"]
remplace_par: []
status: actif
tags: [llm, rag, semantic-search, hybrid-search, agents]
url_docs: https://docs.haystack.deepset.ai/
url_repo: https://github.com/deepset-ai/haystack
---

# Haystack

## Pourquoi

Framework d'orchestration LLM de **deepset**, orienté **production**. Son modèle : des **pipelines** explicites où l'on câble des **composants** (retrievers, embedders, rankers, générateurs, routeurs) en un graphe lisible, avec un contrôle fin du flux de la récupération à la génération. Haystack **2.x** est une réécriture complète (composants + pipelines typés) par rapport à la 1.x. Solide sur le **RAG**, la recherche sémantique, la recherche **hybride** (dense + BM25) et, désormais, les **agents**. Écrit en **Python**, licence **Apache-2.0**.

## Quand l'utiliser

- Mettre un **RAG ou une recherche sémantique en production** avec un pipeline explicite, testable et observable.
- Vouloir du **contrôle fin** sur chaque étape (retrieval, reranking, routing, génération) plutôt que des abstractions opaques.
- Recherche **hybride** dense + lexicale, branchée sur Elasticsearch / OpenSearch / une base vectorielle.
- Préférer une licence **Apache-2.0** et un éditeur orienté entreprise (deepset).

## Quand NE PAS l'utiliser

- Prototypage rapide tirant parti du **plus gros catalogue d'intégrations** → [[Dev/Services/LangChain|LangChain]].
- App **centrée données** où l'indexation multi-format prime → [[Dev/Services/LlamaIndex|LlamaIndex]].
- Besoin d'**optimiser automatiquement** les prompts → [[Dev/Services/DSPy|DSPy]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; bibliothèque importée, pipelines sérialisables (YAML) déployables comme service.
- Offre **managée payante** de deepset (deepset AI Platform / Studio) pour construire et opérer les pipelines — optionnelle.
- Coût dominé par les appels LLM, l'embedding et l'infra de la base de recherche/vectorielle.

## Pièges

- **Rupture 1.x → 2.x** : l'ancien `farm-haystack` et la 2.x ont des API incompatibles — vérifier sur quelle version pointe un tutoriel.
- Écosystème d'intégrations **plus restreint** que LangChain : certains connecteurs récents manquent ou sont communautaires.
- Le modèle « pipeline de composants » est puissant mais **plus verbeux** pour un simple appel LLM one-shot.

## Alternatives

- [[Dev/Services/LangChain|LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.
- [[Dev/Services/LlamaIndex|LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- [[Dev/Services/DSPy|DSPy]] — Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques.

## Liens

- Concept : [[RAG]] — et ses techniques [[Chunking strategies]], [[Hybrid retrieval]], [[Reranking]], [[Advanced RAG]].
- Bases de recherche / vectorielles : [[Dev/Services/Elasticsearch|Elasticsearch]], [[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/Weaviate|Weaviate]], [[Dev/Services/pgvector|pgvector]].
- Peut router ses appels via [[Dev/Services/LiteLLM|LiteLLM]] ; modèles et embedders depuis [[Dev/Services/HuggingFace|HuggingFace]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.haystack.deepset.ai/
