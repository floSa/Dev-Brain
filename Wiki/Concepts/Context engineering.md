---
galaxie: wiki
type: concept
nom: Context engineering
alias: [ingénierie de contexte, gestion du contexte, context window management]
categorie: concept/llm
domaines: [ai-eng]
tags: [context-engineering, llm, agents]
---

# Context engineering

## Aperçu

- Discipline qui décide **ce qui entre dans la fenêtre de contexte** du modèle, sous quelle forme et dans quel ordre, sous une contrainte de **budget de tokens** — au-delà de la simple formulation du prompt.
- Principe directeur : le modèle ne « sait » que ce qui est dans son contexte à l'instant T ; tout le reste n'existe pas pour lui.

## Concepts clés

### Budget de tokens
- La fenêtre est finie et coûteuse. Chaque ajout (instructions, historique, documents, résultats d'outils, few-shot) consomme du budget — il faut **arbitrer**, pas tout empiler.

### Sélectionner vs compresser
- **Sélectionner** : ne récupérer que le pertinent ([[RAG]]), filtrer par métadonnées, éviter le bruit.
- **Compresser** : résumer l'historique, mémoire à fenêtre glissante, éviction des tours anciens ([[Agent memory]]).

### Ordre et position
- Phénomène *lost in the middle* : l'information au **milieu** d'un long contexte est moins bien exploitée que celle du **début** et de la **fin**. Placer les instructions critiques aux extrémités.

### Provenance et fraîcheur
- Tracer d'où vient chaque morceau (source, date) pour gérer conflits et obsolescence, et isoler le contexte non fiable.

## Les maths, simplement

- Coût de l'attention **quadratique** en longueur de contexte : doubler le contexte quadruple (à l'ordre $O(n^2)$) le calcul d'attention — un contexte long n'est pas gratuit.
- D'où l'arbitrage : maximiser le **signal utile** par token sous un plafond $n$ de tokens, plutôt que remplir la fenêtre.

## En pratique

- **Récupérer plutôt qu'empiler** : un [[RAG]] ciblé bat le « tout coller dans le prompt ».
- Sessions longues → **résumé glissant** / mémoire ([[Agent memory]]) au lieu de réinjecter tout l'historique.
- Mettre les **instructions clés en tête et en fin** ; isoler les données peu fiables.
- Réutiliser un préfixe stable via le [[prompt-caching]] pour amortir coût et latence.
- À distinguer du [[Prompt engineering|prompt engineering]] : celui-ci travaille la **formulation**, l'ingénierie de contexte travaille le **quoi** et le **combien**.

## Approches voisines & alternatives

- [[RAG]] — principal levier pour n'injecter que le contexte pertinent.
- [[Agent memory]] — gère ce qu'un agent retient et réinjecte entre les tours.
- [[Tool use patterns]] — les résultats d'outils reviennent dans le contexte et consomment du budget.
- [[Tokenization]] — la fenêtre se compte en tokens, unité de tout le budget.
- [[Prompt engineering]] — travaille la formulation ; complémentaire de la gestion du contexte.
- [[prompt-caching]], [[Reliability patterns]] — leviers complémentaires.

## Pour aller plus loin

- Liu et al. (2023) — *Lost in the Middle: How Language Models Use Long Contexts*.
- Anthropic / Google — guides « long context » et bonnes pratiques de structuration du contexte.
