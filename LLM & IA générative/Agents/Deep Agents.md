---
role: brique
nom: Deep Agents
alias: [deepagents, langchain-ai-deepagents]
pitch: "Harnais d'agent « batteries incluses » de l'équipe LangChain (MIT), construit sur LangGraph — système de fichiers à backends interchangeables, sous-agents à contexte isolé (outil `task`), résumé et déport du contexte sur disque, planification en option (`write_todos`) ; agnostique du modèle, Python et TypeScript."
categorie: llm/agents
famille: paquet
domaines: [ai-eng]
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[Claude Agent SDK]]", "[[open_deep_research]]"]
complements: ["[[LangGraph]]"]
tags: [llm, agents, multi-agent, tool-use, context-engineering, mcp]
url_docs: https://docs.langchain.com/oss/python/deepagents/overview
url_repo: https://github.com/langchain-ai/deepagents
---

# Deep Agents

<!-- AUTO:BANDEAU:START -->
> Harnais d'agent « batteries incluses » de l'équipe LangChain (MIT), construit sur LangGraph — système de fichiers à backends interchangeables, sous-agents à contexte isolé (outil `task`), résumé et déport du contexte sur disque, planification en option (`write_todos`) ; agnostique du modèle, Python et TypeScript.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

**Harnais d'agent** de l'équipe [[LangChain]] : un agent opinionated qui tourne tel quel, dont on
remplace ensuite les pièces. Il empile trois couches — [[LangGraph]] pour le runtime (streaming,
persistance, checkpoints), `create_agent` de LangChain pour la boucle minimale, puis Deep Agents
pour ce qui fait tenir une tâche longue : un **système de fichiers** (local, en mémoire, store
LangGraph ou bac à sable) où l'agent dépose ses résultats, des **sous-agents** à contexte isolé
appelés par l'outil `task`, le **résumé** des longs échanges avec déport des sorties d'outils sur
disque, et une liste de tâches `write_todos`, en option depuis la 0.7. Tout modèle qui sait appeler
des outils convient. La notion derrière est décrite dans [[Architecture deep agent]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tâche longue et multi-étapes — recherche, rédaction, code — qui déborde la fenêtre de contexte : fichiers et sous-agents sortent le volume du contexte principal | Tâche courte ou chaîne d'étapes connue d'avance : un workflow fixe ou une simple boucle ReAct coûte moins, et le harnais n'apporte rien |
| Vouloir la boucle, les outils de fichiers et la délégation déjà câblés plutôt que les réécrire sur [[LangGraph]] | Modèle sans appel d'outils : le harnais suppose du tool calling, et le dépôt le pose en condition d'emploi |
| Rester agnostique du modèle : API frontier, poids ouverts hébergés, ou local via Ollama, vLLM, llama.cpp | Besoin d'un graphe d'états écrit à la main, transition par transition : descendre à [[LangGraph]] |
| Réutiliser un graphe LangGraph existant comme sous-agent (`CompiledSubAgent`) | API à figer : version 0.x, et la planification est passée d'incluse à optionnelle en 0.7 — épingler la version |

## Mise en œuvre

- Installation — `uv add deepagents` ; port TypeScript distinct, `deepagentsjs`
- Point d'entrée — `create_deep_agent(model=…, tools=[…], system_prompt=…)`, puis `agent.invoke({"messages": …})` ; sous-agents déclarés en dictionnaires (`name`, `description`, `system_prompt`, `tools`, `model`, `mode`)
- Prérequis — Python ≥ 3.11, un modèle qui supporte l'appel d'outils ; un bac à sable si l'outil `execute` doit lancer des commandes, car les permissions des outils de fichiers ne s'appliquent pas aux backends bac à sable
- Exécution — en bibliothèque dans l'application hôte ; déploiement et suivi via LangSmith en option
- Coût — gratuit sous MIT ; la dépense est celle des LLM, et chaque sous-agent y ajoute ses propres appels

## Écosystème

### Alternatives

- [[Claude Agent SDK]] — SDK d'Anthropic qui expose la boucle d'agent de Claude Code comme bibliothèque (Python, TypeScript) — outils intégrés (fichiers, shell, web), sous-agents, hooks, permissions, sessions, MCP, skills ; réservé aux modèles Claude, sous conditions commerciales d'Anthropic. — même famille de harnais, mais verrouillé sur Claude ; Deep Agents reste agnostique du modèle.
- [[open_deep_research]] — Agent de recherche approfondie open source de LangChain (MIT) — clarifie la demande, rédige un brief, délègue à des chercheurs parallèles pilotés par un superviseur LangGraph, puis produit le rapport ; modèles, moteurs de recherche et MCP configurables ; dépôt archivé (dernier commit 2026-08-10). — un agent de recherche figé, à ne pas prendre comme point de départ : l'exemple `deep_research` de ce dépôt-ci est sa relève.

### Compléments

- [[LangGraph]] — Bibliothèque d'orchestration d'agents stateful de l'équipe LangChain — graphes cycliques avec état persistant, reprise, human-in-the-loop et streaming ; la couche bas niveau pour agents fiables, utilisable sans LangChain. — c'est le runtime sous Deep Agents, et n'importe quel graphe compilé y devient un sous-agent.

## Ressources

- Documentation — https://docs.langchain.com/oss/python/deepagents/overview
- Dépôt — https://github.com/langchain-ai/deepagents
- Documentation — https://docs.langchain.com/oss/python/deepagents/subagents

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Architecture deep agent]] — la notion : planification, fichiers, sous-agents
- [[Sous-agents et isolation du contexte]] — ce que la délégation achète, et ce qu'elle coûte
- [[Deep research]] — le cas d'usage type, avec un exemple `deep_research` dans le dépôt
- [[Harnais d'agent]] — ce qui entoure la boucle et décide de sa fiabilité
- [[Context engineering]] — la gestion du budget de contexte que le harnais automatise
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
