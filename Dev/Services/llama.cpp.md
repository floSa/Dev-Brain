---
galaxie: dev
type: service
nom: llama.cpp
alias: [llamacpp, llama-cpp, ggml]
pitch: "Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux."
categorie: llm/local
licence_type: open-source
hosted: self
maturite: production
langage: C/C++
scaling: single-node
alternatives: ["[[Dev/Services/Ollama|Ollama]]", "[[Dev/Services/LM Studio|LM Studio]]", "[[Dev/Services/text-generation-webui|text-generation-webui]]", "[[Dev/Services/vLLM|vLLM]]", "[[Dev/Services/TGI|TGI]]", "[[Dev/Services/SGLang|SGLang]]", "[[Dev/Services/TensorRT-LLM|TensorRT-LLM]]"]
remplace_par: []
status: actif
tags: [llm, local-llm, inference, gpu, quantization]
url_docs: https://github.com/ggml-org/llama.cpp/tree/master/docs
url_repo: https://github.com/ggml-org/llama.cpp
---

# llama.cpp

## Pourquoi

Moteur d'inférence LLM écrit en **C/C++** au-dessus de la bibliothèque de tenseurs **ggml**, conçu pour tourner partout avec un minimum de dépendances. C'est la référence de l'inférence **sur CPU et GPU grand public** : il introduit le format **GGUF** (poids + métadonnées dans un seul fichier) et une **quantization agressive** (K-quants, importance matrix, de 2 à 8 bits) qui fait tenir des modèles de plusieurs milliards de paramètres dans la RAM/VRAM d'une machine ordinaire. Backends multiples (CUDA, Metal, Vulkan, ROCm, CPU AVX). Livre des binaires (`llama-cli`, `llama-server` avec API OpenAI-compatible) et sert de socle bas niveau à [[Dev/Services/Ollama|Ollama]], [[Dev/Services/LM Studio|LM Studio]] et la plupart des outils locaux.

## Quand l'utiliser

- Faire tourner un LLM sur **CPU**, Apple Silicon ou GPU grand public, voire des cibles embarquées.
- Maîtriser finement la **quantization** (format GGUF, niveau de bits, imatrix) pour le compromis qualité/mémoire.
- Embarquer l'inférence dans un binaire **portable et sans dépendances lourdes** (pas de runtime Python).
- Comprendre / contrôler ce que des wrappers comme [[Dev/Services/Ollama|Ollama]] font en coulisses.

## Quand NE PAS l'utiliser

- Simplicité « une commande » et registre de modèles → [[Dev/Services/Ollama|Ollama]] (qui l'enveloppe).
- Débit GPU maximal pour **beaucoup de requêtes concurrentes** en production → [[Dev/Services/vLLM|vLLM]], [[Dev/Services/TGI|TGI]] ou [[Dev/Services/SGLang|SGLang]].
- Serving distribué multi-GPU / multi-nœuds : llama.cpp vise une machine.

## Déploiement & coût

- Open-source (MIT), gratuit ; compilation locale (CMake) ou binaires pré-compilés.
- Self-host uniquement ; `llama-server` expose une API HTTP (dont un mode OpenAI-compatible).
- Scaling **single-node** ; mode RPC expérimental pour répartir un modèle sur quelques machines, mais ce n'est pas un serveur de production scalable.

## Pièges

- Trouver le **bon niveau de quantization** est un compromis : trop agressif (Q2/Q3) dégrade nettement la qualité.
- Les **backends GPU** demandent une compilation adaptée (flags CUDA/Metal/Vulkan) — un binaire CPU n'utilise pas le GPU.
- Projet à **cadence très rapide** (releases quasi quotidiennes) : options et formats évoluent, GGUF a déjà cassé la compat par le passé.

## Alternatives

- [[Dev/Services/Ollama|Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[Dev/Services/vLLM|vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[Dev/Services/TGI|TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[Dev/Services/SGLang|SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[Dev/Services/LM Studio|LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[Dev/Services/text-generation-webui|text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

## Liens

- Socle d'inférence de [[Dev/Services/Ollama|Ollama]] (et d'autres runtimes locaux).
- Modèles convertis au format GGUF depuis [[Dev/Services/HuggingFace|HuggingFace]].
- [[Quantization]] agressive des poids (GGUF, K-quants, imatrix) — cœur du projet.
- [[Comparatif - Exécution & serving LLM]] — comparatif de la catégorie
- Doc : https://github.com/ggml-org/llama.cpp/tree/master/docs
