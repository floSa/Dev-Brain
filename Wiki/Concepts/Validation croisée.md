---
galaxie: wiki
type: concept
nom: Validation croisée
alias: [Cross-validation, K-Fold, Validation croisée stratifiée, TimeSeriesSplit, CV]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [model-evaluation, resampling, supervised]
---

# Validation croisée

## Aperçu

- Estime la performance de **généralisation** d'un modèle en le réentraînant sur plusieurs découpages entraînement/test du même jeu de données.
- Réutilise chaque observation tour à tour en test → estimation plus stable et moins gaspilleuse qu'un unique *train/test split*.

## Concepts clés

### K-Fold
- Partitionne les données en $K$ plis. Pour chaque pli : entraîner sur $K-1$ plis, évaluer sur le pli restant. Score final = moyenne des $K$ scores. $K=5$ ou $10$ par défaut.

### Stratifiée
- K-Fold qui préserve la proportion des classes dans chaque pli. Indispensable en [[ROC-AUC & courbe PR|classification]] déséquilibrée, sinon un pli peut manquer une classe rare.

### TimeSeriesSplit
- Pour les séries temporelles : le test est **toujours postérieur** à l'entraînement (fenêtre glissante ou extensible). Interdit d'entraîner sur le futur — un K-Fold classique fuiterait l'information temporelle.

### Leave-One-Out (LOO)
- Cas extrême $K=n$ : un seul point en test à chaque fois. Quasi sans biais mais coûteux et à forte variance ; réservé aux petits jeux.

### CV imbriquée
- Boucle externe pour estimer la performance, boucle interne pour régler les hyperparamètres. Évite le biais optimiste quand on fait de la [[Optimisation d'hyperparamètres|sélection de modèle]] et qu'on évalue sur les mêmes plis.

## Les maths, simplement

- Estimateur de performance : $\widehat{\text{CV}} = \dfrac{1}{K}\sum_{k=1}^{K} L\big(\text{modèle entraîné sans le pli }k,\ \text{pli }k\big)$.
- L'écart-type des scores de plis renseigne sur la **stabilité** de l'estimation, pas sur l'incertitude de la vraie erreur (les plis ne sont pas indépendants).
- Compromis classique : $K$ petit → biais élevé / variance faible ; $K$ grand → biais faible / variance élevée. Lien direct avec le [[Compromis biais-variance]].

## En pratique

- **Fuite de données** : toute transformation apprise (imputation, [[Mise à l'échelle|mise à l'échelle]], encodage) doit être ajustée *dans* chaque pli, pas avant. → mettre le `Pipeline` complet dans la CV.
- Le rééchantillonnage avec remise du [[Bootstrap]] est le cousin de la CV pour estimer la distribution d'une métrique ; la CV, elle, partitionne sans remise.
- Reproductibilité : fixer la graine (`random_state`) pour comparer des modèles sur les mêmes plis.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.model_selection — cross_val_score, KFold, StratifiedKFold, TimeSeriesSplit]].

## Approches voisines & alternatives

- [[Walk-forward CV]] — la déclinaison temporelle (TimeSeriesSplit en détail) : origine de prévision glissante, jamais d'entraînement sur le futur.
- [[Optimisation d'hyperparamètres]] — consomme la CV comme fonction de score pour comparer des configurations.
- [[Compromis biais-variance]] — la CV mesure l'écart de généralisation que ce compromis décrit.
- [[ROC-AUC & courbe PR]] — les métriques agrégées sur les plis de CV.
- [[Classification metrics]] / [[Regression metrics]] / [[Clustering evaluation]] — les scores agrégés sur les plis, selon la nature de la tâche.
- [[Bootstrap]] — autre technique de rééchantillonnage, avec remise, pour l'incertitude d'une statistique.

## Pour aller plus loin

- Stone (1974) — *Cross-Validatory Choice and Assessment of Statistical Predictions*.
- ESL ch. 7.10 (cross-validation, le bon usage et les pièges de fuite).
