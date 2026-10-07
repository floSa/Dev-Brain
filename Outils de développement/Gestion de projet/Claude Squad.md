---
role: brique
nom: Claude Squad
alias: [claude-squad, cs, smtg-ai/claude-squad]
pitch: "Application de terminal (AGPL-3.0, Go) qui gère plusieurs agents de code en parallèle, chacun dans une session tmux et un worktree git à lui, avec aperçu, diff, validation et poussée de la branche — mais tmux et gh sont requis, et l'AGPL pèse si l'outil est offert en service."
categorie: devtools/projet
famille: cli
domaines: [ai-eng]
licence_type: open-source
maturite: production
langage: Go
alternatives: ["[[Vibe Kanban]]"]
complements: []
tags: [multi-agent, version-control, agents]
url_docs: https://smtg-ai.github.io/claude-squad/
url_repo: https://github.com/smtg-ai/claude-squad
---

# Claude Squad

<!-- AUTO:BANDEAU:START -->
> Application de terminal (AGPL-3.0, Go) qui gère plusieurs agents de code en parallèle, chacun dans une session tmux et un worktree git à lui, avec aperçu, diff, validation et poussée de la branche — mais tmux et gh sont requis, et l'AGPL pèse si l'outil est offert en service.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI Go | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Application de terminal, lancée par la commande `cs`, qui pilote **plusieurs agents de code à la fois** sur un même dépôt. Chaque tâche reçoit une session **tmux** (un terminal isolé qui continue en arrière-plan) et un **worktree git** (une copie de travail sur sa propre branche), si bien que deux agents ne s'écrasent pas. Une fenêtre unique liste les sessions, montre l'aperçu de l'agent et le diff de ses changements ; on peut s'attacher à une session pour relancer l'agent, la mettre en pause (`c`, qui commit et suspend), la reprendre (`r`) ou pousser la branche (`s`). Le programme lancé par défaut est `claude` ; `cs -p "codex"`, `cs -p "gemini"` ou une commande Aider changent d'agent, et des **profils** dans `~/.claude-squad/config.json` permettent d'en choisir un à la création de la session. Le mode `--autoyes` est expérimental : il accepte les demandes de l'agent sans demander.

Version 1.0.20 du 2026-08-20, licence AGPL-3.0 lue dans le dépôt (`LICENSE.md`), dépôt poussé le 2026-08-20. L'AGPL n'a de conséquence que si l'outil est modifié et offert à des tiers par le réseau ; pour un usage personnel ou interne, rien à publier.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Lancer trois ou quatre agents sur trois tâches séparées, depuis un seul terminal, sans gérer les worktrees à la main (cf. [[Branches courtes et worktrees pour agents]]) | Une interface graphique avec tableau de cartes et revue de diff commentée : [[Vibe Kanban]], aujourd'hui en maintenance communautaire |
| Travailler sur un serveur ou en SSH : tout tient dans un terminal | Un poste sans tmux ni `gh` : ce sont les deux prérequis du README |
| Garder la main sur ce qui part : l'aperçu et le diff précèdent la poussée | Laisser tourner des agents sans surveillance : `--autoyes` est expérimental, et chaque agent consomme son propre quota |
| Changer d'agent d'une session à l'autre par les profils | Une tâche qui dépend d'une autre : les sessions ne se parlent pas, le découpage reste à la charge de l'utilisateur (cf. [[Backlog.md - l'outil]]) |

## Mise en œuvre

- Installation — `brew install claude-squad` (puis un lien `cs`), ou le script `install.sh` du dépôt qui pose `cs` dans `~/.local/bin`
- Point d'entrée — la commande `cs` dans un dépôt git ; `cs debug` affiche le chemin de la configuration
- Prérequis — tmux, `gh`, et l'agent choisi installé et authentifié (`OPENAI_API_KEY` pour Codex)
- Exécution — sur le poste ; rien à héberger
- Coût — gratuit sous licence AGPL-3.0 ; la dépense est celle des agents

## Écosystème

### Alternatives

- [[Vibe Kanban]] — Application locale (Apache-2.0, Rust) : un tableau Kanban où chaque carte lance un agent de code dans un espace de travail isolé — branche, terminal, serveur de développement — avec revue de diff commentée et création de pull request — mais la société bloop qui la portait a fermé le 2026-04-10 et le projet vit en maintenance communautaire. — là où Claude Squad tient dans un terminal, Vibe Kanban offre un tableau et une revue dans le navigateur.
- voisin : [[t3code]] — plan de contrôle au-dessus des CLI d'agents installées localement, desktop, web et mobile.
- voisin : [[swarm-forge]] — orchestrateur tmux d'agents de code, un git worktree par agent ; aucune licence déclarée.

## Ressources

- Documentation — https://smtg-ai.github.io/claude-squad/
- Dépôt — https://github.com/smtg-ai/claude-squad

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Branches courtes et worktrees pour agents]] — isoler le travail de chaque agent
- [[Agents de code]] — les agents que l'application pilote
- [[Outils de développement]] — le hub du domaine
