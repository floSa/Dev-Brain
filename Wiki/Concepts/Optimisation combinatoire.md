---
galaxie: wiki
type: concept
nom: Optimisation combinatoire
alias: [Combinatorial optimization, Sac à dos, Knapsack, Problème d'affectation, Assignment problem, Set cover, Couverture d'ensemble, Voyageur de commerce, TSP]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [optimization, combinatorial-optimization, dynamic-programming]
---

# Optimisation combinatoire

## Aperçu

- Cherche la **meilleure configuration dans un ensemble discret et fini** (sous-ensembles, permutations, affectations) : l'espace des solutions est énorme mais énumérable.
- Beaucoup de ces problèmes sont **NP-difficiles** — pas d'algorithme exact polynomial connu → on combine formulations exactes ([[Programmation linéaire en nombres entiers (MIP)|MIP]]), structures spéciales et heuristiques.

## Concepts clés

### Sac à dos (knapsack)
- Choisir un sous-ensemble d'objets (valeur, poids) maximisant la valeur sous une capacité. NP-difficile, mais résolu **exactement** par programmation dynamique en $O(nW)$ (pseudo-polynomial).

### Affectation (assignment)
- Affecter $n$ agents à $n$ tâches au coût total minimal. Cas **facile** : l'algorithme **hongrois** le résout en $O(n^3)$ — la matrice de contraintes est totalement unimodulaire, donc la relaxation LP donne directement une solution entière.

### Couverture (set cover)
- Couvrir un univers d'éléments avec le moins de sous-ensembles possible. NP-difficile ; l'**heuristique gloutonne** garantit un facteur $\ln n$ de l'optimum (borne serrée).

## Les maths, simplement

- Structure décisive : l'**unimodularité totale**. Si la matrice des contraintes est TU, la relaxation LP a des sommets entiers → le problème est en réalité « facile » (affectation, flots, plus court chemin).
- Sinon, le **gap d'intégralité** mesure la difficulté, et l'**approximabilité** classe les problèmes (facteur garanti d'une heuristique vs inapproximable).

## En pratique

- Modéliser en [[Programmation linéaire en nombres entiers (MIP)|MIP]] puis confier à un solveur est souvent le chemin le plus court vers une solution exacte.
- Grandes instances : heuristiques (glouton), métaheuristiques (recuit simulé, tabou, algorithmes génétiques), ou solveurs spécialisés (OR-Tools pour routage/affectation).
- Identifier la structure d'abord : un problème d'affectation ou de flot a un algorithme polynomial dédié — inutile de sortir un MIP générique.

## Approches voisines & alternatives

- [[Programmation linéaire en nombres entiers (MIP)]] — l'outil exact de référence pour formuler et résoudre ces problèmes.
- [[Convexity]] — ces problèmes sont non convexes par nature (domaine discret) ; d'où leur difficulté.
- [[Optimisation sous contrainte]] — le pendant continu ; ici les variables sont discrètes.
- Programmation dynamique — résout exactement les cas à sous-structure optimale (sac à dos, plus court chemin).

## Pour aller plus loin

- Papadimitriou & Steiglitz — *Combinatorial Optimization: Algorithms and Complexity*.
- Korte & Vygen — *Combinatorial Optimization: Theory and Algorithms*.
