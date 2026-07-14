---
galaxie: dev
type: service
nom: TimescaleDB
alias: [timescaledb, timescale]
pitch: "Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres."
categorie: database/timeseries
licence_type: open-source
hosted: both
maturite: production
langage: C
scaling: single-node
alternatives: ["[[Dev/Services/InfluxDB|InfluxDB]]"]
remplace_par: []
status: actif
tags: [timeseries, postgres]
url_docs: https://www.tigerdata.com/docs
url_repo: https://github.com/timescale/timescaledb
---

# TimescaleDB

## Pourquoi

Extension Postgres — comme [[Dev/Services/pgvector|pgvector]] — qui ajoute le **temporel** à une base relationnelle. Une table devient une **hypertable** partitionnée par le temps de façon transparente : ingestion soutenue, compression colonne, rétention et agrégats continus, tout en gardant SQL, jointures et transactions ACID. Cœur open-source Apache 2.0 ; fonctions avancées sous licence Timescale (TSL), libres en self-host. Éditée par Tiger Data (ex-Timescale).

## Quand l'utiliser

- Postgres déjà présent : ajouter du temporel sans monter une nouvelle base.
- Séries temporelles à requêter en **SQL standard**, avec jointures sur des tables relationnelles.
- Métriques / IoT / finance où la cohérence transactionnelle compte.
- Besoin d'agrégats continus et de compression sur l'historique.

## Quand NE PAS l'utiliser

- Aucun Postgres et pas d'envie d'en gérer un → [[Dev/Services/InfluxDB|InfluxDB]] (serveur temporel autonome).
- Analytique colonne massive non temporelle → [[Dev/Services/ClickHouse|ClickHouse]].
- Très haut débit d'écriture pure flux sans besoin relationnel → évaluer [[Dev/Services/InfluxDB|InfluxDB]].

## Déploiement & coût

- Self-host : extension à activer sur une instance Postgres (`CREATE EXTENSION timescaledb`).
- Managé : Tiger Cloud (ex-Timescale Cloud).
- Scaling lié à Postgres (vertical + réplicas lecture) ; le multi-nœuds distribué a été abandonné. Apache 2.0 gratuit ; la TSL n'interdit que la revente en DBaaS.

## Pièges

- **Deux licences** : noyau Apache 2.0 vs fonctions Community sous TSL — vérifier ce qui est couvert.
- Le multi-nœuds distribué est déprécié : penser scaling vertical + réplicas, pas sharding natif.
- Bien dimensionner l'intervalle de chunk (partition temporelle) : trop fin ou trop large dégrade les perfs.
- Retours d'expérience détaillés : `Dev/REX/REX - TimescaleDB.md`.

## Alternatives

- [[Dev/Services/InfluxDB|InfluxDB]] — SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases temporelles]] — comparatif des moteurs temporels
- Doc : https://www.tigerdata.com/docs
