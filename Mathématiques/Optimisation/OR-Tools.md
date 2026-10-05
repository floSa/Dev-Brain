---
role: brique
nom: OR-Tools
alias: [Google OR-Tools, ortools, CP-SAT, CP-SAT solver, Google Optimization Tools]
pitch: "Suite C++ de Google pour l'optimisation combinatoire, utilisable depuis Python : solveur CP-SAT (contraintes sur entiers, recherche parallèle), solveurs LP (Glop, PDLP), enveloppes MIP vers des solveurs tiers, bibliothèque de tournées et algorithmes de graphes ; Apache-2.0."
categorie: math/optimisation
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[PuLP]]", "[[Pyomo]]", "[[CVXPY]]", "[[HiGHS]]", "[[PyVRP]]"]
complements: []
tags: [constraint-programming, combinatorial-optimization, linear-programming, scheduling, vehicle-routing]
url_docs: https://developers.google.com/optimization/
url_repo: https://github.com/google/or-tools
---

# OR-Tools

<!-- AUTO:BANDEAU:START -->
> Suite C++ de Google pour l'optimisation combinatoire, utilisable depuis Python : solveur CP-SAT (contraintes sur entiers, recherche parallèle), solveurs LP (Glop, PDLP), enveloppes MIP vers des solveurs tiers, bibliothèque de tournées et algorithmes de graphes ; Apache-2.0.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Suite logicielle de Google pour les problèmes d'**optimisation combinatoire**, écrite en C++ avec des
interfaces Python, C# et Java. Le README la décrit en six blocs : deux solveurs de programmation par
contraintes (CP* et **CP-SAT**), deux solveurs de programmation linéaire (Glop, simplexe, et PDLP,
méthode de premier ordre), des enveloppes autour de solveurs commerciaux ou libres, dont les solveurs en
nombres entiers, des algorithmes de sacs à dos et de bin packing, des algorithmes de **tournées**
(voyageur de commerce, VRP) et des algorithmes de graphes (plus court chemin, flots, affectation).

L'élément qui structure l'usage est **CP-SAT** : un solveur qui travaille sur des **entiers** et qui sert
aussi bien un modèle de contraintes qu'un modèle linéaire en nombres entiers. Il porte les variables
d'intervalle et les contraintes `no_overlap` et `cumulative` de l'ordonnancement. À l'inverse de
[[PuLP]], OR-Tools est à la fois le modeleur et le solveur.

Relevé le 2026-10-05 : **v9.15** du 2026-01-12 (9.14 le 2025-06-19), paquet PyPI `ortools` 9.15.6755 du
2026-01-14, classé *Production/Stable*, Python 3.9 et plus ; dépôt actif (dernier commit sur la branche
`stable` le 2026-09-17, push du 2026-10-05) ; licence Apache-2.0 lue dans le fichier `LICENSE`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un problème riche en règles — ordre, exclusion, cardinalité, ressources : CP-SAT, avec ses intervalles, est fait pour ça ([[Programmation par contraintes]]) | Un LP ou un MIP purement linéaire et de grande taille : un solveur linéaire dédié comme [[HiGHS]] est plus direct, et CP-SAT impose des coefficients entiers |
| Ordonnancer un atelier ou construire un planning de personnel, sans licence à acheter ([[Ordonnancement d'atelier (job-shop, flow-shop)]], [[Plannings de personnel (rostering)]]) | Une optimisation convexe ou non linéaire : CP-SAT n'a pas de nombres réels, voir [[CVXPY]] ou [[Pyomo]] |
| Un seul paquet qui couvre contraintes, LP, tournées et graphes, appelable depuis Python | Des tournées de grande taille ou riches en variantes : [[PyVRP]] s'y consacre, et sa propre comparaison place le module de routage d'OR-Tools en retrait au-delà de 500 visites (source partie prenante) |
| Changer de solveur sans réécrire : l'interface MIP enveloppe plusieurs solveurs, dont des solveurs commerciaux comme Gurobi ou CPLEX | Seulement exprimer un modèle LP/MIP lisible et passer la main à un solveur au choix : [[PuLP]] est plus court |

## Mise en œuvre

- Installation — `uv add ortools` ; le binaire est dans la roue, aucun solveur à installer
- Point d'entrée — `from ortools.sat.python import cp_model`, puis `CpModel()` pour déclarer variables (`new_int_var`) et contraintes (`add`, `add_no_overlap`, `add_cumulative`) et `CpSolver().solve(model)`
- Prérequis — Python 3.9 minimum ; **tout coefficient et tout domaine de CP-SAT est un entier** : multiplier les grandeurs décimales (centimes plutôt qu'euros, minutes plutôt qu'heures) avant de les poser
- Exécution — dans le process appelant ; `solver.parameters.max_time_in_seconds` borne le temps, `num_workers` règle le parallélisme, `log_search_progress = True` affiche la borne et l'écart
- Coût — gratuit, Apache-2.0 ; aucune édition payante n'apparaît dans le README ni dans la documentation lus

## Limites à connaître

- **Le statut se lit avant la valeur.** `solve` renvoie `OPTIMAL`, `FEASIBLE`, `INFEASIBLE`, `MODEL_INVALID` ou `UNKNOWN` ; une limite de temps rend `FEASIBLE`, pas l'optimum. L'écart entre la meilleure solution et la borne inférieure dit s'il reste à chercher.
- **Le parallélisme change le résultat.** CP-SAT est conçu pour le parallèle : la documentation de dépannage place le seuil de la recherche parallèle à 8 travailleurs, qui mêlent relaxations linéaires, recherche par cœurs, voisinages (LNS) et solveurs de première solution ; à 16 et au-delà s'ajoutent des sous-solveurs qui améliorent la borne. Mesurer sur la machine cible, pas sur un portable.
- **Modèle infaisable** : la documentation propose les hypothèses (`assumptions`) pour obtenir un sous-ensemble de contraintes en conflit, plutôt que deviner.
- **Le routage et CP-SAT sont deux outils.** La bibliothèque de tournées a son propre modèle (`RoutingModel`) ; les contraintes de CP-SAT ne s'y ajoutent pas directement.

## Écosystème

### Alternatives

- [[PuLP]] — Modeleur de programmation linéaire et en nombres entiers (LP/MIP) en Python : on décrit le modèle en objets Python, PuLP le passe à un solveur (CBC par défaut, ou Gurobi, CPLEX, HiGHS…). — le même besoin pour un modèle linéaire, par un modeleur qui délègue la résolution plutôt que par une suite qui porte son propre solveur ; PuLP sait d'ailleurs appeler CP-SAT.
- [[Pyomo]] — Langage de modélisation algébrique en Python pour LP, MIP, non linéaire, disjonctif et stochastique : le modèle est un objet Python, la résolution est confiée à un solveur externe que Pyomo n'installe pas ; BSD-3-Clause, projet COIN-OR. — le modeleur à choisir quand le problème sort du linéaire entier.
- [[CVXPY]] — Langage de modélisation Python pour l'optimisation convexe : le problème s'écrit comme les maths, CVXPY vérifie la convexité (DCP) puis le traduit pour un solveur (Clarabel, OSQP et SCS livrés, HiGHS, SCIP et d'autres en option) ; Apache-2.0. — le choix quand les variables sont réelles et le problème convexe, où CP-SAT n'a pas de réels.
- [[HiGHS]] — Solveur libre de programmation linéaire, quadratique convexe et en nombres entiers (simplexe, points intérieurs, PDLP, un solveur MIP), en C++ sans dépendance, appelé par highspy et par la plupart des modeleurs Python ; MIT, ni non linéaire ni QP en entiers. — le solveur linéaire et MIP dédié, à la place des solveurs MIP d'OR-Tools, quand le modèle est linéaire et grand.
- [[PyVRP]] — Solveur de tournées de véhicules en Python à cœur C++ : capacités, fenêtres de temps, flotte hétérogène, multi-dépôts, collectes-livraisons, clients optionnels, recherche locale itérée ; MIT, avec une édition Enterprise payante vendue à part. — le spécialiste des tournées, à la place du module de routage d'OR-Tools.

### Compléments

Aucun complément déclaré : OR-Tools se suffit pour contraintes, LP et tournées ; les modeleurs voisins sont des alternatives.

## Ressources

- Documentation — https://developers.google.com/optimization/
- Dépôt — https://github.com/google/or-tools
- Guide CP-SAT — https://github.com/google/or-tools/tree/stable/ortools/sat/docs

## Voir aussi

- [[Optimisation]] — le hub du dossier
- [[Programmation par contraintes]] — la notion : domaines, propagation, contraintes globales, CP-SAT
- [[Programmation linéaire en nombres entiers (MIP)]] — la notion voisine, pour les modèles linéaires
- [[Optimisation combinatoire]] — la classe de problèmes que la suite résout
- [[Tournées de véhicules (VRP)]] — le problème que sa bibliothèque de routage traite
- [[Comparatif - Solveurs d'optimisation]] — la vue du dossier
