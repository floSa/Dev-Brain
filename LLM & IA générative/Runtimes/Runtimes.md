---
role: hub
nom: Runtimes
alias: [runtimes LLM, serving LLM, inférence locale]
pitch: Faire tourner un modèle de langage — sur un poste, sur un GPU, ou derrière une API à haut débit.
domaines: [ai-eng, mlops]
tags: [local-llm, inference, inference-optimization, quantization, model-serving]
---

# Runtimes

> Faire tourner un modèle de langage — sur un poste, sur un GPU, ou derrière une API à haut débit.

## Ce qu'il faut comprendre

- Le clivage qui décide de tout est **un poste de travail contre un serveur de production**, et il ne se rattrape pas après coup. Un runtime de poste optimise la latence d'une conversation à la fois et la simplicité d'installation ([[Ollama]], [[LM Studio]], [[llama.cpp]]) ; un moteur de serving optimise le **débit** de dizaines de requêtes concurrentes sur GPU ([[vLLM]], [[SGLang]], [[TGI]], [[TensorRT-LLM]]). Les seconds sont plus lents que les premiers sur une requête unique, et c'est le comportement attendu.
- Le débit sur GPU se gagne sur deux mécanismes, et ce sont eux qui départagent les moteurs : le **batching continu** (une requête finie libère sa place immédiatement, au lieu d'attendre son lot) et la **gestion du cache KV** — pagination chez [[vLLM]], réutilisation automatique des préfixes chez [[SGLang]]. Cf. [[Inference optimization]].
- La **quantization** est ce qui rend l'exécution locale possible : réduire la précision des poids fait tenir un modèle dans la VRAM disponible, au prix d'une dégradation qu'il faut mesurer et non supposer. Le format GGUF de [[llama.cpp]] est l'écosystème de fait du local ; [[llmfit]] répond en amont à la seule question qui compte — quel modèle tient réellement sur cette machine.
- Il y a une **couche basse et des couches d'emballage**, et les confondre fait choisir le mauvais outil. [[llama.cpp]] est le moteur ; [[Ollama]], [[LM Studio]] et [[text-generation-webui]] l'enveloppent d'une ergonomie et d'une API. Descendre à la couche basse se paie en réglages, monter se paie en opacité sur ce qui est réellement exécuté.
- L'**API OpenAI-compatible est devenue le format commun** de tous ces runtimes. C'est ce qui rend une application portable d'un moteur à l'autre, et ce qui permet de développer en local pour déployer sur GPU sans réécrire le code d'appel.
- Le **décodage** est le réglage qui change le plus la sortie à modèle constant : [[Decoding strategies]] pour les compromis température / top-p / beam, [[Constrained decoding]] quand la sortie doit respecter une grammaire — un mécanisme du runtime, pas de la bibliothèque appelante. [[Speculative decoding]] et [[Multi-Token Prediction]] sont les deux façons de produire plus d'un token par passe.
- Côté application, une génération se **streame** : [[Server-Sent Events & streaming LLM]] est le protocole que ces serveurs exposent, et le premier token perçu compte plus que le débit total pour l'utilisateur.
- Un modèle peut être **la brique elle-même** quand il est assez petit pour embarquer son moteur : [[needle]] tient dans 14 Mo et garantit sa sortie par grammaire. C'est la même logique que les [[Small Language Models]] — le bon modèle est le plus petit qui passe l'éval.

## Choisir

- Lancer un modèle ouvert en deux commandes sur mon poste → [[Ollama]].
- La même chose avec une interface graphique et le choix des moteurs → [[LM Studio]].
- Régler finement la quantization, ou tourner sur CPU / GPU grand public → [[llama.cpp]].
- Essayer beaucoup de backends et de modalités depuis une UI web → [[text-generation-webui]].
- Servir en production sur GPU, priorité au débit → [[vLLM]].
- Même besoin avec beaucoup de préfixes partagés (prompts systèmes, few-shot) → [[SGLang]].
- Rester dans l'écosystème Hugging Face, endpoints inclus → [[TGI]].
- Extraire la dernière latence d'un parc NVIDIA, compilation acceptée → [[TensorRT-LLM]].
- De l'appel d'outils et de l'extraction structurée sur un appareil contraint → [[needle]].
- Savoir ce que ma machine peut faire tourner avant de télécharger → [[llmfit]].
- Appeler des modèles hébergés par d'autres plutôt que les héberger → [[LiteLLM]] ou [[OpenRouter]], et non ce dossier.

<!-- AUTO:START -->
### Briques
- [[llama.cpp]] — Moteur d'inférence LLM en C/C++ (projet ggml) sur CPU et GPU grand public — format GGUF et quantization agressive, dépendances minimales ; la brique bas niveau derrière la plupart des runtimes locaux.
- [[LM Studio]] — Application de bureau pour exécuter des LLM en local — GUI soignée (recherche, téléchargement, chat), moteurs llama.cpp (GGUF) et MLX (Apple Silicon) et serveur local à API OpenAI-compatible ; propriétaire mais gratuit.
- [[needle]] — Modèle spécialisé de 45 M paramètres pour l'appel d'outils et l'extraction structurée (Apache-2.0, poids compris) — quantifié en 2 bits dans un binaire de 14 Mo qui embarque son propre moteur, du Raspberry Pi au WebAssembly ; sortie JSON garantie par grammaire et score de confiance pour escalader vers un gros modèle.
- [[Ollama]] — Runtime local de LLM le plus simple — une commande pour récupérer et lancer un modèle open (GGUF, via llama.cpp), API REST OpenAI-compatible et Modelfiles ; pensé pour le poste de dev et le prototypage.
- [[SGLang]] — Moteur de serving LLM rapide articulé autour de RadixAttention (réutilisation automatique du cache KV de préfixes) — haut débit GPU, sorties structurées et programmation de pipelines LLM ; écosystème PyTorch/LMSYS.
- [[TensorRT-LLM]] — Moteur d'inférence LLM open-source de NVIDIA — compilation TensorRT et kernels CUDA pour le débit et la latence maximaux sur GPU NVIDIA, parallélisme multi-GPU/multi-nœuds ; API Python de haut niveau, runtimes Python et C++.
- [[text-generation-webui]] — UI web open-source (Gradio) pour LLM locaux — multi-backends commutables (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), chat, vision, tool-calling et API compatible OpenAI/Anthropic ; le couteau suisse historique de l'inférence locale.
- [[TGI]] — Serveur d'inférence LLM de Hugging Face (Rust + Python) — production-grade : continuous batching, sharding multi-GPU, streaming ; moteur des Inference Endpoints HF.
- [[vLLM]] — Moteur de serving LLM haut débit (PagedAttention, continuous batching) — référence open-source du throughput GPU en production, API OpenAI-compatible et parallélisme tensoriel multi-GPU.

### Comparatifs
- [[Comparatif - Exécution & serving LLM]]
<!-- AUTO:END -->
