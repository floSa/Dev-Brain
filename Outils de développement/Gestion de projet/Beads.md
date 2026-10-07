---
role: brique
nom: Beads
alias: [beads, bd, gastownhall/beads, steveyegge/beads]
pitch: "Outil en ligne de commande (MIT, Go) qui tient les tâches d'un projet comme un graphe de dépendances dans une base Dolt, pour que des agents trouvent le travail prêt, le réclament de façon atomique et gardent la mémoire d'un long chantier — mais ce n'est pas un fichier lisible dans le dépôt : la base se synchronise par `bd dolt push` et `pull`, et le fichier JSONL n'est qu'un export."
categorie: devtools/projet
famille: cli
domaines: [ai-eng]
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[Backlog.md - l'outil]]"]
complements: []
tags: [project-management, agents]
url_docs: https://beads.gascity.com
url_repo: https://github.com/gastownhall/beads
---

# Beads

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande (MIT, Go) qui tient les tâches d'un projet comme un graphe de dépendances dans une base Dolt, pour que des agents trouvent le travail prêt, le réclament de façon atomique et gardent la mémoire d'un long chantier — mais ce n'est pas un fichier lisible dans le dépôt : la base se synchronise par `bd dolt push` et `pull`, et le fichier JSONL n'est qu'un export.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande, `bd`, qui sert de **mémoire structurée** à un agent de code : au lieu de plans écrits en Markdown, un graphe de tâches (les « beads ») avec des liens de dépendance (`blocks`, `related`, `parent-child`, `relates-to`, `duplicates`, `supersedes`). `bd ready` liste les tâches sans bloqueur ouvert, `bd update <id> --claim` en réserve une de façon atomique (assigne et passe en cours), `bd close` la clôt et libère celles qui l'attendaient. Les identifiants sont des empreintes (`bd-a1b2`, puis `bd-a1b2.1` pour une sous-tâche), ce qui évite les collisions quand plusieurs agents ou branches créent des tâches en parallèle. La sortie est en JSON pour les agents, et une « compaction » résume les anciennes tâches closes pour économiser le contexte.

**Où vivent les données.** Pas dans des fichiers Markdown : dans une base [Dolt](https://github.com/dolthub/dolt), un SQL versionné avec fusion au niveau de la cellule. Par défaut elle est **embarquée** (dans `.beads/embeddeddolt/`, un seul écrivain) ; `bd init --server` se connecte à un `dolt sql-server` pour plusieurs écrivains. La synchronisation entre machines passe par `bd dolt push` et `pull` vers une référence de votre dépôt git ; `.beads/issues.jsonl` est un export, ni la source de vérité ni une sauvegarde. Version 1.3.1 du 2026-09-30, licence MIT lue dans le dépôt, dépôt poussé le 2026-10-07. Le dépôt est passé de `steveyegge/beads` à `gastownhall/beads`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un long chantier confié à un ou plusieurs agents, où l'ordre des tâches et leurs blocages comptent | Des tâches qu'un humain veut relire dans une pull request : [[Backlog.md - l'outil]] écrit des fichiers Markdown, relisibles dans le diff |
| Des agents en parallèle qui doivent se répartir le travail sans collision : identifiants par empreinte, réservation atomique | Un seul agent, une courte tâche : un fichier de contexte suffit (cf. [[Fichiers de contexte pour agents]]) |
| Garder une mémoire de projet que l'agent relit au début de chaque session (`bd prime`, `bd remember`) | Une équipe sans appétit pour une base à synchroniser : le README donne un guide de mise à niveau avec migration de schéma et une garde de version contre un binaire trop vieux |
| Travailler sans écrire dans le dépôt commun : `bd init --stealth`, ou sans git du tout avec `BEADS_DIR` | Un tableau Kanban partagé entre personnes : [[Vikunja]], [[Wekan]] ou [[Kanboard]] |

## Mise en œuvre

- Installation — `brew install beads`, `npm install -g @beads/bd`, ou le script d'installation du dépôt ; les sommes de contrôle des versions sont vérifiées par le script. À installer une fois, pas à cloner dans le projet
- Point d'entrée — `bd init` dans le projet, qui crée ou met à jour `AGENTS.md` ; `bd setup claude`, `bd setup codex` et d'autres installent les crochets de chaque agent
- Prérequis — aucun pour la base embarquée ; Dolt serveur seulement pour plusieurs écrivains
- Exécution — sur le poste ; macOS, Linux, Windows et FreeBSD d'après le README. Un serveur MCP (`beads-mcp`) existe sur PyPI
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- [[Backlog.md - l'outil]] — Outil en ligne de commande (MIT, TypeScript) qui range les tâches d'un projet en fichiers Markdown dans le dépôt, avec critères d'acceptation, jalons et dépendances, un Kanban dans le terminal ou le navigateur et un accès pour les agents par instructions ou MCP — mais il n'y a ni serveur ni compte, donc rien ne se partage hors de git. — là où Beads garde un graphe que les agents interrogent, Backlog.md garde des fichiers que l'humain relit.
- voisin : [[Vibe Kanban]] — application locale qui lance un agent par carte ; elle pilote des agents, elle ne tient pas leur mémoire de tâches.

## Ressources

- Documentation — https://beads.gascity.com
- Dépôt — https://github.com/gastownhall/beads

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Backlog, Kanban, Scrum et Shape Up]] — la notion : le Kanban en solo et avec des agents
- [[Fichiers de contexte pour agents]] — le `AGENTS.md` que `bd init` écrit
- [[Branches courtes et worktrees pour agents]] — plusieurs agents sur un même dépôt
- [[Outils de développement]] — le hub du domaine
