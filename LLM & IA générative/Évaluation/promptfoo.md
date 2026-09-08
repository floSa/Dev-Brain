---
role: brique
nom: promptfoo
alias: [promptfoo, promptfoo.dev]
pitch: "Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic."
categorie: llm/eval
famille: cli
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: ["[[DeepEval]]", "[[Ragas]]", "[[TruLens]]"]
complements: []
tags: [llm, llm-eval, testing, ai-security]
url_docs: https://www.promptfoo.dev/docs/intro/
url_repo: https://github.com/promptfoo/promptfoo
---

# promptfoo

<!-- AUTO:BANDEAU:START -->
> Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | production | à jour · 2026-08-28 |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de test et d'évaluation de prompts, d'agents et de pipelines RAG, pensé pour la ligne de
commande et la CI/CD. Sa philosophie est **déclarative** : un fichier YAML versionné décrit
les prompts, les fournisseurs et modèles à comparer, les cas de test et les assertions —
exactitude, contient, similarité sémantique, [[LLM-as-judge]] — puis `promptfoo eval` rend une
matrice de comparaison côte à côte. Second volet, propre à lui dans son dossier : le
**red-teaming**, un scan de vulnérabilités couvrant plus de 50 types (prompt injection,
jailbreak, fuite de données). Écrit en TypeScript et Node.js, avec un wrapper Python, il est
utilisé par OpenAI et Anthropic, et a été racheté par OpenAI en mars 2026.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comparer plusieurs modèles ou prompts sur un jeu de cas et bloquer une régression en CI avant le merge | Besoin d'une observabilité de production continue, et non d'une passe d'éval → [[Langfuse]], [[Phoenix Arize]] |
| Traiter l'éval comme du test déclaratif — un YAML versionné — plutôt que comme du code de test à maintenir | Assertions LLM-as-judge : variance et sensibilité au modèle juge — fixer le modèle, agréger, garder des assertions déterministes quand c'est possible |
| Red-teamer une app LLM : scanner injection de prompt, jailbreak et autres vulnérabilités | Une suite d'éval en CI devient vite lente et coûteuse — échantillonner, mettre en cache |
| Workflow local-first : tout tourne en CLI, sur le poste ou dans le pipeline, sans plateforme imposée | Rachat par OpenAI en mars 2026 : gouvernance et couplage produit à surveiller, même si la licence MIT est annoncée maintenue |

## Mise en œuvre

- Installation — `npx promptfoo`, ou une installation `npm` ; un wrapper Python existe
- Point d'entrée — un fichier YAML de prompts, fournisseurs, cas et assertions, puis `promptfoo eval`
- Prérequis — Node.js ; un modèle juge pour les assertions LLM-as-judge et pour le red-teaming
- Exécution — mono-nœud, en local ou dans la CI
- Coût — gratuit sous MIT ; le coût réel est en tokens, proportionnel au volume de tests ; une offre Enterprise/cloud (partage d'équipe, dashboards) existe en option, le cœur restant utilisable seul

## Écosystème

### Alternatives

- [[DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- [[Ragas]] — Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.
- [[TruLens]] — Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.

## Ressources

- Documentation — https://www.promptfoo.dev/docs/intro/
- Dépôt — https://github.com/promptfoo/promptfoo

## Voir aussi

- [[LLM eval metrics]] — la notion du dossier
- [[AI security]] — ce que couvre son volet red-teaming : prompt injection, jailbreak
- [[RAG eval]] — ce que mesurent ses assertions sur un pipeline RAG
- [[Comparatif - Évaluation LLM]] — ce qui départage les outils du dossier
