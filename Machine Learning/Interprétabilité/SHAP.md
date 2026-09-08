---
role: brique
nom: SHAP
alias: [shap, SHapley Additive exPlanations, TreeSHAP, KernelSHAP]
pitch: "Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres."
categorie: ml/interpretabilite
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[LIME]]", "[[interpreto]]", "[[Captum]]"]
complements: []
tags: [explainability, supervised]
url_docs: https://shap.readthedocs.io/
url_repo: https://github.com/shap/shap
---

# SHAP

<!-- AUTO:BANDEAU:START -->
> Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-07 |
<!-- AUTO:BANDEAU:END -->

## Définition

Le standard de fait de l'[[Explicabilité des modèles]] post-hoc. Chaque variable reçoit une **valeur de Shapley** (théorie des jeux) : une contribution **additive** à la prédiction, locale mais agrégeable en vue globale — c'est cette propriété de somme qui distingue SHAP des surrogates approximatifs. Trois moteurs cohabitent et n'ont pas le même coût : **TreeSHAP**, exact et rapide sur les ensembles d'arbres ; **KernelSHAP**, model-agnostic mais fondé sur du rééchantillonnage, donc prohibitif dès que les variables se multiplient ; DeepSHAP et GradientSHAP, qui exploitent le GPU du modèle. Deux limites de méthode valent d'être sues avant de lire un graphique : Shapley suppose des coalitions arbitraires de variables, donc des variables **corrélées** produisent des attributions trompeuses ; et une attribution décrit le modèle, pas le mécanisme réel — explication n'est pas causalité.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Expliquer un modèle à arbres avec des attributions **exactes** et rapides (TreeSHAP) | Simple classement global approximatif : la permutation importance de [[Scikit-Learn]] suffit, et coûte moins cher |
| Besoin de cohérence : des contributions qui somment à la prédiction, du local au global | Boîte noire lourde où KernelSHAP devient trop lent → [[LIME]] ou un surrogate |
| Auditer ou déboguer un modèle, présenter une décision individuelle | Réseau [[PyTorch]] : une rétropropagation vaut mieux que des milliers de perturbations → [[Captum]] |
| Visualisations prêtes à lire : beeswarm, waterfall, dependence | Modèle interprétable par nature ([[GLM]], [[GAM]], arbre court) : le post-hoc n'apporte rien |
| | Modèle de langage HuggingFace, avec pipeline concept de bout en bout → [[interpreto]] |

## Mise en œuvre

- Installation — `uv add shap`
- Point d'entrée — import Python : un `Explainer` par famille de modèle (`TreeExplainer`, `KernelExplainer`, `DeepExplainer`)
- Prérequis — aucun au-delà du modèle à expliquer ; l'API de **visualisation** bouge d'une version à l'autre, épingler la version
- Exécution — single-node, en mémoire ; TreeSHAP très rapide, KernelSHAP coûteux, DeepSHAP et GradientSHAP sur le GPU du modèle
- Coût — gratuit, MIT ; aucune infrastructure

## Écosystème

### Alternatives

- [[LIME]] — Explications locales model-agnostic par surrogate linéaire — perturbe autour d'un point et ajuste un modèle simple interprétable ; rapide et générique (tabulaire, texte, image), mais explications instables et purement locales ; dépôt sans commit depuis juillet 2021, dernière release en juin 2020 — préférer SHAP.
- [[interpreto]] — Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs.
- [[Captum]] — Bibliothèque d'interprétabilité officielle de PyTorch (Meta) — une trentaine de méthodes d'attribution unifiées (Integrated Gradients, DeepLift, GradCAM, Shapley, TracIn) applicables à n'importe quel modèle PyTorch, entrées comme couches ou neurones.

## Ressources

- Documentation — https://shap.readthedocs.io/
- Dépôt — https://github.com/shap/shap

## Voir aussi

- [[Explicabilité des modèles]] — le cadre qu'il outille : Shapley, et l'articulation local ↔ global
- [[Comparatif - Explicabilité|Comparatif — Explicabilité]] — ce qui départage les outils du dossier
- [[XGBoost]] · [[LightGBM]] · [[CatBoost]] — les modèles où TreeSHAP est exact et natif
