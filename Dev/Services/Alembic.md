---
galaxie: dev
type: service
nom: Alembic
alias: [alembic]
pitch: "Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle."
categorie: tooling/migration
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Flyway|Flyway]]", "[[Dev/Services/Liquibase|Liquibase]]"]
remplace_par: []
status: actif
tags: [migration, relational]
url_docs: https://alembic.sqlalchemy.org/
url_repo: https://github.com/sqlalchemy/alembic
---

# Alembic

## Pourquoi

Outil de **migrations de schéma** pour [[Dev/Services/SQLAlchemy|SQLAlchemy]], écrit par le même auteur (Mike Bayer). Chaque changement est un script Python versionné, relié au précédent (révisions chaînées) et tracé en base. L'**autogénération** compare les modèles SQLAlchemy au schéma réel et produit un script de diff à relire. Gère les `ALTER`, les branches/merges de révisions et l'exécution offline (SQL généré sans connexion).

## Quand l'utiliser

- Versionner l'évolution du schéma d'une app qui utilise SQLAlchemy.
- Dériver les migrations des modèles ORM via l'autogénération.
- Rejouer les migrations de façon déterministe en CI/CD avant déploiement (`alembic upgrade head`).

## Quand NE PAS l'utiliser

- Projet sans SQLAlchemy, ou migrations SQL-first / multi-SGBD → [[Dev/Services/Flyway|Flyway]] ou [[Dev/Services/Liquibase|Liquibase]].
- Migrations couplées à un ORM TypeScript → [[Dev/Services/Prisma|Prisma]].

## Déploiement & coût

- Bibliothèque / CLI open-source (MIT), gratuite ; installée avec l'app, exécutée en local ou en CI.
- Pas de service à héberger : single-node.

## Pièges

- L'autogénération ne détecte pas tout (changements de type subtils, renommages, contraintes côté serveur) → **toujours relire** le script généré.
- L'ordre des révisions et les merges de branches peuvent diverger entre développeurs → discipline sur la révision `head`.
- Retours d'expérience détaillés : `Dev/REX/REX - Alembic.md`.

## Alternatives

- [[Dev/Services/Flyway|Flyway]] — Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build.
- [[Dev/Services/Liquibase|Liquibase]] — Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD.

## Liens

- [[Migrations de schéma]] — le concept (Wiki)
- [[Dev/Services/SQLAlchemy|SQLAlchemy]] — l'ORM dont Alembic dérive les migrations
- [[Comparatif - Migrations de schéma]] — comparatif des outils de migration
- Doc : https://alembic.sqlalchemy.org/
