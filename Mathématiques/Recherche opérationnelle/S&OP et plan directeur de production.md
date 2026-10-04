---
role: notion
nom: S&OP et plan directeur de production
alias: [S&OP, Sales and Operations Planning, Sales & Operations Planning, plan industriel et commercial, PIC, plan directeur de production, PDP, MPS, Master Production Schedule, aggregate planning, planification agrégée, planning agrégé, ATP, available to promise, disponible à la vente, time fences, horizon gelé]
categorie: math/recherche-operationnelle
domaines: [data-sci, ml-eng]
tags: [scheduling, forecasting, inventory, linear-programming]
---

# S&OP et plan directeur de production

## Aperçu

- Deux plans emboîtés. Le **plan agrégé** (S&OP, plan industriel et commercial) fixe, par famille de produits et par mois, **combien produire, avec quelle main-d'œuvre et quel stock**, pour que ventes, production et finance travaillent sur le même chiffre. Le **plan directeur de production** (PDP, *master production schedule*, MPS) le désagrège en **quantités par produit fini et par semaine**, et c'est lui qui alimente le calcul des besoins, voir [[MRP et calcul des besoins]].
- Le premier est une **décision de capacité sur plusieurs mois**, le second un **engagement de calendrier sur quelques semaines**. Ni l'un ni l'autre ne dit sur quelle machine ni dans quel ordre : cette question est celle de [[Ordonnancement d'atelier (job-shop, flow-shop)]].
- Entrée commune : une prévision de la demande, voir [[Forecasting framing]] et [[Hierarchical forecasting]] (prévoir par famille, puis par produit, et réconcilier). Sortie commune : une quantité par période, que la politique de stock de [[Stock de sécurité et taux de service]] et de [[Politiques de réapprovisionnement (s,S) et (R,Q)]] vient compléter pour les articles gérés au point de commande.

## Concepts clés

### Le S&OP : un processus avant d'être un modèle

- La synthèse de la littérature de Thomé, Scavarda, Fernandez et Scavarda (2012, 271 articles classés) ramène le S&OP à un **processus de gestion**, dont le résultat attendu dans la plupart des articles est **l'intégration entre fonctions** (ventes, production, achats), peu d'études y intégrant les plans financiers. Les auteurs signalent aussi qu'il manque des cadres unifiés pour **mesurer** un S&OP ou sa maturité, et que les preuves quantitatives de son effet sur la performance restent rares.
- La description de praticiens (Nethi, 2020, billet de blog professionnel, donc source non académique) retient cinq étapes : **collecte et nettoyage des données**, **plan de demande** (une prévision de consensus, sur 12 mois glissants), **plan d'approvisionnement** (taux de production et stocks sous contraintes de capacité et de matières), **pré-S&OP** (résoudre les écarts, préparer les recommandations), **réunion exécutive** (approuver le plan équilibré). Cadence mensuelle ou trimestrielle, horizon de 12 à 24 mois. D'autres sources découpent autrement ; le point commun est le calendrier fixe et l'arbitrage final par la direction.
- Ce que le processus tranche n'est pas un calcul : **quel écart entre demande et capacité accepter**, et **qui arbitre quand les fonctions ne sont pas d'accord** (marge contre service contre stock). Le modèle chiffre les options ; la réunion choisit.

### Plan agrégé : poursuivre, lisser, ou mélanger

- **Stratégie de poursuite** (*chase*) : la production suit la demande, on ajuste main-d'œuvre, heures supplémentaires ou sous-traitance. Pas de stock, mais des coûts de variation de capacité.
- **Stratégie de lissage** (*level*) : production constante, le stock absorbe les variations. Capacité stable, mais coût de possession et risque de rupture sur les pics.
- **Stratégie mixte** : le cas général. Les leviers sont la production normale, les heures supplémentaires, le stock, le retard (commande différée), l'embauche et le licenciement.
- Le problème se pose comme une **programmation linéaire**. Hanssmann et Hess (1960) la proposent pour la détermination des taux de production et des effectifs mensuels qui minimisent les coûts de salaire, heures supplémentaires, embauche, licenciement, stock et pénurie, en remarquant que **Holt, Modigliani, Muth et Simon** avaient résolu le problème avec des coûts **quadratiques** alors que les coûts pratiques sont le plus souvent linéaires. Holt, Modigliani et Simon (1955) en tirent une **règle de décision linéaire** : la production du mois est une fonction linéaire de la prévision et du stock, calibrée sur une usine réelle.

### Le PDP : un tableau par produit fini

- Pour chaque produit fini, par semaine : **prévision**, **commandes fermes**, **stock projeté** (*projected available balance*), **quantité du PDP**, et **disponible à la vente** (*available to promise*, ATP).
- Le calcul ci-dessous retient, pour chaque semaine, la plus grande de la prévision et des commandes fermes comme demande (une convention de consommation de la prévision parmi d'autres), puis déclenche un lot du PDP dès que le stock projeté passerait sous zéro. La quantité du PDP n'est **pas** une copie de la prévision : c'est une décision de planificateur, bornée par la capacité.
- **ATP** : ce qu'on peut encore promettre à un client sans toucher aux engagements. Pour la première période, stock initial plus quantité du PDP, moins les commandes jusqu'au prochain lot du PDP ; pour les suivantes, quantité du PDP moins les commandes jusqu'au prochain lot (formulation de Wikiversity, « Master Production Schedule »).
- **Horizons gelés** (*time fences*) : le calendrier se découpe en une zone **ferme** (aucun changement sans accord explicite), une zone **semi-ferme** (changements limités) et une zone **libre**. Les sources diffèrent sur les noms et le nombre de barrières (*demand time fence*, *planning time fence* ; Wikiversity en liste quatre) : retenir le principe, pas le vocabulaire.

## Les maths, simplement

- Plan agrégé sur $T$ périodes, demande $d_t$, avec $R_t$ production en temps normal, $O_t$ en heures supplémentaires, $I_t$ le stock et $B_t$ le retard en fin de période :
  $$\min \sum_t \bigl(c_R R_t + c_O O_t + h\,I_t + b\,B_t\bigr) \quad \text{sous} \quad I_t - B_t = I_{t-1} - B_{t-1} + R_t + O_t - d_t,$$
  avec $0 \le R_t \le C_R$ (capacité normale), $0 \le O_t \le C_O$, $I_t, B_t \ge 0$ et stock et retard nuls en fin d'horizon. C'est un LP : voir [[Programmation linéaire en nombres entiers (MIP)]] pour la famille (ici sans entiers), et [[Optimisation sous contrainte]] pour la dualité.
- Exemple chiffré, calculé ici avec `scipy.optimize.linprog` (HiGHS) : demande $d = [100, 120, 160, 180, 140, 100]$ (800 unités), capacité normale 140, heures supplémentaires jusqu'à 40, coûts $c_R = 10$, $c_O = 15$, stock 2 et retard 8 par unité et par période.

| Stratégie | Coût | Remarque |
|---|---|---|
| Poursuite (produire la demande, heures supplémentaires au-dessus de 140) | 8 300 | 60 unités en heures supplémentaires |
| Lissage (133,3 par période, retards autorisés) | 8 680 | 680 de stock et de retard |
| **Optimum du LP** | **8 240** | 20 unités de stock en période 2, 40 en heures supplémentaires en période 4 |

- Lecture : l'optimum bat les deux stratégies pures de 0,7 % et de 5,1 %, en **préconstruisant 20 unités** avant le pic plutôt qu'en payant des heures supplémentaires sur toute la montée. L'écart est modeste sur cet exemple jouet ; l'intérêt est la forme du raisonnement, pas le chiffre.
- Tableau du PDP, produit fini unique, stock initial 40, lot du PDP de 80, prévision $[30, 30, 30, 30, 35, 35, 35, 35]$, commandes fermes $[38, 27, 10, 5, 0, 0, 0, 0]$ (calcul ci-dessus, en Python) :
  - lots du PDP en semaines 2, 4 et 7 ; stock projeté de fin de semaine $[2, 52, 22, 72, 37, 2, 47, 12]$ ;
  - ATP : 2 en semaine 1 (40 moins les 38 déjà promis), 43 en semaine 2 (80 moins 27 et 10), 75 en semaine 4 (80 moins 5), 80 en semaine 7. Une demande de 50 unités pour la semaine 3 dépasse l'ATP de 43 du lot de la semaine 2 : elle ne peut être promise que sur le lot de la semaine 4 (ATP 75), donc livrée en semaine 4 au plus tôt, sauf à déplacer un lot du PDP. L'ATP dit **ce qui est tenable**, pas s'il vaut la peine de remanier le PDP.

## En pratique

- **Le S&OP s'abîme sur la prévision et sur l'arbitrage, pas sur le solveur.** Un plan agrégé qui ne s'appuie pas sur une demande reconnue par les ventes est contesté dès la première réunion. La qualité de prévision se mesure comme dans [[Forecasting metrics]] ; une demande intermittente ou très variable demande les méthodes de [[Intermittent demand]].
- **Prévoir par famille, où les erreurs des références se compensent en partie, est en général plus précis que prévoir par référence** (effet d'agrégation) : c'est pour cela que le plan agrégé travaille par famille. La cohérence entre niveaux de prévision est le sujet de [[Hierarchical forecasting]].
- **Incertitude** : le plan agrégé est déterministe. Les stocks tampons et les marges de sécurité qui absorbent l'écart entre la prévision et le réel se dimensionnent avec [[Stock de sécurité et taux de service]] ; une prévision probabiliste donne un quantile plutôt qu'une moyenne, voir [[De la prévision probabiliste à la quantité commandée]]. Une étude (Schlenkrich, Seiringer, Altendorfer, Parragh, arXiv 2402.14506, soumise en 2024 et révisée jusqu'en août 2026) compare, en simulation à événements discrets, MRP, optimisation déterministe et optimisation stochastique à horizon glissant : l'optimisation fait en général mieux que le MRP seul, mais **quand des stocks tampons physiques existent, ils absorbent le bruit d'atelier et réduisent l'avantage de l'optimisation stochastique**. Résultat de simulation, à relire dans sa configuration avant de le transposer.
- **Sophistication du PDP** : Jonsson et Kjellsdotter Ivert (2015, enquête auprès d'entreprises suédoises, trois indicateurs : faisabilité du plan, rotation des stocks, service client) trouvent que les méthodes de PDP **sans prise en compte de la capacité** donnent une moindre faisabilité du plan que les méthodes sophistiquées, et que **la maturité du processus pèse plus que la méthode**. Enquête corrélationnelle : elle ne dit pas qu'un outil sophistiqué corrige un processus immature.
- **Le plan doit être faisable** : un PDP qui dépasse la capacité d'atelier produit des retards que le MRP puis l'ordonnancement ne pourront que constater. D'où la vérification de capacité avant de figer le PDP.
- **Où est l'optimisation** : l'exemple ci-dessus compte 24 variables, un LP agrégé de cette forme reste de petite taille et n'a pas besoin d'un solveur spécialisé. Le gain tient plus à l'exposition des hypothèses de coût qu'à l'algorithme. Les coûts d'embauche, de licenciement et de retard sont des estimations : l'optimum ne dit rien de sa sensibilité à leur erreur, qui se teste en les faisant varier.

## Approches voisines & alternatives

- [[MRP et calcul des besoins]] — la suite : le PDP donne les besoins en produits finis, le MRP les éclate en composants.
- [[Ordonnancement d'atelier (job-shop, flow-shop)]] — l'étape suivante en aval : quand et sur quelle machine, une fois les quantités fixées.
- [[Politiques de réapprovisionnement (s,S) et (R,Q)]] — l'alternative pour les articles à demande stable, gérés au point de commande plutôt que par un plan.
- [[Quantité économique de commande et tailles de lot]] — la taille des lots du PDP et du MRP.
- [[Classification ABC-XYZ]] — décider quelles familles méritent un plan fin et lesquelles un pilotage au point de commande.
- [[Hierarchical forecasting]] — réconcilier les prévisions par famille et par produit.
- [[Programmation linéaire en nombres entiers (MIP)]] — la formulation exacte quand les décisions sont entières (équipes, lancements).
- [[Optimisation sous contrainte]] — dualité : les prix implicites de la capacité (valeur d'une heure supplémentaire de plus).

## Pour aller plus loin

- Thomé, Scavarda, Fernandez, Scavarda (2012), *Sales and operations planning: A research synthesis*, International Journal of Production Economics 138(1), 1-13 : <https://ideas.repec.org/a/eee/proeco/v138y2012i1p1-13.html> (résumé lu, texte intégral non lu)
- Holt, Modigliani, Simon (1955), *A Linear Decision Rule for Production and Employment Scheduling*, Management Science 2(1), 1-30 : <https://ideas.repec.org/a/inm/ormnsc/v2y1955i1p1-30.html> (résumé lu)
- Hanssmann, Hess (1960), *A Linear Programming Approach to Production and Employment Scheduling*, Management Technology 1(1), 46-51 : <https://ideas.repec.org/a/inm/ormnsc/vmt-1y1960i1p46-51.html> (résumé lu)
- Jonsson, Kjellsdotter Ivert (2015), *Improving performance with sophisticated master production scheduling*, International Journal of Production Economics 168, 118-130 : <https://research.chalmers.se/en/publication/218729> (résumé lu)
- Schlenkrich, Seiringer, Altendorfer, Parragh, *Enhancing Rolling Horizon Production Planning Through Stochastic Optimization Evaluated by Means of Simulation*, arXiv 2402.14506 : <https://arxiv.org/abs/2402.14506> (résumé lu ; dernière révision indiquée août 2026)
- Nethi (2020), *5 Steps of S&OP to Achieve an Integrated Business Plan*, Mastering SAP : <https://masteringsap.com/five-essential-steps-of-sales-and-operations-planning-to-achieve-an-integrated-business-plan/> (page lue, source praticienne)
- Wikiversity, *Master Production Schedule* : <https://en.wikiversity.org/wiki/Master_Production_Schedule> (formules du stock projeté et de l'ATP ; source collaborative, à recouper avec un manuel de production)
- Connexions brain : [[MRP et calcul des besoins]], [[Ordonnancement d'atelier (job-shop, flow-shop)]], [[Forecasting framing]], [[Hierarchical forecasting]], [[Stock de sécurité et taux de service]], [[Quantité économique de commande et tailles de lot]].
