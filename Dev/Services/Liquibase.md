---
galaxie: dev
type: service
nom: Liquibase
alias: [liquibase]
pitch: "Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD."
categorie: tooling/migration
licence_type: open-core
hosted: self
maturite: production
langage: Java
scaling: single-node
alternatives: ["[[Dev/Services/Flyway|Flyway]]", "[[Dev/Services/Alembic|Alembic]]"]
remplace_par: []
status: actif
tags: [migration, relational]
url_docs: https://docs.liquibase.com/
url_repo: https://github.com/liquibase/liquibase
---

# Liquibase

## Pourquoi

Gère l'évolution d'un schéma de base comme du code versionné. Les changements sont décrits dans un **changelog** (XML, YAML, JSON ou SQL), chaque `changeSet` étant appliqué une seule fois et tracé dans une table de contrôle. Atouts : abstraction multi-SGBD (un même changelog déclaratif sur plusieurs moteurs), **rollback**, contextes/labels, et intégration CI/CD. Cœur open-source (Apache 2.0), édition Pro commerciale.

## Quand l'utiliser

- Versionner le schéma et rejouer les migrations de façon déterministe entre environnements.
- Besoin d'un format abstrait (YAML/XML) portable entre SGBD, ou de rollback gérés.
- Pipeline CI/CD appliquant les migrations automatiquement au déploiement.

## Quand NE PAS l'utiliser

- Préférence pour des migrations **SQL-first** minimalistes → [[Dev/Services/Flyway|Flyway]].
- Migrations générées et couplées à un ORM TypeScript → [[Dev/Services/Prisma|Prisma]].

## Déploiement & coût

- CLI Java (ou plugins Maven/Gradle, image Docker) exécutée en local ou en CI.
- Cœur gratuit (Apache 2.0) ; fonctions avancées (qualité, observabilité) en édition Pro payante — modèle open-core.

## Pièges

- L'abstraction XML/YAML ajoute une couche : sur un seul SGBD, le SQL brut est parfois plus simple.
- Les rollbacks automatiques ne couvrent pas tous les changements (DDL destructifs) — à tester.
- Retours d'expérience détaillés : `Dev/REX/REX - Liquibase.md`.

## Alternatives

- [[Dev/Services/Flyway|Flyway]] — Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build.
- [[Dev/Services/Alembic|Alembic]] — Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle.

## Liens

- [[Migrations de schéma]] — le concept (Wiki)
- [[Comparatif - Migrations de schéma]] — comparatif des outils de migration
- Doc : https://docs.liquibase.com/
