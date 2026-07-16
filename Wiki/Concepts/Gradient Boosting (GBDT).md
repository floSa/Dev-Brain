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

### Les hyperparamètres, et à quoi ils servent

Ils se rangent en trois groupes. Confondre les groupes est la cause la plus fréquente d'un réglage qui ne converge pas.

**1. Le couple qui gouverne tout**

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `learning_rate` ($\nu$) | Rétrécit la contribution de chaque arbre | ↓ = généralise mieux, exige plus d'arbres. Le levier n°1 |
| `n_estimators` | Nombre d'arbres | ↑ = plus de capacité, surapprend passé l'optimum |

- Ces deux-là sont **liés par un produit** : diviser `learning_rate` par 2 demande environ 2× plus d'arbres pour le même ajustement. Ne jamais les régler séparément.
- La bonne pratique évacue la question : fixer `learning_rate` bas (0,01-0,05), mettre `n_estimators` très haut, et laisser l'**early stopping** trouver le nombre d'arbres. Le second paramètre cesse alors d'en être un.

**2. La complexité de chaque arbre — combien de biais on retire par pas**

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `max_depth` | Profondeur maximale | ↑ = interactions plus riches, surapprentissage. 3-8 en boosting (≠ Random Forest) |
| `num_leaves` (LightGBM) | Nombre de feuilles | Le vrai levier de LightGBM, qui croît **par feuille** et non par niveau. Garder $< 2^{\texttt{max\_depth}}$ |
| `min_child_weight` / `min_data_in_leaf` | Poids/effectif minimal d'une feuille | ↑ = feuilles plus peuplées, moins de bruit appris |

**3. La régularisation — comment on encaisse le bruit**

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `subsample` | Fraction des **lignes** par arbre | < 1 = décorrèle les arbres (*stochastic gradient boosting*), effet régularisant |
| `colsample_bytree` | Fraction des **colonnes** par arbre | < 1 = idem, utile quand les variables sont nombreuses ou redondantes |
| `reg_lambda` (L2) / `reg_alpha` (L1) | Pénalité sur les valeurs de feuilles | ↑ = prédictions plus prudentes ([[Régularisation]]) |
| `early_stopping_rounds` | Arrête si la validation ne progresse plus | **Le plus rentable de tous.** À activer par défaut |

**Le même paramètre change de nom selon la bibliothèque** — la source d'erreur la plus banale. Correspondance entre [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]] et [[Dev/Services/CatBoost|CatBoost]] :

| Rôle | XGBoost | LightGBM | CatBoost |
|---|---|---|---|
| Taux d'apprentissage | `eta` / `learning_rate` | `learning_rate` | `learning_rate` |
| Nombre d'arbres | `n_estimators` | `num_iterations` | `iterations` |
| Complexité de l'arbre | `max_depth` | `num_leaves` | `depth` |
| Pénalité L2 | `lambda` | `lambda_l2` | `l2_leaf_reg` |
| Lignes échantillonnées | `subsample` | `bagging_fraction` | `subsample` |

## Les maths, simplement

- Objectif : minimiser $\sum_i L(y_i, F(x_i))$ sur la fonction $F$. À l'étape $m$, on calcule le pseudo-résidu $r_{im} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]_{F = F_{m-1}}$.
- On ajuste un arbre $h_m$ sur ces $r_{im}$, puis $F_m = F_{m-1} + \nu\, h_m$. Itérer = descendre le gradient, un arbre par pas.
- Perte quadratique → $r_{im} = y_i - F_{m-1}(x_i)$ : on apprend littéralement sur les résidus.

## En pratique

- **L'ordre de réglage qui marche** : activer l'early stopping et fixer `learning_rate` bas → régler la complexité de l'arbre (`max_depth` / `num_leaves`) → ajouter du sous-échantillonnage (`subsample`, `colsample_bytree`) → finir par les pénalités. Chercher les quatre groupes d'un coup en grille est un gâchis de calcul ([[Optimisation d'hyperparamètres]]).
- **`max_depth` ne se règle pas comme en [[Random Forest]]** : ici les arbres doivent rester *faibles* (3 à 8), là-bas on les laisse profonds. Reprendre les réflexes de l'un chez l'autre donne un modèle médiocre.
- Séquentiel → moins parallélisable que Random Forest ; sensible au surapprentissage si trop d'arbres sans shrinkage.
- Les implémentations modernes — [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/CatBoost|CatBoost]] — ajoutent gestion native des NA, binning d'histogrammes, régularisation et parallélisme : ce sont elles que l'on utilise en pratique.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.ensemble.HistGradientBoostingClassifier / HistGradientBoostingRegressor]] (variante histogramme rapide, intégrée à sklearn).

## Approches voisines & alternatives

- [[AdaBoost]] — l'ancêtre : même famille, mais repondère les exemples au lieu de changer la cible. Le gradient boosting en est la généralisation (AdaBoost = perte exponentielle).
- [[Arbres de décision]] — l'apprenant de base ; le boosting en empile beaucoup, faibles et séquentiels.
- [[Random Forest]] — l'autre famille d'ensembles d'arbres : parallèle et orientée variance, là où le boosting est séquentiel et orienté biais. Random Forest se règle plus facilement ; le boosting plafonne souvent plus haut.
- [[Perceptron et MLP]] — le concurrent des réseaux, qui perd sur tabulaire à taille de données usuelle.
- [[Types de données et choix de modèle]] — pourquoi c'est le défaut sur tabulaire, et sa limite : il n'extrapole pas.

## Pour aller plus loin

- Friedman (2001) — *Greedy Function Approximation: A Gradient Boosting Machine*.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 10.
