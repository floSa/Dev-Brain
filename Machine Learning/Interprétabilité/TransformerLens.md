---
role: brique
nom: TransformerLens
alias: [transformer_lens, HookedTransformer, TransformerBridge]
pitch: "Bibliothèque de référence de l'interprétabilité mécaniste des Transformers — expose les activations et les poids en notation canonique (têtes séparées, flux résiduel décomposé) avec un système de hooks, pour rétro-concevoir les circuits appris."
categorie: ml/interpretabilite
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[nnsight]]", "[[SAELens]]"]
complements: []
tags: [explainability, llm]
url_docs: https://transformerlensorg.github.io/TransformerLens/
url_repo: https://github.com/TransformerLensOrg/TransformerLens
---

# TransformerLens

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de référence de l'interprétabilité mécaniste des Transformers — expose les activations et les poids en notation canonique (têtes séparées, flux résiduel décomposé) avec un système de hooks, pour rétro-concevoir les circuits appris.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-02 |
<!-- AUTO:BANDEAU:END -->

## Définition

L'outil de référence de l'[[Interprétabilité mécaniste|interprétabilité mécaniste]], créé par Neel Nanda, aujourd'hui maintenu par Bryce Meyer et Jonah Larson : la quasi-totalité des résultats publiés du domaine en sont sortis. Sa valeur n'est pas d'exposer des activations — n'importe quel hook PyTorch le fait — mais de **réécrire les poids en notation canonique**. Là où HuggingFace fusionne les têtes d'attention dans une seule matrice pour l'efficacité, TransformerLens les **sépare** et donne accès aux `W_Q`, `W_K`, `W_V`, `W_O` de chaque tête, ainsi qu'au flux résiduel décomposé par composant : c'est ce qui rend le raisonnement en circuits praticable, plutôt que de démêler un tenseur fusionné. Les poids sont donc **retraités**, pas ceux de HuggingFace tels quels — l'intérêt et le risque à la fois, les valeurs numériques pouvant différer légèrement. Le coût dominant est la mémoire : `run_with_cache` conserve tout, et la saturation arrive vite si l'on ne met pas en cache que les hooks nécessaires.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Analyse de circuits : identifier ce que fait un composant, tracer un mécanisme (induction heads, circuit IOI) | Modèle trop gros pour la machine : elle charge tout localement → [[nnsight]] et son exécution distante |
| Activation patching et ablation : le système de hooks est fait pour intervenir en cours de passe | Entraîner ou analyser des **SAE** : la partie a été sortie du projet à la v2 → [[SAELens]] (`HookedSAETransformer`) |
| Raisonner en têtes d'attention séparées ou en flux résiduel décomposé — la notation canonique est l'argument décisif | Simple attribution : hors sujet → [[Captum]] ou [[interpreto]] |
| Modèles GPT-style de taille petite à moyenne : plus de 9 000 modèles portés, 50+ familles d'architectures | Production : outil de recherche, coûteux en mémoire puisqu'il conserve les activations |
| Reproduire un résultat publié du domaine — l'écosystème et les notebooks sont écrits pour elle | Architecture exotique non portée : le passage à la notation canonique se fait modèle par modèle |

## Mise en œuvre

- Installation — `uv add transformer_lens` ; la **v3 a changé l'interface**, `TransformerBridge` étant le point d'entrée et `HookedTransformer` déprécié bien que disponible — beaucoup de notebooks en ligne visent encore l'ancienne API, épingler la version
- Point d'entrée — import Python : charger un modèle porté, puis `run_with_cache` et les hooks
- Prérequis — `torch`, `transformers`, `einops` ; l'essentiel du domaine se fait sur GPT-2 small, qui tourne sur un GPU grand public voire en CPU
- Exécution — single-node, entièrement local
- Coût — gratuit, MIT ; le coût réel est la **mémoire**, l'analyse conservant les activations de toutes les couches

## Écosystème

### Alternatives

- [[nnsight]] — Bibliothèque d'intervention sur les internes d'un réseau PyTorch — capture et modifie activations et gradients via un contexte à exécution différée, et sait exécuter ces interventions à distance sur des modèles trop gros pour la machine locale (infrastructure NDIF).
- [[SAELens]] — Écosystème dédié aux sparse autoencoders sur modèles de langage — entraînement, catalogue de SAE pré-entraînés et outillage d'analyse des features, en intégration étroite avec TransformerLens.

## Ressources

- Documentation — https://transformerlensorg.github.io/TransformerLens/
- Dépôt — https://github.com/TransformerLensOrg/TransformerLens

## Voir aussi

- [[Interprétabilité mécaniste]] — le concept parent : circuits, patching, ablation, steering ; et pourquoi l'ablation à zéro fabrique des artefacts
- [[Superposition]] — l'obstacle que l'analyse par composant rencontre
- [[Sparse autoencoders]] — le démêlage, désormais confié à un outil dédié
- [[Transformer architectures]] · [[Self-attention]] — l'objet d'étude, et la structure que la notation canonique rend lisible
- [[Comparatif - Explicabilité]] — ce qui départage les outils du dossier
- [[HuggingFace]] — la source des poids, avant retraitement
