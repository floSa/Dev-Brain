---
role: brique
nom: Vibe Kanban
alias: [vibe-kanban, BloopAI/vibe-kanban]
pitch: "Application locale (Apache-2.0, Rust) : un tableau Kanban où chaque carte lance un agent de code dans un espace de travail isolé — branche, terminal, serveur de développement — avec revue de diff commentée et création de pull request — mais la société bloop qui la portait a fermé le 2026-04-10 et le projet vit en maintenance communautaire."
categorie: devtools/projet
famille: application
domaines: [ai-eng]
licence_type: open-source
maturite: beta
langage: Rust
hosted: [self]
scaling: single-node
alternatives: ["[[Claude Squad]]"]
complements: []
tags: [multi-agent, project-management, version-control]
url_docs: https://www.vibekanban.com/docs
url_repo: https://github.com/BloopAI/vibe-kanban
---

# Vibe Kanban

<!-- AUTO:BANDEAU:START -->
> Application locale (Apache-2.0, Rust) : un tableau Kanban où chaque carte lance un agent de code dans un espace de travail isolé — branche, terminal, serveur de développement — avec revue de diff commentée et création de pull request — mais la société bloop qui la portait a fermé le 2026-04-10 et le projet vit en maintenance communautaire.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Rust | open-source | self-hébergé · mono-nœud | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Application qui se lance par `npx vibe-kanban` et s'ouvre dans le navigateur. On y planifie le travail en cartes sur un tableau Kanban, puis on crée des **espaces de travail** où des agents de code exécutent : chacun reçoit une branche, un terminal et un serveur de développement. L'application affiche le diff, accepte des commentaires en ligne qui repartent vers l'agent, propose un aperçu de l'application avec les outils de développement du navigateur, ouvre la pull request avec une description rédigée par un modèle, puis la fusion. Elle ne contient pas d'agent : elle pilote ceux que l'utilisateur a déjà installés et authentifiés, plus de dix d'après le README (Claude Code, Codex, Gemini CLI, GitHub Copilot, Amp, Cursor, [[OpenCode]], Droid, CCR et [[Qwen Code]]).

**À savoir avant de s'y fier.** Le README s'ouvre sur « Vibe Kanban is sunsetting ». Le billet du 2026-04-10 annonce la fermeture de bloop, la société qui l'éditait, faute de modèle économique : le projet continue, maintenu par la communauté, et les espaces de travail locaux continuent de fonctionner. Les services distants (cartes, commentaires, projets, organisations) devaient disparaître après trente jours, au profit d'une architecture entièrement locale ; le README garde pourtant un guide d'auto-hébergement de l'instance « Cloud ». À vérifier avant de bâtir une organisation d'équipe dessus. La dernière release est la v0.1.44 du 2026-04-24 ; le dépôt a été poussé le 2026-09-19.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Lancer plusieurs agents en parallèle sur un même dépôt, chacun sur sa branche, sans gérer les worktrees à la main (cf. [[Branches courtes et worktrees pour agents]]) | Un outil qui garantit une maintenance : plus d'éditeur derrière, une release en avril et des pushes depuis |
| Relire le diff d'un agent et lui répondre en commentaires sur place, plutôt que dans un chat | Un backlog partagé entre personnes : les cartes distantes étaient la partie hébergée par bloop ; en solo, un fichier ou un tableau libre suffit (cf. [[Backlog, Kanban, Scrum et Shape Up]]) |
| Passer d'un agent à l'autre sans changer d'interface : le README en liste plus de dix | Un poste partagé ou un accès distant : par défaut le serveur écoute sur `127.0.0.1` ; derrière un proxy inverse, `VK_ALLOWED_ORIGINS` doit lister les origines, sinon les requêtes reçoivent un 403 |
| Garder la main sur la fusion : la revue du diff reste le geste central (cf. [[Revue, tests et définition de terminé avec un agent]]) | Un agent absent de la liste du README : l'application ne le pilotera pas |

## Mise en œuvre

- Installation — aucune : `npx vibe-kanban`, après s'être authentifié auprès de l'agent choisi ; Rust, Node.js 20 ou plus et pnpm pour le construire
- Point d'entrée — l'interface web ouverte par la commande ; variables `HOST`, `PORT`, `BACKEND_PORT`
- Prérequis — un agent de code installé et authentifié, git
- Exécution — local ; la télémétrie PostHog est désactivée quand ses clés de construction sont vides, ce que le README donne comme valeur par défaut
- Coût — gratuit sous licence Apache-2.0 ; la dépense est celle des agents et de leurs modèles

## Écosystème

### Alternatives

- [[Claude Squad]] — Application de terminal (AGPL-3.0, Go) qui gère plusieurs agents de code en parallèle, chacun dans une session tmux et un worktree git à lui, avec aperçu, diff, validation et poussée de la branche — mais tmux et gh sont requis, et l'AGPL pèse si l'outil est offert en service. — là où Vibe Kanban offre un tableau et une revue de diff dans le navigateur, Claude Squad tient dans un terminal, sur tmux.
- voisin : [[t3code]] — plan de contrôle au-dessus des CLI d'agents de code installées localement, desktop, web et mobile ; il pilote des agents lui aussi, sans le tableau de cartes.
- voisin : [[swarm-forge]] — orchestrateur tmux d'agents de code, un git worktree par agent ; aucune licence déclarée.
- voisin : Ruflo et Crystal — d'autres gestionnaires d'agents en parallèle, cités en texte simple, non fichés dans le brain.

## Ressources

- Documentation — https://www.vibekanban.com/docs
- Dépôt — https://github.com/BloopAI/vibe-kanban
- Article — https://www.vibekanban.com/blog/shutdown (annonce de la fermeture de bloop)

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Branches courtes et worktrees pour agents]] — isoler le travail de chaque agent
- [[Backlog, Kanban, Scrum et Shape Up]] — le Kanban en solo et avec des agents
- [[Agents de code]] — les agents que l'application pilote
- [[Outils de développement]] — le hub du domaine
