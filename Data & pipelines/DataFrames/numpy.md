---
role: brique
nom: numpy
alias: [np, NumPy]
pitch: "Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique."
categorie: data/tableau
famille: paquet
licence_type: open-source
maturite: production
langage: C / Python
alternatives: ["[[xarray]]", "[[Dask]]", "[[CuPy]]"]
complements: []
tags: [array, in-memory]
url_docs: https://numpy.org/doc/stable/
url_repo: https://github.com/numpy/numpy
---

# numpy

<!-- AUTO:BANDEAU:START -->
> Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C / Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-06 |
<!-- AUTO:BANDEAU:END -->

## Définition

Le cœur est le `ndarray` : un tableau **N-dimensionnel homogène** stocké de façon contiguë
en mémoire, sur lequel les opérations sont vectorisées en C, sans boucle Python. Autour de
lui viennent le *broadcasting*, l'indexation avancée, l'algèbre linéaire (`linalg`, adossée
à BLAS/LAPACK), les transformées de Fourier, le tirage aléatoire reproductible
(`np.random.default_rng`) et un système de `dtype`. Trois conséquences se paient à l'usage :
un seul `dtype` par tableau, donc rien d'hétérogène ; le slicing renvoie le plus souvent une
**vue**, si bien que la modifier modifie la source ; et les entiers à largeur fixe débordent
en silence. C'est la brique sur laquelle reposent [[pandas]], scikit-learn, SciPy et
matplotlib.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Calcul numérique pur sur vecteurs, matrices et tenseurs : algèbre linéaire, statistiques, simulation | Tableaux plus grands que la RAM, ou calcul à distribuer → [[Dask]] et son `dask.array`, de même API |
| Vectoriser pour la performance : remplacer des boucles Python par des opérations sur tableaux entiers | Accélération **GPU** d'un code numpy existant → [[CuPy]], compatible drop-in |
| Servir d'interface bas niveau entre bibliothèques — c'est le format d'échange numérique de l'écosystème | Différentiation automatique → [[JAX]] ou [[PyTorch]] : numpy ne dérive pas |
| Tirage aléatoire reproductible par générateur explicite | Le *broadcasting* peut aligner des formes par erreur : vérifier les `shape` reste à la charge de l'appelant |

## Mise en œuvre

- Installation — `uv add numpy`
- Point d'entrée — import Python, `import numpy as np` ; cœur compilé en C
- Prérequis — Python ; une BLAS/LAPACK est embarquée dans les roues officielles
- Exécution — dans le process appelant, mono-nœud et en mémoire ; certaines routines `linalg` sont multi-thread via BLAS
- Coût — gratuit, licence BSD-3-Clause, aucune limite d'usage

## Écosystème

### Alternatives

- [[xarray]] — Tableaux N-dimensionnels étiquetés : ajoute dimensions, coordonnées et attributs au-dessus de numpy — le pandas des données multidimensionnelles (NetCDF, climat, géospatial).
- [[Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.
- [[CuPy]] — NumPy/SciPy sur GPU : tableau ndarray compatible drop-in exécuté sur CUDA/ROCm, pour accélérer le calcul numérique existant sans réécrire le code.

## Ressources

- Documentation — https://numpy.org/doc/stable/
- Dépôt — https://github.com/numpy/numpy

## Voir aussi

- [[DataFrames]] — le hub du dossier
- [[pandas]] — bâti dessus : ses colonnes sont des `ndarray`
- [[Comparatif - Manipulation de données]] — ce qui départage les outils du dossier
