---
galaxie: wiki
type: concept
nom: Mixture of Experts
alias: [MoE, mélange d'experts, sparse MoE, Switch Transformer, experts conditionnels, top-k routing]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [mixture-of-experts, transformers, deep-learning, scaling-laws]
---

# Mixture of Experts

## Aperçu

- Architecture où le réseau feed-forward dense d'un [[Transformer architectures|Transformer]] est remplacé par **plusieurs experts**, dont un **routeur** n'active qu'une petite fraction par token.
- Idée clé : **découpler le nombre de paramètres du coût de calcul**. Un modèle MoE porte beaucoup de paramètres (capacité) mais n'en utilise que quelques-uns par token (calcul faible).

## Concepts clés

### Routage et activation creuse
- Un **routeur** (gating) note les experts pour chaque token et n'envoie le token qu'aux **top-k** (souvent k=1 ou 2). Les autres experts restent inactifs : c'est la **sparsité conditionnelle**.
- **Switch Transformer** (top-1) a montré qu'un seul expert par token suffit ; **Mixtral 8×7B** (top-2) est l'exemple grand public d'un MoE performant.

### Le problème d'équilibrage
- Sans contrainte, le routeur **se concentre** sur quelques experts (les autres meurent). On ajoute une **perte auxiliaire d'équilibrage** (load balancing) pour répartir les tokens, parfois une **capacité par expert** qui *droppe* le surplus.

### Coût caché : la mémoire
- Le calcul est faible, mais **tous les experts doivent tenir en mémoire** (VRAM). Un MoE est lourd à héberger malgré son faible FLOP par token → souvent **expert parallelism** réparti sur plusieurs GPU.

## Les maths, simplement

- Sortie : $y = \sum_{i \in \text{top-}k} g_i(x)\, E_i(x)$ — somme des experts $E_i$ sélectionnés, pondérée par les scores de routage $g_i(x)$ (softmax du gating, renormalisé sur le top-k).
- Découplage capacité / calcul : avec $N$ experts et $k$ actifs, on a $\approx N\times$ les paramètres d'un FFN dense pour seulement $k\times$ son calcul. C'est pourquoi le MoE déplace favorablement les [[Scaling laws|lois d'échelle]] à compute donné.

## En pratique

- Un MoE brille quand le **budget mémoire** suit mais le **budget calcul** (entraînement/inférence) est contraint — sinon un modèle dense équivalent est plus simple à servir.
- À l'inférence, le routage rend le **batching** moins prévisible (tokens d'un même lot vers des experts différents) : compter sur un runtime qui gère ([[Dev/Services/vLLM|vLLM]], [[Dev/Services/SGLang|SGLang]]).
- Les [[Small Language Models|petits modèles]] denses restent souvent préférables sur l'edge : un MoE économise du calcul, pas de la mémoire.

## Approches voisines & alternatives

- [[Transformer architectures]] — le MoE remplace les couches feed-forward denses de l'architecture.
- [[Scaling laws]] — le MoE est un levier pour grimper en paramètres à compute quasi constant.
- [[Small Language Models]] — approche inverse : compacité par densité plutôt que par sparsité.
- [[PEFT]] — autre façon de découpler capacité et coût, mais côté **adaptation** (adapters, LoRA) plutôt qu'architecture.

## Pour aller plus loin

- Shazeer et al. (2017) — *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*.
- Fedus et al. (2021) — *Switch Transformers* (routage top-1, équilibrage).
- Jiang et al. (2024) — *Mixtral of Experts* (MoE open-weight top-2).
