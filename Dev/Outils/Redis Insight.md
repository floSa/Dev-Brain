---
galaxie: dev
type: outil
nom: Redis Insight
alias: [redisinsight, redis insight]
pitch: "Client graphique officiel de Redis : exploration des clés, profiling et workbench pour modules (JSON, Search)."
categorie: tooling/db-admin
domaines: [data-eng]
licence_type: source-available
os: "Windows, macOS, Linux, web (Docker)"
langage: TypeScript/Electron
status: actif
alternatives: ["[[Dev/Outils/DBeaver|DBeaver]]"]
tags: [db-client, key-value, in-memory]
url_docs: https://redis.io/docs/latest/develop/tools/insight/
url_repo: https://github.com/redis/RedisInsight
---

# Redis Insight

## Pourquoi

Le client graphique **officiel** de Redis. Navigation dans l'espace de clés (par type : strings, hashes, listes, streams…), workbench pour exécuter des commandes avec coloration et aide, et surtout un support de premier ordre des **modules** Redis (JSON, Search/query, séries temporelles). Outils d'analyse mémoire et de profilage des commandes lentes. Source-available sous SSPLv1, gratuit.

## Quand l'utiliser

- Inspecter et éditer le contenu d'une instance Redis sans `redis-cli`.
- Exploiter les modules (RedisJSON, RediSearch) avec une UI dédiée.
- Diagnostiquer l'usage mémoire et repérer les commandes lentes.

## Quand NE PAS l'utiliser

- Mêler Redis et d'autres SGBD dans un seul outil → [[Dev/Outils/DBeaver|DBeaver]] (support Redis).
- Scripting reproductible → `redis-cli`.

## Bases & plateformes

- Redis (auto-hébergé et Redis Cloud), modules inclus.
- Windows, macOS, Linux (Electron) ou conteneur Docker (UI web).

## Pièges

- Licence SSPL : pas une licence OSI, à vérifier selon le contexte de redistribution.
- Centré Redis : aucun autre moteur.

## Alternatives

- [[Dev/Outils/DBeaver|DBeaver]] — Client SQL universel open-source : un seul outil pour Postgres, MySQL, Oracle, Mongo et 80+ bases.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Dev/Services/Redis|Redis]] — le moteur exploré
- [[Comparatif - Clients de bases de données]] — comparatif des clients GUI
- Doc : https://redis.io/docs/latest/develop/tools/insight/
