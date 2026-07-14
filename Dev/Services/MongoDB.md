---
galaxie: dev
type: service
nom: MongoDB
alias: [mongo, mongodb]
pitch: "Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding."
categorie: database/document
licence_type: source-available
hosted: both
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Dev/Services/Redis|Redis]]", "[[Dev/Services/Apache Cassandra|Apache Cassandra]]"]
remplace_par: []
status: actif
tags: [nosql, document-db]
url_docs: https://www.mongodb.com/docs/
url_repo: https://github.com/mongodb/mongo
---

# MongoDB

## Pourquoi

Base NoSQL orientée **documents** : chaque enregistrement est un document BSON (JSON binaire) à schéma libre, regroupé en collections. On stocke l'objet tel qu'il est manipulé côté application, sans migration de schéma à chaque évolution du modèle. Requêtes riches, index secondaires, pipeline d'agrégation, et scale horizontal natif via réplica sets (haute dispo) et sharding (partitionnement).

## Quand l'utiliser

- Données semi-structurées ou au schéma mouvant (catalogues, profils, contenus, événements).
- Modèle agrégat : l'objet métier se lit et s'écrit d'un bloc, peu de relations transverses.
- Besoin de scaler horizontalement en écriture sans réarchitecturer (sharding intégré).
- Prototypage rapide où le schéma n'est pas encore figé.

## Quand NE PAS l'utiliser

- Fortes garanties relationnelles, jointures complexes, intégrité référentielle → [[Dev/Services/Postgres|Postgres]] (dont le `JSONB` couvre déjà le semi-structuré modéré).
- Cache ou structures en mémoire à très faible latence → [[Dev/Services/Redis|Redis]].
- Écritures massives en colonnes larges multi-datacenter → [[Dev/Services/Apache Cassandra|Apache Cassandra]].

## Déploiement & coût

- Self-host (Docker, paquet) ou managé via **MongoDB Atlas** (AWS/GCP/Azure).
- Réplica set pour la HA, sharding pour le volume ; lectures distribuables sur les secondaires.
- Licence **SSPL** (source-available, non reconnue OSI) depuis 2018 : gratuit en self-host, mais l'offre « as a service » est contrainte — Atlas pour le managé sans friction.

## Pièges

- Pas de jointures natives au sens SQL : abuser de `$lookup` trahit souvent un modèle mal pensé.
- Cohérence par défaut au niveau document ; les transactions multi-documents existent mais coûtent.
- Schéma libre n'est pas absence de schéma : sans validation JSON Schema, la dérive de modèle s'installe.
- Index oubliés = collection scans ; surveiller la taille du working set tenant en RAM.

## Alternatives

- [[Dev/Services/Redis|Redis]] — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub.
- [[Dev/Services/Apache Cassandra|Apache Cassandra]] — Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases NoSQL]] — comparatif des moteurs NoSQL
- Doc : https://www.mongodb.com/docs/
