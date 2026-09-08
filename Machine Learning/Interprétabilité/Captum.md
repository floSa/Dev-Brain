---
role: brique
nom: Captum
alias: [captum, Captum.ai]
pitch: "Bibliothèque d'interprétabilité officielle de PyTorch (Meta) — une trentaine de méthodes d'attribution unifiées (Integrated Gradients, DeepLift, GradCAM, Shapley, TracIn) applicables à n'importe quel modèle PyTorch, entrées comme couches ou neurones."
categorie: ml/interpretabilite
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[SHAP]]", "[[interpreto]]", "[[nnsight]]"]
complements: []
tags: [explainability, deep-learning]
url_docs: https://captum.ai/
url_repo: https://github.com/pytorch/captum
---

# Captum

<!-- AUTO:BANDEAU:START -->
> Bibliothèque d'interprétabilité officielle de PyTorch (Meta) — une trentaine de méthodes d'attribution unifiées (Integrated Gradients, DeepLift, GradCAM, Shapley, TracIn) applicables à n'importe quel modèle PyTorch, entrées comme couches ou neurones.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-04-18 |
<!-- AUTO:BANDEAU:END -->

## Définition

L'outil d'interprétabilité de l'écosystème [[PyTorch]], maintenu par Meta : une trentaine d'algorithmes d'attribution sous une API unique — la famille par gradient (Integrated Gradients, Saliency, SmoothGrad, GradCAM, DeepLift) comme celle par perturbation (Shapley, Occlusion, Feature Ablation). Sa particularité est la **granularité** : Captum n'attribue pas seulement aux entrées, mais aussi aux **couches** (Layer Conductance), aux **neurones** (Neuron Conductance) et jusqu'aux **exemples d'entraînement** (TracIn, fonctions d'influence) — « quelle donnée d'entraînement a causé cette prédiction ? », une question que ni SHAP ni LIME ne posent. La méthode impose une discipline que l'outil ne rappelle pas : Integrated Gradients répond toujours « important **par rapport à quoi** ? », et sa baseline vaut zéro par défaut, ce qui rend les entrées nulles invisibles par construction ; la somme des attributions doit valoir $f(x) - f(\text{baseline})$, contrôle gratuit et presque toujours omis, qu'un écart signale un nombre de pas insuffisant. Enfin une carte d'attribution montre où le modèle regarde, jamais s'il a raison.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Modèle [[PyTorch]], quel qu'il soit — vision, texte, tabulaire, multimodal | Modèle non PyTorch : la bibliothèque est fermée à `torch.autograd` → [[SHAP]] pour un ensemble d'arbres, [[LIME]] pour le reste |
| Attribution par gradient : une rétropropagation plutôt que des milliers de passes de perturbation | Interprétabilité mécaniste : Captum attribue, elle ne rétro-conçoit pas de circuits → [[TransformerLens]] ou [[nnsight]] |
| Attribuer à autre chose que l'entrée : une couche, un neurone, ou les données d'entraînement (TracIn) | Méthodes à base de concepts sur modèles de langage : Captum a TCAV, pas la chaîne complète → [[interpreto]] |
| Comparer plusieurs méthodes d'attribution sans réécrire le code d'accroche | Explication destinée à un métier : elle produit des tenseurs, pas des rapports — la couche de restitution reste à écrire |
| Évaluer la fidélité des attributions : `captum.metrics` (infidelity, sensitivity) | |

## Mise en œuvre

- Installation — `uv add captum` ; dépendance principale `torch`, aucune autre lourde
- Point d'entrée — import Python, un objet par méthode (`IntegratedGradients`, `DeepLift`, `LayerConductance`…) appliqué au modèle ; sur du texte, agréger au niveau du **mot** avant d'afficher, la [[Tokenization|tokenisation]] découpant les mots
- Prérequis — un modèle PyTorch déjà entraîné, et une baseline explicitée
- Exécution — single-node, sur la machine du modèle ; GPU conseillé dès que le modèle est gros, l'attribution restant bien plus légère qu'un entraînement
- Coût — gratuit, BSD-3-Clause ; le coût est le calcul — 20 à 300 passes avant/arrière par explication pour Integrated Gradients, davantage pour les méthodes par perturbation

## Écosystème

### Alternatives

- [[SHAP]] — Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres.
- [[interpreto]] — Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs.
- [[nnsight]] — Bibliothèque d'intervention sur les internes d'un réseau PyTorch — capture et modifie activations et gradients via un contexte à exécution différée, et sait exécuter ces interventions à distance sur des modèles trop gros pour la machine locale (infrastructure NDIF).

## Ressources

- Documentation — https://captum.ai/
- Dépôt — https://github.com/pytorch/captum

## Voir aussi

- [[Attribution par gradient]] — le concept parent : Saliency, IG, SmoothGrad, et pourquoi la saturation impose IG
- [[Explicabilité des modèles]] — le chapeau de la famille
- [[Comparatif - Explicabilité]] — ce qui départage les outils du dossier
- [[Interprétabilité mécaniste]] — l'étage au-dessus, hors de son périmètre
- [[CNN]] — le terrain d'origine de GradCAM
