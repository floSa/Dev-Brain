---
galaxie: wiki
type: concept
nom: Régression logistique
alias: [Logistic regression, Régression logit]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [classification, linear-model, supervised, maximum-likelihood]
---

# Régression logistique

## Aperçu

- Modèle linéaire pour cible **catégorielle** : prédit la **probabilité** d'un événement (classification).
- Sortie bornée dans $[0,1]$ via la fonction logistique ; frontière de décision linéaire dans l'espace des variables.

## Concepts clés

### Du linéaire à la probabilité
- Le prédicteur linéaire $z = \beta_0 + \sum_j \beta_j x_j$ passe dans la sigmoïde $\sigma(z) = 1/(1+e^{-z})$ → une probabilité.

### Log-odds (logit)
- $\log\frac{p}{1-p} = z$. Chaque $\beta_j$ agit sur le **log-rapport de cotes** ; $e^{\beta_j}$ s'interprète comme un odds ratio.

### Estimation
- Pas de solution fermée : maximum de vraisemblance, optimisé par descente de gradient ou Newton (IRLS).

### Multiclasse
- Softmax (régression logistique multinomiale) ou stratégie one-vs-rest.

## Les maths, simplement

- $p = \sigma(X\beta)$ avec $\sigma(z)=\frac{1}{1+e^{-z}}$.
- Perte = log-vraisemblance binomiale (entropie croisée) : $-\sum_i [\,y_i \log p_i + (1-y_i)\log(1-p_i)\,]$.
- Maximiser cette vraisemblance relève du [[Maximum de vraisemblance]] ; le problème est convexe → optimum global.

## En pratique

- Calibrer le seuil de décision selon le coût des erreurs (pas forcément $0{,}5$).
- Classes déséquilibrées : poids de classe, rééchantillonnage, métriques adaptées (AUC, F1).
- Régulariser ([[Régularisation]]) — scikit-learn applique une pénalité L2 par défaut.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.linear_model.LogisticRegression]], `statsmodels.Logit` (inférence).

## Approches voisines & alternatives

- [[Régression linéaire]] — l'analogue pour une cible continue.
- [[GLM]] — la logistique *est* un GLM (lien logit, loi binomiale).
- [[Régularisation]] — pénalités L1/L2 sur les coefficients logistiques.
- [[Maximum de vraisemblance]] — le principe d'estimation sous-jacent.
- [[Gradient descent]], [[Newton & quasi-Newton]] — la log-vraisemblance n'a pas de forme close : descente de gradient ou Newton (IRLS).
- [[Classification]] — le chapeau de la tâche : score, seuil, métriques, choix de famille.
- [[SVM]] — même frontière linéaire, mais par marge maximale ; meilleur quand $d \gg n$, sans probabilités natives.
- [[Naive Bayes]] — le pendant génératif : converge plus vite à petit $n$, mais probabilités sur-confiantes.
- [[Perceptron et MLP]] — la logistique *est* un perceptron sans couche cachée ; le MLP en est la généralisation non linéaire.
- [[Arbres de décision]], [[Gradient Boosting (GBDT)]] — les alternatives non linéaires, dominantes sur tabulaire.

## Pour aller plus loin

- Cox (1958).
- ESL ch. 4.
