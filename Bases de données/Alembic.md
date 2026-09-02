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
complements: []
tags: [migration, relational]
url_docs: https://alembic.sqlalchemy.org/
url_repo: https://github.com/sqlalchemy/alembic
---

# Alembic

## Pourquoi

Outil de **migrations de schéma** pour [[SQLAlchemy]], écrit par le même auteur (Mike Bayer). Chaque changement est un script Python versionné, relié au précédent (révisions chaînées) et tracé en base. L'**autogénération** compare les modèles SQLAlchemy au schéma réel et produit un script de diff à relire. Gère les `ALTER`, les branches/merges de révisions et l'exécution offline (SQL généré sans connexion).

## Quand l'utiliser

- Versionner l'évolution du schéma d'une app qui utilise SQLAlchemy.
- Dériver les migrations des modèles ORM via l'autogénération.
- Rejouer les migrations de façon déterministe en CI/CD avant déploiement (`alembic upgrade head`).

## Quand NE PAS l'utiliser

- Projet sans SQLAlchemy, ou migrations SQL-first / multi-SGBD → [[Flyway]] ou [[Liquibase]].
- Migrations couplées à un ORM TypeScript → [[Prisma]].

## Déploiement & coût

- Bibliothèque / CLI open-source (MIT), gratuite ; installée avec l'app, exécutée en local ou en CI.
- Pas de service à héberger : single-node.

## Pièges

- L'autogénération ne détecte pas tout (changements de type subtils, renommages, contraintes côté serveur) → **toujours relire** le script généré.
- L'ordre des révisions et les merges de branches peuvent diverger entre développeurs → discipline sur la révision `head`.

## Alternatives

- [[Flyway]] — Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build.
- [[Liquibase]] — Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD.

## Liens

- [[Migrations de schéma]] — le concept (Wiki)
- [[SQLAlchemy]] — l'ORM dont Alembic dérive les migrations
- [[Comparatif - Migrations de schéma]] — comparatif des outils de migration
- Doc : https://alembic.sqlalchemy.org/
