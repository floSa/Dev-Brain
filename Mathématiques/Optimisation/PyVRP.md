---
role: brique
nom: PyVRP
alias: [pyvrp, Python VRP solver, PyVRP VRP solver]
pitch: "Solveur de tournées de véhicules en Python à cœur C++ : capacités, fenêtres de temps, flotte hétérogène, multi-dépôts, collectes-livraisons, clients optionnels, recherche locale itérée ; MIT, avec une édition Enterprise payante vendue à part."
categorie: math/optimisation
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[OR-Tools]]", "[[HGS-CVRP]]"]
complements: []
tags: [vehicle-routing, logistics, combinatorial-optimization]
url_docs: https://pyvrp.org/
url_repo: https://github.com/PyVRP/PyVRP
---

# PyVRP

<!-- AUTO:BANDEAU:START -->
> Solveur de tournées de véhicules en Python à cœur C++ : capacités, fenêtres de temps, flotte hétérogène, multi-dépôts, collectes-livraisons, clients optionnels, recherche locale itérée ; MIT, avec une édition Enterprise payante vendue à part.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Solveur de **tournées de véhicules** (VRP) développé par Applied Routing, installable par `pip install pyvrp`.
Les composants critiques sont en C++, l'interface de modélisation est en Python. Le README énumère les variantes
prises en charge : capacités avec collectes et livraisons, flotte aux véhicules de capacités, de coûts et de
durées de poste différents, **fenêtres de temps** et délais de mise à disposition, plusieurs dépôts, rechargements
en cours de route, clients optionnels avec un gain de visite, groupes de clients imposant des restrictions
conjointes.

L'algorithme est une **recherche locale itérée** (ILS), dont le code reprend celui de la recherche génétique
hybride ([[HGS-CVRP]]), comme le disent les mentions de sa licence ; la documentation de développement la décrit. Le point d'entrée est un objet `Model` : on
ajoute lieux, dépôts, clients, types de véhicules et arêtes, puis on appelle `solve` avec un critère d'arrêt. Une
solution de départ, même infaisable, peut être fournie (`initial_solution`) pour repartir d'un plan existant.

**Édition payante.** Le README signale **PyVRP Enterprise**, une version étendue vendue par Applied Routing :
planification automatique des pauses (heures de conduite UE et US), contraintes d'équité, compatibilités
véhicule-client et séquencement, regroupement géographique. Le dépôt MIT ne les contient pas ; il est complet
pour les variantes ci-dessus.

Relevé le 2026-10-05 : **v0.14.0** du 2026-08-20 (PyPI, classé *Production/Stable*, Python 3.11 et plus),
dépôt actif (push du 2026-09-30), licence MIT lue dans `LICENSE.md` (copyrights de Thibaut Vidal pour
HGS-CVRP, d'ORTEC pour HGS-DIMACS et des contributeurs de PyVRP).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des tournées avec capacités, fenêtres de temps, flotte hétérogène ou multi-dépôts, sans écrire d'heuristique ([[Tournées de véhicules (VRP)]]) | Un besoin de pauses réglementaires, d'équité entre chauffeurs ou de compatibilités véhicule-client : ce sont les fonctions de l'édition Enterprise, payante |
| Plusieurs milliers de visites : PyVRP annonce que son échelle le permet, d'après sa propre comparaison | Des temps de trajet qui varient avec l'heure : la comparaison publiée par le projet indique que la fonction n'est pas prise en charge |
| Une interface Python haut niveau (`Model`) plutôt que de bâtir les contraintes à la main | Un problème de planning ou d'ordonnancement, pas de tournées : [[OR-Tools]] (CP-SAT) |
| Reprendre un plan existant comme solution de départ | Seulement le CVRP canonique, à étudier ou à reproduire : [[HGS-CVRP]], l'implémentation de référence |

## Mise en œuvre

- Installation — `uv add pyvrp`
- Point d'entrée — `from pyvrp import Model` ; `m.add_location(x=, y=)` puis `m.add_depot(location)`, `m.add_client(location, delivery=...)`, `m.add_vehicle_type(n, capacity=..., start_depot=..., end_depot=...)`, `m.add_edge(frm, to, distance=..., duration=...)`, et `m.solve(stop=MaxRuntime(secondes))` (`from pyvrp.stop import MaxRuntime`)
- Prérequis — Python 3.11 minimum ; **distances, durées, charges et fenêtres sont des entiers** dans la signature de l'API (0.14.0) : mettre les mètres, les secondes, les centimes à l'échelle et arrondir avant de les poser ; une matrice de trajets réels vient d'un moteur de routage
- Exécution — dans le process appelant ; `seed` rend le calcul reproductible ; la compilation sous Windows n'est pas prise en charge par les développeurs, qui renvoient vers WSL
- Coût — gratuit, MIT ; l'édition Enterprise est vendue par Applied Routing

## Limites à connaître

- **Des comparaisons à lire avec recul.** La page « Why choose PyVRP? » compare le projet à VROOM, jsprit et OR-Tools ; elle est écrite par ses développeurs. Elle classe PyVRP en tête sur l'échelle et la qualité de solution, et en retrait sur l'activité du projet et la facilité de modification.
- **Trajets constants.** Les durées de trajet dépendant de l'heure sont marquées « non prises en charge » dans la comparaison du projet ; le modèle suppose les clients et les demandes connus avant le départ.
- **Étendre exige du C++.** Les composants critiques sont en C++ : changer le comportement demande de lire aussi la littérature des tournées.
- **Un projet encore jeune.** La communauté est plus petite que celle d'OR-Tools, d'après la documentation du projet.

## Écosystème

### Alternatives

- [[OR-Tools]] — Suite C++ de Google pour l'optimisation combinatoire, utilisable depuis Python : solveur CP-SAT (contraintes sur entiers, recherche parallèle), solveurs LP (Glop, PDLP), enveloppes MIP vers des solveurs tiers, bibliothèque de tournées et algorithmes de graphes ; Apache-2.0. — la suite généraliste dont le module de routage demande d'écrire les contraintes soi-même.
- [[HGS-CVRP]] — Implémentation C++ de référence de la recherche génétique hybride pour le problème de tournées avec capacités (CVRP) et son voisinage SWAP*, en exécutable et en interface C, pensée pour des instances jusqu'à environ 1 000 clients ; MIT. — l'algorithme dont PyVRP s'inspire, limité au CVRP canonique.
- voisin : **VROOM** et **jsprit** — solveurs de tournées libres que la documentation de PyVRP compare à lui ; sans fiche dans le brain.

### Compléments

Aucun complément déclaré.

## Ressources

- Documentation — https://pyvrp.org/
- Dépôt — https://github.com/PyVRP/PyVRP
- Article — Wouda, Lan, Kool (2024), *PyVRP: a high-performance VRP solver package*, INFORMS Journal on Computing 36(4) : https://arxiv.org/abs/2403.13795

## Voir aussi

- [[Optimisation]] — le hub du dossier
- [[Tournées de véhicules (VRP)]] — la notion : variantes, méthodes, instances de référence
- [[Optimisation combinatoire]] — la classe de problèmes
- [[Comparatif - Solveurs d'optimisation]] — la vue du dossier
