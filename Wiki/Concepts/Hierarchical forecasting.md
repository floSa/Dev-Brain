---
galaxie: wiki
type: concept
nom: Hierarchical forecasting
alias: [Prévision hiérarchique, Réconciliation, Hierarchical reconciliation, MinT, bottom-up, top-down]
categorie: concept/ts
domaines: [data-sci, ml-eng]
tags: [forecasting, timeseries]
---

# Hierarchical forecasting

## Aperçu

- Prévoir un ensemble de séries liées par des contraintes d'agrégation : total → régions → magasins, ou produit × géographie. Les prévisions des niveaux doivent **s'additionner** (cohérence).
- Prévoir chaque niveau indépendamment donne des prévisions **incohérentes** (le total ≠ somme des parts). La **réconciliation** corrige cela et améliore souvent la précision à tous les niveaux.

## Concepts clés

### Hiérarchie & cohérence
- Les séries de base (feuilles) et leurs agrégats forment une structure décrite par une **matrice de sommation** $S$. Une prévision est *cohérente* si elle vit dans l'espace engendré par $S$ (les agrégats sont exactement les sommes des feuilles).

### Bottom-up
- Prévoir le niveau le plus fin, puis sommer vers le haut. Aucune perte d'information au bas, mais les feuilles sont bruitées → agrégats parfois instables.

### Top-down
- Prévoir le total (stable, lisse), puis le **désagréger** selon des proportions historiques ou prévues. Bon en haut, mais les proportions des feuilles sont difficiles à estimer.

### Middle-out
- Prévoir un niveau intermédiaire, agréger vers le haut et désagréger vers le bas. Compromis quand un niveau « métier » est le plus fiable.

### Réconciliation optimale (MinT)
- Projeter les prévisions de base (faites à *tous* les niveaux) sur l'espace cohérent en **minimisant la variance de l'erreur de réconciliation** (trace minimization). Généralise bottom-up/top-down ; OLS, WLS, ou MinT(shrink) selon l'estimation de la covariance des résidus.

### Hiérarchies groupées / croisées
- Quand les dimensions ne s'emboîtent pas strictement (géographie × catégorie), structures *grouped* — mêmes outils de réconciliation.

## Les maths, simplement

- Prévisions de base $\hat y$ (tous niveaux), réconciliées $\tilde y = S G \hat y$ où $G$ ramène vers les feuilles et $S$ ré-agrège. Cohérence garantie par construction.
- Bottom-up : $G=[\,0 \mid I\,]$ (ignore les agrégats). MinT : $G=(S^\top W^{-1} S)^{-1} S^\top W^{-1}$, avec $W$ la covariance des erreurs de base — exploite la corrélation entre niveaux.

## En pratique

- La cohérence n'est pas qu'esthétique : la planification l'exige (un budget régional = somme des budgets magasins).
- Réconcilier avec MinT(shrink) bat généralement bottom-up et top-down purs ; commencer par bottom-up comme baseline.
- Outils : `HierarchicalForecast` (Nixtla) pour la réconciliation, posée sur des modèles de base [[Dev/Services/statsforecast|statsforecast]] par nœud.

## Approches voisines & alternatives

- [[Forecasting framing]] — local vs global et le parc de séries, dont la hiérarchie est un cas structuré.
- [[Forecasting metrics]] — évaluer la précision à chaque niveau d'agrégation, pas seulement au total.
- [[ARIMA SARIMA]] / [[Exponential smoothing]] — modèles de base posés sur chaque nœud avant réconciliation.

## Pour aller plus loin

- Hyndman, Ahmed, Athanasopoulos & Shang (2011) — *Optimal combination forecasts for hierarchical time series*.
- Wickramasuriya, Athanasopoulos & Hyndman (2019) — réconciliation MinT (trace minimization).
- Hyndman & Athanasopoulos — FPP3, ch. 11 (forecasting hierarchical and grouped series).
