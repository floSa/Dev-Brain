---
galaxie: dev
type: service
nom: text-generation-webui
alias: [oobabooga, textgen, text-gen-webui]
pitch: "UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale."
categorie: llm/local
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Ollama|Ollama]]", "[[Dev/Services/llama.cpp|llama.cpp]]", "[[Dev/Services/LM Studio|LM Studio]]", "[[Dev/Services/vLLM|vLLM]]", "[[Dev/Services/TGI|TGI]]", "[[Dev/Services/SGLang|SGLang]]", "[[Dev/Services/TensorRT-LLM|TensorRT-LLM]]"]
remplace_par: []
status: actif
tags: [llm, local-llm, inference, gpu, quantization]
url_docs: https://github.com/oobabooga/text-generation-webui/wiki
url_repo: https://github.com/oobabooga/text-generation-webui
---

# text-generation-webui

## Pourquoi

Interface web (bâtie sur [[Dev/Services/Gradio|Gradio]]) pour faire tourner des LLM en local, par **oobabooga** — le « couteau suisse » historique du milieu. Sa force : le **multi-backends commutables sans redémarrage** — [[Dev/Services/llama.cpp|llama.cpp]], ik_llama.cpp, Transformers, ExLlamaV3 et [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] — ce qui permet de charger à peu près n'importe quel format de modèle (GGUF, GPTQ, EXL2…). Chat, mode notebook, **vision**, **tool-calling**, extensions, et une **API compatible OpenAI/Anthropic** (Chat/Completions/Messages). Désormais distribué aussi comme **app de bureau** (rebrand « TextGen »). Écrit en **Python**, licence **AGPL-3.0**.

## Quand l'utiliser

- **Tester et comparer** des modèles de formats variés (GGUF, GPTQ, EXL2…) dans une seule UI, sans réinstaller un moteur par format.
- Besoin d'une **UI riche** locale : chat + notebook + extensions + paramètres de sampling fins.
- Exposer un modèle local via une **API OpenAI/Anthropic-compatible** pour brancher des apps.
- Expérimentation / bidouille (personas, RAG simple, vision) sur un poste équipé GPU.

## Quand NE PAS l'utiliser

- Démarrage ultra-simple en une commande → [[Dev/Services/Ollama|Ollama]].
- GUI de bureau packagée et soignée → [[Dev/Services/LM Studio|LM Studio]].
- Serving GPU haut débit multi-utilisateurs en production → [[Dev/Services/vLLM|vLLM]], [[Dev/Services/TGI|TGI]] ou [[Dev/Services/SGLang|SGLang]].
- Contrainte de licence : l'**AGPL-3.0** peut être bloquante pour certains usages commerciaux/intégrations.

## Déploiement & coût

- Open-source (**AGPL-3.0**), gratuit ; self-host (installeurs un-clic par OS, ou Python) ; tourne sur GPU NVIDIA/AMD et CPU selon le backend.
- Pas de SaaS officiel ; usage local ou sur un serveur perso, UI exposée sur le réseau.
- Scaling **single-node** : une machine, un modèle chargé à la fois (mais backend interchangeable).

## Pièges

- **AGPL-3.0** : copyleft fort — attention en contexte commercial/intégration (obligation de fournir le code des modifications aux utilisateurs).
- La multiplicité des backends/loaders est puissante mais **source de confusion** (choisir le bon loader selon le format).
- Dépendances lourdes (CUDA, ExLlama, etc.) : l'installation peut casser entre versions ; préférer les installeurs fournis.
- Orienté **poste de travail** : pas pensé pour la forte concurrence ni le multi-GPU de serving.

## Alternatives

- [[Dev/Services/Ollama|Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[Dev/Services/llama.cpp|llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[Dev/Services/LM Studio|LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[Dev/Services/vLLM|vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[Dev/Services/TGI|TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[Dev/Services/SGLang|SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

## Liens

- UI construite sur [[Dev/Services/Gradio|Gradio]] ; modèles tirés du hub [[Dev/Services/HuggingFace|HuggingFace]].
- Peut piloter [[Dev/Services/llama.cpp|llama.cpp]] et [[Dev/Services/TensorRT-LLM|TensorRT-LLM]] comme backends.
- [[Comparatif - Exécution & serving LLM]] — comparatif de la catégorie
- Doc : https://github.com/oobabooga/text-generation-webui/wiki
