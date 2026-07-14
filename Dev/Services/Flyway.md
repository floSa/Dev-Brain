---
galaxie: dev
type: service
nom: Flyway
alias: [flyway]
pitch: "Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build."
categorie: tooling/migration
licence_type: open-core
hosted: self
maturite: production
langage: Java
scaling: single-node
alternatives: ["[[Dev/Services/Liquibase|Liquibase]]", "[[Dev/Services/Alembic|Alembic]]"]
remplace_par: []
status: actif
tags: [migration, relational]
url_docs: https://documentation.red-gate.com/flyway
url_repo: https://github.com/flyway/flyway
---

# Flyway

## Pourquoi

Outil de migration **SQL-first** : les changements sont des fichiers SQL numérotés (`V1__init.sql`, `V2__add_table.sql`) appliqués dans l'ordre et tracés dans une table d'historique. Philosophie minimaliste — pas de DSL d'abstraction, on écrit le SQL du moteur cible. Cœur open-source (Apache 2.0) ; édité par Redgate, avec des éditions payantes (Team/Enterprise) pour les fonctions avancées.

## Quand l'utiliser

- Versionner le schéma en restant proche du SQL natif, sans couche d'abstraction.
- Migrations simples, lisibles, faciles à relire en revue de code.
- Intégration au build (plugins Maven/Gradle) et exécution en CI/CD.

## Quand NE PAS l'utiliser

- Besoin d'un format abstrait portable multi-SGBD ou de rollbacks structurés → [[Dev/Services/Liquibase|Liquibase]].
- Migrations dérivées d'un schéma d'ORM TypeScript → [[Dev/Services/Prisma|Prisma]].

## Déploiement & coût

- CLI Java, plugins Maven/Gradle, image Docker ; exécution locale ou en CI.
- Community gratuite (Apache 2.0) ; fonctions avancées (undo, dry-run, certains moteurs) en éditions payantes — modèle open-core. Tier Teams fermé aux nouveaux clients depuis mai 2025 (orientation Enterprise).

## Pièges

- Pas d'abstraction : un même changement doit être réécrit par moteur si l'on cible plusieurs SGBD.
- L'undo (rollback) est réservé aux éditions payantes.
- Retours d'expérience détaillés : `Dev/REX/REX - Flyway.md`.

## Alternatives

- [[Dev/Services/Liquibase|Liquibase]] — Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD.
- [[Dev/Services/Alembic|Alembic]] — Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle.

## Liens

- [[Migrations de schéma]] — le concept (Wiki)
- [[Comparatif - Migrations de schéma]] — comparatif des outils de migration
- Doc : https://documentation.red-gate.com/flyway
