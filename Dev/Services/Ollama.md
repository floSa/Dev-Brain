---
galaxie: dev
type: service
nom: Ollama
alias: [ollama]
pitch: "Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage."
categorie: llm/local
licence_type: open-source
hosted: self
maturite: production
langage: Go
scaling: single-node
alternatives: ["[[Dev/Services/llama.cpp|llama.cpp]]", "[[Dev/Services/LM Studio|LM Studio]]", "[[Dev/Services/text-generation-webui|text-generation-webui]]", "[[Dev/Services/vLLM|vLLM]]", "[[Dev/Services/TGI|TGI]]", "[[Dev/Services/SGLang|SGLang]]", "[[Dev/Services/TensorRT-LLM|TensorRT-LLM]]"]
remplace_par: []
status: actif
tags: [llm, local-llm, inference, gpu, quantization]
url_docs: https://docs.ollama.com/
url_repo: https://github.com/ollama/ollama
---

# Ollama

## Pourquoi

Runtime local de LLM qui privilégie la simplicité : `ollama run llama3` télécharge un modèle quantifié depuis la bibliothèque officielle et lance une session, sans configuration. Écrit en **Go**, Ollama enveloppe [[Dev/Services/llama.cpp|llama.cpp]] (modèles **GGUF**) et y ajoute un registre de modèles (`ollama.com/library`), des **Modelfiles** (à la Dockerfile : modèle de base + paramètres + system prompt), un démon serveur avec **API REST** et un endpoint **OpenAI-compatible**. Multiplateforme (macOS, Linux, Windows), il utilise le GPU s'il est présent (Metal, CUDA, ROCm) et retombe sur le CPU sinon.

## Quand l'utiliser

- **Poste de dev / prototypage** : faire tourner un LLM open en local en une commande.
- Brancher une app sur un LLM local via l'**API OpenAI-compatible** (RAG, agents, tests) sans dépendre d'un fournisseur cloud.
- Données sensibles à garder **on-device**, sans appel réseau.
- Comparer rapidement plusieurs modèles open (un `pull` par modèle).

## Quand NE PAS l'utiliser

- Débit GPU élevé pour servir **beaucoup d'utilisateurs concurrents** en production → [[Dev/Services/vLLM|vLLM]], [[Dev/Services/TGI|TGI]] ou [[Dev/Services/SGLang|SGLang]].
- Contrôle bas niveau fin (flags, quantizations sur mesure, hardware exotique) → [[Dev/Services/llama.cpp|llama.cpp]] directement.
- Déploiement multi-GPU / multi-nœuds : Ollama vise une seule machine.

## Déploiement & coût

- Open-source (MIT), gratuit ; self-host (binaire ou conteneur), démon sur `localhost:11434`.
- Offre managée récente **Ollama Cloud** (modèles hébergés, payante) pour décharger les gros modèles — mais le cœur reste local.
- Scaling **single-node** : une instance par machine ; pas de sharding multi-GPU natif comme les serveurs haut débit.

## Pièges

- Modèles **quantifiés par défaut** (souvent Q4) : qualité moindre que le poids plein — choisir explicitement un tag plus précis si besoin.
- Un modèle qui dépasse la VRAM bascule en RAM/CPU et **ralentit fortement**, sans erreur claire.
- Le batching concurrent reste limité face à un vrai serveur d'inférence : inadapté à une forte charge simultanée.

## Alternatives

- [[Dev/Services/llama.cpp|llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[Dev/Services/vLLM|vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[Dev/Services/TGI|TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[Dev/Services/SGLang|SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[Dev/Services/LM Studio|LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[Dev/Services/text-generation-webui|text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

## Liens

- Construit sur [[Dev/Services/llama.cpp|llama.cpp]] (inférence GGUF sous-jacente).
- Modèles tirés du hub [[Dev/Services/HuggingFace|HuggingFace]] (conversion en GGUF).
- [[Comparatif - Exécution & serving LLM]] — comparatif de la catégorie
- Doc : https://docs.ollama.com/
