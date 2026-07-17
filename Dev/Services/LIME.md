---
galaxie: dev
type: service
nom: LIME
alias: [lime, Local Interpretable Model-agnostic Explanations]
pitch: "Explications locales model-agnostic par surrogate linéaire — perturbe autour d'un point et ajuste un modèle simple interprétable ; rapide et générique (tabulaire, texte, image), mais explications instables et purement locales."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/SHAP|SHAP]]", "[[Dev/Services/interpreto|interpreto]]"]
remplace_par: []
status: actif
tags: [explainability, supervised]
url_docs: https://github.com/marcotcr/lime
url_repo: https://github.com/marcotcr/lime
---

# LIME

## Pourquoi

**L**ocal **I**nterpretable **M**odel-agnostic **E**xplanations : explique **une** prédiction d'une boîte noire en l'approximant **localement** par un modèle simple (linéaire). Concrètement, LIME **perturbe** l'entrée autour du point, observe les sorties du modèle, et ajuste un surrogate pondéré par la proximité. Générique : tabulaire, **texte** (mots saillants) et **image** (super-pixels). Une porte d'entrée légère vers l'[[Explicabilité des modèles]].

## Quand l'utiliser

- Explication **locale** rapide de n'importe quel classifieur, sans hypothèse sur le modèle.
- **Texte / image** : surligner les mots ou régions qui ont fait pencher la décision.
- Quand les méthodes exactes de [[Dev/Services/SHAP|SHAP]] ne s'appliquent pas au modèle.

## Quand NE PAS l'utiliser

- Besoin de **cohérence** et d'agrégation local→global → [[Dev/Services/SHAP|SHAP]] (valeurs de Shapley).
- Modèle à **arbres** → TreeSHAP exact et rapide ([[Dev/Services/SHAP|SHAP]]) plutôt qu'un surrogate approximatif.
- **Stabilité** critique → les explications LIME varient d'un tirage à l'autre.

## Déploiement & coût

- Bibliothèque open-source (**BSD-2-Clause**), gratuite ; `uv add lime`.
- **Single-node, en mémoire** ; coût = nombre de perturbations × inférences du modèle.
- Aucune infra.

## Pièges

- **Instabilité** : perturbations aléatoires → explications différentes pour le même point ; fixer la graine, augmenter l'échantillon.
- **Voisinage arbitraire** : largeur de noyau et nombre d'échantillons influencent fortement le résultat.
- **Fidélité locale seulement** : ne dit rien du comportement global du modèle.
- Projet **quasi-dormant** (peu de releases récentes) ; SHAP est plus vivant et mieux fondé.

## Alternatives

- [[Dev/Services/SHAP|SHAP]] — Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres.
- [[Dev/Services/interpreto|interpreto]] — Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs.

## Liens

- [[Explicabilité des modèles]] — le cadre qu'il outille (surrogate local).
- [[Dev/Services/SHAP|SHAP]] — l'alternative cohérente et fondée, à préférer quand elle s'applique.
- [[Dev/Patterns/Comparatif - Explicabilité|Comparatif — Explicabilité]]
- Doc : https://github.com/marcotcr/lime
