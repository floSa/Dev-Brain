---
galaxie: dev
type: service
nom: Ray
alias: [ray, ray-project, ray core]
pitch: "Moteur de calcul distribué Python (« AI compute engine ») : un runtime de tâches et d'acteurs scalant du laptop au cluster, surmonté de bibliothèques ML (Train, Tune, Serve, Data, RLlib)."
categorie: compute/distributed
licence_type: open-source
hosted: both
maturite: production
langage: Python / C++
scaling: distributed
alternatives: ["[[Dev/Services/Dask|Dask]]", "[[Dev/Services/Spark|Spark]]"]
remplace_par: []
status: actif
tags: [distributed, parallel, gpu]
url_docs: https://docs.ray.io/
url_repo: https://github.com/ray-project/ray
---

# Ray

## Pourquoi

Framework de **calcul distribué pour Python**, issu du RISELab de Berkeley et porté par Anyscale (entré à la PyTorch Foundation en 2025). Deux étages : un **cœur** (Ray Core) qui distribue du code Python arbitraire via deux primitives — les **tâches** (`@ray.remote` sur des fonctions) et les **acteurs** (classes à état) — sur les cœurs d'une machine ou un cluster, avec un object store partagé en mémoire ; et un **ensemble de bibliothèques ML** bâties dessus — [[Dev/Services/Ray Tune|Ray Tune]] (HPO), [[Dev/Services/Ray Serve|Ray Serve]] (serving), Ray Train (entraînement distribué), Ray Data (traitement), RLlib (RL). Le même code passe du portable au cluster sans réécriture.

## Quand l'utiliser

- Paralléliser du **code Python arbitraire** (pas seulement des dataframes) : simulations, traitements custom, pipelines hétérogènes.
- Charges **ML/IA distribuées** : entraînement multi-GPU, HPO, serving, RL — via les bibliothèques de l'écosystème.
- Calcul **à état** distribué grâce aux acteurs (services longs, agents, accumulateurs).
- Scaler du laptop au **cluster** (K8s via KubeRay, cloud) avec une seule API.

## Quand NE PAS l'utiliser

- Mise à l'échelle d'API **numpy/pandas** familières → [[Dev/Services/Dask|Dask]] (collections drop-in, plus simple pour ce cas).
- Traitement **big data** SQL / DataFrame sur écosystème JVM → [[Dev/Services/Spark|Spark]].
- Données qui tiennent sur une machine → [[Dev/Services/Polars|Polars]] / [[Dev/Services/pandas|pandas]] ; pas de cluster à gérer.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), `uv add "ray[default]"` (extras `ray[train]`, `ray[tune]`, `ray[serve]`, `ray[data]`).
- **Self-host** : cluster local en une commande, ou multi-nœuds sur Kubernetes (KubeRay), cloud, HPC.
- **Managé** : Anyscale (payant) — clusters Ray opérés, autoscaling et observabilité sans gérer l'infra.
- Coût = l'infra du cluster (CPU/GPU) ; le runtime est gratuit.

## Pièges

- La **sérialisation** (cloudpickle) des objets passés aux tâches/acteurs peut surprendre : objets non picklables, copies coûteuses dans l'object store.
- Penser **placement des ressources** (`num_cpus`, `num_gpus`) : mal déclaré = sur-souscription ou GPU inutilisés.
- L'**object store** partagé est en mémoire : son débordement provoque du spilling disque, source de lenteurs.
- Écosystème large et mouvant : bien épingler les versions des bibliothèques (Tune/Serve/Train évoluent vite).

## Alternatives

- [[Dev/Services/Dask|Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.
- [[Dev/Services/Spark|Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark.

## Liens

- Famille Ray : [[Dev/Services/Ray Tune|Ray Tune]] (HPO), [[Dev/Services/Ray Serve|Ray Serve]] (serving) — bibliothèques bâties sur ce cœur.
- [[Comparatif - Calcul distribué]] — comparatif de la catégorie
- Peut servir de backend d'exécution à [[Dev/Services/Modin|Modin]].
- Doc : https://docs.ray.io/
