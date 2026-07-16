---
galaxie: wiki
type: concept
nom: Random Forest
alias: [RF, Forêts aléatoires, Random forests, Forêt aléatoire]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, tree-based, ensemble, bagging]
---

# Random Forest

## Aperçu

- Ensemble supervisé : agrège de nombreux [[Arbres de décision]] entraînés indépendamment, puis moyenne (régression) ou vote (classification).
- Réduit drastiquement la variance d'un arbre seul tout en gardant un réglage facile. Robuste, peu sensible aux hyperparamètres, bonne baseline tabulaire.

## Concepts clés

### Bagging
- *Bootstrap aggregating* ([[Bagging]]) : chaque arbre est entraîné sur un rééchantillon avec remise du jeu de données. Des arbres légèrement différents, agrégés, lissent les erreurs individuelles.

### Décorrélation par sous-échantillonnage des variables
- À chaque découpage, l'arbre ne considère qu'un sous-ensemble aléatoire de variables ($\sqrt{p}$ en classification typiquement). Empêche les arbres de tous se ressembler — c'est ce qui distingue Random Forest d'un simple bagging d'arbres.

### Arbres indépendants & profonds
- Les arbres sont construits en parallèle, sans interaction, et souvent peu élagués. La variance individuelle est élevée mais s'annule par moyenne.

### Les hyperparamètres, et à quoi ils servent

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `n_estimators` | Nombre d'arbres | ↑ = toujours mieux, puis plafonne. **Ne surapprend pas** : c'est une moyenne, pas une capacité. Le seul coût est le temps |
| `max_features` | Variables tirées à chaque nœud | **Le vrai levier.** ↓ = arbres plus décorrélés, moins de variance, plus de biais. Défaut : $\sqrt{d}$ en classification, $d/3$ en régression |
| `max_depth` | Profondeur maximale | Laissé **libre** par défaut, contrairement au [[Gradient Boosting (GBDT)|boosting]] : ici les arbres doivent être forts, la moyenne s'occupe de la variance |
| `min_samples_leaf` | Effectif minimal d'une feuille | ↑ = lisse le modèle. Le frein utile si les arbres libres surapprennent le bruit |
| `bootstrap` | Rééchantillonnage avec remise | `True` par défaut ; c'est lui qui rend l'OOB possible |
| `class_weight` | Poids des classes | `balanced` sur classes rares, avant de songer au rééchantillonnage ([[Imbalanced classification]]) |
| `n_jobs` | Parallélisme | `-1` : les arbres sont indépendants, la parallélisation est gratuite |

- **`max_features` est le seul paramètre qui mérite vraiment une recherche.** Le reste tient à des valeurs par défaut correctes — c'est la raison de la réputation « ça marche sans réglage » du modèle.
- Curseur à retenir : `max_features` bas → arbres très différents les uns des autres → la moyenne réduit fort la variance. `max_features = d` → tous les arbres se ressemblent et la forêt dégénère vers un [[Bagging|bagging]] ordinaire.

### Out-of-bag (OOB)
- Chaque observation est absente d'environ 1/3 des rééchantillons → erreur OOB = validation quasi gratuite, sans jeu de test séparé.

## Les maths, simplement

- Moyenne de $B$ prédicteurs i.i.d. de variance $\sigma^2$ et corrélation $\rho$ : variance résultante $\rho\sigma^2 + \frac{1-\rho}{B}\sigma^2$. Augmenter $B$ écrase le second terme ; **réduire $\rho$** (sous-échantillonnage des variables) écrase le premier.
- D'où la double aléa : rééchantillonnage des lignes (bagging) **et** des colonnes (décorrélation).

## En pratique

- Peu de réglage : `n_estimators` (plus = mieux, plafonne), `max_features` (le levier de décorrélation), `max_depth` souvent laissé libre.
- Parallélisable trivialement (arbres indépendants). Inférence plus lourde qu'un arbre seul.
- Moins performant que le [[Gradient Boosting (GBDT)|Gradient Boosting]] sur cible difficile, mais plus simple à régler et plus robuste au surapprentissage.
- Perd la lisibilité de l'arbre unique : on retombe sur l'importance des variables (impureté ou permutation) pour interpréter.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.ensemble.RandomForestClassifier / RandomForestRegressor]].

## Approches voisines & alternatives

- [[Arbres de décision]] — l'apprenant de base ; Random Forest = son ensemble par bagging.
- [[Gradient Boosting (GBDT)|Gradient Boosting]] — l'autre grande famille d'ensembles d'arbres : séquentiel (réduit le biais) là où Random Forest est parallèle (réduit la variance).
- [[Isolation Forest]] — même brique d'arbres, mais non supervisée et à coupes aléatoires : isoler les anomalies plutôt que prédire.
- [[Types de données et choix de modèle]] — ce que Random Forest exige de la donnée, et quand lui préférer autre chose.

## Pour aller plus loin

- Breiman (2001) — *Random Forests*.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 15.
