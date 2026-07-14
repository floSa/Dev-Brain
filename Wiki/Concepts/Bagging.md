---
galaxie: wiki
type: concept
nom: Bagging
alias: [Bootstrap aggregating, Ensachage]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, ensemble, bagging]
---

# Bagging

## Aperçu

- *Bootstrap aggregating* : technique d'ensemble **parallèle**. Entraîner le même apprenant sur plusieurs rééchantillons bootstrap du jeu de données, puis agréger (moyenne en régression, vote en classification).
- Objectif : **réduire la variance** sans toucher au biais. Efficace sur des apprenants instables à forte variance (arbres profonds), inutile sur des apprenants stables (régression linéaire).

## Concepts clés

### Bootstrap
- Chaque modèle voit un tirage **avec remise** de même taille que le jeu d'origine. Environ 63 % d'observations uniques par tirage ; le reste est dupliqué ou absent.

### Agrégation
- Les prédictions des $B$ modèles sont combinées : moyenne (régression), vote majoritaire ou moyenne des probabilités (classification). Les erreurs individuelles décorrélées se lissent.

### Out-of-bag (OOB)
- Les ~37 % d'observations non tirées par un modèle servent à l'évaluer → estimation d'erreur quasi gratuite, sans jeu de test séparé.

### Variantes
- [[Random Forest]] = bagging d'arbres **+ décorrélation** par sous-échantillonnage des variables à chaque nœud.
- *Pasting* (tirage sans remise), *random subspaces* (sous-échantillonnage des colonnes), *Extra-Trees* (seuils aléatoires).

## Les maths, simplement

- Moyenne de $B$ prédicteurs de variance $\sigma^2$ et corrélation $\rho$ : variance $\rho\sigma^2 + \frac{1-\rho}{B}\sigma^2$. Le bagging écrase le second terme (en augmentant $B$) ; il ne touche pas au premier — d'où l'intérêt de **décorréler** (Random Forest).
- Le biais de l'ensemble reste celui d'un modèle seul : le bagging ne corrige pas un apprenant biaisé.

## En pratique

- Trivialement parallélisable (modèles indépendants). Peu de réglage : nombre d'estimateurs, taille du rééchantillon.
- Utiliser des apprenants **profonds / instables** : plus leur variance est forte, plus le bagging aide.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.ensemble.BaggingClassifier / BaggingRegressor]], et son cas vedette [[Dev/Services/Scikit-Learn|RandomForest]].

## Approches voisines & alternatives

- [[Ensembling]] — la page chapeau : le bagging y figure comme la famille **parallèle** (réduction de variance).
- [[Random Forest]] — l'application archétypale du bagging (arbres + décorrélation des variables).
- [[Boosting]] — l'autre grande famille d'ensembles : **séquentielle** et orientée **biais**, là où le bagging est parallèle et orienté variance.
- [[Arbres de décision]] — l'apprenant de base typique d'un bagging.

## Pour aller plus loin

- Breiman (1996) — *Bagging Predictors*.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 8 & 15.
