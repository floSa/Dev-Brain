---
galaxie: dev
type: service
nom: InfluxDB
alias: [influxdb, influx]
pitch: "SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles."
categorie: database/timeseries
licence_type: open-source
hosted: both
maturite: production
langage: Rust
scaling: single-node
alternatives: ["[[Dev/Services/TimescaleDB|TimescaleDB]]"]
remplace_par: []
status: actif
tags: [timeseries]
url_docs: https://docs.influxdata.com/
url_repo: https://github.com/influxdata/influxdb
---

# InfluxDB

## Pourquoi

SGBD spécialisé **séries temporelles** : données horodatées (métriques, événements, capteurs) écrites en flux continu. Modèle pensé pour l'append séquentiel, la rétention automatique et les requêtes par fenêtres temporelles (downsampling, agrégations glissantes). Le cœur InfluxDB 3 est réécrit en **Rust** sur la pile Apache Arrow / DataFusion / Parquet ; OSS sous licence MIT/Apache 2 (GA avril 2025).

## Quand l'utiliser

- Métriques d'infrastructure et d'application, monitoring, observabilité.
- Télémétrie IoT / capteurs : fort débit d'écriture horodatée.
- Données qui vieillissent : rétention et downsampling automatiques.
- Requêtes temporelles (fenêtres, agrégations par intervalle) plus que jointures relationnelles.

## Quand NE PAS l'utiliser

- Données relationnelles, jointures et transactions ACID → [[Dev/Services/Postgres|Postgres]].
- Besoin de SQL standard et de l'écosystème Postgres tout en faisant du temporel → [[Dev/Services/TimescaleDB|TimescaleDB]].
- Analytique colonne haute cardinalité non strictement temporelle → [[Dev/Services/ClickHouse|ClickHouse]].

## Déploiement & coût

- Self-host : InfluxDB 3 Core (OSS, mono-nœud) ; InfluxDB 3 Enterprise ajoute le clustering.
- Managé : InfluxDB Cloud.
- OSS gratuit (MIT/Apache 2) ; haute disponibilité et clustering relèvent des éditions Enterprise/Cloud.

## Pièges

- La **cardinalité des séries** (nombre de combinaisons de tags) est le facteur de coût mémoire historique — à maîtriser dès la modélisation.
- Langage de requête mouvant selon les versions (InfluxQL, puis Flux, puis SQL en v3) — vérifier la version cible.
- Pensé append : mises à jour et suppressions ponctuelles peu naturelles.
- Retours d'expérience détaillés : `Dev/REX/REX - InfluxDB.md`.

## Alternatives

- [[Dev/Services/TimescaleDB|TimescaleDB]] — Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases temporelles]] — comparatif des moteurs temporels
- Doc : https://docs.influxdata.com/
