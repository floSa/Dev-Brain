---
role: brique
nom: TGI
alias: [tgi, text-generation-inference]
pitch: "Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF."
categorie: llm/runtime
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Rust/Python
scaling: distributed
alternatives: ["[[Ollama]]", "[[llama.cpp]]", "[[LM Studio]]", "[[text-generation-webui]]", "[[vLLM]]", "[[SGLang]]", "[[TensorRT-LLM]]"]
complements: []
tags: [llm, model-serving, inference, gpu]
url_docs: https://huggingface.co/docs/text-generation-inference
url_repo: https://github.com/huggingface/text-generation-inference
---

# TGI

<!-- AUTO:BANDEAU:START -->
> Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Rust/Python | open-source | self-hébergé ou managé · distribué | production | dépôt archivé · 2026-03-21 |
<!-- AUTO:BANDEAU:END -->

## Définition

*Text Generation Inference*, le serveur d'inférence maison de Hugging Face. Son architecture
est bicéphale : un **routeur Rust** encaisse les requêtes et compose les batches, devant des
**workers Python** qui exécutent le modèle, les deux communiquant en gRPC. Il apporte le
continuous batching, l'attention optimisée (Flash, Paged), le **streaming par SSE**, la
quantization (bitsandbytes, GPTQ, AWQ, FP8) et le **sharding tensoriel multi-GPU** pour les
gros modèles. C'est le moteur derrière les Inference Endpoints de Hugging Face : c'est cet
ancrage écosystème qui le fait choisir, pas le débit brut.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Ancrage fort dans l'écosystème Hugging Face : hub, endpoints managés, mêmes formats | **Historique de licence** : de la v0.9.4 (mi-2023) à début 2024, TGI était sous licence restrictive HFOIL avant retour à Apache-2.0 — vérifier la version si la conformité compte |
| Streaming robuste et batching continu sous charge | GPU NVIDIA comme cible principale, et image conteneur volumineuse |
| Répartir un gros modèle sur plusieurs GPU par sharding | Le couple routeur Rust / workers Python complique le débogage bas niveau face à un serveur tout-Python |
| Vouloir un serveur *production-grade* maintenu, sans tout assembler soi-même | |

## Mise en œuvre

- Installation — conteneur officiel ; rien à compiler
- Point d'entrée — un serveur HTTP avec streaming SSE, plus les Inference Endpoints côté managé
- Prérequis — un serveur GPU, NVIDIA en pratique ; les poids se chargent depuis le hub
- Exécution — distribué : sharding tensoriel multi-GPU, réplicas via l'orchestrateur ; disponible aussi en managé
- Coût — gratuit en self-host, Apache-2.0 sur la branche actuelle ; les Inference Endpoints sont facturés à l'usage ou au GPU

## Écosystème

### Alternatives

- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

## Ressources

- Documentation — https://huggingface.co/docs/text-generation-inference
- Dépôt — https://github.com/huggingface/text-generation-inference

## Voir aussi

- [[Inference optimization]] — la notion du dossier : continuous batching et sharding en sont des cas
- [[Server-Sent Events & streaming LLM]] — le mécanisme de streaming qu'il expose
- [[Comparatif - Exécution & serving LLM]] — ce qui départage les moteurs du dossier
- [[Speculative decoding]] — l'accélération de décodage qu'il implémente, via Medusa et EAGLE
- [[HuggingFace]] — le hub et les Inference Endpoints dont il est le moteur
