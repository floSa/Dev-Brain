---
galaxie: dev
type: service
nom: TensorRT-LLM
alias: [TRT-LLM, trt-llm, tensorrt-llm]
pitch: "Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++."
categorie: llm/local
licence_type: open-source
hosted: self
maturite: production
langage: C++/Python
scaling: distributed
alternatives: ["[[Dev/Services/Ollama|Ollama]]", "[[Dev/Services/llama.cpp|llama.cpp]]", "[[Dev/Services/LM Studio|LM Studio]]", "[[Dev/Services/text-generation-webui|text-generation-webui]]", "[[Dev/Services/vLLM|vLLM]]", "[[Dev/Services/TGI|TGI]]", "[[Dev/Services/SGLang|SGLang]]"]
remplace_par: []
status: actif
tags: [llm, model-serving, inference, gpu, quantization]
url_docs: https://nvidia.github.io/TensorRT-LLM/
url_repo: https://github.com/NVIDIA/TensorRT-LLM
---

# TensorRT-LLM

## Pourquoi

Bibliothèque d'inférence LLM de **NVIDIA**, taillée pour extraire le maximum de débit et de latence des **GPU NVIDIA**. Le modèle est compilé en un moteur **TensorRT** optimisé (fusion d'opérations, kernels CUDA dédiés, précision réduite), piloté par des runtimes **Python et C++**. Une **API Python de haut niveau** (architecture PyTorch-native) sert à définir et charger les modèles. Supporte l'in-flight batching, le paged KV cache, la **quantization** (FP8, INT4 AWQ/GPTQ, FP4 sur Blackwell), le speculative decoding et le **parallélisme tensoriel / pipeline / expert** sur plusieurs GPU et nœuds. C'est le moteur derrière le backend TensorRT-LLM de [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] et des microservices NIM.

## Quand l'utiliser

- Servir un LLM sur parc GPU NVIDIA récent (H100/H200/Blackwell) en visant la **latence et le débit absolus**.
- Exploiter les dernières optimisations matérielles NVIDIA (FP8/FP4, kernels Blackwell) qu'un moteur générique n'utilise pas encore.
- Déploiement **multi-GPU / multi-nœuds** d'un gros modèle (tensor/pipeline/expert parallel).
- Intégration dans une stack NVIDIA déjà en place (Triton, NIM).

## Quand NE PAS l'utiliser

- Poste de dev / prototypage local → [[Dev/Services/Ollama|Ollama]], [[Dev/Services/LM Studio|LM Studio]] ou [[Dev/Services/llama.cpp|llama.cpp]].
- GPU non-NVIDIA ou besoin de portabilité matérielle → [[Dev/Services/vLLM|vLLM]] (support plus large).
- Haut débit sans la complexité de compilation → [[Dev/Services/vLLM|vLLM]], [[Dev/Services/SGLang|SGLang]] ou [[Dev/Services/TGI|TGI]].
- Itération rapide : l'étape de build du moteur (par modèle, par GPU, par config) alourdit le cycle.

## Déploiement & coût

- Open-source (Apache-2.0), gratuit ; self-host sur **GPU NVIDIA uniquement** (Linux ; conteneurs NGC fournis).
- Pas de SaaS ; brique des produits NVIDIA (backend Triton, microservices NIM).
- Scaling **distribué** : tensor/pipeline/expert parallelism multi-GPU et multi-nœuds.

## Pièges

- Verrou matériel total : NVIDIA uniquement, et les meilleures perfs ciblent les générations récentes.
- Le moteur doit être **(re)compilé** pour chaque couple modèle / GPU / précision — étape lourde, peu adaptée à l'expérimentation.
- Courbe d'apprentissage raide (build flags, plugins, quantization) ; certaines briques (AutoDeploy, Ray Orchestrator) restent en beta.
- Versionnage couplé à TensorRT/CUDA : mises à niveau parfois sensibles.

## Alternatives

- [[Dev/Services/Ollama|Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[Dev/Services/llama.cpp|llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[Dev/Services/LM Studio|LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[Dev/Services/text-generation-webui|text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[Dev/Services/vLLM|vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[Dev/Services/TGI|TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[Dev/Services/SGLang|SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.

## Liens

- Backend d'inférence de [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] (déploiement production NVIDIA).
- Modèles servis depuis [[Dev/Services/HuggingFace|HuggingFace]] (conversion en moteur TensorRT).
- [[Comparatif - Exécution & serving LLM]] — comparatif de la catégorie
- Doc : https://nvidia.github.io/TensorRT-LLM/
