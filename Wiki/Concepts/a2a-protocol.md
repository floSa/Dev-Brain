---
role: notion
nom: a2a-protocol
alias: [A2A, Agent2Agent, Agent-to-Agent, protocole A2A, agent card]
categorie: concept/llm
domaines: [ai-eng]
tags: [agents, multi-agent, llm, tool-use]
---

# a2a-protocol

## Aperçu

- **Agent2Agent (A2A)** est un protocole ouvert qui permet à des agents **construits séparément**, hébergés ailleurs, de se découvrir, de se déléguer des tâches et d'échanger des résultats.
- Créé par Google, donné à la **Linux Foundation** (mi-2025), spécification **v1.0** en 2026, soutenu par 150+ organisations (Google, Microsoft, AWS, Salesforce, ServiceNow).

## Concepts clés

### Le pendant horizontal de MCP

Les deux protocoles répondent à des questions différentes, et se composent plutôt qu'ils ne se concurrencent :

| | [[mcp-protocol]] | A2A |
|---|---|---|
| Relie | un agent à des **outils** | un agent à d'autres **agents** |
| Axe | vertical (agent → capacités) | horizontal (agent ↔ pair) |
| L'autre bout est | une fonction, une ressource | un système autonome, opaque |

Un même agent expose typiquement les deux : il consomme des outils par MCP et se rend joignable par A2A.

### Agent opaque

Le pari central d'A2A : un agent distant est une **boîte noire**. On ne connaît ni son modèle, ni ses prompts, ni son outillage interne — seulement ce qu'il annonce savoir faire. Cette opacité est délibérée : elle permet la collaboration entre organisations sans exposer d'implémentation ni de propriété intellectuelle.

C'est aussi ce qui rend la délégation difficile à garantir : on ne peut pas inspecter le raisonnement de celui à qui on confie une tâche.

### Agent Card et cycle de tâche

La découverte passe par une **Agent Card** : un document publié par l'agent qui décrit son identité, ses compétences, son point d'entrée et ses modalités d'authentification. Un agent client la lit pour décider s'il délègue.

L'échange s'organise ensuite autour d'une **tâche** au cycle de vie explicite (soumise, en cours, nécessitant une entrée, terminée, échouée), avec des messages et des artefacts produits en chemin. Les tâches longues sont assumées : un agent peut travailler des minutes ou des heures et notifier en continu.

## En pratique

- Pertinent quand les agents relèvent d'**équipes ou d'organisations distinctes**. À l'intérieur d'un même système, un framework multi-agents ([[Dev/Services/CrewAI|CrewAI]], [[Dev/Services/LangGraph|LangGraph]]) reste plus simple et plus contrôlable.
- Traiter tout agent distant comme une **source non fiable** : ses réponses entrent dans le contexte local et portent le même risque qu'une entrée utilisateur — cf. [[Prompt injection]].
- L'agrégation de plusieurs agents opaques rend le débogage pénible : tracer bout en bout dès le départ, cf. [[LLM observability]].
- Adoption réelle mais jeune : [[Dev/Services/Hermes Agent|Hermes Agent]] implémente A2A v1.0 depuis août 2026.
- Piège : déléguer à un pair sans **budget ni délai maximum**. Une tâche distante qui n'aboutit pas bloque la boucle appelante.

## Approches voisines & alternatives

- [[mcp-protocol]] — l'axe vertical (outils) ; complémentaire, pas concurrent.
- [[Multi-agent systems]] — les questions de coordination qu'A2A transporte sans les résoudre.
- [[Agent patterns]] — la délégation à un pair est un patron d'organisation parmi d'autres.
- [[agent-loops]] — un appel A2A est une action de la boucle, avec sa latence et son risque d'échec.
- Alternative : exposer l'agent distant comme une **simple API HTTP** (ou un outil MCP) — moins de cérémonie, mais on perd la découverte, le cycle de tâche long et l'interopérabilité entre écosystèmes.

## Pour aller plus loin

- Spécification et implémentations : https://github.com/a2aproject/A2A
- Linux Foundation (2025) — annonce du projet Agent2Agent ; v1.0 stabilisée en 2026.
- Liés : [[Agent evaluation]], [[Human-in-the-loop]] — valider une délégation à fort enjeu avant exécution.
