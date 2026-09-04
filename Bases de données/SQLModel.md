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
complements: ["[[Pydantic]]", "[[FastAPI]]", "[[Alembic]]"]
tags: [orm, relational, type-hints, data-validation]
url_docs: https://sqlmodel.tiangolo.com/
url_repo: https://github.com/fastapi/sqlmodel
---

# SQLModel

<!-- AUTO:BANDEAU:START -->
> Une couche fine au-dessus de Pydantic et SQLAlchemy : une seule classe typée sert à la fois de modèle de validation et de table ORM, taillée pour FastAPI.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

Couche fine qui réconcilie Pydantic — validation, sérialisation — et SQLAlchemy — ORM, accès
SQL : une classe `SQLModel` est **à la fois** un modèle Pydantic et une table SQLAlchemy. Une
seule définition typée sert de schéma de validation des entrées, de modèle de réponse et
d'entité persistée, sans duplication entre couche API et couche données. Écrite par Sebastián
Ramírez, auteur de FastAPI, avec lequel l'intégration est l'usage de référence.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Application FastAPI voulant partager une seule définition de modèle entre validation HTTP et persistance | Périmètre volontairement réduit : SQLModel n'expose qu'une partie de l'API SQLAlchemy, et les requêtes pointues imposent d'y redescendre |
| Typage et validation Pydantic **plus** un ORM, sans maintenir deux jeux de classes en parallèle | Pré-1.0, en 0.0.x : un projet qui exige une API stable et figée ne peut pas s'appuyer dessus |
| CRUD simple à modéré, en acceptant de redescendre au besoin vers la couche sous-jacente | Double héritage Pydantic + table : confondre les modèles `table=True` et les DTO de validation mélange schéma API et schéma de base |
| | Elle hérite des pièges de sa couche ORM : requêtes N+1, chargement paresseux |

## Mise en œuvre

- Installation — `uv add sqlmodel` ; tire Pydantic et SQLAlchemy comme dépendances
- Point d'entrée — une classe `SQLModel`, avec `table=True` pour les entités persistées
- Prérequis — Python ; les migrations de schéma se délèguent à un outil distinct
- Exécution — dans le process de l'application, single-node ; rien à héberger
- Coût — gratuit, licence MIT

## Écosystème

### Alternatives

- [[SQLAlchemy]] — Toolkit SQL et ORM Python de référence : couche Core d'expression SQL + ORM Data Mapper, entièrement typé depuis la 2.0.
- [[Prisma]] — ORM TypeScript nouvelle génération : schéma déclaratif, client typé et migrations générées.

### Compléments

- [[Pydantic]] — Validation de données pilotée par les annotations de type Python, avec un cœur de validation en Rust : parsing, coercition et erreurs claires. — le socle de validation et de typage.
- [[FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement. — l'intégration de référence, du même auteur.
- [[Alembic]] — Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle. — les migrations de schéma, que SQLModel ne fait pas.

## Ressources

- Documentation — https://sqlmodel.tiangolo.com/
- Dépôt — https://github.com/fastapi/sqlmodel

## Voir aussi

- [[ORM]] — la notion du dossier
- [[Comparatif - ORM]] — ce qui départage les ORM du dossier
