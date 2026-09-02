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

## Pourquoi

Framework d'**agents stateful** issu du projet de recherche **MemGPT** (Berkeley) — d'où son nom historique. Son cœur : une **mémoire persistante** gérée comme une **hiérarchie type OS** (contexte « en RAM » vs stockage « disque »), que l'agent **édite lui-même** via des outils dédiés. Résultat : l'agent **se souvient entre sessions**, met à jour ses faits sur l'utilisateur et le domaine, et **apprend** au fil du temps au lieu de repartir de zéro à chaque conversation. Letta expose une **API agents** complète (REST), des SDK Python et TypeScript, et un **Agent Development Environment** visuel. Licence **Apache-2.0**.

## Quand l'utiliser

- Agents **longue durée** qui doivent **se souvenir** d'un utilisateur, d'un projet, d'un historique (assistants personnels, support, copilotes).
- Vouloir la **mémoire comme primitive de première classe**, pas comme un bricolage de RAG ajouté après coup.
- Servir des agents derrière une **API stateful** (l'état vit côté serveur, pas dans le client).

## Quand NE PAS l'utiliser

- Tâche **courte et sans état** (un appel, une extraction) : la machinerie de mémoire est superflue → [[smolagents]] / [[Instructor]].
- Besoin de **contrôle bas niveau du graphe** d'exécution (cycles, branchements explicites) → [[LangGraph]].
- Orchestration **multi-agents en rôles** comme primitive centrale → [[CrewAI]] / [[Agno]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; **serveur Letta** self-host (Docker) exposant l'API agents, ou **Letta Cloud** managé.
- Persistance d'état à prévoir (base de données) — c'est le cœur du produit.
- Coût réel dominé par les appels **LLM** ; la gestion de mémoire ajoute des appels (auto-édition, récupération).

## Pièges

- **Mémoire qui enfle** : sans tri ni invalidation, les souvenirs s'accumulent (bruit, coût, contexte saturé) — cf. [[Agent memory]].
- **Cloisonnement** : isoler la mémoire par utilisateur, sinon fuite de données d'une session à l'autre.
- Versions **0.x** et API en évolution rapide — épingler les versions.

## Alternatives

- [[Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.
- [[OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

## Liens

- Implémente directement le concept [[Agent memory]] — mémoire hiérarchique façon OS, héritée de **MemGPT** (Packer et al., 2023).
- Même famille de **frameworks d'agents** que [[CrewAI]], [[Agno]], [[OpenAI Agents SDK]], [[smolagents]], [[AutoGen]], et la couche d'orchestration [[LangGraph]].
- Concepts : [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Multi-agent systems]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://docs.letta.com/
