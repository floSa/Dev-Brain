---
role: brique
nom: TimescaleDB
alias: [timescaledb, timescale]
pitch: "Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres."
categorie: database/series-temporelles
famille: extension
licence_type: open-source
maturite: production
langage: C
alternatives: ["[[InfluxDB]]"]
complements: ["[[Postgres]]"]
tags: [timeseries, postgres]
url_docs: https://www.tigerdata.com/docs
url_repo: https://github.com/timescale/timescaledb
---

# TimescaleDB

<!-- AUTO:BANDEAU:START -->
> Extension Postgres qui transforme une table en hypertable temporelle — du temporel en restant en SQL/Postgres.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Extension C | open-source | dans le moteur hôte, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Extension Postgres qui ajoute le **temporel** à une base relationnelle. Une table devient une
**hypertable**, partitionnée par le temps de façon transparente : ingestion soutenue,
compression en colonnes, rétention et agrégats continus, tout en gardant SQL, jointures et
transactions ACID. Le dimensionnement de l'intervalle de chunk — la partition temporelle —
est le réglage structurant : trop fin ou trop large, les performances se dégradent. Éditée
par Tiger Data, ex-Timescale.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Postgres déjà présent : ajouter du temporel sans monter une nouvelle base | Aucun Postgres dans le projet : en installer un pour cela seul est rarement gagnant |
| Séries temporelles à requêter en **SQL standard**, avec jointures sur des tables relationnelles | Le multi-nœuds distribué est abandonné : la montée en charge est verticale plus des réplicas de lecture, pas du sharding natif |
| Métriques, IoT, finance, où la cohérence transactionnelle compte | Deux licences dans le même produit — noyau Apache 2.0, fonctions Community sous TSL : ce qui est couvert se vérifie fonction par fonction |
| Agrégats continus et compression sur l'historique | Analytique colonne massive, non temporelle → [[ClickHouse]] |

## Mise en œuvre

- Installation — `CREATE EXTENSION timescaledb` sur une instance Postgres existante ; managé sur Tiger Cloud, ex-Timescale Cloud
- Point d'entrée — SQL : une table déclarée en hypertable, puis requêtée comme n'importe quelle table Postgres
- Prérequis — un Postgres en place, et un intervalle de chunk dimensionné avant l'ingestion
- Exécution — dans le moteur Postgres hôte ; scaling vertical et réplicas de lecture, le multi-nœuds distribué ayant été abandonné
- Coût — gratuit ; noyau sous Apache 2.0, fonctions Community sous licence TSL, libres en self-host — la TSL n'interdit que la revente en DBaaS

## Écosystème

### Alternatives

- [[InfluxDB]] — SGBD de séries temporelles pensé métriques et IoT : ingestion haut débit, rétention et requêtes par fenêtres temporelles.

### Compléments

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — le moteur hôte, sans lequel l'extension n'existe pas.

## Ressources

- Documentation — https://www.tigerdata.com/docs
- Dépôt — https://github.com/timescale/timescaledb

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases temporelles]] — ce qui départage les moteurs du dossier
- [[pgvector]] — l'autre extension Postgres du brain, côté vectoriel
