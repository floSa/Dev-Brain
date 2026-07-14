---
galaxie: dev
type: service
nom: Instructor
alias: [instructor, 567-labs-instructor]
pitch: "Bibliothèque de sorties structurées pour LLM (Jason Liu) — emballe le client du fournisseur pour extraire des objets Pydantic validés, avec re-tentatives automatiques sur erreur de validation ; 15+ fournisseurs, multi-langages."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/PydanticAI|PydanticAI]]"]
remplace_par: []
status: actif
tags: [llm, structured-output, data-validation, type-hints]
url_docs: https://python.useinstructor.com/
url_repo: https://github.com/567-labs/instructor
---

# Instructor

## Pourquoi

Bibliothèque **minimaliste** dédiée à une seule chose, bien faite : obtenir d'un LLM une **sortie structurée validée**. Créée par **Jason Liu**, elle **emballe le client du fournisseur** (OpenAI, Anthropic, Gemini, Ollama…) et ajoute un paramètre `response_model` prenant un modèle [[Dev/Services/Pydantic|Pydantic]] ; la réponse est parsée, **validée**, et **re-demandée automatiquement** au LLM si la validation échoue (avec le message d'erreur en feedback). Pas de couche d'agent, pas d'orchestration : on garde son propre flux et on greffe l'extraction typée. Très diffusée (3M+ téléchargements/mois) et déclinée en plusieurs langages (TypeScript, Go, Ruby, PHP, Elixir). Licence **MIT**.

## Quand l'utiliser

- **Extraction** d'un objet typé à partir de texte/LLM (parsing de documents, classification, enrichissement) sans bâtir d'agent.
- Ajouter des **sorties structurées fiables** à un code existant **sans changer de framework** (on garde son client).
- Besoin de **re-tentatives sur validation** et de support **multi-fournisseurs** avec une API unique et fine.

## Quand NE PAS l'utiliser

- Besoin d'un **agent complet** (boucle d'outils, état, dépendances) → [[Dev/Services/PydanticAI|PydanticAI]] (même esprit Pydantic, mais framework d'agents).
- Application déjà bâtie sur un framework généraliste qui gère nativement le structured output → [[Dev/Services/LangChain|LangChain]].

## Déploiement & coût

- Open-source (MIT), gratuit ; simple dépendance `pip`/`uv`, aucune infra.
- Coût réel = appels **LLM** ; attention aux **re-tentatives** qui multiplient les appels en cas de schéma difficile à satisfaire.
- Scaling = celui de l'application hôte (single-node).

## Pièges

- Les **re-tentatives automatiques** peuvent gonfler la facture et la latence si le modèle peine à respecter le schéma — borner `max_retries`.
- Qualité du résultat très dépendante de la **clarté du schéma** (descriptions de champs = partie du prompt).
- Couvre l'**extraction**, pas l'orchestration : pour enchaîner des étapes, il faut une couche au-dessus.

## Alternatives

- [[Dev/Services/PydanticAI|PydanticAI]] — Framework d'agents typés de l'équipe Pydantic — agents model-agnostic à sorties structurées validées, injection de dépendances et type-safety Python ; pensé pour des apps LLM de production (Logfire, MCP, durable execution).

## Liens

- Repose sur [[Dev/Services/Pydantic|Pydantic]] pour la définition et la validation des schémas.
- Met en œuvre le concept [[Structured outputs]] (le patron des sorties structurées).
- À opposer au [[Constrained decoding|décodage contraint]] ([[Dev/Services/Outlines|Outlines]], [[Dev/Services/Guidance|Guidance]]) : Instructor **demande + valide + retente** (tout fournisseur, API fermée OK) ; eux **contraignent le décodage** (validité garantie, modèle sous contrôle).
- Sert de [[Guardrails|garde-fou de sortie]] : la validation de schéma + retry est un garde-fou applicatif.
- Couple **sorties structurées** avec [[Dev/Services/PydanticAI|PydanticAI]] : Instructor = bibliothèque focalisée extraction ; PydanticAI = framework d'agents complet.
- [[Comparatif - Frameworks LLM]] — comparatif de la catégorie
- Doc : https://python.useinstructor.com/
