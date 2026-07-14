---
galaxie: wiki
type: concept
nom: Optimisation d'hyperparamètres
alias: [Hyperparameter tuning, GridSearch, RandomSearch, Optimisation bayésienne, HPO, Réglage des hyperparamètres]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [hyperparameter-tuning, model-evaluation, bayesian]
---

# Optimisation d'hyperparamètres

## Aperçu

- Cherche la configuration (hyperparamètres) qui maximise la performance estimée d'un modèle — réglages **fixés avant** l'entraînement, par opposition aux paramètres appris.
- Chaque candidat est noté par [[Validation croisée]] ; la stratégie de recherche distingue les méthodes.

## Concepts clés

### Hyperparamètre vs paramètre
- Paramètre : appris par l'algorithme (coefficients, poids des feuilles). Hyperparamètre : choisi par l'utilisateur (force de [[Régularisation]] $\lambda$, profondeur d'arbre, taux d'apprentissage, $K$ voisins).

### Grid search
- Produit cartésien de valeurs candidates, chaque combinaison évaluée. Exhaustif et reproductible mais explose avec la dimension (malédiction combinatoire).

### Random search
- Tire les configurations au hasard dans les plages. À budget égal, **surpasse souvent la grille** : seuls quelques hyperparamètres comptent vraiment, et l'aléatoire les échantillonne plus finement (Bergstra & Bengio, 2012).

### Optimisation bayésienne
- Construit un **modèle de substitution** (processus gaussien, TPE) de la fonction performance, puis choisit le prochain candidat via une **fonction d'acquisition** (expected improvement) qui arbitre exploration/exploitation. Converge en moins d'essais — utile quand chaque entraînement est coûteux.

### CV imbriquée
- Régler et évaluer sur les mêmes plis donne un score **optimiste**. La boucle interne règle, la boucle externe évalue → estimation honnête.

## Les maths, simplement

- Problème : $\boldsymbol{\theta}^\star = \arg\max_{\boldsymbol{\theta}\in\Theta} \ \widehat{\text{CV}}(\boldsymbol{\theta})$, où $\widehat{\text{CV}}$ est le score de [[Validation croisée]] de la configuration $\boldsymbol{\theta}$.
- Fonction boîte noire, sans gradient, coûteuse à évaluer → d'où les stratégies sans dérivée (grille, aléatoire, substitution bayésienne).
- Acquisition (bayésien) : $\boldsymbol{\theta}_{\text{next}} = \arg\max\ \text{EI}(\boldsymbol{\theta})$ équilibre gain espéré et incertitude du substitut.

## En pratique

- Définir des plages **log** pour les paramètres d'échelle ($\lambda$, taux d'apprentissage) : `loguniform`, pas `uniform`.
- Commencer en random search large pour cerner la zone utile, puis affiner (bayésien ou grille resserrée).
- Couper tôt les essais sans promesse (successive halving, Hyperband) pour économiser le budget.
- Régler revient à viser le point bas du [[Compromis biais-variance]] (curseur de complexité / régularisation).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.model_selection — GridSearchCV, RandomizedSearchCV, HalvingGridSearchCV]] ; [[Dev/Services/Optuna|Optuna]] pour le bayésien et le pruning ; [[Dev/Services/Hyperopt|Hyperopt]] (TPE historique) ; [[Dev/Services/Ray Tune|Ray Tune]] pour l'orchestration distribuée (schedulers ASHA/PBT).

## Approches voisines & alternatives

- [[Validation croisée]] — la fonction de score que toute recherche optimise.
- [[Compromis biais-variance]] — ce que le réglage navigue concrètement.
- [[Régularisation]] — son $\lambda$ est l'hyperparamètre le plus emblématique à régler.

## Pour aller plus loin

- Bergstra & Bengio (2012) — *Random Search for Hyper-Parameter Optimization*.
- Snoek, Larochelle & Adams (2012) — *Practical Bayesian Optimization of Machine Learning Algorithms*.
