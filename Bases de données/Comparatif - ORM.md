---
role: comparatif
nom: Comparatif - ORM
categorie: database/orm
tags: [orm]
---

# Comparatif - ORM

> On tranche sur : le langage de la stack, et la quantité de SQL qu'on veut garder sous la main.

![[Comparatif - ORM.base]]

## Ce qui départage

- [[SQLAlchemy]] — deux couches : l'ORM pour le CRUD, Core pour le SQL complexe ; la migration de schéma n'est pas incluse, c'est [[Alembic]].
- [[SQLModel]] — une seule classe typée sert de modèle Pydantic **et** de table SQLAlchemy, mais elle est en 0.0.x et n'expose qu'une partie de l'API sous-jacente.
- [[Prisma]] — le seul TypeScript : schéma déclaratif unique, client typé et migrations générées ; le client Python est communautaire.
