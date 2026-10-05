---
role: brique
nom: HGS-CVRP
alias: [HGS CVRP, Hybrid Genetic Search CVRP, HGS, PyHygese, SWAP*]
pitch: "Implémentation C++ de référence de la recherche génétique hybride pour le problème de tournées avec capacités (CVRP) et son voisinage SWAP*, en exécutable et en interface C, pensée pour des instances jusqu'à environ 1 000 clients ; MIT."
categorie: math/optimisation
famille: cli
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[PyVRP]]"]
complements: []
tags: [vehicle-routing, logistics, combinatorial-optimization]
url_docs: https://github.com/vidalt/HGS-CVRP
url_repo: https://github.com/vidalt/HGS-CVRP
---

# HGS-CVRP

<!-- AUTO:BANDEAU:START -->
> Implémentation C++ de référence de la recherche génétique hybride pour le problème de tournées avec capacités (CVRP) et son voisinage SWAP*, en exécutable et en interface C, pensée pour des instances jusqu'à environ 1 000 clients ; MIT.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI C++ | open-source | en ligne de commande, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Implémentation de **la recherche génétique hybride** (HGS) avec contrôle avancé de la diversité, de Vidal et
al. (2012), **spécialisée dans le CVRP** : tournées de véhicules avec capacités, au départ d'un dépôt. Elle est
écrite pour être transparente, ciblée et concise : le README dit n'avoir gardé que les éléments qui font le
succès de la méthode. Elle ajoute un voisinage, **SWAP\***, qui échange deux clients entre routes différentes
sans les insérer à la place l'un de l'autre. Le dépôt est celui du chercheur qui l'a conçue, Thibaut Vidal ; il
sert de référence aux travaux académiques et aux comparaisons de méthodes.

Le programme se compile avec CMake et produit un exécutable `hgs` qui lit une instance au format `.vrp`, tourne
jusqu'à une limite de temps ou d'itérations sans amélioration, et écrit une solution. Il traite aussi les
distances asymétriques et une limite de durée. Le dépôt livre une interface C ; des *wrappers* Python
(PyHygese) et Julia (Hygese.jl), maintenus à part, appellent la dernière version.

Le README fixe un périmètre : calibré pour des instances **de taille moyenne, jusqu'à 1 000 clients**, et pas
pour plus de 5 000, qui demandent d'autres stratégies (décomposition, voisinages limités).

Relevé le 2026-10-05 : dernière version **v2.0.0** du 2022-05-09 ; v1.0.0 correspond aux résultats de l'article
de Vidal (2022, *Computers & Operations Research* 140) ; dernier push du 2025-03-26 (changements CMake pour
l'importer depuis d'autres projets) ; dépôt non archivé ; licence MIT lue dans `LICENSE`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un CVRP canonique à résoudre vite, avec une heuristique de référence solide sur 100 à 1 000 clients | Des fenêtres de temps, plusieurs dépôts, une flotte hétérogène ou des collectes-livraisons : [[PyVRP]] les prend en charge, HGS-CVRP non |
| Reproduire ou comparer à une méthode publiée : le dépôt et l'article sont la référence citée | Un modèle écrit en Python, sans compilation : [[PyVRP]] s'installe par `pip` |
| Embarquer un solveur C++ dans une application, par l'interface C | Plus de 5 000 clients : le README le déclare hors périmètre |
| Étudier l'algorithme : le README le décrit comme concis | Un problème d'ordonnancement ou de contraintes riches : [[OR-Tools]] |

## Mise en œuvre

- Installation — `git clone https://github.com/vidalt/HGS-CVRP`, puis `cmake .. -DCMAKE_BUILD_TYPE=Release` et `make bin` dans un dossier `build` ; CMake est requis
- Point d'entrée — `./hgs instance.vrp solution.sol -seed 1 -t 30` ; options `-it` (itérations sans amélioration, 20 000 par défaut), `-t` (limite de temps en secondes), `-seed`, `-veh` (taille de flotte imposée), `-round` (arrondi des distances, activé par défaut)
- Prérequis — un compilateur C++ et CMake ; pour Python, le paquet `hygese` (PyHygese), version 0.1.0 sur PyPI en 2026-05
- Exécution — un processus local, sans service ; `-seed` fixe le hasard
- Coût — gratuit, MIT ; le README invite à contacter l'auteur pour les cas hors périmètre

## Limites à connaître

- **Le CVRP et rien d'autre.** Le périmètre est le problème canonique, plus les distances asymétriques et la durée : aucune fenêtre de temps dans le dépôt.
- **Les distances sont arrondies par défaut.** L'option `-round` vaut 1, qui arrondit les distances à l'entier le plus proche : sur des coordonnées réelles, à désactiver (`-round 0`) ou à mettre à l'échelle avant de comparer des coûts.
- **Peu d'activité.** Dernière version en 2022 et dernier push en 2025-03 : un dépôt de référence et de recherche, pas un produit suivi. La fiche de [[PyVRP]] décrit un projet plus actif et plus large.
- **Citer la version.** Le README recommande de nommer la version de GitHub employée, car le code évolue.

## Écosystème

### Alternatives

- [[PyVRP]] — Solveur de tournées de véhicules en Python à cœur C++ : capacités, fenêtres de temps, flotte hétérogène, multi-dépôts, collectes-livraisons, clients optionnels, recherche locale itérée ; MIT, avec une édition Enterprise payante vendue à part. — le paquet Python, plus large en variantes, dont le code reprend celui de HGS-CVRP.

### Compléments

Aucun complément déclaré.

## Ressources

- Dépôt — https://github.com/vidalt/HGS-CVRP
- Article — Vidal (2022), *Hybrid Genetic Search for the CVRP: Open-Source Implementation and SWAP\* Neighborhood*, arXiv 2012.10384 : https://arxiv.org/abs/2012.10384
- Article — Vidal, Crainic, Gendreau, Lahrichi, Rei (2012), Operations Research 60(3), 611-624 : https://doi.org/10.1287/opre.1120.1048
- Dépôt — https://github.com/chkwon/PyHygese (le *wrapper* Python)

## Voir aussi

- [[Optimisation]] — le hub du dossier
- [[Tournées de véhicules (VRP)]] — la notion : le problème, ses variantes et ses instances de référence
- [[Optimisation combinatoire]] — la classe de problèmes
- [[Comparatif - Solveurs d'optimisation]] — la vue du dossier
