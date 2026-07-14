---
galaxie: dev
type: service
nom: vLLM
alias: [vllm]
pitch: "Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU."
categorie: llm/local
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Ollama|Ollama]]", "[[Dev/Services/llama.cpp|llama.cpp]]", "[[Dev/Services/LM Studio|LM Studio]]", "[[Dev/Services/text-generation-webui|text-generation-webui]]", "[[Dev/Services/TGI|TGI]]", "[[Dev/Services/SGLang|SGLang]]", "[[Dev/Services/TensorRT-LLM|TensorRT-LLM]]"]
remplace_par: []
status: actif
tags: [llm, model-serving, inference, gpu]
url_docs: https://docs.vllm.ai/
url_repo: https://github.com/vllm-project/vllm
---

# vLLM

## Pourquoi

Moteur de serving LLM **haut débit** sur GPU, devenu la référence open-source du throughput en production. Son innovation, **PagedAttention**, gère le cache KV comme la mémoire virtuelle d'un OS (pages), ce qui élimine la fragmentation et permet un **continuous batching** très efficace : les requêtes entrent et sortent du batch en continu au lieu d'attendre un lot complet. Exposé en **API OpenAI-compatible** (drop-in), il supporte le **parallélisme tensoriel et pipeline** (multi-GPU, multi-nœuds), la quantization (AWQ, GPTQ, FP8), le prefix caching et le speculative decoding. Écrit en **Python** avec des kernels CUDA ; projet hébergé par la **PyTorch Foundation** depuis 2025.

## Quand l'utiliser

- Servir un LLM open à **fort débit / forte concurrence** en production (le throughput est l'objectif premier).
- Remplacer une API propriétaire par un endpoint **OpenAI-compatible** auto-hébergé.
- Exploiter **plusieurs GPU** (tensor/pipeline parallel) pour un modèle qui ne tient pas sur une carte.
- Maximiser l'usage GPU sous charge variable (continuous batching).

## Quand NE PAS l'utiliser

- Poste de dev / prototypage simple, ou pas de GPU → [[Dev/Services/Ollama|Ollama]] ou [[Dev/Services/llama.cpp|llama.cpp]].
- Stack et endpoints managés Hugging Face → [[Dev/Services/TGI|TGI]].
- Pipelines LLM programmables avec cache de préfixes poussé → [[Dev/Services/SGLang|SGLang]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; self-host sur serveur **GPU** (`uv pip install vllm`, ou conteneur).
- Pas d'offre SaaS officielle, mais brique standard de nombreuses plateformes d'inférence managées.
- Scaling **distribué** : tensor/pipeline parallelism sur plusieurs GPU et nœuds, réplicas pilotés par l'orchestrateur (K8s).

## Pièges

- Empreinte **VRAM** importante : par défaut vLLM préalloue le cache KV (`gpu_memory_utilization`) — surprenant au premier lancement.
- Quasi exclusivement **GPU NVIDIA** (le support AMD/CPU progresse mais reste secondaire).
- Surface d'options large (parallélisme, quantization, longueur de contexte) : le tuning fin demande de l'expérience.

## Alternatives

- [[Dev/Services/Ollama|Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[Dev/Services/llama.cpp|llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[Dev/Services/TGI|TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[Dev/Services/SGLang|SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[Dev/Services/LM Studio|LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[Dev/Services/text-generation-webui|text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

## Liens

- Modèles servis depuis [[Dev/Services/HuggingFace|HuggingFace]] (poids transformers).
- Endpoint OpenAI-compatible : se branche comme une API [[Dev/Services/FastAPI|FastAPI]] devant un orchestrateur.
- Concepts mis en œuvre : [[Inference optimization]] (PagedAttention, KV-cache, continuous batching), [[Speculative decoding]] ; sert [[Small Language Models]] et [[Reasoning models]].
- [[Quantization]] des poids supportée (AWQ, GPTQ, FP8) pour réduire l'empreinte VRAM.
- [[Comparatif - Exécution & serving LLM]] — comparatif de la catégorie
- Doc : https://docs.vllm.ai/
