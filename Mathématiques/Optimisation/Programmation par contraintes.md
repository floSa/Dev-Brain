---
role: notion
nom: Programmation par contraintes
alias: [constraint programming, CP, CP-SAT, CSP, constraint satisfaction problem, problème de satisfaction de contraintes, contraintes globales, global constraints, alldifferent, propagation de contraintes, constraint propagation, cohérence d'arc, arc consistency, lazy clause generation, LCG, MiniZinc]
categorie: math/optimisation
domaines: [data-sci, ml-eng]
tags: [constraint-programming, combinatorial-optimization, scheduling]
---

# Programmation par contraintes

## Aperçu

- On **déclare** le problème au lieu de décrire comment le résoudre : des variables, un **domaine** de valeurs pour chacune, et des **contraintes** qui lient les variables. Un solveur cherche ensuite une affectation qui les satisfait toutes, ou la meilleure selon un objectif.
- Google définit la programmation par contraintes comme la recherche de solutions admissibles dans un très grand ensemble de candidats, quand le problème se modélise par des contraintes arbitraires, et la distingue de l'optimisation classique : elle est fondée sur la **faisabilité** plus que sur l'optimalité. Les solveurs modernes minimisent aussi un objectif.
- Dans ce dossier, elle est rangée avec les **méthodes de résolution** (règle D-R12) et non avec les problèmes de décision : une même modélisation sert un planning de personnel, un atelier ou une tournée, voir [[Plannings de personnel (rostering)]], [[Ordonnancement d'atelier (job-shop, flow-shop)]] et [[Tournées de véhicules (VRP)]].

## Concepts clés

### Variables, domaines, contraintes

- Une contrainte n'est pas forcément linéaire : « ces six valeurs sont toutes différentes », « ces tâches ne se chevauchent pas », « cette suite de valeurs est un circuit ». Le modèle reste lisible, car il reprend la formulation du métier.
- **Variables d'intervalle** (début, durée, fin) et contraintes de non-chevauchement ou de ressource cumulée : ce qui rend la méthode naturelle pour l'ordonnancement.
- CP-SAT, le solveur d'OR-Tools, **travaille sur les entiers** : un problème à coefficients non entiers se met à l'échelle d'abord (multiplication par un entier assez grand), d'après sa documentation.

### Propagation et recherche

- Le solveur alterne deux opérations. La **propagation** supprime des domaines les valeurs qui ne peuvent figurer dans aucune solution compte tenu des contraintes. La **recherche** choisit une variable, essaie une valeur, propage, et revient en arrière en cas d'échec.
- Exemple de propagation : $x, y \in \{1, 2\}$, $z \in \{1, 2, 3\}$ avec $x, y, z$ tous différents. Décomposée en inégalités deux à deux, la contrainte ne retire **aucune** valeur (calculé ici : les trois domaines restent intacts, chaque valeur a un « support »). Traitée **globalement**, elle voit que $x$ et $y$ occupent à eux deux les valeurs 1 et 2, donc $z = 3$. Le solveur CP-SAT, interrogé ici sur ce modèle, trouve les deux seules solutions $(1,2,3)$ et $(2,1,3)$.
- **Contraintes globales** : des contraintes qui portent sur plusieurs variables avec un algorithme de filtrage dédié. Régin (1994, *AAAI*) donne pour `alldifferent` un algorithme de filtrage fondé sur la théorie des couplages, qui atteint la cohérence d'arc généralisée en temps $O(p^2 d^2)$ (pour $p$ variables de domaine au plus $d$) ; il reste, d'après une synthèse, la référence. Le catalogue des contraintes globales employées par le MiniZinc Challenge compte environ cinquante entrées, dont `all_different` et `cumulative` parmi les plus utilisées (page consultée).

### Le tournant : l'apprentissage de clauses

- Les solveurs à base de SAT apprennent des **clauses** à chaque échec pour ne pas refaire la même erreur. La **génération paresseuse de clauses** (*lazy clause generation*, Ohrimenko, Stuckey et Codish, 2009, *Constraints* 14(3), 357-391) transforme un moteur de propagation en un solveur SAT : chaque propagateur produit à la demande les clauses qui expliquent ses déductions, ce qui donne des **nogoods** forts. Les auteurs rapportent que le système résout beaucoup de problèmes à domaines finis nettement plus vite que d'autres techniques.
- Le descriptif de CP-SAT, soumis au MiniZinc Challenge, présente l'architecture : un solveur SAT à apprentissage de clauses, au-dessus un module de contraintes (booléens, entiers, intervalles), à côté un **simplexe** qui fournit une relaxation linéaire globale (relaxation, coupes, heuristiques, techniques de dualité), et en haut un **portefeuille de travailleurs spécialisés** qui échangent des informations. C'est un mélange de méthodes de CP, de SAT et de MIP.

## Les maths, simplement

- Un problème de satisfaction de contraintes (CSP) est un triplet $(X, D, C)$ : variables $X = \{x_1, \dots, x_n\}$, domaines $D = \{D_1, \dots, D_n\}$, contraintes $C$. Une solution est une affectation $x_i \in D_i$ qui satisfait toute contrainte de $C$.
- **Cohérence d'arc** : pour une contrainte entre $x$ et $y$, une valeur de $D_x$ est conservée seulement si elle a un **support** dans $D_y$. La cohérence d'arc généralisée étend cette idée aux contraintes sur plus de deux variables, comme `alldifferent`.
- Trois exemples mesurés ici (OR-Tools 9.15) pour donner l'échelle :

| Problème | Modèle | Résultat |
|---|---|---|
| SEND + MORE = MONEY (chiffres tous différents, 8 lettres) | une contrainte `AllDifferent`, une équation linéaire | **1 solution**, $S{=}9,E{=}5,N{=}6,D{=}7,M{=}1,O{=}0,R{=}8,Y{=}2$ ; 0 conflit, 0 branche mesurés (aucune recherche n'a été nécessaire) |
| 8 reines | trois `AllDifferent` (lignes, deux diagonales) | **92 solutions**, énumérées en 0,04 s |
| Job-shop de la doc d'OR-Tools (3 ordres, 3 machines) | intervalles, `NoOverlap`, précédences | optimum **11** prouvé, voir [[Ordonnancement d'atelier (job-shop, flow-shop)]] |

- Modèle des 8 reines :

```python
from ortools.sat.python import cp_model
m = cp_model.CpModel(); n = 8
q = [m.NewIntVar(0, n - 1, f"q{i}") for i in range(n)]      # q[i] : colonne de la reine de la ligne i
m.AddAllDifferent(q)                                          # une par colonne
m.AddAllDifferent([q[i] + i for i in range(n)])               # une par diagonale montante
m.AddAllDifferent([q[i] - i for i in range(n)])               # une par diagonale descendante
```

## En pratique

- **Quand la CP gagne** : le problème est **riche en contraintes combinatoires** (ordre, exclusion, cardinalité, ressources, successions de postes) et l'objectif secondaire. Ordonnancement et plannings de personnel sont les terrains habituels. Le Handbook of Constraint Programming (Rossi, van Beek, Walsh, Elsevier, 2006) cite comme domaines d'application réussis l'ordonnancement, la planification, les tournées de véhicules, la configuration, les réseaux et la bio-informatique.
- **Quand le MIP gagne** : objectif linéaire, contraintes linéaires, grandes tailles ; la relaxation linéaire apporte une borne que la CP seule n'a pas. Google conseille d'ailleurs, pour un problème à objectif et contraintes linéaires, de considérer son solveur linéaire (MPSolver) plutôt que CP-SAT. CP-SAT embarque une relaxation linéaire, ce qui brouille la frontière : l'essayer sur les deux formulations est plus fiable que de choisir à l'avance. Voir [[Programmation linéaire en nombres entiers (MIP)]].
- **Solveurs** : CP-SAT (OR-Tools, libre) a gagné les catégories « Fixed », « Free », « Parallel » et « Open » du MiniZinc Challenge 2026 ; la catégorie « Local Search » est allée à un autre solveur (résultats consultés ; 34 solveurs, 24 problèmes). Les autres médaillés de 2026 sont Pumpkin, PicatSAT, Choco-solver, Parasol, CUFE, QiuQi-MIXSolver et Yuck ; leur licence n'a pas été vérifiée ici. Le brain n'a pas encore de page de brique pour ces solveurs ; ils sont cités en texte simple.
- **MiniZinc** est un langage de modélisation indépendant du solveur : on écrit le modèle une fois et on l'essaie sur plusieurs solveurs.
- **Entiers seulement** : les durées et les coûts se mettent à l'échelle (centimes plutôt qu'euros, minutes plutôt qu'heures), comme le demande la documentation de CP-SAT.
- **Lire la borne** : un solveur qui minimise renvoie la meilleure solution trouvée et une borne inférieure ; l'écart entre les deux dit s'il reste à chercher ou à prouver.

## Approches voisines & alternatives

- [[Programmation linéaire en nombres entiers (MIP)]] — l'autre grande famille exacte : relaxation linéaire et coupes, plutôt que propagation et apprentissage de clauses.
- [[Optimisation combinatoire]] — le cadre des problèmes que la CP résout (affectation, couverture, séquencement).
- [[Optimisation sous contrainte]] — contraintes continues et dualité, sans domaines finis.
- [[Ordonnancement d'atelier (job-shop, flow-shop)]] — le terrain d'élection des variables d'intervalle.
- [[Plannings de personnel (rostering)]] — contraintes de cardinalité et de succession de postes.
- [[Tournées de véhicules (VRP)]] — contraintes de capacité et de fenêtres, souvent traitées par des heuristiques dédiées.
- [[PuLP]] — modeleur LP/MIP (alternative quand le modèle est linéaire).
- [[OR-Tools]] — le solveur CP-SAT, la brique libre qui met cette approche en œuvre.

## Pour aller plus loin

- Rossi, van Beek, Walsh (dir.) (2006), *Handbook of Constraint Programming*, Elsevier, Foundations of Artificial Intelligence : <https://shop.elsevier.com/books/handbook-of-constraint-programming/rossi/978-0-444-52726-4> (notice lue, ouvrage non lu)
- Régin (1994), *A Filtering Algorithm for Constraints of Difference in CSPs*, AAAI : <https://www.dcs.gla.ac.uk/~pat/cpM/papers/allDiff/ReginAAAI-1994.pdf> (résumé relevé par un moteur de recherche) ; synthèse : *The alldifferent Constraint: A Survey* <https://arxiv.org/abs/cs/0105015>
- Ohrimenko, Stuckey, Codish (2009), *Propagation via lazy clause generation*, Constraints 14(3), 357-391 : <https://doi.org/10.1007/978-3-642-04244-7_29> (résumé lu)
- Documentation OR-Tools, *Constraint Optimization* : <https://developers.google.com/optimization/cp> et *CP-SAT Solver* : <https://developers.google.com/optimization/cp/cp_solver> (pages lues)
- Descriptif de CP-SAT au MiniZinc Challenge 2026 : <https://www.minizinc.org/challenge/2026/description_or-tools_cp-sat.txt> (lu)
- MiniZinc Challenge, résultats 2026 : <https://minizinc.org/challenge/2026/results> ; catalogue des contraintes globales : <https://www.minizinc.org/challenge/globals/> (pages lues)
- Connexions brain : [[Programmation linéaire en nombres entiers (MIP)]], [[Optimisation combinatoire]], [[Ordonnancement d'atelier (job-shop, flow-shop)]], [[Plannings de personnel (rostering)]], [[Tournées de véhicules (VRP)]].
