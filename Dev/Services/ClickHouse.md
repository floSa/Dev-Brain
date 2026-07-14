---
galaxie: dev
type: service
nom: ClickHouse
alias: [clickhouse]
pitch: "SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence."
categorie: database/columnar
licence_type: open-source
hosted: both
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[Dev/Services/DuckDB|DuckDB]]"]
remplace_par: []
status: actif
tags: [columnar, olap, distributed]
url_docs: https://clickhouse.com/docs
url_repo: https://github.com/ClickHouse/ClickHouse
---

# ClickHouse

## Pourquoi

SGBD **orienté colonnes** conçu pour l'OLAP. Les données sont stockées et traitées par colonne, fortement compressées, avec une exécution **vectorisée** : il balaie des centaines de millions de lignes par seconde. Architecture **distribuée** (sharding + réplication) pour scaler horizontalement. Origine open-source (2016), licence Apache 2.0.

## Quand l'utiliser

- Analytique temps réel sur gros volumes : dashboards, observabilité, événements.
- Agrégations massives balayant beaucoup de lignes sur peu de colonnes.
- Ingestion à fort débit de logs, métriques, télémétrie.
- Besoin de scale-out horizontal sur un cluster.

## Quand NE PAS l'utiliser

- OLTP transactionnel, beaucoup de petites écritures et mises à jour ponctuelles → [[Dev/Services/Postgres|Postgres]].
- Analytique locale / embarquée sur un seul poste, sans cluster → [[Dev/Services/DuckDB|DuckDB]].
- Mises à jour et suppressions fréquentes ligne à ligne (modèle pensé pour l'append).

## Déploiement & coût

- Self-host (binaire, cluster) ou managé (ClickHouse Cloud).
- Scaling distribué : sharding pour le volume, réplication pour la disponibilité.
- Apache 2.0, gratuit ; le coût réel est l'exploitation du cluster.

## Pièges

- Updates et deletes coûteux (mutations asynchrones) — pas pour l'écriture en place.
- Cohérence éventuelle sur la réplication.
- Le choix du moteur de table (famille MergeTree) et des clés de tri détermine les perfs.
- Retours d'expérience détaillés : `Dev/REX/REX - ClickHouse.md`.

## Alternatives

- [[Dev/Services/DuckDB|DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases colonnes]] — comparatif des moteurs colonne / OLAP
- Doc : https://clickhouse.com/docs
