---
role: brique
nom: Ray
alias: [ray, ray-project, ray core]
pitch: "Moteur de calcul distribué Python (« AI compute engine ») : un runtime de tâches et d'acteurs scalant du laptop au cluster, surmonté de bibliothèques ML (Train, Tune, Serve, Data, RLlib)."
categorie: compute/distribue
famille: paquet
licence_type: open-source
maturite: production
langage: Python / C++
alternatives: ["[[Dask]]", "[[Spark]]"]
complements: []
tags: [distributed, parallel, gpu]
url_docs: https://docs.ray.io/
url_repo: https://github.com/ray-project/ray
---

# Ray

<!-- AUTO:BANDEAU:START -->
> Moteur de calcul distribué Python (« AI compute engine ») : un runtime de tâches et d'acteurs scalant du laptop au cluster, surmonté de bibliothèques ML (Train, Tune, Serve, Data, RLlib).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python / C++ | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de calcul distribué pour Python, issu du RISELab de Berkeley, porté par Anyscale
et entré à la PyTorch Foundation en 2025. Son unité n'est ni la table ni le tableau mais la
**tâche** (`@ray.remote` sur une fonction) et l'**acteur** (une classe à état) : c'est ce
qui lui permet de distribuer du code Python quelconque, et pas seulement des collections.
Le cœur — un ordonnanceur et un object store partagé en mémoire — porte tout un étage de
bibliothèques ML : [[Ray Tune]] pour l'optimisation d'hyperparamètres, [[Ray Serve]] pour
le serving, Ray Train, Ray Data et RLlib. Le même code passe du portable au cluster.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Paralléliser du code Python arbitraire — simulations, traitements sur mesure, pipelines hétérogènes | La **sérialisation** cloudpickle des objets passés aux tâches et acteurs surprend : objets non picklables, copies coûteuses dans l'object store |
| Charges ML/IA distribuées : entraînement multi-GPU, HPO, serving, RL, via l'écosystème | Ressources mal déclarées (`num_cpus`, `num_gpus`) : sur-souscription, ou GPU laissés inutilisés |
| Calcul **à état** distribué grâce aux acteurs — services longs, agents, accumulateurs | L'object store partagé est en mémoire : quand il déborde, le spilling disque plombe les temps |
| Scaler du portable au cluster avec une seule API — K8s via KubeRay, cloud | Écosystème large et mouvant : épingler les versions de Tune, Serve et Train, qui évoluent vite |
| | Données qui tiennent sur une machine → [[Polars]] ou [[pandas]], sans cluster à gérer |

## Mise en œuvre

- Installation — `uv add "ray[default]"` ; extras `ray[train]`, `ray[tune]`, `ray[serve]`, `ray[data]`
- Point d'entrée — import Python, `@ray.remote` sur fonctions et classes, puis `ray.get`
- Prérequis — Python ; un cluster (Kubernetes via KubeRay, cloud, HPC) pour le multi-nœuds
- Exécution — cluster local en une commande, ou multi-nœuds self-hébergé ; managé chez Anyscale, avec autoscaling et observabilité
- Coût — gratuit, Apache-2.0 ; le coût réel est l'infrastructure CPU/GPU, ou l'abonnement Anyscale

## Écosystème

### Alternatives

- [[Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark.

## Ressources

- Documentation — https://docs.ray.io/
- Dépôt — https://github.com/ray-project/ray

## Voir aussi

- [[Calcul distribué]] — le hub du domaine
- [[Ray Tune]] · [[Ray Serve]] — la famille Ray, bâtie sur ce cœur
- [[Modin]] — peut prendre Ray comme backend d'exécution
- [[Comparatif - Calcul distribué]] — ce qui départage les moteurs du dossier
