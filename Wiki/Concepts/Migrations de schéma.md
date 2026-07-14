---
galaxie: wiki
type: concept
nom: Migrations de schéma
alias: [migration, migrations, schema migration, db migration]
categorie: concept/data
domaines: [data-eng]
tags: [migration, relational]
---

# Migrations de schéma

## Aperçu

- Faire évoluer la **structure** d'une base (tables, colonnes, index, contraintes) de façon contrôlée et reproductible, au même titre que le code.
- Chaque changement est un script versionné, appliqué une seule fois et tracé : la base passe d'une version connue à la suivante de manière déterministe.

## Concepts clés

### Migration versionnée
- Une suite ordonnée de scripts (numérotés ou horodatés), chacun appliqué une fois et enregistré dans une table d'historique.
- Garantit que tous les environnements (dev, CI, prod) convergent vers le même schéma.

### Forward-only vs rollback
- Forward-only : on n'écrit que des migrations « en avant » ; pour annuler, on écrit une nouvelle migration corrective.
- Rollback : chaque migration porte son inverse (`down`) — pratique mais impossible pour les changements destructifs (données perdues).

### Déclaratif vs impératif
- Impératif / SQL-first : on écrit explicitement le DDL de chaque étape ([[Dev/Services/Flyway|Flyway]]).
- Déclaratif : on décrit l'état cible (changelog abstrait [[Dev/Services/Liquibase|Liquibase]], ou schéma d'ORM) et l'outil génère le diff.

## En pratique

- Versionner les migrations dans le dépôt, à côté du code applicatif.
- Les rejouer automatiquement en CI/CD avant le déploiement.
- Pièges : migrations non idempotentes, changements destructifs sans sauvegarde, dérive entre le schéma réel et les scripts (modifications manuelles en prod).
- Migrations longues (gros `ALTER`) : verrous et indisponibilité — prévoir des stratégies en ligne.

## Approches voisines & alternatives

- Outils dédiés (Dev) : [[Dev/Services/Liquibase|Liquibase]] (changelog multi-SGBD), [[Dev/Services/Flyway|Flyway]] (SQL-first).
- Migrations intégrées à un ORM : [[Dev/Services/Prisma|Prisma]] (Prisma Migrate), ou côté Python [[Dev/Services/Alembic|Alembic]] (couplé à [[Dev/Services/SQLAlchemy|SQLAlchemy]]).
- Concept parent : [[Wiki/Concepts/Bases de données|Bases de données]].

## Pour aller plus loin

- Comparatif des outils de migration : [[Comparatif - Migrations de schéma]] (vue Dev).
- Notion connexe : [[ORM]] (les ORM embarquent souvent leur propre moteur de migration).
