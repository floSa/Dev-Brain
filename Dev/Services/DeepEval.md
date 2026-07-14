---
galaxie: dev
type: service
nom: DeepEval
alias: [deepeval, confident-ai-deepeval]
pitch: "Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option."
categorie: llm/eval
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Ragas|Ragas]]", "[[Dev/Services/TruLens|TruLens]]", "[[Dev/Services/promptfoo|promptfoo]]"]
remplace_par: []
status: actif
tags: [llm, llm-eval, llm-as-judge, testing]
url_docs: https://deepeval.com/
url_repo: https://github.com/confident-ai/deepeval
---

# DeepEval

## Pourquoi

Framework Python d'**évaluation et de test** de LLM (Apache-2.0, éditeur Confident AI), souvent décrit comme le **« pytest des LLM »** : on écrit des cas de test et des assertions (`assert_test`) sur des métriques, exécutables localement et en **CI**. Il fournit **50+ métriques** prêtes à l'emploi — *G-Eval* (critères en langage naturel), hallucination, answer relevancy, métriques **RAG**, **agents**, **tool-use**, conversationnelles, **sécurité** et multimodales — basées sur du **LLM-as-judge** et des modèles NLP qui tournent en local. Il s'intègre nativement à la plateforme managée **Confident AI** (datasets partagés, suivi de régression, monitoring de prod) pour les équipes.

## Quand l'utiliser

- Traiter l'éval LLM comme des **tests** : assertions, fixtures, intégration **pytest** et **CI** (bloquer une régression avant merge).
- Besoin d'un **large catalogue de métriques** couvrant RAG, agents, sécurité et conversation, au-delà du seul RAG.
- Définir des critères **sur mesure** en langage naturel via *G-Eval* sans coder la métrique.
- Évoluer vers une plateforme partagée (Confident AI) sans changer de framework d'éval.

## Quand NE PAS l'utiliser

- Périmètre **strictement RAG** avec métriques reference-free reconnues → [[Dev/Services/Ragas|Ragas]] est plus direct.
- Besoin de **tracer/noter une app instrumentée** au fil de l'exécution → [[Dev/Services/TruLens|TruLens]].
- Recherche d'une **plateforme d'observabilité** complète (et pas un framework de test) → [[Dev/Services/Langfuse|Langfuse]], [[Dev/Services/Phoenix Arize|Phoenix Arize]].

## Déploiement & coût

- **Bibliothèque** importée et lancée en local/CI (`hosted: self`, `single-node`) ; gratuit (Apache-2.0).
- Métriques **LLM-as-judge** = appels à un modèle juge (API ou local) : coût en tokens proportionnel au nombre de tests.
- **Confident AI** est un produit managé séparé (SaaS) — optionnel, le framework reste utilisable seul.

## Pièges

- Comme toute métrique LLM-as-judge : **variance** et sensibilité au modèle juge — fixer le modèle et agréger.
- Couplage **Confident AI** mis en avant : bien distinguer ce qui est OSS (le framework) de ce qui est SaaS.
- Une suite de tests LLM en CI peut devenir **lente et coûteuse** — échantillonner, mettre en cache.

## Alternatives

- [[Dev/Services/Ragas|Ragas]] — Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.
- [[Dev/Services/TruLens|TruLens]] — Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.
- [[Dev/Services/promptfoo|promptfoo]] — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.

## Liens

- Scores exportables vers des plateformes d'observabilité comme [[Dev/Services/Langfuse|Langfuse]] / [[Dev/Services/Phoenix Arize|Phoenix Arize]].
- Évalue des apps bâties avec [[Dev/Services/LangChain|LangChain]] / [[Dev/Services/LlamaIndex|LlamaIndex]].
- Concepts : [[LLM eval metrics]], [[LLM-as-judge]] (G-Eval), [[RAG eval]].
- [[Comparatif - Évaluation LLM]] — comparatif de la catégorie
- Doc : https://deepeval.com/
