---
role: comparatif
nom: Comparatif - Migrations de schéma
categorie: database/migration
tags: [migration]
---

# Comparatif - Migrations de schéma

> On tranche sur : du SQL écrit à la main, un format abstrait portable, ou un diff généré depuis l'ORM.

![[Comparatif - Migrations de schéma.base]]

## Ce qui départage

- [[Alembic]] — dérive les migrations des modèles [[SQLAlchemy]] par autogénération, qui ne détecte pas tout et se relit toujours.
- [[Flyway]] — SQL-first, aucune abstraction : un fichier numéroté par version, à réécrire par moteur si l'on en cible plusieurs, et l'undo est réservé aux éditions payantes.
- [[Liquibase]] — changelog XML/YAML/JSON portable entre SGBD, avec rollback, au prix d'une couche d'abstraction de plus.
