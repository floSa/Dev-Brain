---
galaxie: dev
type: service
nom: LM Studio
alias: [lmstudio, lms, llmster]
pitch: "Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit."
categorie: llm/local
licence_type: proprietary
hosted: self
maturite: production
langage: 
scaling: single-node
alternatives: ["[[Dev/Services/Ollama|Ollama]]", "[[Dev/Services/llama.cpp|llama.cpp]]", "[[Dev/Services/text-generation-webui|text-generation-webui]]", "[[Dev/Services/vLLM|vLLM]]", "[[Dev/Services/TGI|TGI]]", "[[Dev/Services/SGLang|SGLang]]", "[[Dev/Services/TensorRT-LLM|TensorRT-LLM]]"]
remplace_par: []
status: actif
tags: [llm, local-llm, inference, gpu, quantization]
url_docs: https://lmstudio.ai/docs
url_repo: 
---

# LM Studio

## Pourquoi

Application de bureau qui rend l'exécution locale de LLM accessible via une **interface graphique** : recherche et téléchargement de modèles (depuis Hugging Face), chat intégré, réglage des paramètres, et un **serveur local à API OpenAI-compatible** pour brancher ses apps. Sous le capot, elle s'appuie sur des moteurs **open-source** — [[Dev/Services/llama.cpp|llama.cpp]] (GGUF) partout, et **Apple MLX** sur Apple Silicon — mais **l'application elle-même est propriétaire** (closed-source). Multiplateforme (macOS, Windows, Linux). Existe aussi en version **headless** (`llmster`) et via un **CLI** (`lms`) pour les serveurs et la CI.

## Quand l'utiliser

- Exécuter des LLM en local **avec une GUI** : découvrir, comparer et chatter sans ligne de commande.
- Profil non-CLI ou onboarding rapide : tout est cliquable (téléchargement, quantization, GPU offload).
- Brancher une app sur un LLM local via l'**API OpenAI-compatible** (RAG, agents, tests) sans cloud.
- Stations **Apple Silicon** : tirer parti du backend **MLX** natif.

## Quand NE PAS l'utiliser

- Stack 100 % open-source / souveraineté du code → [[Dev/Services/Ollama|Ollama]] ou [[Dev/Services/llama.cpp|llama.cpp]].
- Serving GPU haut débit multi-utilisateurs en production → [[Dev/Services/vLLM|vLLM]], [[Dev/Services/TGI|TGI]] ou [[Dev/Services/SGLang|SGLang]].
- Automatisation/scriptabilité serveur sans GUI → [[Dev/Services/Ollama|Ollama]] (démon léger) ; LM Studio reste centré sur l'app de bureau (même si `llmster`/`lms` comblent en partie).
- Contrôle bas niveau fin des flags d'inférence → [[Dev/Services/llama.cpp|llama.cpp]] directement.

## Déploiement & coût

- **Propriétaire mais gratuit** pour usage personnel et commercial ; l'app GUI est closed-source, seuls les moteurs sous-jacents (llama.cpp, MLX) et le CLI/SDK sont open.
- Self-host de bureau (binaire macOS/Windows/Linux) ; serveur local sur le réseau via les endpoints OpenAI-compatibles.
- Scaling **single-node** : une machine ; `llmster` permet un déploiement headless (Linux, cloud, CI) mais pas un serving distribué.

## Pièges

- **Closed-source** : pas d'audit du code de l'app, dépendance à un éditeur (à peser pour un usage entreprise sensible).
- Modèles **quantifiés** par défaut : qualité moindre que le poids plein si l'on ne choisit pas le bon quant.
- Orienté **poste de travail** : le batching concurrent et le débit ne rivalisent pas avec un vrai serveur d'inférence.
- Un modèle qui dépasse la VRAM bascule en RAM/CPU et ralentit fortement.

## Alternatives

- [[Dev/Services/Ollama|Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[Dev/Services/llama.cpp|llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[Dev/Services/text-generation-webui|text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[Dev/Services/vLLM|vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[Dev/Services/TGI|TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[Dev/Services/SGLang|SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

## Liens

- Construit sur [[Dev/Services/llama.cpp|llama.cpp]] (inférence GGUF) et Apple MLX.
- Modèles tirés du hub [[Dev/Services/HuggingFace|HuggingFace]].
- Endpoint OpenAI-compatible : se branche comme une API [[Dev/Services/FastAPI|FastAPI]] devant les apps.
- [[Comparatif - Exécution & serving LLM]] — comparatif de la catégorie
- Doc : https://lmstudio.ai/docs
