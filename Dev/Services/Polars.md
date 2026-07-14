---
galaxie: dev
type: service
nom: Polars
alias: [polars, py-polars]
pitch: "DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core."
categorie: tooling/data
licence_type: open-source
hosted: self
maturite: production
langage: Rust
scaling: single-node
alternatives: ["[[Dev/Services/pandas|pandas]]", "[[Dev/Services/Modin|Modin]]", "[[Dev/Services/Dask|Dask]]"]
remplace_par: []
status: actif
tags: [dataframe, columnar, lazy-evaluation, out-of-core]
url_docs: https://docs.pola.rs/
url_repo: https://github.com/pola-rs/polars
---

# Polars

## Pourquoi

DataFrames **écrits en Rust** sur le format colonnaire **Apache Arrow**. Deux modes : *eager* (comme pandas) et surtout **lazy** — la requête est construite puis passée à un **optimiseur** (predicate/projection pushdown, élimination de colonnes) avant d'être exécutée en **multi-thread**. Un **moteur streaming** traite des jeux plus grands que la RAM par morceaux. Le résultat : un ordre de grandeur plus rapide que pandas sur les charges group-by / jointures, avec une API expressive (`select`, `filter`, `group_by`, `with_columns`).

## Quand l'utiliser

- Pipelines tabulaires où la **vitesse** et l'usage mémoire comptent (millions à milliards de lignes sur une machine).
- API **lazy** : enchaîner les transformations et laisser l'optimiseur planifier (`scan_parquet(...).filter(...).group_by(...).collect()`).
- Données **plus grosses que la RAM** sur un seul nœud → moteur streaming, sans monter un cluster.
- Projet neuf sans dette pandas, ou portion chaude d'un pipeline existant.

## Quand NE PAS l'utiliser

- Code et écosystème déjà 100 % pandas → migration coûteuse ; [[Dev/Services/Modin|Modin]] garde l'API pandas telle quelle.
- Besoin de l'index riche / séries temporelles façon pandas → [[Dev/Services/pandas|pandas]] (Polars n'a pas d'index).
- Calcul **distribué sur cluster** multi-nœuds → [[Dev/Services/Dask|Dask]] (Polars reste single-node).
- Tableaux numériques N-dim purs → [[Dev/Services/numpy|numpy]].

## Déploiement & coût

- Bibliothèque (`uv add polars`) ; cœur Rust, bindings Python. MIT, gratuit.
- **Single-node, multi-thread** : exploite tous les cœurs sans configuration.
- Streaming out-of-core pour dépasser la RAM ; interop zéro-copie avec Arrow / PyArrow.

## Pièges

- Pas d'**index** ni de mutation en place : penser en transformations, pas en assignations style pandas.
- API d'expressions différente de pandas — la bascule demande de réapprendre les idiomes (`pl.col(...)`).
- Le mode lazy ne calcule rien avant `.collect()` : oublier le collect = aucun résultat.
- API encore en évolution rapide ; épingler la version sur les projets longs.

## Alternatives

- [[Dev/Services/pandas|pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.
- [[Dev/Services/Modin|Modin]] — Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.
- [[Dev/Services/Dask|Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.

## Liens

- Format mémoire : Apache Arrow (colonnaire) — interop avec PyArrow et le backend Arrow de [[Dev/Services/pandas|pandas]].
- [[Dev/Patterns/Comparatif - Manipulation de données]] — Polars vs pandas / numpy / Modin.
- Doc : https://docs.pola.rs/
