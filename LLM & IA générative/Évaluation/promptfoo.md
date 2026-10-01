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
alternatives: ["[[DeepEval]]", "[[Ragas]]", "[[TruLens]]", "[[Inspect AI]]", "[[garak]]"]
complements: []
tags: [llm, llm-eval, testing, ai-security, red-teaming]
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
**red-teaming**, un scan de vulnérabilités fait de **plugins** (types de vulnérabilité :
prompt injection, jailbreak, fuite de données, contenu nocif) et de **stratégies** (techniques
d'attaque appliquées aux plugins). Écrit en TypeScript et Node.js, avec un wrapper Python, il est
utilisé par OpenAI et Anthropic, et a été racheté par OpenAI en mars 2026. Relevé le 2026-10-01 :
**v0.123.1** (2026-09-18), environ 25 600 étoiles ; le README affirme que le projet reste sous
licence MIT après le rachat (texte du fichier `LICENSE` relu le même jour).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Comparer plusieurs modèles ou prompts sur un jeu de cas et bloquer une régression en CI avant le merge | Besoin d'une observabilité de production continue, et non d'une passe d'éval → [[Langfuse]], [[Phoenix Arize]] |
| Traiter l'éval comme du test déclaratif — un YAML versionné — plutôt que comme du code de test à maintenir | Assertions LLM-as-judge : variance et sensibilité au modèle juge — fixer le modèle, agréger, garder des assertions déterministes quand c'est possible |
| Red-teamer une app LLM : scanner injection de prompt, jailbreak et autres vulnérabilités | Un red-teaming strictement **hors ligne** : par défaut la génération des attaques passe par un service distant de l'éditeur (voir *Prérequis*) → [[garak]], dont les sondes sont des prompts fixes lancés en local |
| | Une suite d'éval en CI devient vite lente et coûteuse — échantillonner, mettre en cache |
| Workflow local-first : tout tourne en CLI, sur le poste ou dans le pipeline, sans plateforme imposée | Rachat par OpenAI en mars 2026 : gouvernance et couplage produit à surveiller, même si la licence MIT est annoncée maintenue |

## Mise en œuvre

- Installation — `npx promptfoo`, ou une installation `npm` ; un wrapper Python existe
- Point d'entrée — un fichier YAML de prompts, fournisseurs, cas et assertions, puis `promptfoo eval`
- Prérequis — Node.js ; un modèle juge pour les assertions LLM-as-judge. **Red-teaming et hors ligne** (documentation, lue le 2026-10-01) : par défaut promptfoo utilise la clé OpenAI locale pour générer et noter les attaques, et à défaut de clé **relaie les requêtes vers l'API de l'éditeur** ; l'évaluation de la cible, elle, reste locale. Pour tout garder sur le site : `PROMPTFOO_DISABLE_REDTEAM_REMOTE_GENERATION=true` et un `redteam.provider` pointé vers un modèle local — la documentation avertit que la qualité des attaques générées en local « est généralement faible » pour la plupart des modèles, et que les plugins et stratégies personnalisés demandent une clé OpenAI ou son propre fournisseur
- Exécution — mono-nœud, en local ou dans la CI
- Coût — gratuit sous MIT ; le coût réel est en tokens, proportionnel au volume de tests ; une offre Enterprise, dont une variante Enterprise On-Prem (contrôle d'accès par rôle, gestion d'équipes, rapports, intégrations SIEM, support, exécuteur dédié pour réseau isolé), existe en option payante, le cœur en ligne de commande restant sous MIT ; la documentation ne liste pas ce que l'édition communautaire ne fait pas. Le serveur auto-hébergeable de la communauté (image Docker, SQLite) est présenté par la documentation comme non recommandé en production

## Écosystème

### Alternatives

- [[DeepEval]] — Framework d'évaluation LLM « pytest pour les LLM » (Apache-2.0, Confident AI) — 50+ métriques prêtes à l'emploi (G-Eval, hallucination, RAG, agents, sécurité) en assertions de test exécutables en CI ; plateforme managée Confident AI en option.
- [[Ragas]] — Framework d'évaluation de pipelines RAG et d'apps LLM (Apache-2.0, explodinggradients) — métriques sans référence calculées par LLM-as-judge (faithfulness, context precision/recall, answer relevancy) et génération de jeux de tests synthétiques ; la référence open-source de l'éval RAG.
- [[TruLens]] — Bibliothèque d'évaluation et de traçage d'apps LLM (MIT, TruEra/Snowflake) — instrumente n'importe quel stack et note la qualité via des feedback functions (groundedness, context/answer relevance) ; socle de Snowflake AI Observability.
- [[Inspect AI]] — Framework d'évaluation de LLM et d'agents (MIT, UK AI Security Institute et Meridian Labs) — des tâches composées d'un dataset, d'un solver et d'un scorer (texte ou noté par un modèle), 200+ évaluations prêtes à lancer, sandbox pour le code non fiable, visualiseur web et extension VS Code.

- [[garak]] — Scanner de vulnérabilités de LLM par sondes (Apache-2.0, NVIDIA) — une quarantaine de familles de sondes (injection de prompt, jailbreaks, encodages, fuites, génération de code malveillant) lancées contre un modèle local ou distant, avec détecteurs, rapports JSONL et HTML ; la plupart des détecteurs tournent en local, les attaques multi-tours demandent un modèle juge.

## Ressources

- Documentation — https://www.promptfoo.dev/docs/intro/
- Dépôt — https://github.com/promptfoo/promptfoo
- Documentation — configuration du red-teaming (génération distante ou locale) : https://www.promptfoo.dev/docs/red-team/configuration/

## Voir aussi

- [[LLM eval metrics]] — la notion du dossier
- [[AI security]] — ce que couvre son volet red-teaming : prompt injection, jailbreak
- [[RAG eval]] — ce que mesurent ses assertions sur un pipeline RAG
- [[Comparatif - Évaluation LLM]] — ce qui départage les outils du dossier
