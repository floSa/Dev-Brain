---
galaxie: dev
type: service
nom: numpy
alias: [np, NumPy]
pitch: "Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique."
categorie: tooling/data
licence_type: open-source
hosted: self
maturite: production
langage: C / Python
scaling: single-node
alternatives: ["[[Dev/Services/xarray|xarray]]", "[[Dev/Services/Dask|Dask]]", "[[Dev/Services/CuPy|CuPy]]"]
remplace_par: []
status: actif
tags: [array, in-memory]
url_docs: https://numpy.org/doc/stable/
url_repo: https://github.com/numpy/numpy
---

# numpy

## Pourquoi

Paquet **fondamental du calcul scientifique** en Python. Son cœur est le `ndarray` : un **tableau N-dimensionnel homogène** stocké de façon contiguë en mémoire, sur lequel les opérations sont **vectorisées en C** (pas de boucle Python). Apporte le *broadcasting*, l'indexation avancée, l'algèbre linéaire (`linalg`), les transformées de Fourier, le tirage aléatoire et un système de `dtype`. C'est la **brique sur laquelle tout repose** : [[Dev/Services/pandas|pandas]], scikit-learn, SciPy, matplotlib et la plupart des libs scientifiques manipulent des `ndarray`.

## Quand l'utiliser

- Calcul **numérique pur** sur vecteurs / matrices / tenseurs : algèbre linéaire, statistiques, simulation.
- Vectoriser pour la performance : remplacer des boucles Python par des opérations sur tableaux entiers.
- Interface bas niveau entre libs : c'est le format d'échange numérique de l'écosystème.
- Tirage aléatoire reproductible (`np.random.default_rng`).

## Quand NE PAS l'utiliser

- Données **tabulaires hétérogènes** avec étiquettes de colonnes et index → [[Dev/Services/pandas|pandas]] ou [[Dev/Services/Polars|Polars]].
- Tableaux **plus grands que la RAM** ou calcul distribué → [[Dev/Services/Dask|Dask]] (`dask.array`, même API).
- Accélération **GPU** d'un code numpy existant → [[Dev/Services/CuPy|CuPy]] ; différentiation automatique → [[Dev/Services/JAX|JAX]] / [[Dev/Services/PyTorch|PyTorch]].

## Déploiement & coût

- Bibliothèque (`uv add numpy`) ; cœur C compilé. BSD-3-Clause, gratuit.
- **Single-node, en mémoire** ; certaines routines `linalg` s'appuient sur BLAS/LAPACK multi-thread.
- Empreinte mémoire prévisible : un `ndarray` = données brutes contiguës + métadonnées légères.

## Pièges

- Tableau **homogène** : un seul `dtype` par tableau (pour de l'hétérogène, c'est pandas).
- Le *broadcasting* est puissant mais peut aligner des formes par erreur — vérifier les `shape`.
- Vue vs copie : le slicing renvoie souvent une **vue** ; modifier la vue modifie la source.
- Dépassements silencieux sur les entiers à largeur fixe (`int32`…).

## Alternatives

- [[Dev/Services/xarray|xarray]] — Tableaux N-dimensionnels étiquetés : ajoute dimensions, coordonnées et attributs au-dessus de numpy — le pandas des données multidimensionnelles (NetCDF, climat, géospatial).
- [[Dev/Services/Dask|Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.
- [[Dev/Services/CuPy|CuPy]] — NumPy/SciPy sur GPU : tableau ndarray compatible drop-in exécuté sur CUDA/ROCm, pour accélérer le calcul numérique existant sans réécrire le code.

## Liens

- Briques bâties dessus : [[Dev/Services/pandas|pandas]] (colonnes en `ndarray`), scikit-learn, SciPy.
- À l'échelle / hors RAM : [[Dev/Services/Dask|Dask]] réimplémente l'API numpy en `dask.array`.
- GPU / autodiff : [[Dev/Services/CuPy|CuPy]] (drop-in GPU), [[Dev/Services/JAX|JAX]], [[Dev/Services/PyTorch|PyTorch]].
- Doc : https://numpy.org/doc/stable/
