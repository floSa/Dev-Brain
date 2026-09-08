---
role: brique
nom: PydanticAI
alias: [pydantic-ai, pydanticai]
pitch: "Framework d'agents typés de l'équipe Pydantic — agents model-agnostic à sorties structurées validées, injection de dépendances et type-safety Python ; pensé pour des apps LLM de production (Logfire, MCP, durable execution)."
categorie: llm/agents
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Instructor]]", "[[LangChain]]"]
complements: []
tags: [llm, agents, tool-use, structured-output, type-hints]
url_docs: https://pydantic.dev/docs/ai/
url_repo: https://github.com/pydantic/pydantic-ai
---

# PydanticAI

<!-- AUTO:BANDEAU:START -->
> Framework d'agents typés de l'équipe Pydantic — agents model-agnostic à sorties structurées validées, injection de dépendances et type-safety Python ; pensé pour des apps LLM de production (Logfire, MCP, durable execution).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-08 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'**agents** de l'équipe qui édite [[Pydantic]], appliquant la même philosophie aux
LLM : le développeur définit des **types**, et le framework garantit que les entrées et les
sorties s'y conforment. Le cœur en découle — des agents **model-agnostic** (OpenAI, Anthropic,
Gemini, modèles locaux…) dont la **sortie est un objet Pydantic validé**, et une **injection de
dépendances** typée pour passer du contexte aux outils et aux prompts. La **type-safety** capture
les erreurs à l'écriture, par mypy ou pyright, plutôt qu'à l'exécution. Pensé pour la production :
intégration **Logfire** pour l'observabilité, support **MCP**, et **durable execution** pour les
workflows longs. Version 1.x stable.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Construire des agents en Python avec une exigence forte de typage et de sorties structurées fiables | Aucun type-checker en CI : la type-safety n'a de valeur qu'avec mypy ou pyright activé — sinon l'argument central disparaît |
| Équipe déjà investie dans Pydantic : courbe d'apprentissage minimale, mêmes modèles | Besoin d'intégrations tierces toutes faites : elles sont plus rares ici, et retrievers comme outils sont parfois à câbler soi-même |
| Besoin d'observabilité native (Logfire) tout en restant agnostique du fournisseur | Projet à figer : jeune et rapide, releases quasi hebdomadaires — épingler la version, l'API bouge encore |

## Mise en œuvre

- Installation — bibliothèque `pip` / `uv`, importée dans l'application
- Point d'entrée — API Python : agent typé, sortie en modèle Pydantic, dépendances injectées ; support MCP pour consommer des outils externes
- Prérequis — Python, un accès LLM, et un type-checker (mypy ou pyright) en CI pour que le typage serve
- Exécution — en bibliothèque dans l'application hôte, aucune infra propre ; la durable execution couvre les workflows longs
- Coût — gratuit, MIT ; Pydantic Logfire est un service managé optionnel, payant au-delà du palier gratuit, et le framework s'utilise sans. La dépense réelle est celle des LLM

## Écosystème

### Alternatives

- [[Instructor]] — Bibliothèque de sorties structurées pour LLM (Jason Liu) — emballe le client du fournisseur pour extraire des objets Pydantic validés, avec re-tentatives automatiques sur erreur de validation ; 15+ fournisseurs, multi-langages.
- [[LangChain]] — Framework d'applications LLM le plus répandu — interfaces standardisées (modèles, embeddings, vector stores, outils) pour composer chaînes et agents ; large écosystème d'intégrations, socle de LangGraph et LangSmith.

## Ressources

- Documentation — https://pydantic.dev/docs/ai/
- Dépôt — https://github.com/pydantic/pydantic-ai

## Voir aussi

- [[Agents]] — le hub du dossier
- [[Comparatif - Frameworks LLM]] — ce qui départage les briques du dossier
- [[Structured outputs]] — le patron des sorties structurées, dont PydanticAI est une mise en œuvre
