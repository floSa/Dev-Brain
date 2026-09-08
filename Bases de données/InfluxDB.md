---
role: brique
nom: InfluxDB
alias: [influxdb, influx]
pitch: "SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles."
categorie: database/series-temporelles
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Rust
scaling: single-node
alternatives: ["[[TimescaleDB]]"]
complements: []
tags: [timeseries]
url_docs: https://docs.influxdata.com/
url_repo: https://github.com/influxdata/influxdb
---

# InfluxDB

<!-- AUTO:BANDEAU:START -->
> SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Rust | open-source | self-hébergé ou managé · mono-nœud | production | à jour · 2026-09-04 |
<!-- AUTO:BANDEAU:END -->

## Définition

SGBD spécialisé **séries temporelles** : des données horodatées — métriques, événements,
capteurs — écrites en flux continu. Le modèle est pensé pour l'append séquentiel, avec
rétention et downsampling automatiques, et des requêtes par fenêtres temporelles plutôt que
par jointures relationnelles. Le cœur d'InfluxDB 3, disponible depuis avril 2025, est réécrit
sur la pile Apache Arrow, DataFusion et Parquet.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Métriques d'infrastructure et d'application, monitoring, observabilité | La **cardinalité des séries** — le nombre de combinaisons de tags — est le facteur de coût mémoire : elle se borne dès la modélisation |
| Télémétrie IoT et capteurs : fort débit d'écriture horodatée | Le langage de requête a changé trois fois — InfluxQL, puis Flux, puis SQL en v3 : la version cible se vérifie avant d'écrire quoi que ce soit |
| Données qui vieillissent : rétention et downsampling automatiques | Mises à jour et suppressions ponctuelles : le moteur est pensé append, elles y sont peu naturelles |
| Requêtes temporelles — fenêtres, agrégations par intervalle — plus que jointures | Haute disponibilité et clustering : l'édition self-host Core est mono-nœud |
| | Données relationnelles, jointures et transactions ACID → [[Postgres]] |
| | Analytique colonne à haute cardinalité, non strictement temporelle → [[ClickHouse]] |

## Mise en œuvre

- Installation — InfluxDB 3 Core en self-host, Enterprise pour le clustering, ou InfluxDB Cloud pour le managé
- Point d'entrée — SQL en v3 ; InfluxQL puis Flux sur les versions antérieures
- Prérequis — une modélisation des tags qui borne la cardinalité des séries
- Exécution — self-hébergé mono-nœud côté OSS, ou managé ; le clustering relève d'Enterprise
- Coût — OSS gratuit sous MIT/Apache 2 ; haute disponibilité et clustering en éditions Enterprise ou Cloud

## Écosystème

### Alternatives

- [[TimescaleDB]] — Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres.

## Ressources

- Documentation — https://docs.influxdata.com/
- Dépôt — https://github.com/influxdata/influxdb

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases temporelles]] — ce qui départage les moteurs du dossier
