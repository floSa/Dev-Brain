---
role: brique
nom: Alembic
alias: [alembic]
pitch: "Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle."
categorie: database/migration
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Flyway]]", "[[Liquibase]]"]
complements: ["[[SQLAlchemy]]", "[[SQLModel]]"]
tags: [migration, relational]
url_docs: https://alembic.sqlalchemy.org/
url_repo: https://github.com/sqlalchemy/alembic
---

# Alembic

<!-- AUTO:BANDEAU:START -->
> Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de **migrations de schéma** pour SQLAlchemy, écrit par le même auteur, Mike Bayer.
Chaque changement est un script Python versionné, relié au précédent par une chaîne de
révisions et tracé dans une table de la base. L'**autogénération** compare les modèles
SQLAlchemy au schéma réel et produit un script de diff. Le reste suit : `ALTER`, branches et
merges de révisions, et exécution offline, qui écrit le SQL sans se connecter à la base.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Versionner l'évolution du schéma d'une application déjà bâtie sur SQLAlchemy | Le schéma doit être décrit en SQL natif ou hors de SQLAlchemy : Alembic dérive ses migrations des modèles |
| Dériver les migrations des modèles ORM par autogénération, plutôt qu'écrire le DDL à la main | L'autogénération ne détecte pas tout — types subtils, renommages, contraintes côté serveur : le script produit se relit toujours |
| Rejouer les migrations de façon déterministe en CI/CD (`alembic upgrade head`) | L'ordre des révisions et les merges de branches divergent entre développeurs : la tête `head` demande de la discipline |
| | Migrations couplées à un ORM TypeScript → [[Prisma]] |

## Mise en œuvre

- Installation — `uv add alembic`, puis `alembic init` pour créer le dossier de versions
- Point d'entrée — CLI : `alembic revision --autogenerate`, `alembic upgrade head`
- Prérequis — un projet SQLAlchemy et ses modèles ; Python
- Exécution — en local ou en CI, single-node ; rien à héberger
- Coût — gratuit, licence MIT

## Écosystème

### Alternatives

- [[Flyway]] — Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build.
- [[Liquibase]] — Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD.

### Compléments

- [[SQLAlchemy]] — Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0. — les modèles dont Alembic dérive les migrations.
- [[SQLModel]] — Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI. — lui délègue ses migrations, comme SQLAlchemy.

## Ressources

- Documentation — https://alembic.sqlalchemy.org/
- Dépôt — https://github.com/sqlalchemy/alembic

## Voir aussi

- [[Migrations de schéma]] — la notion du dossier
- [[Comparatif - Migrations de schéma]] — ce qui départage les outils du dossier
