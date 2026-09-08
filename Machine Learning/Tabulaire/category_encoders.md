---
role: brique
nom: category_encoders
alias: [category-encoders, categorical-encoding, WOEEncoder]
pitch: "Encodeurs catégoriels compatibles scikit-learn — Target, Weight of Evidence, James-Stein, CatBoost, hashing — pour les variables à forte cardinalité."
categorie: ml/tabulaire
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Scikit-Learn]]"]
complements: ["[[Featuretools]]"]
tags: [feature-engineering]
url_docs: https://contrib.scikit-learn.org/category_encoders/
url_repo: https://github.com/scikit-learn-contrib/category_encoders
---

# category_encoders

<!-- AUTO:BANDEAU:START -->
> Encodeurs catégoriels compatibles scikit-learn — Target, Weight of Evidence, James-Stein, CatBoost, hashing — pour les variables à forte cardinalité.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-07 |
<!-- AUTO:BANDEAU:END -->

## Définition

Collection de transformers d'encodage catégoriel suivant l'API scikit-learn — `fit` /
`transform` —, insérables tels quels dans un `Pipeline` ou un `ColumnTransformer`. Au-delà des
encodeurs natifs, elle apporte une large famille d'encodeurs **supervisés**, calculés par la
cible : Target, Weight of Evidence, James-Stein, M-estimate, Leave-One-Out, CatBoost encoder,
GLMM, Quantile ; et non supervisés : hashing, BaseN. La cible visée est la variable à forte
cardinalité, où le One-Hot explose en dimension. Projet `scikit-learn-contrib`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Variables catégorielles à forte cardinalité, où le One-Hot explose en dimension | Faible cardinalité : les encodeurs natifs de [[Scikit-Learn]] suffisent, y compris le repli anti-fuite du target encoding depuis la 1.3 |
| Encodeur précis absent de scikit-learn : WoE, James-Stein, M-estimate, CatBoost encoder | Les encodeurs par la cible (Target, WoE, LOO) sont des vecteurs de fuite : à ajuster dans le pipeline, pli par pli → [[Data leakage]] |
| Scoring de crédit : le Weight of Evidence y est le format attendu → [[Régression logistique]] | Lissage à régler : trop faible, on surajuste les petites modalités ; trop fort, le signal se noie dans la moyenne globale |
| Pipeline scikit-learn existant : les encodeurs s'y insèrent sans friction | WoE ne vaut que pour une cible binaire, sinon passer par `PolynomialWrapper` |
| | Modèle qui gère nativement les catégorielles : encoder en amont n'a plus d'objet → [[CatBoost]] |

## Mise en œuvre

- Installation — `uv add category-encoders`
- Point d'entrée — transformers scikit-learn (`TargetEncoder`, `WOEEncoder`, `JamesSteinEncoder`…) posés dans un `Pipeline`
- Prérequis — scikit-learn et pandas
- Exécution — CPU, sur une machine
- Coût — gratuit, BSD-3-Clause ; rien à héberger

## Écosystème

### Alternatives

- [[Scikit-Learn]] — Boîte à outils ML généraliste en Python — une API fit/predict unifiée pour modèles supervisés, clustering, décomposition (PCA…), preprocessing et métriques.

### Compléments

- [[Featuretools]] — Ingénierie de features automatisée par Deep Feature Synthesis : empile des primitives d'agrégation et de transformation sur des données relationnelles/temporelles pour générer des centaines de variables. Fournit en amont les colonnes que ces encodeurs préparent.

## Ressources

- Documentation — https://contrib.scikit-learn.org/category_encoders/
- Dépôt — https://github.com/scikit-learn-contrib/category_encoders

## Voir aussi

- [[Encodage des variables catégorielles]] — la notion qu'il implémente
- [[Ingénierie des caractéristiques]] — l'étape qui l'englobe
