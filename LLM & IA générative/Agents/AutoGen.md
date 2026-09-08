---
role: brique
nom: AutoGen
alias: [autogen, microsoft-autogen]
pitch: "Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2)."
categorie: llm/agents
famille: paquet
licence_type: open-source
maturite: deprecated
langage: "Python, .NET"
alternatives: ["[[CrewAI]]", "[[OpenAI Agents SDK]]", "[[Agno]]", "[[smolagents]]", "[[Letta]]", "[[swarm-forge]]", "[[PraisonAI]]"]
complements: []
tags: [llm, agents, tool-use, multi-agent]
url_docs: https://microsoft.github.io/autogen/
url_repo: https://github.com/microsoft/autogen
---

# AutoGen

<!-- AUTO:BANDEAU:START -->
> Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python, .NET | open-source | en bibliothèque, rien à héberger | deprecated | à jour · 2026-06-30 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework **multi-agents** issu de Microsoft Research, popularisé par son modèle d'**agents
conversationnels** : plusieurs agents — assistant, exécuteur de code, proxy utilisateur —
échangent des messages, se répartissent les sous-tâches et appellent des **outils** pour résoudre
un problème. La réécriture 0.4 a introduit une architecture asynchrone et événementielle. Le
« GroupChat » d'AutoGen a fait la catégorie et l'a fortement influencée. Le dépôt
`microsoft/autogen` est **en maintenance depuis fin 2025** — *« will not receive new features…
community managed going forward »* — et trois projets coexistent désormais : AutoGen (legacy),
le fork communautaire **AG2** (`ag2ai/ag2`, compatible avec le style v0.2), et **Microsoft Agent
Framework**, fusion d'AutoGen et de [[Semantic Kernel]], vers lequel Microsoft oriente les
nouveaux projets.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Maintenir ou comprendre une base de code existante déjà bâtie sur AutoGen | Nouveau projet : le dépôt n'aura plus de fonctionnalités, et l'arbitrage AutoGen / AG2 / Agent Framework est à faire avant d'écrire une ligne |
| Prototyper rapidement un schéma multi-agents conversationnel dont on connaît déjà les idiomes | Besoin de garanties de support et d'évolution : maintenance seule, pas de nouvelles fonctionnalités |
| | Suivre des exemples trouvés sur le web : 0.2 (GroupChat historique), 0.4 (refonte) et AG2 (fork) ne ciblent pas la même API |
| | Budget non borné : les boucles d'agents conversationnels s'emballent et sont difficiles à borner |

## Mise en œuvre

- Installation — bibliothèque importée dans l'application (`pip` pour Python, NuGet pour .NET)
- Point d'entrée — API d'agents conversationnels ; le GroupChat comme primitive d'orchestration
- Prérequis — Python ou .NET, un accès LLM, et un **bac à sable** (conteneur) dès qu'un agent exécuteur de code entre en jeu
- Exécution — en bibliothèque dans l'application hôte, mono-nœud ; le scaling est celui de l'hôte
- Coût — gratuit, MIT (documentation en CC-BY-4.0) ; la dépense réelle est celle des LLM, à border explicitement

## Écosystème

### Alternatives

- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.
- [[Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.
- [[swarm-forge]] — Orchestrateur tmux d'agents de code (Robert C. Martin, Clojure/Babashka) : chaque agent travaille dans son propre git worktree et passe le relais par handoffs asynchrones validés par une porte d'audit ; aucune licence déclarée.
- [[PraisonAI]] — Framework multi-agents low-code Python (MIT) — un fichier YAML déclare agents, tâches et processus sans écrire de code ; auto-réflexion des agents, mémoire et RAG intégrés, ~100 outils fournis et clients MCP (stdio, HTTP, SSE, WebSocket).

## Ressources

- Documentation — https://microsoft.github.io/autogen/
- Dépôt — https://github.com/microsoft/autogen

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Agent patterns]] — patrons d'architecture d'agents
- [[agent-loops]] — la boucle perception / action d'un agent
- [[Tool use patterns]] — patrons d'appel d'outils
- [[Agent memory]] — mémoire persistante d'agent
