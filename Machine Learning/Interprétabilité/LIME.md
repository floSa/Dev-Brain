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

<!-- AUTO:BANDEAU:START -->
> Explications locales model-agnostic par surrogate linéaire — perturbe autour d'un point et ajuste un modèle simple interprétable ; rapide et générique (tabulaire, texte, image), mais explications instables et purement locales ; dépôt sans commit depuis juillet 2021, dernière release en juin 2020 — préférer SHAP.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | deprecated |
<!-- AUTO:BANDEAU:END -->

## Définition

*Local Interpretable Model-agnostic Explanations* : expliquer **une** prédiction d'une boîte noire en l'approximant **localement** par un modèle simple. LIME perturbe l'entrée autour du point, observe les sorties du modèle, puis ajuste un surrogate linéaire pondéré par la proximité — d'où sa généricité (tabulaire, **texte** avec les mots saillants, **image** avec les super-pixels) et sa légèreté. Les deux limites sont dans la méthode elle-même : les perturbations étant aléatoires, deux exécutions sur le même point donnent des explications **différentes** — il faut fixer la graine et augmenter l'échantillon ; et la largeur du noyau, comme la taille du voisinage, sont des choix arbitraires qui pèsent fortement sur le résultat. La fidélité obtenue est locale, et ne dit rien du comportement global. Le projet est par ailleurs **à l'arrêt en amont** : le code fonctionne, mais rien n'évoluera et rien ne sera corrigé.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Explication locale rapide de n'importe quel classifieur, sans hypothèse sur le modèle | Besoin de cohérence et d'agrégation du local vers le global → [[SHAP]] et ses valeurs de Shapley |
| Texte ou image : surligner les mots ou les régions qui ont fait pencher la décision | Modèle à arbres : TreeSHAP est exact et rapide, un surrogate approximatif n'a pas de raison d'être → [[SHAP]] |
| Les méthodes exactes ne s'appliquent pas au modèle sous la main | Stabilité critique : les explications varient d'un tirage à l'autre |
| | Modèle de langage HuggingFace, avec évaluation des explications → [[interpreto]] |

## Mise en œuvre

- Installation — `uv add lime` (version 0.2.0.1, dernière release en juin 2020)
- Point d'entrée — import Python : un explainer par type d'entrée (`LimeTabularExplainer`, `LimeTextExplainer`, `LimeImageExplainer`)
- Prérequis — aucun au-delà du modèle ; fixer la graine pour des explications reproductibles
- Exécution — single-node, en mémoire ; le coût est le nombre de perturbations multiplié par les inférences du modèle
- Coût — gratuit, BSD-2-Clause ; aucune infrastructure, mais aucune maintenance amont non plus

## Écosystème

### Alternatives

- [[SHAP]] — Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres.
- [[interpreto]] — Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs.

## Ressources

- Documentation — https://github.com/marcotcr/lime
- Dépôt — https://github.com/marcotcr/lime

## Voir aussi

- [[Explicabilité des modèles]] — le cadre qu'il outille : le surrogate local, et ses limites
- [[Comparatif - Explicabilité|Comparatif — Explicabilité]] — ce qui départage les outils du dossier
