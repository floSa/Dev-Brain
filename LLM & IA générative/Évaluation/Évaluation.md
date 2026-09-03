---
role: hub
nom: Évaluation
alias: [éval LLM, évaluation LLM]
pitch: Mesurer ce que vaut une application LLM sur un jeu de tests — avant la production, et de façon rejouable.
domaines: [ai-eng, mlops]
tags: [llm-eval, benchmark, rag-eval, llm-as-judge, model-evaluation]
---

# Évaluation

> Mesurer ce que vaut une application LLM sur un jeu de tests — avant la production, et de façon rejouable.

## Ce qu'il faut comprendre

- **Sans éval, il n'y a pas de progrès mesurable**, et c'est la faiblesse la plus répandue des applications LLM : elle ne se voit pas de l'intérieur, parce qu'un système qui répond toujours quelque chose a toujours l'air de marcher.
- Ce dossier est l'**offline** : un jeu figé, un score reproductible, un test qu'on rejoue en CI. Le pendant **online** — le trafic réel, les traces, le coût — est dans [[Observabilité des LLM]]. Les deux se ressemblent au point qu'on achète l'une pour l'autre ; elles ne répondent pas à la même question.
- **Trois mailles, souvent confondues.** [[LLM eval metrics]] est le menu des façons de noter une sortie ; un **benchmark** est une métrique appliquée à une suite figée ([[LLM benchmarks]], [[RAG benchmarks]], [[Code and math benchmarks]]) ; une **éval maison** est la même mécanique sur son propre golden set. Un benchmark public compare des modèles, il ne dit rien de votre produit.
- La difficulté propre au domaine est qu'**il n'y a pas de réponse de référence unique**. D'où [[LLM-as-judge]], qui note du texte libre à l'échelle — en assumant que le juge est lui-même un modèle biaisé, à calibrer contre des annotations humaines avant d'y croire.
- **Un pipeline se localise, un agent se trace.** [[RAG eval]] note séparément le retrieval et la génération, parce qu'un bon score global sur un mauvais contexte n'apprend rien. [[Agent evaluation]] juge une **trajectoire** entière — étapes, appels d'outils, coût, latence — pas une réponse isolée.
- Le seul cas où la vérification est **mécanique** est celui où l'on peut exécuter le résultat : [[Code and math benchmarks]]. C'est le terrain des [[Reasoning models]], et la raison pour laquelle leurs progrès y sont plus crédibles que sur le texte libre.

## Choisir

- Mesurer un pipeline RAG, métriques prêtes à l'emploi → [[Ragas]].
- En faire des tests exécutés en CI, façon pytest → [[DeepEval]].
- Comparer des prompts et des modèles, chercher les régressions et les failles → [[promptfoo]].
- Instrumenter un stack existant sans le réécrire → [[TruLens]].
- Regarder le trafic réel plutôt qu'un jeu figé → [[Observabilité des LLM]].
- Évaluer un modèle ML classique (accuracy, F1, BLEU) plutôt qu'un système LLM → [[Machine Learning]].

<!-- AUTO:START -->
### Notions
- [[Agent evaluation]] — domaines : ai-eng
- [[Code and math benchmarks]] — domaines : ai-eng, ml-eng
- [[LLM benchmarks]] — domaines : ai-eng, ml-eng
- [[LLM eval metrics]] — domaines : ai-eng
- [[LLM-as-judge]] — domaines : ai-eng
- [[RAG benchmarks]] — domaines : ai-eng
- [[RAG eval]] — domaines : ai-eng

### Briques
- [[DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- [[promptfoo]] — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.
- [[Ragas]] — Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.
- [[TruLens]] — Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.

### Comparatifs
- [[Comparatif - Évaluation LLM]]
<!-- AUTO:END -->
