---
galaxie: wiki
type: concept
nom: Classification metrics
alias: [Métriques de classification, exactitude, accuracy, précision, rappel, F1, F1-score, log-loss, matrice de confusion, sensibilité, spécificité, taux de vrais négatifs, VPP, VPN, valeur prédictive positive, valeur prédictive négative, prévalence, rapport de vraisemblance, MCC, Brier]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [model-evaluation, classification, supervised]
---

# Classification metrics

## Aperçu

- Mesurent la qualité d'un classifieur en confrontant prédictions et vérité terrain, **à seuil fixé** — par opposition aux courbes [[ROC-AUC & courbe PR]] qui balaient tous les seuils.
- Toutes dérivent de la matrice de confusion ; le bon choix dépend du coût relatif des erreurs et du déséquilibre des classes.

## Concepts clés

### Matrice de confusion
- Croise prédictions et réalité : vrais positifs (VP), faux positifs (FP), vrais négatifs (VN), faux négatifs (FN). Socle de toutes les métriques seuillées.

### Exactitude (accuracy)
- Part de prédictions correctes. Simple mais **trompeuse en déséquilibre** : prédire toujours la classe majoritaire peut afficher 99 % sans rien apprendre.

### Précision, rappel, F1
- Précision = parmi les prédits positifs, lesquels le sont vraiment. Rappel (sensibilité) = parmi les positifs réels, lesquels sont retrouvés. F1 = moyenne harmonique des deux. Le seuil arbitre le compromis précision/rappel.

### Spécificité & valeurs prédictives
- **Spécificité** (taux de vrais négatifs) = parmi les négatifs réels, lesquels sont correctement écartés : $VN/(VN+FP)$. Pendant « classe négative » du rappel ; une forte spécificité = peu de fausses alertes. Sensibilité/spécificité caractérisent le **test**, indépendamment de la fréquence des cas.
- **VPP** (= précision) et **VPN** = fiabilité d'une prédiction positive / négative. Contrairement à sensibilité et spécificité, elles **dépendent de la prévalence** : à test identique, une classe positive plus rare fait chuter la VPP. Piège classique du dépistage en population saine.
- **Rapports de vraisemblance** : $LR^+=\text{sensibilité}/(1-\text{spécificité})$, $LR^-=(1-\text{sensibilité})/\text{spécificité}$. Indépendants de la prévalence, ils condensent les deux métriques et transforment une probabilité pré-test en post-test (cote post = cote pré × LR) → [[Inférence bayésienne]].

### Métriques sur les probabilités
- Log-loss et score de Brier notent les **probabilités**, pas la décision binaire. La log-loss pénalise lourdement une confiance erronée. Lien direct avec la [[Calibration]].

### Multiclasse : macro / micro / weighted
- Moyennage des scores par classe. **Macro** = à égalité (révèle les classes rares), **micro** = pondéré par effectif (≈ exactitude en mono-label), **weighted** = pondéré par le support.

## Les maths, simplement

- $P=\dfrac{VP}{VP+FP}$, $R=\dfrac{VP}{VP+FN}$, $F_1=\dfrac{2PR}{P+R}$ ; $F_\beta=(1+\beta^2)\dfrac{PR}{\beta^2 P+R}$ ($\beta>1$ privilégie le rappel).
- Spécificité $=\dfrac{VN}{VN+FP}$ ; VPP $=\dfrac{VP}{VP+FP}$ (= précision) ; VPN $=\dfrac{VN}{VN+FN}$ — les deux dernières varient avec la prévalence, pas les deux premières.
- Log-loss $=-\dfrac{1}{n}\sum_i\sum_c y_{ic}\log\hat p_{ic}$ ; Brier (binaire) $=\dfrac{1}{n}\sum_i(\hat p_i-y_i)^2$.
- MCC (coefficient de Matthews) $\in[-1,1]$ : corrélation prédiction/réalité utilisant les quatre cases, robuste au déséquilibre.

## En pratique

- **Déséquilibre** : abandonner l'exactitude → F1, rappel à précision fixée, MCC, ou les courbes [[ROC-AUC & courbe PR]] (PR en priorité quand le positif est rare).
- Choisir selon le coût métier : le rappel prime quand un FN est grave (dépistage), la précision quand un FP coûte (filtre anti-spam).
- Sur une classe positive rare, une VPP correcte exige une **spécificité** quasi parfaite : le grand nombre de négatifs domine les FP. Rapporter sensibilité/spécificité sans la prévalence ne dit rien de la fiabilité réelle d'une prédiction.
- Rapporter la métrique **agrégée sur les plis** de [[Validation croisée]], jamais sur un unique split.
- Les métriques de probabilité (log-loss, Brier) supposent un modèle bien calibré → vérifier la [[Calibration]].
- Outils : [[Dev/Services/Scikit-Learn|sklearn.metrics — classification_report, f1_score, log_loss, matthews_corrcoef, confusion_matrix]].

## Approches voisines & alternatives

- [[Classification]] — le chapeau de la tâche dont ces métriques mesurent le résultat.
- [[ROC-AUC & courbe PR]] — évaluation indépendante du seuil (toutes les décisions à la fois) vs résumé à un seuil fixé.
- [[Calibration]] — justesse des probabilités prédites, complémentaire des métriques de décision.
- [[Ranking metrics]] — quand seul l'ordre des prédictions compte ; Precision@k/Recall@k en transposent l'esprit à une liste.
- [[Inférence bayésienne]] — les rapports de vraisemblance y transposent la mise à jour pré/post-test (cote × LR) : lecture diagnostique de sensibilité et spécificité.
- [[Cross-entropy]] — origine information-théorique du log-loss : la perte d'entraînement et la métrique de probabilité ne font qu'un.
- [[Régression logistique]] — produit les scores de probabilité que ces métriques évaluent.
- [[Validation croisée]] — le cadre qui produit des estimations fiables de ces métriques.
- [[Métriques vision]] — transpose l'esprit précision/rappel à la détection (mAP) et la segmentation (IoU, Dice), où compte le recouvrement spatial.

## Pour aller plus loin

- Sokolova & Lapalme (2009) — *A systematic analysis of performance measures for classification tasks*.
- Chicco & Jurman (2020) — pourquoi le MCC l'emporte sur F1 et l'exactitude en classification binaire déséquilibrée.
