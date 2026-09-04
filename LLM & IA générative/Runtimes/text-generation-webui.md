---
role: brique
nom: text-generation-webui
alias: [oobabooga, textgen, text-gen-webui]
pitch: "UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale."
categorie: llm/runtime
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Ollama]]", "[[llama.cpp]]", "[[LM Studio]]", "[[vLLM]]", "[[TGI]]", "[[SGLang]]", "[[TensorRT-LLM]]"]
complements: []
tags: [llm, local-llm, inference, gpu, quantization]
url_docs: https://github.com/oobabooga/text-generation-webui/wiki
url_repo: https://github.com/oobabooga/text-generation-webui
---

# text-generation-webui

<!-- AUTO:BANDEAU:START -->
> UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Application Python | open-source | self-hébergé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Interface web bâtie sur [[Gradio]] par **oobabooga**, le couteau suisse historique de
l'inférence locale. Sa singularité tient en un point : elle **commute de backend sans
redémarrer** — llama.cpp, ik_llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM — donc charge
GGUF, GPTQ et EXL2 dans une même UI, là où les autres imposent un moteur par format. S'y
ajoutent le chat, un mode notebook, la vision, le *tool-calling*, des extensions, et une API
compatible **OpenAI et Anthropic**. Désormais distribuée aussi comme application de bureau,
sous le nom « TextGen ».

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tester et comparer des modèles de formats variés — GGUF, GPTQ, EXL2 — sans réinstaller un moteur par format | Licence **AGPL-3.0** : copyleft fort, obligation de fournir le code des modifications aux utilisateurs — bloquant pour beaucoup d'intégrations commerciales |
| UI riche en local : chat, mode notebook, extensions, paramètres de sampling fins | La multiplicité des loaders est aussi une source d'erreur : le bon loader dépend du format du modèle |
| Exposer un modèle local via une API compatible OpenAI **et** Anthropic | Dépendances lourdes (CUDA, ExLlama) : l'installation casse entre versions — s'en tenir aux installeurs fournis |
| Expérimentation sur un poste équipé GPU : personas, RAG simple, vision | Un seul modèle chargé à la fois, et rien qui vise la forte concurrence ou le multi-GPU de serving |

## Mise en œuvre

- Installation — installeurs un-clic par OS, ou installation Python ; existe aussi en application de bureau
- Point d'entrée — l'UI web Gradio, doublée d'une API compatible OpenAI et Anthropic (Chat, Completions, Messages)
- Prérequis — GPU NVIDIA ou AMD selon le backend, CPU possible ; un loader à choisir selon le format du modèle
- Exécution — une machine, mono-nœud, un modèle chargé à la fois, backend commutable à chaud ; UI exposable sur le réseau
- Coût — gratuit ; la contrainte réelle est la licence AGPL-3.0, pas le prix

## Écosystème

### Alternatives

- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.
- [[TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.

## Ressources

- Documentation — https://github.com/oobabooga/text-generation-webui/wiki
- Dépôt — https://github.com/oobabooga/text-generation-webui

## Voir aussi

- [[Inference optimization]] — la notion du dossier : ce que les backends optimisent
- [[Comparatif - Exécution & serving LLM]] — ce qui départage les moteurs du dossier
- [[HuggingFace]] — d'où viennent les poids, quel que soit le format
