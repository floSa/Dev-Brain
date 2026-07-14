---
galaxie: dev
type: service
nom: Guidance
alias: [guidance, guidance-ai]
pitch: "Langage de contrôle de LLM (guidance-ai, ex-Microsoft Research) : entrelace génération et contrôle (conditionnels, boucles, outils) et contraint la sortie par regex/grammaire, avec token healing."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Outlines|Outlines]]"]
remplace_par: []
status: actif
tags: [structured-output, decoding, llm]
url_docs: https://github.com/guidance-ai/guidance
url_repo: https://github.com/guidance-ai/guidance
---

# Guidance

## Pourquoi

**Langage de contrôle** pour piloter un LLM plus finement que le prompting/chaining classique. Deux idées combinées : **contraindre la génération** (regex, grammaires **CFG**, JSON Schema via [[Dev/Services/Pydantic|Pydantic]]) par [[Constrained decoding|décodage contraint]], et **entrelacer contrôle et génération** dans un même programme Python — conditionnels, boucles, appels d'outils s'intercalent entre les segments générés. Apporte le **token healing** (réparation des frontières de tokens entre texte fixe et texte généré, cf. [[Tokenization]]) et le *fast-forward* des tokens imposés par la structure (gain de vitesse et de coût). Créé à **Microsoft Research**, désormais maintenu par l'org **guidance-ai**. Fonctions **stateless et composables**. Backends : transformers, [[Dev/Services/llama.cpp|llama.cpp]], [[Dev/Services/vLLM|vLLM]], OpenAI, Azure. Licence **MIT**.

## Quand l'utiliser

- Programmes LLM où **la structure se mêle au texte** : gabarit à trous typés, alternance « génère → décide → génère », mini-DSL de sortie.
- Imposer une **grammaire / regex** stricte tout en gardant du **flot de contrôle** côté Python (impossible à exprimer en simple JSON Schema).
- Réduire le coût/latence via *token healing* + *fast-forward* sur des sorties très contraintes, modèle local sous la main.

## Quand NE PAS l'utiliser

- Besoin simple « un objet conforme à ce schéma » sans flot de contrôle → [[Dev/Services/Outlines|Outlines]] (plus focalisé) ou le JSON mode natif.
- Extraction multi-fournisseurs côté API fermée, sans modèle local → [[Dev/Services/Instructor|Instructor]] (prompt + validation + retry).
- Équipe rétive à un **DSL** : la courbe d'apprentissage du langage Guidance est réelle.

## Déploiement & coût

- `pip` / `uv add guidance`, MIT, gratuit. Tourne avec le backend choisi ; contrainte réelle (masquage de tokens) surtout avec un modèle **local** ([[Dev/Services/llama.cpp|llama.cpp]], transformers, **GPU** utile). Single-node.
- Les backends API (OpenAI/Azure) ne donnent pas toujours accès aux logits : une partie des garanties de contrainte y est dégradée.

## Pièges

- **DSL propre** : plus expressif mais plus à apprendre et à maintenir qu'un appel structuré ponctuel.
- Comme tout décodage contraint, on **garantit la forme, pas le sens**, et on **biaise la distribution** — valider la sémantique en sortie.
- Le support exact (token healing, grammaires) **dépend du backend** : vérifier ce qui est réellement contraint vs simplement suggéré côté API distante.

## Alternatives

- [[Dev/Services/Outlines|Outlines]] — Même famille (décodage contraint) mais orientée **schéma → sortie** : on déclare un JSON Schema / une regex / une grammaire, sans tisser de flot de contrôle dans la génération ; embarqué nativement par les moteurs de serving.

## Liens

- Met en œuvre le concept [[Constrained decoding]] (masquage par grammaire + *token healing*).
- Produit des [[Structured outputs|sorties structurées]] tout en gérant l'entrelacement contrôle/génération (cf. [[Decoding strategies]]).
- À opposer à [[Dev/Services/Instructor|Instructor]] (prompt + retry, tout fournisseur) ; complémentaire des frameworks d'agents comme [[Dev/Services/PydanticAI|PydanticAI]].
- Doc : https://github.com/guidance-ai/guidance
