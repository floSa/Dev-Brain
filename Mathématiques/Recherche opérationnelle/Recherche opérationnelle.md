---
role: hub
nom: Recherche opérationnelle
alias: [operations research, gestion de stock, gestion des stocks, inventory management, planification de la production, ordonnancement, supply chain planning]
pitch: Décider combien commander et quand, puis planifier, ordonnancer et tourner — du vendeur de journaux au plan agrégé, au MRP, à l'atelier, aux plannings de personnel et aux tournées de véhicules.
domaines: [data-sci, ml-eng]
tags: [inventory, newsvendor, scheduling, vehicle-routing, logistics, optimization]
---

# Recherche opérationnelle

> Décider combien commander et quand, puis planifier, ordonnancer et tourner — du vendeur de journaux au plan agrégé, au MRP, à l'atelier, aux plannings de personnel et aux tournées de véhicules.

## Ce qu'il faut comprendre

- **Le dossier porte des problèmes de décision, pas des méthodes de résolution.** La question est celle d'un métier — quelle quantité, à quel moment, avec quelle marge de sécurité — et sa réponse est le plus souvent une formule ou une politique, pas un solveur. Les méthodes (descente, MIP, modeleurs) sont dans [[Optimisation]] ; le critère de partage est la règle D-R12 de la taxonomie. Le dossier a commencé par la gestion de stock ; la planification de la production, l'ordonnancement, les plannings de personnel et les tournées l'ont rejoint.
- **Une seule période d'abord.** [[Modèle du vendeur de journaux (newsvendor)]] est la brique élémentaire : commander une fois avant de connaître la demande. La réponse n'est ni la moyenne ni la médiane de la demande, c'est un **quantile**, dont le niveau est fixé par le rapport du coût de rupture au coût de surstock.
- **Puis la répétition.** [[Quantité économique de commande et tailles de lot]] fixe la **taille** d'une commande quand la demande est stable (compromis lancement contre possession, optimum plat) et traite le cas d'une demande variable dans le temps. [[Stock de sécurité et taux de service]] fixe la **marge** : le même quantile, appliqué à la demande sur le délai, avec deux définitions de service qu'il ne faut pas confondre. [[Politiques de réapprovisionnement (s,S) et (R,Q)]] assemble les deux : quand commander, combien.
- **La loi de la demande vient de la prévision.** [[De la prévision probabiliste à la quantité commandée]] est la couture avec le dossier [[Séries temporelles]] : la quantité optimale demande un quantile, que ni une erreur quadratique ni une somme de quantiles de périodes ne donnent. Les pages [[Intermittent demand]], [[Hierarchical forecasting]], [[Forecasting framing]], [[Forecasting metrics]] et [[Prédiction conforme]] fournissent l'entrée et la mesure de sa qualité.
- **Classer avant de piloter.** [[Classification ABC-XYZ]] range les références par valeur et par régularité de la demande, pour appliquer à chaque classe une politique et une cible de service différentes. Les seuils sont des conventions, et la page le dit.
- **Mesurer.** [[Indicateurs de stock (rotation, couverture, rupture)]] est un référentiel de définitions : leur variation d'une entreprise à l'autre est le premier piège d'un tableau de bord.
- **Du stock au plan, de la quantité au calendrier.** [[S&OP et plan directeur de production]] fixe, par famille puis par produit, combien produire et pour quelle semaine : un plan agrégé qu'un LP chiffre, puis un tableau que le PDP décline. [[MRP et calcul des besoins]] éclate ce plan en composants et en dates de lancement, par une récurrence déterministe qui ne vérifie pas la capacité. [[Ordonnancement d'atelier (job-shop, flow-shop)]] vient ensuite : dans quel ordre, sur quelle machine, avec une borne inférieure pour mesurer l'écart.
- **Des personnes et des véhicules.** [[Plannings de personnel (rostering)]] couvre une demande de présence en respectant des règles dures et en soignant des règles souples ; [[Tournées de véhicules (VRP)]] construit les routes d'une flotte sous capacité et fenêtres de temps. Les modèles de base sont déterministes : chaque page dit ce qu'elle ne couvre pas.
- **Simuler avant de décider.** Quand la formule ne tient plus — demande variable, délais aléatoires, pannes —, [[SimPy]] fait tourner la politique sur un modèle de l'atelier ou du stock et en mesure le comportement. C'est une évaluation, pas une recherche de l'optimum, et c'est pourquoi la brique est ici et pas dans [[Optimisation]], avec les solveurs.
- **Un point d'attention : la capacité.** Le MRP la suppose infinie ; le plan agrégé et l'atelier la rendent explicite. Un plan qui franchit l'étape du MRP sans vérification de charge n'est pas un plan faisable.
- **Ce qui n'est pas ici, et pourquoi.** [[Optimisation combinatoire]], [[Optimisation sous contrainte]], [[Programmation linéaire en nombres entiers (MIP)]] et [[Programmation par contraintes]] restent dans [[Optimisation]] : le MIP et la programmation par contraintes s'appliquent à un stock comme à un horaire, ils ne portent aucun problème en propre. Ces notions donnent les outils des pages ci-dessus, et les pages ci-dessus les renvoient vers eux. La prévision de la demande reste dans [[Séries temporelles]] : c'est l'entrée de la décision, pas la décision.

## Choisir

- Une commande unique avant une demande incertaine (saison, péremption) → [[Modèle du vendeur de journaux (newsvendor)]].
- Une demande stable, quelle taille de commande → [[Quantité économique de commande et tailles de lot]].
- Combien de stock de sécurité pour un taux de service donné → [[Stock de sécurité et taux de service]].
- Quand déclencher une commande et jusqu'à quel niveau → [[Politiques de réapprovisionnement (s,S) et (R,Q)]].
- Transformer la sortie d'un modèle de prévision en quantité → [[De la prévision probabiliste à la quantité commandée]].
- Décider quelles références méritent une politique fine → [[Classification ABC-XYZ]].
- Savoir si la politique en place marche → [[Indicateurs de stock (rotation, couverture, rupture)]].
- Fixer combien produire par famille et par mois, et ce qu'on peut promettre → [[S&OP et plan directeur de production]].
- Passer d'un plan de produits finis aux composants à lancer et à acheter → [[MRP et calcul des besoins]].
- Placer des ordres de fabrication sur des machines → [[Ordonnancement d'atelier (job-shop, flow-shop)]].
- Construire un planning d'équipes qui couvre la demande → [[Plannings de personnel (rostering)]].
- Construire les tournées d'une flotte de véhicules → [[Tournées de véhicules (VRP)]].
- Modéliser un de ces problèmes avec des contraintes plutôt que des inégalités linéaires → [[Programmation par contraintes]], au dossier [[Optimisation]].
- Résoudre un de ces problèmes par un outil libre → [[OR-Tools]] pour les contraintes et les plannings, [[PyVRP]] ou [[HGS-CVRP]] pour les tournées, [[PuLP]] ou [[HiGHS]] pour un modèle linéaire en nombres entiers, tous au dossier [[Optimisation]].
- Essayer une politique de stock ou d'atelier par simulation avant de la déployer → [[SimPy]].

<!-- AUTO:START -->
### Notions
- [[Classification ABC-XYZ]] — domaines : data-sci
- [[De la prévision probabiliste à la quantité commandée]] — domaines : data-sci, ml-eng
- [[Indicateurs de stock (rotation, couverture, rupture)]] — domaines : data-sci
- [[Modèle du vendeur de journaux (newsvendor)]] — domaines : data-sci
- [[MRP et calcul des besoins]] — domaines : data-sci, ml-eng
- [[Ordonnancement d'atelier (job-shop, flow-shop)]] — domaines : data-sci, ml-eng
- [[Plannings de personnel (rostering)]] — domaines : data-sci, ml-eng
- [[Politiques de réapprovisionnement (s,S) et (R,Q)]] — domaines : data-sci, ml-eng
- [[Quantité économique de commande et tailles de lot]] — domaines : data-sci
- [[S&OP et plan directeur de production]] — domaines : data-sci, ml-eng
- [[Stock de sécurité et taux de service]] — domaines : data-sci
- [[Tournées de véhicules (VRP)]] — domaines : data-sci, ml-eng
<!-- AUTO:END -->
