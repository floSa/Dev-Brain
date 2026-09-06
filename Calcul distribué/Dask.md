---
role: brique
nom: Dask
alias: [dask, dask.distributed]
pitch: "Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster."
categorie: compute/distribue
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[pandas]]", "[[Polars]]", "[[numpy]]", "[[Modin]]", "[[Spark]]", "[[Ray]]"]
complements: ["[[xarray]]"]
tags: [distributed, parallel, out-of-core, lazy-evaluation]
url_docs: https://docs.dask.org/
url_repo: https://github.com/dask/dask
---

# Dask

<!-- AUTO:BANDEAU:START -->
> Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de calcul parallèle et distribué en **Python pur**, à deux étages. En haut,
des collections qui imitent les API connues — `dask.array` pour numpy, `dask.dataframe`
pour pandas, `dask.bag` — de sorte qu'on scale du code familier sans le réécrire. En bas,
un planificateur de tâches : les opérations sont **paresseuses**, elles construisent un
graphe, optimisé puis exécuté au `.compute()` sur les cœurs d'une machine ou sur un cluster
via `dask.distributed`. C'est ce qui permet de traiter, par morceaux, des données plus
grosses que la RAM.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Jeux plus grands que la RAM, ou trop lents sur une machine, tout en gardant l'API numpy/pandas | Tout est **paresseux** : rien ne se calcule avant `.compute()` — penser en graphe, pas en exécution immédiate |
| Passer à un cluster multi-nœuds avec `dask.distributed` — K8s, HPC, cloud | Le **partitionnement** (taille des chunks) fait toute la performance : mal réglé, c'est la lenteur ou l'OOM |
| Paralléliser du code Python arbitraire au-delà des dataframes — `dask.delayed`, futures | Couverture pandas/numpy **partielle** : tri global et certains `merge` restent coûteux ou absents |
| Scaler scikit-learn ou XGBoost via leurs intégrations Dask | Le distribué ajoute sérialisation et réseau : ne pas l'introduire si une machine suffit |
| | Données qui tiennent en mémoire sur un nœud → [[pandas]] ou [[Polars]], plus simples et souvent plus rapides à cette échelle |
| | Vitesse mono-nœud sans cluster → [[Polars]], multi-thread et streaming |
| | Garder l'API pandas sans gérer de graphe ni de cluster → [[Modin]], drop-in, qui peut d'ailleurs tourner sur Dask |
| | Calcul de tableaux N-dimensionnels qui tient en RAM → [[numpy]] seul |

## Mise en œuvre

- Installation — `uv add "dask[complete]"`
- Point d'entrée — import Python : `dask.array`, `dask.dataframe`, `dask.delayed`, puis `.compute()`
- Prérequis — 100 % Python, rien d'autre en local ; un cluster pour le mode distribué
- Exécution — scheduler local en threads ou processus sans configuration, ou cluster `dask.distributed` sur K8s, HPC, cloud
- Coût — gratuit, BSD-3-Clause ; le coût réel est l'infrastructure du cluster, auto-hébergée ou managée (Coiled)

## Écosystème

### Alternatives

- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.
- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.
- [[numpy]] — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.
- [[Modin]] — Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark.
- [[Ray]] — Moteur de calcul distribué Python (« AI compute engine ») : un runtime de tâches et d'acteurs scalant du laptop au cluster, surmonté de bibliothèques ML (Train, Tune, Serve, Data, RLlib).

### Compléments

- [[xarray]] — Tableaux N-dimensionnels étiquetés : ajoute dimensions, coordonnées et attributs au-dessus de numpy — le pandas des données multidimensionnelles (NetCDF, climat, géospatial). — les tableaux étiquetés qui dépassent la RAM en `chunks=`, la voie documentée du passage à l'échelle

## Ressources

- Documentation — https://docs.dask.org/
- Dépôt — https://github.com/dask/dask

## Voir aussi

- [[Calcul distribué]] — le hub du domaine
- [[Comparatif - Calcul distribué]] — ce qui départage les moteurs du dossier
