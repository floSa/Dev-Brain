---
galaxie: dev
type: service
nom: AutoGen
alias: [autogen, microsoft-autogen]
pitch: "Framework multi-agents de Microsoft Research — agents conversationnels qui collaborent et appellent des outils ; en maintenance depuis fin 2025 (successeur : Microsoft Agent Framework ; fork communautaire : AG2)."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: deprecated
langage: "Python, .NET"
scaling: single-node
alternatives: ["[[Dev/Services/CrewAI|CrewAI]]", "[[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]]", "[[Dev/Services/Agno|Agno]]", "[[Dev/Services/smolagents|smolagents]]", "[[Dev/Services/Letta|Letta]]"]
remplace_par: []
status: actif
tags: [llm, agents, tool-use, multi-agent]
url_docs: https://microsoft.github.io/autogen/
url_repo: https://github.com/microsoft/autogen
---

# AutoGen

## Pourquoi

Framework **multi-agents** issu de **Microsoft Research**, popularisé par son modèle d'**agents conversationnels** : plusieurs agents (assistant, exécuteur de code, proxy utilisateur…) échangent des messages, se répartissent les sous-tâches et appellent des **outils** pour résoudre un problème. La réécriture 0.4 a introduit une architecture asynchrone et événementielle. AutoGen a fortement influencé la catégorie (le « GroupChat » est devenu une référence). Code sous licence **MIT** (docs en CC-BY-4.0).

⚠️ **Statut 2026** : le dépôt `microsoft/autogen` est officiellement **en maintenance** depuis fin 2025 — *« will not receive new features… community managed going forward »*. Microsoft oriente les nouveaux projets vers **Microsoft Agent Framework** (fusion d'AutoGen et de [[Dev/Services/Semantic Kernel|Semantic Kernel]]). En parallèle, une partie de la communauté maintient le **fork AG2** (`ag2ai/ag2`), compatible avec le style v0.2. Trois projets coexistent donc : AutoGen (legacy), AG2 (fork communautaire), Agent Framework (successeur Microsoft).

## Quand l'utiliser

- **Maintenir / comprendre** une base de code existante déjà bâtie sur AutoGen.
- Prototyper rapidement un schéma **multi-agents conversationnel** dont on connaît déjà les idiomes.

## Quand NE PAS l'utiliser

- **Nouveau** projet : préférer **Microsoft Agent Framework** (successeur) ou, hors écosystème Microsoft, [[Dev/Services/CrewAI|CrewAI]] / [[Dev/Services/LangGraph|LangGraph]].
- Besoin de **garanties de support et d'évolution** : le dépôt est en maintenance, pas de nouvelles fonctionnalités.

## Déploiement & coût

- Open-source (MIT), gratuit ; bibliothèque importée dans l'app (`pip` / NuGet), aucune infra propre.
- Coût réel dominé par les appels aux **LLM** ; un agent exécuteur de code nécessite un **bac à sable** (conteneur) à sécuriser et provisionner.
- Scaling = celui de l'application hôte (single-node).

## Pièges

- **Legacy** : construire du neuf dessus expose à l'absence de correctifs et d'évolutions — bien arbitrer AutoGen vs AG2 vs Agent Framework.
- **Confusion de versions** : 0.2 (GroupChat historique), 0.4 (refonte), AG2 (fork) — les exemples du web ne ciblent pas tous la même API.
- Boucles d'agents **coûteuses et difficiles à borner** : conversations qui s'emballent, dépenses LLM non maîtrisées sans garde-fous.

## Alternatives

- [[Dev/Services/CrewAI|CrewAI]] — Framework multi-agents Python autonome (indépendant de LangChain) — orchestre des agents en rôles via des Crews et des Flows ; open-source avec une plateforme Enterprise managée pour la production.
- [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]] — SDK d'agents léger d'OpenAI (MIT), successeur de Swarm passé en production — primitives minimales (agents, handoffs, guardrails, sessions, tracing intégré) ; Python et TypeScript, agnostique du fournisseur.
- [[Dev/Services/Agno|Agno]] — Framework d'agents Python haute performance (ex-phidata, Apache-2.0) — instanciation d'agent ultra-légère, mémoire/connaissance/raisonnement intégrés ; livré avec AgentOS, runtime self-host pour la production.
- [[Dev/Services/smolagents|smolagents]] — Bibliothèque d'agents minimaliste de Hugging Face (Apache-2.0) — l'agent écrit ses actions en code Python plutôt qu'en JSON (CodeAgent) ; cœur en ~1000 lignes, agnostique du LLM (LiteLLM) et compatible MCP.
- [[Dev/Services/Letta|Letta]] — Framework d'agents stateful (ex-MemGPT, Apache-2.0) — mémoire persistante hiérarchique façon OS qui s'auto-édite entre sessions ; l'agent apprend dans la durée, via API et serveur self-host ou Letta Cloud.

## Liens

- **Successeur** : Microsoft Agent Framework — fusion d'AutoGen et de [[Dev/Services/Semantic Kernel|Semantic Kernel]] ; nouveau socle Microsoft pour agents et workflows multi-agents.
- **Fork communautaire** : AG2 (`ag2ai/ag2`) — continuité open-source du projet hors Microsoft.
- Même famille de **frameworks d'agents** que [[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/OpenAI Agents SDK|OpenAI Agents SDK]], [[Dev/Services/Agno|Agno]], [[Dev/Services/smolagents|smolagents]], [[Dev/Services/Letta|Letta]] et la couche d'orchestration [[Dev/Services/LangGraph|LangGraph]].
- Concepts : [[Multi-agent systems]], [[Agent patterns]], [[agent-loops]], [[Tool use patterns]], [[Agent memory]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://microsoft.github.io/autogen/
