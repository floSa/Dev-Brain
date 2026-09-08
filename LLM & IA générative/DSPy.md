---
role: brique
nom: DSPy
alias: [dspy, stanfordnlp-dspy, Demonstrate-Search-Predict]
pitch: "Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques."
categorie: llm/socle
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[LangChain]]", "[[LlamaIndex]]", "[[Haystack]]"]
complements: []
tags: [llm, prompt-optimization, nlp]
url_docs: https://dspy.ai/
url_repo: https://github.com/stanfordnlp/dspy
---

# DSPy

<!-- AUTO:BANDEAU:START -->
> Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-21 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework du Stanford NLP (Omar Khattab) pour **programmer plutôt que prompter**. Au lieu
d'écrire des prompts en chaînes de caractères, on déclare des **signatures** typées
(entrées → sorties) et on les compose en **modules** (`Predict`, `ChainOfThought`, `ReAct`).
Un **optimiseur** — le *teleprompter* : MIPROv2, BootstrapFewShot — génère et règle
automatiquement ces prompts, voire fine-tune, à partir d'exemples et d'une **métrique**,
jusqu'à convergence. Le sigle se relit *Declarative Self-improving Python*. Le programme
devient modulaire, versionnable et recompilable : il résiste au changement de modèle là où
un prompt écrit à la main se réécrit. Tout repose donc sur la métrique — mal choisie, elle
produit un programme parfaitement optimisé pour la mauvaise chose.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Remplacer le prompt engineering manuel par une optimisation pilotée par métrique sur un jeu d'exemples | Aucun jeu d'exemples ni métrique : sans signal à optimiser, l'outil perd son intérêt principal |
| Pipeline LLM à plusieurs étapes (RAG, classification, extraction) qu'on veut faire converger objectivement | La compilation lance de nombreux appels LLM pour explorer prompts et démonstrations : un budget distinct de l'inférence, à provisionner |
| Garder un programme portable entre modèles : recompiler plutôt que réécrire les prompts à chaque changement | Paradigme déroutant au départ — signatures, modules, compilateur — et API encore mouvante entre majeures |
| Contexte recherche ou évaluation, où la mesure guide l'itération | |

## Mise en œuvre

- Installation — dépendance Python installée dans l'app (`uv add` / `pip install`)
- Point d'entrée — import Python : on déclare des signatures, on compose des modules, puis on compile avec un optimiseur
- Prérequis — Python ≥ 3.10 ; surtout, un jeu d'exemples et une métrique, sans quoi il n'y a rien à compiler
- Exécution — en bibliothèque, rien à héberger ; les appels aux fournisseurs passent par [[LiteLLM]] en interne
- Coût — gratuit ; le poste réel est la **compilation**, d'autant plus chère que le modèle « enseignant » est gros

## Écosystème

### Alternatives

- [[LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.
- [[LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- [[Haystack]] — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.

## Ressources

- Documentation — https://dspy.ai/
- Dépôt — https://github.com/stanfordnlp/dspy

## Voir aussi

- [[Prompt engineering]] — la notion que l'optimiseur remplace par une compilation
- Modèles depuis [[HuggingFace]] ; vector stores pour les modules RAG : [[Qdrant]], [[Chroma]]
- [[LLM & IA générative]] — le hub du domaine
- [[Comparatif - Frameworks LLM]] — ce qui départage les frameworks de la catégorie
