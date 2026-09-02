---
role: brique
nom: MongoDB Compass
alias: [compass, mongodb compass]
pitch: "Client graphique officiel de MongoDB : exploration de documents, requêtes visuelles et analyse de schéma."
categorie: database/admin
famille: application
domaines: [data-eng]
licence_type: source-available
os: "Windows, macOS, Linux"
langage: TypeScript/Electron
alternatives: ["[[DBeaver]]"]
complements: []
tags: [db-client, document-db, nosql]
url_docs: https://www.mongodb.com/docs/compass/
url_repo: https://github.com/mongodb-js/compass
---

# MongoDB Compass

## Pourquoi

Le client graphique **officiel** de MongoDB. Pensé pour le modèle document : navigation dans les collections, construction visuelle de requêtes et de pipelines d'agrégation, **analyse de schéma** (distribution des champs et types sur un échantillon), inspection des index et plans d'exécution. Source-available sous SSPL, et gratuit pour tous depuis 2024.

## Quand l'utiliser

- Explorer une base MongoDB sans écrire de requêtes shell.
- Construire et déboguer des pipelines d'agrégation visuellement.
- Comprendre la forme réelle des documents (schéma implicite, types hétérogènes).

## Quand NE PAS l'utiliser

- Mêler MongoDB et des bases relationnelles dans un seul outil → [[DBeaver]] (Mongo en édition payante).
- Préférer le shell `mongosh` pour le scripting reproductible.

## Bases & plateformes

- MongoDB (serveur auto-hébergé et Atlas).
- Windows, macOS, Linux (application Electron).

## Pièges

- L'analyse de schéma porte sur un **échantillon** : non exhaustive sur de très grosses collections.
- Centré Mongo : aucun autre moteur.

## Alternatives

- [[DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.

## Liens

- [[Bases de données]] — le concept (Wiki)
- [[MongoDB]] — le moteur exploré
- [[Comparatif - Clients de bases de données]] — comparatif des clients GUI
- Doc : https://www.mongodb.com/docs/compass/
