---
role: brique
nom: imbalanced-learn
alias: [imblearn, imbalanced learn, imb-learn]
pitch: "Rééchantillonnage pour classes déséquilibrées, API compatible scikit-learn — SMOTE et variantes, undersampling, méthodes combinées et ensembles rééquilibrés, dans un Pipeline qui cantonne le resampling au pli d'entraînement."
categorie: ml/tabulaire
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: []
tags: [class-imbalance, classification, supervised]
url_docs: https://imbalanced-learn.org/
url_repo: https://github.com/scikit-learn-contrib/imbalanced-learn
---

# imbalanced-learn

<!-- AUTO:BANDEAU:START -->
> Rééchantillonnage pour classes déséquilibrées, API compatible scikit-learn — SMOTE et variantes, undersampling, méthodes combinées et ensembles rééquilibrés, dans un Pipeline qui cantonne le resampling au pli d'entraînement.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-06-07 |
<!-- AUTO:BANDEAU:END -->

## Définition

imbalanced-learn — importé `imblearn` — étend [[Scikit-Learn]] pour la classification à classes
déséquilibrées. Il fournit le sur-échantillonnage synthétique (SMOTE et ses variantes), le
sous-échantillonnage, les méthodes combinées et des estimateurs d'ensemble rééquilibrés, tous
exposés par la même API transformer/estimator. Son `Pipeline` dédié est le point clé : il
garantit que le rééchantillonnage ne s'applique qu'au pli d'entraînement, jamais au pli de
validation. Projet scikit-learn-contrib, sans équivalent direct dans le brain — il complète
scikit-learn plutôt qu'il ne le remplace.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Classe d'intérêt rare (fraude, panne, churn), une fois la métrique et la pondération réglées | Rééchantillonner avant le split : c'est une fuite caractérisée → [[Data leakage]] |
| Synthétiser des exemples minoritaires : SMOTE, BorderlineSMOTE, ADASYN, KMeansSMOTE, SMOTENC | Métrique (PR-AUC), seuil et `class_weight` pas encore réglés : le rééchantillonnage vient en dernier |
| Sous-échantillonner proprement : RandomUnderSampler, NearMiss, Tomek Links, Edited Nearest Neighbours | Arbres boostés qui gèrent le déséquilibre par `scale_pos_weight` → [[XGBoost]], [[LightGBM]] |
| Méthodes combinées (SMOTEENN, SMOTETomek) ou ensembles rééquilibrés (BalancedRandomForest, EasyEnsemble, RUSBoost) | SMOTE interpole entre plus proches voisins : sensible aux catégorielles (préférer SMOTENC), au bruit et aux outliers |
| Cantonner le sampler à la validation croisée, via `imblearn.pipeline.Pipeline` | Probabilités biaisées après rééchantillonnage : recalibrer → [[Calibration]] |
| | Très peu de positifs : SMOTE amplifie le bruit plutôt qu'il ne crée de l'information |
| | Données non tabulaires (images, texte brut) : l'augmentation se fait dans le pipeline d'entraînement, pas par interpolation sur des features |

## Mise en œuvre

- Installation — `uv add imbalanced-learn`
- Point d'entrée — samplers à l'API scikit-learn (`SMOTE`, `RandomUnderSampler`…) posés dans un `imblearn.pipeline.Pipeline`
- Prérequis — scikit-learn, NumPy et SciPy ; la version suit celle de scikit-learn
- Exécution — CPU, sur une machine
- Coût — gratuit, MIT ; rien à héberger

## Ressources

- Documentation — https://imbalanced-learn.org/
- Dépôt — https://github.com/scikit-learn-contrib/imbalanced-learn

## Voir aussi

- [[Imbalanced classification]] — la notion du dossier : métrique, seuil, pondération, puis rééchantillonnage
