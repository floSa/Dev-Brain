---
role: notion
nom: Architecture deep agent
alias: [deep agent, agent profond, agents profonds, agents à planification]
categorie: llm/agents
domaines: [ai-eng]
tags: [agents, llm, multi-agent, context-engineering, tool-use]
---

# Architecture deep agent

## Aperçu

- Un **deep agent** est un agent conçu pour les tâches **longues et à plusieurs étapes** — recherche, rédaction, développement — qu'une boucle ReAct nue ne mène pas au bout : son contexte sature avant la fin.
- Ce n'est pas un modèle plus profond, c'est un **assemblage** : une liste de tâches, un système de fichiers, des sous-agents, et une gestion active du contexte. Chacun de ces éléments existe seul ; leur combinaison est le patron.

## Concepts clés

### Le problème que le patron résout

Une boucle d'agent accumule tout dans la fenêtre : chaque appel d'outil, chaque résultat. Sur une tâche de plusieurs dizaines d'étapes, le contexte se remplit de résultats intermédiaires devenus inutiles, le modèle perd le fil, et le coût par tour grimpe. Les quatre éléments ci-dessous déplacent l'information **hors de la fenêtre** sans la perdre.

### Planification explicite

- L'agent écrit et met à jour une **liste de tâches** (l'outil `write_todos` dans [[Deep Agents]]). L'outil se contente de consigner la liste dans l'état de l'agent.
- Elle sert d'ancre : le plan reste sous les yeux du modèle à chaque tour, ce qui l'empêche de dériver. Cela reprend [[Agent patterns|plan-and-execute]], mais le plan est **révisable en cours de route**.
- Dans [[Deep Agents]], depuis la 0.7, la planification est **optionnelle** : elle était incluse par défaut avant. Le patron ne l'exige donc pas — le fichier et la délégation portent l'essentiel.

### Le système de fichiers comme mémoire de travail

- L'agent lit, écrit, édite et cherche des fichiers (`ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`). Le fichier est un **espace de travail hors fenêtre** : un résultat volumineux s'y dépose, l'agent n'en garde que le chemin et un résumé.
- Le stockage est un choix d'implémentation, pas de principe. [[Deep Agents]] propose des backends interchangeables : état en mémoire, disque local, store LangGraph, bac à sable. Le plan peut aussi y être écrit, pour survivre à une troncature du contexte.
- Un système de fichiers **virtuel** suffit : ce que le modèle voit, c'est une interface de fichiers, pas forcément un disque. Une commande shell (`execute`) est un ajout distinct, et c'est elle qui exige un bac à sable.

### Les sous-agents

- Une tâche volumineuse est **déléguée** à un agent neuf, qui travaille dans son propre contexte et ne rend qu'un rapport final. Le contexte principal ne voit pas les dizaines de pages lues pour le produire.
- C'est le levier le plus fort du patron, et il a sa propre page : [[Sous-agents et isolation du contexte]].

### Le contexte géré activement

- Les longs échanges sont **résumés**, et les sorties d'outils trop grosses déportées sur disque — c'est ce que [[Context engineering]] décrit comme compression, appliqué ici par le harnais lui-même.
- Le [[Harnais d'agent]] porte cette responsabilité : le modèle ne décide pas seul de ce qu'il garde.

## En pratique

- **À employer** quand la tâche dépasse ce qu'une fenêtre tient, ou quand elle se découpe en sous-problèmes indépendants — c'est le cas de la [[Deep research]].
- **À éviter** quand le chemin est connu d'avance ou la tâche courte : un workflow déterministe ou un ReAct à deux outils coûte moins et se débogue mieux. Le patron ajoute des outils, des instructions et des appels de délégation à chaque tour.
- **Commencer par un seul élément.** Le fichier seul soulage déjà la saturation ; ajouter la délégation seulement quand un sous-problème produit trop de matière intermédiaire.
- Mise en œuvre clé en main : [[Deep Agents]] (LangChain, agnostique du modèle) et [[Claude Agent SDK]] (mêmes ingrédients — fichiers, sous-agents — mais sur Claude uniquement). Sur un graphe écrit à la main : [[LangGraph]].
- Piège : empiler planification, fichiers, sous-agents et résumé avant d'avoir mesuré la saturation réelle — la complexité masque les régressions, comme pour tout patron d'agent.

## Approches voisines & alternatives

- [[Agent patterns]] — le catalogue dont ce patron combine plusieurs entrées : plan-and-execute, orchestrateur–exécutants, réflexion.
- [[Harnais d'agent]] — un deep agent est un harnais particulièrement fourni ; la notion décrit l'ensemble de ce que le harnais apporte.
- [[Sous-agents et isolation du contexte]] — la délégation, prise isolément.
- [[Multi-agent systems]] — quand les agents se parlent entre eux ; ici, un agent délègue et n'attend qu'un résultat.
- [[Context engineering]] — la discipline dont le patron automatise une partie.
- [[Agent memory]] — ce que l'agent retient d'une session à l'autre ; le fichier en est une forme, et [[OpenViking]] l'expose justement comme un système de fichiers.
- [[Deep research]] — le cas d'usage qui a popularisé le patron.
- Alternative : **un ReAct simple** avec deux ou trois outils — [[agent-loops]] — suffisant tant que la tâche tient dans la fenêtre.

## Pour aller plus loin

- Documentation *Deep Agents* (LangChain) — les backends, l'outil `task` et les sous-agents.
- Anthropic (2025) — *How we built our multi-agent research system* : plan sauvegardé en mémoire externe pour survivre à la troncature du contexte.
- Anthropic (2024) — *Building Effective Agents* : commencer par le plus simple qui fonctionne.
