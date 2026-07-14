---
galaxie: dev
type: service
nom: DSPy
alias: [dspy, stanfordnlp-dspy, Demonstrate-Search-Predict]
pitch: "Framework de Stanford pour programmer — non prompter — les LLM : modules déclaratifs à signatures typées qu'un optimiseur compile en prompts (ou fine-tune) jusqu'à convergence des métriques."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/LangChain|LangChain]]", "[[Dev/Services/LlamaIndex|LlamaIndex]]", "[[Dev/Services/Haystack|Haystack]]"]
remplace_par: []
status: actif
tags: [llm, prompt-optimization, nlp]
url_docs: https://dspy.ai/
url_repo: https://github.com/stanfordnlp/dspy
---

# DSPy

## Pourquoi

Framework du **Stanford NLP** (Omar Khattab) pour **programmer plutôt que prompter** les LLM. Au lieu d'écrire des prompts en chaînes de caractères, on déclare des **signatures** typées (entrées → sorties) et on les compose en **modules** (`Predict`, `ChainOfThought`, `ReAct`…). Un **optimiseur** (*teleprompter* : MIPROv2, BootstrapFewShot…) génère et **règle automatiquement** les prompts — voire fine-tune — à partir d'exemples et d'une **métrique**, jusqu'à convergence de la qualité. Le sigle se relit *Declarative Self-improving Python*. L'intérêt : des programmes LLM **modulaires, versionnables et auto-optimisables**, qui résistent aux changements de modèle. Écrit en **Python** (≥ 3.10), licence **MIT**.

## Quand l'utiliser

- Remplacer le **prompt engineering manuel** par une optimisation pilotée par métrique sur un jeu d'exemples.
- Pipelines LLM à **plusieurs étapes** (RAG, classification, extraction) qu'on veut faire converger objectivement.
- Garder un programme **portable** entre modèles : recompiler plutôt que réécrire les prompts à chaque changement.
- Contexte recherche/eval où la **mesure** guide l'itération.

## Quand NE PAS l'utiliser

- App orientée **intégrations et agents prêts à l'emploi** → [[Dev/Services/LangChain|LangChain]].
- **RAG centré données** clé en main → [[Dev/Services/LlamaIndex|LlamaIndex]].
- Pipeline de production à **composants explicites** → [[Dev/Services/Haystack|Haystack]].
- Pas de **jeu d'exemples ni de métrique** : sans signal à optimiser, DSPy perd son intérêt principal.

## Déploiement & coût

- Open-source (MIT), gratuit ; bibliothèque importée, aucune infra dédiée.
- Coût notable à la **compilation** : l'optimisation lance de nombreux appels LLM pour explorer prompts/démonstrations — budgéter cette phase (distincte de l'inférence en production).
- S'appuie sur [[Dev/Services/LiteLLM|LiteLLM]] en interne pour appeler les fournisseurs.

## Pièges

- La phase d'**optimisation consomme beaucoup de tokens** : surveiller le budget, surtout avec un gros modèle « enseignant ».
- Qualité de l'optimisation **dépend de la métrique** : une métrique mal choisie produit un programme bien optimisé… pour la mauvaise chose.
- Paradigme **déroutant au départ** (signatures, modules, compilateur) : courbe d'apprentissage différente du prompting classique.
- API encore **mouvante** entre versions majeures.

## Alternatives

- [[Dev/Services/LangChain|LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.
- [[Dev/Services/LlamaIndex|LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.
- [[Dev/Services/Haystack|Haystack]] — Framework d'orchestration LLM de deepset (Apache-2.0) — pipelines modulaires et explicites pour RAG, recherche sémantique et agents, pensés pour la production ; contrôle fin du retrieval à la génération.

## Liens

- S'appuie sur [[Dev/Services/LiteLLM|LiteLLM]] pour l'accès multi-fournisseurs ; modèles depuis [[Dev/Services/HuggingFace|HuggingFace]].
- Vector stores pour les modules RAG : [[Dev/Services/Qdrant|Qdrant]], [[Dev/Services/Chroma|Chroma]].
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://dspy.ai/
