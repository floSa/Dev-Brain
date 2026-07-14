---
galaxie: wiki
type: concept
nom: Mixed precision
alias: [Mixed precision, précision mixte, AMP, automatic mixed precision, fp16, bf16, float16, bfloat16, loss scaling, autocast, half precision, demi-précision]
categorie: concept/dl
domaines: [ml-eng]
tags: [mixed-precision, deep-learning, gpu, memory-optimization]
---

# Mixed precision

## Aperçu

- Entraîner en mélangeant **basse précision** (16 bits, fp16 ou bf16) pour la majorité des calculs et **fp32** là où c'est sensible — pour diviser la mémoire et exploiter les **Tensor Cores**, sans dégrader la convergence.
- C'est aujourd'hui le réglage **par défaut** de tout entraînement GPU sérieux : $\approx 2\times$ moins de mémoire d'activations et un débit nettement supérieur, à qualité quasi inchangée.

## Concepts clés

### fp16 vs bf16
- **fp16** : 5 bits d'exposant, 10 de mantisse — bonne précision mais **plage dynamique étroite** ; les petits gradients tombent à zéro (*underflow*).
- **bf16** : 8 bits d'exposant (comme fp32), 7 de mantisse — **même plage** que fp32, moins de précision fine. Plus robuste, sans *loss scaling* ; standard sur GPU récents (Ampere+) et TPU.

### Loss scaling
- Pour fp16, on **multiplie la perte** par un facteur $S$ avant la rétropropagation pour remonter les petits gradients dans la plage représentable, puis on **divise** les gradients par $S$ avant la mise à jour. Le *dynamic loss scaling* ajuste $S$ automatiquement.

### Copie maître fp32
- Les poids sont conservés en **fp32** (la « copie maître ») pour accumuler des mises à jour minuscules ; la version 16 bits ne sert qu'au calcul forward/backward. Sans cela, les updates plus petits que le pas de quantification fp16 seraient perdus.

## Les maths, simplement

- Un float a une **plage** fixée par l'exposant et une **précision** par la mantisse. bf16 sacrifie la mantisse (précision) mais garde l'exposant de fp32 (plage) : $\text{range}(\text{bf16}) \approx \text{range}(\text{fp32})$, d'où la stabilité sans *scaling*.
- Mémoire d'activations divisée par $\approx 2$ (2 octets au lieu de 4) — gain direct combinable avec [[Gradient checkpointing]] et le sharding de l'[[Entraînement distribué]].

## En pratique

- API : un simple `autocast` choisit la précision par opération ; un `GradScaler` gère le *loss scaling* (inutile en bf16).
- Préférer **bf16** dès que le matériel le permet : pas de *loss scaling*, moins de divergences. Réserver **fp16** au matériel plus ancien.
- Distinct de la [[Quantization]] : ici on réduit la précision **à l'entraînement** (16 bits flottants) ; la quantization réduit la précision **à l'inférence** (souvent en entiers 4/8 bits).
- Pièges : normalisations (LayerNorm/softmax) et accumulations à garder en fp32 ; un *NaN* qui apparaît signale souvent un *overflow* fp16 → passer en bf16 ou ajuster le *scaling*.

## Approches voisines & alternatives

- [[Quantization]] — réduction de précision côté **inférence/déploiement** (entiers), pendant de la précision mixte côté entraînement.
- [[Gradient checkpointing]] — autre levier mémoire, cumulable.
- [[Entraînement distribué]] — la précision mixte y est quasi systématique (FSDP/ZeRO en bf16).
- [[Dev/Services/PyTorch|PyTorch]] — `torch.amp` (autocast + GradScaler) en standard.

## Pour aller plus loin

- Micikevicius et al. (2017) — *Mixed Precision Training*.
- Kalamkar et al. (2019) — *A Study of BFLOAT16 for Deep Learning Training*.
