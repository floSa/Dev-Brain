---
role: brique
nom: PraisonAI
alias: [praisonai, praison-ai, praisonaiagents]
pitch: "Framework multi-agents low-code Python (MIT) — un fichier YAML déclare agents, tâches et processus sans écrire de code ; auto-réflexion des agents, mémoire et RAG intégrés, ~100 outils fournis et clients MCP (stdio, HTTP, SSE, WebSocket)."
categorie: llm/agents
famille: paquet
licence_type: open-source
maturite: production
langage: "Python, JavaScript"
alternatives: ["[[CrewAI]]", "[[AutoGen]]", "[[Agno]]", "[[smolagents]]"]
complements: []
tags: [llm, agents, multi-agent, tool-use, low-code, mcp]
url_docs: https://praison.ai/docs
url_repo: https://github.com/MervinPraison/PraisonAI
---

# PraisonAI

<!-- AUTO:BANDEAU:START -->
> Framework multi-agents low-code Python (MIT) — un fichier YAML déclare agents, tâches et processus sans écrire de code ; auto-réflexion des agents, mémoire et RAG intégrés, ~100 outils fournis et clients MCP (stdio, HTTP, SSE, WebSocket).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python, JavaScript | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'agents dont le parti pris est **l'entrée low-code** : un `agents.yaml` décrit les
agents, leurs rôles, leurs tâches et le processus qui les enchaîne, et `praisonai` l'exécute. Le
SDK Python (`praisonaiagents`) reste disponible pour ce qui déborde du déclaratif — le YAML est
une porte d'entrée, pas une limite. Second trait distinctif : la couche d'**auto-réflexion**, où
un agent relit sa propre sortie et la reprend avant de la rendre, sans qu'un second agent
critique soit câblé à la main. Livre aussi mémoire et RAG intégrés, une centaine d'outils prêts à
l'emploi, et des **clients MCP** sur quatre transports. Contrairement à une idée répandue dans
les comparatifs, PraisonAI **n'enrobe ni CrewAI ni AutoGen** : c'est une implémentation
autonome, dont le YAML est le différenciateur face à des API impératives.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Décrire un système multi-agents en **configuration** plutôt qu'en code, et le versionner comme tel | L'auto-réflexion **double au moins** le nombre d'appels : gain de qualité contre coût et latence, à mesurer et non à supposer |
| Besoin d'auto-réflexion sur les sorties sans construire soi-même la boucle critique | Le YAML masque la boucle d'agent : quand elle dérape, le débogage se fait quand même dans le SDK |
| Vouloir mémoire, RAG et un large jeu d'outils **fournis** plutôt qu'assemblés | Chaîne de dépendances à garder mince : surface fonctionnelle large (mémoire, RAG, ~100 outils, UI, MCP) — installer par extras plutôt qu'en bloc |
| Brancher des serveurs MCP existants sans écrire d'adaptateur | Projet à figer : cadence de commits élevée et API mouvante, épingler les versions |
| | Préférence pour un **canvas visuel** plutôt qu'un fichier YAML → [[Langflow]] ou [[Dify]] |

## Mise en œuvre

- Installation — `pip install praisonai` (CLI + YAML) ou `pip install praisonaiagents` (SDK seul) ; installer par extras, pas en bloc
- Point d'entrée — un `agents.yaml` exécuté par la CLI `praisonai` ; le SDK Python prend le relais pour le hors-déclaratif. Interfaces optionnelles : chat léger fourni, tableau de bord multi-canaux, intégration à un constructeur visuel
- Prérequis — Python et un accès LLM ; les serveurs MCP consommés se déclarent sur quatre transports (stdio, HTTP, SSE, WebSocket)
- Exécution — en bibliothèque dans l'application hôte, ou en conteneur, mono-nœud ; exécution distante d'agents et d'outils possible via paramètres dédiés
- Coût — gratuit, MIT ; la dépense réelle est celle des LLM, et auto-réflexion comme délégation **multiplient** les appels pour une même tâche

## Écosystème

### Alternatives

- [[CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[AutoGen]] — Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2).
- [[Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour exécuter des systèmes multi-agents en production.
- [[smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP, mais l'exécution de code est à isoler en sandbox.

## Ressources

- Documentation — https://praison.ai/docs (abondante mais inégale selon les fonctionnalités ; le dépôt reste la référence)
- Dépôt — https://github.com/MervinPraison/PraisonAI

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Agent patterns]] — patrons d'architecture d'agents
- [[agent-loops]] — la boucle perception / action d'un agent
- [[Tool use patterns]] — patrons d'appel d'outils
- [[Agent memory]] — mémoire persistante d'agent
- [[mcp-protocol]] — le protocole d'exposition d'outils et de ressources
