---
galaxie: dev
type: service
nom: LangGraph
alias: [langgraph, langchain-ai-langgraph]
pitch: "Bibliothèque d'orchestration d'agents stateful de l'équipe LangChain — graphes cycliques avec état persistant, reprise, human-in-the-loop et streaming ; la couche bas niveau pour agents fiables, utilisable sans LangChain."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [llm, agents, tool-use]
url_docs: https://docs.langchain.com/oss/python/langgraph/overview
url_repo: https://github.com/langchain-ai/langgraph
---

# LangGraph

## Pourquoi

Bibliothèque d'orchestration d'**agents stateful**, développée par l'équipe [[Dev/Services/LangChain|LangChain]] mais **utilisable seule**. Elle modélise un agent comme un **graphe** de nœuds (étapes) et d'arêtes (transitions, y compris **cycliques** et conditionnelles), avec un **état partagé** persisté entre les pas. Ce modèle bas niveau apporte ce qui manque à une simple chaîne : **reprise après interruption** (checkpoints), **human-in-the-loop**, **mémoire** durable, exécution **streaming** et observabilité des transitions. Inspirée de Pregel/Beam (calcul sur graphes) et de l'API de NetworkX. Se situe **au-dessus de** LangChain dans le stack : LangChain fournit les briques (modèles, outils), LangGraph orchestre leur enchaînement stateful. Écrit en **Python** (portage JS), cœur sous licence **MIT**.

## Quand l'utiliser

- Agents **non triviaux** : boucles, branchements conditionnels, plusieurs outils, plusieurs étapes.
- Besoin d'**état durable** : reprise après panne, sessions longues, checkpoints.
- **Human-in-the-loop** : suspendre, faire valider/corriger par un humain, puis reprendre.
- Systèmes **multi-agents** coordonnés, avec contrôle explicite du flux et du partage d'état.

## Quand NE PAS l'utiliser

- Chaîne **linéaire simple** ou appel LLM one-shot : la surcouche graphe est inutile → [[Dev/Services/LangChain|LangChain]] (chaînes/LCEL) suffit.
- App **centrée RAG/données** sans logique d'agent complexe → [[Dev/Services/LlamaIndex|LlamaIndex]] ou [[Dev/Services/Haystack|Haystack]].

## Déploiement & coût

- Cœur open-source (MIT), gratuit ; bibliothèque importée dans l'app.
- ⚠️ Le **runtime serveur** `langgraph-api` (et la **LangGraph Platform** managée) est sous **Elastic License 2.0** : un déploiement en production de ce serveur requiert une clé/licence commerciale. Le cœur LangGraph reste MIT — distinguer la bibliothèque du serveur d'exécution managé.
- Coût réel dominé par les appels LLM ; persistance d'état à prévoir (base/checkpointer).

## Pièges

- **Confusion de licence** fréquente : la lib est MIT, mais `langgraph-api` / LangGraph Platform ne le sont pas — vérifier avant de bâtir une offre dessus.
- Modèle **graphe + état** plus exigeant : il faut penser nœuds, transitions et schéma d'état — plus de cérémonie qu'une chaîne.
- Écosystème jeune et **API en évolution** ; bien épingler les versions.

## Alternatives

<!-- LangGraph est une couche d'orchestration complémentaire (cf. Liens), pas un substitut direct des frameworks généralistes. -->
- Pour un besoin d'agent plus léger, les frameworks généralistes ([[Dev/Services/LangChain|LangChain]], [[Dev/Services/LlamaIndex|LlamaIndex]], [[Dev/Services/Haystack|Haystack]]) intègrent leur propre couche d'agents.

## Liens

- **Au-dessus de** [[Dev/Services/LangChain|LangChain]] : même équipe (LangChain Inc.), orchestre ses briques de façon stateful ; utilisable néanmoins sans LangChain.
- Même famille de **frameworks d'agents** que [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/AutoGen|AutoGen]], [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]], [[Dev/Services/Agno|Agno]], [[Dev/Services/smolagents|smolagents]] et [[Dev/Services/Letta|Letta]] — mais LangGraph se place en couche d'orchestration bas niveau, **complémentaire** plutôt que substitut.
- Peut router ses appels via [[Dev/Services/LiteLLM|LiteLLM]] (abstraction multi-fournisseurs).
- Concepts : [[Agent patterns]], [[agent-loops]], [[Multi-agent systems]], [[Tool use patterns]], [[Agent memory]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.langchain.com/oss/python/langgraph/overview
