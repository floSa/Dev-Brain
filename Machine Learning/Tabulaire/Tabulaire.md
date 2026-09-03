---
role: hub
nom: Tabulaire
alias: [données tabulaires]
pitch: Des lignes, des colonnes, une cible — les arbres et leurs ensembles, et le travail sur les variables qui décide de leur score.
domaines: [data-sci, ml-eng]
tags: [tree-based, boosting, ensemble, feature-engineering, class-imbalance, supervised]
---

# Tabulaire

> Des lignes, des colonnes, une cible — les arbres et leurs ensembles, et le travail sur les variables qui décide de leur score.

## Ce qu'il faut comprendre

- **Ce dossier ne range pas « tout ce qui se met dans un DataFrame ».** Manipuler et transformer des tables relève de [[DataFrames]] et de [[Data & pipelines]] ; modéliser une table dont une colonne est la cible relève d'ici. Le critère se lit en deux temps. Ce qui vaut **quelle que soit la nature de la donnée** — cadrer le problème, les modèles linéaires, la boîte classique — est dans [[Socle]] ; ce qui **suppose des colonnes** est ici : les arbres et leurs ensembles, et le travail sur les variables, qui n'existe que parce qu'une variable est une colonne nommée. Ce dossier range donc les deux moitiés du même métier — les modèles qui gagnent sur ce terrain, et la préparation qui décide de leur score.
- **Le gradient boosting est la réponse par défaut, et ce n'est pas une opinion** : sur données hétérogènes, il bat encore le deep learning à coût bien moindre. [[Gradient Boosting (GBDT)]] et [[Boosting]] pour le mécanisme, [[Arbres de décision]] pour la brique, [[Ensembling]] et [[Bagging]] pour le contraste avec [[Random Forest]] — moyenner réduit la variance, corriger séquentiellement réduit le biais.
- **Les trois implémentations majeures se départagent sur un point précis chacune**, pas sur la précision : la gestion native des variables catégorielles, la vitesse sur gros volumes, et l'étendue de l'écosystème distribué. Le reste s'égalise après réglage.
- **Le rendement se déplace vite du modèle vers les variables**, et cette moitié du dossier pèse plus lourd que l'autre. [[Ingénierie des caractéristiques]] est le premier levier ; [[Encodage des variables catégorielles]] le deuxième, et le plus mal fait — un encodage par la cible fuit si on l'ajuste sur les mêmes lignes que le modèle, c'est une source classique de [[Data leakage]]. [[Mise à l'échelle]] ne sert pas aux arbres mais reste nécessaire aux modèles linéaires et aux distances. [[Sélection de variables]] arrive en dernier.
- **Le déséquilibre des classes se traite dans le pipeline, pas avant** : [[Imbalanced classification]]. Rééchantillonner l'ensemble du jeu avant la validation croisée duplique des lignes de part et d'autre de la coupure et fabrique un score faux ; le rééchantillonnage n'a droit de cité que sur le pli d'entraînement. Souvent, une pondération de classe et un seuil bien choisi suffisent — et une [[Calibration]] correcte vaut mieux qu'un jeu artificiellement équilibré.
- **Un score de boosting n'est pas une probabilité** tant qu'il n'a pas été calibré : [[Calibration]], indispensable dès qu'on transforme la sortie en décision chiffrée (coût, seuil, priorisation).
- L'explication d'un modèle à arbres est immédiate et exacte — c'est un des rares cas où l'explicabilité ne coûte presque rien. Cf. [[Interprétabilité]] et [[SHAP]].

## Choisir

- Le défaut, l'écosystème le plus large, du distribué disponible → [[XGBoost]].
- Beaucoup de lignes, une contrainte de temps d'entraînement → [[LightGBM]].
- Beaucoup de variables catégorielles, peu de temps pour régler → [[CatBoost]], dont l'encodage ordonné évite la fuite par construction. Cf. [[Comparatif - Boosting]].
- Encoder des catégorielles à forte cardinalité, hors des trois précédents → [[category_encoders]].
- Générer automatiquement des variables depuis plusieurs tables liées → [[Featuretools]].
- Traiter un déséquilibre de classes dans un pipeline scikit-learn → [[imbalanced-learn]].
- Un modèle de référence avant tout ça, ou un cadrage à poser → [[Socle]] et [[Scikit-Learn]].
- Comprendre pourquoi une valeur manque avant de la remplacer → [[Mécanismes de données manquantes]], puis [[Imputation des valeurs manquantes]].

<!-- AUTO:START -->
### Notions
- [[AdaBoost]] — domaines : data-sci, ml-eng
- [[Arbres de décision]] — domaines : data-sci, ml-eng
- [[Bagging]] — domaines : data-sci, ml-eng
- [[Boosting]] — domaines : data-sci, ml-eng
- [[Encodage des variables catégorielles]] — domaines : data-sci
- [[Ensembling]] — domaines : data-sci, ml-eng
- [[Extra Trees]] — domaines : data-sci, ml-eng
- [[Gradient Boosting (GBDT)]] — domaines : data-sci, ml-eng
- [[Imbalanced classification]] — domaines : data-sci, ml-eng
- [[Imputation des valeurs manquantes]] — domaines : data-sci
- [[Ingénierie des caractéristiques]] — domaines : data-sci, ml-eng
- [[Mise à l'échelle]] — domaines : data-sci
- [[Mécanismes de données manquantes]] — domaines : data-sci
- [[Random Forest]] — domaines : data-sci, ml-eng
- [[Sélection de variables]] — domaines : data-sci, ml-eng

### Briques
- [[CatBoost]] — Gradient boosting Yandex avec gestion native des variables catégorielles (encodage ordonné) et arbres symétriques ; robuste avec peu de tuning.
- [[category_encoders]] — Encodeurs catégoriels compatibles scikit-learn — Target, Weight of Evidence, James-Stein, CatBoost, hashing — pour les variables à forte cardinalité.
- [[Featuretools]] — Ingénierie de features automatisée par Deep Feature Synthesis : empile des primitives d'agrégation et de transformation sur des données relationnelles/temporelles pour générer des centaines de variables.
- [[imbalanced-learn]] — Rééchantillonnage pour classes déséquilibrées, API compatible scikit-learn — SMOTE et variantes, undersampling, méthodes combinées et ensembles rééquilibrés, dans un Pipeline qui cantonne le resampling au pli d'entraînement.
- [[LightGBM]] — Gradient boosting Microsoft optimisé vitesse et mémoire : croissance des arbres par feuille (leaf-wise) et binning histogramme, taillé pour les gros volumes.
- [[XGBoost]] — Implémentation de référence du gradient boosting : optimisée, régularisée et distribuée (Spark, Dask, Ray) ; cheval de bataille des compétitions sur données tabulaires.

### Comparatifs
- [[Comparatif - Boosting]]
<!-- AUTO:END -->

## Notes
