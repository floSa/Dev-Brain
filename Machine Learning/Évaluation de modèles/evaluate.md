---
role: brique
nom: evaluate
alias: [hf evaluate, huggingface evaluate, 🤗 evaluate]
pitch: "Bibliothèque HuggingFace de métriques d'évaluation ML prêtes à l'emploi — accuracy, F1, BLEU, ROUGE, exact match… chargées depuis le Hub via une API unique load/compute, comparables d'un projet à l'autre."
categorie: ml/eval
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[seqeval]]"]
tags: [model-evaluation, nlp, benchmark]
url_docs: https://huggingface.co/docs/evaluate
url_repo: https://github.com/huggingface/evaluate
---

# evaluate

<!-- AUTO:BANDEAU:START -->
> Bibliothèque HuggingFace de métriques d'évaluation ML prêtes à l'emploi — accuracy, F1, BLEU, ROUGE, exact match… chargées depuis le Hub via une API unique load/compute, comparables d'un projet à l'autre.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Une standardisation du **calcul des métriques d'évaluation**. Au lieu de réimplémenter accuracy, F1, BLEU, ROUGE, METEOR ou exact-match, on charge la métrique depuis le Hub (`evaluate.load("accuracy")`) et on l'alimente (`add_batch`, `compute`). Trois familles d'objets : **metrics** (qualité du modèle face à des références), **comparisons** (deux modèles entre eux) et **measurements** (propriétés d'un jeu de données). Chaque métrique est versionnée sur le Hub avec sa carte et ses dépendances, ce qui rend les scores reproductibles et comparables entre projets — c'est le point, plus que le calcul lui-même. Deux conséquences du mécanisme : `evaluate.load` **exécute le script de la métrique** téléchargé depuis le Hub, ce qui impose de n'utiliser que des métriques de confiance ; et le format d'entrée est strict par métrique (`predictions`, `references`), un mauvais shape donnant un score faux sans erreur explicite. Enfin BLEU et ROUGE existent en plusieurs variantes de tokenisation et de lissage : comparer suppose la même implémentation que la baseline.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Évaluer un modèle sur des métriques standard sans les réécrire, en NLP surtout (BLEU, ROUGE, exact-match) | Évaluation de systèmes LLM, RAG ou agents — faithfulness, juge LLM → [[Ragas]], [[DeepEval]], ou LightEval que HuggingFace recommande désormais pour les LLM |
| Boucle d'entraînement ou `Trainer` : passer une métrique en `compute_metrics` | Métriques ML classiques déjà couvertes dans un pipeline sklearn : `sklearn.metrics` évite une dépendance → [[Scikit-Learn]] |
| Besoin de scores comparables à la littérature : mêmes implémentations versionnées que les benchmarks publics | Suivi de runs et tableaux de bord : evaluate calcule, il ne journalise pas → [[MLflow]], [[Weights & Biases]] |
| Mesurer des propriétés de jeu de données — nombre de mots, distribution des labels — via les *measurements* | |

## Mise en œuvre

- Installation — `uv add evaluate` ; dernière version 0.4.6 (sept. 2025), stable mais peu d'évolutions — pour l'évaluation de LLM, l'amont pointe vers LightEval
- Point d'entrée — `evaluate.load("<métrique>")`, puis `add_batch` et `compute`
- Prérequis — un accès réseau au premier `load`, la métrique étant téléchargée depuis le Hub puis mise en cache ; certaines tirent des dépendances lourdes installées à part (`sacrebleu`, `rouge_score`, `bert_score`)
- Exécution — dans le process appelant, rien à héberger
- Coût — gratuit, Apache-2.0

## Écosystème

### Alternatives

- Pas de substitut direct dans le brain pour ce créneau — un jeu de métriques ML réutilisables et versionnées. Les fiches voisines couvrent des besoins distincts : `sklearn.metrics` pour un pipeline scikit-learn, les évaluateurs dédiés pour les systèmes LLM.

### Compléments

- [[seqeval]] — Calcul des métriques d'étiquetage de séquence au niveau entité (F1, precision, recall) pour la NER et le chunking — schémas IOB1/2, IOE1/2, IOBES, BILOU, mode strict compatible conlleval ; la référence pour scorer un tagger. — chargé par evaluate sous la métrique `seqeval`.

## Ressources

- Documentation — https://huggingface.co/docs/evaluate
- Dépôt — https://github.com/huggingface/evaluate

## Voir aussi

- [[Évaluation de modèles]] — le hub du domaine
- [[Classification metrics]] · [[Ranking metrics]] — les concepts derrière les métriques calculées
- [[HuggingFace]] — bibliothèque sœur ; le `compute_metrics` de son `Trainer`
- [[datasets]] — même mécanisme de chargement depuis le Hub, et la source des références d'évaluation
