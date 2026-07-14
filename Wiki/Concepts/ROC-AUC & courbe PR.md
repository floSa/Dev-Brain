---
galaxie: wiki
type: concept
nom: ROC-AUC / courbe PR
alias: [ROC, AUC, courbe ROC, courbe PR, precision-recall, AUC-ROC, AUC-PR, ROC-AUC]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [model-evaluation, classification, supervised]
---

# ROC-AUC / courbe PR

## Aperçu

- Évaluent un classifieur **probabiliste** sur tous les seuils de décision à la fois, sans figer une frontière unique.
- ROC trace sensibilité vs taux de faux positifs ; la courbe précision-rappel trace précision vs sensibilité — plus parlante quand le positif est rare.

## Concepts clés

### Matrice de confusion & seuil
- Un score continu devient une décision par seuillage. Chaque seuil donne (VP, FP, VN, FN) → un point de courbe. Faire varier le seuil balaie la courbe entière.

### Courbe ROC & AUC
- Axe Y = sensibilité (TPR), axe X = taux de faux positifs (FPR). L'aire sous la courbe (**AUC**) résume la séparation des classes.
- Interprétation probabiliste : AUC = probabilité qu'un positif tiré au hasard ait un score supérieur à un négatif tiré au hasard. $0{,}5$ = hasard, $1$ = parfait.

### Courbe précision-rappel
- Axe Y = précision, axe X = rappel (= sensibilité). La ligne de base n'est pas $0{,}5$ mais la **prévalence** du positif.
- Sous fort déséquilibre, la ROC reste flatteuse (le grand nombre de négatifs écrase le FPR) alors que la PR révèle l'effondrement de la précision. → préférer PR quand le positif est rare et coûteux (fraude, maladie).

### Choix du seuil
- AUC mesure le classement, pas la décision. Pour agir, fixer un seuil selon le coût relatif FP/FN (ou viser un point précision/rappel cible).

## Les maths, simplement

- $\text{TPR} = \dfrac{VP}{VP+FN}$ (sensibilité, rappel) ; $\text{FPR} = \dfrac{FP}{FP+VN}$ ; $\text{précision} = \dfrac{VP}{VP+FP}$.
- $\text{AUC-ROC} = \Pr\big(\text{score}(x^+) > \text{score}(x^-)\big)$ — équivalente à la statistique de Mann-Whitney.
- AUC-PR (average precision) $= \sum_n (R_n - R_{n-1})\,P_n$ — moyenne des précisions pondérée par le gain de rappel.

## En pratique

- Modèle non calibré → le **classement** (donc l'AUC) peut être bon même si les probabilités sont fausses ; recalibrer (Platt, isotonique) si on a besoin de vraies probabilités → [[Calibration]].
- Toujours rapporter la métrique **agrégée sur les plis** de [[Validation croisée]], pas sur un unique split.
- La [[Régression logistique]] produit directement les probabilités qui alimentent ces courbes ; tout modèle exposant un `predict_proba` ou un score le permet.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.metrics — roc_auc_score, average_precision_score, RocCurveDisplay, PrecisionRecallDisplay]].

## Approches voisines & alternatives

- [[Validation croisée]] — le cadre qui produit des estimations fiables de ces métriques.
- [[Régression logistique]] — fournit les scores de probabilité seuillés par les courbes.
- [[Classification metrics]] — F1, exactitude, log-loss, Brier : métriques à seuil fixé (résumé en un point vs courbe complète).
- [[Calibration]] — justesse des probabilités, complémentaire de la discrimination que mesure l'AUC.
- [[Ranking metrics]] — l'AUC-ROC est une métrique de rang ; NDCG/MAP/MRR généralisent à l'ordonnancement de listes.

## Pour aller plus loin

- Fawcett (2006) — *An Introduction to ROC Analysis*.
- Saito & Rehmsmeier (2015) — pourquoi la courbe PR est plus informative que la ROC en déséquilibre.
