---
galaxie: wiki
type: concept
nom: Positional encoding
alias: [encodage de position, encodage positionnel, RoPE, rotary embeddings, ALiBi, sinusoidal positional encoding]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [positional-encoding, transformers, attention]
---

# Positional encoding

## Aperçu

- La [[Self-attention|self-attention]] est **permutation-invariante** : sans information ajoutée, « le chat mange » et « mange le chat » lui sont identiques. L'encodage de position **réinjecte l'ordre**.
- Le choix de l'encodage conditionne directement la **longueur de contexte** atteignable et la capacité à extrapoler au-delà de la taille vue à l'entraînement.

## Concepts clés

### Absolu : sinusoïdal vs appris
- **Sinusoïdal** (Transformer original) : on ajoute aux embeddings des ondes sinus/cosinus de fréquences variées — déterministe, sans paramètre, extrapolable en théorie.
- **Appris** (BERT, GPT-2) : un vecteur de position entraîné par index — simple, mais **borné** à la longueur maximale vue à l'entraînement.

### Relatif : RoPE et ALiBi
- **RoPE** (rotary) : fait **tourner** les vecteurs Query/Key d'un angle proportionnel à la position → le produit scalaire d'attention ne dépend que de l'écart relatif entre deux tokens. Standard de fait des LLM récents (Llama, Mistral, Qwen).
- **ALiBi** : ajoute un **biais linéaire** aux scores d'attention, pénalisant les tokens lointains. Pas d'embedding de position du tout, bonne extrapolation.

### Extension de contexte
- À partir de RoPE, on **rallonge le contexte** d'un modèle déjà entraîné par interpolation/ajustement des fréquences : *position interpolation*, *NTK-aware*, **YaRN**. C'est ce qui fait passer un modèle de 4k à 128k tokens.

## Les maths, simplement

- Sinusoïdal : $PE_{(p,\,2i)} = \sin\!\big(p / 10000^{2i/d}\big)$ et $PE_{(p,\,2i+1)} = \cos(\cdot)$ — chaque dimension $i$ oscille à une fréquence propre, donnant une signature unique à chaque position $p$.
- RoPE applique à chaque paire de dimensions une rotation d'angle $p\,\theta_i$ ; alors $\langle R_p q,\, R_k k\rangle$ ne dépend que de $p-k$ → l'attention devient fonction de l'**écart relatif**, ce qui aide l'extrapolation.

## En pratique

- Pour un nouveau modèle decoder-only : **RoPE** est le défaut raisonnable (relatif, extrapolable, bien outillé).
- Avant d'utiliser un modèle sur un contexte plus long que sa fenêtre native, vérifier **comment** il a été étendu (YaRN, interpolation) — au-delà, la qualité s'effondre malgré une fenêtre annoncée.
- Le coût mémoire des longs contextes vient surtout de l'[[Inference optimization|attention et du KV-cache]], pas de l'encodage de position lui-même.

## Approches voisines & alternatives

- [[Self-attention]] — c'est elle que l'encodage de position complète ; les deux sont indissociables dans un [[Transformer architectures|Transformer]].
- [[Transformer architectures]] — l'encodage de position est une brique systématique de l'architecture.
- [[Context engineering]] — la fenêtre de contexte utilisable dépend de l'encodage choisi et de son extension.

## Pour aller plus loin

- Vaswani et al. (2017) — encodage sinusoïdal (Transformer original).
- Su et al. (2021) — *RoFormer* (RoPE) · Press et al. (2022) — *ALiBi*.
- Peng et al. (2023) — *YaRN: Efficient Context Window Extension*.
