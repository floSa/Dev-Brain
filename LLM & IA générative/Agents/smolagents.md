---
role: brique
nom: smolagents
alias: [smolagents, smol-agents]
pitch: "Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox."
categorie: llm/agents
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[OpenAI Agents SDK]]", "[[CrewAI]]", "[[Agno]]", "[[AutoGen]]", "[[Letta]]", "[[PraisonAI]]"]
complements: []
tags: [llm, agents, tool-use, mcp]
url_docs: https://huggingface.co/docs/smolagents
url_repo: https://github.com/huggingface/smolagents
---

# smolagents

<!-- AUTO:BANDEAU:START -->
> Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'agents **minimaliste** de Hugging Face : tout le cœur tient en ~1000 lignes, donc
se lit et s'audite de bout en bout. Son parti pris est le **CodeAgent** — l'agent exprime ses
actions en **code Python exécutable** plutôt qu'en appels d'outils JSON. Cette approche réduit le
nombre d'étapes, puisque composition, boucles et logique conditionnelle vivent directement dans
le code généré, et colle mieux à la façon dont les LLM ont été entraînés. Elle a un corollaire
qui n'est pas négociable : ce code doit s'exécuter quelque part, et le `LocalPythonExecutor`
fourni **n'est pas une frontière de sécurité**. Agnostique du modèle (transformers ou Ollama en
local, fournisseurs du Hub, OpenAI et Anthropic via [[LiteLLM]]) et compatible MCP.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Vouloir un framework d'agent léger et lisible, sans cérémonie ni abstractions lourdes | **Production sans bac à sable** : exécuter du code écrit par un LLM est dangereux, et le `LocalPythonExecutor` n'isole pas — sandboxer (Docker, E2B, Modal, Blaxel) dès qu'on quitte le prototype jetable |
| Tâches où l'agent gagne à raisonner en code : manipulation de données, enchaînement d'appels, logique conditionnelle | Budget non borné : comme tout agent, les itérations peuvent s'emballer — borner les pas |
| Rester portable entre LLM, local ou API, et brancher des outils MCP | Projet à figer : bibliothèque jeune et API en évolution — épingler les versions |

## Mise en œuvre

- Installation — bibliothèque `pip` / `uv`, importée dans l'application
- Point d'entrée — API Python : `CodeAgent`, ses outils, et les serveurs MCP consommés
- Prérequis — Python, un accès LLM, et un **bac à sable** pour l'exécution du code généré : Docker, ou une offre managée (E2B, Modal, Blaxel)
- Exécution — en bibliothèque dans l'application hôte ; le code produit par l'agent, lui, s'exécute dans le bac à sable qu'on lui donne
- Coût — gratuit, Apache-2.0 ; la dépense est celle des LLM, plus le bac à sable s'il est managé

## Écosystème

### Alternatives

- [[OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.
- [[PraisonAI]] — Framework multi-agents low-code Python (MIT) — un fichier YAML déclare agents, tâches et processus sans écrire de code ; auto-réflexion des agents, mémoire et RAG intégrés, ~100 outils fournis et clients MCP (stdio, HTTP, SSE, WebSocket).

## Ressources

- Documentation — https://huggingface.co/docs/smolagents
- Dépôt — https://github.com/huggingface/smolagents

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Agent patterns]] — patrons d'architecture d'agents
- [[agent-loops]] — la boucle perception / action d'un agent
- [[Tool use patterns]] — patrons d'appel d'outils
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Agent memory]] — mémoire persistante d'agent
- [[Sandboxing de code généré]] — isoler l'exécution du code produit par un LLM
