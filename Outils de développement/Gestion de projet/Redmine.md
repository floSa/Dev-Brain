---
role: brique
nom: Redmine
alias: [redmine, Redmine PM]
pitch: "Application web de gestion de projet à héberger (GPL v2 ou ultérieure, Ruby on Rails) : plusieurs projets, tickets au workflow configurable, diagramme de Gantt, wiki, suivi du temps et dépôts de code intégrés."
categorie: devtools/projet
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: Ruby
scaling: single-node
alternatives: ["[[Kanboard]]"]
complements: []
tags: [issue-tracking, project-management, self-hosted]
url_docs: https://www.redmine.org/projects/redmine/wiki/Guide
url_repo: https://github.com/redmine/redmine
---

# Redmine

<!-- AUTO:BANDEAU:START -->
> Application web de gestion de projet à héberger (GPL v2 ou ultérieure, Ruby on Rails) : plusieurs projets, tickets au workflow configurable, diagramme de Gantt, wiki, suivi du temps et dépôts de code intégrés.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Ruby | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Application web de gestion de projet, à installer sur son propre serveur. Un seul Redmine gère **plusieurs projets**, avec des sous-projets ; chaque utilisateur y a un rôle par projet, et chaque projet active ou non ses modules (tickets, wiki, forum, dépôt de code). Les statuts, les types de ticket et les transitions de workflow par type et par rôle se configurent depuis l'interface d'administration. Des champs personnalisés s'ajoutent aux tickets, aux saisies de temps, aux projets et aux utilisateurs.

Relevé le 2026-10-07 sur redmine.org : trois versions suivies, **6.0.11** (2026-08-26), **6.1.5** et **7.0.2** (2026-09-30). La plus récente est entièrement maintenue ; la précédente reçoit des corrections et la sécurité ; la troisième, seulement les correctifs de sécurité importants. Le code est développé sur le dépôt Subversion officiel ; le dépôt GitHub est un **miroir** et ne porte pas de « releases » (l'API GitHub n'en renvoie aucune).

**Licence.** GPL v2 ou ultérieure, d'après l'en-tête des sources et le fichier `doc/COPYING` (texte de la GPL v2). Aucune édition payante n'apparaît dans les pages lues (accueil, fonctions, téléchargement). Pour un usage interne ou chez un client, la GPL ne demande rien tant qu'une version modifiée n'est pas redistribuée.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Plusieurs projets ou clients dans une seule instance, chacun avec ses droits | Un seul projet, une seule personne : un tableau [[Kanboard]] ou un fichier Markdown suffit |
| Un workflow de tickets à définir par type et par rôle, avec champs personnalisés et traçabilité (qui a demandé quoi, quand) | Un tableau Kanban natif, tout de suite : la liste officielle des fonctions n'en mentionne pas, il faut [[Kanboard]] ou un plugin |
| Planning par dates de début et d'échéance : Gantt et calendrier générés depuis les tickets | Un besoin de tableau agile (Scrum, Kanban) sans installer de plugin : la liste officielle des fonctions n'en parle pas |
| Le suivi du temps par ticket, avec un rapport par personne, type ou activité | La facturation et les feuilles de temps comme cœur du besoin : [[Kimai]] est fait pour cela |

## Mise en œuvre

- Installation — archive `.tar.gz` ou `.zip`, ou image Docker officielle (« Docker Official Image » sur Docker Hub, maintenue par la communauté Docker) ; le projet recommande les versions publiées, pas le tronc
- Point d'entrée — l'interface web ; une **API REST** (XML et JSON) donne accès en lecture et en écriture aux tickets, projets, saisies de temps et utilisateurs
- Prérequis — Redmine 7.0 : Ruby 3.2 à 4.0 et Rails 8.1 ; PostgreSQL 14 ou plus, MySQL 8.0 à 8.4, SQL Server, SQLite 3 (déconseillé en production multi-utilisateur). Le projet note que Ruby 4.0.0 à 4.0.3 ralentit fortement l'affichage du wiki et conseille Ruby 4.0.4 ou plus. JRuby n'est pas pris en charge
- Exécution — une application Rails à servir par un serveur d'application (voir le guide d'installation) ; authentification par la base, **LDAP** (plusieurs sources) ou plugin ; notifications et création de tickets par courriel ; intégration de dépôts Subversion, Git, Mercurial, Bazaar et CVS
- Coût — gratuit ; le coût est la machine, la base et l'équipe qui met à jour

## Limites à connaître

- **Peu de méthode agile intégrée.** Redmine donne des tickets, un calendrier et un Gantt ; Scrum, Kanban et Shape Up (voir [[Backlog, Kanban, Scrum et Shape Up]]) passent par des plugins, que cette fiche n'a pas évalués.
- **Un écosystème de plugins à surveiller.** Les plugins et thèmes sont listés sur redmine.org ; chacun est du code tiers, à vérifier avant chaque montée de version (Redmine 7.0 passe à Rails 8.1, 6.0 et 6.1 sont sur Rails 7.2).
- **Un dépôt GitHub qui n'est pas la source.** Il se décrit lui-même comme un miroir du dépôt Subversion officiel ; c'est là que le code se développe.

## Écosystème

### Alternatives

- [[Kanboard]] — Application web de tableau Kanban à héberger (MIT, PHP, en mode maintenance) : colonnes, limite de travail en cours, couloirs, sous-tâches, actions automatiques, API JSON-RPC, sans fioriture. — un tableau seul, sans Gantt ni wiki dans sa documentation, contre une application complète : Kanboard est un tableau ; Redmine gère plusieurs projets et leur traçabilité.
- Jira (Atlassian, propriétaire) — la référence en entreprise : workflows, rapports, droits par projet, traçabilité. Cité en texte simple, sans page : voir [[Backlog, Kanban, Scrum et Shape Up]].
- OpenProject, Plane, Taiga, Leantime — autres plateformes de suivi de projet, sans fiche ici ; citées en texte simple.

## Ressources

- Documentation — https://www.redmine.org/projects/redmine/wiki/Guide
- Dépôt — https://github.com/redmine/redmine (miroir ; dépôt officiel : https://svn.redmine.org/redmine)
- Documentation — fonctions : https://www.redmine.org/projects/redmine/wiki/Features
- Documentation — prérequis par version : https://www.redmine.org/projects/redmine/wiki/RedmineInstall
- Documentation — API REST : https://www.redmine.org/projects/redmine/wiki/Rest_api

## Voir aussi

- [[Gestion de projet]] — le hub du dossier
- [[Backlog, Kanban, Scrum et Shape Up]] — la notion : méthodes de suivi, solo et avec agents, et le parallèle avec Jira.
- [[Comparatif - Suivi de projet auto-hébergé]] — le comparatif : méthode supportée, poids, état d'entretien.
- [[Mesurer un projet - DORA, coût des agents et temps passé]] — la notion : le temps et la livraison se mesurent à part du suivi des tickets.
