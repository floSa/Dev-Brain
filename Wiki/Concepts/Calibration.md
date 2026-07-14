---
galaxie: wiki
type: concept
nom: Calibration
alias: [Calibration des probabilités, fiabilité, diagramme de fiabilité, reliability diagram, Platt scaling, régression isotonique, temperature scaling, ECE, Expected Calibration Error]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [model-evaluation, calibration, classification]
---

# Calibration

## Aperçu

- Un modèle est **calibré** si ses probabilités prédites correspondent aux fréquences observées : parmi les cas annoncés à 0,8, environ 80 % sont effectivement positifs.
- À distinguer du pouvoir de **discrimination** (savoir classer/séparer) : un modèle peut très bien ordonner (AUC élevée) tout en produisant des probabilités fausses.

## Concepts clés

### Discrimination vs calibration
- Discrimination = capacité à ordonner les exemples ([[ROC-AUC & courbe PR]]). Calibration = justesse des probabilités. Indépendantes : optimiser l'une ne garantit pas l'autre.

### Diagramme de fiabilité
- Regrouper les prédictions par bac de probabilité, tracer fréquence observée vs probabilité moyenne prédite. La diagonale = calibration parfaite ; au-dessus = sous-confiance, en dessous = sur-confiance.

### ECE (Expected Calibration Error)
- Écart moyen pondéré entre confiance prédite et exactitude observée, bac par bac. Résume le diagramme en un scalaire (sensible au choix du binning).

### Recalibrage post-hoc
- **Platt scaling** (sigmoïde ajustée sur un jeu de calibration), **régression isotonique** (monotone, non paramétrique, plus flexible mais gourmande en données), **temperature scaling** (réseaux profonds). Toujours sur un **jeu dédié**, jamais celui d'entraînement.

### Sources de mauvaise calibration
- Réseaux profonds modernes souvent sur-confiants ; marges de SVM et scores de boosting déformés ; le rééquilibrage des classes décale les probabilités.

## Les maths, simplement

- Calibration parfaite : $\Pr(Y=1\mid \hat p = p)=p$ pour tout $p$.
- $\text{ECE}=\sum_{m=1}^{M}\dfrac{|B_m|}{n}\,\big|\,\text{acc}(B_m)-\text{conf}(B_m)\,\big|$, où $B_m$ est le $m$-ième bac de probabilité.
- Le score de Brier se décompose en fiabilité (calibration) − résolution (discrimination) + incertitude : une même valeur mêle donc les deux aspects.

## En pratique

- Indispensable quand la **probabilité elle-même** sert : décision sous coût, seuil métier, fusion de scores, estimation de risque — pas seulement le classement.
- Protocole : mesurer (diagramme + ECE) → recalibrer (Platt / isotonique) sur un jeu réservé → revérifier.
- La [[Régression logistique]] est souvent bien calibrée d'emblée (elle optimise directement la log-vraisemblance) ; ce n'est pas le cas des marges de SVM ni des scores bruts de boosting.
- Les métriques de probabilité de [[Classification metrics]] (log-loss, Brier) pénalisent déjà en partie une mauvaise calibration.
- Outils : [[Dev/Services/Scikit-Learn|sklearn — CalibratedClassifierCV, calibration_curve, brier_score_loss]].

## Approches voisines & alternatives

- [[ROC-AUC & courbe PR]] — mesure la discrimination, **aveugle** à la calibration (l'AUC est invariante à toute transformation monotone des scores).
- [[Classification metrics]] — log-loss et Brier, métriques propres sensibles à la calibration.
- [[Régression logistique]] — exemple type de modèle naturellement calibré.
- [[Validation croisée]] — recalibrer dans les plis pour éviter la fuite d'information.

## Pour aller plus loin

- Niculescu-Mizil & Caruana (2005) — *Predicting good probabilities with supervised learning*.
- Guo et al. (2017) — *On Calibration of Modern Neural Networks* (temperature scaling).
