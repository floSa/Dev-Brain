---
role: brique
nom: Instructor
alias: [instructor, 567-labs-instructor]
pitch: "Bibliothèque de sorties structurées pour LLM (Jason Liu) — emballe le client du fournisseur pour extraire des objets Pydantic validés, avec re-tentatives automatiques sur erreur de validation ; 15+ fournisseurs, multi-langages."
categorie: llm/sortie-structuree
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[PydanticAI]]"]
complements: []
tags: [llm, structured-output, data-validation, type-hints]
url_docs: https://python.useinstructor.com/
url_repo: https://github.com/567-labs/instructor
---

# Instructor

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de sorties structurées pour LLM (Jason Liu) — emballe le client du fournisseur pour extraire des objets Pydantic validés, avec re-tentatives automatiques sur erreur de validation ; 15+ fournisseurs, multi-langages.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque minimaliste dédiée à une seule chose : obtenir d'un LLM une **sortie structurée
validée**. Elle emballe le client du fournisseur — OpenAI, Anthropic, Gemini, Ollama et une
quinzaine d'autres — et ajoute un paramètre `response_model` prenant un modèle [[Pydantic]] ;
la réponse est parsée, validée, et **re-demandée automatiquement** au LLM si la validation
échoue, avec le message d'erreur en retour. Ni couche d'agent ni orchestration : on garde son
propre flux et l'on y greffe l'extraction typée. C'est ce qui la rend utilisable derrière une
API fermée, là où le décodage contraint ne l'est pas. Créée par Jason Liu, très diffusée (plus
de 3 M de téléchargements par mois) et déclinée en TypeScript, Go, Ruby, PHP et Elixir.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Extraire un objet typé depuis du texte — parsing de documents, classification, enrichissement — sans bâtir d'agent | Les re-tentatives automatiques gonflent facture et latence quand le modèle peine à respecter le schéma : borner `max_retries` |
| Ajouter des sorties structurées fiables à un code existant sans changer de framework, en gardant son client | La qualité du résultat dépend fortement de la clarté du schéma — les descriptions de champs font partie du prompt |
| Vouloir des re-tentatives sur validation et un support multi-fournisseurs derrière une API unique et fine | Couvre l'extraction, pas l'orchestration : enchaîner des étapes demande une couche au-dessus |

## Mise en œuvre

- Installation — `uv add instructor`
- Point d'entrée — on emballe le client du fournisseur et l'on passe un `response_model` [[Pydantic]]
- Prérequis — un client de fournisseur existant ; aucune infra à prévoir
- Exécution — mono-nœud, dans l'application hôte
- Coût — gratuit sous MIT ; le coût réel est celui des appels LLM, que les re-tentatives multiplient sur un schéma difficile à satisfaire

## Écosystème

### Alternatives

- [[PydanticAI]] — Framework d'agents typés de l'équipe Pydantic — agents model-agnostic à sorties structurées validées, injection de dépendances et type-safety Python ; pensé pour des apps LLM de production (Logfire, MCP, durable execution).

## Ressources

- Documentation — https://python.useinstructor.com/
- Dépôt — https://github.com/567-labs/instructor

## Voir aussi

- [[Structured outputs]] — le patron qu'elle met en œuvre
- [[Constrained decoding]] — l'approche opposée, celle d'[[Outlines]] et de [[Guidance]] : eux contraignent le décodage, elle demande, valide et retente
- [[Guardrails]] — validation de schéma et retry font un garde-fou applicatif de sortie
- [[Comparatif - Frameworks LLM]] — ce qui départage les frameworks du domaine
