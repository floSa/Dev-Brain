---
galaxie: wiki
type: concept
nom: RAG eval
alias: [RAG evaluation, évaluation RAG, évaluation des pipelines RAG, faithfulness, groundedness, context precision, context recall, answer relevancy]
categorie: concept/llm
domaines: [ai-eng]
tags: [rag-eval, llm-eval, rag, retrieval]
---

# RAG eval

## Aperçu

- Évaluer un pipeline [[RAG]], c'est **localiser** où ça rate : le retrieval (a-t-on trouvé les bons passages ?) ou la génération (la réponse est-elle fidèle au contexte et pertinente ?).
- Noter les deux étages **séparément** : une bonne réponse sur un mauvais contexte est un coup de chance, un mauvais contexte plombe tout le reste.

## Concepts clés

### Évaluer le retrieval
- **Context precision** : les passages récupérés sont-ils pertinents et bien classés (le pertinent en tête).
- **Context recall** : a-t-on récupéré **tout** le nécessaire pour répondre.
- Avec un golden set, on retombe sur les [[Reranking|métriques d'ordonnancement]] (NDCG, MRR).

### Évaluer la génération
- **Faithfulness / groundedness** : la réponse s'appuie-t-elle sur le contexte, sans rien inventer au-delà.
- **Answer relevancy** : répond-elle réellement à la question posée.

### Avec ou sans référence
- **Reference-free** : métriques calculées par [[Routing and cascading|un autre LLM]] juge (LLM-as-judge), sans réponse gold — c'est l'approche de [[Dev/Services/Ragas|Ragas]].
- **Avec golden set** : comparaison à des passages / réponses de référence, construits souvent **synthétiquement** (question → passages → réponse).

### La triade RAG
- Formalisée par [[Dev/Services/TruLens|TruLens]] : *context relevance*, *groundedness*, *answer relevance* — un triangle qui couvre retrieval + génération.

## Les maths, simplement

- Faithfulness $\approx \dfrac{\#\,\text{affirmations de la réponse soutenues par le contexte}}{\#\,\text{affirmations totales de la réponse}}$ — proche de 1 = peu d'hallucination.
- Context recall $\approx \dfrac{\#\,\text{passages pertinents récupérés}}{\#\,\text{passages pertinents existants}}$ — exige de connaître la vérité terrain (golden set).

## En pratique

- Outiller : [[Dev/Services/Ragas|Ragas]] (référence open-source, sans référence), [[Dev/Services/DeepEval|DeepEval]] (assertions façon pytest, en CI), [[Dev/Services/TruLens|TruLens]] (tracing + feedback functions).
- Le **LLM-as-judge** a des biais (verbosité, position), du coût et de la variance : fixer le modèle juge, calibrer sur quelques jugements humains avant de lui faire confiance.
- Figer un **golden set** et évaluer en CI à chaque changement : c'est ce qui détecte les régressions quand on ajoute une brique d'[[Advanced RAG]].
- Mesurer **avant** d'optimiser : sans eval, un pipeline avancé masque ses propres régressions.

## Approches voisines & alternatives

- [[RAG]] — le système évalué.
- [[Advanced RAG]] — chaque brique (hybride, reranking, query transform) ne se justifie que mesurée ici.
- [[Query transformations]] — typiquement validées ou recalées par cette éval.
- [[Dev/Services/Ragas|Ragas]], [[Dev/Services/DeepEval|DeepEval]], [[Dev/Services/TruLens|TruLens]] — l'outillage dédié.
- [[LLM-as-judge]] — le mécanisme sous-jacent des métriques reference-free.
- [[LLM eval metrics]] — l'éval LLM générale, dont le RAG eval est la spécialisation retrieval.

## Pour aller plus loin

- Es et al. (2023) — *RAGAS: Automated Evaluation of Retrieval Augmented Generation*.
- Documentation TruLens — *The RAG Triad*.
