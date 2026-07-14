---
galaxie: wiki
type: concept
nom: Ensembling
alias: [méthodes d'ensemble, ensemble learning, ensemble de modèles, agrégation de modèles]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [ensemble, supervised]
---

# Ensembling

## Aperçu

- Combiner plusieurs modèles en un seul prédicteur, plus performant et plus robuste qu'aucun pris isolément.
- Marche quand les modèles se trompent **différemment** : leurs erreurs se compensent à l'agrégation.

## Concepts clés

### Pourquoi ça marche
- Des erreurs décorrélées s'annulent en moyenne. Le gain est maximal quand les modèles sont à la fois **précis** et **diversifiés** (données, variables, algorithmes ou hyperparamètres différents).

### Bagging — parallèle, réduit la variance
- Le même apprenant sur des rééchantillons bootstrap, agrégés par vote ou moyenne. Voir [[Bagging]] ; archétype [[Random Forest]].

### Boosting — séquentiel, réduit le biais
- Des apprenants faibles empilés, chacun corrigeant les erreurs du précédent. Voir [[Boosting]] ; dominant sur tabulaire [[Gradient Boosting (GBDT)]].

### Stacking & blending
- Un **méta-modèle** apprend à combiner les prédictions de modèles de base **hétérogènes** (ex. arbre + linéaire + kNN). *Stacking* : le méta s'entraîne sur des prédictions *out-of-fold*. *Blending* : un hold-out dédié, plus simple mais moins efficace.

### Voting / averaging
- Combinaison **fixe**, sans apprentissage : vote majoritaire (*hard*) ou moyenne des probabilités (*soft*) en classification, moyenne en régression.

## Les maths, simplement

- Moyenne de $B$ prédicteurs de variance $\sigma^2$ et corrélation $\rho$ : variance $\rho\sigma^2 + \frac{1-\rho}{B}\,\sigma^2$. Plus les modèles sont décorrélés ($\rho$ petit), plus la variance chute — d'où l'importance de la **diversité**.
- Lecture biais-variance : le bagging attaque le terme de variance, le boosting le terme de biais. Voir [[Compromis biais-variance]].

## En pratique

- Souvent **le meilleur** sur données tabulaires (compétitions). Coût : entraînement et inférence plus lourds, interprétabilité réduite.
- Diversifier réellement (algorithmes ou jeux de variables différents) : empiler cinq variantes du même modèle n'apporte presque rien.
- Stacking : utiliser des prédictions **out-of-fold** pour entraîner le méta-modèle, sinon [[Data leakage]].
- Outils : [[Dev/Services/Scikit-Learn|VotingClassifier / StackingClassifier]] ; [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/CatBoost|CatBoost]] côté boosting.

## Approches voisines & alternatives

- [[Bagging]] — famille parallèle, orientée variance.
- [[Boosting]] — famille séquentielle, orientée biais.
- [[Random Forest]], [[Gradient Boosting (GBDT)]] — les ensembles d'arbres les plus utilisés.
- [[Arbres de décision]] — l'apprenant de base le plus courant des ensembles.
- [[Compromis biais-variance]] — la grille de lecture des gains d'un ensemble.

## Pour aller plus loin

- Wolpert (1992) — *Stacked Generalization*.
- Dietterich (2000) — *Ensemble Methods in Machine Learning*.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 8, 10, 15, 16.
