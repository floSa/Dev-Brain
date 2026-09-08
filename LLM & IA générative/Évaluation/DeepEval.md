---
role: brique
nom: DeepEval
alias: [deepeval, confident-ai-deepeval]
pitch: "Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option."
categorie: llm/eval
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Ragas]]", "[[TruLens]]", "[[promptfoo]]"]
complements: []
tags: [llm, llm-eval, llm-as-judge, testing]
url_docs: https://deepeval.com/
url_repo: https://github.com/confident-ai/deepeval
---

# DeepEval

<!-- AUTO:BANDEAU:START -->
> Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-06 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'évaluation et de test de LLM souvent décrit comme le **« pytest des LLM »** : on
écrit des cas de test et des assertions (`assert_test`) sur des métriques, exécutables en
local comme en CI, de sorte qu'une régression se bloque avant le merge. Il fournit plus de 50
métriques prêtes à l'emploi — *G-Eval*, qui prend un critère écrit en langage naturel,
hallucination, answer relevancy, métriques RAG, agents, tool-use, conversationnelles, sécurité
et multimodales — assises sur du [[LLM-as-judge]] et sur des modèles NLP tournant en local.
Ses scores s'exportent vers des plateformes d'observabilité comme [[Langfuse]] ou
[[Phoenix Arize]]. L'éditeur Confident AI propose une plateforme managée du même nom, avec
datasets partagés et suivi de régression.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Traiter l'éval LLM comme des tests : assertions, fixtures, intégration pytest et CI | Recherche d'une plateforme d'observabilité complète plutôt que d'un framework de test → [[Langfuse]], [[Phoenix Arize]] |
| Vouloir un large catalogue de métriques couvrant RAG, agents, sécurité et conversation, au-delà du seul RAG | Comme toute métrique LLM-as-judge : variance et sensibilité au modèle juge — fixer le modèle et agréger |
| Définir des critères sur mesure en langage naturel via *G-Eval*, sans coder la métrique | Le couplage à Confident AI est mis en avant : bien distinguer ce qui est OSS (le framework) de ce qui est SaaS |
| Évoluer vers une plateforme partagée sans changer de framework d'éval | Une suite de tests LLM en CI devient vite lente et coûteuse — échantillonner, mettre en cache |

## Mise en œuvre

- Installation — `uv add deepeval`
- Point d'entrée — des cas de test et des assertions `assert_test` sur des métriques, exécutés par pytest
- Prérequis — un modèle juge, API ou local, pour les métriques LLM-as-judge ; certaines métriques s'appuient sur des modèles NLP qui tournent en local
- Exécution — mono-nœud, en local ou dans la CI
- Coût — gratuit sous Apache-2.0 ; le coût réel est en tokens du modèle juge, proportionnel au nombre de tests ; Confident AI est un produit managé séparé et optionnel

## Écosystème

### Alternatives

- [[Ragas]] — Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.
- [[TruLens]] — Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.
- [[promptfoo]] — Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.

## Ressources

- Documentation — https://deepeval.com/
- Dépôt — https://github.com/confident-ai/deepeval

## Voir aussi

- [[LLM eval metrics]] — la notion du dossier
- [[RAG eval]] — ce que mesurent ses métriques RAG
- [[Comparatif - Évaluation LLM]] — ce qui départage les outils du dossier
