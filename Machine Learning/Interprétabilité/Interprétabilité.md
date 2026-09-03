---
role: hub
nom: Interprétabilité
alias: [explicabilité, XAI]
pitch: Rendre compte d'une prédiction — ce qui l'a causée pour le métier, et ce qui se passe à l'intérieur du réseau pour le chercheur.
domaines: [ml-eng, data-sci, ai-eng]
tags: [explainability, deep-learning, transformers, llm, model-evaluation]
---

# Interprétabilité

> Rendre compte d'une prédiction — ce qui l'a causée pour le métier, et ce qui se passe à l'intérieur du réseau pour le chercheur.

## Ce qu'il faut comprendre

- **Ce dossier range deux métiers qui portent le même nom et ne servent pas le même public.** L'**explicabilité post-hoc** attribue une prédiction à des variables d'entrée, sur un modèle qu'on traite comme une boîte noire : c'est ce qu'on montre à un métier ou à un régulateur. L'**interprétabilité mécaniste** ouvre le réseau pour comprendre *comment* il calcule : c'est un travail de recherche, sur des Transformers, et il ne produit pas de justification exploitable en production. Confondre les deux fait choisir le mauvais outil dans les deux sens.
- **Une explication n'est pas une cause**, et c'est la limite à énoncer avant d'en produire une. Une attribution dit ce qui a pesé dans *ce* modèle sur *ce* point, pas ce qui provoque le phénomène dans le monde. La causalité relève de [[Statistiques & inférence]]. [[Explicabilité des modèles]] pose le cadre général.
- **Deux familles d'attribution post-hoc, deux compromis.** Les valeurs de Shapley donnent des attributions cohérentes, additives et théoriquement fondées, mais coûteuses — sauf sur les modèles à arbres, où un algorithme exact les rend immédiates ; c'est pour ça qu'elles sont le défaut sur [[Tabulaire]]. Les surrogates locaux, eux, sont rapides et applicables à n'importe quoi, mais leurs explications sont instables d'une exécution à l'autre. Sur réseaux profonds, une troisième voie utilise le gradient — [[Attribution par gradient]].
- **L'interprétabilité mécaniste a son propre vocabulaire**, et il faut le lire avant de toucher aux outils : [[Interprétabilité mécaniste]] pour le programme, [[Superposition]] pour le problème central — un réseau encode plus de concepts qu'il n'a de neurones, donc un neurone ne veut rien dire à lui seul — et [[Sparse autoencoders]] pour la réponse la plus travaillée aujourd'hui, qui cherche à démêler ces concepts. [[Probing]] est la technique de base : entraîner un classifieur léger sur des activations pour savoir ce qu'elles contiennent.
- **Sur du texte et des images, l'explication doit être posée sur la bonne unité.** Attribuer à des tokens sous-mot ne parle à personne ; les approches à base de concepts remontent d'un cran, et c'est ce qui rend une explication montrable.
- Un usage souvent oublié de ces outils est le **débogage**, pas la conformité : une attribution qui pointe une variable absurde révèle presque toujours un [[Data leakage]] — c'est le rendement le plus élevé de ce dossier.

## Choisir

- Une explication à montrer à un métier, sur du tabulaire ou des arbres → [[SHAP]], et son TreeSHAP exact.
- Une explication locale rapide, sur n'importe quel modèle, en acceptant l'instabilité → [[LIME]].
- Des attributions sur un réseau PyTorch, texte ou image → [[Captum]].
- Expliquer un modèle de langage HuggingFace, par attributions ou par concepts → [[interpreto]]. Cf. [[Comparatif - Explicabilité]].
- Lire et manipuler les internes d'un Transformer en notation canonique → [[TransformerLens]].
- Intervenir sur les activations d'un réseau, y compris à distance sur un gros modèle → [[nnsight]].
- Entraîner ou réutiliser des sparse autoencoders → [[SAELens]].
- Surveiller la dérive plutôt qu'expliquer une prédiction → [[Evidently]], au niveau du domaine.

<!-- AUTO:START -->
### Notions
- [[Attribution par gradient]] — domaines : data-sci, ml-eng
- [[Interprétabilité mécaniste]] — domaines : ai-eng, data-sci
- [[Probing]] — domaines : data-sci, ai-eng
- [[Sparse autoencoders]] — domaines : data-sci, ai-eng
- [[Superposition]] — domaines : data-sci, ai-eng

### Briques
- [[Captum]] — Bibliothèque d'interprétabilité officielle de PyTorch (Meta) — une trentaine de méthodes d'attribution unifiées (Integrated Gradients, DeepLift, GradCAM, Shapley, TracIn) applicables à n'importe quel modèle PyTorch, entrées comme couches ou neurones.
- [[interpreto]] — Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs.
- [[LIME]] — Explications locales model-agnostic par surrogate linéaire — perturbe autour d'un point et ajuste un modèle simple interprétable ; rapide et générique (tabulaire, texte, image), mais explications instables et purement locales ; dépôt sans commit depuis juillet 2021, dernière release en juin 2020 — préférer SHAP.
- [[nnsight]] — Bibliothèque d'intervention sur les internes d'un réseau PyTorch — capture et modifie activations et gradients via un contexte à exécution différée, et sait exécuter ces interventions à distance sur des modèles trop gros pour la machine locale (infrastructure NDIF).
- [[SAELens]] — Écosystème dédié aux sparse autoencoders sur modèles de langage — entraînement, catalogue de SAE pré-entraînés et outillage d'analyse des features, en intégration étroite avec TransformerLens.
- [[SHAP]] — Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres.
- [[TransformerLens]] — Bibliothèque de référence de l'interprétabilité mécaniste des Transformers — expose les activations et les poids en notation canonique (têtes séparées, flux résiduel décomposé) avec un système de hooks, pour rétro-concevoir les circuits appris.

### Comparatifs
- [[Comparatif - Explicabilité]]
<!-- AUTO:END -->

## Notes
