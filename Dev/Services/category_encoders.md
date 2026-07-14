---
galaxie: dev
type: service
nom: category_encoders
alias: [category-encoders, categorical-encoding, WOEEncoder]
pitch: "Encodeurs catégoriels compatibles scikit-learn — Target, Weight of Evidence, James-Stein, CatBoost, hashing — pour les variables à forte cardinalité."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Scikit-Learn|Scikit-Learn]]"]
remplace_par: []
status: actif
tags: [feature-engineering]
url_docs: https://contrib.scikit-learn.org/category_encoders/
url_repo: https://github.com/scikit-learn-contrib/category_encoders
---

# category_encoders

## Pourquoi

Collection de **transformers d'encodage catégoriel** suivant l'API scikit-learn (`fit`/`transform`, intégrables dans un `Pipeline` / `ColumnTransformer`). Au-delà des `OneHotEncoder` / `OrdinalEncoder` / `TargetEncoder` natifs de sklearn, elle apporte une large famille d'encodeurs **supervisés** (par la cible) et non supervisés : Target, **Weight of Evidence**, James-Stein, M-estimate, Leave-One-Out, CatBoost encoder, GLMM, Quantile, plus hashing et BaseN. Pensée pour les variables à **forte cardinalité**. Projet `scikit-learn-contrib`.

## Quand l'utiliser

- Variables catégorielles à **forte cardinalité** où le One-Hot explose en dimension.
- Besoin d'un encodeur précis absent de sklearn : **WoE** (scoring crédit, cf. [[Régression logistique]]), James-Stein, M-estimate, CatBoost encoder.
- Pipeline sklearn existant : les encodeurs s'y insèrent sans friction.

## Quand NE PAS l'utiliser

- Faible cardinalité, encodage simple → `OneHotEncoder` / `TargetEncoder` de [[Dev/Services/Scikit-Learn|Scikit-Learn]] suffisent (sklearn ≥ 1.3 gère le repli anti-fuite du target encoding).
- Modèle gérant nativement les catégorielles → [[Dev/Services/CatBoost|CatBoost]] (pas besoin d'encoder en amont).

## Déploiement & coût

- Bibliothèque Python open-source (BSD-3-Clause), `uv add category-encoders` ; rien à héberger.
- Single-node, au-dessus de pandas / scikit-learn.
- Maintenue dans l'écosystème `scikit-learn-contrib`.

## Pièges

- Les encodeurs **par la cible** (Target, WoE, LOO) sont des vecteurs de **fuite de données** : `fit` sur le train seul, dans le pipeline, à l'intérieur de chaque pli de validation croisée.
- Le lissage (*smoothing*) se règle : trop faible = surajustement aux petites modalités, trop fort = signal noyé dans la moyenne globale.
- WoE ne vaut que pour une **cible binaire** (sinon `PolynomialWrapper`).

## Alternatives

- [[Dev/Services/Scikit-Learn|Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

## Liens

- Concept implémenté : [[Encodage des variables catégorielles]]
- Étape englobante : [[Ingénierie des caractéristiques]]
- Doc : https://contrib.scikit-learn.org/category_encoders/
