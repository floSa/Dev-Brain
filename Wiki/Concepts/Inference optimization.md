---
galaxie: wiki
type: concept
nom: Inference optimization
alias: [optimisation de l'inférence, KV-cache, cache KV, continuous batching, batching dynamique, PagedAttention, débit LLM, latence LLM]
categorie: concept/llm
domaines: [ai-eng, mlops]
tags: [inference-optimization, inference, llm, gpu]
---

# Inference optimization

## Aperçu

- L'inférence d'un LLM est **autorégressive** : un token à la fois, chaque pas relisant tout le contexte. Sans optimisation, c'est lent et le GPU est mal exploité.
- L'optimisation de l'inférence regroupe les techniques qui **réduisent latence et coût** et **augmentent le débit** sans changer la sortie du modèle — c'est le cœur des runtimes de serving.

## Concepts clés

### Le KV-cache
- Sans cache, l'attention recalculerait les clés/valeurs de tout le préfixe à chaque pas. Le **KV-cache** les mémorise : on ne calcule que pour le nouveau token.
- Indispensable, mais sa **taille croît** avec la longueur de contexte × le nombre de requêtes simultanées → c'est souvent le **premier poste de VRAM**, devant les poids.

### Deux régimes : prefill vs decode
- **Prefill** (traitement du prompt) : calcul massivement parallèle, *compute-bound*.
- **Decode** (génération token par token) : *memory-bound* — limité par la bande passante mémoire, GPU sous-utilisé. La plupart des optimisations visent le decode.

### Batching
- **Static batching** : attendre un lot complet → latence et gaspillage. **Continuous batching** (in-flight) : les requêtes entrent et sortent du lot à chaque pas, ce qui sature le GPU sous charge variable. Gain de débit majeur.

### Gestion mémoire du cache
- **PagedAttention** ([[Dev/Services/vLLM|vLLM]]) gère le KV-cache par pages, comme la mémoire virtuelle d'un OS → fin de la fragmentation.
- **Prefix caching / RadixAttention** ([[Dev/Services/SGLang|SGLang]]) réutilise le cache des préfixes partagés (system prompt, few-shot) entre requêtes.

### Réduire le calcul lui-même
- **Quantization** des poids et du cache (FP8, INT8/4) ; **Flash Attention** (attention fusionnée, économe en mémoire) ; **décodage spéculatif** pour produire plusieurs tokens par passe.

## Les maths, simplement

- Mémoire du KV-cache (octets) $\approx 2 \cdot b \cdot s \cdot n_{\text{layers}} \cdot h \cdot \text{prec}$ : le `2` = clés + valeurs, $b$ le batch, $s$ la longueur, $n_{\text{layers}}$ les couches, $h$ la dimension cachée, $\text{prec}$ les octets par élément. Elle croît **linéairement** avec le contexte et le nombre de requêtes — d'où le rôle central de sa gestion.
- Le decode est *memory-bound* : le temps par token est dominé par la **lecture des poids** (et du cache) depuis la VRAM, pas par les FLOPs. D'où l'intérêt du batching (amortir la lecture des poids sur plusieurs requêtes) et de la quantization (moins d'octets à lire).

## En pratique

- Ne pas réimplémenter : utiliser un runtime qui intègre déjà ces optimisations — [[Dev/Services/vLLM|vLLM]], [[Dev/Services/SGLang|SGLang]], [[Dev/Services/TGI|TGI]].
- Mesurer les **deux** métriques : *time-to-first-token* (dominé par le prefill) et débit / *inter-token latency* (dominé par le decode).
- Activer le **prefix caching** quand un long system prompt est partagé entre requêtes (gros gain à peu de frais).
- Surveiller la VRAM : le KV-cache, pas les poids, est souvent ce qui plafonne la concurrence atteignable.

## Approches voisines & alternatives

- [[Speculative decoding]] — technique d'optimisation d'inférence à part entière : plusieurs tokens vérifiés par passe.
- [[Decoding strategies]] — l'optimisation accélère le décodage sans changer la distribution cible.
- [[prompt-caching]] — cache des préfixes au niveau API ; s'appuie sur le KV-cache côté serveur.
- *Quantization* (à créer, `concept/dl`) — réduit les octets à lire : levier d'inférence majeur.
- [[Flash Attention and efficient attention]] — attention optimisée mémoire (et MQA/GQA pour alléger le KV-cache).
- Runtimes qui implémentent tout ceci : [[Dev/Services/vLLM|vLLM]] (PagedAttention), [[Dev/Services/SGLang|SGLang]] (RadixAttention), [[Dev/Services/TGI|TGI]] (continuous batching), [[Dev/Services/TensorRT-LLM|TensorRT-LLM]].

## Pour aller plus loin

- Kwon et al. (2023) — *Efficient Memory Management for LLM Serving with PagedAttention* (papier vLLM).
- Zheng et al. (2024) — *SGLang: Efficient Execution of Structured Language Model Programs* (RadixAttention).
- Dao et al. (2022) — *FlashAttention*.
