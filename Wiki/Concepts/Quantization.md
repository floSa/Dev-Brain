---
galaxie: wiki
type: concept
nom: Quantization
alias: [Quantification, quantisation, INT8, INT4, FP8, GGUF, GPTQ, AWQ, PTQ, QAT, K-quants, NVFP4, MXFP4, FP4, microscaling, block scaling, quantization 4 bits]
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

### Les formats 4 bits natifs : microscaling, NVFP4 vs MXFP4
- Nouveauté de la génération Blackwell : le 4 bits n'est plus une astuce logicielle, c'est un **format matériel** exécuté directement sur les tensor cores. Le mantissa/exposant est le même (E2M1, 4 bits) ; toute la différence est dans le **facteur d'échelle par bloc**.
- **MXFP4** — standard **ouvert** (OCP Microscaling Formats) : blocs de **32** valeurs, échelle contrainte à une **puissance de 2** (8 bits d'exposant). Simple, portable — AMD MI355X l'implémente aussi.
- **NVFP4** — variante NVIDIA : blocs de **16** valeurs (deux fois plus fins) et échelle en **FP8 E4M3** (donc pas seulement une puissance de 2), plus une échelle FP32 par tenseur. Plus de métadonnées, nettement plus de fidélité numérique.
- L'écart n'est pas cosmétique : sur un entraînement 8 Md / 1 T tokens, **MXFP4 demande ~36 % de tokens en plus** pour atteindre la même perte que NVFP4. Un format 4 bits mal conçu se paie en compute d'entraînement, pas en qualité finale. NVFP4 est par ailleurs compatible en lecture avec les checkpoints MXFP4.
- Intuition derrière le gain : la quantization souffre des **valeurs extrêmes** (cf. outliers plus haut). Plus le bloc est petit, moins une valeur aberrante contamine ses voisines ; plus l'échelle est fine (FP8 plutôt que puissance de 2), moins on gaspille de dynamique.

### La bascule 2026 : le 4 bits n'est plus réservé à l'inférence
- Historiquement, le 4 bits servait à **faire tenir** un modèle déjà entraîné. Depuis 2026, il sert aussi à **entraîner** : NVFP4 annonce jusqu'à **1,73×** de débit face à une baseline FP8, à perte négligeable.
- Cela ne rend pas la QAT obsolète — cela déplace la frontière : la précision basse devient le régime d'entraînement par défaut sur matériel récent, avec des maîtres en précision plus haute là où c'est nécessaire (cf. [[Mixed precision]]).
- Corollaire pour un poste de travail : les formats disponibles dépendent maintenant du **GPU**, pas seulement du runtime. FP8 demande du Hopper/Blackwell, NVFP4 du Blackwell. Sur une carte plus ancienne, on reste sur GGUF / AWQ / GPTQ.

## Les maths, simplement

- Quantization : $x_q = \operatorname{round}(x/s) + z$ ; déquantization : $\hat{x} = s\,(x_q - z)$. L'erreur $\hat{x}-x$ est l'**erreur de quantization**.
- Budget mémoire : passer de 16 à $b$ bits divise la taille des poids par $\approx 16/b$ — d'où le rôle clé dans l'[[Inference optimization|optimisation de l'inférence]].
- **Coût réel des métadonnées** : en microscaling, chaque bloc de $B$ valeurs porte une échelle de $e$ bits, soit $b + e/B$ bits effectifs par poids. NVFP4 : $4 + 8/16 = 4{,}5$ bits. MXFP4 : $4 + 8/32 = 4{,}25$ bits. NVFP4 « coûte » donc 6 % de mémoire en plus — et récupère largement la différence en qualité.
- Pourquoi le bloc fin gagne : l'échelle d'un bloc est dictée par son maximum absolu ($s \propto \max|x|$). Une seule valeur extrême écrase la résolution de **tout** son bloc. Réduire $B$ de 32 à 16 réduit le nombre de valeurs « victimes » par outlier — c'est exactement le même raisonnement que les schémas activation-aware, appliqué à la géométrie du découpage.

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
- [[Mixed precision]] — la quantization d'**entraînement** en est le prolongement direct : mêmes questions d'échelle et de maîtres en haute précision, à 4 bits au lieu de 16.
- [[Multi-head Latent Attention]] — levier orthogonal sur le KV-cache : MLA réduit le **nombre** de valeurs à stocker, la quantization le **nombre de bits** par valeur.
- [[Mixture of Experts]] — un MoE économise du calcul mais pas de la VRAM ; la quantization est le complément qui attaque le poste restant.
- [[Dev/Services/vLLM|vLLM]] — serving GPU haut débit avec quantization AWQ/GPTQ/FP8.
- [[Dev/Services/llama.cpp|llama.cpp]] — quantization agressive GGUF/K-quants pour l'inférence locale.

## Pour aller plus loin

- Dettmers et al. (2022) — *LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale*.
- Frantar et al. (2022) — *GPTQ* ; Lin et al. (2023) — *AWQ*.
- Dettmers et al. (2023) — *QLoRA: Efficient Finetuning of Quantized LLMs*.
- OCP — *Microscaling Formats (MX) Specification* (le standard ouvert derrière MXFP4).
- NVIDIA (2025-2026) — *Pretraining LLMs with NVFP4* et le billet Red Hat *Accelerating LLMs with NVFP4 quantization* (blocs de 16, échelle E4M3, comparaison MXFP4).
