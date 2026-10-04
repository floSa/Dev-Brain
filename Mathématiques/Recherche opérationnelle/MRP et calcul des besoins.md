---
role: notion
nom: MRP et calcul des besoins
alias: [MRP, Material Requirements Planning, calcul des besoins, calcul des besoins nets, CBN, éclatement de nomenclature, BOM explosion, nomenclature, bill of materials, BOM, code bas niveau, low-level code, ordre planifié, planned order release, MRP II, nervosité du MRP]
categorie: math/recherche-operationnelle
domaines: [data-sci, ml-eng]
tags: [scheduling, inventory]
---

# MRP et calcul des besoins

## Aperçu

- Le MRP (*material requirements planning*) répond à une question de **dépendance** : étant donné ce qu'on veut livrer de produits finis, **quels composants, en quelle quantité, à quelle date lancer ou commander**. Il part du plan directeur (voir [[S&OP et plan directeur de production]]), éclate la nomenclature niveau par niveau, retranche les stocks et les commandes en cours, et **décale chaque besoin du délai d'obtention**.
- Il diffère de la gestion de stock au point de commande, voir [[Politiques de réapprovisionnement (s,S) et (R,Q)]] : là, la demande de chaque article est traitée comme aléatoire et indépendante. Ici, la demande d'un composant est **calculée** à partir des ordres de son parent, donc connue, groupée et irrégulière (un lot de parent donne un pic chez l'enfant).
- Référence historique : Orlicky, *Material Requirements Planning: The New Way of Life in Production and Inventory Management* (1975). La page ne décrit que le calcul et ses limites, pas un progiciel.

## Concepts clés

### L'enregistrement MRP d'un article

Pour chaque article et chaque période (semaine le plus souvent), six lignes, sous la forme que décrivent les cours de gestion de production :

- **Besoins bruts** : ce que les parents (ou le plan directeur, pour un produit fini) demandent.
- **Réceptions programmées** : commandes déjà passées, qui arrivent à cette période.
- **Stock projeté** : $\text{stock}_t = \text{stock}_{t-1} + \text{réceptions programmées}_t + \text{réceptions planifiées}_t - \text{besoins bruts}_t$.
- **Besoins nets** : la part des besoins bruts que le stock projeté ne couvre pas (un stock de sécurité éventuel joue le rôle de plancher).
- **Réceptions planifiées** : la quantité que le MRP propose de recevoir, dimensionnée par la **règle de lot** (lot pour lot, lot fixe, multiple, période fixe, voir [[Quantité économique de commande et tailles de lot]]).
- **Lancements planifiés** : la réception planifiée **décalée du délai** : $\text{période de lancement} = \text{période de réception} - \text{délai}$.

### Éclatement de nomenclature et niveaux

- La **nomenclature** (BOM) dit combien de chaque composant entre dans un parent. L'éclatement multiplie chaque lancement du parent par la quantité par parent et l'inscrit comme **besoin brut** du composant. Un seul niveau s'applique aux enfants directs ; l'éclatement complet descend jusqu'aux achats.
- Le **code bas niveau** attribue à chaque article le niveau le plus bas où il apparaît, de sorte que **tous ses parents sont planifiés avant lui** : sinon un composant commun à deux niveaux serait calculé avant d'avoir reçu tous ses besoins.
- Le **pegging** (traçage) relie un besoin de composant à la commande ou au parent qui le génère, pour comprendre pourquoi une quantité est demandée.

### Demande dépendante, dimensionnement et groupage

- Un composant utilisé par plusieurs parents **agrège** leurs lancements ; un lot au niveau parent produit un pic de besoins au niveau enfant, que le lot de l'enfant peut encore amplifier. L'exemple chiffré plus bas montre un besoin de 160 composants à la semaine 3 alors que le produit fini n'en réclame que 60.
- Le choix de la règle de lot est donc un choix à plusieurs niveaux, pas article par article. Wagner-Whitin et les heuristiques de lot (voir [[Quantité économique de commande et tailles de lot]]) en sont les outils.

## Les maths, simplement

- Le MRP n'est pas un problème d'optimisation : c'est une **récurrence déterministe**, appliquée de haut en bas dans la nomenclature. Pour une règle de lot donnée, le résultat est unique. L'optimisation intervient en amont (taille des lots) et en aval (capacité).
- Exemple, calculé ici en Python (récurrence ci-dessus, 10 semaines, un produit A qui contient 1 B et 2 C, B contenant lui-même 1 C : C est donc demandé à la fois par A et par B) :

| Article | Données | Résultat |
|---|---|---|
| **A** | besoins bruts 40, 50, 30, 60 en semaines 4, 6, 8, 10 ; stock 10 ; délai 1 ; lot pour lot | lancements 30, 50, 30, 60 en semaines 3, 5, 7, 9 |
| **B** (1 par A) | stock 30 ; délai 2 ; lot de 100 | réceptions 100 en semaines 5 et 9 ; lancements de 100 en semaines 3 et 7 |
| **C** (2 par A, 1 par B) | réception programmée de 50 en semaine 2 ; délai 1 ; lot pour lot | besoins bruts 160, 100, 160, 120 en semaines 3, 5, 7, 9 ; lancements 110, 100, 160, 120 en semaines 2, 4, 6, 8 |

- Lecture : le besoin brut de C en semaine 3 vaut $2 \times 30 + 100 = 160$, dont 100 viennent du lot de B. La réception programmée de C (50 en semaine 2) n'en couvre qu'une partie : le besoin net est de 110. **Rien dans le calcul n'indique que l'atelier peut lancer 160 unités de C en semaine 6 alors que 100 suffisent en semaine 4.** Le résultat est un plan de besoins, pas un plan faisable.
- Code (extrait) :

```python
def mrp(gross, onhand, sched, lead, lot=None):
    T = len(gross); pab = onhand; rec = [0]*T; rel = [0]*T
    for t in range(T):
        pab += sched[t] - gross[t]
        if pab < 0:
            need = -pab
            q = need if lot is None else -(-need // lot) * lot   # lot pour lot ou multiple
            rec[t] = q; pab += q
            if t - lead >= 0: rel[t - lead] = q                  # sinon : retard, lancement immédiat
    return rec, rel
```

## En pratique

- **Le MRP suppose des paramètres statiques et une capacité infinie** : c'est le diagnostic repris en introduction par Schlenkrich et al. (arXiv 2402.14506), qui cherchent précisément à le remplacer par une optimisation couplée à la simulation. Turner et Pauw (1992) attribuent l'échec des systèmes MRP à réduire les stocks à **des défauts fondamentaux de la logique et de ses hypothèses**, et proposent OPT comme alternative (résumé seul lu).
- **Délais planifiés fixes** : le MRP décale chaque besoin d'un délai connu d'avance. Dans l'atelier réel, le délai dépend aussi de l'ordre dans lequel les tâches passent sur les machines, que fixe [[Ordonnancement d'atelier (job-shop, flow-shop)]]. Le calcul ci-dessus ne compare pas le délai planifié au délai réel.
- **Capacité** : le MRP ne la contrôle pas. Une vérification de charge après coup, puis une correction à la main, ou une optimisation de lot capacitaire, la réintroduisent. Schlenkrich et al. comparent MRP, optimisation déterministe et optimisation stochastique à horizon glissant en simulation : l'optimisation fait en général mieux, et **les stocks tampons physiques absorbent le bruit d'atelier** au point de réduire son avantage (résumé lu, résultats de simulation à relire dans leur configuration).
- **Nervosité** : un petit changement de demande peut déplacer de nombreux lancements en cascade. Blackburn, Kropp et Millen (1986, *Management Science* 32(4), 413-429) comparent cinq stratégies pour l'amortir : geler le calendrier dans l'horizon de planification, passer en lot pour lot après le premier niveau, constituer des stocks de sécurité, prévoir au-delà de l'horizon, appliquer une procédure de coût de changement (liste relevée dans le résumé que renvoie un moteur de recherche, la page de l'éditeur n'était pas accessible). C'est l'origine pratique des horizons gelés du plan directeur.
- **Qualité des données** : un MRP tient ou tombe sur la nomenclature, les délais, les stocks et les réceptions programmées. Un stock informatique faux se traduit par un plan faux, sans message d'erreur.
- **Demande de composants à très faible rotation** (pièces de rechange par exemple) : la logique de dépendance ne s'applique pas, la demande est intermittente, voir [[Intermittent demand]].

## Approches voisines & alternatives

- [[S&OP et plan directeur de production]] — l'amont : le PDP donne les besoins en produits finis que le MRP éclate.
- [[Politiques de réapprovisionnement (s,S) et (R,Q)]] — l'alternative pour les articles à demande indépendante : on ne calcule pas les besoins, on tient un niveau.
- [[Quantité économique de commande et tailles de lot]] — le dimensionnement des réceptions planifiées.
- [[Ordonnancement d'atelier (job-shop, flow-shop)]] — l'aval : une fois les ordres lancés, quel ordre sur quelle machine.
- [[Stock de sécurité et taux de service]] — le plancher de stock du calcul et la protection contre l'aléa de demande ou de délai.
- [[Optimisation combinatoire]] — le lot sizing capacitaire est un problème combinatoire.
- [[Programmation linéaire en nombres entiers (MIP)]] — la formulation exacte du lot sizing sur plusieurs niveaux et sous capacité.

## Pour aller plus loin

- Orlicky (1975), *Material Requirements Planning: The New Way of Life in Production and Inventory Management*, McGraw-Hill (référence relevée, ouvrage non lu).
- Schlenkrich, Seiringer, Altendorfer, Parragh, *Enhancing Rolling Horizon Production Planning Through Stochastic Optimization Evaluated by Means of Simulation*, arXiv 2402.14506 : <https://arxiv.org/abs/2402.14506> (introduction lue).
- Turner, Pauw (1992), *Does the MRP Logic Work for Finite Capacity Planning and Operations Scheduling?*, South African Journal of Industrial Engineering 5(2) : <https://sajie.journals.ac.za/pub/article/view/417> (résumé lu).
- Blackburn, Kropp, Millen (1986), *A Comparison of Strategies to Dampen Nervousness in MRP Systems*, Management Science 32(4), 413-429 : <https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.32.4.413> (page éditeur en 403, contenu relevé par un moteur de recherche).
- Guide de révision CPIM sur le calcul de l'enregistrement MRP (formules du stock projeté et du décalage), source de révision : <https://open-exam-prep.com/study-guides/cpim/mrp-capacity/material-requirements-planning> (secondaire, à recouper avec un manuel).
- Connexions brain : [[S&OP et plan directeur de production]], [[Quantité économique de commande et tailles de lot]], [[Politiques de réapprovisionnement (s,S) et (R,Q)]], [[Ordonnancement d'atelier (job-shop, flow-shop)]].
