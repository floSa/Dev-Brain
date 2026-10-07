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

- Ce dossier range surtout des **méthodes** : ce sont des notions, et la plupart des outils qu'elles citent vivent ailleurs. Y vivent seulement les outils de **suivi** auto-hébergés ([[Redmine]], [[Kanboard]]) et de **mesure** ([[ccusage]], [[ActivityWatch]], [[Kimai]]). Une méthode de conduite de projet reste ici même quand elle suppose un agent de code (règle D-R13 de la taxonomie) ; l'agent lui-même, le produit qu'on installe, est dans [[Agents de code]].
- Le fil conducteur est [[Cycle de vie d'un projet assisté par agent]] : cadrer, spécifier, planifier, implémenter, vérifier, documenter, livrer. Chaque autre page détaille une étape ou une porte de décision de ce cycle.
- Deux écoles se croisent. Celle qui **écrit d'abord** : spécification, PRD, ADR ([[Développement piloté par la spécification]], [[PRD et user stories]], [[ADR et design docs]]). Celle qui **boucle sur du vérifiable** : tests, revue, boucle courte ([[Revue, tests et définition de terminé avec un agent]], [[Boucle de Ralph]]). Les deux se combinent ; la première coûte du temps de rédaction, la seconde de la rigueur sur les tests.
- Un agent ne remplace pas la méthode : il en amplifie les défauts. Le contraste est posé dans [[Vibe coding contre ingénierie agentique]].
- La documentation du projet a sa page voisine, hors de ce dossier : [[Diátaxis et docs-as-code]].

## Choisir

- Démarrer un projet avec un agent et ne pas savoir par où commencer → [[Cycle de vie d'un projet assisté par agent]], puis la page de l'étape qui bloque.
- Choisir un skill précis pour une étape : le tableau étape, besoin, skill, jeu → [[Quel skill pour quelle étape]], qui renvoie aux jeux [[Superpowers]], [[Skills d'Addy Osmani]], [[Skills de Matt Pocock]], [[Ponytail]] et [[pm-skills]].
- Une fonctionnalité floue à cadrer → [[PRD et user stories]] ; une fois cadrée, la spécification exécutable : [[Développement piloté par la spécification]], avec [[Spec Kit]] (spécification, plan, tâches), [[OpenSpec]] (un dossier par changement sur du code existant) ou [[BMAD]] (un jeu d'agents et de workflows qui couvre tout le cycle, jusqu'aux stories ; voir [[BMAD - la méthode]] et [[BMAD - tour complet des skills]]).
- Organiser le travail, seul ou en petite équipe → [[Backlog, Kanban, Scrum et Shape Up]] : en solo, un backlog et un tableau suffisent.
- Une décision d'architecture à garder → [[ADR et design docs]] ; la structure du système à dessiner → [[Modèle C4]], avec [[Mermaid]], [[Excalidraw]], [[draw.io]] ou [[GitDiagram]] (un schéma d'un dépôt existant).
- Donner à l'agent ce qu'il ne peut pas deviner → [[Fichiers de contexte pour agents]], avec [[Context engineering]] et [[Agent skills]] pour le mécanisme ; [[i-have-adhd]] n'en contraint que le format de sortie ; [[Graphify]] et [[ai-memory]] fournissent la carte du dépôt et la mémoire entre sessions.
- Une tâche longue, bien bornée et vérifiable par test → [[Boucle de Ralph]]. Plusieurs agents en parallèle sur le même dépôt → [[Branches courtes et worktrees pour agents]] (voir aussi [[swarm-forge]] et [[t3code]]).
- Savoir si le travail de l'agent est « terminé » → [[Revue, tests et définition de terminé avec un agent]], avec [[pytest]], [[Hypothesis]], [[testcontainers]] et [[pre-commit]].
- Nommer les commits, numéroter les versions, tenir le changelog → [[Commits conventionnels, versions et changelog]], sur une forge comme [[Forgejo]] ou [[GitLab CE]].
- Mesurer si l'ensemble marche, et ce que coûtent les agents → [[Mesurer un projet - DORA, coût des agents et temps passé]].
- Suivre les tickets sur son propre serveur → [[Comparatif - Suivi de projet auto-hébergé]] : [[Kanboard]] pour un tableau Kanban seul (en mode maintenance), [[Redmine]] pour plusieurs projets avec workflows, Gantt et wiki. Jira (propriétaire) en entreprise : voir le parallèle dans [[Backlog, Kanban, Scrum et Shape Up]].
- Chiffrer ce que consomment les agents → [[ccusage]] (jetons et coût estimé, 18 agents). Savoir où passe son temps sans rien saisir → [[ActivityWatch]] (local). Déclarer et facturer du temps par client → [[Kimai]] (AGPL-3.0, plugins payants à part).

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
- [[Quel skill pour quelle étape]] — domaines : ai-eng, ml-eng
- [[Revue, tests et définition de terminé avec un agent]] — domaines : ai-eng, ml-eng, mlops
- [[Vibe coding contre ingénierie agentique]] — domaines : ai-eng, ml-eng

### Briques
- [[ActivityWatch]] — Application à installer sur le poste (MPL-2.0) qui enregistre en local l'application, la fenêtre, l'onglet de navigateur ou le fichier édité, pour savoir où passe le temps ; les données restent sur la machine.
- [[ccusage]] — Outil en ligne de commande (MIT) qui lit les journaux locaux de 18 agents de code (Claude Code, Codex, OpenCode, Goose…) et en tire jetons et coût estimé par jour, semaine, mois ou session.
- [[Kanboard]] — Application web de tableau Kanban à héberger (MIT, PHP, en mode maintenance) : colonnes, limite de travail en cours, couloirs, sous-tâches, actions automatiques, API JSON-RPC, sans fioriture.
- [[Kimai]] — Application web de suivi du temps à héberger (AGPL-3.0, PHP, Symfony) : feuilles de temps, clients et projets, tarifs, budgets, factures et API JSON, multi-utilisateur avec LDAP ou SAML.
- [[Redmine]] — Application web de gestion de projet à héberger (GPL v2 ou ultérieure, Ruby on Rails) : plusieurs projets, tickets au workflow configurable, diagramme de Gantt, wiki, suivi du temps et dépôts de code intégrés.

### Comparatifs
- [[Comparatif - Suivi de projet auto-hébergé]]
<!-- AUTO:END -->
