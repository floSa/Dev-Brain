---
galaxie: dev
type: service
nom: Outlines
alias: [outlines, dottxt-outlines]
pitch: "Bibliothèque de génération structurée (.txt / dottxt-ai) : garantit une sortie conforme à un schéma JSON, une regex ou une grammaire par décodage contraint — masquage des tokens invalides à chaque pas."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Guidance|Guidance]]"]
remplace_par: []
status: actif
tags: [structured-output, decoding, llm]
url_docs: https://dottxt-ai.github.io/outlines/
url_repo: https://github.com/dottxt-ai/outlines
---

# Outlines

## Pourquoi

Bibliothèque dédiée à la **génération structurée** par [[Constrained decoding|décodage contraint]] : on fournit un **JSON Schema**, un modèle [[Dev/Services/Pydantic|Pydantic]], une **regex**, une liste de choix ou une **grammaire** (CFG), et Outlines **garantit** que la sortie est conforme — en **masquant les tokens invalides à chaque pas** de génération (validité par construction, pas de parsing fragile). Le cœur compile le schéma en automate (projet **outlines-core**, en Rust). Développé par **.txt (dottxt-ai)**. Particularité : « same code runs across OpenAI, Ollama, vLLM, and more » — et il est **embarqué par les principaux moteurs de serving** ([[Dev/Services/vLLM|vLLM]], [[Dev/Services/TGI|TGI]], [[Dev/Services/SGLang|SGLang]], LoRAX, xinference). Licence **Apache-2.0**.

## Quand l'utiliser

- Exiger une sortie **garantie valide** (JSON conforme à un schéma, énumération, regex) d'un **modèle ouvert** que l'on contrôle ([[Dev/Services/vLLM|vLLM]], [[Dev/Services/llama.cpp|llama.cpp]], [[Dev/Services/Ollama|Ollama]], transformers).
- Extraction / classification où un post-traitement par re-tentative serait trop coûteux ou peu fiable.
- Brancher la génération structurée **dans un moteur de serving** qui expose déjà Outlines en backend.

## Quand NE PAS l'utiliser

- On n'a accès qu'à une **API fermée** sans logits exposés : le décodage contraint réel n'est pas possible côté client → préférer le JSON mode natif ou [[Dev/Services/Instructor|Instructor]] (prompt + validation + retry).
- Besoin d'**interleaving** génération / contrôle (boucles, appels d'outils au fil du texte) → [[Dev/Services/Guidance|Guidance]].
- Simple extraction multi-fournisseurs sans changer de stack → [[Dev/Services/Instructor|Instructor]] suffit.

## Déploiement & coût

- `pip` / `uv add outlines`, Apache-2.0, gratuit. Tourne là où tourne le modèle (single-node, **GPU** recommandé pour les modèles locaux).
- Coût caché = **compilation** de l'automate (schéma → FSM) : amortie par mise en cache ; un schéma très large peut peser sur la latence de première requête.

## Pièges

- Le décodage contraint **garantit la forme, pas le sens** : un JSON valide peut contenir des valeurs absurdes — valider la sémantique ([[Dev/Services/Pydantic|Pydantic]]).
- Contraindre **biaise la distribution** (on masque des tokens que le modèle voulait émettre) : un schéma trop rigide peut dégrader la qualité du contenu.
- Désalignement **tokenisation ↔ grammaire** : pièges aux frontières de tokens (cf. [[Tokenization]]) ; dépend du support du modèle/moteur.

## Alternatives

- [[Dev/Services/Guidance|Guidance]] — Même famille (décodage contraint) mais orientée **langage de contrôle** : on entrelace génération, conditionnels, boucles et appels d'outils dans un même programme, avec *token healing*.

## Liens

- Met en œuvre le concept [[Constrained decoding]] (masquage de tokens par grammaire/FSM).
- Réalise des [[Structured outputs|sorties structurées]] par le mécanisme le plus garanti de [[Decoding strategies]].
- À opposer à [[Dev/Services/Instructor|Instructor]] : Outlines **contraint le décodage** (validité garantie) ; Instructor **demande + valide + retente** (côté client, tout fournisseur).
- Backends typiques : [[Dev/Services/vLLM|vLLM]], [[Dev/Services/llama.cpp|llama.cpp]], [[Dev/Services/Ollama|Ollama]].
- Doc : https://dottxt-ai.github.io/outlines/
