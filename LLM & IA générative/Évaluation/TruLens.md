---
role: brique
nom: TruLens
alias: [trulens, truera-trulens, trulens-eval]
pitch: "Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability."
categorie: llm/eval
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Ragas]]", "[[DeepEval]]", "[[promptfoo]]"]
complements: []
tags: [llm, llm-eval, tracing, llm-as-judge]
url_docs: https://www.trulens.org/
url_repo: https://github.com/truera/trulens
---

# TruLens

<!-- AUTO:BANDEAU:START -->
> Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-03 |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'évaluation et de traçage d'apps LLM et d'agents. Son modèle : instrumenter
l'application — le stack importe peu — pour capturer les **traces**, puis y attacher des
**feedback functions**, des évaluations programmables qui notent chaque étape interne et pas
seulement la sortie finale : *groundedness* (la réponse est-elle ancrée dans le contexte ?),
*context relevance*, *answer relevance* — le « RAG triad » —, mais aussi toxicité, pertinence
ou critères maison. Les résultats s'explorent dans un tableau de bord local, ce qui permet de
comparer des versions d'une même app. Créée par TruEra, racheté par Snowflake en 2024, elle
est le socle open-source de **Snowflake AI Observability**.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Évaluer en instrumentant : noter les étapes internes d'une chaîne ou d'un agent, pas seulement sa sortie | La frontière éval ↔ observabilité est floue : TruLens trace, mais n'est pas une plateforme de monitoring multi-équipes hébergée → [[Langfuse]], [[LangSmith]], [[Phoenix Arize]] |
| Diagnostiquer un RAG par le *RAG triad* — groundedness, context relevance, answer relevance | Feedback functions LLM-as-judge bruitées : fixer le modèle évaluateur, agréger les résultats |
| Itérer en comparant des versions d'app sur les mêmes feedback functions, tableau de bord à l'appui | L'instrumentation ajoute une surcharge : échantillonner sous charge |
| Écosystème Snowflake / Cortex, où c'est la brique d'observabilité IA native | |

## Mise en œuvre

- Installation — `uv add trulens`
- Point d'entrée — instrumentation de l'app, puis des feedback functions attachées aux traces ; tableau de bord local pour l'exploration
- Prérequis — un modèle évaluateur, API ou local, pour les feedback functions LLM-as-judge
- Exécution — mono-nœud, bibliothèque importée dans l'app
- Coût — gratuit sous MIT ; le coût réel est en tokens du modèle évaluateur ; en production gérée, la version intégrée à Snowflake AI Observability s'appuie sur Cortex et entraîne les coûts Snowflake associés

## Écosystème

### Alternatives

- [[Ragas]] — Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.
- [[DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- [[promptfoo]] — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.

## Ressources

- Documentation — https://www.trulens.org/
- Dépôt — https://github.com/truera/trulens

## Voir aussi

- [[LLM eval metrics]] — la notion du dossier
- [[LLM-as-judge]] — le mécanisme derrière ses feedback functions ; [[RAG eval]] pour le *RAG triad*
- [[Comparatif - Évaluation LLM]] — ce qui départage les outils du dossier
