---
role: brique
nom: Letta
alias: [letta, memgpt, mem-gpt, letta-code]
pitch: "Harnais d'agents à état (ex-MemGPT, Apache-2.0) — agents à mémoire persistante qui réécrivent eux-mêmes leur contexte et leurs skills, pilotés par CLI, application de bureau ou serveur d'application ; l'ancien serveur d'API V1 est retiré, Letta Cloud est le mode par défaut mais le mode local se passe de compte."
categorie: llm/memoire
famille: cli
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: ["[[Agno]]", "[[CrewAI]]", "[[AutoGen]]", "[[OpenAI Agents SDK]]", "[[smolagents]]", "[[OpenViking]]", "[[Mem0]]", "[[Graphiti]]", "[[Cognee]]"]
complements: []
tags: [llm, agents, tool-use]
url_docs: https://docs.letta.com/
url_repo: https://github.com/letta-ai/letta-code
---

# Letta

<!-- AUTO:BANDEAU:START -->
> Harnais d'agents à état (ex-MemGPT, Apache-2.0) — agents à mémoire persistante qui réécrivent eux-mêmes leur contexte et leurs skills, pilotés par CLI, application de bureau ou serveur d'application ; l'ancien serveur d'API V1 est retiré, Letta Cloud est le mode par défaut mais le mode local se passe de compte.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Harnais d'**agents à état**, issu du projet de recherche **MemGPT** (Berkeley) dont il garde
le nom d'origine. Depuis 2026, le produit actif est **Letta Code** : un agent qui garde sa
mémoire, son identité et ses compétences d'une session à l'autre, et qui **réécrit lui-même**
son contexte (blocs de mémoire, skills, prompt système) ; la mémoire est un système de
fichiers versionné par git (MemFS). Il se pilote par CLI, application de bureau, navigateur ou
messagerie. **L'ancien serveur d'API V1 est
retiré** : le README du dépôt `letta` le renvoie à une branche `archive` et à `letta-code`.
Letta Cloud est le mode **par défaut** ; le mode local fonctionne sans compte, mais les
ordinateurs distants et les secrets partagés exigent une connexion à Letta.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un agent **longue durée** doit apprendre d'un projet ou d'un utilisateur — assistant personnel, copilote de code, agent toujours actif — avec la mémoire comme **primitive de première classe** | Il faut une **brique de mémoire** à brancher sur un agent déjà écrit, avec `add` et `search` → [[Mem0]], [[Cognee]] |
| Le mode **local** convient : la doc cite Ollama, LM Studio, llama.cpp et tout point d'accès compatible Chat Completions avec appel d'outils ; aucun compte Letta requis | Le besoin est une **API stateful** servie à des applications tierces, comme le faisait l'ancien serveur V1 : ce serveur est retiré |
| L'équipe accepte un agent qui modifie son propre contexte, sa mémoire restant versionnée par git | Des faits **datés**, à interroger dans le temps → [[Graphiti]] |
| | Orchestration **multi-agents en rôles** comme primitive centrale → [[CrewAI]], [[Agno]] ; contrôle fin du graphe d'exécution → [[LangGraph]] |
| | Cadence de versions élevée (v0.34.1, plusieurs versions par jour fin septembre 2026) : épingler la version |

## Mise en œuvre

- Installation — `npm install -g @letta-ai/letta-code`, ou `uv tool install letta` (le paquet PyPI embarque l'environnement Node.js) ; constat du 2026-10-01 : v0.34.1 du 2026-09-30 (npm et PyPI), 3,5 k étoiles pour `letta-code` et 25 k pour le dépôt historique `letta`, dont le dernier commit date de 2026-09-10
- Point d'entrée — la commande `letta` (interface terminal) ; `letta server` pour le serveur d'application local ou auto-hébergé ; application de bureau (macOS, Windows, Linux) ; Agent SDK TypeScript
- Prérequis — Letta Cloud est le défaut au premier lancement : choisir « local » (`letta backend local`) pour rester on-prem ; configurer le fournisseur de modèle avec `/connect`. Sous Windows natif, la réflexion automatique côté client est désactivée par défaut
- Exécution — local sans compte, ou Cloud pour partager la mémoire entre machines ; canaux Slack, Telegram, Discord, WhatsApp et Signal documentés pour les agents locaux
- Coût — gratuit sous Apache-2.0 (code de `letta-code` lu dans son fichier LICENSE) : usage chez un client, embarquement et service hébergé permis, avec conservation des mentions ; le coût réel est dominé par les appels LLM, auxquels la gestion de mémoire en ajoute

## Écosystème

### Alternatives

- [[Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.
- [[OpenViking]] — Base de contexte auto-évolutive pour agents (Volcengine/ByteDance, AGPL-3.0) — mémoires, documents et skills exposés en système de fichiers `viking://` parcourable, avec chargement en trois niveaux de détail pour maîtriser le budget de tokens.

- [[Mem0]] — Couche de mémoire pour agents LLM (Apache-2.0, open-core) — un LLM extrait les faits d'une conversation, rangés par utilisateur, agent ou session dans un vector store, puis retrouvés par recherche ; la mémoire graphe, les webhooks et l'export sont réservés à la plateforme hébergée.
- [[Graphiti]] — Framework de graphe de connaissances temporel pour agents (Zep, Apache-2.0) — extrait par LLM entités et faits d'épisodes, chaque fait portant sa fenêtre de validité ; recherche hybride vecteur, BM25 et graphe sur Neo4j, FalkorDB ou Neptune. La plateforme Zep n'existe plus que dans le cloud.
- [[Cognee]] — Moteur de mémoire pour agents (Topoteretes, Apache-2.0) — ingère documents et conversations, en tire un graphe de connaissances et un index vectoriel, puis les interroge ; pile locale SQLite, LanceDB et Kuzu par défaut, accès par jeu de données avec rôles ; version 1.x classée beta.

## Ressources

- Documentation — https://docs.letta.com/
- Dépôt — https://github.com/letta-ai/letta-code
- Dépôt — historique, serveur V1 retiré (branche `archive`) : https://github.com/letta-ai/letta
- Documentation — auto-hébergement : https://docs.letta.com/self-hosting/index.md

## Voir aussi

- [[Agent memory]] — la notion qu'il implémente directement, héritée de MemGPT (Packer et al., 2023)
- [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Multi-agent systems]] — les notions voisines
- [[LLM & IA générative]] — le hub du domaine
