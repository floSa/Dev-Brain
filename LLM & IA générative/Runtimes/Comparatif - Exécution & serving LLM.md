---
role: comparatif
nom: Comparatif - Exécution & serving LLM
categorie: llm/runtime
tags: [local-llm, model-serving, inference, quantization]
---

# Comparatif - Exécution & serving LLM

> On tranche sur : qui consomme le modèle — un poste de travail ou beaucoup de requêtes concurrentes — puis, à cet étage, le matériel accepté et la forme livrée : bibliothèque, démon, GUI ou moteur compilé.

![[Comparatif - Exécution & serving LLM.base]]

## Ce qui départage

- [[llama.cpp]] — le **socle bas niveau** que la plupart des autres enveloppent : C/C++ sur ggml, dépendances minimales, format **GGUF** et quantization agressive (K-quants, imatrix, 2 à 8 bits) qui fait tenir un gros modèle dans une machine ordinaire. Il vise **une** machine, et un binaire compilé sans les bons flags CUDA/Metal/Vulkan n'utilise pas le GPU.
- [[Ollama]] — llama.cpp rendu opérationnel en **une commande** : registre de modèles, Modelfiles à la Dockerfile, démon avec API OpenAI-compatible. Modèles quantifiés par défaut (souvent Q4), et un modèle qui dépasse la VRAM bascule en RAM/CPU et ralentit fortement, sans erreur claire.
- [[LM Studio]] — le même terrain, mais avec une **GUI** : recherche, téléchargement et chat cliquables, plus le backend **MLX** natif sur Apple Silicon, que personne d'autre ici n'a. C'est le seul du lot dont **l'application est propriétaire** — pas d'audit du code, dépendance à un éditeur.
- [[text-generation-webui]] — le seul à **commuter de backend sans redémarrer** (llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM), donc à charger GGUF, GPTQ et EXL2 dans une même UI. Deux contreparties : la licence **AGPL-3.0**, bloquante en intégration commerciale, et le choix du bon loader par format.
- [[vLLM]] — **PagedAttention** : le cache KV géré en pages comme la mémoire virtuelle d'un OS, ce qui supprime la fragmentation et rend le continuous batching efficace. C'est la référence du débit, au prix d'une préallocation VRAM (`gpu_memory_utilization`) surprenante au premier lancement.
- [[SGLang]] — **RadixAttention** : le cache KV en arbre radix, qui réutilise automatiquement les **préfixes partagés** entre requêtes — RAG few-shot, templates d'agents. Le gain est proportionnel à ce partage : sur des requêtes toutes différentes, il s'amenuise.
- [[TGI]] — routeur **Rust** devant des workers Python, et le moteur des Inference Endpoints de Hugging Face : c'est l'ancrage écosystème qui le choisit, pas le débit brut. Vérifier la version si la conformité compte — de mi-2023 à début 2024 il était sous licence restrictive HFOIL, avant retour à Apache-2.0.
- [[TensorRT-LLM]] — le modèle est **compilé** en un moteur TensorRT, avec les kernels et les précisions les plus récentes de NVIDIA (FP8, FP4 sur Blackwell). Latence et débit maximaux, mais un build par couple modèle / GPU / précision — inadapté à l'expérimentation, et verrou matériel total.
- [[needle]] — l'intrus assumé : **pas un runtime mais un modèle** de 45 M paramètres qui embarque son propre moteur dans 14 Mo, dédié à l'appel d'outils et à l'extraction structurée, JSON garanti par grammaire. Fenêtre de 256 tokens glissante : ni chat, ni génération libre.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
