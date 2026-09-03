---
role: hub
nom: Agents
alias: [frameworks d'agents, agents LLM]
pitch: Les bibliothèques avec lesquelles on écrit un agent — une boucle qui planifie, appelle des outils et reprend là où elle en était.
domaines: [ai-eng]
tags: [agents, multi-agent, tool-use, agent-memory, llm]
---

# Agents

> Les bibliothèques avec lesquelles on écrit un agent — une boucle qui planifie, appelle des outils et reprend là où elle en était.

## Ce qu'il faut comprendre

- Un agent n'est pas un modèle plus intelligent, c'est **une boucle** : le modèle propose une action, on l'exécute, on lui rend le résultat, il recommence jusqu'à une condition d'arrêt. [[agent-loops]] décrit ce cycle et [[Agent patterns]] les formes qu'il prend (ReAct, plan-and-execute, réflexion). Tout ce que ce dossier contient sert à écrire cette boucle sans la réécrire.
- Le premier arbitrage est **le niveau d'abstraction**, et il se paie dans les deux sens. Une bibliothèque minimale ([[smolagents]], [[OpenAI Agents SDK]]) laisse voir la boucle et se déboguer ; un framework à rôles ([[CrewAI]], [[AutoGen]]) fait beaucoup de choses implicitement, ce qui va vite au prototype et devient opaque quand ça échoue en production. [[LangGraph]] occupe la position intermédiaire assumée : on écrit le graphe soi-même, mais l'état, la reprise et le streaming sont fournis.
- Le vrai discriminant en production n'est pas l'ergonomie mais **l'état**. Un agent qui plante à l'étape 7 sur 12 doit reprendre à 7, pas à 1 — c'est ce que [[LangGraph]] appelle la persistance et les checkpoints, et c'est ce qui manque à la plupart des boucles écrites à la main. La mémoire entre sessions est un problème distinct : cf. [[Agent memory]].
- **Le multi-agent est un choix coûteux**, pas un progrès automatique. [[Multi-agent systems]] pose la question honnêtement : découper en rôles clarifie les prompts, et multiplie les appels, la latence et les modes de défaillance. Un agent unique bien outillé bat souvent trois agents qui se parlent — le multi-agent gagne quand les rôles ont de vraies frontières d'information ou d'autorisation.
- **Les outils sont l'agent.** [[tool-use]] est le mécanisme d'échange, [[Tool use patterns]] la façon de les concevoir : peu d'outils, aux noms sans ambiguïté, aux erreurs lisibles par le modèle. Un agent médiocre est presque toujours un agent mal outillé. La forme portable de l'outillage est MCP ([[mcp-protocol]]), et [[a2a-protocol]] traite l'étage au-dessus — deux agents de fournisseurs différents qui se parlent.
- Le **harnais** est ce qui entoure la boucle et décide de sa fiabilité réelle : [[Harnais d'agent]] — quels outils sont exposés, quel contexte est rechargé à chaque tour, quelle action demande une confirmation. C'est du ressort de l'application, pas du framework.
- **Évaluer un agent n'est pas évaluer un LLM** : ce qui compte est la trajectoire, pas la dernière réponse. [[Agent evaluation]] — l'agent a-t-il appelé le bon outil, dans le bon ordre, s'est-il arrêté. Un agent qui donne la bonne réponse par un chemin faux régressera silencieusement.
- Deux choix structurels reviennent dans les fiches et méritent d'être compris avant de choisir : **l'action écrite en code** plutôt qu'en JSON ([[smolagents]] et son CodeAgent — plus expressif, mais il faut une sandbox), et **la sortie typée et validée** comme contrat de bout en bout ([[PydanticAI]]).

## Choisir

- Un agent stateful, reprenable, à contrôler pas à pas → [[LangGraph]].
- Des sorties typées et validées, une base de code Python déjà typée → [[PydanticAI]].
- Le minimum viable, agnostique du fournisseur, tracing inclus → [[OpenAI Agents SDK]].
- Une boucle courte à lire en entier, l'action écrite en Python → [[smolagents]], avec sandbox.
- Une équipe d'agents à rôles, vite montée → [[CrewAI]].
- Déclarer agents et tâches en YAML sans écrire de code → [[PraisonAI]].
- Un runtime d'agents à héberger avec mémoire et connaissance intégrées → [[Agno]].
- Une intégration dans un SI Microsoft, en C# ou Java → [[Semantic Kernel]], en sachant qu'il converge vers Microsoft Agent Framework.
- Un projet de recherche multi-agents conversationnel → [[AutoGen]], en sachant qu'il est en maintenance depuis fin 2025.
- Un agent qui édite du code, déjà écrit et installable → [[Agents de code]], pas ce dossier.
- Une application conversationnelle à déployer telle quelle → [[Assistants]].

<!-- AUTO:START -->
### Notions
- [[Agent patterns]] — domaines : ai-eng
- [[Agent skills]] — domaines : ai-eng
- [[agent-loops]] — domaines : ai-eng
- [[Harnais d'agent]] — domaines : ai-eng
- [[Human-in-the-loop]] — domaines : ai-eng
- [[Multi-agent systems]] — domaines : ai-eng
- [[Reliability patterns]] — domaines : ai-eng
- [[Tool use patterns]] — domaines : ai-eng
- [[tool-use]] — domaines : ai-eng

### Briques
- [[Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[LangGraph]] — Bibliothèque d'orchestration d'agents stateful de l'équipe LangChain — graphes cycliques avec état persistant, reprise, human-in-the-loop et streaming ; la couche bas niveau pour agents fiables, utilisable sans LangChain.
- [[OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[PraisonAI]] — Framework multi-agents low-code Python (MIT) — un fichier YAML déclare agents, tâches et processus sans écrire de code ; auto-réflexion des agents, mémoire et RAG intégrés, ~100 outils fournis et clients MCP (stdio, HTTP, SSE, WebSocket).
- [[PydanticAI]] — Framework d'agents typés de l'équipe Pydantic — agents model-agnostic à sorties structurées validées, injection de dépendances et type-safety Python ; pensé pour des apps LLM de production (Logfire, MCP, durable execution).
- [[Semantic Kernel]] — SDK d'orchestration LLM de Microsoft (C#, Python, Java) — plugins, function calling et planificateurs pour intégrer des agents dans des applications d'entreprise ; désormais convergé dans Microsoft Agent Framework, son successeur.
- [[smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.
<!-- AUTO:END -->
