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
complements: []
tags: [distributed, parallel, out-of-core, lazy-evaluation]
url_docs: https://docs.dask.org/
url_repo: https://github.com/dask/dask
---

# Dask

## Pourquoi

Bibliothèque de **calcul parallèle et distribué en Python pur**. Deux étages : des **collections** qui imitent les API connues — `dask.array` (≈ [[numpy]]), `dask.dataframe` (≈ [[pandas]]), `dask.bag` — et un **planificateur de tâches**. Les opérations sont **paresseuses** : elles construisent un graphe de tâches, optimisé puis exécuté (`.compute()`) en parallèle, sur les cœurs d'une machine ou sur un **cluster** via `dask.distributed`. Permet de traiter des données **plus grosses que la RAM** (par morceaux) et de scaler des bibliothèques familières sans tout réécrire.

## Quand l'utiliser

- Jeux **plus grands que la RAM** ou trop lents sur une machine, tout en gardant l'API numpy/pandas.
- Passage à un **cluster** multi-nœuds avec un scheduler distribué (`dask.distributed`).
- Pipelines de tâches **personnalisés** au-delà des dataframes : `dask.delayed`, `futures` pour paralléliser du code Python arbitraire.
- Scaler scikit-learn, XGBoost, etc. via leurs intégrations Dask.

## Quand NE PAS l'utiliser

- Données qui tiennent en mémoire sur un nœud → [[pandas]] ou [[Polars]] (plus simples, souvent plus rapides à cette échelle).
- Besoin de vitesse single-node sans cluster → [[Polars]] (multi-thread + streaming).
- Garder l'API pandas sans gérer un graphe / cluster → [[Modin]] (drop-in, peut d'ailleurs tourner sur Dask).
- Calcul array N-dim qui tient en RAM → [[numpy]] seul.

## Déploiement & coût

- Bibliothèque (`uv add "dask[complete]"`) ; 100 % Python. BSD-3-Clause, gratuit.
- **Scheduler local** (threads/processus) sans configuration, ou **cluster distribué** (`dask.distributed`) sur K8s, HPC, cloud.
- Coût = l'infra du cluster (auto-hébergé ou managé, ex. Coiled). Maintenue par une communauté large (Anaconda, Coiled, NVIDIA…).

## Pièges

- Tout est **paresseux** : rien ne se calcule avant `.compute()` — penser en graphe, pas en exécution immédiate.
- Le **partitionnement** (taille des chunks/partitions) conditionne la performance ; mal réglé = lenteur ou OOM.
- Couverture pandas/numpy **partielle** : certaines opérations (tri global, certains `merge`) sont coûteuses ou absentes.
- Le distribué ajoute de la complexité (sérialisation, réseau) : ne pas l'introduire si une seule machine suffit.

## Alternatives

- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.
- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.
- [[numpy]] — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.
- [[Modin]] — Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark.
- [[Ray]] — Moteur de calcul distribué Python (« AI compute engine ») : un runtime de tâches et d'acteurs scalant du laptop au cluster, surmonté de bibliothèques ML (Train, Tune, Serve, Data, RLlib).

## Liens

- APIs scalées : [[pandas]] (`dask.dataframe`) et [[numpy]] (`dask.array`).
- Peut servir de moteur d'exécution à [[Modin]].
- Autres moteurs de calcul distribué : [[Spark]] (big data JVM), [[Ray]] (Python ML).
- [[Comparatif - Calcul distribué]] — comparatif de la catégorie
- Doc : https://docs.dask.org/
