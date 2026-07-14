---
galaxie: wiki
type: concept
nom: Quantization
alias: [Quantification, quantisation, INT8, INT4, FP8, GGUF, GPTQ, AWQ, PTQ, QAT, K-quants]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [quantization, model-compression, deep-learning, inference-optimization]
---

# Quantization

## Aperçu

- Réduire la **précision numérique** des poids (et parfois des activations) — de FP16/FP32 vers INT8, INT4 ou FP8 — pour diviser la **mémoire** et accélérer le **calcul**, au prix d'une perte de qualité maîtrisée.
- C'est le levier qui fait tenir un LLM de plusieurs milliards de paramètres sur une machine ordinaire : un modèle en **4 bits** occupe environ **¼** de sa taille FP16.

## Concepts clés

### PTQ vs QAT
- **Post-Training Quantization (PTQ)** : quantizer un modèle déjà entraîné, sans réentraînement — rapide, c'est le cas courant pour les LLM.
- **Quantization-Aware Training (QAT)** : simuler la quantization **pendant** l'entraînement → meilleure qualité aux très basses précisions, mais coûteux.

### Mapping et granularité
- Conversion affine : un **facteur d'échelle** $s$ et un **zéro** $z$ relient le réel et l'entier. Granularité **par tenseur**, **par canal** ou **par groupe** : plus fin = plus précis, plus de métadonnées.
- Problème des **outliers** : quelques activations extrêmes dégradent la quantization → schémas qui les isolent (LLM.int8(), AWQ).

### Schémas LLM courants
- **GGUF / K-quants** (llama.cpp), **GPTQ** (par couche, second ordre), **AWQ** (activation-aware), **FP8** (GPU Hopper/Blackwell), **bitsandbytes** pour QLoRA.

## Les maths, simplement

- Quantization : $x_q = \operatorname{round}(x/s) + z$ ; déquantization : $\hat{x} = s\,(x_q - z)$. L'erreur $\hat{x}-x$ est l'**erreur de quantization**.
- Budget mémoire : passer de 16 à $b$ bits divise la taille des poids par $\approx 16/b$ — d'où le rôle clé dans l'[[Inference optimization|optimisation de l'inférence]].

## En pratique

- Le **4 bits** est le point d'équilibre qualité/mémoire pour le LLM local ; en dessous (Q2/Q3), la qualité chute nettement — surveiller la « falaise ».
- Se combine avec le fine-tuning : **[[LoRA et QLoRA|QLoRA]]** entraîne des adaptateurs LoRA au-dessus d'un modèle gelé en 4 bits (NF4).
- Runtimes qui l'exploitent : [[Dev/Services/vLLM|vLLM]] (AWQ, GPTQ, FP8) pour le débit GPU, [[Dev/Services/llama.cpp|llama.cpp]] (GGUF, K-quants, imatrix) pour CPU et GPU grand public.
- Complémentaire de la [[Distillation]] : distiller réduit la **taille**, quantizer réduit la **précision** — souvent enchaînés.

## Approches voisines & alternatives

- [[Distillation]] — compression par réduction de taille (prof → élève), opposée/complémentaire à la baisse de précision.
- [[Pruning]] — compression par suppression de poids/structures ; orthogonale à la baisse de précision, souvent enchaînée.
- [[Small Language Models]] — la quantization est une de leurs briques d'efficience.
- [[Inference optimization]] — la quantization s'inscrit dans l'arsenal d'accélération de l'inférence.
- [[LoRA et QLoRA]] — QLoRA marie quantization 4 bits (NF4) et fine-tuning par adaptateurs de rang faible.
- [[PEFT]] — le parapluie du fine-tuning paramétriquement efficace, que la 4-bit rend encore plus léger.
- [[Dev/Services/vLLM|vLLM]] — serving GPU haut débit avec quantization AWQ/GPTQ/FP8.
- [[Dev/Services/llama.cpp|llama.cpp]] — quantization agressive GGUF/K-quants pour l'inférence locale.

## Pour aller plus loin

- Dettmers et al. (2022) — *LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale*.
- Frantar et al. (2022) — *GPTQ* ; Lin et al. (2023) — *AWQ*.
- Dettmers et al. (2023) — *QLoRA: Efficient Finetuning of Quantized LLMs*.
