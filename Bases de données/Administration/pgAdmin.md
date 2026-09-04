---
role: brique
nom: pgAdmin
alias: [pgadmin, pgadmin4]
pitch: "Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur."
categorie: database/admin
famille: application
domaines: [data-eng]
licence_type: open-source
os: "Windows, macOS, Linux, web (Docker)"
langage: Python
alternatives: ["[[DBeaver]]"]
complements: ["[[Postgres]]"]
tags: [db-client, postgres, relational]
url_docs: https://www.pgadmin.org/docs/
url_repo: https://github.com/pgadmin-org/pgadmin4
---

# pgAdmin

<!-- AUTO:BANDEAU:START -->
> Console d'administration web officielle de PostgreSQL : gestion, requêtes et supervision du serveur.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application Python | open-source | Windows, macOS, Linux, web (Docker) | — |
<!-- AUTO:BANDEAU:END -->

## Définition

L'outil d'administration officiel de PostgreSQL. C'est une application web — servie en local
ou en mode serveur multi-utilisateurs — qui couvre tout le cycle : navigateur d'objets,
éditeur SQL, tableau de bord d'activité du serveur, gestion des rôles, sauvegarde et
restauration, suivi des sessions. Elle suit les spécificités de Postgres de près : rôles,
tablespaces, extensions, VACUUM.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Administrer un serveur PostgreSQL avec un outil aligné sur ses spécificités — rôles, tablespaces, extensions, VACUUM | Interface web parfois moins réactive qu'un client natif sur de gros jeux de résultats |
| Tableau de bord d'activité intégré : sessions, verrous, statistiques | Centré Postgres : inutile dès qu'il faut toucher un autre moteur |
| Déploiement web multi-utilisateurs, en mode serveur via Docker | |

## Mise en œuvre

- Installation — paquet de bureau pour Windows, macOS ou Linux, ou conteneur pour le mode serveur
- Point d'entrée — interface web : navigateur d'objets, éditeur SQL, tableau de bord d'activité
- Prérequis — un serveur PostgreSQL ou un dérivé compatible ; l'application est en Python
- Exécution — en local sur le poste, ou en mode serveur multi-utilisateurs via Docker
- Coût — gratuit, sous PostgreSQL License (permissive, de type BSD)

## Écosystème

### Alternatives

- [[DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.

### Compléments

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — le moteur que la console administre

## Ressources

- Documentation — https://www.pgadmin.org/docs/

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Clients de bases de données]] — ce qui départage les clients du dossier
