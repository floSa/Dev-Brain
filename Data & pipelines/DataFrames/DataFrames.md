---
role: hub
nom: DataFrames
alias: [manipulation de données, tables en mémoire]
pitch: Charger, filtrer, joindre et agréger de la donnée tabulaire en mémoire — le geste le plus fréquent de tout le domaine.
domaines: [data-sci, data-eng]
tags: [dataframe, array, lazy-evaluation, out-of-core]
---

# DataFrames

> Charger, filtrer, joindre et agréger de la donnée tabulaire en mémoire — le geste le plus fréquent de tout le domaine.

## Ce qu'il faut comprendre

- Deux structures se cachent sous le mot « tableau », et les confondre coûte cher. Le **ndarray** ([[numpy]]) est un bloc contigu d'un seul type, sans nom de colonne — c'est le socle numérique. Le **DataFrame** ([[pandas]], [[Polars]]) est un ensemble de colonnes typées, nommées, indexables. On ne fait pas un group-by sur un ndarray, on ne fait pas d'algèbre linéaire sur un DataFrame.
- Le clivage décisif est **eager contre lazy**. [[pandas]] exécute chaque opération immédiatement et matérialise un intermédiaire à chaque étape. [[Polars]] construit un plan, l'optimise (élagage de colonnes, descente de filtres, fusion d'étapes) puis exécute. Sur une chaîne de dix opérations, l'écart n'est pas un facteur de vitesse, c'est un facteur de mémoire.
- Le mur réel n'est pas le CPU, c'est la **RAM**. Trois échappatoires, et elles ne sont pas interchangeables : paralléliser sur les cœurs sans réécrire ([[Modin]]), streamer en dehors de la mémoire ([[Polars]] en mode streaming), ou distribuer sur plusieurs machines — ce qui sort de ce sous-domaine.
- Au-delà de deux dimensions, l'index de [[pandas]] cesse d'être le bon outil. [[xarray]] ajoute dimensions nommées, coordonnées et attributs par-dessus [[numpy]] : c'est ce qu'attendent les données climatiques, géospatiales et tout ce qui vit en NetCDF.
- **Apache Arrow** est la raison pour laquelle ces briques s'échangent des données sans les recopier. C'est aussi ce qui rend un pont [[connectorx]] → [[Polars]] presque gratuit, là où passer par des objets Python coûte un ordre de grandeur.

## Choisir

- Le cas général, l'écosystème le plus large, des exemples partout → [[pandas]].
- Une chaîne de transformations sur un jeu qui frôle la RAM, ou la vitesse comme critère → [[Polars]].
- Du code [[pandas]] existant à accélérer sans le réécrire → [[Modin]].
- Du calcul numérique pur, des matrices, de la vectorisation → [[numpy]].
- Des tableaux à plus de deux dimensions, avec des axes qui ont un sens physique → [[xarray]].
- Une base SQL à charger vite dans l'un des précédents → [[connectorx]].

<!-- AUTO:START -->
### Briques
- [[Modin]] — Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.
- [[numpy]] — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.
- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.
- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.
- [[xarray]] — Tableaux N-dimensionnels étiquetés : ajoute dimensions, coordonnées et attributs au-dessus de numpy — le pandas des données multidimensionnelles (NetCDF, climat, géospatial).

### Comparatifs
- [[Comparatif - Manipulation de données]]
<!-- AUTO:END -->
