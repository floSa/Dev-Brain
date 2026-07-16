---
galaxie: wiki
type: concept
nom: Mise à l'échelle
alias: [Normalisation, Standardisation, Feature scaling, Scaling, StandardScaler, MinMaxScaler, RobustScaler]
categorie: concept/ml
domaines: [data-sci]
tags: [feature-engineering]
---

# Mise à l'échelle

## Aperçu

- Ramener les variables numériques à des amplitudes comparables, pour qu'aucune ne domine par sa seule unité.
- Indispensable aux modèles à distance, à gradient ou régularisés ; inutile aux arbres.

## Concepts clés

### Standardisation (StandardScaler)
- Centre-réduit : moyenne 0, écart-type 1 (*z-score*). Choix par défaut. Suppose une dispersion à peu près régulière ; sensible aux outliers.

### Normalisation min-max (MinMaxScaler)
- Ramène à un intervalle borné $[0, 1]$. Utile quand des bornes sont attendues (pixels d'image, entrées de réseau de neurones). Très sensible aux valeurs extrêmes, qui écrasent le reste.

### RobustScaler
- Centre sur la médiane, divise par l'écart interquartile (IQR). Robuste aux outliers — à préférer quand la distribution a des queues lourdes.

### Normalisation vs standardisation
- « Normaliser » = borner l'échelle (min-max) ; « standardiser » = centrer-réduire. Vocabulaire souvent confondu — préciser laquelle des deux.

## Les maths, simplement

- Standardisation : $z = \dfrac{x - \mu}{\sigma}$ ($\mu$ moyenne, $\sigma$ écart-type).
- Min-max : $x' = \dfrac{x - x_{\min}}{x_{\max} - x_{\min}}$.
- Robuste : $x' = \dfrac{x - \mathrm{med}(x)}{\mathrm{IQR}(x)}$.

## En pratique

- **Requis** : k-NN, SVM, [[K-Means]], [[PCA]], régression régularisée, réseaux de neurones — tout ce qui repose sur des distances, des gradients ou une pénalité.
- **Inutile** : arbres et ensembles d'arbres (invariants à toute transformation monotone par variable).
- `fit` sur le train uniquement (sinon fuite, cf. [[Ingénierie des caractéristiques]]), `transform` le test avec les mêmes paramètres.
- Outliers marqués → RobustScaler ; bornes nécessaires → MinMax ; sinon Standard.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.preprocessing]] (`StandardScaler`, `MinMaxScaler`, `RobustScaler`).

## Approches voisines & alternatives

- [[Ingénierie des caractéristiques]] — l'étape englobante.
- [[Régularisation]] — la pénalité dépend de l'échelle, standardiser d'abord.
- [[Clustering]], [[K-Means]] — méthodes à distance, échelle déterminante.
- [[SVM]], [[k-NN]] — les deux modèles supervisés où l'oubli de standardisation est l'erreur n°1.
- [[Types de données et choix de modèle]] — quels modèles l'exigent, lesquels s'en passent (les arbres).
- [[PCA]] — l'ACP doit être précédée d'une standardisation.

## Pour aller plus loin

- Documentation scikit-learn — *Preprocessing data : standardization, scaling*.
- Galerie scikit-learn — *Compare the effect of different scalers on data with outliers*.
