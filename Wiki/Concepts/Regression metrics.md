---
galaxie: wiki
type: concept
nom: Regression metrics
alias: [Métriques de régression, MSE, RMSE, MAE, R2, R², R² ajusté, coefficient de détermination, erreur quadratique moyenne, Huber, régression quantile]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [model-evaluation, regression, supervised]
---

# Regression metrics

## Aperçu

- Mesurent l'écart entre valeurs prédites et observées pour une cible **continue**.
- Le choix dépend de la sensibilité aux gros écarts (quadratique vs absolu) et du besoin d'une échelle interprétable.

## Concepts clés

### Erreurs quadratiques : MSE, RMSE
- MSE = moyenne des carrés des résidus ; pénalise fortement les grandes erreurs. RMSE = sa racine, exprimée **dans l'unité de la cible** (lisible).

### Erreurs absolues : MAE
- Moyenne des valeurs absolues des résidus ; toutes les erreurs pèsent linéairement, donc **robuste aux valeurs aberrantes**.

### R² (coefficient de détermination)
- Part de variance expliquée : 1 = parfait, 0 = aussi bon que prédire la moyenne, négatif = pire que la moyenne. Croît mécaniquement avec le nombre de variables → utiliser le **R² ajusté** pour comparer des modèles de taille différente.

### Pertes robustes / quantile
- Huber (quadratique près de zéro, linéaire au loin) amortit les outliers ; la perte pinball évalue une **régression quantile** (prédire un quantile plutôt que la moyenne).

### Erreurs relatives
- MAPE, sMAPE expriment l'erreur en pourcentage (comparables entre échelles) mais explosent près de zéro et sont asymétriques — surtout utiles en prévision de séries temporelles.

## Les maths, simplement

- $\text{MSE}=\dfrac{1}{n}\sum_i(y_i-\hat y_i)^2$, $\text{RMSE}=\sqrt{\text{MSE}}$, $\text{MAE}=\dfrac{1}{n}\sum_i|y_i-\hat y_i|$.
- $R^2=1-\dfrac{\sum_i(y_i-\hat y_i)^2}{\sum_i(y_i-\bar y)^2}$ ; ajusté : $\bar R^2=1-(1-R^2)\dfrac{n-1}{n-p-1}$.
- MSE est minimisée par la **moyenne** conditionnelle, MAE par la **médiane** conditionnelle : elles ne récompensent pas le même prédicteur.

## En pratique

- RMSE si les grosses erreurs coûtent cher ; MAE si l'on veut la robustesse aux outliers — rapporter les deux est sain.
- R² pour communiquer (sans dimension), jamais seul : l'accompagner d'une erreur dans l'unité métier.
- Toujours sur données de test / plis de [[Validation croisée]] ; un R² d'entraînement élevé peut cacher un surapprentissage ([[Compromis biais-variance]]).
- Inspecter les **résidus** (graphe résidus vs prédits) au-delà du scalaire agrégé : hétéroscédasticité, structure résiduelle, points influents.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.metrics — mean_squared_error, mean_absolute_error, r2_score]].

## Approches voisines & alternatives

- [[Régression linéaire]] — le modèle de référence dont on mesure ici l'erreur.
- [[GLM]] — pour des cibles non gaussiennes, la déviance généralise l'erreur quadratique.
- [[Validation croisée]] — estimation hors échantillon de ces métriques.
- [[Compromis biais-variance]] — décompose l'erreur quadratique attendue (biais² + variance + bruit).
- [[Forecasting metrics]] — la déclinaison séries temporelles : erreurs scaled (MASE, RMSSE) et relatives (MAPE, sMAPE, WAPE), robustes aux échelles et aux zéros.

## Pour aller plus loin

- Hyndman & Koehler (2006) — *Another look at measures of forecast accuracy*.
- Willmott & Matsuura (2005) — RMSE vs MAE, lequel rapporter et pourquoi.
