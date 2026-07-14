---
galaxie: wiki
type: concept
nom: Transformer architectures
alias: [Transformer, transformeur, architecture transformeur, encoder-decoder, decoder-only, encoder-only]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [transformers, deep-learning, attention, nlp]
---

# Transformer architectures

## Aperçu

- Architecture de réseau de neurones bâtie autour de la [[Self-attention|self-attention]], sans récurrence ni convolution — l'ossature de presque tous les [[Tokenization|LLM]] modernes.
- Sa force : **parallélisme** total à l'entraînement (toute la séquence d'un coup, contrairement aux RNN) et accès direct entre positions distantes.

## Concepts clés

### Le bloc Transformer
- Chaque couche empile deux sous-blocs : **multi-head [[Self-attention|self-attention]]** puis un **réseau feed-forward** (FFN) position par position. Autour de chacun : **connexion résiduelle** + **normalisation de couche** (LayerNorm / RMSNorm).
- *Pre-LN* (normalisation avant le sous-bloc) est devenu le standard : entraînement plus stable en profondeur que le *post-LN* original.

### Trois familles
- **Encoder-only** (BERT) : attention bidirectionnelle, pour comprendre / classer / produire des [[embeddings]].
- **Decoder-only** (GPT, Llama, Mistral) : attention **causale**, génération autorégressive — la famille dominante des LLM.
- **Encoder-decoder** (le Transformer original, T5) : un encodeur lit la source, un décodeur génère en *cross-attention* sur l'encodeur — traduction, résumé.

### Ce qui complète l'attention
- L'attention étant permutation-invariante, il faut un [[Positional encoding|encodage de position]]. Le FFN peut être remplacé par un [[Mixture of Experts|mélange d'experts]] pour grossir le modèle à calcul constant.

## Les maths, simplement

- Une couche : $h' = h + \text{Attn}(\text{Norm}(h))$ puis $h'' = h' + \text{FFN}(\text{Norm}(h'))$ — les **résiduels** ($+ h$) laissent le gradient remonter à travers des dizaines de couches.
- Le FFN est typiquement $\text{FFN}(x) = W_2\,\sigma(W_1 x)$ avec une dimension cachée $\approx 4\times$ celle du modèle ; il porte l'essentiel des paramètres d'une couche.
- Coût dominé par deux termes : l'attention en $O(n^2 d)$ (longueur de séquence) et les FFN en $O(n d^2)$ (largeur du modèle).

## En pratique

- Le choix d'architecture découle de la tâche : génération → **decoder-only** ; embeddings / classification → **encoder-only** ; seq-to-seq strict → encoder-decoder.
- Ne pas partir de zéro : [[Dev/Services/HuggingFace|HuggingFace]] sur [[Dev/Services/PyTorch|PyTorch]] fournit les implémentations de référence ; l'[[PEFT|adaptation paramétriquement efficace]] permet de spécialiser un modèle pré-entraîné.
- La taille utile se raisonne avec les [[Scaling laws|lois d'échelle]] (compute / données / paramètres) ; les [[Small Language Models|petits modèles]] visent le même socle en plus compact.

## Approches voisines & alternatives

- [[Self-attention]] — le sous-bloc central ; le Transformer en est l'assemblage avec FFN, résiduels et normalisation.
- [[Positional encoding]] — fournit l'ordre des tokens, indispensable à l'attention.
- [[Mixture of Experts]] — remplace les FFN denses par des experts conditionnels pour découpler capacité et calcul.
- [[Flash Attention and efficient attention]] — rend l'attention viable sur longs contextes.
- [[Vision Transformers (ViT)]] — applique cette architecture aux images (patchs au lieu de tokens texte), en concurrence des [[CNN]] ; voir aussi [[Vision par ordinateur]].
- [[State Space Models]] — Mamba et alternatives sous-quadratiques au Transformer.

## Pour aller plus loin

- Vaswani et al. (2017) — *Attention Is All You Need* (l'architecture fondatrice).
- Devlin et al. (2018) — *BERT* (encoder-only) · Radford et al. (2018-2019) — *GPT* (decoder-only).
- Xiong et al. (2020) — *On Layer Normalization in the Transformer Architecture* (Pre-LN vs Post-LN).
