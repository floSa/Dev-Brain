---
role: brique
nom: SQLAlchemy
alias: [sqlalchemy]
pitch: "Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0."
categorie: database/orm
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Prisma]]", "[[SQLModel]]"]
complements: ["[[Alembic]]", "[[psycopg2]]"]
tags: [orm, relational, type-hints]
url_docs: https://docs.sqlalchemy.org/
url_repo: https://github.com/sqlalchemy/sqlalchemy
---

# SQLAlchemy

<!-- AUTO:BANDEAU:START -->
> Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-01 |
<!-- AUTO:BANDEAU:END -->

## Définition

Toolkit d'accès aux bases relationnelles le plus établi en Python, organisé en **deux
couches** : Core — langage d'expression SQL, gestion des connexions, dialectes — et ORM, un
mapping objet-relationnel façon Data Mapper, avec identity map et unit of work. Depuis la
**2.0**, l'API est unifiée, entièrement typée (`Mapped[...]`) et prend en charge `asyncio`.
Chaque SGBD est piloté par un dialecte et un driver. Écrit par Mike Bayer.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Accès aux données d'une application Python — web, data, ML — avec contrôle fin du SQL généré | Requêtes **N+1** dès que le chargement paresseux n'est pas maîtrisé : `lazy`, `eager`, `selectinload` |
| Besoin des deux niveaux : l'ORM pour le CRUD, Core ou SQL brut pour les requêtes complexes | Saut d'API important entre 1.x et 2.0 — style `select()`, sessions : la version visée se vérifie |
| Modèles typés et accès async, avec un driver compatible, en 2.0 | La migration de schéma n'est pas incluse : c'est un outil distinct |
| | Micro-script à une poignée de requêtes : la couche ne se rembourse pas, un driver brut suffit |
| | Seulement des migrations, sans couche d'accès → outils dédiés, [[Flyway]] ou [[Liquibase]] |

## Mise en œuvre

- Installation — `uv add sqlalchemy`, plus le driver du SGBD visé
- Point d'entrée — deux couches : Core (`Engine`, `select()`) et ORM (`Session`, `Mapped[...]`)
- Prérequis — Python, et un dialecte plus un driver pour le moteur cible (psycopg, asyncpg, mysqlclient…)
- Exécution — dans le process de l'application, single-node ; rien à héberger
- Coût — gratuit, licence MIT

## Écosystème

### Alternatives

- [[Prisma]] — ORM TypeScript nouvelle génération : schéma déclaratif, client typé et migrations générées.
- [[SQLModel]] — Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI.

### Compléments

- [[Alembic]] — Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle. — la migration de schéma, que SQLAlchemy ne fait pas.
- [[psycopg2]] — Adaptateur PostgreSQL de référence pour Python (LGPL) — implémentation DB-API 2.0 en C au-dessus de libpq, sûre et performante ; figé en fonctionnalités, successeur psycopg 3. — le driver du dialecte Postgres par défaut.

## Ressources

- Documentation — https://docs.sqlalchemy.org/
- Dépôt — https://github.com/sqlalchemy/sqlalchemy

## Voir aussi

- [[ORM]] — la notion du dossier
- [[Comparatif - ORM]] — ce qui départage les ORM du dossier
