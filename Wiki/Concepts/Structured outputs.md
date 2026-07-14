---
galaxie: wiki
type: concept
nom: Structured outputs
alias: [sorties structurées, sortie structurée, JSON mode]
categorie: concept/llm
domaines: [ai-eng]
tags: [structured-output, llm, tool-use, data-validation]
---

# Structured outputs

## Aperçu

- Contraindre un LLM à produire une sortie **conforme à un schéma** (JSON, modèle Pydantic) plutôt que du texte libre, pour la rendre **directement exploitable** par du code.
- Transforme le LLM en composant fiable d'un pipeline : on sait *à l'avance* la forme de ce qui sort.

## Concepts clés

### Le schéma comme contrat
- Le schéma (types, champs requis, énumérations) définit la sortie attendue. Les **descriptions de champs** font partie du prompt : elles guident le modèle autant qu'elles documentent.

### Trois mécanismes, du plus souple au plus garanti
- **Prompt + parsing + re-tentative** : demander du JSON, parser, redemander avec l'erreur en feedback si invalide (approche [[Dev/Services/Instructor|Instructor]]).
- **JSON mode / schéma natif** du fournisseur : l'API force une sortie JSON (parfois conforme à un JSON Schema fourni).
- **Décodage contraint** : une grammaire / un automate masque à chaque pas les tokens interdits → validité **garantie par construction** (cf. [[Constrained decoding]] et [[Decoding strategies]]).

### Validation
- Même conforme syntaxiquement, la sortie doit être **validée** sémantiquement ([[Dev/Services/Pydantic|Pydantic]]) : un JSON valide peut contenir des valeurs absurdes.

### Lien avec l'appel d'outils
- Un *function call* est une sortie structurée : le modèle émet des **arguments typés** conformes au schéma de l'outil (cf. [[Tool use patterns]]).

## Les maths, simplement

- Décodage contraint = masquage à chaque pas : $p'(t) = \dfrac{p(t)\,\mathbb{1}[t \in \mathcal{G}]}{\sum_{t' \in \mathcal{G}} p(t')}$, où $\mathcal{G}$ est l'ensemble des tokens autorisés par la grammaire à cet état. Les tokens hors schéma reçoivent une probabilité nulle, le reste est renormalisé.

## En pratique

- Définir un **schéma clair** avec des descriptions de champs explicites ; c'est le premier levier de qualité.
- Préférer le **JSON mode natif** ou le **décodage contraint** quand le fournisseur les offre : validité garantie, pas de parsing fragile.
- **Borner les re-tentatives** : un schéma difficile multiplie les appels (coût, latence).
- Choix d'outil : [[Dev/Services/Instructor|Instructor]] pour de l'**extraction** typée légère sans changer de framework ; [[Dev/Services/PydanticAI|PydanticAI]] pour des **agents typés** complets.
- Sortie structurée ≠ contenu correct : valider le **sens**, pas seulement la forme.

## Approches voisines & alternatives

- [[Tool use patterns]] — le function calling est une sortie structurée (arguments d'outil conformes à un schéma).
- [[Decoding strategies]] — le décodage contraint est le mécanisme qui garantit la conformité.
- [[Dev/Services/Instructor|Instructor]] — Bibliothèque de sorties structurées pour LLM (Jason Liu) — emballe le client du fournisseur pour extraire des objets Pydantic validés, avec re-tentatives automatiques sur erreur de validation ; 15+ fournisseurs, multi-langages.
- [[Dev/Services/PydanticAI|PydanticAI]] — Framework d'agents typés de l'équipe Pydantic — agents model-agnostic à sorties structurées validées, injection de dépendances et type-safety Python ; pensé pour des apps LLM de production (Logfire, MCP, durable execution).
- [[Dev/Services/Outlines|Outlines]] / [[Dev/Services/Guidance|Guidance]] — réalisent la sortie structurée par [[Constrained decoding|décodage contraint]] (validité garantie par construction, modèle sous contrôle).

## Pour aller plus loin

- Documentation *structured outputs* / *JSON mode* des fournisseurs (Anthropic, OpenAI).
- Bibliothèques de [[Constrained decoding|décodage contraint]] : [[Dev/Services/Outlines|Outlines]], [[Dev/Services/Guidance|Guidance]] (XGrammar, jsonformer, LM Format Enforcer à créer).
