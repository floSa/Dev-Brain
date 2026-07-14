---
galaxie: dev
type: service
nom: SHAP
alias: [shap, SHapley Additive exPlanations, TreeSHAP, KernelSHAP]
pitch: "Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/LIME|LIME]]"]
remplace_par: []
status: actif
tags: [explainability, supervised]
url_docs: https://shap.readthedocs.io/
url_repo: https://github.com/shap/shap
---

# SHAP

## Pourquoi

Standard de fait de l'[[Explicabilité des modèles]]. Calcule des **valeurs de Shapley** (théorie des jeux) : chaque variable reçoit une contribution **additive** à la prédiction, locale mais agrégeable en vue globale. Sa force pratique : **TreeSHAP**, exact et rapide sur les ensembles d'arbres ([[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/CatBoost|CatBoost]]) ; plus KernelSHAP (model-agnostic), DeepSHAP, et des visualisations soignées (beeswarm, waterfall, dependence).

## Quand l'utiliser

- Expliquer un modèle à arbres avec attributions **exactes** et rapides (TreeSHAP).
- Besoin de **cohérence** : contributions qui somment à la prédiction, du local au global.
- Auditer / déboguer un modèle, présenter une décision individuelle.

## Quand NE PAS l'utiliser

- Simple **classement global** approximatif → permutation importance (scikit-learn) suffit, plus léger.
- Boîte noire lourde où **KernelSHAP est trop lent** → [[Dev/Services/LIME|LIME]] ou un surrogate.
- Modèle **interprétable par nature** ([[GLM]], [[GAM]], arbre court) → pas besoin de post-hoc.

## Déploiement & coût

- Bibliothèque open-source (**MIT**), gratuite ; `uv add shap`.
- **Single-node, en mémoire** ; TreeSHAP très rapide, **KernelSHAP coûteux** (rééchantillonnage). DeepSHAP/GradientSHAP exploitent le GPU du modèle.
- Aucune infra.

## Pièges

- **KernelSHAP lent et approximatif** : prohibitif sur gros volumes / nombreuses features.
- **Corrélations** entre variables → attributions trompeuses (Shapley suppose des coalitions arbitraires).
- **Explication ≠ causalité** : SHAP décrit le modèle, pas le mécanisme réel.
- API de **visualisation** mouvante d'une version à l'autre ; épingler la version.

## Alternatives

- [[Dev/Services/LIME|LIME]] — Explications locales model-agnostic par surrogate linéaire — perturbe autour d'un point et ajuste un modèle simple interprétable ; rapide et générique (tabulaire, texte, image), mais explications instables et purement locales.

## Liens

- [[Explicabilité des modèles]] — le cadre qu'il outille (Shapley, local↔global).
- [[Dev/Services/LIME|LIME]] — l'autre approche post-hoc, par surrogate local.
- [[Dev/Services/XGBoost|XGBoost]] · [[Dev/Services/LightGBM|LightGBM]] · [[Dev/Services/CatBoost|CatBoost]] — TreeSHAP exact y est natif.
- [[Dev/Patterns/Comparatif - Explicabilité|Comparatif — Explicabilité]]
- Doc : https://shap.readthedocs.io/
