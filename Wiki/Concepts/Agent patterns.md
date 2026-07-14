---
galaxie: wiki
type: concept
nom: Agent patterns
alias: [patrons d'agents, agent design patterns, agentic patterns]
categorie: concept/llm
domaines: [ai-eng]
tags: [agents, llm, tool-use]
---

# Agent patterns

## Aperçu

- Catalogue des structures récurrentes pour bâtir un **agent LLM** : comment enchaîner raisonnement, appels d'outils et décisions pour accomplir une tâche.
- Page chapeau : chaque patron répond à un besoin (autonomie, fiabilité, coût) ; les pages voisines détaillent les briques mobilisées.

## Concepts clés

### ReAct (raisonner + agir)
- Alterne **pensée** (raisonnement explicite) et **action** (appel d'outil), en observant le résultat avant l'étape suivante. Socle de la plupart des agents — cf. [[agent-loops]].

### Plan-and-execute
- **Planifier** d'abord la suite d'étapes, **exécuter** ensuite, re-planifier si besoin. Moins d'appels de raisonnement et meilleure traçabilité ; rigide quand l'environnement change en cours de route.

### Reflexion / self-critique
- L'agent **juge sa propre sortie** et recommence si elle est insuffisante (critique → révision). Gagne en qualité, coûte des tokens et des tours.

### Routing
- Un nœud **classe** la requête et la dirige vers le bon sous-agent ou la bonne chaîne. Réduit le coût en évitant le gros modèle quand un petit suffit.

### Orchestrateur–exécutants (supervisor/worker)
- Un agent **superviseur** décompose la tâche et délègue à des **exécutants** spécialisés. Bascule vers [[Multi-agent systems]] dès que les exécutants sont eux-mêmes des agents.

## Les maths, simplement

- Coût d'un run = somme des appels LLM : $C = \sum_{t=1}^{T} \big(\text{tok}^{\text{in}}_t + \text{tok}^{\text{out}}_t\big)\,c_{\text{tok}}$, où $T$ est le nombre d'étapes de la boucle et $c_{\text{tok}}$ le prix par token.
- Chaque patron agit sur $T$ : planifier réduit les allers-retours, réfléchir les augmente. Choisir un patron, c'est arbitrer **qualité contre $T$** (donc latence et dépense).

## En pratique

- Démarrer simple : un **ReAct** avec 2-3 outils couvre beaucoup de cas. N'ajouter planification ou réflexion que si une mesure le justifie.
- Borner les itérations et prévoir une **sortie d'échec** — sans garde-fou, la boucle s'emballe (cf. [[agent-loops]]).
- Implémentation : [[Dev/Services/LangGraph|LangGraph]] pour le contrôle fin (graphe d'états, cycles, reprise) ; [[Dev/Services/CrewAI|CrewAI]] pour l'abstraction rôles/équipe ; [[Dev/Services/LangChain|LangChain]] et [[Dev/Services/PydanticAI|PydanticAI]] pour des agents simples à typés.
- Piège : empiler les patrons (plan + réflexion + multi-agents) avant d'avoir évalué — la complexité masque les régressions.

## Approches voisines & alternatives

- [[agent-loops]] — le moteur d'exécution que ces patrons orchestrent.
- [[Tool use patterns]] — comment l'agent agit sur le monde.
- [[Agent memory]] — ce que l'agent retient entre les étapes.
- [[Multi-agent systems]] — quand un seul agent ne suffit pas.
- [[Agent evaluation]] — vérifier que ces patrons tiennent leurs promesses (taux de réussite, trajectoire).
- [[Reliability patterns]] — borner et fiabiliser la boucle que ces patrons orchestrent.
- [[Human-in-the-loop]] — patron de contrôle : un humain valide les actions à fort enjeu avant exécution.
- [[RAG]] / [[Advanced RAG]] — l'**agentic RAG** est un patron où l'agent décide quand et quoi récupérer.
- Alternative la plus simple : un **workflow déterministe** (chaîne fixe d'appels LLM) — préférable quand les étapes sont connues d'avance ; l'agent ne se justifie que si le chemin dépend des observations.

## Pour aller plus loin

- Yao et al. (2022) — *ReAct: Synergizing Reasoning and Acting in Language Models*.
- Anthropic (2024) — *Building Effective Agents* (workflows vs agents, patrons de base).
