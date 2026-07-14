---
galaxie: wiki
type: concept
nom: LLM eval metrics
alias: [métriques d'évaluation LLM, évaluation LLM, LLM evaluation, exact match, BLEU, ROUGE, BERTScore, pass@k, G-Eval, offline eval]
categorie: concept/llm
domaines: [ai-eng]
tags: [llm-eval, model-evaluation, llm, nlp]
---

# LLM eval metrics

## Aperçu

- Évaluer un LLM est dur : la sortie est **ouverte** (plusieurs réponses correctes, aucun gold unique) et la qualité est multi-dimensionnelle (exactitude, pertinence, format, ton, sûreté).
- « LLM eval metrics » = le **menu** des façons de noter une sortie. Choisir la métrique, c'est d'abord décider *ce qu'on mesure* et *si on dispose d'une réponse de référence*.

## Concepts clés

### Avec référence (reference-based)
- On compare à une réponse « vérité terrain ».
- **Exact match / accuracy** : tâches fermées (QCM, classification, extraction).
- **Chevauchement de surface** : BLEU, ROUGE (n-grammes) — hérités de la traduction/résumé, corrèlent mal avec la qualité perçue.
- **Similarité sémantique** : BERTScore, similarité d'[[embeddings]] — tolère la reformulation.

### Sans référence (reference-free)
- Pas de gold : un juge note directement la sortie. C'est le rôle du [[LLM-as-judge]] (fidélité, pertinence, critères métier) — devenu l'approche dominante pour le texte libre.

### Par exécution / par tâche
- Quand la sortie est **vérifiable**, on exécute : code → tests unitaires (**pass@k**), maths → vérification du résultat. Cf. [[Code and math benchmarks]]. Métrique objective, sans juge.

### Intrinsèque vs extrinsèque
- **Intrinsèque** : [[Perplexity]] — qualité du modèle de langue, sans tâche. Utile en pré-entraînement, insuffisante pour juger une application.
- **Extrinsèque** : performance sur une tâche réelle (la seule qui compte pour une app).

### Offline vs online
- **Offline** : sur un jeu figé, avant déploiement (CI, [[LLM benchmarks]]).
- **Online** : en production, sur le trafic réel → [[LLM observability]].

## Les maths, simplement

- **pass@k** $= \mathbb{E}\left[\,1 - \dfrac{\binom{n-c}{k}}{\binom{n}{k}}\,\right]$ : probabilité qu'au moins 1 des $k$ échantillons passe, estimée à partir de $n$ générations dont $c$ correctes. Objective dès qu'un vérificateur existe.
- **ROUGE-N** $= \dfrac{\#\,\text{n-grammes communs (réf} \cap \text{généré)}}{\#\,\text{n-grammes de la référence}}$ — rappel de n-grammes ; aveugle au sens, d'où sa faible corrélation au jugement humain.

## En pratique

- Choisir selon la tâche : sortie fermée → exact match ; sortie vérifiable → exécution (pass@k) ; texte libre → [[LLM-as-judge]] + quelques jugements humains pour calibrer.
- Ne jamais se fier à une seule métrique : croiser objectif (exécution), sémantique (BERTScore) et juge.
- Figer un **jeu d'éval versionné** et le rejouer à chaque changement (prompt, modèle, RAG) → détecte les régressions. Outiller : [[Dev/Services/DeepEval|DeepEval]] (assertions en CI), [[Dev/Services/Ragas|Ragas]], [[Dev/Services/TruLens|TruLens]].
- BLEU/ROUGE : à réserver aux tâches proches de la traduction/résumé ; ailleurs, trompeur.

## Approches voisines & alternatives

- [[LLM-as-judge]] — la métrique sans référence dominante pour le texte libre.
- [[RAG eval]] — spécialisation retrieval + génération de ces métriques.
- [[LLM benchmarks]] — ces métriques agrégées sur des suites standardisées.
- [[Code and math benchmarks]] — le cas « éval par exécution ».
- [[Perplexity]] — la métrique intrinsèque, complémentaire.
- [[LLM observability]] — les mêmes métriques, mais en ligne sur le trafic réel.

## Pour aller plus loin

- Liang et al. (2022) — *HELM: Holistic Evaluation of Language Models*.
- Zhang et al. (2020) — *BERTScore: Evaluating Text Generation with BERT*.
- Chen et al. (2021) — *Evaluating Large Language Models Trained on Code* (pass@k).
