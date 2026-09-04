---
role: brique
nom: TensorRT-LLM
alias: [TRT-LLM, trt-llm, tensorrt-llm]
pitch: "Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++."
categorie: llm/runtime
famille: paquet
licence_type: open-source
maturite: production
langage: C++/Python
alternatives: ["[[Ollama]]", "[[llama.cpp]]", "[[LM Studio]]", "[[text-generation-webui]]", "[[vLLM]]", "[[TGI]]", "[[SGLang]]"]
complements: []
tags: [llm, model-serving, inference, gpu, quantization]
url_docs: https://nvidia.github.io/TensorRT-LLM/
url_repo: https://github.com/NVIDIA/TensorRT-LLM
---

# TensorRT-LLM

<!-- AUTO:BANDEAU:START -->
> Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie C++/Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'inférence de NVIDIA, taillée pour extraire le maximum de ses propres GPU. Le
principe la sépare de tous ses voisins : le modèle n'est pas chargé, il est **compilé** en un
moteur TensorRT — fusion d'opérations, kernels CUDA dédiés, précision réduite — puis piloté par
un runtime Python ou C++. Une API Python de haut niveau, d'architecture PyTorch-native, sert à
définir et charger les modèles. Elle couvre l'*in-flight batching*, le paged KV cache, la
quantization (FP8, INT4 AWQ/GPTQ, FP4 sur Blackwell), le *speculative decoding* et le
parallélisme tensoriel, pipeline et expert sur plusieurs GPU et nœuds.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Parc GPU NVIDIA récent (H100, H200, Blackwell) et objectif de latence et de débit absolus | Verrou matériel total : NVIDIA seulement, et les meilleures performances ciblent les générations récentes |
| Exploiter les optimisations matérielles les plus récentes — FP8, FP4, kernels Blackwell — qu'un moteur générique n'utilise pas encore | Le moteur se **recompile** pour chaque couple modèle / GPU / précision : étape lourde, mal adaptée à l'expérimentation |
| Déployer un gros modèle en multi-GPU ou multi-nœuds (tensor, pipeline, expert parallel) | Courbe d'apprentissage raide — flags de build, plugins, quantization — et des briques encore en beta (AutoDeploy, Ray Orchestrator) |
| Stack NVIDIA déjà en place : Triton, microservices NIM | Versionnage couplé à TensorRT et CUDA : les montées de version sont parfois sensibles |

## Mise en œuvre

- Installation — paquet Python, ou conteneurs NGC fournis par NVIDIA
- Point d'entrée — une API Python de haut niveau pour définir et charger, puis des runtimes Python et C++ pour exécuter
- Prérequis — GPU NVIDIA sous Linux, exclusivement ; une étape de build du moteur par modèle, GPU et précision
- Exécution — distribué : parallélisme tensoriel, pipeline et expert sur plusieurs GPU et nœuds
- Coût — gratuit, licence Apache-2.0 ; la dépense est le parc GPU. Pas d'offre managée : c'est une brique des produits NVIDIA

## Écosystème

### Alternatives

- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.

## Ressources

- Documentation — https://nvidia.github.io/TensorRT-LLM/
- Dépôt — https://github.com/NVIDIA/TensorRT-LLM

## Voir aussi

- [[Inference optimization]] — la notion du dossier : ce que la compilation optimise
- [[Comparatif - Exécution & serving LLM]] — ce qui départage les moteurs du dossier
- [[NVIDIA Triton]] — le serveur dont il est un backend d'inférence
- [[Quantization]] — FP8, INT4 et FP4, les précisions réduites qu'il exploite
- [[HuggingFace]] — d'où viennent les poids, avant conversion en moteur TensorRT
