---
role: hub
nom: Gestion de projet
alias: [project management, conduite de projet, cycle de vie logiciel, méthodes de projet]
pitch: Conduire un projet de développement, avec ou sans agent — cycle de vie, spécification, backlog, décisions, contexte, revue, versions, mesure.
domaines: [data-sci, data-eng, mlops, ml-eng, ai-eng]
tags: [project-management, spec-driven, adr, skills]
---

# Gestion de projet

> Conduire un projet de développement, avec ou sans agent — cycle de vie, spécification, backlog, décisions, contexte, revue, versions, mesure.

## Ce qu'il faut comprendre

- Ce dossier range d'abord des **méthodes** (des notions), puis les **outils qui les servent autour de l'agent** : contexte du dépôt, agents en parallèle, revue, versions et changelog, commandes du projet. Une méthode ou un outil de conduite de projet reste ici même quand il suppose un agent de code (règle D-R13 de la taxonomie) ; l'agent lui-même, le produit qu'on installe, est dans [[Agents de code]], et l'outil de documentation du dépôt a sa page voisine ci-dessous.
- Le fil conducteur est [[Cycle de vie d'un projet assisté par agent]] : cadrer, spécifier, planifier, implémenter, vérifier, documenter, livrer. Chaque autre page détaille une étape ou une porte de décision de ce cycle.
- Deux écoles se croisent. Celle qui **écrit d'abord** : spécification, PRD, ADR ([[Développement piloté par la spécification]], [[PRD et user stories]], [[ADR et design docs]]). Celle qui **boucle sur du vérifiable** : tests, revue, boucle courte ([[Revue, tests et définition de terminé avec un agent]], [[Boucle de Ralph]]). Les deux se combinent ; la première coûte du temps de rédaction, la seconde de la rigueur sur les tests.
- Un agent ne remplace pas la méthode : il en amplifie les défauts. Le contraste est posé dans [[Vibe coding contre ingénierie agentique]].
- La documentation du projet a sa page voisine, hors de ce dossier : [[Diátaxis et docs-as-code]].

## Choisir

- Démarrer un projet avec un agent et ne pas savoir par où commencer → [[Cycle de vie d'un projet assisté par agent]], puis la page de l'étape qui bloque.
- Une fonctionnalité floue à cadrer → [[PRD et user stories]] ; une fois cadrée, la spécification exécutable : [[Développement piloté par la spécification]], avec [[Spec Kit]] (spécification, plan, tâches) ou [[BMAD]] (un jeu d'agents et de workflows qui couvre tout le cycle, jusqu'aux stories).
- Organiser le travail, seul ou en petite équipe → [[Backlog, Kanban, Scrum et Shape Up]] : en solo, un backlog et un tableau suffisent.
- Une décision d'architecture à garder → [[ADR et design docs]] ; la structure du système à dessiner → [[Modèle C4]], avec [[Mermaid]], [[Excalidraw]], [[draw.io]] ou [[GitDiagram]] (un schéma d'un dépôt existant).
- Donner à l'agent ce qu'il ne peut pas deviner → [[Fichiers de contexte pour agents]], avec [[Context engineering]] et [[Agent skills]] pour le mécanisme ; [[i-have-adhd]] n'en contraint que le format de sortie ; [[Graphify]] et [[ai-memory]] fournissent la carte du dépôt et la mémoire entre sessions.
- Donner à l'agent le code du projet, ou à un humain le moyen de le lire → [[Repomix]] (le dépôt en un seul fichier, pour un modèle), [[Serena]] (des outils au niveau du symbole, appelés par l'agent ; GPL-3.0-or-later), [[DeepWiki-Open]] (un wiki généré, pour un lecteur). La documentation à jour des bibliothèques se sert par Context7, serveur MCP sous licence MIT dont l'index est un service hébergé fermé (Upstash), sans auto-hébergement : cité ici sans page, règle 15 du chantier ; les trois outils libres ci-dessus couvrent le besoin voisin, le code du projet lui-même.
- Une tâche longue, bien bornée et vérifiable par test → [[Boucle de Ralph]]. Plusieurs agents en parallèle sur le même dépôt → [[Branches courtes et worktrees pour agents]] (voir aussi [[swarm-forge]] et [[t3code]]) ; pour piloter ces agents depuis un tableau Kanban, une carte par agent, [[Vibe Kanban]] (la société qui l'éditait a fermé en 2026-04, le projet est tenu par la communauté). Claude Squad, Ruflo et Crystal font la même chose et n'ont pas de page.
- Savoir si le travail de l'agent est « terminé » → [[Revue, tests et définition de terminé avec un agent]], avec [[pytest]], [[Hypothesis]], [[testcontainers]] et [[pre-commit]] ; une première relecture automatique des pull requests, avant la revue humaine : [[PR-Agent]], auto-hébergeable, avec un modèle local possible.
- Nommer les commits, numéroter les versions, tenir le changelog → [[Commits conventionnels, versions et changelog]], sur une forge comme [[Forgejo]] ou [[GitLab CE]]. Les outils : [[Commitizen]] (commits guidés, version, tag, journal par commande), [[git-cliff]] (le journal et le numéro, à la forme voulue) et [[release-please]] (la release par pull request, sur GitHub) — départagés dans [[Comparatif - Versions et changelog]]. Les commandes du projet, que l'agent comme l'humain lance, s'écrivent une fois dans un `justfile` ([[just]]) ; les versions d'outils et les tâches d'un projet multi-langage dans un `mise.toml` ([[mise]]).
- Mesurer si l'ensemble marche, et ce que coûtent les agents → [[Mesurer un projet - DORA, coût des agents et temps passé]].

<!-- AUTO:START -->
### Notions
- [[ADR et design docs]] — domaines : ai-eng, mlops
- [[Backlog, Kanban, Scrum et Shape Up]] — domaines : ai-eng, data-eng, mlops
- [[Boucle de Ralph]] — domaines : ai-eng
- [[Branches courtes et worktrees pour agents]] — domaines : ai-eng, mlops
- [[Commits conventionnels, versions et changelog]] — domaines : ai-eng, mlops
- [[Cycle de vie d'un projet assisté par agent]] — domaines : ai-eng, ml-eng
- [[Développement piloté par la spécification]] — domaines : ai-eng
- [[Fichiers de contexte pour agents]] — domaines : ai-eng
- [[Mesurer un projet - DORA, coût des agents et temps passé]] — domaines : mlops, ai-eng
- [[Modèle C4]] — domaines : ai-eng, mlops, data-eng
- [[PRD et user stories]] — domaines : ai-eng, data-eng
- [[Revue, tests et définition de terminé avec un agent]] — domaines : ai-eng, ml-eng, mlops
- [[Vibe coding contre ingénierie agentique]] — domaines : ai-eng, ml-eng
<!-- AUTO:END -->
