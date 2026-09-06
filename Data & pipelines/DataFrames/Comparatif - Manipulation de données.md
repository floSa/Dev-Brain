---
role: comparatif
nom: Comparatif - Manipulation de données
categorie: data/tableau
tags: [dataframe, array, columnar, out-of-core]
---

# Comparatif - Manipulation de données

> On tranche sur : la forme de la donnée — table étiquetée, tableau N-dim nu, cube à axes nommés — puis ce qui borne, la RAM d'une machine ou la dette d'API déjà écrite.

![[Comparatif - Manipulation de données.base]]

## Ce qui départage

- [[pandas]] — l'**index** de premier ordre (alignement automatique, `resample`, MultiIndex) et l'interop maximale : c'est le format d'échange par défaut entre libs Python, scikit-learn et statsmodels compris. Mono-thread et tout en RAM ; `apply` ligne à ligne est lent, le dtype `object` coûte cher, et le `SettingWithCopyWarning` vient de la frontière vue/copie.
- [[Polars]] — Rust sur Arrow, avec un mode **lazy** qui passe la requête à un **optimiseur** (predicate et projection pushdown) avant de l'exécuter en multi-thread, et un moteur **streaming** qui traite plus gros que la RAM sur un seul nœud. Pas d'**index** ni de mutation en place, idiomes d'expressions à réapprendre, et rien ne se calcule avant `.collect()`.
- [[Modin]] — le seul **remplaçant transparent** : une ligne d'import, et le code pandas existant sature tous les cœurs, sur un moteur Ray, Dask ou MPI interchangeable. Couverture d'API **non totale** — le non-implémenté retombe **silencieusement** sur pandas, donc sans gain — et sur petits volumes la surcharge de parallélisation coûte plus qu'elle ne rend.
- [[numpy]] — le `ndarray` **homogène** stocké de façon contiguë, vectorisé en C : ce n'est pas un outil tabulaire, c'est la brique sur laquelle pandas et le reste reposent. Un seul `dtype` par tableau, le slicing renvoie souvent une **vue** que l'on modifie par erreur, et les entiers à largeur fixe débordent en silence.
- [[xarray]] — les **étiquettes** portées sur le N-dimensionnel : dimensions nommées, coordonnées et attributs, donc `da.sel(time="2024-01", lat=48.5)` au lieu d'une position ; NetCDF et Zarr natifs, et `chunks=...` délègue l'out-of-core à [[Dask]]. L'alignement automatique par coordonnées fabrique des `NaN` **en silence** quand les axes ne coïncident pas.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
