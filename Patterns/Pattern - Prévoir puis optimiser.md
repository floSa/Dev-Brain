---
role: pattern
contexte: Décider chaque semaine une quantité à commander, un plan de production ou des tournées à partir d'un historique de demande — prévoir une loi de la demande, la convertir en quantité, puis planifier sous contraintes, et essayer la chaîne par simulation avant de la déployer.
services_cles: [statsforecast, darts, Chronos, HiGHS, PuLP, OR-Tools, PyVRP, SimPy, Prefect]
projets_appliques: []
tags: [pattern, forecasting, inventory, linear-programming, scheduling, simulation]
---

# Pattern — Prévoir puis optimiser

## Contexte

Un industriel ou un distributeur a un historique de ventes ou de consommations, et doit décider : combien commander, combien produire, quelles tournées lancer. La décision se répète (chaque semaine), une personne en est responsable, et le coût d'une rupture et celui d'un surstock se chiffrent dans la même unité. La donnée reste sur site.

La chaîne a cinq étages, et chacun se remplace sans toucher les autres :

```
historique → loi de la demande → quantité → plan sous contraintes → simulation → suivi
```

À appliquer quand trois conditions tiennent : un historique exploitable, des coûts unitaires connus ou estimables, une décision à rythme fixe. Sans la deuxième, la quantité n'a pas de cible et la chaîne se réduit à une moyenne. Le cadre est dans [[Recherche opérationnelle]] (le problème) et [[Séries temporelles]] (l'entrée), les méthodes de résolution dans [[Optimisation]].

## Stack

| Étage | Brique ou notion | Quand la prendre |
|---|---|---|
| Prévoir | [[statsforecast]] | beaucoup de séries, méthodes statistiques rapides |
| Prévoir | [[darts]] | échantillons de trajectoires, backtesting, une API pour plusieurs modèles |
| Prévoir | [[Chronos]], [[Foundation models pour séries temporelles]] | peu d'historique par série ; les quantiles natifs se vérifient |
| Prévoir | [[Hierarchical forecasting]], [[Intermittent demand]] | familles de produits ; demande par à-coups (pièces de rechange) |
| Borne | [[Prédiction conforme]] | une borne haute à couverture annoncée, sans loi |
| Quantité | [[De la prévision probabiliste à la quantité commandée]], [[Modèle du vendeur de journaux (newsvendor)]] | toute commande dont le coût de rupture et de surstock est connu |
| Quantité | [[Stock de sécurité et taux de service]], [[Politiques de réapprovisionnement (s,S) et (R,Q)]] | une revue répétée, un délai d'approvisionnement |
| Tri | [[Classification ABC-XYZ]] | décider quelles références méritent une politique fine |
| Plan | [[S&OP et plan directeur de production]], [[MRP et calcul des besoins]] | produire : du plan agrégé aux composants |
| Plan | [[PuLP]] ou [[HiGHS]] | le plan est un modèle linéaire ou en nombres entiers |
| Calendrier | [[OR-Tools]] | ordre, ressources, plannings : CP-SAT |
| Tournées | [[PyVRP]], [[HGS-CVRP]] | livrer : variantes riches, ou CVRP canonique |
| Simulation | [[SimPy]] | essayer la politique avant de la déployer |
| Orchestration | [[Prefect]] | enchaîner, reprendre et planifier les étages |
| Suivi | [[Walk-forward CV]], [[Indicateurs de stock (rotation, couverture, rupture)]] | le coût réalisé et le niveau de service obtenu |

Le comparatif des solveurs est [[Comparatif - Solveurs d'optimisation]], celui des modèles de prévision [[Comparatif - Forecasting]].

## Décisions clés

### 1. Prévoir une loi, pas un point

- La quantité à commander est un **quantile** de la demande, au niveau du rapport coût de rupture sur coût de rupture plus coût de surstock. Une prévision ponctuelle ne le donne pas.
- La notion chiffre, sur une simulation exécutée (demande lognormale, rapport de coûts 4 contre 1), un surcoût de 22,5 % pour qui commande la moyenne : un ordre de grandeur sur un exemple fabriqué, pas une mesure sur un jeu réel.

### 2. Ne pas sommer des quantiles de périodes

- La quantité couvre un délai : c'est la loi d'une **somme** de demandes corrélées. Sommer les quantiles de chaque période commande trop, échantillonner les périodes indépendamment commande trop peu ; la notion le montre par une simulation.
- Prendre des trajectoires jointes, une loi de la somme, ou prévoir directement la demande cumulée sur le délai.

### 3. La quantité est souvent une formule, pas un solveur

- Un quantile ([[Modèle du vendeur de journaux (newsvendor)]]), une marge ([[Stock de sécurité et taux de service]]) et une politique de revue ([[Politiques de réapprovisionnement (s,S) et (R,Q)]]) se calculent sans solveur.
- Le solveur intervient quand des contraintes **couplent** les décisions : capacité d'une ligne, budget, plusieurs références qui se disputent un camion, ordre des opérations. C'est alors [[Programmation linéaire en nombres entiers (MIP)]] ou [[Programmation par contraintes]].

### 4. Des contrats clairs entre étages

- La sortie de la prévision (trajectoires ou quantiles, par période) est l'entrée du calcul de quantité ; la sortie de celui-ci (quantité par période) est l'entrée du plan. Le pas de la prévision est la période du plan : le vérifier avant d'écrire une ligne de modèle.
- Prévoir par famille puis par produit et réconcilier ([[Hierarchical forecasting]]) quand le plan agrégé et le plan détaillé doivent s'accorder.

### 5. Choisir le solveur après la formulation

- Un modèle linéaire en nombres entiers s'écrit avec un modeleur ([[PuLP]]) et se résout avec un solveur libre ([[HiGHS]]) ; si le modèle est lent, la cause est le plus souvent la formulation avant le solveur.
- Un problème riche en règles, un atelier ou un planning de personnel, se pose en contraintes avec [[OR-Tools]]. Des tournées avec fenêtres de temps ou flotte hétérogène demandent [[PyVRP]], le CVRP simple [[HGS-CVRP]].
- Un résultat de solveur se lit avec son statut et sa borne ; une valeur renvoyée sans statut n'est pas un optimum.

### 6. Simuler avant de déployer

- Rejouer la politique sur des trajectoires de demande avec [[SimPy]] : le coût réalisé et le niveau de service **obtenu face à la cible**, sur plusieurs répétitions et non sur un tirage.
- Évaluer la prévision elle-même par [[Walk-forward CV]] : à chaque origine, produire la quantité avec les seules données passées, observer la demande, compter le coût.

### 7. Recalculer à rythme fixe, et mesurer la décision

- Rejouer la chaîne à chaque période, sur un horizon glissant, comme pour une tournée dont les clients changent ([[Tournées de véhicules (VRP)]]).
- Suivre la rotation, la couverture et les ruptures avec des définitions écrites ([[Indicateurs de stock (rotation, couverture, rupture)]]) : leur variation d'une entreprise à l'autre est le premier piège d'un tableau de bord.

## Pièges

- **Optimiser sur la moyenne.** Le plan est « optimal » pour une demande qui n'arrive jamais ; la marge disparaît.
- **Un quantile natif pris pour calibré.** Les quantiles d'un modèle de fondation se contrôlent sur l'historique avant d'être commandés ([[Calibration]], [[Prédiction conforme]]).
- **Un modèle précis sur une donnée incertaine.** Le solveur rend un chiffre exact à partir d'une prévision qui ne l'est pas : garder la marge de sécurité de l'étage précédent.
- **La capacité oubliée.** Le calcul des besoins ne vérifie pas la capacité ; un plan qui franchit l'étape sans contrôle de charge n'est pas faisable ([[MRP et calcul des besoins]]).
- **Un solveur avant d'en avoir besoin.** Un solveur pour une quantité que la formule donne ajoute une dépendance sans bénéfice.
- **Un modèle infaisable ou non borné.** Vérifier la faisabilité sur un petit cas avant de passer à l'échelle ; le même piège est décrit dans [[Pattern - Pipeline scraping → matching → optimisation]].
- **Des étages non rejouables.** Sans graine et sans versionnage des entrées, le plan de la semaine dernière ne se reconstruit pas.

## Voir aussi

- [[Recherche opérationnelle]] — le hub des problèmes de décision : stock, plan, atelier, tournées
- [[Optimisation]] — le hub des méthodes et des solveurs
- [[Séries temporelles]] — le hub de la prévision
- [[Comparatif - Solveurs d'optimisation]] — choisir le modeleur et le solveur
- [[Comparatif - Forecasting]] — choisir le modèle de prévision
- [[De la prévision probabiliste à la quantité commandée]] — la couture entre les deux premiers étages
- [[Pattern - Pipeline scraping → matching → optimisation]] — la même idée de décision par optimisation, côté collecte
- [[Pattern - Pipeline de maintenance prédictive on-prem]] — la décision chiffrée de [[Politique de maintenance et coût]]
