---
role: brique
nom: vLLM
alias: [vllm]
pitch: "Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU."
categorie: llm/runtime
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Ollama]]", "[[llama.cpp]]", "[[LM Studio]]", "[[text-generation-webui]]", "[[TGI]]", "[[SGLang]]", "[[TensorRT-LLM]]"]
complements: ["[[Tunix]]"]
tags: [llm, model-serving, inference, gpu]
url_docs: https://docs.vllm.ai/
url_repo: https://github.com/vllm-project/vllm
---

# vLLM

<!-- AUTO:BANDEAU:START -->
> Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | open-source | self-hébergé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de serving qui a fait du débit GPU un sujet d'ingénierie mémoire. Son apport,
**PagedAttention**, gère le cache KV en **pages**, comme la mémoire virtuelle d'un système
d'exploitation : la fragmentation disparaît, et le **continuous batching** devient efficace —
les requêtes entrent et sortent du lot en continu au lieu d'attendre un batch complet. S'y
ajoutent le parallélisme tensoriel et pipeline sur plusieurs GPU et nœuds, la quantization
(AWQ, GPTQ, FP8), le *prefix caching* et le *speculative decoding*, le tout derrière une API
OpenAI-compatible. Projet hébergé par la PyTorch Foundation depuis 2025.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Servir un LLM open à fort débit et forte concurrence, le throughput étant l'objectif premier | Le cache KV est **préalloué** (`gpu_memory_utilization`) : l'empreinte VRAM au premier lancement surprend |
| Remplacer une API propriétaire par un endpoint OpenAI-compatible auto-hébergé | Quasi exclusivement GPU **NVIDIA** — le support AMD et CPU progresse mais reste secondaire |
| Faire tenir sur plusieurs GPU un modèle qui ne tient pas sur une carte | Surface d'options large (parallélisme, quantization, longueur de contexte) : le réglage fin demande de l'expérience |
| Charge variable à absorber sans laisser le GPU inoccupé | |

## Mise en œuvre

- Installation — `uv pip install vllm`, ou conteneur
- Point d'entrée — un serveur HTTP à API OpenAI-compatible, et une API Python pour l'inférence hors ligne
- Prérequis — un serveur GPU, NVIDIA en pratique ; les poids se chargent depuis Hugging Face
- Exécution — distribué : parallélisme tensoriel et pipeline sur plusieurs GPU et nœuds, réplicas pilotés par l'orchestrateur
- Coût — gratuit, licence Apache-2.0 ; la dépense est l'infrastructure GPU. Pas d'offre managée officielle, mais brique de nombreuses plateformes d'inférence

## Écosystème

### Alternatives

- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

### Compléments

- [[Tunix]] — Bibliothèque Google de post-training de LLM en JAX (Flax NNX) — SFT, préférences (DPO/ORPO), RL (GRPO, PPO, RL agentique) et distillation, pensée TPU et passage à l'échelle ; le pendant JAX/TPU de TRL. — vLLM lui sert de moteur de rollouts pour le RL.

## Ressources

- Documentation — https://docs.vllm.ai/
- Dépôt — https://github.com/vllm-project/vllm

## Voir aussi

- [[Inference optimization]] — la notion du dossier : PagedAttention, cache KV, continuous batching
- [[Comparatif - Exécution & serving LLM]] — ce qui départage les moteurs du dossier
- [[Speculative decoding]] — l'accélération de décodage qu'il implémente
- [[Quantization]] — AWQ, GPTQ et FP8, pour réduire l'empreinte VRAM
- [[Small Language Models]] · [[Reasoning models]] — deux familles de modèles qu'il sert
- [[HuggingFace]] — d'où viennent les poids
