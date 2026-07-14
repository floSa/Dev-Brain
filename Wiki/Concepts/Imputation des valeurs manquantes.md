---
galaxie: wiki
type: concept
nom: Imputation des valeurs manquantes
alias: [Imputation, Missing value imputation, Gestion des valeurs manquantes, MICE, KNN imputer]
categorie: concept/ml
domaines: [data-sci]
tags: [feature-engineering, missing-data]
---

# Imputation des valeurs manquantes

## Aperçu

- Remplacer les valeurs absentes par des valeurs plausibles, pour qu'un modèle qui n'accepte pas les `NaN` puisse s'entraîner.
- Du plus simple (médiane) au plus riche (imputation multiple), avec un compromis biais / variance / coût.

## Concepts clés

### Mécanisme du manque (MCAR / MAR / MNAR)
- **MCAR** : manque purement aléatoire, indépendant de tout. **MAR** : explicable par d'autres variables observées. **MNAR** : dépend de la valeur manquante elle-même (la plus délicate).
- Le mécanisme conditionne la validité de l'imputation : sous MNAR, même une bonne méthode biaise. Détail dans [[Mécanismes de données manquantes]].

### Imputation simple
- Constante par colonne : **médiane** (numérique, robuste aux outliers), moyenne, ou mode (catégoriel). Rapide, baseline. Sous-estime la variance et casse les corrélations entre variables.

### KNN
- `KNNImputer` : remplace par la moyenne (pondérée) des $k$ voisins les plus proches sur les variables observées. Capte les corrélations locales ; sensible à l'échelle (standardiser d'abord, cf. [[Mise à l'échelle]]) et coûteux.

### Imputation multiple (MICE)
- *Multiple Imputation by Chained Equations* : chaque variable à trous est régressée sur les autres, de façon itérative. Produit plusieurs jeux imputés → propage l'incertitude du manque au lieu de la masquer.
- Dans scikit-learn : `IterativeImputer` (encore expérimental, nécessite `enable_iterative_imputer`).

### Indicateur de manquant
- Ajouter une colonne binaire « était manquant » (`add_indicator`) : préserve l'information portée par l'absence elle-même, souvent prédictive.

## Les maths, simplement

- Imputation par médiane : $\hat{x}_{ij} = \mathrm{median}\{x_{kj} : x_{kj}\ \text{observé}\}$ — une constante par colonne $j$.
- MICE : on échantillonne itérativement $x_j \mid x_{-j}$ via un modèle (souvent linéaire) jusqu'à stabilisation, répété pour obtenir $m$ jeux complétés.

## En pratique

- Imputer **dans le pipeline** : `fit` les statistiques (médiane, modèle) sur le train seul, sinon fuite (cf. [[Ingénierie des caractéristiques]]).
- Médiane > moyenne en présence d'outliers ; garder l'`add_indicator` quand le manque est informatif.
- KNN / MICE plus fidèles mais plus coûteux et sensibles ; mesurer l'impact réel sur le score aval avant de complexifier.
- Les arbres boostés (XGBoost, LightGBM) gèrent nativement les `NaN` — l'imputation devient parfois superflue.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.impute]] (`SimpleImputer`, `KNNImputer`, `IterativeImputer`).

## Approches voisines & alternatives

- [[Mécanismes de données manquantes]] — le **pourquoi** du manque (MCAR/MAR/MNAR) ; décide quelle méthode reste non biaisée.
- [[Ingénierie des caractéristiques]] — l'étape englobante.
- [[Mise à l'échelle]] — à appliquer avant le KNN (méthode à distance).
- [[Encodage des variables catégorielles]] — gérer les modalités manquantes selon le cas.

## Pour aller plus loin

- van Buuren — *Flexible Imputation of Missing Data* (référence MICE).
- Documentation scikit-learn — *Imputation of missing values*.
