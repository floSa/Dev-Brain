---
role: notion
nom: Ordonnancement d'atelier (job-shop, flow-shop)
alias: [job-shop, jobshop, job shop scheduling, flow-shop, flowshop, flow shop scheduling, open-shop, ordonnancement, ordonnancement d'atelier, makespan, durée totale, règle de Johnson, Johnson's rule, règles de priorité, dispatching rules, flexible job shop]
categorie: math/recherche-operationnelle
domaines: [data-sci, ml-eng]
tags: [scheduling, combinatorial-optimization, constraint-programming]
---

# Ordonnancement d'atelier (job-shop, flow-shop)

## Aperçu

- Des **tâches** à placer sur des **machines**, dans le temps : décider, pour chaque tâche, sur quelle machine elle passe et à quel instant, sans qu'une machine fasse deux tâches à la fois ni qu'une tâche soit commencée avant la fin de la précédente du même ordre de fabrication.
- Deux formes de référence. Le **flow-shop** : tous les ordres de fabrication passent par les mêmes machines **dans le même ordre**, la décision est l'ordre des ordres. Le **job-shop** : chaque ordre de fabrication a **sa propre gamme** (suite de machines), la décision est l'ordre des tâches sur chaque machine. L'**open-shop** laisse en plus libre l'ordre des machines d'un ordre.
- Le critère le plus étudié est la **durée totale** (*makespan*, notée $C_{\max}$) : l'instant où la dernière tâche finit. Les retards à des dates dues, la somme des temps de séjour et les coûts de changement de série sont d'autres critères, souvent plus proches du besoin réel.
- La question se pose après les quantités : [[S&OP et plan directeur de production]] et [[MRP et calcul des besoins]] fixent combien et pour quand ; ici, **dans quel ordre, sur quelle machine, à quelle heure**.

## Concepts clés

### Notation et familles de problèmes

- La littérature décrit un problème par trois champs $\alpha \mid \beta \mid \gamma$ : l'environnement machine, les contraintes de tâche, le critère. $F2 \mid\mid C_{\max}$ est le flow-shop à deux machines à minimiser en durée totale ; $J \mid\mid C_{\max}$ le job-shop. La notation est popularisée par Graham, Lawler, Lenstra et Rinnooy Kan (1979, *Annals of Discrete Mathematics* 5, 287-326) ; l'article n'a pas été lu, l'attribution vient de pages secondaires.
- **Flow-shop de permutation** : le même ordre d'ordres de fabrication sur toutes les machines. C'est le sous-cas que traite la plupart des travaux sur le flow-shop, et celui des instances de Taillard.
- **Flexible job-shop** : chaque tâche peut aller sur plusieurs machines. Le problème gagne un choix d'affectation ; il se modélise comme le job-shop, avec des intervalles optionnels.
- **Contraintes réelles** que le modèle de base écarte : temps de réglage dépendant de la séquence (le voyageur de commerce en est un cas particulier, ce qui rend ce cas encore plus difficile d'après la synthèse de Wikipédia), dates de disponibilité, dates dues, pannes, fenêtres de maintenance (voir [[Politique de maintenance et coût]]), opérateurs partagés.

### Ce qui se résout vite, ce qui ne se résout pas

- **Flow-shop à deux machines, durée totale** : polynomial. La **règle de Johnson** (1954, *Naval Research Logistics Quarterly* 1(1), 61-68) donne l'ordre optimal : les ordres dont le temps sur la machine 1 est au plus égal à celui sur la machine 2 d'abord, par temps croissant sur la machine 1 ; puis les autres, par temps décroissant sur la machine 2. Johnson traite aussi un cas restreint à trois machines.
- **Dès trois machines** (flow-shop, durée totale) et pour le **job-shop** : NP-complet. Garey, Johnson et Sethi (1976, *Mathematics of Operations Research* 1(2), 117-129) l'établissent : durée totale en flow-shop NP-complète pour $m \ge 3$ ; temps de séjour moyen en flow-shop NP-complet pour tout $m \ge 2$ ; durée totale en job-shop NP-complète pour tout $m \ge 2$ (énoncé du résumé retrouvé par recherche ; la synthèse de Wikipédia écrit $m > 2$ pour le job-shop, désaccord non tranché ici).
- Conséquence : au-delà de petites tailles, on ne cherche pas une garantie d'optimalité par énumération ; on prend une **règle de priorité**, une **recherche locale**, ou un **solveur de contraintes ou de programmation en nombres entiers**, et on regarde l'écart à une borne inférieure.

### Trois façons de résoudre

- **Règles de priorité** (*dispatching rules*) : à chaque instant où une machine se libère, choisir parmi les tâches prêtes selon une règle (plus court temps d'abord, plus long, plus petite date due…). Immédiat et explicable, **sans garantie**.
- **Formulations exactes** : programmation en nombres entiers avec des grands $M$ pour les disjonctions (« A avant B ou B avant A »), ou **modèle de contraintes** à variables d'intervalle. Les contraintes de précédence, de non-chevauchement par machine et d'objectif se déclarent presque telles quelles : voir [[Programmation par contraintes]] et [[Programmation linéaire en nombres entiers (MIP)]].
- **Recherche locale et métaheuristiques** : partir d'un ordonnancement, échanger des tâches voisines. Hors du périmètre de cette page.

## Les maths, simplement

- Flow-shop de permutation, $p_{k,j}$ le temps du $j$-ième ordre de la séquence sur la machine $k$, $C_{k,j}$ sa fin :
  $$C_{k,j} = \max\bigl(C_{k-1,j},\; C_{k,j-1}\bigr) + p_{k,j}, \qquad C_{k,0}=C_{0,j}=0, \qquad C_{\max} = C_{m,n}.$$
  Chaque ordre attend que la machine précédente l'ait fini **et** que la machine courante soit libre.
- **Borne inférieure élémentaire** du job-shop : le plus grand de la **durée de la plus longue gamme** et de la **charge de la machine la plus chargée**. Aucun ordonnancement ne fait mieux.
- Exemple de flow-shop à deux machines, six ordres de fabrication $(p_1, p_2)$ : A(3,6), B(5,2), C(1,2), D(6,6), E(7,5), F(3,8). Calculé ici : la règle de Johnson donne la séquence C, A, F, D, E, B de durée totale **31** ; l'énumération des 720 séquences confirme que 31 est le minimum, que l'ordre alphabétique donne **35**, et que la pire séquence monte à **40**. Une séquence différente atteint aussi 31 (C, A, B, F, D, E) : l'optimum n'est pas unique.
- Exemple de job-shop (celui de la documentation d'OR-Tools, trois ordres, trois machines ; chaque couple est (machine, durée)) :
  - ordre 0 = [(0,3), (1,2), (2,2)], ordre 1 = [(0,2), (2,1), (1,4)], ordre 2 = [(1,4), (2,3)] ;
  - **bornes** : la plus longue gamme dure 7 ; les charges des machines 0, 1, 2 valent 5, 10 et 6 ; la borne inférieure élémentaire est donc **10** ;
  - **solveur** : CP-SAT (OR-Tools 9.15, mesuré ici) prouve l'optimum à **11** ; la documentation d'OR-Tools donne la même valeur ;
  - **règles de priorité**, simulées ici sans temps mort volontaire (une tâche prête n'attend pas une machine libre) : plus court d'abord **12**, plus long d'abord **14**.
- Lecture : sur trois ordres, la règle simple perd 9 % sur l'optimum et la mauvaise règle 27 %. L'ordre de grandeur varie selon l'instance, ce qui ne se déduit pas d'un exemple de 8 tâches.
- Modèle CP-SAT du job-shop (variables d'intervalle, non-chevauchement, précédence, objectif $C_{\max}$) :

```python
from ortools.sat.python import cp_model
m = cp_model.CpModel(); H = sum(p for job in jobs for _, p in job)
par_machine = {}; fins = []
for job in jobs:
    prec = None
    for mach, p in job:
        s = m.NewIntVar(0, H, ""); e = m.NewIntVar(0, H, "")
        par_machine.setdefault(mach, []).append(m.NewIntervalVar(s, p, e, ""))
        if prec is not None: m.Add(s >= prec)      # la tâche suit la précédente de l'ordre
        prec = e
    fins.append(prec)
for ivs in par_machine.values(): m.AddNoOverlap(ivs)  # une tâche à la fois par machine
mk = m.NewIntVar(0, H, ""); m.AddMaxEquality(mk, fins); m.Minimize(mk)
```

## En pratique

- **Un horaire optimal sur le papier se dégrade au premier aléa** (panne, retard de matière, ordre urgent). Ce qu'on met en production est donc un **ordonnancement qu'on recalcule**, sur un horizon glissant, à partir de l'état de l'atelier (les données remontent par les protocoles décrits dans [[Protocoles de l'atelier - MQTT, OPC UA et Modbus]]).
- **Le critère de durée totale est rarement le critère du métier.** Respect des dates dues, nombre de changements de série, taux d'utilisation du goulot, priorité de clients : se mettre d'accord sur le critère avant de choisir l'algorithme. Une borne inférieure (ci-dessus) permet de dire « à 10 % du minimum possible » sans connaître l'optimum.
- **Benchmarks** : Taillard (1993, *European Journal of Operational Research* 64(2), 278-285) propose **260 problèmes** tirés au hasard, de taille supérieure aux rares exemples publiés (flow-shop de permutation, job-shop, open-shop ; temps fixes, ni réglages ni dates dues ni dates de disponibilité ; critère : durée totale). Les instances servent à comparer des méthodes ; elles ne reproduisent pas un atelier.
- **Choisir l'outil** : la documentation d'OR-Tools modélise le job-shop avec des variables d'intervalle, un non-chevauchement par machine et des précédences, ce qui laisse de la place pour les réglages ou les calendriers. OR-Tools CP-SAT a reçu l'or de la catégorie « Fixed » du MiniZinc Challenge 2026 (page des résultats consultée). Le brain n'a pas encore de page pour ce solveur : cité en texte simple.
- **Entrées de planification** : les durées d'opération sont des **estimations**. Les lois de durée se calent sur l'historique ; une durée sous-estimée de façon systématique rend l'optimum inatteignable, quelle que soit la méthode.
- **Lien avec la maintenance** : une fenêtre d'arrêt programmé est une indisponibilité de machine, donc une contrainte de plus ; les interventions prédictives sont des tâches à insérer, voir [[Politique de maintenance et coût]].

## Approches voisines & alternatives

- [[Programmation par contraintes]] — la façon la plus directe de modéliser le job-shop (intervalles, non-chevauchement, précédence).
- [[Programmation linéaire en nombres entiers (MIP)]] — formulation avec disjonctions ; correcte, souvent moins efficace que les intervalles sur les problèmes d'ordonnancement.
- [[Optimisation combinatoire]] — le cadre : un espace discret de permutations, de la même famille que le voyageur de commerce.
- [[Plannings de personnel (rostering)]] — mêmes outils (contraintes, intervalles) appliqués aux personnes plutôt qu'aux machines.
- [[Tournées de véhicules (VRP)]] — un autre problème de séquencement sous contraintes de capacité et de fenêtres de temps, appliqué aux véhicules.
- [[MRP et calcul des besoins]] — l'amont : les ordres de fabrication que l'ordonnancement place.
- [[S&OP et plan directeur de production]] — l'amont lointain : la capacité et le plan agrégé.
- [[Politique de maintenance et coût]] — les fenêtres de maintenance comme contraintes d'indisponibilité.

## Pour aller plus loin

- Johnson (1954), *Optimal two- and three-stage production schedules with setup times included*, Naval Research Logistics Quarterly 1(1), 61-68 : <https://ideas.repec.org/a/wly/navlog/v1y1954i1p61-68.html> (résumé lu)
- Garey, Johnson, Sethi (1976), *The Complexity of Flowshop and Jobshop Scheduling*, Mathematics of Operations Research 1(2), 117-129 : <https://doi.org/10.1287/moor.1.2.117> (résumé relevé par un moteur de recherche)
- Graham, Lawler, Lenstra, Rinnooy Kan (1979), *Optimization and approximation in deterministic sequencing and scheduling: a survey*, Annals of Discrete Mathematics 5, 287-326 : <https://ir.cwi.nl/pub/9688> (référence relevée, article non lu)
- Taillard (1993), *Benchmarks for basic scheduling problems*, European Journal of Operational Research 64(2), 278-285 : <https://iaorifors.com/paper/16449> (résumé lu)
- Documentation OR-Tools, *The Job Shop Problem* : <https://developers.google.com/optimization/scheduling/job_shop> (page lue ; instance et optimum de 11 reproduits ici)
- Wikipédia, *Job-shop scheduling* : <https://en.wikipedia.org/wiki/Job-shop_scheduling> (synthèse secondaire)
- MiniZinc Challenge 2026, résultats : <https://minizinc.org/challenge/2026/results> (page lue)
- Connexions brain : [[Programmation par contraintes]], [[Programmation linéaire en nombres entiers (MIP)]], [[Optimisation combinatoire]], [[S&OP et plan directeur de production]], [[MRP et calcul des besoins]], [[Plannings de personnel (rostering)]], [[Tournées de véhicules (VRP)]].
