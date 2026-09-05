---
role: brique
nom: Letta
alias: [letta, memgpt, mem-gpt]
pitch: "Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud."
categorie: llm/memoire
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Agno]]", "[[CrewAI]]", "[[AutoGen]]", "[[OpenAI Agents SDK]]", "[[smolagents]]", "[[OpenViking]]"]
complements: []
tags: [llm, agents, tool-use]
url_docs: https://docs.letta.com/
url_repo: https://github.com/letta-ai/letta
---

# Letta

<!-- AUTO:BANDEAU:START -->
> Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'**agents stateful** issu du projet de recherche **MemGPT** (Berkeley), d'où son
nom historique. Son cœur : une **mémoire persistante** gérée comme une hiérarchie de type OS
— contexte « en RAM » contre stockage « disque » — que l'agent **édite lui-même** via des
outils dédiés. L'agent se souvient donc entre sessions, met à jour ses faits sur
l'utilisateur et le domaine, et apprend au fil du temps au lieu de repartir de zéro à chaque
conversation. Deux conséquences directes de ce modèle : sans tri ni invalidation, les
souvenirs s'accumulent — bruit, coût, contexte saturé ; et la mémoire doit être cloisonnée
par utilisateur, faute de quoi une session fuit dans la suivante.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Agents longue durée qui doivent se souvenir d'un utilisateur, d'un projet, d'un historique — assistants personnels, support, copilotes | Tâche courte et sans état : la machinerie de mémoire est superflue → [[smolagents]], [[Instructor]] |
| Vouloir la mémoire comme **primitive de première classe**, et non comme un RAG bricolé après coup | Besoin de contrôle bas niveau du graphe d'exécution — cycles, branchements explicites → [[LangGraph]] |
| Servir des agents derrière une API stateful, l'état vivant côté serveur et non dans le client | Orchestration multi-agents **en rôles** comme primitive centrale → [[CrewAI]], [[Agno]] |
| | Versions 0.x et API en évolution rapide : épingler les versions |

## Mise en œuvre

- Installation — serveur Letta self-host par Docker, ou Letta Cloud managé
- Point d'entrée — API agents REST complète, SDK Python et TypeScript, et un Agent Development Environment visuel
- Prérequis — une base de données pour la persistance de l'état : c'est le cœur du produit, pas une option
- Exécution — self-hébergé ou managé ; mono-nœud
- Coût — gratuit ; le coût réel est dominé par les appels LLM, et la gestion de mémoire en ajoute (auto-édition, récupération)

## Écosystème

### Alternatives

- [[Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.
- [[OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

## Ressources

- Documentation — https://docs.letta.com/
- Dépôt — https://github.com/letta-ai/letta

## Voir aussi

- [[Agent memory]] — la notion qu'il implémente directement, héritée de MemGPT (Packer et al., 2023)
- [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Multi-agent systems]] — les notions voisines
- [[LLM & IA générative]] — le hub du domaine
