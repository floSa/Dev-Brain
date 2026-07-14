---
galaxie: dev
type: service
nom: promptfoo
alias: [promptfoo, promptfoo.dev]
pitch: "Outil open-source de test et d'éval de prompts/agents/RAG en CLI et CI (MIT, racheté par OpenAI en 2026) — configs YAML déclaratives, comparaison de modèles et red-teaming/scan de vulnérabilités ; utilisé par OpenAI et Anthropic."
categorie: llm/eval
licence_type: open-source
hosted: self
maturite: production
langage: TypeScript
scaling: single-node
alternatives: ["[[Dev/Services/DeepEval|DeepEval]]", "[[Dev/Services/Ragas|Ragas]]", "[[Dev/Services/TruLens|TruLens]]"]
remplace_par: []
status: actif
tags: [llm, llm-eval, testing, ai-security]
url_docs: https://www.promptfoo.dev/docs/intro/
url_repo: https://github.com/promptfoo/promptfoo
---

# promptfoo

## Pourquoi

Outil **open-source** (MIT) de **test et d'évaluation** de prompts, d'agents et de pipelines RAG, pensé pour la **ligne de commande** et la **CI/CD**. La philosophie est **déclarative** : on décrit dans un **fichier YAML** les prompts, les fournisseurs/modèles à comparer, les cas de test et les **assertions** (exactitude, contient, similarité sémantique, **LLM-as-judge**…), puis `promptfoo eval` produit une **matrice de comparaison** côte à côte. Deuxième volet : le **red-teaming / scan de vulnérabilités** (50+ types : prompt injection, jailbreak, fuite de données…). Écrit en **TypeScript/Node.js** (wrapper Python disponible), **utilisé par OpenAI et Anthropic**, et **racheté par OpenAI en mars 2026** — reste open-source MIT.

## Quand l'utiliser

- **Comparer** plusieurs modèles/prompts sur un jeu de cas et bloquer une **régression en CI** avant merge.
- Traiter l'éval comme du **test déclaratif** (YAML versionné) plutôt que comme du code de test à maintenir.
- **Red-team** une app LLM : scanner injection de prompt, jailbreak et autres vulnérabilités.
- Workflow **local-first** : tout tourne en CLI sur le poste/dans le pipeline, sans plateforme imposée.

## Quand NE PAS l'utiliser

- Éval **RAG spécialisée** (faithfulness, context precision/recall reference-free) → [[Dev/Services/Ragas|Ragas]].
- Éval **« pytest des LLM »** intégrée au framework de test Python → [[Dev/Services/DeepEval|DeepEval]].
- **Tracer et noter** une app instrumentée au fil de l'exécution → [[Dev/Services/TruLens|TruLens]].
- Besoin d'une **observabilité de production** continue (et non d'une passe d'éval) → [[Dev/Services/Langfuse|Langfuse]], [[Dev/Services/Phoenix Arize|Phoenix Arize]].

## Déploiement & coût

- **CLI/bibliothèque** lancée en local et en CI (`hosted: self`, `single-node`), gratuit (MIT) ; install via `npx`/`npm`.
- Les assertions **LLM-as-judge** et le red-teaming appellent un modèle → **coût en tokens** proportionnel au volume de tests.
- Une offre **Enterprise/cloud** (partage d'équipe, dashboards) existe en option ; le cœur reste utilisable seul.

## Pièges

- Métriques **LLM-as-judge** = variance et sensibilité au modèle juge : fixer le modèle, agréger, garder des assertions déterministes quand c'est possible.
- Une suite d'éval en CI peut devenir **lente et coûteuse** — échantillonner et mettre en cache.
- **Rachat OpenAI (2026)** : surveiller l'évolution de la gouvernance et du couplage produit, même si la licence MIT est annoncée maintenue.

## Alternatives

- [[Dev/Services/DeepEval|DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- [[Dev/Services/Ragas|Ragas]] — Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.
- [[Dev/Services/TruLens|TruLens]] — Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.

## Liens

- Couvre aussi le **red-teaming** : recoupe les concepts de [[AI security]] (prompt injection, jailbreak).
- Évalue des apps bâties avec [[Dev/Services/LangChain|LangChain]] / [[Dev/Services/LlamaIndex|LlamaIndex]] ; compare des modèles servis via [[Dev/Services/OpenRouter|OpenRouter]] / [[Dev/Services/LiteLLM|LiteLLM]].
- Concepts : [[LLM eval metrics]], [[LLM-as-judge]], [[RAG eval]], [[AI security]].
- [[Comparatif - Évaluation LLM]] — comparatif de la catégorie
- Doc : https://www.promptfoo.dev/docs/intro/
