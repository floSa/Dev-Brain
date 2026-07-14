---
galaxie: wiki
type: concept
nom: Sélection de variables
alias: [Feature selection, Sélection de caractéristiques, Sélection d'attributs, RFE, SelectKBest]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [feature-engineering]
---

# Sélection de variables

## Aperçu

- Garder un sous-ensemble des variables existantes, sans les transformer, pour réduire le surapprentissage et le coût et améliorer l'interprétabilité.
- À distinguer de l'**extraction** ([[PCA]]), qui crée de nouvelles variables au lieu d'en conserver.

## Concepts clés

### Filtrage (filter)
- Score univarié indépendant du modèle : ANOVA-F, chi², information mutuelle, corrélation, `VarianceThreshold`. Rapide et scalable ; ignore les interactions entre variables.
- Outil sklearn : `SelectKBest`, `SelectPercentile`.

### Wrapper
- Entoure un modèle et évalue des sous-ensembles par la performance : élimination récursive `RFE` / `RFECV`, sélection séquentielle. Précis mais coûteux (réentraînements multiples).
- Variante par **importances** : **Boruta** confronte chaque variable à des copies « ombres » mélangées sur une [[Random Forest]] et garde celles qui les dépassent — sélection « toutes variables pertinentes » (cf. [[Explicabilité des modèles]]).

### Intégré (embedded)
- La sélection se fait *pendant* l'entraînement : le Lasso L1 ([[Régularisation]]) annule des coefficients ; les importances des [[Arbres de décision|arbres]] et [[Random Forest]] hiérarchisent les variables. Récupéré via `SelectFromModel`.
- Bon compromis coût / qualité : un seul entraînement.

### Sélection ≠ extraction
- Sélection : conserve des variables d'origine, donc interprétables. Extraction : combine en axes latents → [[Réduction de dimension]], [[PCA]].

## Les maths, simplement

- Filtrage ANOVA-F : score $F$ comparant la variance inter-classes à la variance intra-classe, pour chaque variable prise isolément.
- Intégré L1 : la pénalité $\lambda\lVert\beta\rVert_1$ pousse des coefficients exactement à $0$ → sélection automatique (cf. [[Régularisation]]).

## En pratique

- Filtrage en premier tri rapide (haute dimension) ; wrapper si le budget calcul le permet ; intégré comme défaut pragmatique.
- Faire la sélection **dans la validation croisée** (sur le train de chaque pli) — sinon fuite et score optimiste (cf. [[Ingénierie des caractéristiques]]).
- Variables corrélées : le filtrage univarié les garde toutes ; préférer L1 / embedded pour dédupliquer.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.feature_selection]] (`SelectKBest`, `RFE`, `RFECV`, `SelectFromModel`, `VarianceThreshold`).

## Approches voisines & alternatives

- [[Ingénierie des caractéristiques]] — l'étape englobante.
- [[Régularisation]] — Lasso L1, sélection intégrée par pénalité.
- [[Random Forest]], [[Arbres de décision]] — importances comme critère de sélection.
- [[Explicabilité des modèles]] — permutation importance, MDI et **Boruta** produisent les scores d'importance exploités ici.
- [[Réduction de dimension]], [[PCA]] — extraction, alternative à la sélection.

## Pour aller plus loin

- Guyon & Elisseeff (2003) — *An Introduction to Variable and Feature Selection*.
- Documentation scikit-learn — *Feature selection*.
