---
galaxie: wiki
type: concept
nom: Gradient Boosting (GBDT)
alias: [GBDT, Gradient boosting, Gradient boosted trees, Boosting de gradient, GBM]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, tree-based, ensemble, boosting]
---

# Gradient Boosting (GBDT)

## Aperçu

- Ensemble supervisé séquentiel (une instance de [[Boosting]]) : ajoute des [[Arbres de décision]] les uns après les autres, chacun corrigeant les erreurs résiduelles du modèle courant.
- Vu comme une descente de gradient dans l'espace des fonctions : chaque arbre approxime le gradient de la perte. Souvent le meilleur modèle sur données tabulaires.

## Concepts clés

### Additif & séquentiel
- Le modèle se construit par étapes : $F_m = F_{m-1} + \nu\, h_m$, où $h_m$ est un nouvel arbre et $\nu$ le taux d'apprentissage. À l'opposé du [[Random Forest]] où les arbres sont indépendants.

### Apprendre sur les résidus (gradient)
- Chaque arbre $h_m$ est ajusté pour prédire le **gradient négatif de la perte** évalué au modèle courant — c'est-à-dire la direction qui réduit l'erreur. Avec la perte quadratique, ce gradient se ramène aux résidus.

### Arbres faibles
- Les apprenants sont volontairement peu profonds (souches à quelques niveaux). Faible variance, biais élevé individuellement — le boosting réduit le biais en cumulant.

### Régularisation
- Taux d'apprentissage $\nu$ petit (shrinkage), nombre d'arbres, profondeur, sous-échantillonnage des lignes/colonnes (stochastic gradient boosting), pénalités sur les feuilles. $\nu$ bas + beaucoup d'arbres généralise mieux mais coûte plus.

## Les maths, simplement

- Objectif : minimiser $\sum_i L(y_i, F(x_i))$ sur la fonction $F$. À l'étape $m$, on calcule le pseudo-résidu $r_{im} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]_{F = F_{m-1}}$.
- On ajuste un arbre $h_m$ sur ces $r_{im}$, puis $F_m = F_{m-1} + \nu\, h_m$. Itérer = descendre le gradient, un arbre par pas.
- Perte quadratique → $r_{im} = y_i - F_{m-1}(x_i)$ : on apprend littéralement sur les résidus.

## En pratique

- Plus performant mais plus délicat à régler que le [[Random Forest]] : le trio `learning_rate` / `n_estimators` / `max_depth` se règle ensemble (early stopping sur jeu de validation).
- Séquentiel → moins parallélisable que Random Forest ; sensible au surapprentissage si trop d'arbres sans shrinkage.
- Les implémentations modernes — [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/CatBoost|CatBoost]] — ajoutent gestion native des NA, binning d'histogrammes, régularisation et parallélisme : ce sont elles que l'on utilise en pratique.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.ensemble.HistGradientBoostingClassifier / HistGradientBoostingRegressor]] (variante histogramme rapide, intégrée à sklearn).

## Approches voisines & alternatives

- [[Arbres de décision]] — l'apprenant de base ; le boosting en empile beaucoup, faibles et séquentiels.
- [[Random Forest]] — l'autre famille d'ensembles d'arbres : parallèle et orientée variance, là où le boosting est séquentiel et orienté biais. Random Forest se règle plus facilement ; le boosting plafonne souvent plus haut.

## Pour aller plus loin

- Friedman (2001) — *Greedy Function Approximation: A Gradient Boosting Machine*.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 10.
