---
galaxie: dev
type: service
nom: Modin
alias: [modin]
pitch: "Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI."
categorie: tooling/data
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/pandas|pandas]]", "[[Dev/Services/Polars|Polars]]", "[[Dev/Services/Dask|Dask]]"]
remplace_par: []
status: actif
tags: [dataframe, parallel, distributed]
url_docs: https://modin.readthedocs.io/
url_repo: https://github.com/modin-project/modin
---

# Modin

## Pourquoi

**Remplaçant transparent de [[Dev/Services/pandas|pandas]]** : on change une ligne d'import (`import modin.pandas as pd`) et le code pandas existant tourne **en parallèle sur tous les cœurs** au lieu d'un seul thread. Modin vise une couverture quasi complète de l'API pandas et délègue l'exécution à un moteur de calcul interchangeable : **Ray**, **Dask** ou **unidist/MPI**. La promesse : un *speedup* immédiat sur une machine, puis un passage au **cluster** sans réécrire la logique.

## Quand l'utiliser

- Base de code **pandas existante** lente, qu'on ne veut pas réécrire : Modin la parallélise sans changement.
- Saturer tous les cœurs d'un poste de travail sur des opérations pandas (lecture, group-by, apply).
- Besoin de passer à l'échelle vers un **cluster** Ray/Dask plus tard, en gardant l'API pandas.

## Quand NE PAS l'utiliser

- Projet neuf sans dette pandas, où la performance prime → [[Dev/Services/Polars|Polars]] (plus rapide nativement).
- Petits jeux de données : la surcharge du moteur parallèle peut être plus lente que [[Dev/Services/pandas|pandas]] seul.
- Pipeline déjà orchestré en graphes de tâches, calcul array/dataframe distribué de bout en bout → [[Dev/Services/Dask|Dask]] directement.
- Couverture d'une API pandas exotique : Modin retombe sur pandas pour le non-implémenté (sans gain).

## Déploiement & coût

- Bibliothèque (`uv add "modin[ray]"` / `[dask]` / `[mpi]`) ; choix du moteur par variable d'env ou install. Apache-2.0, gratuit.
- **Parallèle multi-cœurs** par défaut sur une machine ; **distribué** sur cluster via le backend Ray ou Dask.
- Coût d'infra = celui du backend choisi (cluster Ray/Dask à provisionner pour le multi-nœuds).

## Pièges

- Surcharge de parallélisation : sur petits volumes, Modin peut être plus lent que pandas.
- Couverture d'API **non totale** : les méthodes non supportées retombent silencieusement sur pandas (perte du gain).
- Le comportement dépend du backend (Ray/Dask/MPI) — fixer et tester le moteur ciblé.
- N'élimine pas les anti-patterns pandas (`apply` ligne à ligne reste coûteux, même parallélisé).

## Alternatives

- [[Dev/Services/pandas|pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.
- [[Dev/Services/Polars|Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.
- [[Dev/Services/Dask|Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.

## Liens

- API cible : [[Dev/Services/pandas|pandas]] — Modin en est un drop-in replacement.
- Moteur d'exécution possible : [[Dev/Services/Dask|Dask]] (aussi Ray, unidist/MPI — hors brain pour Ray).
- [[Dev/Patterns/Comparatif - Manipulation de données]] — Modin vs pandas / Polars / numpy.
- Doc : https://modin.readthedocs.io/
