---
role: brique
nom: Redis Insight
alias: [redisinsight, redis insight]
pitch: "Client graphique officiel de Redis : exploration des clés, profiling et workbench pour modules (JSON, Search)."
categorie: database/admin
famille: application
domaines: [data-eng]
licence_type: source-available
os: "Windows, macOS, Linux, web (Docker)"
langage: TypeScript/Electron
alternatives: ["[[DBeaver]]"]
complements: ["[[Redis]]"]
tags: [db-client, key-value, in-memory]
url_docs: https://redis.io/docs/latest/develop/tools/insight/
url_repo: https://github.com/redis/RedisInsight
---

# Redis Insight

<!-- AUTO:BANDEAU:START -->
> Client graphique officiel de Redis : exploration des clés, profiling et workbench pour modules (JSON, Search).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application TypeScript/Electron | source-available | Windows, macOS, Linux, web (Docker) | — | à jour · 2026-07-21 |
<!-- AUTO:BANDEAU:END -->

## Définition

Le client graphique officiel de Redis : navigation dans l'espace de clés par type — chaînes,
hashes, listes, streams —, workbench pour exécuter des commandes avec coloration et aide en
ligne, et surtout un support de premier plan des **modules** (JSON, Search et query, séries
temporelles). Il embarque aussi de quoi analyser l'usage mémoire et profiler les commandes
lentes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Inspecter et éditer le contenu d'une instance Redis sans passer par `redis-cli` | Centré Redis : aucun autre moteur |
| Exploiter les modules RedisJSON ou RediSearch avec une interface dédiée | La licence SSPL n'est pas une licence OSI — à vérifier dès qu'il y a redistribution |
| Diagnostiquer l'usage mémoire et repérer les commandes lentes | Le scripting reproductible reste le domaine de `redis-cli` |

## Mise en œuvre

- Installation — installeur Windows, macOS ou Linux, ou conteneur Docker pour l'interface web
- Point d'entrée — navigateur d'espace de clés et workbench de commandes
- Prérequis — une instance Redis, auto-hébergée ou sur Redis Cloud ; l'application est en Electron
- Exécution — sur le poste de travail, ou en conteneur servant l'interface web
- Coût — gratuit ; source-available sous SSPLv1

## Écosystème

### Alternatives

- [[DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.

### Compléments

- [[Redis]] — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub. — le moteur exploré — le client n'a pas d'objet sans lui

## Ressources

- Documentation — https://redis.io/docs/latest/develop/tools/insight/

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Clients de bases de données]] — ce qui départage les clients du dossier
