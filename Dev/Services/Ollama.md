---
role: brique
nom: Ollama
alias: [ollama]
pitch: "Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage."
categorie: llm/runtime
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: single-node
alternatives: ["[[llama.cpp]]", "[[LM Studio]]", "[[text-generation-webui]]", "[[vLLM]]", "[[TGI]]", "[[SGLang]]", "[[TensorRT-LLM]]", "[[needle]]"]
complements: []
tags: [llm, local-llm, inference, gpu, quantization]
url_docs: https://docs.ollama.com/
url_repo: https://github.com/ollama/ollama
---

# Ollama

## Pourquoi

Runtime local de LLM qui privilégie la simplicité : `ollama run llama3` télécharge un modèle quantifié depuis la bibliothèque officielle et lance une session, sans configuration. Écrit en **Go**, Ollama enveloppe [[llama.cpp]] (modèles **GGUF**) et y ajoute un registre de modèles (`ollama.com/library`), des **Modelfiles** (à la Dockerfile : modèle de base + paramètres + system prompt), un démon serveur avec **API REST** et un endpoint **OpenAI-compatible**. Multiplateforme (macOS, Linux, Windows), il utilise le GPU s'il est présent (Metal, CUDA, ROCm) et retombe sur le CPU sinon.

## Quand l'utiliser

- **Poste de dev / prototypage** : faire tourner un LLM open en local en une commande.
- Brancher une app sur un LLM local via l'**API OpenAI-compatible** (RAG, agents, tests) sans dépendre d'un fournisseur cloud.
- Données sensibles à garder **on-device**, sans appel réseau.
- Comparer rapidement plusieurs modèles open (un `pull` par modèle).

## Quand NE PAS l'utiliser

- Débit GPU élevé pour servir **beaucoup d'utilisateurs concurrents** en production → [[vLLM]], [[TGI]] ou [[SGLang]].
- Contrôle bas niveau fin (flags, quantizations sur mesure, hardware exotique) → [[llama.cpp]] directement.
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

- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.
- [[needle]] — Modèle spécialisé de 45 M paramètres pour l'appel d'outils et l'extraction structurée (Apache-2.0, poids compris) — quantifié en 2 bits dans un binaire de 14 Mo qui embarque son propre moteur, du Raspberry Pi au WebAssembly ; sortie JSON garantie par grammaire et score de confiance pour escalader vers un gros modèle.

## Liens

- Construit sur [[llama.cpp]] (inférence GGUF sous-jacente).
- Modèles tirés du hub [[HuggingFace]] (conversion en GGUF).
- Sert de couche modèle à un agent auto-hébergé — cf. [[Pattern - Agent sur LLM auto-hébergé]]. **Deux pièges y sont documentés** : l'endpoint `/v1` casse le tool calling avec certains harnais (utiliser l'API native), et le contexte par défaut de 4 096 tokens est très en dessous de ce qu'exige un agent.
- [[Comparatif - Exécution & serving LLM]] — comparatif de la catégorie
- Doc : https://docs.ollama.com/
