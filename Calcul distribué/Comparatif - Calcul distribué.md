---
role: comparatif
nom: Comparatif - Calcul distribué
categorie: compute/distribue
tags: [distributed, parallel, gpu, out-of-core]
---

# Comparatif - Calcul distribué

> On tranche sur : ce qu'on distribue — une table, un tableau, du code Python quelconque — ou bien on ne distribue rien du tout et l'on descend simplement sur le GPU.

![[Comparatif - Calcul distribué.base]]

## Ce qui départage

- [[Spark]] — le moteur **JVM** du big data : Spark SQL / DataFrames, Structured Streaming et MLlib sous une seule plateforme, avec derrière l'écosystème lakehouse (Hive, Iceberg, Delta) et les offres managées. L'overhead JVM pénalise les petits jobs, le **shuffle** est le goulet principal (partitionnement et skew à surveiller), et les UDF Python non vectorisées traversent lentement le pont Python↔JVM.
- [[Dask]] — le pendant **Python pur** : des collections qui imitent `numpy` et `pandas`, un planificateur paresseux qui construit puis exécute un graphe sur les cœurs ou un cluster, et `dask.delayed` pour du code arbitraire. Rien ne se calcule avant `.compute()`, le **partitionnement** fait toute la performance, et la couverture pandas/numpy reste partielle (tri global, certains `merge`).
- [[Ray]] — l'unité n'est ni la table ni le tableau mais la **tâche** et l'**acteur**, une classe à état : c'est ce qui permet de distribuer du code Python quelconque, et c'est ce qui porte l'écosystème ML ([[Ray Tune]], [[Ray Serve]], Ray Train, Ray Data, RLlib). La sérialisation cloudpickle surprend, les ressources (`num_cpus`, `num_gpus`) mal déclarées laissent des GPU inutilisés, et l'object store en mémoire *spille* sur disque quand il déborde.
- [[CuPy]] — le seul qui ne distribue rien : un **drop-in de [[numpy]] sur GPU** (CUDA ou ROCm) via cuBLAS/cuFFT/cuSOLVER, avec échange zéro-copie vers [[PyTorch]] et [[JAX]], et la possibilité d'écrire un noyau CUDA depuis Python. Le **transfert CPU↔GPU** domine vite le temps total, la couverture numpy/SciPy est large mais incomplète, et la correspondance version CUDA ↔ wheel est stricte.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
