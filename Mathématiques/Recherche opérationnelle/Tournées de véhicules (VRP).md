---
role: notion
nom: Tournées de véhicules (VRP)
alias: [VRP, vehicle routing problem, CVRP, capacitated vehicle routing problem, VRPTW, VRP with time windows, tournées, optimisation de tournées, problème de tournées, route optimization, savings, algorithme des économies, Clarke et Wright, voyageur de commerce, TSP]
categorie: math/recherche-operationnelle
domaines: [data-sci, ml-eng]
tags: [vehicle-routing, logistics, combinatorial-optimization]
---

# Tournées de véhicules (VRP)

## Aperçu

- Une flotte de véhicules part d'un **dépôt**, des **clients** à servir, une demande par client, une capacité par véhicule : décider **quels clients vont dans quelle tournée et dans quel ordre**, pour minimiser la distance ou le coût total.
- Le problème est posé par Dantzig et Ramser (1959, *Management Science* 6(1), 80-91) : une flotte de camions-citernes entre un dépôt et un grand nombre de stations-service, la demande de chaque station étant donnée ; il s'agit d'affecter les stations aux camions de façon à satisfaire les demandes avec un kilométrage minimal. Leur méthode, fondée sur une formulation linéaire, donne une solution proche de l'optimum, et l'article indique qu'aucune application pratique n'avait encore été faite.
- Il contient le **voyageur de commerce** comme cas particulier (un seul véhicule de capacité infinie) : il est donc NP-difficile, voir [[Optimisation combinatoire]]. Pour les tailles réelles, on vise une bonne solution et une mesure de l'écart, pas une preuve d'optimalité.
- Aval d'un plan de production ou de distribution : [[S&OP et plan directeur de production]] fixe ce qui part et quand ; ici, **comment le transporter**. La tournée est aussi la décision qui se cache derrière une revue périodique avec tournée de camion, voir [[Politiques de réapprovisionnement (s,S) et (R,Q)]].

## Concepts clés

### Les variantes à connaître

- **CVRP** (capacité) : chaque véhicule a une capacité, la somme des demandes d'une tournée ne la dépasse pas. C'est le problème de base.
- **VRPTW** (fenêtres de temps) : chaque client doit être servi dans un intervalle. Solomon (1987, *Operations Research* 35(2), 254-265) étudie des heuristiques pour ce cas et conclut, sur un large jeu d'instances (types de données, part de clients à fenêtre, serrage et placement des fenêtres, horizon), qu'**une heuristique d'insertion donne régulièrement de très bons résultats** ; il fournit ainsi un jeu d'instances de référence.
- **Collecte et livraison** (VRPPD), **retours** (VRPB), **dépôts multiples** (MDVRP), **tournées ouvertes** (OVRP, le véhicule ne revient pas), **véhicules électriques** (EVRP, contraintes de batterie), **tournées à profits** : la liste des variantes relevée sur la page Wikipédia (secondaire).
- Les contraintes d'usage : flotte hétérogène, temps de service, pauses réglementaires, compatibilité client-véhicule, plusieurs voyages par véhicule. PyVRP en liste plusieurs dans son README.

### Trois familles de méthodes

- **Heuristiques de construction** : bâtir des tournées par une règle gloutonne. La plus connue est l'algorithme des **économies** de Clarke et Wright (1964, *Operations Research* 12(4), 568-581) : partir d'une tournée par client, puis fusionner les paires de tournées qui économisent le plus de distance par rapport à deux allers-retours séparés. Rapide, sans garantie.
- **Métaheuristiques** : améliorer une solution par recherche locale et recombinaison. La **recherche génétique hybride** (HGS) est une métaheuristique de référence du CVRP. Vidal publie une implémentation libre pour le CVRP (arXiv 2012.10384, dépôt `vidalt/HGS-CVRP`, licence MIT, C++), avec le voisinage **SWAP\*** (échanger deux clients entre tournées sans réinsertion à l'endroit même). PyVRP (Wouda, Lan, Kool, *INFORMS Journal on Computing* 36(4), 943-955, 2024 ; dépôt `PyVRP/PyVRP`, licence MIT) reprend HGS dans un paquet Python avec noyau C++, conçu pour le VRPTW et extensible à d'autres variantes ; l'article annonce des résultats à l'état de l'art sur le VRPTW et le CVRP (affirmation du résumé, non vérifiée ici).
- **Méthodes exactes** : formulations en nombres entiers résolues par coupes ou par génération de colonnes (*branch-and-cut*, *branch-and-price*, partition d'ensembles de tournées). Hors de portée des grandes instances, utiles pour mesurer l'écart des heuristiques sur les petites. Voir [[Programmation linéaire en nombres entiers (MIP)]].

## Les maths, simplement

- Formulation de **flot de véhicules** à deux indices (Toth et Vigo, 2002, relevée dans la synthèse Wikipédia) : une variable binaire $x_{ij}$ par arc, exactement un arc entrant et un arc sortant par client, conservation des véhicules au dépôt, et des **inégalités de capacité** qui interdisent les sous-tournées déconnectées du dépôt et les tournées trop chargées. La forme usuelle pour un sous-ensemble $S$ de clients, de demande totale $q(S)$, est
  $$\sum_{i,j \in S} x_{ij} \le |S| - \left\lceil \frac{q(S)}{Q} \right\rceil.$$
  Il y en a un nombre exponentiel ; on ne les écrit pas toutes, on les ajoute à la demande (coupes). Cette forme est la forme standard, rappelée sans source primaire lue : la synthèse consultée ne donne pas l'expression.
- **Borne sur le nombre de véhicules** : au moins $\lceil \sum_i q_i / Q \rceil$, un bin-packing relâché.
- **Économies de Clarke et Wright** : $s_{ij} = d_{0i} + d_{0j} - d_{ij}$, la distance gagnée en servant $j$ juste après $i$ au lieu de repasser par le dépôt 0. On trie les économies décroissantes et on fusionne les tournées quand $i$ et $j$ sont aux extrémités de deux tournées distinctes et que la capacité tient.
- Expérience calculée ici, **sur des instances aléatoires uniformes de 8 clients** (60 instances, capacité 15, demandes de 2 à 8, dépôt au centre), l'optimum étant obtenu par programmation dynamique sur les sous-ensembles :
  - l'algorithme des économies trouve l'**optimum sur 40 instances sur 60** ;
  - écart moyen à l'optimum : **1,29 %**, écart maximal **9,63 %**.
  Lecture : un algorithme de 1964 est déjà bon sur de petites instances, mais l'écart maximal montre que l'absence de garantie n'est pas théorique. Ces instances sont **aléatoires et petites** : elles ne disent rien de l'écart sur 100 à 1 000 clients ni sur de vraies données.
- Instance de 9 clients (graine 3, demande totale 53, capacité 15, donc au moins 4 véhicules) : optimum et économies donnent le même coût, **401,8**, en 4 tournées.

## En pratique

- **Distances** : une matrice de distances (ou de temps) entre tous les points est l'entrée. Dans une zone réelle, elle vient d'un moteur de routage sur le réseau routier, pas de la distance à vol d'oiseau. Le temps de trajet varie avec l'heure ; les modèles de base le prennent constant.
- **Benchmarks** : Uchoa, Pecin, Pessoa, Poggi, Vidal et Subramanian (2017, *European Journal of Operational Research* 257(3), 845-858) reprochent aux jeux existants d'être **trop faciles**, trop artificiels ou trop homogènes, et proposent **100 instances de 100 à 1 000 clients**, et un jeu étendu de 600 instances, pour discriminer les algorithmes et analyser l'effet des caractéristiques d'instance. Le dépôt HGS-CVRP les emploie pour ses résultats (README) ; les instances de Solomon (1987) jouent ce rôle pour le VRPTW.
- **Choisir un outil** : pour un besoin standard (flotte, capacité, fenêtres de temps, pauses), un paquet de HGS (PyVRP, licence MIT) évite d'écrire une heuristique ; OR-Tools propose aussi un module de routage (TSP, VRP, capacités, fenêtres de temps, visites abandonnées avec pénalité, d'après sa documentation). Aucune page de brique n'existe encore dans le brain pour ces outils : ils sont cités en texte simple.
- **Le coût n'est pas que la distance.** Nombre de véhicules (coût fixe), heures supplémentaires, respect des fenêtres, équilibre de charge entre chauffeurs : l'objectif se choisit avant l'algorithme, et chaque terme demande une unité commune (euro).
- **Statique contre dynamique** : le modèle suppose que les clients et les demandes sont connus avant le départ. Quand de nouveaux clients arrivent en cours de journée, on recalcule sur un horizon glissant, ce qui rapproche le problème de [[Ordonnancement d'atelier (job-shop, flow-shop)]] à horizon glissant.
- **Demande incertaine** : si la demande d'un client est connue seulement par une loi, une tournée peut dépasser la capacité en cours de route. Le modèle de base est déterministe ; le traitement stochastique est un autre sujet.
- **Le calcul de besoin en stock amont** (combien livrer à chaque client) est une autre décision : voir [[Stock de sécurité et taux de service]] et [[Quantité économique de commande et tailles de lot]].

## Approches voisines & alternatives

- [[Optimisation combinatoire]] — le cadre et le voyageur de commerce, cas particulier du VRP.
- [[Programmation linéaire en nombres entiers (MIP)]] — formulations exactes (flot de véhicules, partition d'ensembles) et bornes.
- [[Programmation par contraintes]] — modélisation des fenêtres de temps, des capacités et de contraintes annexes de tournée par des contraintes globales.
- [[Ordonnancement d'atelier (job-shop, flow-shop)]] — le même type de décision (séquence sous contraintes de temps) appliqué à des machines.
- [[Plannings de personnel (rostering)]] — l'affectation des chauffeurs, qui s'ajoute à celle des tournées.
- [[Politiques de réapprovisionnement (s,S) et (R,Q)]] — la revue périodique avec tournée de camion, vue du côté du stock.
- [[Optimisation sous contrainte]] — les multiplicateurs de Lagrange derrière les bornes de relaxation lagrangienne.
- [[PyVRP]] et [[HGS-CVRP]] — les deux implémentations libres de la recherche génétique hybride pour les tournées.
- [[OR-Tools]] — le routage et CP-SAT, en généraliste.

## Pour aller plus loin

- Dantzig, Ramser (1959), *The Truck Dispatching Problem*, Management Science 6(1), 80-91 : <https://ideas.repec.org/a/inm/ormnsc/v6y1959i1p80-91.html> (résumé lu)
- Clarke, Wright (1964), *Scheduling of Vehicles from a Central Depot to a Number of Delivery Points*, Operations Research 12(4), 568-581 : <https://ideas.repec.org/a/inm/oropre/v12y1964i4p568-581.html> (notice lue)
- Solomon (1987), *Algorithms for the Vehicle Routing and Scheduling Problems with Time Window Constraints*, Operations Research 35(2), 254-265 : <https://ideas.repec.org/a/inm/oropre/v35y1987i2p254-265.html> (résumé lu)
- Uchoa et al. (2017), *New Benchmark Instances for the Capacitated Vehicle Routing Problem*, European Journal of Operational Research 257(3), 845-858 : <https://optimization-online.org/2014/10/4597/> (résumé lu)
- Vidal, *Hybrid Genetic Search for the CVRP: Open-Source Implementation and SWAP\* Neighborhood*, arXiv 2012.10384 : <https://arxiv.org/abs/2012.10384> (résumé lu) ; dépôt : <https://github.com/vidalt/HGS-CVRP> (licence MIT lue)
- Wouda, Lan, Kool (2024), *PyVRP: a high-performance VRP solver package*, INFORMS Journal on Computing 36(4), 943-955 : <https://arxiv.org/abs/2403.13795> (résumé lu) ; dépôt : <https://github.com/PyVRP/PyVRP> (licence MIT lue)
- Wikipédia, *Vehicle routing problem* : <https://en.wikipedia.org/wiki/Vehicle_routing_problem> (synthèse secondaire : variantes, formulations)
- Connexions brain : [[Optimisation combinatoire]], [[Programmation linéaire en nombres entiers (MIP)]], [[Programmation par contraintes]], [[Ordonnancement d'atelier (job-shop, flow-shop)]], [[Plannings de personnel (rostering)]].
