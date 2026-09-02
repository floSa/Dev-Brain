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

## Pourquoi

Bibliothèque d'agents **minimaliste** de **Hugging Face** : tout le cœur tient en ~1000 lignes. Son parti pris : le **CodeAgent** — l'agent exprime ses actions en **code Python exécutable** plutôt qu'en appels d'outils JSON. Cette approche réduit le nombre d'étapes (composition, boucles et logique directement dans le code généré) et colle mieux à la façon dont les LLM ont été entraînés. **Agnostique du modèle** (transformers/Ollama en local, fournisseurs du Hub, OpenAI/Anthropic via [[LiteLLM]]) et **compatible MCP** (consomme les outils de n'importe quel serveur MCP). Licence **Apache-2.0**.

## Quand l'utiliser

- Vouloir un framework d'agent **léger et lisible**, sans cérémonie ni abstractions lourdes.
- Tâches où l'agent gagne à **raisonner en code** (manipulation de données, enchaînement d'appels, logique conditionnelle).
- Rester **portable** entre LLM (local ou API) et brancher des outils **MCP**.

## Quand NE PAS l'utiliser

- Besoin d'orchestration **multi-agents structurée** en rôles/équipes → [[CrewAI]] / [[Agno]].
- Besoin d'**état durable** et de reprise (checkpoints, human-in-the-loop) → [[LangGraph]].
- Production sans **sandbox** : le `LocalPythonExecutor` n'est **pas** une frontière de sécurité (cf. Pièges).

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; bibliothèque `pip`/`uv` importée dans l'app, aucune infra propre.
- Coût dominé par les appels **LLM**.
- L'exécution de code généré exige un **bac à sable** : Docker, ou offres managées (E2B, Modal, Blaxel) — à provisionner et sécuriser.

## Pièges

- **Sécurité** : exécuter du code écrit par un LLM est dangereux ; `LocalPythonExecutor` n'isole pas — sandboxer (Docker/E2B/…) dès qu'on quitte le prototype jetable.
- **Coûts/boucles** : comme tout agent, les itérations peuvent s'emballer — borner les pas.
- Bibliothèque **jeune** et API en évolution — épingler les versions.

## Alternatives

- [[OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.
- [[PraisonAI]] — Framework multi-agents low-code Python (MIT) — un fichier YAML déclare agents, tâches et processus sans écrire de code ; auto-réflexion des agents, mémoire et RAG intégrés, ~100 outils fournis et clients MCP (stdio, HTTP, SSE, WebSocket).

## Liens

- Même famille de **frameworks d'agents** que [[OpenAI Agents SDK]], [[CrewAI]], [[Agno]], [[AutoGen]], [[Letta]], [[PraisonAI]] et la couche d'orchestration [[LangGraph]].
- Route ses appels via [[LiteLLM]] (abstraction multi-fournisseurs).
- Concepts : [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Multi-agent systems]], [[Agent memory]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://huggingface.co/docs/smolagents
