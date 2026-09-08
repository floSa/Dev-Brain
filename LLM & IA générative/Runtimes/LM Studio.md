---
role: brique
nom: LM Studio
alias: [lmstudio, lms, llmster]
pitch: "Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit."
categorie: llm/runtime
famille: application
licence_type: proprietary
hosted: [self]
maturite: production
langage: 
scaling: single-node
alternatives: ["[[Ollama]]", "[[llama.cpp]]", "[[text-generation-webui]]", "[[vLLM]]", "[[TGI]]", "[[SGLang]]", "[[TensorRT-LLM]]"]
complements: ["[[LM Studio Bionic]]"]
tags: [llm, local-llm, inference, gpu, quantization]
url_docs: https://lmstudio.ai/docs
url_repo: 
---

# LM Studio

<!-- AUTO:BANDEAU:START -->
> Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application | propriétaire | self-hébergé · mono-nœud | production | aucun amont fiché |
<!-- AUTO:BANDEAU:END -->

## Définition

Application de bureau qui rend l'exécution locale de LLM entièrement cliquable : recherche et
téléchargement de modèles depuis Hugging Face, chat intégré, réglage des paramètres, et un
**serveur local à API OpenAI-compatible** pour y brancher ses applications. Sous le capot, deux
moteurs open-source — llama.cpp pour le GGUF partout, et **Apple MLX** sur Apple Silicon, que
nul autre du dossier n'expose. L'application elle-même, en revanche, est fermée. Elle existe
aussi en version **headless** (`llmster`) et en **CLI** (`lms`), pour les serveurs et la CI.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Exécuter des LLM en local avec une interface graphique : découvrir, comparer et chatter sans ligne de commande | Application fermée : aucun audit du code possible, et une dépendance d'éditeur à peser en contexte sensible |
| Onboarding rapide ou profil non-CLI : téléchargement, quantization et *GPU offload* se règlent à la souris | Pas de version serveur véritable : `llmster` et `lms` donnent du headless, le produit reste centré sur le poste de travail |
| Station **Apple Silicon** : le backend MLX natif | Un modèle qui dépasse la VRAM bascule en RAM/CPU et ralentit fortement |
| Brancher une app sur un LLM local par l'API OpenAI-compatible, sans cloud | Modèles quantifiés par défaut : la qualité est en retrait du poids plein si le quant n'est pas choisi |

## Mise en œuvre

- Installation — binaire macOS, Windows ou Linux ; version headless `llmster` et CLI `lms` pour les serveurs et la CI
- Point d'entrée — l'interface graphique, doublée d'un serveur local exposant les endpoints OpenAI-compatibles
- Prérequis — les poids se téléchargent depuis Hugging Face dans l'application ; Apple Silicon pour le backend MLX
- Exécution — une machine de bureau, mono-nœud ; le mode headless ne fait pas un serving distribué
- Coût — gratuit en usage personnel comme commercial ; l'application est propriétaire, seuls les moteurs sous-jacents et le CLI/SDK sont ouverts

## Écosystème

### Alternatives

- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

### Compléments

- [[LM Studio Bionic]] — Agent de bureau pour modèles ouverts (LM Studio, juillet 2026, propriétaire mais gratuit en local) — projets Work et Code, transcription vocale hors ligne, serveurs MCP ; inférence locale par défaut, bascule optionnelle vers un cloud à rétention zéro pour les tâches lourdes. — la couche agentique du même éditeur, posée sur ce runtime ; application distincte, pas un mode.

## Ressources

- Documentation — https://lmstudio.ai/docs

## Voir aussi

- [[Inference optimization]] — la notion du dossier : ce que le moteur optimise
- [[Comparatif - Exécution & serving LLM]] — ce qui départage les moteurs du dossier
- [[Pattern - Agent sur LLM auto-hébergé]] — le montage complet, où ce runtime tient la couche modèle
- [[HuggingFace]] — d'où viennent les poids
