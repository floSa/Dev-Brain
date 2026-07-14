---
galaxie: wiki
type: concept
nom: Constrained decoding
alias: [génération contrainte, décodage contraint, structured generation, grammar-constrained decoding]
categorie: concept/llm
domaines: [ai-eng]
tags: [decoding, structured-output, tokenization]
---

# Constrained decoding

## Aperçu

- Forcer un LLM à ne produire **que** des sorties valides vis-à-vis d'une **grammaire formelle** (JSON Schema, regex, grammaire hors-contexte) en **masquant, à chaque pas de décodage, les tokens qui la violeraient** → validité **garantie par construction**, sans parsing fragile.
- C'est le mécanisme **le plus fort** des trois pour obtenir des [[Structured outputs|sorties structurées]] — à distinguer du *prompt + validation + retry* ([[Dev/Services/Instructor|Instructor]]) et du *JSON mode* natif des fournisseurs.

## Concepts clés

### Masquer puis renormaliser
- À chaque pas, on **intersecte** le vocabulaire avec l'ensemble des tokens autorisés par l'**état courant** de la grammaire ; les tokens interdits reçoivent une probabilité nulle, le reste est **renormalisé**, puis on échantillonne comme d'habitude (cf. [[Decoding strategies]]).

### Compiler la contrainte en automate
- **JSON Schema / regex → automate fini (FSM)** : approche [[Dev/Services/Outlines|Outlines]] (schéma → regex → FSM), index précompilé puis **mis en cache** — à l'exécution, le masque par état est une simple lecture.
- **Grammaire hors-contexte (CFG) → automate à pile** (*pushdown*) : nécessaire pour les structures **imbriquées / équilibrées** (parenthésage, JSON arbitraire).

### Tokenisation vs grammaire
- La grammaire raisonne en **caractères**, le modèle en **tokens** : un caractère peut chevaucher plusieurs tokens. D'où le **token healing** et l'alignement token↔grammaire (cf. [[Tokenization]]) — sans quoi des sorties valides sont **faussement interdites** aux frontières de tokens.

### Où ça vit
- Côté **serving** : natif ou via Outlines dans vLLM, TGI, SGLang, et grammaires **GBNF** de llama.cpp.
- Côté **client** : il faut accéder aux **logits** pour masquer → **impossible sur une API purement fermée** (on s'y rabat sur le JSON mode ou le retry).

## Les maths, simplement

- Masquage + renormalisation : $p'(t) = \dfrac{p(t)\,\mathbb{1}[t \in \mathcal{G}(s)]}{\sum_{t'} p(t')\,\mathbb{1}[t' \in \mathcal{G}(s)]}$, où $\mathcal{G}(s)$ est l'ensemble des tokens autorisés à l'**état** $s$ de l'automate. Aucune masse de probabilité ne reste hors grammaire.
- L'état avance par **transition** $s \leftarrow \delta(s, t)$ à chaque token émis ; la génération s'arrête quand $s$ atteint un **état acceptant**.

## En pratique

- **Garantir la forme ≠ garantir le sens** : un JSON valide peut être absurde — valider la sémantique en aval ([[Dev/Services/Pydantic|Pydantic]]).
- Contraindre **biaise la distribution** (on masque des tokens que le modèle « voulait » émettre) : un schéma trop serré **dégrade la qualité** du contenu — descriptions de champs claires, ne pas sur-contraindre.
- Préférer le décodage contraint au *parsing + retry* **quand on contrôle le modèle** ([[Dev/Services/Outlines|Outlines]], [[Dev/Services/Guidance|Guidance]]) ; sur **API fermée**, se rabattre sur le JSON mode ou [[Dev/Services/Instructor|Instructor]].
- La **compilation** de l'automate (schéma → FSM) est coûteuse une fois : **réutiliser / cacher** l'index entre requêtes de même schéma.

## Approches voisines & alternatives

- [[Structured outputs]] — le **patron applicatif** ; le décodage contraint en est la réalisation la plus garantie.
- [[Decoding strategies]] — la **famille mère** ; ici on restreint l'espace de tokens à chaque pas plutôt que de seulement le réchauffer/échantillonner.
- [[Dev/Services/Outlines|Outlines]] et [[Dev/Services/Guidance|Guidance]] — bibliothèques de référence. XGrammar, llguidance, LM Format Enforcer et les grammaires GBNF de llama.cpp jouent le même rôle *(pages à créer)*.
- [[Dev/Services/Instructor|Instructor]] — alternative **non contrainte** : prompt + validation + re-tentative, côté client, tout fournisseur — plus souple, mais **sans garantie** par construction.

## Pour aller plus loin

- Willard & Louf (2023) — *Efficient Guided Generation for Large Language Models* (FSM, fondement d'Outlines).
- Documentation *grammars / structured outputs* de vLLM, de llama.cpp (GBNF) et de XGrammar.
