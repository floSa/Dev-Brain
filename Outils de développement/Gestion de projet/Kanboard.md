---
role: brique
nom: Kanboard
alias: [kanboard]
pitch: "Application web de tableau Kanban à héberger (MIT, PHP, en mode maintenance) : colonnes, limite de travail en cours, couloirs, sous-tâches, actions automatiques, API JSON-RPC, sans fioriture."
categorie: devtools/projet
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: PHP
scaling: single-node
alternatives: ["[[Redmine]]"]
complements: []
tags: [issue-tracking, project-management, self-hosted]
url_docs: https://docs.kanboard.org/
url_repo: https://github.com/kanboard/kanboard
---

# Kanboard

<!-- AUTO:BANDEAU:START -->
> Application web de tableau Kanban à héberger (MIT, PHP, en mode maintenance) : colonnes, limite de travail en cours, couloirs, sous-tâches, actions automatiques, API JSON-RPC, sans fioriture.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application PHP | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Application web de tableau Kanban, à installer sur son propre serveur. Les tâches se déplacent par glisser-déposer entre des colonnes que l'on ajoute, renomme ou retire à tout moment ; une colonne dépassant sa **limite de travail en cours** (WIP) est surlignée. Autour du tableau : couloirs (*swimlanes*), sous-tâches avec estimation et temps passé, commentaires et pièces jointes, descriptions en Markdown, une syntaxe de recherche, des **actions automatiques** (changer l'affectation, la couleur, la catégorie selon un événement) et des **analyses par projet** : diagramme de flux cumulé, burn down, temps moyen par colonne, délai et temps de cycle moyens.

Le site le dit sans détour : l'interface est minimale et le nombre de fonctions **volontairement limité**. Relevé le 2026-10-07 : **v1.2.54** (2026-08-29), dernier push sur le dépôt le 2026-10-03, licence MIT (fichier `LICENSE`), un développeur principal (Frédéric Guillot) et plus de 334 contributeurs selon le site.

**État d'entretien.** Le README écrit que l'application est en **mode maintenance** : l'auteur ne développe plus de grande fonctionnalité nouvelle, seulement de petites corrections ; des versions paraissent régulièrement selon les contributions de la communauté, et les demandes de fusion pour une fonction ou un correctif restent acceptées si elles suivent les consignes. Le projet est vivant, mais sans grande fonction à attendre.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un tableau Kanban simple pour une personne ou une petite équipe : le site annonce une « installation super simple » | Un workflow de tickets par type et par rôle, un wiki, un diagramme de Gantt : [[Redmine]] les décrit, la documentation de Kanboard n'en a pas de chapitre |
| Limiter le travail en cours est le but : la limite de colonne est native | Une feuille de route longue : le projet n'ajoute plus de fonctions majeures |
| Lire le flux : diagramme de flux cumulé, temps de cycle et délai moyens, sans outil de plus | Une navigation confortable sur téléphone : la documentation prévient que le tableau y est peu pratique |
| Une API JSON-RPC pour scripter les tâches, avec un client Python officiel | Un tableau déjà intégré à la forge du projet : les tickets de [[Forgejo]] ou de [[GitLab CE]] évitent un outil de plus |

## Mise en œuvre

- Installation — archive, paquet de distribution, ou image Docker (`docker.io/kanboard/kanboard`, aussi sur ghcr.io et quay.io) ; la documentation conseille d'épingler une version précise plutôt que `latest`, et de lire le ChangeLog avant chaque montée de version
- Point d'entrée — l'interface web ; l'API JSON-RPC (`jsonrpc.php`) accepte les requêtes en lot ; plugins, webhooks, flux RSS et calendriers iCalendar existent
- Prérequis — PHP 8.1 ou plus (depuis la v1.2.46) ; SQLite, MySQL 5.6 ou plus, MariaDB 10 ou plus, PostgreSQL 9.4 ou plus (recommandé), SQL Server en expérimental. Pas de SQLite sur NFS ni dans Docker. Apache, Nginx, IIS ou Caddy ; **incompatible avec Apache mod_security**
- Exécution — authentification locale, **LDAP / Active Directory** ou n'importe quel fournisseur OAuth2 ; volumes de l'image : `/var/www/app/data` (base SQLite, pièces jointes) et `/var/www/app/plugins`
- Coût — gratuit ; le coût est la machine et le suivi des mises à jour

## Limites à connaître

- **Fonctions volontairement rares.** Le modèle est le tableau : la liste des chapitres de la documentation utilisateur ne comporte ni diagramme de Gantt ni wiki. Kanban s'y fait directement ; la discipline de Scrum ou de Shape Up (voir [[Backlog, Kanban, Scrum et Shape Up]]) reste à tenir à la main.
- **Temps saisi à la main.** Les champs « temps estimé » et « temps passé » sont renseignés par l'utilisateur ; un minuteur existe sur les sous-tâches. Rien ne se déduit de l'activité.
- **Mode maintenance.** Une grande fonction manquante n'est pas à attendre de l'auteur ; un plugin (la documentation en décrit l'écriture) ou un autre outil la couvre.

## Écosystème

### Alternatives

- [[Redmine]] — Application web de gestion de projet à héberger (GPL v2 ou ultérieure, Ruby on Rails) : plusieurs projets, tickets au workflow configurable, diagramme de Gantt, wiki, suivi du temps et dépôts de code intégrés. — l'application complète, quand le tableau ne suffit plus.
- Jira (Atlassian, propriétaire) — la référence en entreprise pour les workflows et la traçabilité. Cité en texte simple, sans page : voir [[Backlog, Kanban, Scrum et Shape Up]].
- Vikunja, Wekan, Huly, Leantime, Taiga, Focalboard — tâches et tableaux libres, sans fiche ici ; cités en texte simple (Focalboard : dernier push relevé en 2025-02).

## Ressources

- Documentation — https://docs.kanboard.org/
- Dépôt — https://github.com/kanboard/kanboard
- Documentation — site du projet : https://kanboard.org/
- Documentation — prérequis : https://docs.kanboard.org/v1/admin/requirements/
- Documentation — image Docker : https://docs.kanboard.org/v1/admin/docker/
- Documentation — analyses de projet : https://docs.kanboard.org/v1/user/analytics/

## Voir aussi

- [[Gestion de projet]] — le hub du dossier
- [[Backlog, Kanban, Scrum et Shape Up]] — la notion : Kanban, limite de WIP, et le parallèle avec Jira.
- [[Comparatif - Suivi de projet auto-hébergé]] — le comparatif : méthode supportée, poids, état d'entretien.
- [[Mesurer un projet - DORA, coût des agents et temps passé]] — la notion : le délai et le temps de cycle du tableau se lisent comme des mesures de flux.
