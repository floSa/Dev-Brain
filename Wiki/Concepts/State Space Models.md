---
galaxie: wiki
type: concept
nom: State Space Models
alias: [SSM, modèles à espace d'états, Mamba, S4, S5, selective state space, linear-time sequence model]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [state-space-model, deep-learning, inference-optimization]
---

# State Space Models

## Aperçu

- Famille de modèles de séquences qui propagent l'information via un **état latent** évoluant de façon **linéaire** dans le temps, au lieu de comparer tous les tokens entre eux comme l'attention.
- Argument central : **coût linéaire** en longueur de séquence (contre quadratique pour l'attention) et **état de taille constante** à l'inférence — pas de cache KV qui enfle. **Mamba** (SSM sélectif) est l'exemple qui a rendu l'approche compétitive face au [[Transformer architectures|Transformer]].

## Concepts clés

### De l'équation d'état à la récurrence
- Hérité de l'automatique : un état continu $h(t)$ obéit à $h'(t) = A\,h(t) + B\,x(t)$, $y(t) = C\,h(t)$. **Discrétisé**, cela devient une **récurrence linéaire** sur les tokens.
- Deux vues du même modèle : forme **convolutive** (parallélisable, pour l'entraînement) et forme **récurrente** ($O(1)$ par token, pour l'inférence en flux). C'est ce double visage qui fait la force des SSM (S4).

### La sélectivité (Mamba)
- Les SSM linéaires « purs » sont invariants dans le temps → incapables de raisonnement dépendant du contenu. **Mamba** rend $B$, $C$ et le pas de discrétisation **fonction de l'entrée** : le modèle décide quoi retenir ou oublier.
- Cette sélectivité casse la forme convolutive ; elle est récupérée par un **scan parallèle** *hardware-aware* (calcul fusionné en SRAM, esprit proche de [[Flash Attention and efficient attention|Flash Attention]]).

### Le compromis face à l'attention
- Gagne sur les **contextes longs** et le **débit** à séquence longue ; perd (parfois) en **copie exacte / rappel associatif**, là où l'attention excelle. D'où les **hybrides** (couches SSM + quelques couches d'attention).

## Les maths, simplement

- Récurrence discrète : $h_t = \bar{A}\,h_{t-1} + \bar{B}\,x_t$ et $y_t = C\,h_t$, où $\bar{A}, \bar{B}$ sont les versions discrétisées de $A, B$ (via le pas $\Delta$).
- Dépliée, c'est une **convolution** $y = x * \bar{K}$ avec un noyau $\bar{K} = (C\bar{B}, C\bar{A}\bar{B}, C\bar{A}^2\bar{B}, \dots)$ : entraînement parallèle en $O(L\log L)$, inférence récurrente en $O(L)$ avec mémoire $O(1)$.

## En pratique

- Pertinent quand la **longueur de contexte** ou le **débit en streaming** dominent (audio, génomique, longs documents) ; l'écosystème (kernels, outillage, modèles pré-entraînés) reste **moins mûr** que celui des transformeurs.
- Les modèles de prod récents sont souvent **hybrides** : Jamba (Mamba + attention + [[Mixture of Experts|MoE]]), Zamba. Voir aussi RWKV (RNN linéaire d'esprit voisin).
- À l'inférence, l'état constant supprime la croissance du cache KV — un levier d'[[Inference optimization|optimisation de l'inférence]] sur les longues générations.

## Approches voisines & alternatives

- [[Transformer architectures]] — l'architecture dominante que les SSM cherchent à concurrencer sur le coût.
- [[Self-attention]] — mécanisme quadratique opposé : rappel exact fort, mais coût qui explose avec la longueur.
- [[Flash Attention and efficient attention]] — autre voie vers l'attention efficace ; les SSM changent de mécanisme plutôt que d'optimiser l'attention.
- [[Mixture of Experts]] — levier de passage à l'échelle orthogonal, souvent combiné aux SSM dans les hybrides.
- [[Inference optimization]] — l'état de taille constante évite l'enflure du cache KV.
- [[Scaling laws]] — les SSM rejouent la question du compute-optimal sur une autre architecture.

## Pour aller plus loin

- Gu, Goel & Ré (2021) — *Efficiently Modeling Long Sequences with Structured State Spaces* (S4).
- Gu & Dao (2023) — *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*.
- Lieber et al. (2024) — *Jamba* (hybride Mamba + attention + MoE).
