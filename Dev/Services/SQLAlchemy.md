---
galaxie: dev
type: service
nom: SQLAlchemy
alias: [sqlalchemy]
pitch: "Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0."
categorie: framework/orm
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Prisma|Prisma]]", "[[Dev/Services/SQLModel|SQLModel]]"]
remplace_par: []
status: actif
tags: [orm, relational, type-hints]
url_docs: https://docs.sqlalchemy.org/
url_repo: https://github.com/sqlalchemy/sqlalchemy
---

# SQLAlchemy

## Pourquoi

Toolkit d'accès aux bases relationnelles le plus établi en Python, organisé en **deux couches** : Core (langage d'expression SQL, gestion des connexions, dialectes) et ORM (mapping objet-relationnel façon Data Mapper — identity map, unit of work). Depuis la **2.0** : API unifiée et entièrement typée (`Mapped[...]`) et support `asyncio`. Écrit par Mike Bayer (zzzeek).

## Quand l'utiliser

- Accès aux données d'une app Python (web, data, ML) avec contrôle fin du SQL généré.
- Besoin des deux niveaux : ORM pour le CRUD, Core / SQL brut pour les requêtes complexes.
- Modèles typés et accès async (avec un driver compatible) en 2.0.

## Quand NE PAS l'utiliser

- Stack TypeScript / Node → [[Dev/Services/Prisma|Prisma]].
- Seulement des migrations sans couche d'accès → outils dédiés [[Dev/Services/Flyway|Flyway]] / [[Dev/Services/Liquibase|Liquibase]].
- Micro-script avec une poignée de requêtes → driver brut (psycopg, sqlite3) suffisant.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite, intégrée à l'application. Pilote chaque SGBD via un dialecte + driver (psycopg, asyncpg, mysqlclient…).
- Pas de service à héberger : single-node, suit le déploiement de l'app.

## Pièges

- Requêtes **N+1** par chargement paresseux non maîtrisé (`lazy` / `eager`, `selectinload`).
- Saut d'API important entre 1.x et 2.0 (style `select()`, sessions) — vérifier la version visée.
- La migration de schéma n'est **pas** incluse : c'est le rôle d'[[Dev/Services/Alembic|Alembic]].
- Retours d'expérience détaillés : `Dev/REX/REX - SQLAlchemy.md`.

## Alternatives

- [[Dev/Services/Prisma|Prisma]] — ORM TypeScript nouvelle génération : schéma déclaratif, client typé et migrations générées.
- [[Dev/Services/SQLModel|SQLModel]] — Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI.

## Liens

- [[ORM]] — le concept (Wiki)
- [[Dev/Services/Alembic|Alembic]] — migrations de schéma pour SQLAlchemy
- [[Comparatif - ORM]] — comparatif des ORM
- Doc : https://docs.sqlalchemy.org/
