---
role: brique
nom: Wekan
alias: [wekan, WeKan, wekan/wekan]
pitch: "Application web de tableaux Kanban à héberger (MIT, JavaScript et Meteor), sur le modèle de Trello : couloirs, listes, cartes, vues tableau, calendrier et Gantt, modules Scrum et graphiques de flux, règles automatiques, imports depuis Trello, Jira, GitHub ou Kanboard, connexion LDAP, SAML ou OAuth2 — mais l'outil est large, sa cadence de versions est très rapide (six en cinq jours début octobre 2026), et le support officiel public se limite aux tickets GitHub."
categorie: devtools/projet
famille: application
domaines: [ai-eng]
licence_type: open-source
hosted: [self]
maturite: production
langage: JavaScript
scaling: single-node
alternatives: ["[[Kanboard]]", "[[Vikunja]]"]
complements: []
tags: [issue-tracking, project-management, self-hosted]
url_docs: https://wekan.fi
url_repo: https://github.com/wekan/wekan
---

# Wekan

<!-- AUTO:BANDEAU:START -->
> Application web de tableaux Kanban à héberger (MIT, JavaScript et Meteor), sur le modèle de Trello : couloirs, listes, cartes, vues tableau, calendrier et Gantt, modules Scrum et graphiques de flux, règles automatiques, imports depuis Trello, Jira, GitHub ou Kanboard, connexion LDAP, SAML ou OAuth2 — mais l'outil est large, sa cadence de versions est très rapide (six en cinq jours début octobre 2026), et le support officiel public se limite aux tickets GitHub.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application JavaScript | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Tableau Kanban collaboratif, libre (licence MIT), à installer sur son propre ordinateur ou serveur. Le README le présente comme utile pour une liste de tâches perso, des vacances entre amis ou une équipe, et affirme que sa plus grosse installation compte 30 000 utilisateurs. L'interface est en temps réel ; une page « tous les tableaux » range les tableaux par espaces de travail. Les cartes se rangent en listes et en **couloirs**, avec modèles de tableaux, de listes et de cartes. Les vues dépassent le Kanban : tableau, calendrier, chronologie, Gantt, statistiques, un mode **Scrum** (backlog produit, sprints, vélocité, burndown) et des graphiques de flux (diagramme de flux cumulé, temps de cycle, débit, prévisions de Monte-Carlo). Des **règles** déclenchent des actions, à la manière d'IFTTT.

L'import vient de Trello, Jira, Asana, Focalboard, [[Kanboard]], Nextcloud Deck, OpenProject, Taskwarrior, GitHub, GitLab, Gitea et Forgejo (liste du README). L'authentification passe par un compte local, SAML, LDAP, OAuth2 ou un lien sans mot de passe ; les pièces jointes se stockent dans MongoDB GridFS, un système de fichiers ou un stockage compatible S3 (MinIO, Azure, Google). Le projet dit n'envoyer aucune télémétrie. Le support officiel public se fait sur les tickets GitHub, un support privé payant existe (texte simple). Version 12.21 du 2026-10-07, licence MIT lue dans le dépôt, dépôt poussé le même jour : les releases sont très fréquentes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un Kanban à la Trello, à héberger, avec couloirs, modèles et règles automatiques | Un tableau minimal à maintenir à peu de frais : [[Kanboard]] est plus petit |
| Migrer depuis Trello, Jira ou [[Kanboard]] : l'import est une fonction prévue | Des listes de tâches personnelles avec rappels et répétitions : [[Vikunja]] |
| Mesurer le flux (temps de cycle, débit, Monte-Carlo) ou suivre un sprint dans le même outil | Plusieurs projets avec workflow de tickets, wiki, dépôts et suivi du temps : [[Redmine]] |
| Un annuaire d'entreprise : LDAP, SAML, OAuth2 sont dans la liste | Un outil dont le rythme de versions est lent à suivre : six versions sont sorties entre le 2026-10-03 et le 2026-10-07 |

## Mise en œuvre

- Installation — Docker (`wekanteam/wekan` sur Docker Hub, `docker-compose.yml` dans le dépôt), Snap avec mises à jour automatiques, Kubernetes ; la page d'installation du site liste les autres modes
- Point d'entrée — l'interface web après lancement
- Prérequis — MongoDB pour les données et, au choix, GridFS, système de fichiers ou S3 pour les pièces jointes
- Exécution — auto-hébergé, mono-nœud
- Coût — gratuit sous licence MIT ; un support privé payant existe

## Écosystème

### Alternatives

- [[Kanboard]] — Application web de tableau Kanban à héberger (MIT, PHP, en mode maintenance) : colonnes, limite de travail en cours, couloirs, sous-tâches, actions automatiques, API JSON-RPC, sans fioriture. — plus petit et en maintenance ; Wekan est plus riche mais plus lourd.
- [[Vikunja]] — Application web de gestion de tâches à héberger (AGPL-3.0 ou ultérieure, Go et Vue.js), livrée en un seul binaire ou conteneur : projets et sous-projets, tâches avec rappels et répétitions, partage entre utilisateurs, vues liste, Gantt, tableau et Kanban, API documentée — mais l'administration, le journal d'audit et le suivi du temps relèvent de la version payante Vikunja Pro. — des listes de tâches avec rappels, là où Wekan reste centré sur le tableau.
- voisin : [[Redmine]] — gestion de projet à plusieurs projets, avec tickets et traçabilité.

## Ressources

- Documentation — https://wekan.fi
- Dépôt — https://github.com/wekan/wekan

## Voir aussi

- [[Gestion de projet]] — le hub du sous-domaine
- [[Comparatif - Suivi de projet auto-hébergé]] — où ces outils se départagent
- [[Backlog, Kanban, Scrum et Shape Up]] — la notion : quelle méthode choisir avant l'outil
- [[Outils de développement]] — le hub du domaine
