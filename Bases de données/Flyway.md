---
role: brique
nom: Flyway
alias: [flyway]
pitch: "Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build."
categorie: database/migration
famille: cli
licence_type: open-core
maturite: production
langage: Java
alternatives: ["[[Liquibase]]", "[[Alembic]]"]
complements: []
tags: [migration, relational]
url_docs: https://documentation.red-gate.com/flyway
url_repo: https://github.com/flyway/flyway
---

# Flyway

<!-- AUTO:BANDEAU:START -->
> Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| CLI Java | open-core | en ligne de commande, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de migration **SQL-first** : chaque changement est un fichier SQL numéroté
(`V1__init.sql`, `V2__add_table.sql`), appliqué dans l'ordre et tracé dans une table
d'historique. La philosophie est minimaliste — aucun DSL d'abstraction, on écrit le SQL du
moteur cible. Édité par Redgate, avec un cœur ouvert et des éditions payantes pour les
fonctions avancées.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Versionner le schéma en restant au plus près du SQL natif, sans couche d'abstraction | Aucune abstraction : un même changement se réécrit moteur par moteur dès qu'on en cible plusieurs |
| Migrations simples et lisibles, faciles à relire en revue de code | L'undo, donc le rollback, est réservé aux éditions payantes |
| Intégration au build (plugins Maven, Gradle) et exécution en CI/CD | Le tier Teams est fermé aux nouveaux clients depuis mai 2025 : l'entrée payante est désormais Enterprise |
| | Migrations dérivées d'un schéma d'ORM TypeScript → [[Prisma]] |

## Mise en œuvre

- Installation — CLI Java, plugins Maven ou Gradle, ou image Docker
- Point d'entrée — un dossier de fichiers SQL numérotés, appliqués dans l'ordre par la CLI
- Prérequis — une JVM, et le SQL écrit pour le moteur cible
- Exécution — en local ou en CI ; rien à héberger
- Coût — Community gratuite sous Apache 2.0 ; undo, dry-run et certains moteurs en éditions payantes — c'est le modèle open-core

## Écosystème

### Alternatives

- [[Liquibase]] — Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD.
- [[Alembic]] — Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle.

## Ressources

- Documentation — https://documentation.red-gate.com/flyway
- Dépôt — https://github.com/flyway/flyway

## Voir aussi

- [[Migrations de schéma]] — la notion du dossier
- [[Comparatif - Migrations de schéma]] — ce qui départage les outils du dossier
