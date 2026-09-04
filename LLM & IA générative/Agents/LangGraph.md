---
role: brique
nom: LangGraph
alias: [langgraph, langchain-ai-langgraph]
pitch: "Bibliothèque d'orchestration d'agents stateful de l'équipe LangChain — graphes cycliques avec état persistant, reprise, human-in-the-loop et streaming ; la couche bas niveau pour agents fiables, utilisable sans LangChain."
categorie: llm/agents
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [llm, agents, tool-use]
url_docs: https://docs.langchain.com/oss/python/langgraph/overview
url_repo: https://github.com/langchain-ai/langgraph
---

# LangGraph

<!-- AUTO:BANDEAU:START -->
> Bibliothèque d'orchestration d'agents stateful de l'équipe LangChain — graphes cycliques avec état persistant, reprise, human-in-the-loop et streaming ; la couche bas niveau pour agents fiables, utilisable sans LangChain.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'orchestration d'**agents stateful**, développée par l'équipe [[LangChain]] mais
**utilisable seule**. Elle modélise un agent comme un **graphe** de nœuds (étapes) et d'arêtes
(transitions, y compris **cycliques** et conditionnelles), avec un **état partagé** persisté
entre les pas. Ce modèle bas niveau apporte ce qui manque à une simple chaîne : reprise après
interruption par checkpoints, human-in-the-loop, mémoire durable, exécution en streaming et
observabilité des transitions. Inspirée de Pregel/Beam (calcul sur graphes) et de l'API de
NetworkX, elle se situe **au-dessus de** LangChain dans le stack — LangChain fournit les briques
(modèles, outils), LangGraph orchestre leur enchaînement.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Agents non triviaux : boucles, branchements conditionnels, plusieurs outils, plusieurs étapes | **Confusion de licence à ne pas commettre** : la bibliothèque est MIT, mais le runtime serveur `langgraph-api` et la LangGraph Platform managée sont sous Elastic License 2.0 — déployer ce serveur en production demande une clé commerciale |
| Besoin d'état durable : reprise après panne, sessions longues, checkpoints | Modèle graphe + état plus exigeant : il faut penser nœuds, transitions et schéma d'état — plus de cérémonie qu'une chaîne |
| Human-in-the-loop : suspendre, faire valider ou corriger par un humain, puis reprendre | Écosystème jeune et API en évolution : épingler les versions |
| Systèmes multi-agents coordonnés, avec contrôle explicite du flux et du partage d'état | |

## Mise en œuvre

- Installation — bibliothèque importée dans l'application ; le serveur `langgraph-api` est un composant distinct
- Point d'entrée — API Python (portage JS) : nœuds, arêtes, schéma d'état, checkpointer
- Prérequis — Python, un accès LLM, et une persistance pour l'état (base ou checkpointer)
- Exécution — en bibliothèque dans l'application hôte ; le runtime serveur et la Platform managée sont un autre produit
- Coût — cœur gratuit sous MIT ; `langgraph-api` / LangGraph Platform sous Elastic License 2.0, licence commerciale requise en production. La dépense réelle reste celle des LLM, plus la persistance d'état

## Écosystème

### Alternatives

- Aucun substitut direct fiché : LangGraph est une **couche d'orchestration**, pas un framework généraliste — les frameworks généralistes du comparatif intègrent leur propre couche d'agents, plus légère et moins explicite.

## Ressources

- Documentation — https://docs.langchain.com/oss/python/langgraph/overview
- Dépôt — https://github.com/langchain-ai/langgraph

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Agent patterns]] — patrons d'architecture d'agents
- [[agent-loops]] — la boucle perception / action d'un agent
- [[Human-in-the-loop]] — la validation humaine intercalée dans la boucle
- [[Multi-agent systems]] — systèmes à plusieurs agents coopérants
- [[Tool use patterns]] — patrons d'appel d'outils
- [[Agent memory]] — mémoire persistante d'agent
