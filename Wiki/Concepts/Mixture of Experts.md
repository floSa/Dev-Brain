---
role: notion
nom: Mixture of Experts
alias: [MoE, mélange d'experts, sparse MoE, Switch Transformer, experts conditionnels, top-k routing, fine-grained experts, shared experts, DeepSeekMoE, ratio de sparsité, expert parallelism]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [mixture-of-experts, transformers, deep-learning, scaling-laws]
---

# Mixture of Experts

## Aperçu

- Architecture où le réseau feed-forward dense d'un [[Transformer architectures|Transformer]] est remplacé par **plusieurs experts**, dont un **routeur** n'active qu'une petite fraction par token.
- Idée clé : **découpler le nombre de paramètres du coût de calcul**. Un modèle MoE porte beaucoup de paramètres (capacité) mais n'en utilise que quelques-uns par token (calcul faible).
- Ce n'est plus une option en 2026 : **tout modèle de frontière à poids ouverts est un MoE** (DeepSeek V4, Qwen 3.x, Kimi, GLM, Nemotron). Le dense a reculé vers les petits modèles et l'edge.

## Concepts clés

### Routage et activation creuse

- Un **routeur** (gating) note les experts pour chaque token et n'envoie le token qu'aux **top-k**. Les autres experts restent inactifs : c'est la **sparsité conditionnelle**.
- **Switch Transformer** (top-1) a montré qu'un seul expert par token suffit ; **Mixtral 8×7B** (top-2) a été le premier MoE open-weight grand public.
- Variante **expert-choice** : au lieu que chaque token choisisse ses experts, chaque expert choisit ses tokens. L'équilibrage devient automatique (chaque expert prend sa capacité) mais un token peut n'être traité par personne.

### Le ratio de sparsité, et sa compression

- Le chiffre qui résume un MoE est le **ratio de sparsité** : paramètres actifs / paramètres totaux. C'est lui qui dit ce que coûte le modèle par token, indépendamment de sa taille annoncée.
- La trajectoire 2024 → 2026 est un **effondrement méthodique** de ce ratio : Mixtral ~28 % → DeepSeek V3 ~5,4 % → DeepSeek V4-Pro ~3,1 %. Chaque étape a environ triplé le rapport total/actif **sans perdre** en qualité aval. C'est le levier d'efficience le plus rentable de la période.
- Les modèles de 2026 se situent grosso modo entre **3 % et 35 %** de sparsité. À sparsité égale, c'est la **stratégie de routage** qui décide de l'économie réelle par token — d'où l'importance de la section suivante.

### Le pattern dominant : fine-grained + shared experts

- **Fine-grained** (DeepSeekMoE) : au lieu de $N$ experts de la taille d'un FFN, découper la dimension cachée de chaque expert (par exemple au huitième) et multiplier leur nombre d'autant, à budget de paramètres **constant**. Le nombre d'experts actifs augmente dans le même rapport.
- Pourquoi ça marche : avec de gros experts, le routeur doit faire des choix grossiers et chaque expert apprend un mélange de spécialités. Découpés fin, les experts se **spécialisent** vraiment et les combinaisons possibles explosent — c'est de la combinatoire gagnée gratuitement.
- **Shared experts** : réserver un ou deux experts **toujours actifs**, en plus des experts routés. Ils absorbent la connaissance générale (celle dont tous les tokens ont besoin), ce qui évite que chaque expert routé la réapprenne en double.
- Le couple **fine-grained + shared** est le pattern dominant de 2026 (DeepSeek, Qwen) : spécialisation fine d'un côté, socle stable de l'autre.

### Le problème d'équilibrage

- Sans contrainte, le routeur **se concentre** sur quelques experts (les autres meurent). On ajoute une **perte auxiliaire d'équilibrage** (load balancing) pour répartir les tokens, parfois une **capacité par expert** qui *droppe* le surplus.
- Alternative apparue avec DeepSeek-V3 : l'équilibrage **sans perte auxiliaire**, par ajustement dynamique d'un biais par expert. La perte auxiliaire améliore l'équilibrage mais dégrade légèrement la qualité — la supprimer récupère cette marge.

### Coût caché : la mémoire, puis les stragglers

- Le calcul est faible, mais **tous les experts doivent tenir en mémoire** (VRAM). Un MoE est lourd à héberger malgré son faible FLOP par token → **expert parallelism** : les experts sont répartis sur plusieurs GPU et les tokens voyagent vers eux.
- D'où un second coût, purement systémique : l'**effet straggler**. Comme le routage est déséquilibré à l'échelle d'un lot, le GPU qui a reçu le plus de tokens dicte la latence de tous les autres, qui attendent. C'est un sujet de recherche actif (*capacity-aware inference*, ICLR 2026) et un poste de perte réel en production.
- À retenir : **un MoE économise du calcul, pas de la mémoire**. Un modèle 1000 Md / 32 Md actifs se sert comme un modèle de 1000 Md côté hébergement.

## Les maths, simplement

- Sortie : $y = \sum_{i \in \text{top-}k} g_i(x)\, E_i(x)$ — somme des experts $E_i$ sélectionnés, pondérée par les scores de routage $g_i(x)$ (softmax du gating, renormalisé sur le top-k).
- Découplage capacité / calcul : avec $N$ experts et $k$ actifs, on a $\approx N\times$ les paramètres d'un FFN dense pour seulement $k\times$ son calcul. C'est pourquoi le MoE déplace favorablement les [[Scaling laws|lois d'échelle]] à compute donné.
- Ratio de sparsité $\rho = \frac{\text{params actifs}}{\text{params totaux}}$. Le coût par token suit $\rho$, la capacité suit le total : à budget de calcul fixé, baisser $\rho$ revient à **acheter de la capacité gratuitement** — jusqu'au point où le routeur n'arrive plus à exploiter autant d'experts.
- Découpage fine-grained : passer de $N$ experts (top-$k$) à $mN$ experts $m$ fois plus petits (top-$mk$) laisse paramètres **et** calcul inchangés, mais fait passer le nombre de combinaisons d'experts de $\binom{N}{k}$ à $\binom{mN}{mk}$ — un gain d'expressivité sans coût.

## En pratique

- Un MoE brille quand le **budget mémoire** suit mais le **budget calcul** (entraînement/inférence) est contraint — sinon un modèle dense équivalent est plus simple à servir.
- À l'inférence, le routage rend le **batching** moins prévisible (tokens d'un même lot vers des experts différents) : compter sur un runtime qui gère ([[Dev/Services/vLLM|vLLM]], [[Dev/Services/SGLang|SGLang]]), avec expert parallelism si le modèle ne tient pas sur un GPU.
- Lire une fiche de modèle : deux chiffres suffisent (**total / actif**). Le total dicte la VRAM et donc la facture d'hébergement ; l'actif dicte la vitesse. Un « 1000 Md » à 32 Md actifs n'est pas un petit modèle, c'est un gros modèle rapide.
- Les [[Small Language Models|petits modèles]] denses restent souvent préférables sur l'edge : un MoE économise du calcul, pas de la mémoire.
- Le [[Quantization|quantization]] est le complément naturel : il attaque précisément le poste que le MoE ne réduit pas.

## Approches voisines & alternatives

- [[Transformer architectures]] — le MoE remplace les couches feed-forward denses de l'architecture.
- [[Scaling laws]] — le MoE est un levier pour grimper en paramètres à compute quasi constant.
- [[Calculs adaptatifs]] — la même sparsité conditionnelle appliquée à la **profondeur** (quelles couches) et non à la largeur (quels experts) : Mixture of Depths en est la transposition.
- [[Architectures hybrides LLM]] — troisième levier, orthogonal : le MoE économise le calcul par token, l'hybride économise la séquence et le KV-cache. Souvent cumulés (Nemotron-3, Jamba, Kimi Linear).
- [[Small Language Models]] — approche inverse : compacité par densité plutôt que par sparsité.
- [[Quantization]] — réduit la mémoire que le MoE ne réduit pas ; les deux se combinent systématiquement.
- [[PEFT]] — autre façon de découpler capacité et coût, mais côté **adaptation** (adapters, LoRA) plutôt qu'architecture.
- [[Entraînement distribué]] — l'expert parallelism est un mode de parallélisme à part entière, propre au MoE.

## Pour aller plus loin

- Shazeer et al. (2017) — *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*.
- Fedus et al. (2021) — *Switch Transformers* (routage top-1, équilibrage).
- Jiang et al. (2024) — *Mixtral of Experts* (MoE open-weight top-2).
- Dai et al. (2024) — *DeepSeekMoE* (experts fine-grained + shared, le pattern dominant).
- Cai et al. (2024-2025) — *A Survey on Mixture of Experts in Large Language Models* (TKDE, arXiv 2407.06204).
