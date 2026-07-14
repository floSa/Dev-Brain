---
galaxie: dev
type: outil
nom: pgAdmin
alias: [pgadmin, pgadmin4]
pitch: "Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur."
categorie: tooling/db-admin
domaines: [data-eng]
licence_type: open-source
os: "Windows, macOS, Linux, web (Docker)"
langage: Python
status: actif
alternatives: ["[[Dev/Outils/DBeaver|DBeaver]]"]
tags: [db-client, postgres, relational]
url_docs: https://www.pgadmin.org/docs/
url_repo: https://github.com/pgadmin-org/pgadmin4
---

# pgAdmin

## Pourquoi

L'outil d'administration **officiel** de PostgreSQL. Application web (servie en local ou en mode serveur) qui couvre tout le cycle Postgres : navigateur d'objets, éditeur SQL, tableau de bord d'activité du serveur, gestion des rôles, sauvegarde/restauration, suivi des sessions. Sous PostgreSQL License (permissive, type BSD).

## Quand l'utiliser

- Administrer un serveur PostgreSQL et profiter d'un outil aligné sur ses spécificités (rôles, tablespaces, extensions, VACUUM).
- Tableau de bord d'activité (sessions, verrous, statistiques) intégré.
- Déploiement web multi-utilisateurs (mode serveur via Docker).

## Quand NE PAS l'utiliser

- Travailler sur plusieurs SGBD différents → [[Dev/Outils/DBeaver|DBeaver]].
- Préférer un client de bureau natif plutôt qu'une UI web.

## Bases & plateformes

- PostgreSQL uniquement (et dérivés compatibles).
- Application Python/web : bureau (Windows, macOS, Linux) ou conteneur serveur.

## Pièges

- UI web parfois moins réactive qu'un client natif sur de gros jeux de résultats.
- Centré Postgres : inutile dès qu'on doit toucher d'autres moteurs.

## Alternatives

- [[Dev/Outils/DBeaver|DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Dev/Services/Postgres|Postgres]] — le moteur administré
- [[Comparatif - Clients de bases de données]] — comparatif des clients GUI
- Doc : https://www.pgadmin.org/docs/
