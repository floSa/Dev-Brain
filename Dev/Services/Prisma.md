---
role: brique
nom: Prisma
alias: [prisma, prisma orm]
pitch: "ORM TypeScript nouvelle génération : schéma déclaratif, client typé et migrations générées."
categorie: database/orm
famille: paquet
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: ["[[SQLAlchemy]]", "[[SQLModel]]"]
complements: []
tags: [orm, relational]
url_docs: https://www.prisma.io/docs
url_repo: https://github.com/prisma/prisma
---

# Prisma

## Pourquoi

ORM de l'écosystème Node/TypeScript. Un fichier `schema.prisma` déclaratif décrit le modèle ; Prisma génère un **client typé** (autocomplétion et vérification de types de bout en bout sur les requêtes) et les **migrations** correspondantes (`prisma migrate`). Couvre Postgres, MySQL, SQL Server, SQLite et MongoDB. La v7 (2025) a remplacé le moteur de requêtes Rust par du TypeScript pur, réduisant les démarrages à froid (utile en serverless).

## Quand l'utiliser

- Backend TypeScript/Node voulant un accès aux données fortement typé et une bonne DX.
- Schéma déclaratif unique servant à la fois de modèle, de client et de source des migrations.
- Déploiement serverless sensible au cold start (v7).

## Quand NE PAS l'utiliser

- Stack Python ([[FastAPI]], data/ML) → privilégier un ORM Python ([[SQLAlchemy]]) ou un outil de migration dédié comme [[Liquibase]] / [[Flyway]].
- Besoin de SQL très fin / fonctionnalités spécifiques d'un moteur que l'ORM masque.

## Déploiement & coût

- Bibliothèque/CLI Node, intégrée à l'application ; open-source (Apache 2.0).
- Services managés optionnels (Accelerate, Postgres hébergé) payants, mais l'ORM lui-même est gratuit.

## Pièges

- Écosystème **TypeScript** avant tout : le client Python est communautaire, pas l'usage principal.
- L'abstraction peut gêner les requêtes très complexes (recours au SQL brut alors nécessaire).

## Alternatives

- [[SQLAlchemy]] — Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0.
- [[SQLModel]] — Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI.

## Liens

- [[ORM]] — le concept (Wiki)
- [[Migrations de schéma]] — Prisma Migrate relève de ce concept
- [[Comparatif - ORM]] — comparatif des ORM
- Doc : https://www.prisma.io/docs
