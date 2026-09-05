---
role: brique
nom: Guidance
alias: [guidance, guidance-ai]
pitch: "Langage de contrôle de LLM (guidance-ai, ex-Microsoft Research) : entrelace génération et contrôle (conditionnels, boucles, outils) et contraint la sortie par regex/grammaire, avec token healing."
categorie: llm/sortie-structuree
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Outlines]]"]
complements: []
tags: [structured-output, decoding, llm]
url_docs: https://github.com/guidance-ai/guidance
url_repo: https://github.com/guidance-ai/guidance
---

# Guidance

<!-- AUTO:BANDEAU:START -->
> Langage de contrôle de LLM (guidance-ai, ex-Microsoft Research) : entrelace génération et contrôle (conditionnels, boucles, outils) et contraint la sortie par regex/grammaire, avec token healing.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Langage de contrôle pour piloter un LLM plus finement que le prompting ou le chaînage
classiques. Deux idées combinées : **contraindre la génération** — regex, grammaires CFG,
JSON Schema via [[Pydantic]] — par [[Constrained decoding|décodage contraint]], et
**entrelacer contrôle et génération** dans un même programme Python, où conditionnels, boucles
et appels d'outils s'intercalent entre les segments générés. S'y ajoutent le *token healing*,
qui répare les frontières de tokens entre texte fixe et texte généré (cf. [[Tokenization]]),
et le *fast-forward* des tokens imposés par la structure. Les fonctions sont stateless et
composables. Créé à Microsoft Research, aujourd'hui maintenu par l'org guidance-ai.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Programme LLM où la structure se mêle au texte : gabarit à trous typés, alternance « génère → décide → génère », mini-DSL de sortie | Besoin simple d'un objet conforme à un schéma, sans flot de contrôle : le JSON mode natif du fournisseur suffit |
| Imposer une grammaire ou une regex stricte tout en gardant du flot de contrôle côté Python — ce qu'un simple JSON Schema ne sait pas exprimer | Le DSL est propre au projet : plus expressif, mais plus à apprendre et à maintenir qu'un appel structuré ponctuel |
| Réduire coût et latence par *token healing* et *fast-forward* sur des sorties très contraintes, modèle local sous la main | Le support réel — token healing, grammaires — dépend du backend : les API distantes n'exposent pas toujours les logits, et une partie des garanties y est dégradée |
| | Comme tout décodage contraint : la forme est garantie, pas le sens, et la distribution est biaisée — valider la sémantique en sortie |

## Mise en œuvre

- Installation — `uv add guidance`
- Point d'entrée — un programme Python où génération et contrôle s'entrelacent, à base de fonctions composables
- Prérequis — un backend : transformers, [[llama.cpp]], [[vLLM]], OpenAI ou Azure ; la contrainte réelle par masquage de tokens suppose un modèle local, GPU utile
- Exécution — mono-nœud, là où tourne le backend choisi
- Coût — gratuit sous MIT ; le *fast-forward* des tokens imposés par la structure réduit coût et latence sur les sorties très contraintes

## Écosystème

### Alternatives

- [[Outlines]] — Bibliothèque de génération structurée (.txt / dottxt-ai) : garantit une sortie conforme à un schéma JSON, une regex ou une grammaire par décodage contraint — masquage des tokens invalides à chaque pas. — même famille (décodage contraint) mais orientée **schéma → sortie** : on déclare un JSON Schema, une regex ou une grammaire, sans tisser de flot de contrôle dans la génération ; embarqué nativement par les moteurs de serving.

## Ressources

- Documentation — https://github.com/guidance-ai/guidance
- Dépôt — https://github.com/guidance-ai/guidance

## Voir aussi

- [[Constrained decoding]] — la notion qu'il met en œuvre : masquage par grammaire et *token healing*
- [[Structured outputs]] — le patron de sortie produit ; [[Decoding strategies]] pour le mécanisme
- [[PydanticAI]] — complémentaire, côté framework d'agents
- [[Comparatif - Frameworks LLM]] — ce qui départage les frameworks du domaine
