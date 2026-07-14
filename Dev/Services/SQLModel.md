---
galaxie: dev
type: service
nom: SQLModel
alias: [sqlmodel]
pitch: "Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI."
categorie: framework/orm
licence_type: open-source
hosted: self
maturite: beta
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/SQLAlchemy|SQLAlchemy]]", "[[Dev/Services/Prisma|Prisma]]"]
remplace_par: []
status: actif
tags: [orm, relational, type-hints, data-validation]
url_docs: https://sqlmodel.tiangolo.com/
url_repo: https://github.com/fastapi/sqlmodel
---

# SQLModel

## Pourquoi

Couche fine qui réconcilie [[Dev/Services/Pydantic|Pydantic]] (validation, sérialisation) et [[Dev/Services/SQLAlchemy|SQLAlchemy]] (ORM, accès SQL) : une classe `SQLModel` est **à la fois** un modèle Pydantic et une table SQLAlchemy. Une seule définition typée sert de schéma de validation des entrées, de modèle de réponse et d'entité persistée — pas de duplication entre couche API et couche données. Écrit par Sebastián Ramírez (tiangolo), auteur de [[Dev/Services/FastAPI|FastAPI]], avec lequel l'intégration est l'usage de référence.

## Quand l'utiliser

- App [[Dev/Services/FastAPI|FastAPI]] voulant partager une seule définition de modèle entre validation HTTP et persistance.
- Besoin du typage et de la validation Pydantic *plus* d'un ORM, sans maintenir deux jeux de classes en parallèle.
- CRUD simple à modéré où l'on accepte de redescendre vers SQLAlchemy pour les requêtes pointues.

## Quand NE PAS l'utiliser

- Contrôle fin du SQL, requêtes complexes, async avancé → [[Dev/Services/SQLAlchemy|SQLAlchemy]] directement (SQLModel n'expose qu'une partie de son API).
- Stack TypeScript / Node → [[Dev/Services/Prisma|Prisma]].
- Projet exigeant une API stable et figée : SQLModel est encore en **0.0.x** (pré-1.0), l'API peut bouger.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite, intégrée à l'application. Tire [[Dev/Services/Pydantic|Pydantic]] et [[Dev/Services/SQLAlchemy|SQLAlchemy]] comme dépendances.
- Pas de service à héberger : single-node, suit le déploiement de l'app. Migrations de schéma déléguées à [[Dev/Services/Alembic|Alembic]] (comme SQLAlchemy).

## Pièges

- **Pré-1.0** (0.0.x) : périmètre volontairement réduit ; certaines fonctions SQLAlchemy ne sont accessibles qu'en retombant sur l'API sous-jacente.
- Double héritage Pydantic + table : bien distinguer les modèles `table=True` (persistés) des modèles de données purs (DTO de validation), sinon confusion entre schéma API et schéma BDD.
- Hérite des pièges SQLAlchemy : requêtes **N+1**, chargement paresseux.
- Retours d'expérience détaillés : `Dev/REX/REX - SQLModel.md`.

## Alternatives

- [[Dev/Services/SQLAlchemy|SQLAlchemy]] — Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0.
- [[Dev/Services/Prisma|Prisma]] — ORM TypeScript nouvelle génération : schéma déclaratif, client typé et migrations générées.

## Liens

- [[ORM]] — le concept (Wiki)
- [[Dev/Services/SQLAlchemy|SQLAlchemy]] — socle ORM/SQL sur lequel SQLModel s'appuie
- [[Dev/Services/Pydantic|Pydantic]] — socle de validation/typage
- [[Dev/Services/FastAPI|FastAPI]] — intégration de référence (même auteur)
- [[Dev/Services/Alembic|Alembic]] — migrations de schéma
- [[Comparatif - ORM]] — comparatif des ORM
- Doc : https://sqlmodel.tiangolo.com/
