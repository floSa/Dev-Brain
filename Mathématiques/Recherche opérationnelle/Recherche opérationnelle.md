---
role: hub
nom: Recherche opérationnelle
alias: [operations research, gestion de stock, gestion des stocks, inventory management]
pitch: Décider combien commander et quand — le modèle du vendeur de journaux, le stock de sécurité, les politiques de réapprovisionnement et les indicateurs qui disent si ça marche.
domaines: [data-sci, ml-eng]
tags: [inventory, newsvendor, optimization]
---

# Recherche opérationnelle

> Décider combien commander et quand — le modèle du vendeur de journaux, le stock de sécurité, les politiques de réapprovisionnement et les indicateurs qui disent si ça marche.

## Ce qu'il faut comprendre

- **Le dossier porte des problèmes de décision, pas des méthodes de résolution.** La question est celle d'un métier — quelle quantité, à quel moment, avec quelle marge de sécurité — et sa réponse est le plus souvent une formule ou une politique, pas un solveur. Les méthodes (descente, MIP, modeleurs) sont dans [[Optimisation]] ; le critère de partage est la règle D-R12 de la taxonomie. Le dossier est ouvert pour la gestion de stock ; la planification et l'ordonnancement viendront le rejoindre.
- **Une seule période d'abord.** [[Modèle du vendeur de journaux (newsvendor)]] est la brique élémentaire : commander une fois avant de connaître la demande. La réponse n'est ni la moyenne ni la médiane de la demande, c'est un **quantile**, dont le niveau est fixé par le rapport du coût de rupture au coût de surstock.
- **Puis la répétition.** [[Quantité économique de commande et tailles de lot]] fixe la **taille** d'une commande quand la demande est stable (compromis lancement contre possession, optimum plat) et traite le cas d'une demande variable dans le temps. [[Stock de sécurité et taux de service]] fixe la **marge** : le même quantile, appliqué à la demande sur le délai, avec deux définitions de service qu'il ne faut pas confondre. [[Politiques de réapprovisionnement (s,S) et (R,Q)]] assemble les deux : quand commander, combien.
- **La loi de la demande vient de la prévision.** [[De la prévision probabiliste à la quantité commandée]] est la couture avec le dossier [[Séries temporelles]] : la quantité optimale demande un quantile, que ni une erreur quadratique ni une somme de quantiles de périodes ne donnent. Les pages [[Intermittent demand]], [[Hierarchical forecasting]], [[Forecasting framing]], [[Forecasting metrics]] et [[Prédiction conforme]] fournissent l'entrée et la mesure de sa qualité.
- **Classer avant de piloter.** [[Classification ABC-XYZ]] range les références par valeur et par régularité de la demande, pour appliquer à chaque classe une politique et une cible de service différentes. Les seuils sont des conventions, et la page le dit.
- **Mesurer.** [[Indicateurs de stock (rotation, couverture, rupture)]] est un référentiel de définitions : leur variation d'une entreprise à l'autre est le premier piège d'un tableau de bord.
- **Ce qui n'est pas ici, et pourquoi.** [[Optimisation combinatoire]], [[Optimisation sous contrainte]] et [[Programmation linéaire en nombres entiers (MIP)]] restent dans [[Optimisation]] : le MIP s'applique à un stock comme à un horaire, il ne porte aucun problème en propre. La prévision de la demande reste dans [[Séries temporelles]] : c'est l'entrée de la décision, pas la décision.

## Choisir

- Une commande unique avant une demande incertaine (saison, péremption) → [[Modèle du vendeur de journaux (newsvendor)]].
- Une demande stable, quelle taille de commande → [[Quantité économique de commande et tailles de lot]].
- Combien de stock de sécurité pour un taux de service donné → [[Stock de sécurité et taux de service]].
- Quand déclencher une commande et jusqu'à quel niveau → [[Politiques de réapprovisionnement (s,S) et (R,Q)]].
- Transformer la sortie d'un modèle de prévision en quantité → [[De la prévision probabiliste à la quantité commandée]].
- Décider quelles références méritent une politique fine → [[Classification ABC-XYZ]].
- Savoir si la politique en place marche → [[Indicateurs de stock (rotation, couverture, rupture)]].

<!-- AUTO:START -->
### Notions
- [[Classification ABC-XYZ]] — domaines : data-sci
- [[De la prévision probabiliste à la quantité commandée]] — domaines : data-sci, ml-eng
- [[Indicateurs de stock (rotation, couverture, rupture)]] — domaines : data-sci
- [[Modèle du vendeur de journaux (newsvendor)]] — domaines : data-sci
- [[Politiques de réapprovisionnement (s,S) et (R,Q)]] — domaines : data-sci, ml-eng
- [[Quantité économique de commande et tailles de lot]] — domaines : data-sci
- [[Stock de sécurité et taux de service]] — domaines : data-sci
<!-- AUTO:END -->
