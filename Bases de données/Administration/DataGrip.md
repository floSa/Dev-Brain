---
role: brique
nom: DataGrip
alias: [datagrip]
pitch: "IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs."
categorie: database/admin
famille: application
domaines: [data-eng]
licence_type: proprietary
os: "Windows, macOS, Linux"
langage: Java/Kotlin
alternatives: ["[[DBeaver]]", "[[HeidiSQL]]"]
complements: []
tags: [db-client, relational, nosql]
url_docs: https://www.jetbrains.com/help/datagrip/
url_repo: 
---

# DataGrip

<!-- AUTO:BANDEAU:START -->
> IDE bases de données de JetBrains : complétion SQL intelligente, refactoring et navigation multi-moteurs.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application Java/Kotlin | propriétaire | Windows, macOS, Linux | — |
<!-- AUTO:BANDEAU:END -->

## Définition

L'IDE base de données de JetBrains. Il apporte au SQL ce qu'un IDE apporte au code :
complétion contextuelle, analyse statique des requêtes, refactoring — renommer une colonne
propage le changement partout —, navigation entre objets et contrôle de version des scripts.
Il parle au relationnel comme à plusieurs bases NoSQL, et repose sur la plateforme IntelliJ,
dont il hérite les raccourcis, les plugins et les thèmes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Écrire beaucoup de SQL et vouloir l'assistance d'un vrai IDE : complétion, refactoring, détection d'erreurs | Empreinte mémoire d'un IDE complet, plus lourde qu'un client minimaliste |
| Déjà investi dans l'écosystème JetBrains — raccourcis, plugins et thèmes communs | |
| Usage non commercial, qui donne accès au plein produit sans payer | |

## Mise en œuvre

- Installation — installeur pour Windows, macOS ou Linux
- Point d'entrée — application de bureau : éditeur SQL, navigation entre objets, versionnage des scripts
- Prérequis — Windows, macOS ou Linux ; plateforme IntelliJ, donc une JVM
- Exécution — sur le poste de travail, aucun service à héberger
- Coût — licence commerciale payante ; gratuit pour l'usage non commercial depuis octobre 2025 (versions ≥ 2025.2.4), à renouveler chaque année

## Écosystème

### Alternatives

- [[DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.
- [[HeidiSQL]] — Client SQL léger pour Windows : MySQL/MariaDB, PostgreSQL, SQL Server et SQLite, gratuit et rapide.

## Ressources

- Documentation — https://www.jetbrains.com/help/datagrip/

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Clients de bases de données]] — ce qui départage les clients du dossier
