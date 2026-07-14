---
galaxie: dev
type: service
nom: TruLens
alias: [trulens, truera-trulens, trulens-eval]
pitch: "Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability."
categorie: llm/eval
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Ragas|Ragas]]", "[[Dev/Services/DeepEval|DeepEval]]", "[[Dev/Services/promptfoo|promptfoo]]"]
remplace_par: []
status: actif
tags: [llm, llm-eval, tracing, llm-as-judge]
url_docs: https://www.trulens.org/
url_repo: https://github.com/truera/trulens
---

# TruLens

## Pourquoi

Bibliothèque Python d'**évaluation et de traçage** d'apps LLM et d'agents (MIT, créée par **TruEra**, racheté par **Snowflake** en 2024). Son modèle : instrumenter l'app (stack-agnostique) pour capturer les **traces**, puis y attacher des **feedback functions** — des évaluations programmables qui notent chaque étape : *groundedness* (réponse ancrée dans le contexte), *context relevance*, *answer relevance* (le « RAG triad »), mais aussi toxicité, pertinence, critères maison. Les résultats s'explorent dans un tableau de bord local pour comparer des versions. C'est aussi le **socle open-source de Snowflake AI Observability**.

## Quand l'utiliser

- **Évaluer en instrumentant** : noter les étapes internes d'une chaîne/agent, pas seulement la sortie finale.
- Diagnostiquer un **RAG** via le *RAG triad* (groundedness / context relevance / answer relevance).
- Itérer en **comparant des versions** d'app sur les mêmes feedback functions, dashboard à l'appui.
- Écosystème **Snowflake / Cortex** : TruLens est la brique d'observabilité IA native.

## Quand NE PAS l'utiliser

- Éval **RAG offline** rapide sans instrumenter le code → [[Dev/Services/Ragas|Ragas]].
- Harnais de **tests en CI** avec large catalogue de métriques et assertions → [[Dev/Services/DeepEval|DeepEval]].
- **Observabilité de production** multi-équipes (dashboards hébergés, gestion de prompts, coûts) → [[Dev/Services/Langfuse|Langfuse]], [[Dev/Services/LangSmith|LangSmith]], [[Dev/Services/Phoenix Arize|Phoenix Arize]].

## Déploiement & coût

- **Bibliothèque** importée dans l'app, dashboard local (`hosted: self`, `single-node`) ; gratuit (MIT).
- Feedback functions LLM-as-judge = **coût en tokens** du modèle évaluateur (API ou local).
- En production gérée, la version intégrée à **Snowflake AI Observability** s'appuie sur Cortex (coûts Snowflake associés).

## Pièges

- Frontière floue **éval ↔ observabilité** : TruLens trace, mais n'est pas une plateforme de monitoring multi-équipes hébergée — pour ça, voir [[Dev/Services/Langfuse|Langfuse]].
- Feedback functions LLM-as-judge **bruitées** : fixer le modèle, agréger.
- L'instrumentation ajoute une **surcharge** : échantillonner en charge.

## Alternatives

- [[Dev/Services/Ragas|Ragas]] — Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.
- [[Dev/Services/DeepEval|DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- [[Dev/Services/promptfoo|promptfoo]] — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.

## Liens

- Socle de **Snowflake AI Observability** (Cortex).
- Instrumente des apps [[Dev/Services/LangChain|LangChain]] / [[Dev/Services/LlamaIndex|LlamaIndex]].
- Complémentaire des plateformes [[Dev/Services/Langfuse|Langfuse]] / [[Dev/Services/Phoenix Arize|Phoenix Arize]] (observabilité hébergée).
- Concepts : [[LLM eval metrics]], [[LLM-as-judge]] (feedback functions), [[RAG eval]].
- [[Comparatif - Évaluation LLM]] — comparatif de la catégorie
- Doc : https://www.trulens.org/
