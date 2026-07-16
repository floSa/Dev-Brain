---
galaxie: wiki
type: concept
nom: Classification
alias: [Classification supervisée, Classifieur, Classifier, Classement]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [classification, supervised]
---

# Classification

## Aperçu

- Branche de l'[[Apprentissage supervisé]] où la cible est **catégorielle** : prédire à quelle classe appartient une observation (spam / non-spam, défaut / sain, une espèce parmi dix).
- Le modèle produit presque toujours un **score ou une probabilité** par classe ; la classe annoncée n'est qu'un seuil appliqué dessus. Ne pas confondre les deux est la source de la plupart des erreurs d'usage.

## Concepts clés

### Quand classer plutôt que régresser
- La cible est une **étiquette sans ordre ni distance** : « chat » et « chien » ne se soustraient pas. Si la cible est un nombre où l'écart a un sens (prix, température), c'est de la [[Régression]].
- Cible ordinale (« faible / moyen / fort ») : cas frontière. Traitée en classification on perd l'ordre ; traitée en régression on invente des distances. Voir [[Types de données et choix de modèle]].

### Les variantes de la tâche
- **Binaire** — deux classes. Le cas de référence, et celui où toutes les métriques sont les plus lisibles.
- **Multiclasse** — $K$ classes exclusives. Obtenu nativement (arbres, [[Naive Bayes]]) ou par décomposition *one-vs-rest* / *one-vs-one* ([[SVM]]).
- **Multi-label** — plusieurs étiquettes simultanées (un article peut être « ML » *et* « Python »). Voir [[Régression et classification multi-sorties]].

### Score, seuil, décision
- Un classifieur ordonne les observations par score ; le **seuil** transforme cet ordre en décision. Déplacer le seuil échange rappel contre précision, sans jamais réentraîner.
- Le seuil se choisit selon le **coût métier** des deux erreurs, pas par défaut à 0,5. Rater une fraude et bloquer un client honnête n'ont pas le même prix.
- Un score n'est pas une probabilité tant qu'il n'est pas calibré : voir [[Calibration]].

### Évaluer : l'accuracy ment
- Sur classes déséquilibrées, prédire toujours la majorité donne une accuracy magnifique et un modèle inutile. À 99 % de sains, « tout va bien » fait 99 %.
- Lire précision, rappel, F1 par classe et la matrice de confusion : [[Classification metrics]]. Comparer les modèles indépendamment du seuil : [[ROC-AUC & courbe PR]] — et préférer la courbe PR quand la classe positive est rare.
- Le déséquilibre est un sujet à part entière : [[Imbalanced classification]].

### Frontière de décision
- Chaque famille de modèles trace une frontière de forme différente : hyperplan pour les [[Régression logistique|modèles linéaires]], escaliers orthogonaux aux axes pour les [[Arbres de décision|arbres]], contours souples pour les [[SVM]] à noyau, locale et irrégulière pour [[k-NN]].
- La forme de la frontière que réclament les données est le meilleur guide de choix du modèle — souvent plus que la métrique.

## Les maths, simplement

- Le classifieur optimal (règle de Bayes) affecte la classe la plus probable : $\hat{y} = \arg\max_k \; P(y = k \mid x)$. Tout classifieur n'est qu'une manière d'estimer ce $P(y = k \mid x)$.
- Perte usuelle — l'[[Cross-entropy|entropie croisée]] : $\ell = -\sum_{k} y_k \log \hat{p}_k$, où $y_k$ vaut 1 pour la vraie classe et 0 sinon. Elle punit d'autant plus fort qu'on s'est trompé **avec confiance**.
- Depuis la matrice de confusion : $\text{précision} = \frac{VP}{VP + FP}$ (parmi mes alertes, combien de vraies), $\text{rappel} = \frac{VP}{VP + FN}$ (parmi les vrais cas, combien j'en attrape). $F_1$ = moyenne harmonique des deux.

## En pratique

- **Baseline obligatoire** : classe majoritaire, puis [[Régression logistique]]. Beaucoup de projets s'arrêtent là sans perte réelle.
- Sur **tabulaire**, commencer par le [[Gradient Boosting (GBDT)|boosting d'arbres]] : il gagne presque toujours et demande peu de préparation. Sur **texte / image**, aller directement vers les représentations apprises ([[embeddings]], [[CNN]], [[Transformer architectures]]).
- Ne pas rééquilibrer par réflexe. Ajuster le seuil ou les poids de classe suffit souvent, et déforme moins que le sur-échantillonnage ([[Imbalanced classification]]).
- Stratifier les découpages : sans `stratify`, un fold peut ne contenir aucun positif ([[Validation croisée]]).
- Si les probabilités servent à décider (tarification, tri, seuil métier), **calibrer** — un [[Random Forest]] ou un [[SVM]] sortent des scores mal calibrés par nature ([[Calibration]]).
- Outils : [[Dev/Services/Scikit-Learn|sklearn]] (`LogisticRegression`, `RandomForestClassifier`, `SVC`, `classification_report`), [[Dev/Services/XGBoost|XGBoost]] / [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/imbalanced-learn|imbalanced-learn]] pour le déséquilibre.

## Approches voisines & alternatives

- [[Régression]] — l'autre branche supervisée : cible continue plutôt que catégorielle.
- [[Apprentissage supervisé]] — le cadre englobant des deux.
- [[Régression logistique]] — la baseline linéaire, et le point de départ par défaut.
- [[Arbres de décision]] / [[Random Forest]] / [[Gradient Boosting (GBDT)]] — la famille dominante sur tabulaire.
- [[SVM]] — marge maximale ; efficace en grande dimension et à petit $n$.
- [[k-NN]] — décision locale par vote des voisins ; baseline non paramétrique.
- [[Naive Bayes]] — probabiliste, très rapide, référence historique sur le texte.
- [[Analyse discriminante]] — le génératif gaussien : LDA/QDA, la baseline oubliée, excellente à petit $n$.
- [[AdaBoost]] / [[Extra Trees]] — les autres membres des familles boosting et bagging.
- [[Classification metrics]] / [[ROC-AUC & courbe PR]] — comment mesurer.
- [[Imbalanced classification]] — quand une classe est rare.
- [[Clustering]] — le pendant non supervisé : former des groupes sans étiquettes connues.
- [[Types de données et choix de modèle]] — l'aiguillage amont.

## Pour aller plus loin

- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 4 (Linear Methods for Classification).
- Documentation scikit-learn — *Classification* et le guide *Choosing the right estimator*.
- Provost & Fawcett — *Data Science for Business*, ch. 7-8 : coûts d'erreur et choix de seuil.
