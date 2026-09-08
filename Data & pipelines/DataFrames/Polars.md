---
role: brique
nom: Polars
alias: [polars, py-polars]
pitch: "DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core."
categorie: data/tableau
famille: paquet
licence_type: open-source
maturite: production
langage: Rust
alternatives: ["[[pandas]]", "[[Modin]]", "[[Dask]]"]
complements: ["[[ADBC]]", "[[DuckDB]]", "[[connectorx]]"]
tags: [dataframe, columnar, lazy-evaluation, out-of-core]
url_docs: https://docs.pola.rs/
url_repo: https://github.com/pola-rs/polars
---

# Polars

<!-- AUTO:BANDEAU:START -->
> DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Rust | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-02 |
<!-- AUTO:BANDEAU:END -->

## Définition

DataFrames écrits en Rust sur le format colonnaire **Apache Arrow**. Deux modes : *eager*,
proche de pandas, et surtout **lazy** — la requête est construite, passée à un
**optimiseur** (predicate pushdown, projection pushdown, élimination de colonnes) puis
exécutée en **multi-thread**. Un moteur **streaming** traite par morceaux des jeux plus gros
que la RAM, sur un seul nœud. Rien ne se calcule avant `.collect()` : l'oublier ne renvoie
pas un résultat mais un plan. Deux absences volontaires structurent l'écriture : il n'y a ni
**index** ni mutation en place, on pense en transformations et non en assignations, avec une
API d'expressions (`pl.col(...)`) qui ne se devine pas depuis pandas.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| La vitesse et l'empreinte mémoire comptent : millions à milliards de lignes sur une machine | Calcul **distribué** sur plusieurs nœuds : Polars reste mono-nœud → [[Dask]] |
| Chaîner les transformations en **lazy** et laisser l'optimiseur planifier avant `.collect()` | Ni index ni mutation en place : il faut réapprendre les idiomes, la bascule depuis pandas n'est pas mécanique |
| Données plus grosses que la RAM sur un seul nœud, via le moteur streaming | Le mode lazy ne calcule rien tant que `.collect()` n'est pas appelé — l'oubli est silencieux |
| Projet neuf sans dette pandas, ou portion chaude d'un pipeline existant | API encore en évolution rapide : épingler la version sur un projet long |

## Mise en œuvre

- Installation — `uv add polars`
- Point d'entrée — import Python, `import polars as pl` ; cœur Rust derrière des bindings
- Prérequis — Python ; interop zéro-copie avec Arrow et PyArrow
- Exécution — dans le process appelant, mono-nœud multi-thread, tous les cœurs sans configuration ; streaming out-of-core pour dépasser la RAM
- Coût — gratuit, licence MIT, aucune limite d'usage

## Écosystème

### Alternatives

- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.
- [[Modin]] — Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.
- [[Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.

### Compléments

- [[ADBC]] — Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement des données Arrow. — `read_database(engine="adbc")` s'appuie dessus pour éviter une conversion.
- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — intégration directe via Arrow, dans les deux sens.
- [[connectorx]] — Charge des données d'une base SQL vers un DataFrame (pandas, Polars, Arrow) à vitesse maximale — moteur Rust zero-copy, copie unique source→destination. — le moteur derrière `read_database(engine="connectorx")`

## Ressources

- Documentation — https://docs.pola.rs/
- Dépôt — https://github.com/pola-rs/polars

## Voir aussi

- [[DataFrames]] — le hub du dossier
- [[Comparatif - Manipulation de données]] — ce qui départage les outils du dossier
