---
role: comparatif
nom: Comparatif - Suivi de projet auto-hébergé
categorie: devtools/projet
tags: [issue-tracking, project-management]
---

# Comparatif - Suivi de projet auto-hébergé

> On tranche sur : le modèle (un tableau, des listes de tâches ou une application à plusieurs projets), puis le poids à héberger, la licence, puis l'état d'entretien.

![[Comparatif - Suivi de projet auto-hébergé.base]]

## Ce qui départage

- [[Kanboard]] — **un tableau Kanban et rien d'autre** : colonnes, limite de travail en cours, couloirs, sous-tâches, analyses de flux (temps de cycle, diagramme de flux cumulé). PHP 8.1 ou plus et une base au choix, SQLite comprise ; MIT. En **mode maintenance** d'après son README : v1.2.54 le 2026-08-29, plus de grande fonction à attendre. Il se prend quand le besoin est « voir et limiter le travail en cours ».
- [[Redmine]] — **une application de gestion de projet** : plusieurs projets et sous-projets, rôles par projet, tickets au workflow configurable, champs personnalisés, Gantt, wiki, suivi du temps, dépôts de code, API REST. Ruby on Rails, avec PostgreSQL, MySQL ou SQL Server en production ; GPL v2 ou ultérieure. Trois versions suivies (6.0.11, 6.1.5, 7.0.2) et un cycle de support publié. Il se prend quand plusieurs clients ou projets partagent une instance et que la traçabilité compte.
- [[Vikunja]] — **des listes de tâches, avec rappels, répétitions et plusieurs vues** : liste, Gantt, tableau et Kanban d'un même projet, projets et sous-projets, partage par utilisateur ou équipe, API OpenAPI ; Go et Vue.js, un seul binaire ou conteneur. AGPL-3.0 ou ultérieure (desktop sous GPL-3.0) ; v2.7.0 du 2026-10-02. Le prix : l'administration, le journal d'audit et le suivi du temps sont dans la version payante Vikunja Pro, pas dans le dépôt libre.
- [[Wekan]] — **un Kanban à la Trello, très complet** : couloirs, modèles, règles automatiques, vues calendrier, Gantt et Scrum, graphiques de flux (temps de cycle, débit, Monte-Carlo), imports depuis Trello, Jira, [[Kanboard]] et d'autres, connexion LDAP, SAML ou OAuth2. JavaScript et Meteor, MIT ; v12.21 du 2026-10-07. Le prix : une fonction très large à tenir, six versions entre le 2026-10-03 et le 2026-10-07, et un support officiel public limité aux tickets GitHub.

## Quelle méthode, quel outil

| Méthode | Kanboard | Redmine | Vikunja | Wekan |
|---|---|---|---|---|
| Kanban, limite de travail en cours | natif | non mentionné dans la liste officielle des fonctions ; plugins non évalués | vue Kanban native ; limite de travail en cours non évaluée | natif, avec couloirs |
| Planning par dates (Gantt, calendrier) | pas de chapitre dans la documentation utilisateur | natif, d'après les dates de début et d'échéance des tickets | vue Gantt native | vues calendrier et Gantt dans la liste du README |
| Scrum, Shape Up | à tenir à la main | à tenir à la main ou par plugin non évalué | non évalué | modules Scrum (backlog, sprints, vélocité) listés par le README ; Shape Up à la main |
| Plusieurs projets, droits par rôle | oui (projets, utilisateurs et groupes) | oui, par projet, avec sous-projets | projets et sous-projets, partage par utilisateur ou équipe | tableaux et espaces de travail ; droits non évalués |
| Suivi du temps | saisi à la main, minuteur sur les sous-tâches | saisi par ticket, rapport par personne, type ou activité | version Pro seulement | une vue « Time » est listée ; non évaluée |

Jira (propriétaire, cité en texte simple) apporte en entreprise des workflows configurables, des droits par projet et de la traçabilité. Redmine couvre une bonne part de ce périmètre dans une application libre ; Kanboard s'en tient au tableau. Huly, Leantime, Taiga et OpenProject, eux aussi en texte simple, couvrent d'autres équilibres ; ils n'ont pas de fiche ici.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Backlog, Kanban, Scrum et Shape Up]] — la notion : quelle méthode choisir avant de choisir l'outil.
