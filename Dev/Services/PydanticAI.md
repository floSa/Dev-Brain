---
galaxie: dev
type: service
nom: PydanticAI
alias: [pydantic-ai, pydanticai]
pitch: "Framework d'agents typés de l'équipe Pydantic — agents model-agnostic à sorties structurées validées, injection de dépendances et type-safety Python ; pensé pour des apps LLM de production (Logfire, MCP, durable execution)."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Instructor|Instructor]]", "[[Dev/Services/LangChain|LangChain]]"]
remplace_par: []
status: actif
tags: [llm, agents, tool-use, structured-output, type-hints]
url_docs: https://ai.pydantic.dev/
url_repo: https://github.com/pydantic/pydantic-ai
---

# PydanticAI

## Pourquoi

Framework d'**agents** de l'équipe qui édite [[Dev/Services/Pydantic|Pydantic]], appliquant la même philosophie aux LLM : le développeur définit des **types**, et le framework garantit que les entrées/sorties s'y conforment. Cœur de l'outil : des agents **model-agnostic** (OpenAI, Anthropic, Gemini, locaux…) dont la **sortie est un objet Pydantic validé**, plus l'**injection de dépendances** typée pour passer du contexte aux outils et aux prompts. La **type-safety** capture les erreurs à l'écriture (mypy/pyright) plutôt qu'à l'exécution. Pensé production : intégration **Logfire** (observabilité), support **MCP**, et **durable execution** pour workflows longs. Licence **MIT**, version 1.x stable.

## Quand l'utiliser

- Construire des **agents en Python** avec une exigence forte de **typage** et de sorties **structurées fiables**.
- Équipe déjà investie dans [[Dev/Services/Pydantic|Pydantic]] : courbe d'apprentissage minimale, mêmes modèles.
- Besoin d'**observabilité** native (Logfire) et de rester **agnostique du fournisseur**.

## Quand NE PAS l'utiliser

- Besoin **uniquement** d'extraire un objet structuré d'un appel LLM, sans logique d'agent → [[Dev/Services/Instructor|Instructor]] (plus léger).
- Très large besoin d'**intégrations** tierces toutes faites (loaders, vector stores, outils) → [[Dev/Services/LangChain|LangChain]].
- Agents à **graphe d'état complexe** (cycles, checkpoints, human-in-the-loop) → [[Dev/Services/LangGraph|LangGraph]].

## Déploiement & coût

- Open-source (MIT), gratuit ; bibliothèque importée dans l'app (`pip`/`uv`), aucune infra propre.
- Observabilité via **Pydantic Logfire** (service managé optionnel, payant au-delà du palier gratuit) — le framework reste utilisable sans.
- Coût réel dominé par les appels aux **LLM** sous-jacents.

## Pièges

- Projet **jeune et rapide** (releases quasi hebdomadaires) : épingler la version, l'API bouge encore.
- La **type-safety** n'a de valeur qu'avec un type-checker activé (mypy/pyright) en CI — sinon on perd l'argument central.
- Moins d'**intégrations toutes faites** que LangChain : il faut parfois câbler soi-même retrievers et outils.

## Alternatives

- [[Dev/Services/Instructor|Instructor]] — Bibliothèque de sorties structurées pour LLM (Jason Liu) — emballe le client du fournisseur pour extraire des objets Pydantic validés, avec re-tentatives automatiques sur erreur de validation ; 15+ fournisseurs, multi-langages.
- [[Dev/Services/LangChain|LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.

## Liens

- Bâti sur [[Dev/Services/Pydantic|Pydantic]] — réutilise ses modèles et sa validation pour les sorties LLM.
- Met en œuvre le concept [[Structured outputs]] (le patron des sorties structurées).
- Couple **sorties structurées** avec [[Dev/Services/Instructor|Instructor]] : PydanticAI est un framework d'agents complet, Instructor une bibliothèque focalisée extraction.
- Peut router ses appels via [[Dev/Services/LiteLLM|LiteLLM]] (abstraction multi-fournisseurs).
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://ai.pydantic.dev/
