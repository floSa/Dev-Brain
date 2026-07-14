---
galaxie: dev
type: outil
nom: DataGrip
alias: [datagrip]
pitch: "IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs."
categorie: tooling/db-admin
domaines: [data-eng]
licence_type: proprietary
os: "Windows, macOS, Linux"
langage: Java/Kotlin
status: actif
alternatives: ["[[Dev/Outils/DBeaver|DBeaver]]", "[[Dev/Outils/HeidiSQL|HeidiSQL]]"]
tags: [db-client, relational, nosql]
url_docs: https://www.jetbrains.com/datagrip/documentation/
url_repo: 
---

# DataGrip

## Pourquoi

L'IDE base de données de JetBrains. Apporte au SQL ce que les IDE apportent au code : **complétion contextuelle**, analyse statique des requêtes, refactoring (renommer une colonne propage partout), navigation entre objets, contrôle de version des scripts. Multi-moteurs (relationnel + plusieurs NoSQL). Depuis octobre 2025, **gratuit pour usage non commercial** ; licence commerciale payante sinon.

## Quand l'utiliser

- Écrire beaucoup de SQL et vouloir l'assistance d'un vrai IDE (complétion, refactoring, détection d'erreurs).
- Déjà investi dans l'écosystème JetBrains (raccourcis, plugins, thèmes communs).
- Usage non commercial (apprentissage, perso) qui bénéficie du plein produit gratuitement.

## Quand NE PAS l'utiliser

- Besoin d'un outil 100 % libre et gratuit en contexte commercial → [[Dev/Outils/DBeaver|DBeaver]].
- Poste léger, démarrage instantané sous Windows → [[Dev/Outils/HeidiSQL|HeidiSQL]].

## Bases & plateformes

- Relationnel (Postgres, MySQL, Oracle, SQL Server…) et plusieurs NoSQL (Mongo, Redis, Cassandra).
- Windows, macOS, Linux (plateforme IntelliJ, JVM).

## Pièges

- Produit **propriétaire** : la gratuité ne couvre que l'usage non commercial (≥ 2025.2.4), renouvelable annuellement.
- Empreinte mémoire d'un IDE complet, plus lourde qu'un client minimaliste.

## Alternatives

- [[Dev/Outils/DBeaver|DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.
- [[Dev/Outils/HeidiSQL|HeidiSQL]] — Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Clients de bases de données]] — comparatif des clients GUI
- Doc : https://www.jetbrains.com/datagrip/documentation/
