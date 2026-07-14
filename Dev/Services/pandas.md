---
galaxie: dev
type: service
nom: pandas
alias: [pd]
pitch: "DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python."
categorie: tooling/data
licence_type: open-source
hosted: self
maturite: production
langage: Python / Cython
scaling: single-node
alternatives: ["[[Dev/Services/Polars|Polars]]", "[[Dev/Services/Modin|Modin]]", "[[Dev/Services/Dask|Dask]]"]
remplace_par: []
status: actif
tags: [dataframe, in-memory]
url_docs: https://pandas.pydata.org/docs/
url_repo: https://github.com/pandas-dev/pandas
---

# pandas

## Pourquoi

Bibliothèque de **manipulation de données tabulaires** en Python, bâtie sur [[Dev/Services/numpy|numpy]]. Deux structures : `Series` (colonne indexée) et `DataFrame` (table de colonnes hétérogènes). Sa force est un **index** de premier ordre (alignement automatique, time series) et une grammaire complète — filtres booléens, `groupby`/`agg`, `merge`/`join`, `pivot`, fenêtres glissantes, I/O multi-format (CSV, Parquet, SQL, Excel). C'est le **pivot de l'écosystème data Python** : presque toute lib (scikit-learn, statsmodels, viz) parle DataFrame.

## Quand l'utiliser

- Exploration et nettoyage de données qui **tiennent en mémoire** sur une machine.
- Besoin de l'index riche : séries temporelles (`resample`, `asfreq`), alignement, MultiIndex.
- Interop maximale : c'est le format d'échange par défaut entre libs Python.
- Depuis pandas 2.0, backend mémoire **PyArrow** optionnel (types Arrow, chaînes plus compactes, lecture Parquet accélérée).

## Quand NE PAS l'utiliser

- Volumes lourds ou besoin de vitesse / parallélisme → [[Dev/Services/Polars|Polars]] (Rust, lazy, multi-thread).
- Garder l'API pandas mais saturer tous les cœurs sans réécrire → [[Dev/Services/Modin|Modin]].
- Données plus grosses que la RAM ou calcul sur cluster → [[Dev/Services/Dask|Dask]] (`dask.dataframe`).
- Calcul purement numérique sur tableaux N-dim sans étiquettes → [[Dev/Services/numpy|numpy]] directement.

## Déploiement & coût

- Bibliothèque Python (`uv add pandas`) ; rien à héberger. BSD-3-Clause, gratuit.
- **Single-node, tout en mémoire**, mono-thread sur la plupart des opérations (le GIL borne le parallélisme).
- Empreinte mémoire élevée : compter ~5–10× la taille du fichier source pour les manipulations intermédiaires.

## Pièges

- Le `SettingWithCopyWarning` : vue vs copie. Préférer `.loc[...]` pour les assignations.
- `apply` ligne à ligne est lent — vectoriser, ou passer à un outil dédié au volume.
- `object` dtype (souvent des chaînes) coûte cher en mémoire ; envisager le backend PyArrow.
- Mono-thread + tout en RAM : sur de gros volumes, échantillonner ou changer d'outil.

## Alternatives

- [[Dev/Services/Polars|Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.
- [[Dev/Services/Modin|Modin]] — Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.
- [[Dev/Services/Dask|Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.

## Liens

- Socle numérique : [[Dev/Services/numpy|numpy]] — pandas stocke ses colonnes dans des `ndarray`.
- [[Dev/Patterns/Comparatif - Manipulation de données]] — pandas vs Polars / numpy / Modin.
- Doc : https://pandas.pydata.org/docs/
