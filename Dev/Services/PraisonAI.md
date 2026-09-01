---
galaxie: dev
type: service
nom: PraisonAI
alias: [praisonai, praison-ai, praisonaiagents]
pitch: "Framework multi-agents low-code Python (MIT) — un fichier YAML déclare agents, tâches et processus sans écrire de code ; auto-réflexion des agents, mémoire et RAG intégrés, ~100 outils fournis et clients MCP (stdio, HTTP, SSE, WebSocket)."
categorie: llm/framework
licence_type: open-source
hosted: both
maturite: production
langage: "Python, JavaScript"
scaling: single-node
alternatives: ["[[Dev/Services/CrewAI|CrewAI]]", "[[Dev/Services/AutoGen|AutoGen]]", "[[Dev/Services/Agno|Agno]]", "[[Dev/Services/smolagents|smolagents]]"]
remplace_par: []
status: actif
tags: [llm, agents, multi-agent, tool-use, low-code, mcp]
url_docs: https://docs.praison.ai
url_repo: https://github.com/MervinPraison/PraisonAI
---

# PraisonAI

## Pourquoi

Framework d'agents dont le parti pris est **l'entrée low-code** : un `agents.yaml` décrit les agents, leurs rôles, leurs tâches et le processus qui les enchaîne, et `praisonai` l'exécute. Le SDK Python (`praisonaiagents`) reste disponible pour les cas qui débordent du déclaratif — le YAML est une porte d'entrée, pas une limite.

Deuxième trait distinctif : la **couche d'auto-réflexion**. Un agent peut relire sa propre sortie et la reprendre avant de la rendre, sans qu'un second agent critique soit câblé à la main. Le framework livre aussi mémoire et RAG intégrés, une centaine d'outils prêts à l'emploi, et des **clients MCP** sur quatre transports (stdio, HTTP, SSE, WebSocket) pour consommer des serveurs d'outils externes.

Contrairement à une idée répandue dans les comparatifs, PraisonAI **n'enrobe ni [[Dev/Services/CrewAI|CrewAI]] ni [[Dev/Services/AutoGen|AutoGen]]** : c'est une implémentation autonome. Il rejoint donc la famille des frameworks multi-agents Python, avec le YAML comme différenciateur face à leurs API impératives. Licence **MIT**, développement soutenu.

## Quand l'utiliser

- Décrire un système multi-agents en **configuration** plutôt qu'en code, et le versionner comme tel.
- Besoin d'auto-réflexion sur les sorties sans construire soi-même la boucle critique.
- Vouloir mémoire, RAG et un large jeu d'outils **fournis** plutôt qu'assemblés.
- Brancher des serveurs **MCP** existants sans écrire d'adaptateur.

## Quand NE PAS l'utiliser

- Contrôle bas niveau du graphe d'état (cycles explicites, checkpoints, reprise) → [[Dev/Services/LangGraph|LangGraph]].
- Bibliothèque **minimale et lisible de bout en bout**, à auditer intégralement → [[Dev/Services/smolagents|smolagents]].
- Performance d'instanciation et runtime de production gouverné → [[Dev/Services/Agno|Agno]].
- Simple appel LLM ou extraction structurée, sans agents → [[Dev/Services/Instructor|Instructor]] / [[Dev/Services/PydanticAI|PydanticAI]].
- Préférence pour un **canvas visuel** plutôt qu'un fichier YAML → [[Dev/Services/Langflow|Langflow]] / [[Dev/Services/Dify|Dify]].

## Déploiement & coût

- Open-source (MIT), gratuit : `pip install praisonai` (CLI + YAML) ou `pip install praisonaiagents` (SDK seul).
- S'exécute en bibliothèque dans l'application hôte, ou en conteneur ; scaling = celui de l'hôte (single-node).
- Exécution distante d'agents et d'outils possible via paramètres dédiés, en plus du self-host.
- Interfaces optionnelles : chat léger fourni, tableau de bord multi-canaux, intégration à un constructeur visuel.
- Coût réel dominé par les appels **LLM** ; auto-réflexion et délégation **multiplient** les appels pour une même tâche.

## Pièges

- L'**auto-réflexion double au moins** le nombre d'appels : gain de qualité contre coût et latence, à mesurer et non à supposer.
- Le YAML masque la boucle d'agent : quand elle dérape, le débogage se fait quand même dans le SDK.
- Surface fonctionnelle **large** (mémoire, RAG, ~100 outils, UI, MCP) donc dépendances nombreuses — installer par extras plutôt qu'en bloc.
- Cadence de commits élevée et API mouvante : épingler les versions.
- Documentation abondante mais inégale selon les fonctionnalités ; le dépôt reste la référence.

## Alternatives

- [[Dev/Services/CrewAI|CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[Dev/Services/AutoGen|AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[Dev/Services/Agno|Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[Dev/Services/smolagents|smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.

## Liens

- Même famille de **frameworks d'agents** que [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/AutoGen|AutoGen]], [[Dev/Services/Agno|Agno]], [[Dev/Services/smolagents|smolagents]], et la couche d'orchestration [[Dev/Services/LangGraph|LangGraph]].
- Peut router ses appels via [[Dev/Services/LiteLLM|LiteLLM]] (abstraction multi-fournisseurs).
- Concepts : [[Multi-agent systems]], [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Agent memory]], [[mcp-protocol]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.praison.ai
