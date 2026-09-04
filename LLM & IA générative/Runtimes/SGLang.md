---
role: brique
nom: SGLang
alias: [sglang]
pitch: "Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS."
categorie: llm/runtime
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Ollama]]", "[[llama.cpp]]", "[[LM Studio]]", "[[text-generation-webui]]", "[[vLLM]]", "[[TGI]]", "[[TensorRT-LLM]]"]
complements: []
tags: [llm, model-serving, inference, gpu]
url_docs: https://docs.sglang.io/
url_repo: https://github.com/sgl-project/sglang
---

# SGLang

<!-- AUTO:BANDEAU:START -->
> Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | open-source | self-hébergé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur de serving qui co-conçoit un **runtime** et un **langage frontend** pour programmer des
interactions LLM complexes. Son cœur, **RadixAttention**, range le cache KV en arbre radix et
**réutilise automatiquement les préfixes** partagés entre requêtes — few-shot, templates
d'agents, appels répétés. S'y ajoutent un scheduler CPU à surcoût nul, le continuous batching,
la paged attention, le *speculative decoding*, le parallélisme tensoriel, le *chunked prefill*,
les sorties structurées et la quantization (FP8, INT4, AWQ, GPTQ). Porté par LMSYS, intégré à
l'écosystème PyTorch depuis mars 2025, avec un support « day-one » des modèles récents.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Haut débit quand les requêtes **partagent un préfixe** : RAG few-shot, agents, prompts gabarisés | Le gain de RadixAttention est proportionnel au partage : sur des requêtes toutes différentes, il s'amenuise |
| Imposer des sorties structurées — JSON, grammaire — côté serveur et à grande échelle | GPU NVIDIA ou AMD requis : pas de cible CPU sérieuse |
| Programmer des pipelines LLM multi-étapes — appels chaînés, branchements — depuis le frontend | Projet jeune à itération rapide : options mouvantes, documentation parfois en retard sur le code |
| Servir vite un modèle qui vient de sortir, le support amont étant réactif | |

## Mise en œuvre

- Installation — `uv pip install "sglang[all]"`, ou conteneur
- Point d'entrée — un serveur d'inférence, et le langage frontend SGLang pour décrire les pipelines
- Prérequis — un serveur GPU NVIDIA ou AMD ; les poids se chargent depuis Hugging Face
- Exécution — distribué : parallélisme tensoriel multi-GPU, réplicas via l'orchestrateur
- Coût — gratuit, licence Apache-2.0 ; la dépense est l'infrastructure GPU. Pas d'offre managée officielle, mais adopté par des fournisseurs d'inférence

## Écosystème

### Alternatives

- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

## Ressources

- Documentation — https://docs.sglang.io/
- Dépôt — https://github.com/sgl-project/sglang

## Voir aussi

- [[Inference optimization]] — la notion du dossier : RadixAttention et *prefix caching* en sont des cas
- [[prompt-caching]] — la réutilisation de préfixe vue côté application
- [[Comparatif - Exécution & serving LLM]] — ce qui départage les moteurs du dossier
- [[Speculative decoding]] — l'accélération de décodage qu'il implémente, via EAGLE
- [[Reasoning models]] — la famille de modèles qu'il sert en priorité
- [[PyTorch]] — l'écosystème qui l'héberge
- [[HuggingFace]] — d'où viennent les poids
