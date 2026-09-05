---
role: brique
nom: Modin
alias: [modin]
pitch: "Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI."
categorie: data/tableau
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[pandas]]", "[[Polars]]", "[[Dask]]"]
complements: []
tags: [dataframe, parallel, distributed]
url_docs: https://modin.readthedocs.io/
url_repo: https://github.com/modin-project/modin
---

# Modin

<!-- AUTO:BANDEAU:START -->
> Accélère pandas sans réécriture : `import modin.pandas as pd` parallélise les opérations sur tous les cœurs, avec backends Ray, Dask ou unidist/MPI.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Remplaçant transparent de [[pandas]] : on change une ligne d'import
(`import modin.pandas as pd`) et le code existant s'exécute **en parallèle sur tous les
cœurs** au lieu d'un seul thread. L'exécution est déléguée à un moteur interchangeable —
Ray, Dask ou unidist/MPI — ce qui ouvre le passage au cluster sans réécrire la logique. La
couverture de l'API pandas se veut quasi complète, mais elle n'est **pas totale** : ce qui
n'est pas implémenté retombe **silencieusement** sur pandas, donc sans gain et sans
avertissement. Le comportement dépend par ailleurs du moteur retenu, qu'il faut fixer et
tester, et les anti-patterns pandas restent coûteux une fois parallélisés.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Base de code **pandas existante** trop lente, qu'on ne veut pas réécrire | Pipeline déjà exprimé en graphes de tâches, calcul array et dataframe distribué de bout en bout → [[Dask]] directement |
| Saturer tous les cœurs d'un poste sur des opérations pandas : lecture, group-by, apply | Petits jeux de données : la surcharge de parallélisation coûte plus qu'elle ne rapporte |
| Passer plus tard au **cluster** en gardant l'API pandas | Couverture d'API non totale, et le non-implémenté retombe **en silence** sur pandas — le gain disparaît sans le dire |
| | Ne corrige aucun anti-pattern : un `apply` ligne à ligne reste coûteux, même parallélisé |

## Mise en œuvre

- Installation — `uv add "modin[ray]"`, ou `modin[dask]` / `modin[mpi]` selon le moteur
- Point d'entrée — un seul import à changer, `import modin.pandas as pd`
- Prérequis — Python ; le moteur se choisit à l'installation ou par variable d'environnement
- Exécution — multi-cœurs sur une machine par défaut ; distribué sur un cluster Ray ou Dask à provisionner
- Coût — gratuit en Apache-2.0 ; le coût d'infra est celui du moteur choisi

## Écosystème

### Alternatives

- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python.
- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core.
- [[Dask]] — Calcul parallèle et distribué Python natif : collections imitant numpy et pandas (dask.array / dask.dataframe), exécutées en graphes de tâches paresseux, du portable au cluster.

## Ressources

- Documentation — https://modin.readthedocs.io/
- Dépôt — https://github.com/modin-project/modin

## Voir aussi

- [[DataFrames]] — le hub du dossier
- [[Comparatif - Manipulation de données]] — ce qui départage les outils du dossier
