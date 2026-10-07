---
role: brique
nom: Backlog.md - l'outil
alias: [Backlog.md, MrLesk/Backlog.md, backlog-md]
pitch: "Outil en ligne de commande (MIT, TypeScript) qui range les tâches d'un projet en fichiers Markdown dans le dépôt, avec critères d'acceptation, jalons et dépendances, un Kanban dans le terminal ou le navigateur et un accès pour les agents par instructions ou MCP — mais il n'y a ni serveur ni compte, donc rien ne se partage hors de git."
categorie: devtools/projet
famille: cli
domaines: [ai-eng]
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: ["[[Beads]]"]
complements: []
tags: [project-management, spec-driven, agents]
url_docs: https://backlog.md
url_repo: https://github.com/MrLesk/Backlog.md
---

# Backlog.md - l'outil

<!-- AUTO:BANDEAU:START -->
> Outil en ligne de commande (MIT, TypeScript) qui range les tâches d'un projet en fichiers Markdown dans le dépôt, avec critères d'acceptation, jalons et dépendances, un Kanban dans le terminal ou le navigateur et un accès pour les agents par instructions ou MCP — mais il n'y a ni serveur ni compte, donc rien ne se partage hors de git.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil en ligne de commande qui transforme un dossier en **tableau de projet** fait de fichiers Markdown. Chaque tâche est un fichier `.md` du dépôt, dans un dossier `backlog/` (ou `.backlog/`, ou un chemin réglé dans `backlog.config.yml`), avec une description, des **critères d'acceptation**, une liste de vérification « terminé » réutilisable, des jalons et des dépendances. `backlog board` dessine le Kanban dans le terminal, `backlog browser` en sert une version locale à glisser-déposer, `backlog search` cherche dans les tâches, les documents et les décisions. Pas de serveur, pas de compte, pas de télémétrie d'après le README. Git est facultatif : `backlog init --no-git` fonctionne sur de simples fichiers.

Le README en fait une méthode : trois points de relecture avant le code. Relire la **spécification** (l'agent découpe l'idée en tâches avec critères d'acceptation), relire le **plan** (l'agent l'écrit dans la tâche avant d'implémenter), puis relire le **code** (une tâche, une fenêtre de contexte, une pull request). Les tâches terminées restent dans git comme trace de ce qui a été tenté. Version 1.53.0 du 2026-09-24, licence MIT lue dans le dépôt, dépôt poussé le 2026-10-07.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Relire des tâches courtes avant que l'agent n'écrive du code, plutôt qu'un gros diff après coup (cf. [[Développement piloté par la spécification]]) | Un plan de spécification par changement, avec deltas et archivage : c'est le rôle d'[[OpenSpec]], qui se tient à côté |
| Garder le backlog **dans le dépôt**, lisible par un humain et par n'importe quel agent, sans service à héberger | Un graphe de dépendances que plusieurs agents interrogent et réclament de façon atomique : [[Beads]] est fait pour cela |
| Un Kanban sans application à installer : un terminal ou un onglet de navigateur local suffit | Un tableau partagé entre plusieurs personnes avec droits et notifications : [[Kanboard]], [[Redmine]] ou [[Vikunja]] se déploient sur site |
| Brancher l'agent par un fichier d'instructions (`backlog instructions overview`), ou par MCP si l'équipe préfère | Éditer les fichiers à la main : le README conseille les commandes (CLI, MCP, navigateur) pour garder les champs cohérents |

## Mise en œuvre

- Installation — `npm i -g backlog.md`, `bun add -g backlog.md`, `brew install backlog-md`, ou `nix run github:MrLesk/Backlog.md` ; `npx backlog.md init` pour essayer sans installer
- Point d'entrée — `backlog init "Mon projet"` dans le dépôt ; l'assistant propose des instructions pour agent (recommandé), un connecteur MCP (Claude Code, Codex, Gemini CLI, Kiro, Cursor) ou rien
- Prérequis — Node.js ou Bun pour les installations par paquet ; le paquet Nix existe pour Linux x86_64 et aarch64 et pour macOS arm64
- Exécution — sur le poste, en ligne de commande ; `backlog browser` ouvre le tableau local (`--port`, `--no-open`)
- Coût — gratuit sous licence MIT ; la dépense est celle des agents

## Écosystème

### Alternatives

- [[Beads]] — Outil en ligne de commande (MIT, Go) qui tient les tâches d'un projet comme un graphe de dépendances dans une base Dolt, pour que des agents trouvent le travail prêt, le réclament de façon atomique et gardent la mémoire d'un long chantier — mais ce n'est pas un fichier lisible dans le dépôt : la base se synchronise par `bd dolt push` et `pull`, et le fichier JSONL n'est qu'un export. — là où Backlog.md garde des fichiers Markdown relisibles par un humain, Beads garde un graphe que les agents interrogent.
- voisin : [[Vibe Kanban]] — application locale qui lance un agent par carte dans un espace de travail isolé ; elle ne tient pas le backlog en fichiers, elle pilote les agents.
- voisin : [[OpenSpec]] — cadre de spécification : un dossier de plan, de spécification et de tâches par changement, que l'agent applique puis archive. Backlog.md découpe le travail en tâches relisibles, OpenSpec décrit le comportement visé ; les deux se lisent avant le code.

## Ressources

- Documentation — https://backlog.md
- Dépôt — https://github.com/MrLesk/Backlog.md

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Backlog, Kanban, Scrum et Shape Up]] — la notion : le Kanban en solo et avec des agents
- [[Fichiers de contexte pour agents]] — le fichier d'instructions que `backlog init` écrit
- [[Développement piloté par la spécification]] — la famille d'approches
- [[Outils de développement]] — le hub du domaine
