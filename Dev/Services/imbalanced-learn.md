---
galaxie: dev
type: service
nom: imbalanced-learn
alias: [imblearn, imbalanced learn, imb-learn]
pitch: "Rééchantillonnage pour classes déséquilibrées, API compatible scikit-learn — SMOTE et variantes, undersampling, méthodes combinées et ensembles rééquilibrés, dans un Pipeline qui cantonne le resampling au pli d'entraînement."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [class-imbalance, classification, supervised]
url_docs: https://imbalanced-learn.org/
url_repo: https://github.com/scikit-learn-contrib/imbalanced-learn
---

# imbalanced-learn

## Pourquoi

imbalanced-learn (importé `imblearn`) étend [[Dev/Services/Scikit-Learn|Scikit-Learn]] pour la classification à **classes déséquilibrées**. Il fournit les techniques de rééchantillonnage — sur-échantillonnage synthétique (SMOTE et variantes), sous-échantillonnage, méthodes combinées — et des estimateurs d'ensemble rééquilibrés, exposés via la même API transformer/estimator. Son `Pipeline` dédié garantit que le rééchantillonnage ne s'applique qu'au **pli d'entraînement**, ce qui évite la fuite de données. Projet scikit-learn-contrib.

## Quand l'utiliser

- Classe d'intérêt **rare** (fraude, panne, churn) où le rééchantillonnage aide, **après** la métrique et la pondération.
- Synthétiser des exemples minoritaires : **SMOTE**, BorderlineSMOTE, ADASYN, KMeansSMOTE, SMOTENC (features catégorielles).
- Sous-échantillonner proprement : RandomUnderSampler, NearMiss, Tomek Links, Edited Nearest Neighbours.
- Méthodes combinées (SMOTEENN, SMOTETomek) ou ensembles rééquilibrés (BalancedRandomForest, BalancedBaggingClassifier, EasyEnsemble, RUSBoost).
- Intégrer le sampler dans un `imblearn.pipeline.Pipeline` pour qu'il reste cantonné à la validation croisée.

## Quand NE PAS l'utiliser

- Avant d'avoir réglé la **métrique** (PR-AUC), le **seuil** et `class_weight` — le rééchantillonnage vient en dernier (cf. [[Imbalanced classification]]).
- Arbres boostés qui gèrent le déséquilibre nativement via `scale_pos_weight` → [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]].
- Données non tabulaires (images, texte brut) où l'augmentation se fait dans le pipeline d'entraînement, pas par interpolation SMOTE sur features.

## Déploiement & coût

- Open-source (MIT), gratuit ; `uv add imbalanced-learn`. Rien à héberger.
- Dépend de scikit-learn / NumPy / SciPy et suit les versions de scikit-learn. Calcul **single-node** (CPU).

## Pièges

- **Rééchantillonner avant le split** = [[Data leakage]] : toujours via le `Pipeline` imblearn, jamais sur le dataset entier.
- SMOTE interpole entre plus proches voisins : sensible aux features catégorielles (préférer SMOTENC) et au bruit / outliers.
- Après rééchantillonnage les **probabilités sont biaisées** → recalibrer ([[Calibration]]) ou préférer la pondération.
- Ne crée pas d'information : avec très peu de positifs, SMOTE peut amplifier le bruit et surajuster.

## Alternatives

Pas d'équivalent direct dans le brain — imbalanced-learn **complète** [[Dev/Services/Scikit-Learn|Scikit-Learn]] plutôt qu'il ne le remplace. Approches concurrentes au rééchantillonnage : `class_weight='balanced'` (scikit-learn), `scale_pos_weight` des arbres boostés ([[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]]), et l'ajustement de seuil.

## Liens

- [[Imbalanced classification]] — le concept : métrique, seuil, pondération, rééchantillonnage.
- [[Dev/Services/Scikit-Learn|Scikit-Learn]] — la base dont imbalanced-learn reprend et étend l'API (transformers, Pipeline).
- [[Data leakage]] — rééchantillonner hors du pli d'entraînement en est une cause classique.
- [[Calibration]] — recalibrer les probabilités après rééchantillonnage.
- Doc : https://imbalanced-learn.org/
