---
role: brique
nom: llama.cpp
alias: [llamacpp, llama-cpp, ggml]
pitch: "Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux."
categorie: llm/runtime
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: C/C++
scaling: single-node
alternatives: ["[[Ollama]]", "[[LM Studio]]", "[[text-generation-webui]]", "[[vLLM]]", "[[TGI]]", "[[SGLang]]", "[[TensorRT-LLM]]", "[[needle]]"]
complements: []
tags: [llm, local-llm, inference, gpu, quantization]
url_docs: https://github.com/ggml-org/llama.cpp/tree/master/docs
url_repo: https://github.com/ggml-org/llama.cpp
---

# llama.cpp

<!-- AUTO:BANDEAU:START -->
> Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme C/C++ | open-source | self-hébergé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur d'inférence écrit au-dessus de la bibliothèque de tenseurs **ggml**, conçu pour tourner
partout avec un minimum de dépendances. Il apporte le format **GGUF** — poids et métadonnées
dans un seul fichier — et une **quantization agressive** (K-quants, *importance matrix*, de 2 à
8 bits) qui fait tenir un modèle de plusieurs milliards de paramètres dans la mémoire d'une
machine ordinaire. Backends CUDA, Metal, Vulkan, ROCm et CPU AVX, choisis **à la compilation**.
C'est le socle bas niveau qu'Ollama, LM Studio et la plupart des outils locaux
enveloppent, et il vise **une** machine.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Faire tourner un LLM sur CPU, Apple Silicon ou GPU grand public, voire sur une cible embarquée | Un binaire compilé sans les flags du backend (CUDA, Metal, Vulkan) n'utilise pas le GPU — et ne le dit pas |
| Maîtriser finement la quantization : format GGUF, niveau de bits, *importance matrix* | Quantization trop agressive : en Q2/Q3 la qualité se dégrade nettement |
| Embarquer l'inférence dans un binaire portable, sans runtime Python | Cadence de publication quasi quotidienne : options et formats bougent, GGUF a déjà cassé la compatibilité |
| Contrôler ou comprendre ce que les runtimes de plus haut niveau font en coulisses | Répartir un modèle sur plusieurs machines : le mode RPC est expérimental, ce n'est pas un serveur de production |

## Mise en œuvre

- Installation — compilation locale par CMake, ou binaires pré-compilés par plateforme
- Point d'entrée — les binaires `llama-cli` et `llama-server`, ce dernier exposant une API HTTP dont un mode OpenAI-compatible
- Prérequis — un modèle au format GGUF ; pour le GPU, une compilation avec les flags du backend visé
- Exécution — une machine, CPU ou GPU ; mode RPC expérimental pour répartir un modèle sur quelques machines
- Coût — gratuit, licence MIT ; la dépense est celle du matériel

## Écosystème

### Alternatives

- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.
- [[needle]] — Modèle spécialisé de 45 M paramètres pour l'appel d'outils et l'extraction structurée (Apache-2.0, poids compris) — quantifié en 2 bits dans un binaire de 14 Mo qui embarque son propre moteur, du Raspberry Pi au WebAssembly ; sortie JSON garantie par grammaire et score de confiance pour escalader vers un gros modèle.

## Ressources

- Documentation — https://github.com/ggml-org/llama.cpp/tree/master/docs
- Dépôt — https://github.com/ggml-org/llama.cpp

## Voir aussi

- [[Inference optimization]] — la notion du dossier : ce que le moteur optimise
- [[Comparatif - Exécution & serving LLM]] — ce qui départage les moteurs du dossier
- [[Quantization]] — le mécanisme dont GGUF, les K-quants et l'*imatrix* sont la mise en œuvre
- [[HuggingFace]] — d'où viennent les poids, convertis en GGUF
