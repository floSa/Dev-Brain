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

<!-- AUTO:BANDEAU:START -->
> ORM TypeScript nouvelle génération : schéma déclaratif, client typé et migrations générées.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie TypeScript | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

ORM de l'écosystème Node et TypeScript. Un fichier `schema.prisma` déclaratif décrit le
modèle ; Prisma en génère un **client typé** — autocomplétion et vérification de types de
bout en bout sur les requêtes — et les **migrations** correspondantes, via `prisma migrate`.
Il couvre Postgres, MySQL, SQL Server, SQLite et MongoDB. La v7, en 2025, a remplacé le
moteur de requêtes Rust par du TypeScript pur, ce qui réduit les démarrages à froid — un gain
qui compte en serverless.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Backend TypeScript ou Node voulant un accès aux données fortement typé | Écosystème **TypeScript** avant tout : le client Python est communautaire, ce n'est pas l'usage principal |
| Schéma déclaratif unique servant à la fois de modèle, de client et de source des migrations | L'abstraction gêne les requêtes très complexes, ou les fonctionnalités propres à un moteur qu'elle masque : il faut alors redescendre au SQL brut |
| Déploiement serverless sensible au cold start, depuis la v7 | Stack Python — data, ML, [[FastAPI]] → un ORM Python ([[SQLAlchemy]]) ou un outil de migration dédié, [[Liquibase]] ou [[Flyway]] |

## Mise en œuvre

- Installation — bibliothèque et CLI Node, installées avec l'application
- Point d'entrée — le fichier `schema.prisma`, le client généré, et `prisma migrate` pour les migrations
- Prérequis — une stack Node/TypeScript ; Postgres, MySQL, SQL Server, SQLite ou MongoDB comme cible
- Exécution — dans le process de l'application, single-node ; rien à héberger
- Coût — gratuit, licence Apache 2.0 ; les services managés optionnels (Accelerate, Postgres hébergé) sont payants

## Écosystème

### Alternatives

- [[SQLAlchemy]] — Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0.
- [[SQLModel]] — Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI.

## Ressources

- Documentation — https://www.prisma.io/docs
- Dépôt — https://github.com/prisma/prisma

## Voir aussi

- [[ORM]] — la notion du dossier
- [[Migrations de schéma]] — la notion dont relève Prisma Migrate
- [[Comparatif - ORM]] — ce qui départage les ORM du dossier
