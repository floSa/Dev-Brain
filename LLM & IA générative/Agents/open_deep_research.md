---
role: brique
nom: open_deep_research
alias: [Open Deep Research, langchain-ai-open-deep-research]
pitch: "Agent de recherche approfondie open source de LangChain (MIT) — clarifie la demande, rédige un brief, délègue à des chercheurs parallèles pilotés par un superviseur LangGraph, puis produit le rapport ; modèles, moteurs de recherche et MCP configurables ; dépôt archivé (dernier commit 2026-08-10)."
categorie: llm/agents
famille: application
domaines: [ai-eng]
licence_type: open-source
maturite: deprecated
langage: Python
hosted: [self, managed]
alternatives: ["[[Deep Agents]]"]
complements: ["[[LangGraph]]"]
tags: [llm, agents, multi-agent, retrieval, mcp]
url_docs: https://blog.langchain.com/open-deep-research/
url_repo: https://github.com/langchain-ai/open_deep_research
---

# open_deep_research

<!-- AUTO:BANDEAU:START -->
> Agent de recherche approfondie open source de LangChain (MIT) — clarifie la demande, rédige un brief, délègue à des chercheurs parallèles pilotés par un superviseur LangGraph, puis produit le rapport ; modèles, moteurs de recherche et MCP configurables ; dépôt archivé (dernier commit 2026-08-10).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Python | open-source | self-hébergé ou managé | deprecated | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Agent de **recherche approfondie** de LangChain : à partir d'une question ouverte, il produit un
rapport sourcé. Un graphe [[LangGraph]] enchaîne quatre phases — `clarify_with_user`,
`write_research_brief`, un **superviseur** qui délègue des unités de recherche (`ConductResearch`)
à des chercheurs lancés en parallèle, puis `final_report_generation`. Chaque chercheur boucle sur
ses outils de recherche et **compresse** ses trouvailles avant de les rendre. Modèles, moteur de
recherche (Tavily par défaut, recherche native OpenAI ou Anthropic) et serveurs MCP se règlent par
configuration. Classé 6ᵉ du Deep Research Bench en août 2025 (score RACE 0,4344). **Le dépôt est
archivé** : c'est aujourd'hui une référence d'architecture à lire, pas un projet à suivre. Le
patron est décrit dans [[Deep research]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Lire une architecture de recherche approfondie complète et courte — l'essentiel du graphe tient dans `deep_researcher.py` | **Projet neuf** : dépôt archivé, plus rien n'est corrigé ni maintenu (derniers commits : mises à jour de dépendances, août 2026) — partir de [[Deep Agents]], dont l'exemple `deep_research` reprend le sujet |
| Apprendre le patron superviseur / chercheurs avec ses garde-fous : `max_concurrent_research_units`, `max_researcher_iterations` | Besoin d'un produit prêt à l'emploi : c'est un dépôt à cloner et configurer, pas un service |
| Suivre le cours LangChain Academy et son dépôt compagnon `deep_research_from_scratch` | Recherche sur un corpus interne : la recherche est web par défaut (Tavily), une source privée passe par un serveur MCP à fournir soi-même |

## Mise en œuvre

- Installation — cloner le dépôt puis `uv sync` ; le projet n'est pas installé comme bibliothèque
- Point d'entrée — copier `.env.example` en `.env`, lancer `langgraph dev`, ouvrir LangGraph Studio ; les champs de `configuration.py` (`search_api`, `mcp_config`, modèles) se règlent depuis Studio
- Prérequis — Python ≥ 3.10, une clé pour chaque fournisseur de modèle utilisé et une clé Tavily si la recherche par défaut est conservée ; les modèles par défaut sont chez OpenAI
- Exécution — serveur LangGraph local (`127.0.0.1:2024`), ou déploiement sur LangGraph Platform, ou via Open Agent Platform
- Coût — gratuit sous MIT ; chaque unité de recherche est une boucle complète de LLM et de recherches, donc le coût suit le nombre de chercheurs et d'itérations

## Écosystème

### Alternatives

- [[Deep Agents]] — Harnais d'agent « batteries incluses » de l'équipe LangChain (MIT), construit sur LangGraph — système de fichiers à backends interchangeables, sous-agents à contexte isolé (outil `task`), résumé et déport du contexte sur disque, planification en option (`write_todos`) ; agnostique du modèle, Python et TypeScript. — le successeur de fait : son dépôt porte un exemple `deep_research`, et lui est maintenu.

### Compléments

- [[LangGraph]] — Bibliothèque d'orchestration d'agents stateful de l'équipe LangChain — graphes cycliques avec état persistant, reprise, human-in-the-loop et streaming ; la couche bas niveau pour agents fiables, utilisable sans LangChain. — le graphe de l'agent est un graphe LangGraph, servi par `langgraph dev`.

## Ressources

- Documentation — https://blog.langchain.com/open-deep-research/
- Dépôt — https://github.com/langchain-ai/open_deep_research
- Cours — https://github.com/langchain-ai/deep_research_from_scratch

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Deep research]] — la notion : clarifier, planifier, chercher en parallèle, rédiger
- [[Sous-agents et isolation du contexte]] — les chercheurs sont des sous-agents à contexte isolé
- [[Multi-agent systems]] — la topologie superviseur / exécutants
- [[Agent evaluation]] — mesurer un agent de recherche, dont le Deep Research Bench
