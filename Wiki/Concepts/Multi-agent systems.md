---
galaxie: wiki
type: concept
nom: Multi-agent systems
alias: [systèmes multi-agents, multi-agent systems, MAS]
categorie: concept/llm
domaines: [ai-eng]
tags: [multi-agent, agents, llm]
---

# Multi-agent systems

## Aperçu

- Plusieurs **agents LLM** qui se coordonnent pour une tâche, chacun avec son rôle et ses outils, plutôt qu'un seul agent monolithique.
- Promesse : spécialisation et parallélisme. Rançon : coût, latence et coordination en plus.

## Concepts clés

### Topologies
- **Superviseur** (un orchestrateur délègue à des exécutants), **hiérarchique** (superviseurs de superviseurs), **conversationnel** (GroupChat : agents qui discutent), **séquentiel** (pipeline de rôles : recherche → rédaction → revue).

### Coordination & communication
- Les agents échangent par **messages** ; il faut un protocole (qui parle, quand s'arrêter) et un **état partagé**. Sans cadrage, ils tournent en rond ou se répètent.

### Spécialisation
- Découper par rôle (chercheur, codeur, critique) améliore la qualité **quand les compétences diffèrent vraiment** ; inutile si les sous-tâches sont homogènes.

### Quand un seul agent suffit
- Le multi-agents n'aide que si la tâche se décompose en rôles distincts et faiblement couplés. Sinon, un agent unique bien outillé est plus simple et moins cher.

## Les maths, simplement

- Communication tout-à-tous entre $n$ agents : $\binom{n}{2} = \dfrac{n(n-1)}{2}$ canaux, soit une croissance **quadratique** ; le coût en tokens grimpe d'autant que chacun voit les échanges des autres.
- Intuition : ajouter un agent n'ajoute pas un coût constant — d'où les topologies en **étoile** (superviseur) qui ramènent la communication à $O(n)$.

## En pratique

- Commencer **mono-agent** ; passer multi-agents seulement quand un goulot (rôles incompatibles, contexte trop large pour un seul) le justifie.
- Préférer une topologie **superviseur** (étoile) au tout-à-tous : moins de canaux, flux contrôlable, arrêt explicite.
- Outillage : [[Dev/Services/CrewAI|CrewAI]] (équipes de rôles, Crews/Flows), [[Dev/Services/AutoGen|AutoGen]] (agents conversationnels, GroupChat — en maintenance, cf. sa fiche), [[Dev/Services/LangGraph|LangGraph]] (graphe multi-agents à état explicite).
- Pièges : explosion des coûts/latence ; boucles de conversation sans fin ; erreurs qui se propagent d'un agent à l'autre sans contrôle.

## Approches voisines & alternatives

- [[Agent patterns]] — le patron orchestrateur-exécutants est la porte d'entrée du multi-agents.
- [[agent-loops]] — chaque agent fait tourner sa propre boucle.
- [[Tool use patterns]] — un sous-agent peut être exposé comme un simple outil à un autre.
- [[Agent memory]] — l'état partagé entre agents est un problème de mémoire.
- [[Agent evaluation]] — évaluer une équipe d'agents : à qui imputer l'échec ?
- [[mcp-protocol]] — outils et ressources partagés entre agents via des serveurs MCP.
- [[Reliability patterns]] — contenir la propagation d'erreurs d'un agent à l'autre.
- Alternative : **un agent unique avec plusieurs outils** — souvent suffisant, toujours moins cher ; ne passer au multi-agents qu'avec une raison mesurée.

## Pour aller plus loin

- Wu et al. (2023) — *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*.
- Anthropic (2024) — *Building Effective Agents* (orchestrateur-exécutants, quand ne pas multiplier les agents).
