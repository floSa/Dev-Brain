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
complements: []
tags: [model-evaluation, nlp, benchmark]
url_docs: https://huggingface.co/docs/evaluate
url_repo: https://github.com/huggingface/evaluate
---

# evaluate

## Pourquoi

Bibliothèque de l'écosystème [[HuggingFace]] qui standardise le **calcul de métriques d'évaluation**. Au lieu de réimplémenter accuracy, F1, BLEU, ROUGE, METEOR ou exact-match, on charge la métrique depuis le Hub (`evaluate.load("accuracy")`) et on l'alimente (`add_batch` / `compute`). Trois familles d'objets : **metrics** (qualité du modèle vs références), **comparisons** (deux modèles entre eux) et **measurements** (propriétés d'un dataset). Chaque métrique est versionnée sur le Hub avec sa carte et ses dépendances, ce qui rend les scores **reproductibles et comparables** entre projets. S'intègre directement au `Trainer` de `transformers`.

## Quand l'utiliser

- **Évaluer un modèle** sur des métriques standard sans les réécrire (NLP surtout : BLEU/ROUGE/exact-match).
- **Boucle d'entraînement / `Trainer`** : passer une métrique `evaluate` comme `compute_metrics`.
- Besoin de **scores comparables** à la littérature (mêmes implémentations versionnées que les benchmarks publics).
- Mesurer des **propriétés de dataset** (word count, label distribution) via les *measurements*.

## Quand NE PAS l'utiliser

- **Évaluation de systèmes LLM / RAG / agents** (faithfulness, juge LLM) → [[Ragas]], [[DeepEval]], ou la bibliothèque **LightEval** que HuggingFace recommande désormais pour les LLM.
- Métriques ML classiques déjà couvertes par [[Scikit-Learn]] dans un pipeline sklearn : `sklearn.metrics` évite une dépendance de plus.
- Tracking / dashboards de runs → [[MLflow]], [[Weights & Biases]] (evaluate calcule, ne journalise pas).

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add evaluate`. Rien à héberger.
- Les métriques sont **téléchargées depuis le Hub** au premier `load` (puis cachées) — accès réseau initial requis.
- Certaines métriques tirent des dépendances lourdes (ex. `sacrebleu`, `rouge_score`, `bert_score`) installées à part.

## Pièges

- **Maintenance ralentie** : dernière version 0.4.6 (sept. 2025), stable mais peu d'évolutions ; pour l'évaluation de LLM, HuggingFace pointe vers **LightEval**. Convient encore très bien aux métriques classiques.
- `evaluate.load` exécute le **script de la métrique** depuis le Hub : n'utiliser que des métriques de confiance.
- Format d'entrée strict par métrique (`predictions`/`references`) : un mauvais shape donne un score faux sans erreur explicite.
- BLEU/ROUGE ont plusieurs variantes (tokenisation, lissage) : vérifier qu'on compare bien la même implémentation que la baseline.

## Alternatives

Pas de substitut direct dans le brain pour ce créneau (jeu de métriques ML réutilisables et versionnées) : les fiches voisines couvrent des besoins distincts — `sklearn.metrics` pour un pipeline scikit-learn, ou les évaluateurs LLM (cf. *Quand NE PAS l'utiliser* et *Liens*).

## Liens

- [[HuggingFace]] — bibliothèque sœur ; `compute_metrics` du `Trainer`.
- [[datasets]] — même mécanisme de chargement depuis le Hub ; fournit les références d'évaluation.
- [[Scikit-Learn]] — `sklearn.metrics` pour le ML tabulaire.
- [[seqeval]] — métriques d'étiquetage de séquence (NER) au niveau entité ; chargé par evaluate sous la métrique `seqeval`.
- [[Ragas]] · [[DeepEval]] — évaluation spécifique des systèmes LLM/RAG.
- [[Classification metrics]] · [[Ranking metrics]] — les concepts derrière les métriques calculées.
- Doc : https://huggingface.co/docs/evaluate
