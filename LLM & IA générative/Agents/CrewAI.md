---
role: brique
nom: CrewAI
alias: [crewai, crew-ai]
pitch: "Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production."
categorie: llm/agents
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[AutoGen]]", "[[OpenAI Agents SDK]]", "[[Agno]]", "[[smolagents]]", "[[Letta]]", "[[swarm-forge]]", "[[PraisonAI]]"]
complements: []
tags: [llm, agents, tool-use, multi-agent]
url_docs: https://docs.crewai.com/
url_repo: https://github.com/crewAIInc/crewAI
---

# CrewAI

<!-- AUTO:BANDEAU:START -->
> Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework **multi-agents** Python qui modélise une équipe : des **agents** dotés d'un *rôle*,
d'un *objectif* et d'outils, regroupés en **Crews** qui se répartissent des **tâches** selon un
processus séquentiel ou hiérarchique. Pour les besoins plus déterministes, les **Flows** ajoutent
une orchestration événementielle à état, combinable avec les crews. Point souvent mal compris :
CrewAI est **autonome**, réécrit de zéro et **indépendant de [[LangChain]]**, contrairement à ses
débuts. Très adopté (50k+ stars). Le cœur libre est complété par une plateforme **Enterprise**
managée — déploiement, monitoring, gouvernance — restée optionnelle.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Décrire un problème comme une **équipe de rôles** collaborant (recherche → rédaction → revue, par exemple) | L'abstraction « rôles » est trompeuse de simplicité : sans cadrage des tâches et des sorties attendues, les agents partent en boucle ou se répètent |
| Vouloir un framework multi-agents léger et lisible, sans dépendre de LangChain | Coûts et latence à tenir : comme tout système multi-agents, ils grimpent vite — borner itérations et délégations |
| Passer du proto à la prod via les Flows et, si besoin, la plateforme Enterprise managée | API en évolution — Crews d'abord, Flows ensuite : vérifier que les tutoriels ciblent la version courante |

## Mise en œuvre

- Installation — bibliothèque `pip` / `uv`, importée dans l'application
- Point d'entrée — API Python : agents (rôle, objectif, outils), Crews et tâches, Flows événementiels
- Prérequis — Python et un accès LLM ; rien d'autre pour le cœur
- Exécution — en bibliothèque dans l'application hôte ; la plateforme Enterprise, elle, est managée
- Coût — cœur gratuit sous MIT ; CrewAI Enterprise est payante et optionnelle. La dépense réelle est celle des LLM, multipliée par le nombre d'agents

## Écosystème

### Alternatives

- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.
- [[Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.
- [[swarm-forge]] — Orchestrateur tmux d'agents de code (Robert C. Martin, Clojure/Babashka) : chaque agent travaille dans son propre git worktree et passe le relais par handoffs asynchrones validés par une porte d'audit ; aucune licence déclarée.
- [[PraisonAI]] — Framework multi-agents low-code Python (MIT) — un fichier YAML déclare agents, tâches et processus sans écrire de code ; auto-réflexion des agents, mémoire et RAG intégrés, ~100 outils fournis et clients MCP (stdio, HTTP, SSE, WebSocket).

## Ressources

- Documentation — https://docs.crewai.com/
- Dépôt — https://github.com/crewAIInc/crewAI

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Agent patterns]] — patrons d'architecture d'agents
- [[agent-loops]] — la boucle perception / action d'un agent
- [[Tool use patterns]] — patrons d'appel d'outils
- [[Agent memory]] — mémoire persistante d'agent
