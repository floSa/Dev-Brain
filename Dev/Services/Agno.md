---
galaxie: dev
type: service
nom: Agno
alias: [agno, phidata, phi-data]
pitch: "Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production."
categorie: llm/framework
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/CrewAI|CrewAI]]", "[[Dev/Services/AutoGen|AutoGen]]", "[[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]]", "[[Dev/Services/smolagents|smolagents]]", "[[Dev/Services/Letta|Letta]]"]
remplace_par: []
status: actif
tags: [llm, agents, tool-use, multi-agent]
url_docs: https://docs.agno.com/
url_repo: https://github.com/agno-agi/agno
---

# Agno

## Pourquoi

Framework d'agents Python **haute performance**, anciennement **phidata** (rebrand janvier 2025 ; *agno* = « pur » en grec, pour « pur Python, sans graphes ni chaînes »). Met en avant une **instanciation d'agent très rapide et légère** en mémoire, avec **mémoire, connaissance (RAG) et raisonnement** intégrés comme briques de base, et le **multimodal**. Au-delà de la bibliothèque, Agno fournit **AgentOS** : un runtime/plan de contrôle **self-host** (API de production, observabilité, RBAC, scheduling) pour exécuter et gouverner des **systèmes multi-agents** dans son propre cloud. Licence **Apache-2.0**.

## Quand l'utiliser

- Construire des agents (ou systèmes multi-agents) avec **mémoire + connaissance + raisonnement** sans assembler dix briques.
- Vouloir passer du proto à la **production gouvernée** via **AgentOS** (API, RBAC, monitoring) en restant **self-host**.
- Besoins **multimodaux** (texte/image/audio) dans un même framework.

## Quand NE PAS l'utiliser

- Besoin d'orchestration **stateful bas niveau** (graphe cyclique explicite, checkpoints) → [[Dev/Services/LangGraph|LangGraph]].
- Agent **minimaliste jetable** ou raisonnement en code → [[Dev/Services/smolagents|smolagents]] / [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]].
- Simple **appel LLM** ou extraction structurée → [[Dev/Services/Instructor|Instructor]] / [[Dev/Services/PydanticAI|PydanticAI]].

## Déploiement & coût

- Cœur open-source (Apache-2.0), gratuit ; bibliothèque `pip`/`uv` importée dans l'app.
- **AgentOS** s'exécute **dans son propre cloud** (self-host) — pas de dépendance à un SaaS tiers pour le plan de contrôle ; une UI de gestion est fournie.
- Coût réel dominé par les appels **LLM** ; les systèmes multi-agents multiplient les appels — surveiller la dépense.

## Pièges

- **Héritage phidata** : tutoriels et imports antérieurs à 2025 référencent l'ancien nom — vérifier qu'on cible bien `agno`.
- API en **évolution rapide** (v2.x, releases fréquentes) — épingler les versions.
- Le discours **« le plus rapide »** porte sur l'instanciation en mémoire ; le coût/latence réels restent dominés par le LLM, pas par le framework.

## Alternatives

- [[Dev/Services/CrewAI|CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[Dev/Services/AutoGen|AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[Dev/Services/smolagents|smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP.
- [[Dev/Services/Letta|Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.

## Liens

- **Ex-phidata** : même projet, renommé en janvier 2025.
- Même famille de **frameworks d'agents** que [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/AutoGen|AutoGen]], [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]], [[Dev/Services/smolagents|smolagents]], [[Dev/Services/Letta|Letta]], et la couche d'orchestration [[Dev/Services/LangGraph|LangGraph]].
- Peut router ses appels via [[Dev/Services/LiteLLM|LiteLLM]] (abstraction multi-fournisseurs).
- Concepts : [[Multi-agent systems]], [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Agent memory]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.agno.com/
