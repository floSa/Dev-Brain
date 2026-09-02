---
role: brique
nom: SQLModel
alias: [sqlmodel]
pitch: "Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI."
categorie: database/orm
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[SQLAlchemy]]", "[[Prisma]]"]
complements: []
tags: [orm, relational, type-hints, data-validation]
url_docs: https://sqlmodel.tiangolo.com/
url_repo: https://github.com/fastapi/sqlmodel
---

# SQLModel

## Pourquoi

Couche fine qui réconcilie [[Pydantic]] (validation, sérialisation) et [[SQLAlchemy]] (ORM, accès SQL) : une classe `SQLModel` est **à la fois** un modèle Pydantic et une table SQLAlchemy. Une seule définition typée sert de schéma de validation des entrées, de modèle de réponse et d'entité persistée — pas de duplication entre couche API et couche données. Écrit par Sebastián Ramírez (tiangolo), auteur de [[FastAPI]], avec lequel l'intégration est l'usage de référence.

## Quand l'utiliser

- App [[FastAPI]] voulant partager une seule définition de modèle entre validation HTTP et persistance.
- Besoin du typage et de la validation Pydantic *plus* d'un ORM, sans maintenir deux jeux de classes en parallèle.
- CRUD simple à modéré où l'on accepte de redescendre vers SQLAlchemy pour les requêtes pointues.

## Quand NE PAS l'utiliser

- Contrôle fin du SQL, requêtes complexes, async avancé → [[SQLAlchemy]] directement (SQLModel n'expose qu'une partie de son API).
- Stack TypeScript / Node → [[Prisma]].
- Projet exigeant une API stable et figée : SQLModel est encore en **0.0.x** (pré-1.0), l'API peut bouger.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite, intégrée à l'application. Tire [[Pydantic]] et [[SQLAlchemy]] comme dépendances.
- Pas de service à héberger : single-node, suit le déploiement de l'app. Migrations de schéma déléguées à [[Alembic]] (comme SQLAlchemy).

## Pièges

- **Pré-1.0** (0.0.x) : périmètre volontairement réduit ; certaines fonctions SQLAlchemy ne sont accessibles qu'en retombant sur l'API sous-jacente.
- Double héritage Pydantic + table : bien distinguer les modèles `table=True` (persistés) des modèles de données purs (DTO de validation), sinon confusion entre schéma API et schéma BDD.
- Hérite des pièges SQLAlchemy : requêtes **N+1**, chargement paresseux.

## Alternatives

- [[SQLAlchemy]] — Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0.
- [[Prisma]] — ORM TypeScript nouvelle génération : schéma déclaratif, client typé et migrations générées.

## Liens

- [[ORM]] — le concept (Wiki)
- [[SQLAlchemy]] — socle ORM/SQL sur lequel SQLModel s'appuie
- [[Pydantic]] — socle de validation/typage
- [[FastAPI]] — intégration de référence (même auteur)
- [[Alembic]] — migrations de schéma
- [[Comparatif - ORM]] — comparatif des ORM
- Doc : https://sqlmodel.tiangolo.com/
