---
galaxie: dev
type: service
nom: needle
alias: [cactus-needle, needle2, Cactus Needle]
pitch: "Modèle spécialisé de 45 M paramètres pour l'appel d'outils et l'extraction structurée (Apache-2.0, poids compris) — quantifié en 2 bits dans un binaire de 14 Mo qui embarque son propre moteur, du Raspberry Pi au WebAssembly ; sortie JSON garantie par grammaire et score de confiance pour escalader vers un gros modèle."
categorie: llm/local
licence_type: open-source
hosted: self
maturite: beta
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/llama.cpp|llama.cpp]]", "[[Dev/Services/Ollama|Ollama]]"]
remplace_par: []
status: actif
tags: [local-llm, small-language-model, quantization, tool-use, structured-output]
url_docs: https://github.com/cactus-compute/needle/blob/main/doc/apis.md
url_repo: https://github.com/cactus-compute/needle
---

# needle

## Pourquoi

**Ce n'est pas un LLM généraliste**, et c'est le premier point à comprendre. needle est un modèle ouvert de **45 millions de paramètres** dédié à l'appel d'outils, à l'usage d'appareil et à l'extraction structurée. Son contrat est étroit : texte en entrée, JSON en sortie, avec une **grammaire byte-level compilée depuis les schémas d'outils** — la sortie est conforme par construction, pas par re-tentative. Il n'est fait ni pour le chat, ni pour la génération libre.

Le format suit la fonction. Quantifié en **2 bits** (Cactus Quants), le modèle tient dans un binaire unique de **14 Mo**. Fenêtre glissante de 256 tokens, outils épinglés en KV sinks, pic mémoire d'environ **28 Mo par session** quelle que soit la durée de la conversation. L'architecture (Simple Attention Network, arXiv:2607.18363) remplace le FFN par un MLP de Hadamard, avec attention GQA, mémoire clé-valeur « engram » sur tables n-gram hachées et normalisation Sinkhorn des logits de routage.

Deux mécanismes le distinguent d'un petit modèle GGUF quelconque : un **score de confiance calibré** par tête apprise, seuil naturel pour escalader vers un modèle cloud, et un **tool retrieval** intégré — déclarer un gros catalogue d'outils, le modèle n'en expose que le top-5 par tour.

Licence Apache-2.0 pour le code **et pour les poids** : pas de licence de modèle restrictive.

## Quand l'utiliser

- Faire du function calling ou de l'extraction structurée sur un appareil contraint : montre, capteur, robot, téléphone d'entrée de gamme, navigateur en WebAssembly.
- Router localement et n'appeler un gros modèle que sur les cas incertains, en s'appuyant sur le score de confiance.
- Éviter d'embarquer un runtime tiers : le moteur est fourni, weights-agnostic, et un `.cact` fine-tuné tourne sans recompilation.

## Quand NE PAS l'utiliser

- Conversation, rédaction, raisonnement : hors périmètre → [[Dev/Services/Ollama|Ollama]], [[Dev/Services/llama.cpp|llama.cpp]].
- Sortie structurée sur un modèle plus gros et plus capable → [[Dev/Services/Outlines|Outlines]], [[Dev/Services/Instructor|Instructor]].
- Extraction d'entités nommées en zero-shot → [[Dev/Services/GLiNER|GLiNER]].
- Contexte long : la fenêtre est de 256 tokens, glissante.
- Multilingue : les langues supportées ne sont pas documentées, l'anglais seul est probable.

## Déploiement & coût

- `pip install cactus-needle`. Le moteur est téléchargé une fois depuis Hugging Face puis mis en cache — pas de compilation à la charge de l'utilisateur.
- Cibles : macOS arm64, Linux x86-64/arm64/armv7/riscv64/mipsel, Windows x64/arm64, Android, iOS/watchOS/tvOS, WebAssembly (`needle.js` + `needle.wasm`). Un `libneedle.a` est fourni pour l'embarqué.
- Fine-tuning LoRA en JAX (CPU, CUDA, Metal), puis merge et quantization vers un `.cact`.
- Coût d'inférence nul hors matériel. Débits **annoncés par l'éditeur** : 500 tok/s sur Raspberry Pi 5, 400 à 1 500 tok/s sur Quest 3S et Vision Pro, 300 à 700 tok/s sur smartphones à moins de 200 $.

## Pièges

- **Aucune table d'exactitude publiée en texte.** La comparaison à FunctionGemma 270M, LFM2.5 230M et Apple FM ne repose que sur une image de graphe : annoncée par l'éditeur, non reproductible en l'état.
- Le moteur arrive **pré-compilé depuis Hugging Face** ; la source existe (`cactus-compute/cactus`, Apache-2.0) mais la chaîne de build reproductible n'a pas été vérifiée.
- **Télémétrie anonyme activée par défaut** — la couper avec `NEEDLE_TELEMETRY=0` ou `DO_NOT_TRACK=1`.
- L'outil de synthèse de données de fine-tuning appelle [[Dev/Services/OpenRouter|OpenRouter]] par défaut (`OPENROUTER_API_KEY`) : dépendance cloud pour l'entraînement, pas pour l'inférence.
- Le portage rapporté sur ESP32-S3 est un retour tiers, pas un support officiel.

## Alternatives

- [[Dev/Services/llama.cpp|llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[Dev/Services/Ollama|Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.

## Liens

- [[Comparatif - Exécution & serving LLM]] — comparatif de la catégorie
- [[Small Language Models]] — concept : petits modèles et exécution on-device
- [[Constrained decoding]] — concept : décodage sous grammaire
- [[Quantization]] — concept : réduction de précision des poids
- [[Tool use patterns]] — concept : patrons d'appel d'outils
- [[Routing and cascading]] — concept : escalade vers un modèle plus gros
- Poids : https://huggingface.co/Cactus-Compute/needle2 · Repo : https://github.com/cactus-compute/needle
