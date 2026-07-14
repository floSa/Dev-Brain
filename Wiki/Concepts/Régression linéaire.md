---
galaxie: wiki
type: concept
nom: Régression linéaire
alias: [Linear regression, OLS, Moindres carrés ordinaires]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [regression, linear-model, supervised]
---

# Régression linéaire

## Aperçu

- Modèle supervisé : prédit une cible **continue** $y$ comme combinaison linéaire des variables explicatives.
- Le socle des modèles linéaires — interprétable (un coefficient = un effet marginal), rapide, et base de la logistique, du GLM et du GAM.

## Concepts clés

### Le modèle
- $\hat y = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p$. Chaque $\beta_j$ = variation de $y$ pour $+1$ sur $x_j$, les autres variables constantes.

### Moindres carrés (OLS)
- Estime les $\beta$ en minimisant la somme des carrés des résidus. Solution fermée via les équations normales.

### Hypothèses
- Linéarité, erreurs indépendantes, homoscédasticité (variance constante), normalité des résidus (pour l'inférence), pas de colinéarité forte.

### Diagnostic
- $R^2$, résidus vs valeurs ajustées, QQ-plot des résidus, VIF pour la colinéarité.

## Les maths, simplement

- Objectif : $\min_\beta \lVert y - X\beta \rVert^2$. Solution : $\hat\beta = (X^\top X)^{-1} X^\top y$ quand $X^\top X$ est inversible.
- $X^\top X$ mal conditionnée (colinéarité) → estimateurs instables → motive la [[Régularisation]].
- Sous erreurs gaussiennes, OLS coïncide avec l'estimateur du [[Maximum de vraisemblance]].

## En pratique

- Standardiser pour comparer les coefficients ; encoder les catégorielles (one-hot).
- Colinéarité → coefficients ininterprétables : regrouper, retirer, ou régulariser.
- Relation non linéaire → termes polynomiaux, ou passer au [[GAM]].
- Outils : [[Dev/Services/Scikit-Learn|sklearn.linear_model.LinearRegression]], `statsmodels.OLS` (inférence, p-values).

## Approches voisines & alternatives

- [[Régression logistique]] — l'analogue pour une cible catégorielle (classification).
- [[Régularisation]] — Ridge/Lasso/ElasticNet contre la colinéarité et le surapprentissage.
- [[Gradient descent]] — alternative itérative aux équations normales pour estimer les coefficients sur gros volumes.
- [[GLM]] — la généralisation aux cibles non normales (la régression linéaire = GLM lien identité + loi normale).
- [[Arbres de décision]], [[Random Forest]], k-NN — alternatives non linéaires non paramétriques (autre cluster).

## Pour aller plus loin

- Legendre (1805), Gauss (1809) — les moindres carrés.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 3.
