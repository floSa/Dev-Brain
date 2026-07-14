---
galaxie: dev
type: service
nom: xarray
alias: [xray, pydata-xarray]
pitch: "Tableaux N-dimensionnels étiquetés : ajoute dimensions, coordonnées et attributs au-dessus de numpy — le pandas des données multidimensionnelles (NetCDF, climat, géospatial)."
categorie: tooling/data
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/numpy|numpy]]"]
remplace_par: []
status: actif
tags: [array, out-of-core]
url_docs: https://docs.xarray.dev/
url_repo: https://github.com/pydata/xarray
---

# xarray

## Pourquoi

Apporte les **étiquettes** aux tableaux N-dimensionnels. Là où un `ndarray` [[Dev/Services/numpy|numpy]] s'indexe par position (`a[3, :, 0]`), xarray nomme les **dimensions**, attache des **coordonnées** et des **attributs** : on écrit `da.sel(time="2024-01", lat=48.5)`. Deux structures : `DataArray` (un tableau étiqueté) et `Dataset` (plusieurs variables partageant des axes). C'est, pour les données **multidimensionnelles**, ce que [[Dev/Services/pandas|pandas]] est aux tables 2D — d'ailleurs largement inspiré de lui. Lecture/écriture native NetCDF et Zarr ; standard de fait en sciences du climat, océan, géospatial et imagerie. Apache 2.0, projet NumFOCUS.

## Quand l'utiliser

- Données **N-D avec axes nommés** : grilles spatio-temporelles, raster multi-bandes, sorties de simulation.
- Sélection et alignement par étiquette plutôt que par position (`.sel`, `.resample`, `groupby` sur coordonnées).
- Lire/écrire NetCDF, Zarr, GRIB ; manipuler des cubes climat/géo sans réinventer l'indexation.
- Passer à l'**out-of-core** : `chunks=...` délègue le calcul à [[Dev/Services/Dask|Dask]] sur des données plus grosses que la RAM.

## Quand NE PAS l'utiliser

- Calcul numérique pur sans besoin d'étiquettes → [[Dev/Services/numpy|numpy]] directement (moins de surcouche).
- Données **tabulaires 2D** hétérogènes → [[Dev/Services/pandas|pandas]] ou [[Dev/Services/Polars|Polars]].
- Pipeline orienté performance pure sur colonnes → [[Dev/Services/Polars|Polars]] ; xarray privilégie l'expressivité scientifique.
- Petits tableaux où la machinerie de coordonnées ajoute plus de friction que de valeur.

## Déploiement & coût

- Bibliothèque (`uv add xarray`) ; backends optionnels (`netCDF4`, `zarr`, `dask`). Apache 2.0, gratuit.
- **Single-node** en mémoire par défaut ; **out-of-core / parallèle** dès qu'on active les chunks Dask.
- Empreinte mémoire et performance héritées de numpy (cœur) et du backend d'I/O choisi.

## Pièges

- Surcouche d'étiquettes : un peu d'overhead et une courbe d'apprentissage (dims vs coords vs index).
- L'alignement automatique par coordonnées peut produire silencieusement des `NaN` si les axes ne coïncident pas.
- Les performances dépendent du backend (NetCDF vs Zarr) et du découpage en chunks pour Dask.
- Tout n'est pas vectorisable proprement : certaines opérations retombent sur des boucles coûteuses.

## Alternatives

- [[Dev/Services/numpy|numpy]] — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.

## Liens

- Socle numérique : [[Dev/Services/numpy|numpy]] — xarray étiquette ses `ndarray`.
- À l'échelle / hors RAM : [[Dev/Services/Dask|Dask]] — backend de calcul paresseux via les chunks.
- Parent tabulaire : [[Dev/Services/pandas|pandas]] — même philosophie d'étiquetage, en 2D.
- [[Dev/Patterns/Comparatif - Manipulation de données]] — xarray vs numpy / pandas.
- Doc : https://docs.xarray.dev/
