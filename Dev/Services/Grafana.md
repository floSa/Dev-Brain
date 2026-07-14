---
galaxie: dev
type: service
nom: Grafana
alias: [grafana]
pitch: "Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud."
categorie: observability/metric
licence_type: open-source
hosted: both
maturite: production
langage: Go
scaling: distributed
alternatives: []
remplace_par: []
status: actif
tags: [observability, metrics, dashboard, dataviz]
url_docs: https://grafana.com/docs/grafana/latest/
url_repo: https://github.com/grafana/grafana
---

# Grafana

## Pourquoi

Plateforme de **dashboards et d'observabilité** open-source éditée par Grafana Labs, sous **AGPL-3.0-only** (relicenciée depuis Apache 2.0 en 2021). Backend en **Go**, front en React/TypeScript. Sa force est d'être **composable** : elle ne stocke pas les données mais se connecte à 150+ **sources** (Prometheus, [[Dev/Services/Loki|Loki]], [[Dev/Services/InfluxDB|InfluxDB]], [[Dev/Services/Elasticsearch|Elasticsearch]], [[Dev/Services/Postgres|Postgres]]…) pour visualiser **métriques, logs et traces** au même endroit, avec exploration ad hoc et **alerting** intégré.

## Quand l'utiliser

- **Dashboards unifiés** au-dessus de plusieurs sources hétérogènes (métriques + logs + traces).
- Visualiser des métriques **Prometheus** ou des logs **Loki** (LogQL) avec alerting.
- Centraliser la supervision d'une infra / d'une stack data sur un outil ouvert et auto-hébergeable.

## Quand NE PAS l'utiliser

- Pour **stocker** les métriques : Grafana ne stocke rien — il faut une base derrière (Prometheus/Mimir, [[Dev/Services/InfluxDB|InfluxDB]]).
- Pour une simple **app data interactive** en Python (formulaires, ML demo) → [[Dev/Services/Streamlit|Streamlit]], [[Dev/Services/Dash|Dash]] : autre usage que la supervision.

## Déploiement & coût

- **Self-host** : binaire Go unique ou Docker ; haute disponibilité possible avec base partagée (plusieurs instances derrière un load-balancer), d'où `distributed`.
- **Grafana Cloud** managé (bundle Mimir/Loki/Tempo/Pyroscope).
- **AGPLv3** gratuit ; édition **Enterprise** (binaire propriétaire) débloque reporting, RBAC fin et plugins commerciaux sous clé.

## Pièges

- Grafana **ne stocke pas les données** : prévoir et opérer la source (TSDB, Loki…).
- **AGPLv3** : copyleft réseau — vérifier les implications si Grafana est intégré et exposé dans un produit.
- **OSS vs Enterprise** : certaines fonctions (reporting, RBAC avancé) sont réservées à l'édition payante.

## Alternatives

- _Pas encore d'alternative équivalente fichée dans le brain (catégorie naissante)._ Grafana se couple à [[Dev/Services/Loki|Loki]] (logs) et aux sources de métriques, plutôt qu'il ne les remplace.

## Liens

- [[Dev/Services/Loki|Loki]] — agrégation de logs du même éditeur, source naturelle visualisée dans Grafana.
- Sources fréquentes : Prometheus, [[Dev/Services/InfluxDB|InfluxDB]], [[Dev/Services/Elasticsearch|Elasticsearch]], [[Dev/Services/Postgres|Postgres]].
- Doc : https://grafana.com/docs/grafana/latest/
