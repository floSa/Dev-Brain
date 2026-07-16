---
galaxie: wiki
type: concept
nom: Imbalanced classification
alias: [classes déséquilibrées, déséquilibre de classes, class imbalance]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [classification, supervised, class-imbalance]
---

# Imbalanced classification

## Aperçu

- Classification où une classe — souvent celle d'intérêt — est rare : fraude, panne, maladie, churn. Le ratio peut atteindre 1:1000.
- Enjeu : un modèle qui prédit toujours la classe majoritaire affiche une accuracy élevée tout en étant inutile. Il faut adapter la **métrique**, le **seuil**, et parfois les **données** ou la **perte**.

## Concepts clés

### Le piège de l'accuracy
- Sur 99 % de négatifs, prédire « négatif » partout donne 99 % d'accuracy et 0 % de rappel sur la classe rare.
- Mesurer avec précision / rappel / F1 et surtout la **PR-AUC**, plus informative que la ROC-AUC quand les positifs sont rares. Voir [[Classification metrics]] et [[ROC-AUC & courbe PR]].

### Rééchantillonnage
- **Oversampling** de la minorité : duplication, ou synthèse **SMOTE** (interpolation entre plus proches voisins).
- **Undersampling** de la majorité : rapide, mais jette de l'information.
- À faire **dans le pli d'entraînement uniquement**, jamais avant le découpage — sinon [[Data leakage]].

### Pondération & coût
- `class_weight='balanced'` pénalise davantage les erreurs sur la minorité dans la perte, sans ajouter de données.
- Apprentissage sensible au coût (*cost-sensitive*) : matrice de coûts asymétrique reflétant l'enjeu métier.

### Déplacement du seuil
- Le seuil 0,5 est arbitraire ; l'abaisser augmente le rappel au prix de la précision.
- Choisir le seuil sur la courbe précision-rappel selon le compromis métier. Un modèle **calibré** ([[Calibration]]) rend ce choix fiable.

## Les maths, simplement

- SMOTE : nouveau point $x_{\text{new}} = x_i + \lambda\,(x_{z} - x_i)$, avec $\lambda \sim \mathcal{U}(0,1)$ et $x_{z}$ l'un des $k$ voisins minoritaires de $x_i$. Les synthèses tombent sur les segments entre voisins.
- Perte pondérée : $\sum_i w_{y_i}\,L(y_i, \hat y_i)$ avec $w_c \propto 1/n_c$ — une erreur sur la classe rare pèse plus lourd.

## En pratique

- Ordre conseillé : d'abord la **bonne métrique** et le **seuil**, ensuite `class_weight`, et seulement si besoin le rééchantillonnage.
- [[Dev/Services/imbalanced-learn|imbalanced-learn]] (API compatible scikit-learn) pour SMOTE et l'undersampling ; placer le sampler **dans un `Pipeline`** pour qu'il reste cantonné au pli.
- Les arbres boostés ([[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]]) gèrent bien le déséquilibre via `scale_pos_weight`.
- Piège récurrent : optimiser l'accuracy, ou rééchantillonner avant la [[Validation croisée]] (fuite).

## Approches voisines & alternatives

- [[Classification]] — le chapeau de la tâche ; le déséquilibre en est le cas particulier le plus fréquent.
- [[Classification metrics]], [[ROC-AUC & courbe PR]] — choisir la métrique adaptée aux classes rares (PR-AUC plutôt qu'accuracy).
- [[Isolation Forest]] — l'alternative non supervisée quand la classe rare est si rare qu'on ne l'étiquette pas.
- [[k-NN]] — particulièrement vulnérable au déséquilibre : les voisins d'un point rare sont majoritairement fréquents.
- [[Calibration]] — après rééchantillonnage les probabilités sont biaisées ; recalibrer.
- [[Data leakage]] — rééchantillonner hors du pli d'entraînement est une cause classique de fuite.

## Pour aller plus loin

- Chawla et al. (2002) — *SMOTE: Synthetic Minority Over-sampling Technique*.
- He & Garcia (2009) — *Learning from Imbalanced Data*.
- Documentation `imbalanced-learn`.
