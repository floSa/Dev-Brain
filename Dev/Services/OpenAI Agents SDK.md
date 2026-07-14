---
galaxie: dev
type: service
nom: OpenAI Agents SDK
alias: [openai-agents-sdk, openai-agents, agents-sdk, swarm]
pitch: "SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: "Python, TypeScript"
scaling: single-node
alternatives: ["[[Dev/Services/CrewAI|CrewAI]]", "[[Dev/Services/AutoGen|AutoGen]]", "[[Dev/Services/Agno|Agno]]", "[[Dev/Services/smolagents|smolagents]]", "[[Dev/Services/Letta|Letta]]"]
remplace_par: []
status: actif
tags: [llm, agents, tool-use, multi-agent]
url_docs: https://openai.github.io/openai-agents-python/
url_repo: https://github.com/openai/openai-agents-python
---

# OpenAI Agents SDK

## Pourquoi

SDK d'agents **léger** d'OpenAI, **successeur en production de Swarm** (le framework expérimental de 2024). Pari de la **minimalité** : peu de primitives, mais suffisantes — un **Agent** (LLM + instructions + outils), des **handoffs** (un agent passe la main à un autre, base du multi-agents), des **guardrails** (validation entrée/sortie), des **sessions** (historique persistant) et un **tracing intégré** pour visualiser et débugger les exécutions. Les fonctions Python deviennent des outils par introspection (schémas auto, validation Pydantic). **Agnostique du fournisseur** : OpenAI par défaut, mais 100+ modèles via l'API Chat Completions / [[Dev/Services/LiteLLM|LiteLLM]]. SDK **Python et TypeScript**, licence **MIT**.

## Quand l'utiliser

- Vouloir un framework d'agent **minimal et explicite**, sans abstractions lourdes à apprendre.
- Schémas **multi-agents par handoffs** (triage → spécialistes) avec garde-fous et traçabilité.
- Écosystème **OpenAI** (mais pas exclusivement) et besoin d'un **tracing** prêt à l'emploi.

## Quand NE PAS l'utiliser

- Orchestration **stateful bas niveau** (graphe cyclique, checkpoints, reprise) → [[Dev/Services/LangGraph|LangGraph]].
- **Mémoire persistante** longue durée comme primitive centrale → [[Dev/Services/Letta|Letta]].
- Modélisation explicite en **équipes/rôles** riches → [[Dev/Services/CrewAI|CrewAI]] / [[Dev/Services/Agno|Agno]].

## Déploiement & coût

- Open-source (MIT), gratuit ; SDK `pip`/`uv` (ou npm) importé dans l'app, aucune infra propre.
- Le **tracing** envoie par défaut les traces au tableau de bord OpenAI — désactivable ou redirigeable (processors tiers) pour rester self-contained.
- Coût réel dominé par les appels **LLM** ; les handoffs multiplient les tours — borner.

## Pièges

- **Tracing par défaut** vers OpenAI : vérifier la conformité données et désactiver si besoin.
- **Minimalisme** : peu de garde-fous intégrés au-delà des primitives — la robustesse (retries, fallback, timeouts) reste à câbler.
- Jeune (sorti en 2025) ; API encore mouvante — épingler les versions.

## Alternatives

- [[Dev/Services/CrewAI|CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[Dev/Services/AutoGen|AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[Dev/Services/Agno|Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour la production.
- [[Dev/Services/smolagents|smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP.
- [[Dev/Services/Letta|Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.

## Liens

- **Successeur** de Swarm (`openai/swarm`, expérimental) — repris en SDK production.
- Même famille de **frameworks d'agents** que [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/AutoGen|AutoGen]], [[Dev/Services/Agno|Agno]], [[Dev/Services/smolagents|smolagents]], [[Dev/Services/Letta|Letta]], et la couche d'orchestration [[Dev/Services/LangGraph|LangGraph]].
- Peut router ses appels via [[Dev/Services/LiteLLM|LiteLLM]] (abstraction multi-fournisseurs).
- Concepts : [[Multi-agent systems]], [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Agent memory]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://openai.github.io/openai-agents-python/
