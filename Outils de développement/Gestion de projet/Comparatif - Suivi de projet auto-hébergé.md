---
role: comparatif
nom: Comparatif - Suivi de projet auto-hébergé
categorie: devtools/projet
tags: [issue-tracking, project-management]
---

# Comparatif - Suivi de projet auto-hébergé

> On tranche sur : le modèle (un tableau ou une application à plusieurs projets), puis le poids à héberger, puis l'état d'entretien.

![[Comparatif - Suivi de projet auto-hébergé.base]]

## Ce qui départage

- [[Kanboard]] — **un tableau Kanban et rien d'autre** : colonnes, limite de travail en cours, couloirs, sous-tâches, analyses de flux (temps de cycle, diagramme de flux cumulé). PHP 8.1 ou plus et une base au choix, SQLite comprise ; MIT. En **mode maintenance** d'après son README : v1.2.54 le 2026-08-29, plus de grande fonction à attendre. Il se prend quand le besoin est « voir et limiter le travail en cours ».
- [[Redmine]] — **une application de gestion de projet** : plusieurs projets et sous-projets, rôles par projet, tickets au workflow configurable, champs personnalisés, Gantt, wiki, suivi du temps, dépôts de code, API REST. Ruby on Rails, avec PostgreSQL, MySQL ou SQL Server en production ; GPL v2 ou ultérieure. Trois versions suivies (6.0.11, 6.1.5, 7.0.2) et un cycle de support publié. Il se prend quand plusieurs clients ou projets partagent une instance et que la traçabilité compte.

## Quelle méthode, quel outil

| Méthode | Kanboard | Redmine |
|---|---|---|
| Kanban, limite de travail en cours | natif | non mentionné dans la liste officielle des fonctions ; plugins non évalués |
| Planning par dates (Gantt, calendrier) | pas de chapitre dans la documentation utilisateur | natif, d'après les dates de début et d'échéance des tickets |
| Scrum, Shape Up | à tenir à la main | à tenir à la main ou par plugin non évalué |
| Plusieurs projets, droits par rôle | oui (projets, utilisateurs et groupes) | oui, par projet, avec sous-projets |
| Suivi du temps | saisi à la main, minuteur sur les sous-tâches | saisi par ticket, rapport par personne, type ou activité |

Jira (propriétaire, cité en texte simple) apporte en entreprise des workflows configurables, des droits par projet et de la traçabilité. Redmine couvre une bonne part de ce périmètre dans une application libre ; Kanboard s'en tient au tableau. Vikunja, Wekan, Huly, Leantime, Taiga et OpenProject, eux aussi en texte simple, couvrent d'autres équilibres ; ils n'ont pas de fiche ici.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Backlog, Kanban, Scrum et Shape Up]] — la notion : quelle méthode choisir avant de choisir l'outil.
