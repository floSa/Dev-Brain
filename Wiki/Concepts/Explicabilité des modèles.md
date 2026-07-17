---
galaxie: wiki
type: concept
nom: Explicabilité des modèles
alias: [explicabilité, interprétabilité, explainability, interpretability, feature importance, SHAP, LIME, permutation importance]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [explainability, supervised]
---

# Explicabilité des modèles

## Aperçu

- Comprendre **pourquoi** un modèle prédit ce qu'il prédit : quelles variables pèsent, dans quel sens, pour une prédiction donnée (local) ou en moyenne (global). Enjeu de confiance, de débogage, d'audit et de conformité.
- Distinguer **interprétable par nature** (modèle linéaire, arbre court, [[GAM]]) et **expliqué a posteriori** (post-hoc : on explique une boîte noire déjà entraînée).

## Concepts clés

### Local vs global
- **Local** : expliquer **une** prédiction (pourquoi ce client est refusé). [[Dev/Services/SHAP|SHAP]], [[Dev/Services/LIME|LIME]].
- **Global** : importance moyenne des variables sur tout le jeu. Permutation importance, MDI, agrégation des valeurs SHAP.

### Importance par permutation
- Mesure la **chute de performance** quand on permute aléatoirement une variable : si le score s'effondre, la variable comptait. **Model-agnostic**, mais coûteux et trompeur en présence de **corrélations** (importance diluée entre variables corrélées).

### MDI (impureté) & drop-column
- **MDI** : importance native des arbres ([[Arbres de décision]], [[Gradient Boosting (GBDT)]]) = réduction d'impureté cumulée. Rapide mais **biaisée** vers les variables à forte cardinalité.
- **Drop-column** : ré-entraîner sans la variable et mesurer l'écart. Le plus honnête, le plus cher.

### Boruta — importances vs variables-fantômes
- Méthode bâtie sur les importances d'une [[Random Forest]] : chaque variable est dupliquée en **ombre** (valeurs mélangées, donc décorrélées de la cible) ; une variable n'est **confirmée** que si son importance dépasse durablement la meilleure des ombres, sur de nombreux tirages.
- Vise **toutes les variables pertinentes** (et non le sous-ensemble minimal) : c'est le pont entre importance et [[Sélection de variables]].

### Attribution additive — Shapley
- Idée de théorie des jeux : répartir « équitablement » la prédiction entre les variables. [[Dev/Services/SHAP|SHAP]] en donne une version **cohérente** (les contributions somment à la prédiction).

### Surrogate local
- [[Dev/Services/LIME|LIME]] approxime localement la boîte noire par un **modèle simple** (linéaire) ajusté sur des perturbations autour du point.

## Les maths, simplement

- Valeur de Shapley d'une variable $i$ : $\phi_i = \sum_{S \subseteq F\setminus\{i\}} \dfrac{|S|!\,(|F|-|S|-1)!}{|F|!}\,\big[v(S\cup\{i\}) - v(S)\big]$ — contribution marginale moyenne de $i$ sur **toutes** les coalitions $S$ de variables. Garantit efficacité, symétrie, additivité.
- Importance par permutation : $\text{imp}_i = s_{\text{ref}} - \mathbb{E}\big[s_{\text{perm}(i)}\big]$, écart de score avant/après permutation de la colonne $i$.

## En pratique

- Modèles à arbres ([[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]]) → **TreeSHAP** exact et rapide ([[Dev/Services/SHAP|SHAP]]) plutôt que MDI biaisée.
- Boîte noire quelconque, explication d'un cas → [[Dev/Services/LIME|LIME]] ou KernelSHAP (plus lent).
- Importance **globale** robuste → permutation importance sur le jeu de validation (jamais le train).
- **Sélectionner** des variables à partir de ces importances (permutation, MDI, **Boruta**) → cf. [[Sélection de variables]].
- **Expliquer n'est pas expliquer causalement** : SHAP/LIME décrivent le modèle, pas le monde. La causalité relève d'un autre cadre (cf. [[Diff-in-Diff]]).
- Corrélations fortes → attributions instables ; en tenir compte avant de conclure.

## Approches voisines & alternatives

- [[Dev/Services/SHAP|SHAP]], [[Dev/Services/LIME|LIME]] — les deux bibliothèques post-hoc de référence.
- [[Dev/Services/interpreto|interpreto]] — le versant modèles de langage : attributions **et** méthodes à base de concepts (probes, dictionnaires appris), avec des métriques pour évaluer les explications elles-mêmes.
- [[Sélection de variables]] — les scores d'importance (permutation, MDI, **Boruta**) servent directement de critère de sélection.
- [[Ingénierie des caractéristiques]] — l'importance de variables guide la **sélection** de features.
- [[GAM]], [[GLM]] — modèles interprétables par construction, sans explication post-hoc.
- [[Data drift]] — suivre les explications en production aide à diagnostiquer une dérive.

## Pour aller plus loin

- Lundberg & Lee (2017) — *A Unified Approach to Interpreting Model Predictions* (SHAP).
- Ribeiro et al. (2016) — *"Why Should I Trust You?": Explaining the Predictions of Any Classifier* (LIME).
- Molnar — *Interpretable Machine Learning* (référence libre en ligne).
