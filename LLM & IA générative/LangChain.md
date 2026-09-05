---
role: brique
nom: LangChain
alias: [langchain, langchain-ai]
pitch: "Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith."
categorie: llm/socle
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[LlamaIndex]]", "[[Haystack]]", "[[DSPy]]", "[[Semantic Kernel]]", "[[PydanticAI]]"]
complements: []
tags: [llm, rag, agents, tool-use]
url_docs: https://docs.langchain.com/
url_repo: https://github.com/langchain-ai/langchain
---

# LangChain

<!-- AUTO:BANDEAU:START -->
> Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'applications LLM le plus adopté — environ 140 k étoiles, version 1.x. Son cœur :
des **interfaces standardisées** (modèles de chat, embeddings, vector stores, retrievers,
outils) derrière lesquelles se branchent des centaines d'**intégrations**, ce qui permet de
changer de fournisseur ou de base vectorielle sans réécrire la logique. On compose ces
briques en **chaînes** — LCEL, son langage d'expression — et en **agents**, des LLM qui
choisissent des outils en boucle. Un portage JS/TS existe. C'est aussi le socle d'un
écosystème plus large : [[LangGraph]] pour les agents stateful, LangSmith pour
l'observabilité — ce qui explique sa position de choix par défaut, et le fait que beaucoup
d'autres briques du domaine se définissent par rapport à lui.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Prototyper vite une app LLM en s'appuyant sur le catalogue d'intégrations (modèles, vector stores, loaders, outils) | La surface d'API bouge entre majeures (0.x → 1.x) et les modules sont éclatés — `langchain-core`, `langchain-community`, paquets d'intégration : épingler les versions |
| Construire des agents simples à moyens — appel d'outils, RAG conversationnel — sans tout recâbler à la main | Les abstractions masquent les prompts et les appels réels : déboguer un comportement inattendu demande souvent de descendre sous la chaîne |
| Rester agnostique du fournisseur : abstraire OpenAI, Anthropic ou un modèle local derrière une interface commune | |
| Bénéficier de l'écosystème LangGraph et LangSmith pour passer du prototype à la production | |

## Mise en œuvre

- Installation — dépendance Python (`uv add` / `pip install`) ; un portage JS/TS existe
- Point d'entrée — import Python : interfaces standardisées, chaînes LCEL, agents
- Prérequis — aucune infra propre : l'app scale comme n'importe quel service Python
- Exécution — en bibliothèque, rien à héberger ; les appels peuvent être routés via [[LiteLLM]] pour abstraire le fournisseur
- Coût — gratuit ; compléments managés payants de l'éditeur — LangSmith (observabilité et évaluation), LangGraph Platform (déploiement d'agents) —, optionnels ; le coût réel vient des appels aux LLM

## Écosystème

### Alternatives

- [[LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- [[Haystack]] — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.
- [[DSPy]] — Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques.
- [[Semantic Kernel]] — SDK d'orchestration LLM de Microsoft (C#, Python, Java) — plugins, function calling et planificateurs pour intégrer des agents dans des applications d'entreprise ; désormais convergé dans Microsoft Agent Framework, son successeur.
- [[PydanticAI]] — Framework d'agents typés de l'équipe Pydantic — agents model-agnostic à sorties structurées validées, injection de dépendances et type-safety Python ; pensé pour des apps LLM de production (Logfire, MCP, durable execution).

## Ressources

- Documentation — https://docs.langchain.com/
- Dépôt — https://github.com/langchain-ai/langchain

## Voir aussi

- [[RAG]] — la notion, et ses techniques [[Chunking strategies]], [[Hybrid retrieval]], [[Reranking]], [[Advanced RAG]]
- [[LangChain SQL agent]] — son module text-to-SQL (SQLDatabaseToolkit + agent), et la notion [[Text-to-SQL]]
- Modèles et embeddings depuis [[HuggingFace]] ; vector stores comme [[Qdrant]] ou [[Chroma]] pour le RAG
- [[LLM & IA générative]] — le hub du domaine
- [[Comparatif - Frameworks LLM]] — ce qui départage les frameworks de la catégorie
