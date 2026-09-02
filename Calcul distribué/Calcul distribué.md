---
role: hub
nom: Calcul distribué
alias: [calcul distribue, distributed computing, cluster]
pitch: Faire tourner un calcul qui ne tient pas sur une machine — sur plusieurs nœuds, sur GPU, ou sur une infrastructure louée à la demande.
domaines: [data-eng, ml-eng, mlops]
tags: [distributed, gpu, parallel, out-of-core, distributed-training]
---

# Calcul distribué

> Faire tourner un calcul qui ne tient pas sur une machine — sur plusieurs nœuds, sur GPU, ou sur une infrastructure louée à la demande.

## Ce qu'il faut comprendre

- Trois problèmes distincts se cachent sous le mot « distribué », et chacun a ses briques. **Ça ne tient pas en RAM** → travailler par morceaux ([[Dask]], [[Spark]]). **C'est trop lent en séquentiel** → paralléliser sur des cœurs ou sur GPU ([[Ray]], [[CuPy]]). **Je n'ai pas la machine** → louer du calcul à la demande ([[Modal]], [[E2B]], [[Daytona]]).
- La première question à se poser est celle de la **nécessité**. Un cluster coûte en latence de démarrage, en sérialisation, en débogage et en exploitation. [[DuckDB]] ou [[Polars]] sur un seul serveur bien dimensionné battent souvent un petit cluster sur des volumes de quelques dizaines de gigaoctets. Le seuil de bascule est plus haut qu'on ne le croit.
- Le **modèle de programmation** départage plus que la performance. [[Spark]] impose un moteur SQL/DataFrame : très rapide dans son cadre, contraignant en dehors. [[Dask]] reproduit les API pandas et NumPy : la migration est presque gratuite, le contrôle moindre. [[Ray]] distribue des **tâches et des acteurs** Python quelconques : c'est le seul des trois qui accepte du code arbitraire, d'où son adoption côté ML et agents.
- Le **GPU** n'est pas du distribué mais s'y invite toujours : [[CuPy]] rejoue l'API NumPy sur CUDA, ce qui rend l'accélération d'un code numérique existant presque mécanique.

## Choisir

- Du pandas ou du NumPy qui déborde de la RAM → [[Dask]], API quasi identique.
- Un traitement batch massif dans un écosystème déjà JVM/Hadoop, ou du SQL sur plusieurs téraoctets → [[Spark]].
- Distribuer du Python arbitraire : entraînement, tuning, inférence, agents → [[Ray]].
- Du calcul numérique à accélérer sur GPU sans réécrire → [[CuPy]].
- Pas d'infrastructure et un besoin ponctuel de GPU ou de gros CPU → [[Modal]].
- Exécuter du code non fiable (généré par un LLM, soumis par un utilisateur) en bac à sable → [[E2B]].
- Des environnements de développement jetables et reproductibles → [[Daytona]].

<!-- AUTO:START -->
### Briques
- [[CuPy]] — NumPy/SciPy sur GPU : tableau ndarray compatible drop-in exécuté sur CUDA/ROCm, pour accélérer le calcul numérique existant sans réécrire le code.
- [[Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.
- [[Daytona]] — Bacs à sable managés pour code généré par IA — kernel dédié, snapshots d'état et démarrage annoncé sous 90 ms ; passé closed-source en juin 2026, le dépôt public restant figé à la v0.190.0 et non maintenu.
- [[E2B]] — Bacs à sable pour code généré par IA (Apache-2.0) — microVM Firecracker démarrant en moins de 200 ms, pilotée par SDK Python et TypeScript ; cloud managé ou infrastructure auto-hébergée déployée par Terraform.
- [[Modal]] — Plateforme de calcul serverless Python-first (propriétaire) — décorateurs à la place des Dockerfiles, démarrage à froid sous la seconde et facturation à la seconde ; ses Sandboxes isolent le code d'agent par gVisor, avec GPU disponible à l'intérieur.
- [[Ray]] — Moteur de calcul distribué Python (« AI compute engine ») : un runtime de tâches et d'acteurs scalant du laptop au cluster, surmonté de bibliothèques ML (Train, Tune, Serve, Data, RLlib).
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark.

### Comparatifs
- [[Comparatif - Calcul distribué]]
<!-- AUTO:END -->
