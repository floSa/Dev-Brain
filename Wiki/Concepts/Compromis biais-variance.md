---
galaxie: wiki
type: concept
nom: Compromis biais-variance
alias: [Bias-variance tradeoff, Biais-variance, Sous-apprentissage, Surapprentissage, Underfitting, Overfitting]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [model-evaluation, supervised]
---

# Compromis biais-variance

## Aperçu

- L'erreur de généralisation d'un modèle se décompose en **biais** (erreur d'hypothèse, modèle trop rigide) et **variance** (sensibilité au jeu d'entraînement, modèle trop souple).
- Réduire l'un augmente souvent l'autre : le bon modèle est celui qui minimise leur somme, pas l'un des deux seul.

## Concepts clés

### Biais → sous-apprentissage
- Le modèle est trop simple pour capter la structure (ex. droite sur des données courbes). Erreur élevée en entraînement **et** en test. Symptôme : les deux scores plafonnent bas et proches.

### Variance → surapprentissage
- Le modèle colle au bruit de l'échantillon (ex. arbre très profond). Erreur d'entraînement quasi nulle mais erreur de test élevée. Symptôme : grand écart entre score d'entraînement et score de test.

### Complexité du modèle
- Augmenter la complexité (degré polynomial, profondeur d'arbre, nombre de variables) fait baisser le biais et monter la variance. L'erreur de test suit une courbe en U ; l'optimum est entre les deux.

### Leviers pour déplacer le curseur
- Réduire la variance : plus de données, [[Régularisation]], [[Random Forest|bagging]], simplifier le modèle.
- Réduire le biais : modèle plus expressif, [[Gradient Boosting (GBDT)|boosting]], meilleures variables ([[Ingénierie des caractéristiques]]).

## Les maths, simplement

- Pour une cible $y = f(x) + \varepsilon$ avec $\operatorname{Var}(\varepsilon)=\sigma^2$, l'erreur quadratique attendue d'un prédicteur $\hat{f}$ en un point se décompose :
- $\mathbb{E}\big[(y-\hat{f}(x))^2\big] = \underbrace{(\mathbb{E}[\hat{f}(x)] - f(x))^2}_{\text{biais}^2} + \underbrace{\operatorname{Var}(\hat{f}(x))}_{\text{variance}} + \underbrace{\sigma^2}_{\text{bruit irréductible}}$.
- Le bruit irréductible $\sigma^2$ est le plancher : aucun modèle ne descend en dessous.

## En pratique

- Diagnostiquer avec des **courbes d'apprentissage** (erreur train/test vs taille du jeu) : écart qui persiste = variance ; plateau haut des deux = biais.
- La [[Validation croisée]] estime l'erreur de test qui matérialise ce compromis.
- L'[[Optimisation d'hyperparamètres]] revient à chercher le point bas de la courbe en U (force de régularisation, profondeur, nombre d'estimateurs).
- Outils : courbes via [[Dev/Services/Scikit-Learn|sklearn.model_selection.learning_curve / validation_curve]].

## Approches voisines & alternatives

- [[Apprentissage supervisé]] — le cadre dont ce compromis est le dilemme central.
- [[Régularisation]] — ajoute du biais pour réduire la variance ; l'incarnation la plus directe du compromis.
- [[k-NN]] — l'illustration la plus lisible du compromis : la courbe erreur vs `k` le donne à voir directement.
- [[Random Forest]] — réduit la variance par agrégation (bagging) sans toucher au biais.
- [[Gradient Boosting (GBDT)]] — réduit le biais séquentiellement, au risque d'augmenter la variance.
- [[Validation croisée]] — l'outil de mesure du point d'équilibre.
- [[Generalization bounds]] — la version quantifiée du compromis : risque empirique (biais+bruit) + pénalité de capacité (variance).
- [[VC dimension]] — mesure formelle de la capacité d'un modèle, soit le versant variance de ce compromis.

## Pour aller plus loin

- Geman, Bienenstock & Doursat (1992) — *Neural Networks and the Bias/Variance Dilemma*.
- ESL ch. 7.3 (décomposition biais-variance).
