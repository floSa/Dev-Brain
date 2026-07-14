---
galaxie: wiki
type: concept
nom: Régression et classification multi-sorties
alias: [multi-output, multioutput, multi-sorties, multi-target, multi-label, MultiOutputRegressor, MultiOutputClassifier, RegressorChain, ClassifierChain]
categorie: concept/ml
domaines: [data-sci]
tags: [regression, classification, multi-output, supervised]
---

# Régression et classification multi-sorties

## Aperçu

- Prédire **plusieurs cibles à la fois** à partir des mêmes variables : régression multi-cibles (sorties continues) ou classification multi-étiquettes / multi-sorties (sorties catégorielles).
- Deux questions tranchent la stratégie : les cibles sont-elles **corrélées** ? l'estimateur gère-t-il **nativement** plusieurs sorties ?

## Concepts clés

### Ne pas confondre
- **Multi-classe** : une seule cible, plus de deux classes mutuellement exclusives.
- **Multi-étiquette** (multi-label) : plusieurs étiquettes binaires possibles **simultanément** (un texte « politique » *et* « économie »).
- **Multi-sorties** (multi-output) : plusieurs cibles, continues ou catégorielles, prédites ensemble.

### Stratégie 1 — un modèle indépendant par cible
- `MultiOutputRegressor` / `MultiOutputClassifier` clonent un estimateur mono-sortie, un par cible.
- Simple, parallélisable. Mais **ignore les corrélations** entre cibles.

### Stratégie 2 — chaînes
- `RegressorChain` / `ClassifierChain` : chaque modèle prédit une cible en utilisant **les prédictions des précédentes** comme variables d'entrée → capte les dépendances entre cibles.
- L'**ordre** de la chaîne influe ; un ensemble de chaînes (ECC, ordres aléatoires moyennés) stabilise le résultat.

### Stratégie 3 — modèles nativement multi-sorties
- Arbres et [[Random Forest]], k-NN, réseaux de neurones (couche de sortie à $m$ unités), `Ridge` : acceptent directement une cible vectorielle, sans wrapper.

## Les maths, simplement

- Cible vectorielle $Y \in \mathbb{R}^{n \times m}$ ($m$ sorties). Approche indépendante : minimise séparément $\sum_k \mathcal{L}(y_k, f_k(x))$.
- Chaîne : $f_k(x, y_1, \dots, y_{k-1})$ — factorise $P(y \mid x) = \prod_k P(y_k \mid x, y_{<k})$, ce que les modèles indépendants supposent factorisé en $\prod_k P(y_k \mid x)$.

## En pratique

- Cibles indépendantes (ou gain nul mesuré) → un modèle par cible, plus simple à entraîner et débuguer.
- Cibles corrélées → chaînes ou modèle natif ; comparer au baseline indépendant avant de complexifier.
- Évaluer **par cible** puis agréger (macro / micro), cf. [[Regression metrics]] et [[Classification metrics]].
- Multi-étiquette à classes rares → cf. [[Imbalanced classification]] (étiquettes déséquilibrées).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.multioutput]] (`MultiOutputRegressor`, `MultiOutputClassifier`, `RegressorChain`, `ClassifierChain`).

## Approches voisines & alternatives

- [[Régression linéaire]], [[Régression logistique]] — les estimateurs mono-sortie que l'on étend par wrapper.
- [[Random Forest]] — nativement multi-sorties, sans wrapper.
- [[Regression metrics]], [[Classification metrics]] — l'évaluation, à agréger sur les cibles.
- [[Imbalanced classification]] — fréquent en multi-étiquette.

## Pour aller plus loin

- Read et al. (2011) — *Classifier Chains for Multi-label Classification*.
- Documentation scikit-learn — *Multiclass and multioutput algorithms*.
