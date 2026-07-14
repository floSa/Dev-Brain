---
galaxie: dev
type: service
nom: Ragas
alias: [ragas, explodinggradients-ragas]
pitch: "Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG."
categorie: llm/eval
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/DeepEval|DeepEval]]", "[[Dev/Services/TruLens|TruLens]]", "[[Dev/Services/promptfoo|promptfoo]]"]
remplace_par: []
status: actif
tags: [llm, llm-eval, rag-eval, rag]
url_docs: https://docs.ragas.io/
url_repo: https://github.com/explodinggradients/ragas
---

# Ragas

## Pourquoi

Framework Python d'**évaluation** de systèmes RAG et, plus largement, d'applications LLM (Apache-2.0, projet explodinggradients). Sa marque de fabrique : des **métriques sans référence** (reference-free) calculées par **LLM-as-judge** — *faithfulness* (la réponse est-elle fidèle au contexte récupéré ?), *context precision/recall* (le retrieval a-t-il ramené le bon contexte ?), *answer relevancy* — qui permettent de noter un pipeline sans jeu de réponses « vérité terrain » écrit à la main. Il génère aussi des **jeux de tests synthétiques** (questions + contextes) depuis les documents, et s'intègre aux frameworks d'app ([[Dev/Services/LangChain|LangChain]], [[Dev/Services/LlamaIndex|LlamaIndex]]). C'est la référence open-source de l'éval RAG (papier EACL 2024).

## Quand l'utiliser

- **Évaluer un pipeline RAG** : mesurer séparément la qualité du retrieval et de la génération (context precision/recall vs faithfulness).
- Démarrer **sans dataset annoté** : les métriques reference-free et la génération de test sets synthétiques amorcent l'éval.
- **Boucle de dev** : comparer deux configurations (chunking, reranking, prompt) sur les mêmes métriques.
- S'appuyer sur un standard reconnu plutôt que de réinventer des métriques maison.

## Quand NE PAS l'utiliser

- Besoin d'un **harnais de tests** large (assertions pytest, métriques agents/sécurité, CI) → [[Dev/Services/DeepEval|DeepEval]].
- Besoin de **tracer et noter en continu** une app instrumentée, au-delà du RAG → [[Dev/Services/TruLens|TruLens]].
- Besoin d'**observabilité de production** (dashboards, traces, coûts) et pas seulement de scores offline → [[Dev/Services/Langfuse|Langfuse]], [[Dev/Services/Phoenix Arize|Phoenix Arize]].

## Déploiement & coût

- **Bibliothèque** importée dans le code (`pip`/`uv`), exécutée en local ou en CI : pas d'infra propre (`hosted: self`, `single-node`).
- Gratuit (Apache-2.0). Le coût réel vient des **appels LLM** des métriques LLM-as-judge : chaque évaluation consomme des tokens du modèle juge.
- Choix du modèle juge (API ou local) laissé à l'utilisateur — un juge faible dégrade la fiabilité des scores.

## Pièges

- Les métriques LLM-as-judge sont **bruitées et non déterministes** : moyenner sur assez d'exemples, fixer le modèle juge et sa version.
- **API en évolution** (0.x → métriques et noms remaniés) : épingler la version.
- Le coût en tokens **grimpe vite** sur de gros jeux de tests — échantillonner.

## Alternatives

- [[Dev/Services/DeepEval|DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- [[Dev/Services/TruLens|TruLens]] — Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.
- [[Dev/Services/promptfoo|promptfoo]] — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.

## Liens

- Peut alimenter les plateformes [[Dev/Services/Langfuse|Langfuse]] / [[Dev/Services/Phoenix Arize|Phoenix Arize]] (scores Ragas rattachés aux traces).
- Évalue des pipelines bâtis avec [[Dev/Services/LangChain|LangChain]] / [[Dev/Services/LlamaIndex|LlamaIndex]].
- Concepts : [[RAG eval]], [[LLM eval metrics]], [[LLM-as-judge]] (métriques reference-free).
- [[Comparatif - Évaluation LLM]] — comparatif de la catégorie
- Doc : https://docs.ragas.io/
