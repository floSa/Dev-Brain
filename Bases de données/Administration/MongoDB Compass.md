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
complements: ["[[MongoDB]]"]
tags: [db-client, document-db, nosql]
url_docs: https://www.mongodb.com/docs/compass/
url_repo: https://github.com/mongodb-js/compass
---

# MongoDB Compass

<!-- AUTO:BANDEAU:START -->
> Client graphique officiel de MongoDB : exploration de documents, requêtes visuelles et analyse de schéma.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application TypeScript/Electron | source-available | Windows, macOS, Linux | — | à jour · 2026-09-07 |
<!-- AUTO:BANDEAU:END -->

## Définition

Le client graphique officiel de MongoDB, pensé pour le modèle document : navigation dans les
collections, construction visuelle des requêtes et des pipelines d'agrégation, inspection des
index et des plans d'exécution. Sa fonction la plus utile est l'**analyse de schéma** — la
distribution réelle des champs et de leurs types dans une collection, que rien dans un modèle
sans schéma déclaré ne donne autrement.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Explorer une base MongoDB sans écrire de requêtes shell | Centré Mongo : aucun autre moteur |
| Construire et déboguer des pipelines d'agrégation visuellement | Le scripting reproductible reste le domaine de `mongosh` |
| Comprendre la forme réelle des documents — schéma implicite, types hétérogènes | |

## Mise en œuvre

- Installation — installeur Windows, macOS ou Linux
- Point d'entrée — application de bureau : collections, constructeur de requêtes, pipelines d'agrégation
- Prérequis — un serveur MongoDB, auto-hébergé ou sur Atlas ; l'application est en Electron
- Exécution — sur le poste de travail, aucun service à héberger
- Coût — gratuit pour tous depuis 2024 ; source-available sous SSPL

## Écosystème

### Alternatives

- [[DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.

### Compléments

- [[MongoDB]] — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding. — le moteur exploré — le client n'a pas d'objet sans lui

## Ressources

- Documentation — https://www.mongodb.com/docs/compass/

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Clients de bases de données]] — ce qui départage les clients du dossier
