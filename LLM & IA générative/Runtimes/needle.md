---
role: brique
nom: needle
alias: [cactus-needle, needle2, Cactus Needle]
pitch: "Modèle spécialisé de 45 M paramètres pour l'appel d'outils et l'extraction structurée (Apache-2.0, poids compris) — quantifié en 2 bits dans un binaire de 14 Mo qui embarque son propre moteur, du Raspberry Pi au WebAssembly ; sortie JSON garantie par grammaire et score de confiance pour escalader vers un gros modèle."
categorie: llm/runtime
famille: modele
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[llama.cpp]]", "[[Ollama]]"]
complements: []
tags: [local-llm, small-language-model, quantization, tool-use, structured-output]
url_docs: https://github.com/cactus-compute/needle/blob/main/doc/apis.md
url_repo: https://github.com/cactus-compute/needle
---

# needle

<!-- AUTO:BANDEAU:START -->
> Modèle spécialisé de 45 M paramètres pour l'appel d'outils et l'extraction structurée (Apache-2.0, poids compris) — quantifié en 2 bits dans un binaire de 14 Mo qui embarque son propre moteur, du Raspberry Pi au WebAssembly ; sortie JSON garantie par grammaire et score de confiance pour escalader vers un gros modèle.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

Ce n'est pas un LLM généraliste, et c'est le premier point à comprendre : needle est un modèle
de **45 millions de paramètres** dédié à l'appel d'outils, à l'usage d'appareil et à
l'extraction structurée. Son contrat est étroit — texte en entrée, JSON en sortie, avec une
**grammaire byte-level compilée depuis les schémas d'outils**, donc conforme par construction
et non par re-tentative. Le format suit la fonction : quantifié en 2 bits, il tient dans un
binaire unique de **14 Mo qui embarque son propre moteur**, avec une fenêtre glissante de 256
tokens et un pic mémoire d'environ 28 Mo par session, quelle que soit la durée. Deux mécanismes
le distinguent d'un petit GGUF quelconque : un **score de confiance calibré**, seuil naturel
pour escalader vers un modèle cloud, et un **tool retrieval** intégré qui n'expose que le top-5
d'un gros catalogue d'outils. L'architecture — Simple Attention Network — remplace le FFN par
un MLP de Hadamard, avec attention GQA, mémoire clé-valeur *engram* sur tables n-gram hachées
et normalisation Sinkhorn des logits de routage.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| *Function calling* ou extraction structurée sur un appareil contraint : montre, capteur, robot, téléphone d'entrée de gamme, navigateur en WebAssembly | Chat, rédaction, génération libre : hors périmètre, et la fenêtre de 256 tokens glissante l'interdit de toute façon |
| Router localement et n'appeler un gros modèle que sur les cas incertains, en s'appuyant sur le score de confiance | Sortie structurée sur un modèle plus gros et plus capable → [[Outlines]], [[Instructor]] |
| Ne rien embarquer de tiers : le moteur est fourni, *weights-agnostic*, et un `.cact` fine-tuné tourne sans recompilation | Extraction d'entités nommées en zero-shot → [[GLiNER]] |
| Poids sous Apache-2.0 au même titre que le code : aucune licence de modèle restrictive | Multilingue : les langues supportées ne sont pas documentées, l'anglais seul est probable |
| | **Aucune table d'exactitude publiée en texte** : la comparaison à FunctionGemma 270M, LFM2.5 230M et Apple FM ne repose que sur une image de graphe, non reproductible en l'état |
| | Moteur livré **pré-compilé** depuis Hugging Face ; la source existe (`cactus-compute/cactus`, Apache-2.0) mais la chaîne de build reproductible n'a pas été vérifiée |
| | Télémétrie anonyme **activée par défaut** — à couper par `NEEDLE_TELEMETRY=0` ou `DO_NOT_TRACK=1` |
| | L'outil de synthèse de données de fine-tuning appelle [[OpenRouter]] par défaut : dépendance cloud pour l'entraînement, pas pour l'inférence |
| | Le portage rapporté sur ESP32-S3 est un retour tiers, pas un support officiel |

## Mise en œuvre

- Installation — `pip install cactus-needle` ; le moteur est téléchargé une fois depuis Hugging Face puis mis en cache, rien à compiler
- Point d'entrée — API Python ; `needle.js` + `needle.wasm` en navigateur, `libneedle.a` pour l'embarqué
- Prérequis — aucun accélérateur. Cibles : macOS arm64, Linux x86-64/arm64/armv7/riscv64/mipsel, Windows x64/arm64, Android, iOS/watchOS/tvOS, WebAssembly
- Exécution — dans le process appelant, ~28 Mo de pic par session ; fine-tuning LoRA en JAX (CPU, CUDA, Metal), puis merge et quantization vers un `.cact`
- Coût — nul hors matériel. Débits **annoncés par l'éditeur** : 500 tok/s sur Raspberry Pi 5, 400 à 1 500 tok/s sur Quest 3S et Vision Pro, 300 à 700 tok/s sur smartphones à moins de 200 $

## Écosystème

### Alternatives

- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.

## Ressources

- Documentation — https://github.com/cactus-compute/needle/blob/main/doc/apis.md
- Dépôt — https://github.com/cactus-compute/needle
- Poids — https://huggingface.co/Cactus-Compute/needle2
- Papier — arXiv:2607.18363, *Simple Attention Networks*

## Voir aussi

- [[Inference optimization]] — la notion du dossier : ce que le moteur embarqué optimise
- [[Comparatif - Exécution & serving LLM]] — ce qui départage les moteurs du dossier, où il est l'intrus assumé
- [[Small Language Models]] — la famille : petits modèles et exécution on-device
- [[Constrained decoding]] — le décodage sous grammaire, son mécanisme de conformité
- [[Quantization]] — la réduction de précision qui le fait tenir en 14 Mo
- [[Tool use patterns]] — les patrons d'appel d'outils qu'il sert
- [[Routing and cascading]] — l'escalade vers un modèle plus gros, que son score de confiance déclenche
