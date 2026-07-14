---
galaxie: dev
type: service
nom: CrewAI
alias: [crewai, crew-ai]
pitch: "Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production."
categorie: llm/framework
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/AutoGen|AutoGen]]", "[[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]]", "[[Dev/Services/Agno|Agno]]", "[[Dev/Services/smolagents|smolagents]]", "[[Dev/Services/Letta|Letta]]"]
remplace_par: []
status: actif
tags: [llm, agents, tool-use, multi-agent]
url_docs: https://docs.crewai.com/
url_repo: https://github.com/crewAIInc/crewAI
---

# CrewAI

## Pourquoi

Framework **multi-agents** Python qui modélise une équipe : des **agents** dotés d'un *rôle*, d'un *objectif* et d'outils, regroupés en **Crews** qui se répartissent des **tâches** selon un processus (séquentiel ou hiérarchique). Pour les besoins plus déterministes, les **Flows** ajoutent une orchestration événementielle à état, combinable avec les crews. Point souvent mal compris : CrewAI est **autonome**, réécrit de zéro et **indépendant de [[Dev/Services/LangChain|LangChain]]** (contrairement à ses débuts). Très adopté (50k+ stars). Cœur **open-source (MIT)**, complété par une plateforme **Enterprise** managée (déploiement, monitoring, gouvernance).

## Quand l'utiliser

- Décrire un problème comme une **équipe de rôles** collaborant (recherche → rédaction → revue, par ex.).
- Vouloir un framework multi-agents **léger et lisible**, sans dépendre de LangChain.
- Passer du proto à la prod via les **Flows** et, si besoin, la **plateforme Enterprise** managée.

## Quand NE PAS l'utiliser

- Contrôle **bas niveau** du graphe d'état (cycles explicites, checkpoints, reprise) → [[Dev/Services/LangGraph|LangGraph]].
- Simple **appel LLM** ou extraction structurée, sans collaboration d'agents → [[Dev/Services/Instructor|Instructor]] / [[Dev/Services/PydanticAI|PydanticAI]].
- Écosystème **Microsoft / .NET** → Microsoft Agent Framework (cf. [[Dev/Services/AutoGen|AutoGen]]).

## Déploiement & coût

- Cœur open-source (MIT), gratuit ; bibliothèque `pip`/`uv` importée dans l'app.
- Offre **CrewAI Enterprise** managée (payante) : déploiement d'agents, tableaux de bord, journalisation, gouvernance — optionnelle.
- Coût réel dominé par les appels **LLM** ; les processus multi-agents multiplient les appels — surveiller la dépense.

## Pièges

- **Abstraction « rôles »** trompeuse de simplicité : sans cadrage des tâches et des sorties, les agents partent en boucle ou se répètent.
- Comme tout système multi-agents : **coûts et latence** qui grimpent vite — borner itérations et délégations.
- API en **évolution** (Crews puis Flows) ; vérifier que les tutoriels ciblent la version courante.

## Alternatives

- [[Dev/Services/AutoGen|AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[Dev/Services/Agno|Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour la production.
- [[Dev/Services/smolagents|smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP.
- [[Dev/Services/Letta|Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.

## Liens

- Même famille de **frameworks d'agents** que [[Dev/Services/AutoGen|AutoGen]], [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]], [[Dev/Services/Agno|Agno]], [[Dev/Services/smolagents|smolagents]], [[Dev/Services/Letta|Letta]] et la couche d'orchestration [[Dev/Services/LangGraph|LangGraph]].
- Peut router ses appels via [[Dev/Services/LiteLLM|LiteLLM]] (abstraction multi-fournisseurs).
- Concepts : [[Multi-agent systems]], [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Agent memory]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.crewai.com/
