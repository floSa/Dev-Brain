---
galaxie: dev
type: outil
nom: MongoDB Compass
alias: [compass, mongodb compass]
pitch: "Client graphique officiel de MongoDB : exploration de documents, requêtes visuelles et analyse de schéma."
categorie: tooling/db-admin
domaines: [data-eng]
licence_type: source-available
os: "Windows, macOS, Linux"
langage: TypeScript/Electron
status: actif
alternatives: ["[[Dev/Outils/DBeaver|DBeaver]]"]
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

- Mêler MongoDB et des bases relationnelles dans un seul outil → [[Dev/Outils/DBeaver|DBeaver]] (Mongo en édition payante).
- Préférer le shell `mongosh` pour le scripting reproductible.

## Bases & plateformes

- MongoDB (serveur auto-hébergé et Atlas).
- Windows, macOS, Linux (application Electron).

## Pièges

- L'analyse de schéma porte sur un **échantillon** : non exhaustive sur de très grosses collections.
- Centré Mongo : aucun autre moteur.

## Alternatives

- [[Dev/Outils/DBeaver|DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Dev/Services/MongoDB|MongoDB]] — le moteur exploré
- [[Comparatif - Clients de bases de données]] — comparatif des clients GUI
- Doc : https://www.mongodb.com/docs/compass/
