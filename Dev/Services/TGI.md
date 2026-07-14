---
galaxie: dev
type: service
nom: TGI
alias: [tgi, text-generation-inference]
pitch: "Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF."
categorie: llm/local
licence_type: open-source
hosted: both
maturite: production
langage: Rust/Python
scaling: distributed
alternatives: ["[[Dev/Services/Ollama|Ollama]]", "[[Dev/Services/llama.cpp|llama.cpp]]", "[[Dev/Services/LM Studio|LM Studio]]", "[[Dev/Services/text-generation-webui|text-generation-webui]]", "[[Dev/Services/vLLM|vLLM]]", "[[Dev/Services/SGLang|SGLang]]", "[[Dev/Services/TensorRT-LLM|TensorRT-LLM]]"]
remplace_par: []
status: actif
tags: [llm, model-serving, inference, gpu]
url_docs: https://huggingface.co/docs/text-generation-inference
url_repo: https://github.com/huggingface/text-generation-inference
---

# TGI

## Pourquoi

**Text Generation Inference** est le serveur d'inférence LLM maison de **Hugging Face**, pensé pour la production. Architecture **Rust + Python** : un routeur Rust performant (gestion des requêtes, batching) devant des workers Python qui exécutent le modèle, communiquant en gRPC. Il apporte **continuous batching**, attention optimisée (Flash/Paged Attention), **streaming** par SSE, quantization (bitsandbytes, GPTQ, AWQ, FP8) et **sharding multi-GPU** (tensor parallelism) pour les gros modèles. C'est le moteur derrière les **Inference Endpoints** de Hugging Face, donc bien intégré au hub et à son écosystème.

## Quand l'utiliser

- Servir un LLM en production avec un **fort ancrage écosystème Hugging Face** (hub, endpoints managés).
- Besoin de **streaming** robuste et de batching continu sous charge.
- Déployer un gros modèle réparti sur **plusieurs GPU** (sharding).
- Profiter d'un serveur **production-grade** maintenu par HF, sans tout assembler soi-même.

## Quand NE PAS l'utiliser

- Prototypage local / pas de GPU → [[Dev/Services/Ollama|Ollama]] ou [[Dev/Services/llama.cpp|llama.cpp]].
- Recherche du **throughput brut** maximal, hors écosystème HF → [[Dev/Services/vLLM|vLLM]] ou [[Dev/Services/SGLang|SGLang]].
- Programmation de **pipelines LLM** multi-étapes avec cache de préfixes poussé → [[Dev/Services/SGLang|SGLang]].

## Déploiement & coût

- Open-source (**Apache-2.0** sur la branche actuelle) ; self-host par conteneur officiel.
- Offre **managée** : les Inference Endpoints de Hugging Face exécutent TGI (facturés à l'usage / au GPU).
- Scaling **distribué** : sharding tensor-parallel multi-GPU, réplicas via l'orchestrateur.

## Pièges

- **Historique de licence** : de la v0.9.4/v1.0 (mi-2023) jusqu'à début 2024, TGI était sous licence restrictive **HFOIL** ; il est **revenu à Apache-2.0** depuis — vérifier la version si la conformité compte.
- **GPU NVIDIA** comme cible principale ; image conteneur volumineuse.
- Le couple **routeur Rust / workers Python** complique le débogage bas niveau par rapport à un serveur tout-Python.

## Alternatives

- [[Dev/Services/Ollama|Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[Dev/Services/llama.cpp|llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[Dev/Services/vLLM|vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[Dev/Services/SGLang|SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[Dev/Services/LM Studio|LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[Dev/Services/text-generation-webui|text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

## Liens

- Moteur des Inference Endpoints et intégré au hub [[Dev/Services/HuggingFace|HuggingFace]].
- Concepts mis en œuvre : [[Inference optimization]] (continuous batching, sharding), [[Speculative decoding]] (Medusa / EAGLE).
- [[Comparatif - Exécution & serving LLM]] — comparatif de la catégorie
- Doc : https://huggingface.co/docs/text-generation-inference
