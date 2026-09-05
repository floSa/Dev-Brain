---
role: brique
nom: Haystack
alias: [haystack, deepset-haystack, farm-haystack]
pitch: "Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération."
categorie: llm/rag
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[LangChain]]", "[[LlamaIndex]]", "[[DSPy]]"]
complements: []
tags: [llm, rag, semantic-search, hybrid-search, agents]
url_docs: https://docs.haystack.deepset.ai/
url_repo: https://github.com/deepset-ai/haystack
---

# Haystack

<!-- AUTO:BANDEAU:START -->
> Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'orchestration LLM de **deepset**, orienté production. Son modèle est le **pipeline
explicite** : on câble des composants typés — retrievers, embedders, rankers, générateurs,
routeurs — en un graphe lisible, testable et observable, et l'on garde la main sur chaque
étape de la récupération à la génération. Il est solide sur le RAG, la recherche sémantique,
la recherche hybride dense + BM25 et, depuis peu, les agents. La 2.x est une réécriture
complète de la 1.x : composants et pipelines typés, API incompatible avec l'ancien
`farm-haystack`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Mettre un RAG ou une recherche sémantique en production avec un pipeline explicite, testable et observable | Rupture 1.x → 2.x : `farm-haystack` et la 2.x ont des API incompatibles — vérifier sur quelle version pointe un tutoriel avant de le suivre |
| Vouloir du contrôle fin sur chaque étape — retrieval, reranking, routing, génération — plutôt que des abstractions opaques | Écosystème d'intégrations plus restreint : certains connecteurs récents manquent ou sont communautaires |
| Recherche hybride dense + lexicale, branchée sur Elasticsearch, OpenSearch ou une base vectorielle | Le pipeline de composants est plus verbeux qu'il ne faut pour un simple appel LLM one-shot |
| Préférer une licence permissive et un éditeur orienté entreprise (deepset) | |

## Mise en œuvre

- Installation — bibliothèque Python importée dans l'app ; vérifier le paquet visé, l'ancien `farm-haystack` (1.x) n'ayant pas la même API que la 2.x
- Point d'entrée — un pipeline de composants typés, sérialisable en YAML
- Prérequis — une base de recherche ou vectorielle en amont : [[Elasticsearch]], [[Qdrant]], [[Weaviate]], [[pgvector]]
- Exécution — importée dans l'app ; un pipeline sérialisé se déploie comme service
- Coût — gratuit sous Apache-2.0 ; deepset AI Platform / Studio est une offre managée payante et optionnelle ; le coût réel est dominé par les appels LLM, l'embedding et l'infra de la base de recherche

## Écosystème

### Alternatives

- [[LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.
- [[LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- [[DSPy]] — Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques.

## Ressources

- Documentation — https://docs.haystack.deepset.ai/
- Dépôt — https://github.com/deepset-ai/haystack

## Voir aussi

- [[RAG]] — la notion du dossier
- [[Chunking strategies]] · [[Hybrid retrieval]] · [[Reranking]] · [[Advanced RAG]] — les techniques que ses composants implémentent
- [[LiteLLM]] — pour router ses appels de modèle ; [[HuggingFace]] pour les modèles et les embedders
- [[Comparatif - Frameworks LLM]] — ce qui départage les frameworks du domaine
