---
role: brique
nom: Agno
alias: [agno, phidata, phi-data]
pitch: "Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production."
categorie: llm/agents
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[CrewAI]]", "[[AutoGen]]", "[[OpenAI Agents SDK]]", "[[smolagents]]", "[[Letta]]", "[[PraisonAI]]"]
complements: []
tags: [llm, agents, tool-use, multi-agent]
url_docs: https://docs.agno.com/
url_repo: https://github.com/agno-agi/agno
---

# Agno

<!-- AUTO:BANDEAU:START -->
> Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'agents Python dont l'argument est la **performance d'instanciation** : un agent se
crée très vite et pèse peu en mémoire. Anciennement **phidata**, rebaptisé en janvier 2025
(*agno* = « pur » en grec, pour « pur Python, sans graphes ni chaînes »). Il fournit **mémoire,
connaissance (RAG) et raisonnement** comme briques de base plutôt que comme extensions, et gère
le **multimodal** (texte, image, audio). Au-delà de la bibliothèque, il livre **AgentOS** : un
runtime et plan de contrôle **self-host** — API de production, observabilité, RBAC, scheduling,
UI de gestion — pour exécuter et gouverner des systèmes multi-agents dans son propre cloud.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Construire des agents, ou des systèmes multi-agents, avec mémoire + connaissance + raisonnement sans assembler dix briques | Base de code ou tutoriels antérieurs à 2025 : l'héritage phidata traîne dans les imports et les exemples — vérifier qu'on cible bien `agno` |
| Vouloir passer du proto à la production gouvernée via AgentOS (API, RBAC, monitoring) en restant self-host | Projet à figer : API en évolution rapide (v2.x, releases fréquentes), épingler les versions |
| Besoins multimodaux (texte / image / audio) dans un même framework | Attendre un gain de latence du framework : le « le plus rapide » porte sur l'instanciation en mémoire, le coût et la latence réels restant dominés par le LLM |

## Mise en œuvre

- Installation — bibliothèque `pip` / `uv`, importée dans l'application ; AgentOS se déploie à côté
- Point d'entrée — API Python (agents, mémoire, connaissance, raisonnement) ; AgentOS ajoute une API de production et une UI de gestion
- Prérequis — Python et un accès LLM ; pour AgentOS, une infrastructure à soi (aucun SaaS tiers requis)
- Exécution — en bibliothèque dans l'application hôte ; AgentOS s'exécute self-host, dans son propre cloud
- Coût — gratuit, Apache-2.0 ; la dépense réelle est celle des appels LLM, et les systèmes multi-agents les multiplient — surveiller

## Écosystème

### Alternatives

- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.
- [[Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.
- [[PraisonAI]] — Framework multi-agents low-code Python (MIT) — un fichier YAML déclare agents, tâches et processus sans écrire de code ; auto-réflexion des agents, mémoire et RAG intégrés, ~100 outils fournis et clients MCP (stdio, HTTP, SSE, WebSocket).

## Ressources

- Documentation — https://docs.agno.com/
- Dépôt — https://github.com/agno-agi/agno

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Agent patterns]] — patrons d'architecture d'agents
- [[agent-loops]] — la boucle perception / action d'un agent
- [[Tool use patterns]] — patrons d'appel d'outils
- [[Agent memory]] — mémoire persistante d'agent
