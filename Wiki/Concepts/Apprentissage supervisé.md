---
galaxie: wiki
type: concept
nom: Apprentissage supervisé
alias: [Supervised learning, Apprentissage supervise, Modélisation supervisée]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, classification, regression]
---

# Apprentissage supervisé

## Aperçu

- Famille de méthodes qui apprennent une fonction $f : X \to y$ à partir d'exemples **déjà étiquetés** : on connaît la réponse sur les données d'entraînement, on veut la prédire sur des données nouvelles.
- La nature de la cible $y$ décide de la tâche : catégorielle → [[Classification]], continue → [[Régression]]. C'est le premier embranchement de tout projet ML (cf. [[Types de données et choix de modèle]]).

## Concepts clés

### Ce qui définit le cadre
- Un jeu $\{(x_i, y_i)\}_{i=1}^{n}$ : $x_i$ = variables explicatives (*features*), $y_i$ = cible (*label*, *target*). Sans $y$, on est en [[Apprentissage non supervisé]].
- Hypothèse fondatrice : les données d'entraînement et de production sont tirées de la **même distribution**. Quand elle se rompt en production, c'est du [[Data drift]].

### Apprendre = minimiser un risque
- On choisit une fonction de perte $\ell(y, \hat{y})$ qui chiffre le coût d'une erreur, puis on cherche le modèle qui la minimise en moyenne sur l'entraînement.
- La perte encode la tâche : erreur quadratique pour la régression, [[Cross-entropy|entropie croisée]] pour la classification.

### Le vrai objectif : généraliser
- Minimiser l'erreur d'entraînement est facile et trompeur (un [[Arbres de décision|arbre]] profond atteint 0). Ce qui compte est l'erreur sur des données **jamais vues**.
- D'où l'obligation de mesurer sur un jeu tenu à l'écart, via [[Validation croisée|validation croisée]], et de se garder du [[Data leakage]].

### Le dilemme central
- Trop simple → sous-apprentissage (biais) ; trop flexible → surapprentissage (variance). Tout le métier tient dans cet arbitrage : [[Compromis biais-variance]], que l'on pilote par la [[Régularisation]] et l'[[Optimisation d'hyperparamètres]].

### Les grandes familles de modèles
- **Linéaires** — frontière ou surface lisse, très interprétables : [[Régression linéaire]], [[Régression logistique]], [[GLM]], [[GAM]].
- **À base d'arbres** — découpages successifs, dominants sur données tabulaires : [[Arbres de décision]], [[Random Forest]], [[Gradient Boosting (GBDT)]].
- **À noyau / à distance** — reposent sur une notion de proximité : [[SVM]], [[k-NN]].
- **Probabilistes** — modélisent la loi des données : [[Naive Bayes]], [[Analyse discriminante]], [[Gaussian Process]], [[Inférence bayésienne]].
- **Réseaux de neurones** — représentations apprises, indispensables sur données non structurées : [[Perceptron et MLP]], [[CNN]], [[Transformer architectures]].

## Les maths, simplement

- Risque empirique (ce qu'on minimise réellement) : $\hat{R}(f) = \frac{1}{n} \sum_{i=1}^{n} \ell\big(y_i, f(x_i)\big)$ — la perte moyenne sur les $n$ exemples d'entraînement.
- Risque réel (ce qu'on voudrait minimiser, inaccessible) : $R(f) = \mathbb{E}_{(x,y)}\big[\ell(y, f(x))\big]$ — la perte moyenne sur **toute** la distribution. L'écart $R - \hat{R}$ est l'erreur de généralisation, bornée en théorie par [[VC dimension]] / [[Rademacher complexity]].
- Décomposition de l'erreur quadratique : $\mathbb{E}[(y - \hat{f})^2] = \underbrace{\text{Biais}^2}_{\text{modèle trop rigide}} + \underbrace{\text{Variance}}_{\text{modèle trop sensible}} + \underbrace{\sigma^2}_{\text{bruit irréductible}}$.

## En pratique

- **Toujours commencer par une baseline triviale** (classe majoritaire, moyenne de la cible, [[Régression logistique|régression logistique]]). Un modèle complexe qui ne la bat pas ne sert à rien, et beaucoup n'y arrivent pas.
- **Séparer les données avant de regarder quoi que ce soit.** Toute décision prise en voyant le jeu de test le contamine — c'est la cause n°1 de résultats qui s'effondrent en production ([[Data leakage]]).
- Sur données **tabulaires**, le boosting d'arbres reste l'état de l'art ; les réseaux de neurones n'y gagnent que rarement. Sur texte / image / son, c'est l'inverse.
- Les hyperparamètres se règlent **sur la validation, jamais sur le test** — sinon le test devient un second jeu d'entraînement ([[Validation croisée|CV imbriquée]] si on doit à la fois régler et estimer).
- Étiqueter coûte cher : c'est souvent le vrai budget du projet, pas le calcul. Quand les étiquettes manquent, regarder du côté du [[Transfer learning vision|transfer learning]] ou de l'[[Apprentissage non supervisé]].
- Outils : [[Dev/Services/Scikit-Learn|scikit-learn]] (API `fit`/`predict` uniforme), [[Dev/Services/XGBoost|XGBoost]] / [[Dev/Services/LightGBM|LightGBM]] sur tabulaire, [[Dev/Services/PyTorch|PyTorch]] sur non structuré.

## Approches voisines & alternatives

- [[Classification]] — la branche « cible catégorielle » : prédire une classe.
- [[Régression]] — la branche « cible continue » : prédire une quantité.
- [[Apprentissage non supervisé]] — le pendant sans cible : structurer plutôt que prédire.
- [[Types de données et choix de modèle]] — l'aiguillage : quelle tâche et quel modèle selon la donnée disponible.
- [[Reinforcement learning]] — ni étiquettes ni distribution fixe : un agent apprend d'un signal de récompense différé.
- [[Systèmes de recommandation]] — cadre hybride, où le signal est implicite (clics, achats) plutôt qu'étiqueté.

## Pour aller plus loin

- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 2 et 7.
- Vapnik (1998) — *Statistical Learning Theory* : le cadre formel de la minimisation du risque.
- Documentation scikit-learn — *Supervised learning* : le catalogue complet des estimateurs.
