---
galaxie: dev
type: service
nom: SGLang
alias: [sglang]
pitch: "Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS."
categorie: llm/local
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Ollama|Ollama]]", "[[Dev/Services/llama.cpp|llama.cpp]]", "[[Dev/Services/LM Studio|LM Studio]]", "[[Dev/Services/text-generation-webui|text-generation-webui]]", "[[Dev/Services/vLLM|vLLM]]", "[[Dev/Services/TGI|TGI]]", "[[Dev/Services/TensorRT-LLM|TensorRT-LLM]]"]
remplace_par: []
status: actif
tags: [llm, model-serving, inference, gpu]
url_docs: https://docs.sglang.io/
url_repo: https://github.com/sgl-project/sglang
---

# SGLang

## Pourquoi

Moteur de serving LLM (et modèles multimodaux) qui co-conçoit le **runtime backend** et un **langage frontend** pour programmer des interactions complexes. Son cœur, **RadixAttention**, organise le cache KV en arbre radix pour **réutiliser automatiquement les préfixes** partagés entre requêtes (few-shot, templates d'agents, appels répétés) — gain net quand beaucoup de requêtes partagent un même début. S'y ajoutent un **scheduler CPU zéro-overhead**, le continuous batching, la paged attention, le speculative decoding, le tensor parallelism, le chunked prefill, les **sorties structurées** et la quantization (FP8/INT4/AWQ/GPTQ). Écrit en **Python**, porté par **LMSYS**, intégré à l'**écosystème PyTorch** (mars 2025) avec support « day-one » de modèles comme DeepSeek V3/R1.

## Quand l'utiliser

- Servir un LLM à **haut débit** quand les requêtes **partagent des préfixes** (RAG few-shot, agents, prompts gabarisés) : RadixAttention y excelle.
- Imposer des **sorties structurées** (JSON / grammaire) côté serveur, à grande échelle.
- Programmer des **pipelines LLM** multi-étapes (appels chaînés, branchements) via le frontend SGLang.
- Servir des modèles récents rapidement (support amont réactif).

## Quand NE PAS l'utiliser

- Prototypage local / pas de GPU → [[Dev/Services/Ollama|Ollama]] ou [[Dev/Services/llama.cpp|llama.cpp]].
- Intégration et endpoints managés **Hugging Face** → [[Dev/Services/TGI|TGI]].
- Besoin du moteur de throughput le plus éprouvé et documenté, sans préfixes partagés → [[Dev/Services/vLLM|vLLM]].

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; self-host sur serveur **GPU** (`uv pip install "sglang[all]"`, ou conteneur).
- Pas d'offre SaaS officielle ; adopté par des fournisseurs d'inférence pour ses perfs.
- Scaling **distribué** : tensor parallelism multi-GPU, réplicas via l'orchestrateur.

## Pièges

- Le gain de **RadixAttention** dépend du **partage de préfixes** : sur des requêtes toutes différentes, l'avantage s'amenuise.
- **GPU NVIDIA/AMD** requis ; pas de cible CPU sérieuse.
- Projet jeune à itération rapide : montée en version et options mouvantes, doc parfois en retard sur le code.

## Alternatives

- [[Dev/Services/Ollama|Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[Dev/Services/llama.cpp|llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[Dev/Services/vLLM|vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[Dev/Services/TGI|TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[Dev/Services/LM Studio|LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[Dev/Services/text-generation-webui|text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

## Liens

- Modèles servis depuis [[Dev/Services/HuggingFace|HuggingFace]] ; intégré à l'écosystème [[Dev/Services/PyTorch|PyTorch]].
- Concepts mis en œuvre : [[Inference optimization]] (RadixAttention, prefix caching), [[Speculative decoding]] (EAGLE) ; sert [[Reasoning models]].
- [[Comparatif - Exécution & serving LLM]] — comparatif de la catégorie
- Doc : https://docs.sglang.io/
