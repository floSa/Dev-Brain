---
role: notion
nom: Deep research
alias: [recherche approfondie, deep research agent, agent de recherche approfondie]
categorie: llm/agents
domaines: [ai-eng]
tags: [agents, llm, multi-agent, retrieval, context-engineering]
---

# Deep research

## Aperçu

- La **deep research** est une application d'agent : à partir d'une **question ouverte**, l'agent mène de nombreuses recherches, lit, recoupe, puis rédige un **rapport sourcé**. Le résultat attendu est un document, pas une réponse en une ligne.
- Ce n'est pas du [[RAG]] sur un corpus fixe : l'agent **décide** quoi chercher, combien de fois, et quand s'arrêter. C'est l'*agentic RAG* de [[Agent patterns]] porté à l'échelle d'un rapport.

## Concepts clés

### Le déroulé type

La trame se retrouve d'une implémentation à l'autre. [[open_deep_research]] l'écrit comme un graphe à quatre phases :

1. **Clarifier** — demander à l'utilisateur ce qui manque avant de dépenser des recherches (`clarify_with_user`).
2. **Planifier** — transformer la demande en un **brief** de recherche (`write_research_brief`).
3. **Chercher** — un superviseur découpe le brief en unités, confiées à des chercheurs qui tournent **en parallèle** ; chacun boucle sur ses outils puis **compresse** ses trouvailles.
4. **Rédiger** — un dernier appel assemble le rapport à partir des seules trouvailles compressées.

### Pourquoi des sous-agents

- Une recherche approfondie lit énormément de matière pour peu de conclusion. C'est exactement le profil qui justifie la délégation : chaque chercheur garde ses lectures dans son contexte et ne rend qu'un résumé — cf. [[Sous-agents et isolation du contexte]].
- La compression avant de remonter n'est pas un détail : sans elle, le rapport final se rédige sur un contexte saturé.

### Quand s'arrêter

- Une recherche sans borne ne finit pas. Les implémentations combinent un **signal d'arrêt** décidé par l'agent (un outil `ResearchComplete` dans [[open_deep_research]]) et des **plafonds durs** : nombre de chercheurs simultanés, nombre d'itérations, nombre d'appels d'outils.
- Le défaut inverse existe aussi : les premiers agents de recherche d'Anthropic lançaient jusqu'à 50 sous-agents pour une question simple. L'effort doit être **proportionné à la question**, et cette règle s'écrit dans le prompt.

### Provenance et qualité des sources

- Le rapport vaut ce que valent ses sources. Anthropic relève que ses agents privilégiaient des sites optimisés pour le référencement au détriment de sources plus faisant autorité, mais moins bien classées.
- D'où l'importance de la couche de recherche (Tavily, recherche native d'un fournisseur, serveurs MCP) et d'une étape qui rattache chaque affirmation à sa source : le système d'Anthropic y consacre un agent de citation dédié.

## Les maths, simplement

- Le coût d'une recherche croît avec le **produit** du nombre de chercheurs et de leurs itérations : $C \approx U \cdot I \cdot c_{\text{tour}}$, où $U$ est le nombre d'unités de recherche, $I$ le nombre moyen d'itérations par chercheur et $c_{\text{tour}}$ le coût moyen d'un tour (appel de modèle, plus résultats de recherche lus).
- Doubler $U$ **et** $I$ quadruple la dépense. C'est pourquoi les plafonds `max_concurrent_research_units` et `max_researcher_iterations` sont les deux réglages qui pilotent le budget.
- Ordre de grandeur mesuré par Anthropic : environ 15 fois plus de tokens qu'un chat pour un système multi-agents de recherche — une recherche approfondie n'est rentable que si la question **le vaut**.

## En pratique

- **Borner d'abord** : nombre de chercheurs, itérations, budget de tokens. Les régler à partir d'un coût toléré, pas d'une qualité espérée.
- **Choisir la couche de recherche avec soin** : moteur généraliste, recherche native du fournisseur de modèle, ou serveur MCP vers une source interne. Sur un corpus privé, la recherche web n'a aucun sens.
- **Évaluer sur un jeu de questions**, pas au ressenti : le *Deep Research Bench* (score RACE) sert de banc d'essai public — [[open_deep_research]] s'y est classé 6ᵉ en août 2025. Cf. [[Agent evaluation]].
- **Relire les sources citées** : un rapport fluide peut reposer sur une source médiocre ou mal attribuée.
- Construire aujourd'hui : partir de [[Deep Agents]], dont le dépôt contient un exemple `deep_research`, plutôt que d'[[open_deep_research]], dont le dépôt est archivé et qui reste utile comme **référence d'architecture**.

## Approches voisines & alternatives

- [[RAG]] / [[Advanced RAG]] — la récupération sur un corpus indexé d'avance ; la deep research cherche en cours de route, sur des sources ouvertes.
- [[Sous-agents et isolation du contexte]] — le mécanisme qui rend la recherche parallèle et le contexte tenable.
- [[Architecture deep agent]] — le patron générique dont la deep research est le cas d'usage le plus connu.
- [[Multi-agent systems]] — la topologie superviseur / chercheurs en est un cas.
- [[Agent patterns]] — plan-and-execute et orchestrateur–exécutants y sont tous deux à l'œuvre.
- [[Agent evaluation]] — juger un rapport et sa trajectoire, pas seulement sa dernière phrase.
- [[Context engineering]] — compresser avant de remonter est une opération de contexte.
- [[mcp-protocol]] — brancher des sources de recherche spécialisées.
- Alternative : **une requête unique à un modèle avec recherche intégrée** — plus rapide et bien moins chère, suffisante quand la réponse tient en quelques faits.
- [[RAG agentique]] — le même mécanisme à l'échelle d'une question : méthodes, évaluation multi-étapes, coût

## Pour aller plus loin

- Anthropic (2025) — *How we built our multi-agent research system* : architecture orchestrateur et sous-agents, coût en tokens, modes d'échec.
- LangChain (2025) — *Open Deep Research* : article de blog, et cours *Deep Research with LangGraph* (LangChain Academy).
- *Deep Research Bench* — le classement public sur lequel les agents de recherche se comparent.
