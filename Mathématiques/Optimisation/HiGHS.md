---
role: brique
nom: HiGHS
alias: [highspy, HiGHS solver, HiGHS optimizer, ERGO-Code HiGHS]
pitch: "Solveur libre de programmation linéaire, quadratique convexe et en nombres entiers (simplexe, points intérieurs, PDLP, un solveur MIP), en C++ sans dépendance, appelé par highspy et par la plupart des modeleurs Python ; MIT, ni non linéaire ni QP en entiers."
categorie: math/optimisation
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[OR-Tools]]"]
complements: ["[[PuLP]]", "[[Pyomo]]", "[[CVXPY]]"]
tags: [linear-programming, optimization, combinatorial-optimization]
url_docs: https://ergo-code.github.io/HiGHS/
url_repo: https://github.com/ERGO-Code/HiGHS
---

# HiGHS

<!-- AUTO:BANDEAU:START -->
> Solveur libre de programmation linéaire, quadratique convexe et en nombres entiers (simplexe, points intérieurs, PDLP, un solveur MIP), en C++ sans dépendance, appelé par highspy et par la plupart des modeleurs Python ; MIT, ni non linéaire ni QP en entiers.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Solveur pour les modèles **linéaires creux de grande taille**, sous la forme : minimiser `½xᵀQx + cᵀx`
avec `L ≤ Ax ≤ U` et des bornes sur les variables. Quand `Q` est nulle, une partie des variables peut être
entière : HiGHS résout donc les **LP**, les programmes **quadratiques convexes** (`Q` semi-définie positive)
et les **MIP**. Il ne résout pas les QP dont des variables sont entières, ni le non linéaire.

La boîte contient les trois techniques classiques du LP — simplexe primal et dual (le dual est le défaut),
points intérieurs (IPX, série, et HiPO, par factorisation directe) et PDLP, méthode de premier ordre qui
tire parti d'un GPU —, deux techniques de QP (ensemble actif et points intérieurs) et un solveur MIP. Il
choisit la technique d'après le problème, l'option `solver` permet de la forcer. Le cœur est du C++ sans
dépendance tierce ; les interfaces sont C, C#, Fortran, Julia, Rust et Python (`highspy`).

C'est un **solveur**, pas un modeleur : il lit un modèle (fichier MPS ou LP, ou objets construits par
l'API) et rend une solution. On l'atteint donc le plus souvent par un modeleur, [[PuLP]], [[Pyomo]] ou
[[CVXPY]], dont les documentations le listent parmi leurs solveurs.

Relevé le 2026-10-05 : **v1.15.1** du 2026-07-02, paquet PyPI `highspy` 1.15.1, dépôt actif (push du
2026-10-04), licence MIT lue dans `LICENSE.txt` ; la documentation se présente elle-même comme un travail
en cours.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un LP ou un MIP linéaire, de taille moyenne à grande, résolu sans licence à acheter | Des contraintes combinatoires riches — ordre, exclusion, intervalles : [[OR-Tools]] (CP-SAT) est fait pour ça |
| Un solveur par défaut derrière un modeleur : [[PuLP]], [[Pyomo]] et [[CVXPY]] savent l'appeler | Un problème non linéaire, ou un QP avec des variables entières : HiGHS ne les traite pas, voir [[Pyomo]] avec un solveur non linéaire |
| Une dépendance légère à embarquer : pas de bibliothèque tierce, binaire C++ et roue Python | Les plus gros MIP, où les solveurs commerciaux (Gurobi, CPLEX) restent la référence : la page [[Programmation linéaire en nombres entiers (MIP)]] rappelle qu'une mauvaise formulation compte plus que le solveur |
| Résoudre un LP géant sur GPU avec PDLP | Un modèle écrit en objets Python lisibles, sans passer par l'API du solveur : prendre un modeleur et lui confier HiGHS |

## Mise en œuvre

- Installation — `uv add highspy` ; l'exécutable et la bibliothèque se compilent aussi avec CMake ; HiPO demande en plus le paquet `highspy-extras`, sous Apache-2.0
- Point d'entrée — `import highspy`, `h = highspy.Highs()`, puis lecture d'un fichier (`h.readModel`) ou construction du modèle, `h.run()` et lecture de la solution ; les journaux vont par défaut sur la console, un fichier se fixe par l'option `log_file`
- Prérequis — Python 3.9 minimum pour la roue
- Exécution — dans le process, ou en exécutable autonome sur un fichier MPS ou LP ; l'option `threads` vaut 0 par défaut, ce qui fait employer la moitié des fils de la machine, et la documentation juge peu utile d'en prendre plus de huit
- Coût — gratuit, MIT, aucune dépendance tierce

## Limites à connaître

- **Peu de parallélisme exploitable.** La documentation limite les gains aux simplexe dual, aux points intérieurs par factorisation et au MIP ; le simplexe dual parallèle est jugé peu utile. Un gain de temps vient surtout d'un meilleur modèle ou du PDLP sur GPU.
- **Un solveur sans non linéaire.** Le périmètre s'arrête au linéaire et au quadratique convexe.
- **Documentation en chantier.** Le site l'annonce lui-même ; recouper une option avec la liste des options et les exemples avant de la fixer.

## Écosystème

### Alternatives

- [[OR-Tools]] — Suite C++ de Google pour l'optimisation combinatoire, utilisable depuis Python : solveur CP-SAT (contraintes sur entiers, recherche parallèle), solveurs LP (Glop, PDLP), enveloppes MIP vers des solveurs tiers, bibliothèque de tournées et algorithmes de graphes ; Apache-2.0. — l'autre solveur libre de LP et de MIP, qui apporte en plus CP-SAT pour les modèles à contraintes.
- voisin : **CBC**, **GLPK** et **SCIP** — solveurs libres de LP et de MIP, appelés eux aussi par les modeleurs ; sans fiche dans le brain.
- voisin : **Gurobi** et **CPLEX** — solveurs commerciaux, pris en charge par les mêmes modeleurs ; sans fiche dans le brain (règle des briques libres).

### Compléments

- [[PuLP]] — Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…). — le modeleur qui lui passe le modèle.
- [[Pyomo]] — Langage de modélisation algébrique en Python pour LP, MIP, non linéaire, disjonctif et stochastique : le modèle est un objet Python, la résolution est confiée à un solveur externe que Pyomo n'installe pas ; BSD-3-Clause, projet COIN-OR. — le modeleur qui l'appelle, par `pip install highspy`.
- [[CVXPY]] — Langage de modélisation Python pour l'optimisation convexe : le problème s'écrit comme les maths, CVXPY vérifie la convexité (DCP) puis le traduit pour un solveur (Clarabel, OSQP et SCS livrés, HiGHS, SCIP et d'autres en option) ; Apache-2.0. — le modeleur convexe qui lui confie les LP, les QP et les MILP.

## Ressources

- Documentation — https://ergo-code.github.io/HiGHS/
- Dépôt — https://github.com/ERGO-Code/HiGHS
- Site — https://www.highs.dev

## Voir aussi

- [[Optimisation]] — le hub du dossier
- [[Programmation linéaire en nombres entiers (MIP)]] — la notion : formulation, relaxation, branch & bound
- [[Optimisation sous contrainte]] — la notion voisine, pour le cadre des contraintes
- [[Comparatif - Solveurs d'optimisation]] — la vue du dossier
