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

- Ce dossier range des **méthodes**, pas des outils : ce sont des notions, et les outils qu'elles citent vivent ailleurs. Une méthode de conduite de projet reste ici même quand elle suppose un agent de code (règle D-R13 de la taxonomie) ; l'agent lui-même, le produit qu'on installe, est dans [[Agents de code]].
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
- Une tâche longue, bien bornée et vérifiable par test → [[Boucle de Ralph]]. Plusieurs agents en parallèle sur le même dépôt → [[Branches courtes et worktrees pour agents]] (voir aussi [[swarm-forge]] et [[t3code]]).
- Savoir si le travail de l'agent est « terminé » → [[Revue, tests et définition de terminé avec un agent]], avec [[pytest]], [[Hypothesis]], [[testcontainers]] et [[pre-commit]].
- Nommer les commits, numéroter les versions, tenir le changelog → [[Commits conventionnels, versions et changelog]], sur une forge comme [[Forgejo]] ou [[GitLab CE]].
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
