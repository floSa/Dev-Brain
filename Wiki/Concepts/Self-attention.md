---
galaxie: wiki
type: concept
nom: Self-attention
alias: [auto-attention, scaled dot-product attention, multi-head attention, MHA, attention QKV, cross-attention]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [attention, transformers, deep-learning]
---

# Self-attention

## Aperçu

- Mécanisme qui laisse **chaque token regarder tous les autres** et agréger leur information selon une pertinence apprise — le cœur de calcul du [[Transformer architectures|Transformer]].
- Remplace la récurrence (RNN) par une opération **entièrement parallèle** où toute paire de positions interagit directement, quelle que soit la distance.

## Concepts clés

### Query, Key, Value
- Chaque token est projeté en trois vecteurs : **Query** (ce que je cherche), **Key** (ce que je propose), **Value** (ce que je transmets). Le score d'attention entre deux tokens est le produit scalaire Query·Key ; il pondère ensuite les Values.
- *Self*-attention : Q, K et V viennent de la **même** séquence. *Cross*-attention : les Query viennent d'une séquence, les Key/Value d'une autre (décodeur qui regarde l'encodeur).

### Multi-head
- Plutôt qu'une seule attention, on en fait **h en parallèle** dans des sous-espaces projetés différents, puis on concatène. Chaque tête peut se spécialiser (syntaxe, coréférence, position…). C'est le *multi-head attention* (MHA).

### Masquage causal
- Dans un modèle autorégressif (décodeur, [[Tokenization|génération]] token par token), un **masque** empêche une position de regarder le futur → l'attention ne voit que le passé. C'est ce qui rend le [[Transformer architectures|Transformer]] *decoder-only* causal.

### Le coût quadratique
- Toutes les paires de tokens interagissent → calcul et mémoire en **O(n²)** sur la longueur de séquence. C'est le mur des longs contextes, qu'attaquent [[Flash Attention and efficient attention|Flash Attention et l'attention efficace]].

## Les maths, simplement

- $\text{Attention}(Q,K,V) = \text{softmax}\!\left(\dfrac{QK^\top}{\sqrt{d_k}}\right)V$ : les scores $QK^\top$ sont normalisés par $\sqrt{d_k}$ (sinon les produits scalaires explosent en grande dimension et saturent le softmax), transformés en poids qui somment à 1, puis appliqués aux Values.
- $Q = XW_Q,\; K = XW_K,\; V = XW_V$ : les trois projections sont **apprises** ($X$ = embeddings des tokens en entrée). Multi-head = $h$ jeux de $(W_Q, W_K, W_V)$ indépendants.
- Mémoire de la matrice de scores : $O(n^2)$ pour $n$ tokens — d'où le coût des longs contextes.

## En pratique

- L'attention seule est **permutation-invariante** : sans [[Positional encoding|encodage de position]], elle ne sait pas l'ordre des tokens. Les deux vont toujours ensemble.
- Ne jamais réimplémenter le noyau naïf : les frameworks ([[Dev/Services/PyTorch|PyTorch]] `scaled_dot_product_attention`, [[Dev/Services/HuggingFace|HuggingFace]]) appellent un noyau fusionné type [[Flash Attention and efficient attention|FlashAttention]].
- Le KV-cache de l'[[Inference optimization|inférence]] mémorise précisément les Key/Value des tokens passés pour ne pas les recalculer à chaque pas.

## Approches voisines & alternatives

- [[Transformer architectures]] — l'architecture qui empile self-attention + réseau feed-forward ; la self-attention en est le sous-bloc central.
- [[Positional encoding]] — fournit l'information d'ordre que l'attention, à elle seule, ignore.
- [[Flash Attention and efficient attention]] — mêmes maths, mais calcul économe en mémoire et variantes sous-quadratiques (MQA, GQA, fenêtre glissante).
- [[Inference optimization]] — le KV-cache et le batching s'appuient directement sur la structure de l'attention.

## Pour aller plus loin

- Vaswani et al. (2017) — *Attention Is All You Need* (scaled dot-product, multi-head).
- Bahdanau et al. (2015) — *Neural Machine Translation by Jointly Learning to Align and Translate* (l'attention avant le Transformer).
