---
galaxie: wiki
type: concept
nom: Arbres de décision
alias: [Decision tree, Arbre de décision, CART]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, tree-based, classification, regression]
---

# Arbres de décision

## Aperçu

- Modèle supervisé non paramétrique : segmente l'espace des variables par une suite de tests binaires, jusqu'à des feuilles qui portent une prédiction.
- Lisible (chaque chemin racine→feuille = une règle), gère sans préparation le mélange numérique/catégoriel et les non-linéarités. Brique de base du [[Random Forest]] et du [[Gradient Boosting (GBDT)|Gradient Boosting]].

## Concepts clés

### Structure
- Nœud interne = un test sur une variable (`x_j < seuil`) ; deux branches ; feuille = prédiction (classe majoritaire ou moyenne de la cible).

### Apprentissage glouton
- Construction descendante : à chaque nœud, choisir le découpage qui réduit le plus l'impureté des enfants. Aucun retour en arrière.

### Critères d'impureté
- **Classification** : Gini ou entropie — mesurent l'hétérogénéité des classes dans un nœud.
- **Régression** : variance / erreur quadratique des valeurs de la feuille.

### Régularisation
- Un arbre profond mémorise le bruit (surapprentissage). On contrôle via `max_depth`, `min_samples_leaf`, ou élagage (cost-complexity pruning, paramètre $\alpha$).

## Les maths, simplement

- Impureté de Gini d'un nœud : $G = \sum_{k} p_k (1 - p_k) = 1 - \sum_k p_k^2$, où $p_k$ = proportion de la classe $k$. Nulle quand le nœud est pur.
- Entropie : $H = -\sum_k p_k \log_2 p_k$. Même esprit que Gini, dérivée plus coûteuse.
- Découpage choisi : celui qui maximise la **réduction d'impureté** $\Delta = I(\text{parent}) - \sum_{\text{enfants}} \frac{n_{\text{enfant}}}{n} I(\text{enfant})$.

## En pratique

- Sans contrainte de profondeur, un arbre atteint 0 d'erreur d'entraînement mais généralise mal — toujours borner la profondeur ou élaguer.
- Forte variance : un petit changement de données peut redessiner l'arbre. C'est ce que corrigent les ensembles ([[Random Forest]], [[Gradient Boosting (GBDT)|Gradient Boosting]]).
- Pas besoin de standardiser ni d'encoder en one-hot (les seuils sont invariants par transformation monotone).
- L'importance des variables (réduction d'impureté cumulée) est biaisée vers les variables à forte cardinalité — la lire avec prudence.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.tree.DecisionTreeClassifier / DecisionTreeRegressor]].
- Implémentations d'ensembles d'arbres en pratique : [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/CatBoost|CatBoost]] (boosting), au-dessus de cette même brique.

## Approches voisines & alternatives

- [[Random Forest]] — moyenne de nombreux arbres décorrélés ([[Bagging|bagging]]) ; réduit la variance au prix de la lisibilité.
- [[Gradient Boosting (GBDT)|Gradient Boosting]] — arbres construits séquentiellement ([[Boosting|boosting]]) pour corriger les erreurs résiduelles ; souvent le meilleur en performance sur données tabulaires.
- [[Régression logistique]] / [[Régression linéaire]] — alternatives linéaires, plus stables et interprétables quand la frontière est lisse.
- [[SVM]] — frontière à marge maximale : lisse et globale, là où l'arbre découpe en escaliers orthogonaux aux axes.
- [[k-NN]] — l'autre non-paramétrique, mais à distance : exige de standardiser, ce dont l'arbre se dispense.
- [[Isolation Forest]] — la même brique d'arbre retournée vers le non supervisé : isoler l'anormal au lieu de prédire.
- [[Classification]] / [[Régression]] — les deux tâches que l'arbre sert indifféremment.
- [[Types de données et choix de modèle]] — pourquoi l'arbre se passe de standardisation et n'extrapole pas.

## Pour aller plus loin

- Breiman, Friedman, Olshen, Stone (1984) — *Classification and Regression Trees* (CART).
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 9.
