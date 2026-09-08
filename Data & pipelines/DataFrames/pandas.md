---
role: brique
nom: pandas
alias: [pd]
pitch: "DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python."
categorie: data/tableau
famille: paquet
licence_type: open-source
maturite: production
langage: Python / Cython
alternatives: ["[[Polars]]", "[[Modin]]", "[[Dask]]"]
complements: ["[[DuckDB]]"]
tags: [dataframe, in-memory]
url_docs: https://pandas.pydata.org/docs/
url_repo: https://github.com/pandas-dev/pandas
---

# pandas

<!-- AUTO:BANDEAU:START -->
> DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python / Cython | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-07-22 |
<!-- AUTO:BANDEAU:END -->

## Définition

Manipulation de données **tabulaires** en Python, bâtie sur [[numpy]]. Deux structures : la
`Series`, colonne indexée, et le `DataFrame`, table de colonnes hétérogènes. Sa
particularité est un **index** de premier ordre — alignement automatique entre objets,
`resample` et `asfreq` sur les séries temporelles, MultiIndex — au-dessus d'une grammaire
complète : filtres booléens, `groupby`/`agg`, `merge`, `pivot`, fenêtres glissantes, I/O
CSV, Parquet, SQL et Excel. Tout est en mémoire et mono-thread sur la plupart des
opérations : le GIL borne le parallélisme, et il faut compter cinq à dix fois la taille du
fichier source pour les intermédiaires. Depuis la 2.0, un backend mémoire **PyArrow**
optionnel réduit le coût des chaînes et accélère la lecture Parquet.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Exploration et nettoyage de données qui **tiennent en mémoire** sur une machine | Données plus grosses que la RAM, ou calcul à répartir sur un cluster → [[Dask]] |
| L'index riche est utile : séries temporelles, alignement automatique, MultiIndex | Mono-thread et tout en RAM : sur de gros volumes il faut échantillonner ou changer d'outil |
| Interop maximale : c'est le format d'échange par défaut entre bibliothèques Python | `apply` ligne à ligne est lent — il faut vectoriser, la parallélisation seule n'y change rien |
| Backend PyArrow visé : types Arrow, chaînes compactes, lecture Parquet accélérée | Le dtype `object`, celui des chaînes par défaut, coûte cher en mémoire |
| | La frontière vue / copie est piégeuse : le `SettingWithCopyWarning` vient de là, et `.loc[...]` est la parade |

## Mise en œuvre

- Installation — `uv add pandas`, `uv add "pandas[pyarrow]"` pour le backend Arrow
- Point d'entrée — import Python, `import pandas as pd`
- Prérequis — Python ; numpy est tiré comme dépendance
- Exécution — dans le process appelant, mono-nœud et tout en mémoire, mono-thread sur la plupart des opérations
- Coût — gratuit, licence BSD-3-Clause, aucune limite d'usage

## Écosystème

### Alternatives

- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.
- [[Modin]] — Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.
- [[Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.

### Compléments

- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — intégration directe dans les deux sens : DuckDB lit un DataFrame en place et rend son résultat en DataFrame.

## Ressources

- Documentation — https://pandas.pydata.org/docs/
- Dépôt — https://github.com/pandas-dev/pandas

## Voir aussi

- [[DataFrames]] — le hub du dossier
- [[numpy]] — le socle numérique : pandas stocke ses colonnes dans des `ndarray`
- [[Comparatif - Manipulation de données]] — ce qui départage les outils du dossier
