---
role: brique
nom: Vikunja
alias: [vikunja, go-vikunja/vikunja]
pitch: "Application web de gestion de tâches à héberger (AGPL-3.0 ou ultérieure, Go et Vue.js), livrée en un seul binaire ou conteneur : projets et sous-projets, tâches avec rappels et répétitions, partage entre utilisateurs, vues liste, Gantt, tableau et Kanban, API documentée — mais l'administration, le journal d'audit et le suivi du temps relèvent de la version payante Vikunja Pro."
categorie: devtools/projet
famille: application
domaines: [ai-eng]
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: single-node
alternatives: ["[[Kanboard]]", "[[Redmine]]"]
complements: []
tags: [issue-tracking, project-management, self-hosted]
url_docs: https://vikunja.io/docs/
url_repo: https://github.com/go-vikunja/vikunja
---

# Vikunja

<!-- AUTO:BANDEAU:START -->
> Application web de gestion de tâches à héberger (AGPL-3.0 ou ultérieure, Go et Vue.js), livrée en un seul binaire ou conteneur : projets et sous-projets, tâches avec rappels et répétitions, partage entre utilisateurs, vues liste, Gantt, tableau et Kanban, API documentée — mais l'administration, le journal d'audit et le suivi du temps relèvent de la version payante Vikunja Pro.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Go | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Gestionnaire de tâches, pensé comme « le carnet où l'on garde tout » : des **projets** (avec sous-projets), des tâches avec échéance, rappel, répétition (« chaque semaine »), sous-tâches, étiquettes, personnes assignées, et une saisie rapide qui lit les dates et les mots-clés dans le titre (« Quick Add Magic »). Chaque projet s'affiche en **liste**, en **diagramme de Gantt**, en **tableau** ou en **Kanban**. Un projet se partage avec une personne ou une équipe. L'architecture tient en deux parties, l'API et l'interface, **empaquetées dans un seul binaire ou conteneur** : une seule chose à installer. Une API documentée (OpenAPI), une application de bureau (l'interface web emballée) et une application mobile limitée aux fonctions de base existent.

**Licences.** La plus grande partie du dépôt est sous AGPL-3.0 ou ultérieure ; le dossier `desktop/` est sous GPL-3.0 ou ultérieure. L'éditeur vend aussi **Vikunja Cloud** (service hébergé, cité en texte simple) et **Vikunja Pro** (panneau d'administration, journal d'audit, suivi du temps) : le dépôt libre ne contient pas ces fonctions. Le README signale que du code est écrit avec des outils assistés par modèles de langage. Version 2.7.0 du 2026-10-02, dépôt poussé le 2026-10-07.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Une liste de tâches personnelle ou d'équipe, avec rappels et échéances, que l'on héberge | Une application de gestion de projet à plusieurs projets avec workflow de tickets configurable, wiki et dépôts : [[Redmine]] |
| Plusieurs vues d'un même projet (liste, Gantt, Kanban, tableau) sans changer d'outil | Un tableau Kanban seul, sans fioriture : [[Kanboard]] |
| Une seule chose à déployer : binaire ou conteneur, API incluse | Un tableau Kanban à la Trello avec scrum, graphiques de flux et règles automatiques : [[Wekan]] |
| Brancher des scripts ou un agent sur l'API OpenAPI | Le suivi du temps ou le journal d'audit dans l'édition libre : absents, réservés à la version Pro. Pour le temps seul, cf. [[Kimai]] |

## Mise en œuvre

- Installation — binaire, conteneur Docker, paquets Debian, RPM, Arch, Alpine, FreeBSD, Kubernetes, Ansible ; un assistant d'installation interactif sur le site
- Point d'entrée — l'interface web après lancement ; la documentation décrit la configuration, les proxys inverses, les sauvegardes et le durcissement du service systemd
- Prérequis — une base de données ; pour MySQL ou MariaDB, un codage UTF-8 (indiqué par la documentation)
- Exécution — auto-hébergé, mono-nœud ; une instance de démonstration sur try.vikunja.io
- Coût — gratuit sous AGPL-3.0 ou ultérieure ; Vikunja Cloud et Vikunja Pro sont payants

## Écosystème

### Alternatives

- [[Kanboard]] — Application web de tableau Kanban à héberger (MIT, PHP, en mode maintenance) : colonnes, limite de travail en cours, couloirs, sous-tâches, actions automatiques, API JSON-RPC, sans fioriture. — là où Vikunja offre listes, Gantt et Kanban dans une application plus large, Kanboard s'en tient au tableau.
- [[Redmine]] — Application web de gestion de projet à héberger (GPL v2 ou ultérieure, Ruby on Rails) : plusieurs projets, tickets au workflow configurable, diagramme de Gantt, wiki, suivi du temps et dépôts de code intégrés. — plus de projets, de tickets et de traçabilité ; Vikunja vise des listes de tâches plus simples.
- voisin : [[Wekan]] — un Kanban à la Trello, MIT.

## Ressources

- Documentation — https://vikunja.io/docs/
- Dépôt — https://github.com/go-vikunja/vikunja

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Comparatif - Suivi de projet auto-hébergé]] — où ces outils se départagent
- [[Backlog, Kanban, Scrum et Shape Up]] — la notion : quelle méthode choisir avant l'outil
- [[Outils de développement]] — le hub du domaine
