---
galaxie: wiki
type: concept
nom: Boosting
alias: [Boostage]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, ensemble, boosting]
---

# Boosting

## Aperçu

- Technique d'ensemble **séquentielle** : empiler des apprenants **faibles**, chacun corrigeant les erreurs du modèle courant. Le prédicteur final est une somme pondérée.
- Objectif : **réduire le biais** (et, par le réglage, la variance). Transforme une famille d'apprenants médiocres en un prédicteur fort.

## Concepts clés

### Additif & séquentiel
- Le modèle se construit par étapes : $F_m = F_{m-1} + \nu\, h_m$, où $h_m$ est le nouvel apprenant et $\nu$ le taux d'apprentissage. Chaque étape dépend des précédentes — impossible à paralléliser comme le [[Bagging]].

### Apprenants faibles
- Apprenants volontairement simples (souches, arbres peu profonds) : biais élevé, faible variance individuelle. Le boosting réduit le biais en les cumulant.

### Se concentrer sur les erreurs
- *AdaBoost* **repondère** les exemples mal classés pour que l'apprenant suivant s'y focalise.
- *Gradient Boosting* ajuste chaque apprenant sur le **gradient négatif de la perte** (≈ les résidus) du modèle courant.

### Régularisation
- Taux d'apprentissage $\nu$ petit (shrinkage), nombre d'itérations, profondeur, sous-échantillonnage, early stopping. Trop d'itérations sans shrinkage → surapprentissage.

## Les maths, simplement

- Cadre général : minimiser $\sum_i L(y_i, F(x_i))$ en ajoutant un apprenant par pas. *Gradient Boosting* le fait par **descente de gradient dans l'espace des fonctions** ; *AdaBoost* en est le cas particulier avec perte exponentielle et repondération des exemples.
- Contrairement au bagging, le boosting **attaque le biais** : il rapproche progressivement $F$ de l'optimum, au risque de surajuster si on itère trop.

## En pratique

- Souvent le meilleur sur **données tabulaires**, mais plus délicat à régler que le bagging (le trio `learning_rate` / `n_estimators` / `max_depth` se règle ensemble).
- Implémentations dominantes : [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/CatBoost|CatBoost]] ; côté sklearn : [[Dev/Services/Scikit-Learn|HistGradientBoosting / AdaBoost]].

## Approches voisines & alternatives

- [[Ensembling]] — la page chapeau : le boosting y figure comme la famille **séquentielle** (réduction de biais).
- [[AdaBoost]] — le membre fondateur : repondère les exemples ratés. Cas particulier du gradient boosting à perte exponentielle.
- [[Gradient Boosting (GBDT)|Gradient Boosting]] — la variante par descente de gradient, dominante sur tabulaire.
- [[Bagging]] — l'autre grande famille d'ensembles : **parallèle** et orientée **variance**, là où le boosting est séquentiel et orienté biais.
- [[Arbres de décision]] — l'apprenant faible typique d'un boosting.

## Pour aller plus loin

- Freund & Schapire (1997) — *A Decision-Theoretic Generalization of On-Line Learning* (AdaBoost).
- Friedman (2001) — *Greedy Function Approximation: A Gradient Boosting Machine*.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 10.
