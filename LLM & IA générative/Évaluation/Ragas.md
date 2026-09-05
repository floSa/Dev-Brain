---
role: brique
nom: Ragas
alias: [ragas, explodinggradients-ragas]
pitch: "Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG."
categorie: llm/eval
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[DeepEval]]", "[[TruLens]]", "[[promptfoo]]"]
complements: []
tags: [llm, llm-eval, rag-eval, rag]
url_docs: https://docs.ragas.io/
url_repo: https://github.com/explodinggradients/ragas
---

# Ragas

<!-- AUTO:BANDEAU:START -->
> Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'évaluation de systèmes RAG et, plus largement, d'applications LLM. Sa marque de
fabrique : des **métriques sans référence** calculées par [[LLM-as-judge]] — *faithfulness*
(la réponse est-elle fidèle au contexte récupéré ?), *context precision* et *context recall*
(le retrieval a-t-il ramené le bon contexte ?), *answer relevancy* — qui notent un pipeline
sans jeu de réponses « vérité terrain » écrit à la main. C'est le seul de son dossier à
séparer explicitement la qualité du retrieval de celle de la génération. Il génère aussi des
**jeux de tests synthétiques**, questions et contextes, depuis les documents, et s'intègre à
[[LangChain]] et [[LlamaIndex]] ; ses scores peuvent être rattachés aux traces de [[Langfuse]]
ou de [[Phoenix Arize]]. Référence open-source de l'éval RAG, avec un papier à EACL 2024.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Évaluer un pipeline RAG en mesurant séparément retrieval et génération — context precision/recall d'un côté, faithfulness de l'autre | Besoin d'observabilité de production — dashboards, traces, coûts — et pas seulement de scores offline → [[Langfuse]], [[Phoenix Arize]] |
| Démarrer sans dataset annoté : métriques sans référence et génération de jeux de tests synthétiques amorcent l'éval | Métriques LLM-as-judge bruitées et non déterministes : moyenner sur assez d'exemples, fixer le modèle juge et sa version |
| Boucle de dev : comparer deux configurations — chunking, reranking, prompt — sur les mêmes métriques | API 0.x en évolution, métriques et noms remaniés : épingler la version |
| S'appuyer sur un standard reconnu plutôt que de réinventer des métriques maison | Le coût en tokens grimpe vite sur de gros jeux de tests, et un juge faible dégrade la fiabilité des scores — échantillonner, choisir le juge |

## Mise en œuvre

- Installation — `uv add ragas`
- Point d'entrée — des métriques appliquées à un pipeline, ou la génération d'un jeu de tests synthétique depuis les documents
- Prérequis — un modèle juge, API ou local ; son choix est laissé à l'utilisateur et conditionne la fiabilité des scores
- Exécution — mono-nœud, en local ou dans la CI, sans infra propre
- Coût — gratuit sous Apache-2.0 ; le coût réel est en tokens du modèle juge, à chaque évaluation

## Écosystème

### Alternatives

- [[DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- [[TruLens]] — Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.
- [[promptfoo]] — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.

## Ressources

- Documentation — https://docs.ragas.io/
- Dépôt — https://github.com/explodinggradients/ragas

## Voir aussi

- [[RAG eval]] — la notion qu'il met en œuvre
- [[LLM eval metrics]] — la notion du dossier
- [[Comparatif - Évaluation LLM]] — ce qui départage les outils du dossier
