---
role: notion
nom: Sous-agents et isolation du contexte
alias: [sous-agents, subagents, sub-agents, isolation du contexte, context isolation]
categorie: llm/agents
domaines: [ai-eng]
tags: [agents, multi-agent, llm, context-engineering, tool-use]
---

# Sous-agents et isolation du contexte

## Aperçu

- Un **sous-agent** est une instance d'agent que l'agent principal lance pour une sous-tâche. Il travaille dans **sa propre fenêtre de contexte** et ne rend qu'un message final.
- Le gain premier n'est pas le parallélisme ni la spécialisation, c'est l'**isolation** : le travail intermédiaire — pages lues, fichiers parcourus, essais ratés — reste dans le sous-agent, et seul le résultat remonte.

## Concepts clés

### Ce qui traverse la frontière

- **Vers le sous-agent** : uniquement l'énoncé de la tâche. Il ne reçoit ni l'historique de la conversation parente ni ses résultats d'outils. Tout ce dont il a besoin — chemins de fichiers, message d'erreur, décision déjà prise — doit être écrit **dans le prompt de délégation**.
- **Vers le parent** : le **message final** du sous-agent, sous forme de résultat d'outil (`task` dans [[Deep Agents]], `Agent` dans [[Claude Agent SDK]]). Les appels et résultats intermédiaires n'arrivent pas.
- Le parent peut résumer ce message dans sa propre réponse : une consigne explicite est nécessaire pour le restituer tel quel.

### Le mode fork, exception à l'isolation

- Un sous-agent **fork** part de l'historique complet du parent au lieu d'un contexte vierge. Il continue un travail déjà entamé, au prix de l'isolation : c'est un choix, `mode: "fork"` dans [[Deep Agents]].
- Par défaut, l'isolation est la règle.

### Ce qu'on configure par sous-agent

- Un **prompt système** propre, une **description** qui guide le parent dans son choix de délégation, un sous-ensemble d'**outils**, et parfois un **modèle** différent — un petit modèle pour un tri, un grand pour un raisonnement.
- **Restreindre les outils** est aussi une sécurité : un relecteur limité à la lecture ne peut pas modifier un fichier. Dans [[Claude Agent SDK]], un outil omis n'existe simplement pas dans la session du sous-agent.
- Un sous-agent peut être un **graphe complet** : dans [[Deep Agents]], un graphe [[LangGraph]] compilé, doté d'une clé d'état `messages`, se passe comme sous-agent.

### Parallélisme et imbrication

- Plusieurs sous-agents peuvent tourner **en même temps** : les sous-tâches indépendantes coûtent alors le temps de la plus lente. [[open_deep_research]] plafonne ce parallélisme par `max_concurrent_research_units`.
- Un sous-agent peut lui-même en lancer. [[Claude Agent SDK]] borne l'imbrication (3 niveaux par défaut) et la concurrence (20 par défaut), et permet un plafond de dépense par requête.

## Les maths, simplement

- Soit $K$ sous-tâches, chacune produisant $N$ tokens de matière intermédiaire et rendant un résumé de $s$ tokens, avec $s \ll N$. Sans délégation, le contexte principal grossit d'environ $K \cdot N$ ; avec, d'environ $K \cdot s$.
- Le coût total, lui, **augmente** : chaque sous-agent paie ses propres tours, et le parent paie le prompt de délégation. Anthropic mesure, sur son système de recherche, environ 4 fois plus de tokens qu'un chat pour un agent, environ 15 fois pour un système multi-agents.
- Intuition : on n'économise pas des tokens, on **déplace** la matière hors du contexte où elle coûte le plus cher — celui qui est relu à chaque tour.

## En pratique

- **Déléguer ce qui produit beaucoup de matière pour peu de conclusion** : exploration d'un dépôt, lecture de nombreuses sources, analyse d'un gros fichier. Ne pas déléguer une tâche d'une étape.
- **Demander un résumé, pas les données brutes** : c'est ce qui fait le gain. Un sous-agent qui recopie tout ce qu'il a lu annule l'isolation.
- **Écrire une description précise et orientée action** — c'est elle que le parent lit pour choisir. Une description vague, et le parent ne délègue pas, ou délègue au mauvais.
- **Borner** : profondeur, concurrence, budget. Les premiers agents de recherche d'Anthropic ont lancé jusqu'à 50 sous-agents pour une question simple ; la règle d'effort proportionnel à la difficulté doit s'écrire **dans le prompt**.
- **Ne pas déléguer quand l'intermédiaire compte** : si le parent a besoin de voir les étapes, le contexte isolé le prive de ce qu'il cherche.
- Mises en œuvre : [[Deep Agents]], [[Claude Agent SDK]] ; sur graphe écrit à la main, [[LangGraph]] ; en application, [[open_deep_research]] (chercheurs parallèles sous un superviseur).

## Approches voisines & alternatives

- [[Multi-agent systems]] — la famille plus large. Le sous-agent en est une forme **étroite** : topologie en étoile, un seul aller-retour, aucune conversation entre agents. Les frameworks conversationnels ([[AutoGen]]) sont l'autre bout du spectre.
- [[Architecture deep agent]] — le patron qui combine sous-agents, fichiers et planification.
- [[Context engineering]] — l'isolation est une technique de gestion du budget de contexte, au même titre que le résumé et la sélection.
- [[Tool use patterns]] — un sous-agent est vu du parent comme **un outil** dont le résultat est un rapport.
- [[Agent memory]] — l'état partagé entre agents reste un problème de mémoire ; l'isolation le rend explicite en le refusant par défaut.
- [[Reliability patterns]] — une erreur du sous-agent ne doit pas se propager comme un fait dans le contexte du parent.
- [[Agent evaluation]] — évaluer un système à sous-agents pose la question de l'imputation : le parent a-t-il mal délégué, ou le sous-agent mal exécuté ?
- Alternative : **un agent unique avec plus d'outils et un résumé glissant** — moins de coût, moins de parallélisme, mais un contexte qui se remplit.

## Pour aller plus loin

- Anthropic (2025) — *How we built our multi-agent research system* : orchestrateur et sous-agents parallèles, surcoût en tokens, règles d'effort dans le prompt.
- Documentation *Subagents* de Deep Agents (LangChain) et du Claude Agent SDK — définition, modes, plafonds.
- Anthropic (2024) — *Building Effective Agents* : orchestrateur–exécutants, et quand ne pas multiplier les agents.
