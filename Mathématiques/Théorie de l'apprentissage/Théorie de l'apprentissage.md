---
role: hub
nom: Théorie de l'apprentissage
alias: [learning theory, statistical learning theory, théorie statistique de l'apprentissage]
pitch: Pourquoi la généralisation est possible et de quoi elle dépend — les bornes qui relient erreur d'entraînement, capacité du modèle et taille d'échantillon.
domaines: [data-sci, ml-eng]
tags: [learning-theory, pac-learning, vc-dimension, rademacher-complexity, generalization-bound, no-free-lunch]
---

# Théorie de l'apprentissage

> Pourquoi la généralisation est possible et de quoi elle dépend — les bornes qui relient erreur d'entraînement, capacité du modèle et taille d'échantillon.

## Ce qu'il faut comprendre

- **Ces cinq pages ne servent pas à dimensionner quoi que ce soit, et il faut le savoir avant d'y entrer.** Les bornes sont trop lâches pour donner un nombre d'exemples utilisable en pratique. Leur intérêt est ailleurs : elles disent **de quoi** la généralisation dépend, et cette liste-là est courte et vraie — l'erreur observée, la capacité de la classe d'hypothèses, la taille de l'échantillon.
- **[[No Free Lunch theorem]] est le point de départ, et c'est un résultat d'impossibilité.** Moyenné sur tous les problèmes possibles, aucun algorithme ne domine. Le corollaire est fondateur : généraliser **exige un a priori**. Choisir une architecture, une régularisation, une famille de modèles, c'est choisir ce biais inductif — et sans lui, voir des données ne dit rien sur celles qu'on n'a pas vues.
- **[[PAC learning]] donne le cadre**, [[Generalization bounds]] la forme utilisable : risque réel $\le$ risque empirique $+$ terme de complexité. Le terme de complexité est la seule inconnue, et les deux pages suivantes sont deux façons de l'instancier.
- **[[VC dimension]] et [[Rademacher complexity]] mesurent la même chose autrement.** La VC est **combinatoire, binaire et pire cas** : le plus grand nombre de points que la classe sait étiqueter de toutes les façons. La complexité de Rademacher est **dépendante des données** et s'applique aux fonctions à valeurs réelles, donc elle donne des bornes plus serrées — au prix d'être calculée sur l'échantillon qu'on a.
- **La lecture opérationnelle de tout ça est [[Compromis biais-variance]]** : minimiser « erreur d'entraînement + capacité » plutôt que l'erreur d'entraînement seule. Ce dossier en est la version quantitative.

## Choisir

- Comprendre pourquoi il faut un a priori pour apprendre → [[No Free Lunch theorem]].
- Ce que « apprendre » veut dire formellement, et ce qu'est une complexité d'échantillon → [[PAC learning]].
- La forme générale d'une garantie de généralisation → [[Generalization bounds]].
- Mesurer la capacité d'une classe, indépendamment des données → [[VC dimension]].
- La mesurer sur l'échantillon dont on dispose, avec une borne plus serrée → [[Rademacher complexity]].
- L'arbitrage tel qu'on le pratique sur un projet → [[Compromis biais-variance]], au domaine [[Machine Learning]].
- Mesurer l'erreur d'un modèle réel plutôt que la borner → [[Validation croisée]] et [[Classification metrics]], même domaine.

<!-- AUTO:START -->
### Notions
- [[Generalization bounds]] — domaines : data-sci, ml-eng
- [[No Free Lunch theorem]] — domaines : data-sci, ml-eng
- [[PAC learning]] — domaines : data-sci, ml-eng
- [[Rademacher complexity]] — domaines : data-sci, ml-eng
- [[VC dimension]] — domaines : data-sci, ml-eng
<!-- AUTO:END -->
