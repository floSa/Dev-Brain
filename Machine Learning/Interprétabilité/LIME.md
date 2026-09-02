---
role: brique
nom: LIME
alias: [lime, Local Interpretable Model-agnostic Explanations]
pitch: "Explications locales model-agnostic par surrogate linéaire — perturbe autour d'un point et ajuste un modèle simple interprétable ; rapide et générique (tabulaire, texte, image), mais explications instables et purement locales ; dépôt sans commit depuis juillet 2021, dernière release en juin 2020 — préférer SHAP."
categorie: ml/interpretabilite
famille: paquet
licence_type: open-source
maturite: deprecated
langage: Python
alternatives: ["[[SHAP]]", "[[interpreto]]"]
complements: []
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
- Quand les méthodes exactes de [[SHAP]] ne s'appliquent pas au modèle.

## Quand NE PAS l'utiliser

- Besoin de **cohérence** et d'agrégation local→global → [[SHAP]] (valeurs de Shapley).
- Modèle à **arbres** → TreeSHAP exact et rapide ([[SHAP]]) plutôt qu'un surrogate approximatif.
- **Stabilité** critique → les explications LIME varient d'un tirage à l'autre.

## Déploiement & coût

- Bibliothèque open-source (**BSD-2-Clause**), gratuite ; `uv add lime`.
- **Single-node, en mémoire** ; coût = nombre de perturbations × inférences du modèle.
- Aucune infra.

## Pièges

- **Instabilité** : perturbations aléatoires → explications différentes pour le même point ; fixer la graine, augmenter l'échantillon.
- **Voisinage arbitraire** : largeur de noyau et nombre d'échantillons influencent fortement le résultat.
- **Fidélité locale seulement** : ne dit rien du comportement global du modèle.
- Projet **à l'arrêt en amont** : aucun commit depuis juillet 2021, aucune release depuis juin 2020 (`lime 0.2.0.1`). Le code fonctionne encore, mais rien n'évoluera et rien ne sera corrigé — préférer [[SHAP]], plus vivant et mieux fondé.

## Alternatives

- [[SHAP]] — Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres.
- [[interpreto]] — Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs.

## Liens

- [[Explicabilité des modèles]] — le cadre qu'il outille (surrogate local).
- [[SHAP]] — l'alternative cohérente et fondée, à préférer quand elle s'applique.
- [[Comparatif - Explicabilité|Comparatif — Explicabilité]]
- Doc : https://github.com/marcotcr/lime
