---
role: brique
nom: Outlines
alias: [outlines, dottxt-outlines]
pitch: "Bibliothèque de génération structurée (.txt / dottxt-ai) : garantit une sortie conforme à un schéma JSON, une regex ou une grammaire par décodage contraint — masquage des tokens invalides à chaque pas."
categorie: llm/sortie-structuree
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Guidance]]"]
complements: []
tags: [structured-output, decoding, llm]
url_docs: https://dottxt-ai.github.io/outlines/
url_repo: https://github.com/dottxt-ai/outlines
---

# Outlines

<!-- AUTO:BANDEAU:START -->
> Bibliothèque de génération structurée (.txt / dottxt-ai) : garantit une sortie conforme à un schéma JSON, une regex ou une grammaire par décodage contraint — masquage des tokens invalides à chaque pas.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque dédiée à la génération structurée par [[Constrained decoding|décodage
contraint]] : on fournit un JSON Schema, un modèle [[Pydantic]], une regex, une liste de choix
ou une grammaire CFG, et la sortie est **conforme par construction** — les tokens invalides
sont masqués à chaque pas de génération, sans parsing fragile en aval. Le cœur compile le
schéma en automate (`outlines-core`, écrit en Rust). Le même code tourne sur OpenAI, Ollama,
vLLM et d'autres, et la bibliothèque est **embarquée nativement par les principaux moteurs de
serving** — [[vLLM]], [[TGI]], [[SGLang]], LoRAX, xinference. Développée par .txt (dottxt-ai).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Exiger une sortie garantie valide — JSON conforme à un schéma, énumération, regex — d'un modèle ouvert qu'on contrôle | Accès limité à une API fermée sans logits exposés : le décodage contraint réel est alors impossible côté client, et le JSON mode natif du fournisseur est le repli |
| Extraction ou classification où un post-traitement par re-tentative serait trop coûteux ou trop peu fiable | La forme est garantie, pas le sens : un JSON valide peut contenir des valeurs absurdes — valider la sémantique |
| Brancher la génération structurée dans un moteur de serving qui expose déjà Outlines en backend | Contraindre biaise la distribution — on masque des tokens que le modèle voulait émettre : un schéma trop rigide dégrade la qualité du contenu |
| | Désalignement tokenisation ↔ grammaire : les frontières de tokens sont un piège (cf. [[Tokenization]]), et le support dépend du modèle et du moteur |

## Mise en œuvre

- Installation — `uv add outlines`
- Point d'entrée — un JSON Schema, un modèle [[Pydantic]], une regex, une liste de choix ou une grammaire CFG
- Prérequis — l'accès aux logits, donc un modèle qu'on contrôle ([[vLLM]], [[llama.cpp]], [[Ollama]], transformers) ; GPU recommandé en local
- Exécution — mono-nœud, là où tourne le modèle ; aussi embarquée dans les moteurs de serving qui l'exposent en backend
- Coût — gratuit sous Apache-2.0 ; coût caché à la compilation du schéma en automate, amortie par mise en cache, mais un schéma très large pèse sur la latence de la première requête

## Écosystème

### Alternatives

- [[Guidance]] — Langage de contrôle de LLM (guidance-ai, ex-Microsoft Research) : entrelace génération et contrôle (conditionnels, boucles, outils) et contraint la sortie par regex/grammaire, avec token healing. — même famille (décodage contraint) mais orientée **langage de contrôle** : génération, conditionnels, boucles et appels d'outils s'entrelacent dans un même programme.

## Ressources

- Documentation — https://dottxt-ai.github.io/outlines/
- Dépôt — https://github.com/dottxt-ai/outlines

## Voir aussi

- [[Constrained decoding]] — la notion qu'elle met en œuvre : masquage de tokens par grammaire ou FSM
- [[Structured outputs]] — le patron produit, par le mécanisme le plus garanti de [[Decoding strategies]]
- [[Instructor]] — l'approche opposée : demander, valider et retenter côté client, sur tout fournisseur
- [[Comparatif - Frameworks LLM]] — ce qui départage les frameworks du domaine
