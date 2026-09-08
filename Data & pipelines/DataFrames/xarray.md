---
role: brique
nom: xarray
alias: [xray, pydata-xarray]
pitch: "Tableaux N-dimensionnels étiquetés : ajoute dimensions, coordonnées et attributs au-dessus de numpy — le pandas des données multidimensionnelles (NetCDF, climat, géospatial)."
categorie: data/tableau
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[numpy]]"]
complements: ["[[Dask]]"]
tags: [array, out-of-core]
url_docs: https://docs.xarray.dev/
url_repo: https://github.com/pydata/xarray
---

# xarray

<!-- AUTO:BANDEAU:START -->
> Tableaux N-dimensionnels étiquetés : ajoute dimensions, coordonnées et attributs au-dessus de numpy — le pandas des données multidimensionnelles (NetCDF, climat, géospatial).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-07-09 |
<!-- AUTO:BANDEAU:END -->

## Définition

Apporte les **étiquettes** aux tableaux N-dimensionnels. Là où un `ndarray` [[numpy]]
s'indexe par position, xarray nomme les **dimensions**, attache des **coordonnées** et des
**attributs** : on écrit `da.sel(time="2024-01", lat=48.5)`. Deux structures : le
`DataArray`, un tableau étiqueté, et le `Dataset`, plusieurs variables partageant des axes.
Lecture et écriture natives NetCDF et Zarr en font le standard de fait en climat, océan,
géospatial et imagerie. Le prix de la surcouche est double : un peu d'overhead et une
courbe d'apprentissage (dimensions, coordonnées et index ne sont pas la même chose), et
surtout un **alignement automatique par coordonnées** qui fabrique des `NaN` en silence dès
que deux axes ne coïncident pas exactement.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Données N-D à axes nommés : grilles spatio-temporelles, raster multi-bandes, sorties de simulation | L'alignement automatique par coordonnées produit des `NaN` **sans rien signaler** quand les axes divergent |
| Sélection et alignement par étiquette plutôt que par position (`.sel`, `.resample`, `groupby` sur coordonnées) | Petits tableaux : la machinerie de coordonnées ajoute plus de friction qu'elle n'apporte |
| Lire et écrire NetCDF, Zarr ou GRIB sans réinventer l'indexation de cubes | Les performances dépendent du backend d'I/O choisi et du découpage en chunks — ce n'est pas un réglage neutre |
| Passer à l'out-of-core en activant les chunks, sans changer de bibliothèque | Toutes les opérations ne se vectorisent pas proprement : certaines retombent sur des boucles coûteuses |

## Mise en œuvre

- Installation — `uv add xarray` ; extras `netCDF4`, `zarr`, `dask` selon les besoins
- Point d'entrée — import Python, `import xarray as xr` ; `open_dataset` pour lire un fichier
- Prérequis — Python ; numpy comme socle, un backend d'I/O pour chaque format visé
- Exécution — dans le process appelant, mono-nœud et en mémoire par défaut ; out-of-core et parallèle dès que les chunks sont activés
- Coût — gratuit, licence Apache 2.0, projet NumFOCUS

## Écosystème

### Alternatives

- [[numpy]] — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.

### Compléments

- [[Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster. — `chunks=...` lui délègue le calcul, c'est la voie documentée pour dépasser la RAM.

## Ressources

- Documentation — https://docs.xarray.dev/
- Dépôt — https://github.com/pydata/xarray

## Voir aussi

- [[DataFrames]] — le hub du dossier
- [[pandas]] — le parent tabulaire : même philosophie d'étiquetage, en deux dimensions
- [[Comparatif - Manipulation de données]] — ce qui départage les outils du dossier
