---
role: notion
nom: Multi-head Latent Attention
alias: [MLA, attention latente multi-tête, latent attention, compression du KV-cache, low-rank KV compression, decoupled RoPE]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [attention, inference-optimization, transformers, gpu]
---

# Multi-head Latent Attention

## Aperçu

- Mécanisme d'attention introduit par DeepSeek (V2, 2024) qui **compresse le KV-cache** en projetant clés et valeurs dans un **espace latent de faible dimension**. Seul ce vecteur latent est mis en cache ; les clés et valeurs par tête sont reconstruites à la volée.
- L'angle est différent de l'[[Attention linéaire|attention linéaire]] : MLA **reste** du softmax exact sur tout le contexte. Elle ne renonce pas au rappel, elle réduit ce qu'il faut stocker pour l'obtenir.
- Ordre de grandeur : ~70 Ko/token pour DeepSeek-V3 contre 192-328 Ko/token pour un modèle équivalent en GQA — un facteur **2,7 à 4,7×**.

## Concepts clés

### Le problème : le KV-cache, pas les FLOP

- Au décodage, le goulot d'un LLM n'est pas le calcul mais la **mémoire** : à chaque token généré il faut relire le KV-cache complet. Ce cache croît linéairement avec le contexte **et** avec le nombre de couches.
- Concrètement, il fixe la longueur de contexte maximale et le nombre de requêtes concurrentes qu'un GPU peut porter. C'est lui qui décide du coût par utilisateur, pas la puissance de calcul.
- MQA et GQA (cf. [[Flash Attention and efficient attention]]) attaquent le problème en **réduisant le nombre de têtes K/V** — donc en dégradant la capacité d'expression des têtes. MLA attaque autrement.

### L'idée : cacher un latent, pas des têtes

- Chaque token est projeté (*down-projection*) vers un vecteur latent $c$ de dimension $d_c$ très inférieure à la dimension totale des K/V. **C'est ce latent, et lui seul, qui est mis en cache.**
- Au moment de calculer l'attention, une *up-projection* reconstruit les clés et valeurs de **toutes** les têtes depuis ce latent. Les têtes retrouvent donc leur pleine dimension : la contrainte porte sur le **rang** de l'information, pas sur le nombre de têtes.
- Astuce d'implémentation qui rend l'opération gratuite au décodage : la matrice d'*up-projection* peut être **absorbée** dans les matrices de requête et de sortie. On ne décompresse jamais explicitement — le calcul se fait directement dans l'espace latent.

### Le sous-problème RoPE, et sa solution

- RoPE (cf. [[Positional encoding]]) applique une rotation dépendante de la position **aux clés**. Or l'absorption ci-dessus suppose que la transformation clé est indépendante de la position : les deux sont incompatibles telles quelles.
- Solution retenue : **découpler**. Une partie des dimensions porte l'information compressée sans position, une petite partie dédiée porte les clés « RoPE » mises en cache séparément. Le cache reste petit, la position reste géométriquement cohérente.
- C'est le détail que les résumés omettent, et c'est aussi ce qui rend MLA délicate à greffer sur un modèle existant.

### MLA vs GQA — deux compressions différentes

- GQA compresse le cache en **partageant** les K/V entre têtes : perte de diversité entre têtes, gain proportionnel au nombre de groupes. Simple, universellement supporté.
- MLA compresse en **rang** : chaque tête garde sa propre projection, l'information est goulottée par $d_c$. Plus efficace à qualité donnée d'après les mesures DeepSeek, mais plus intrusive dans l'architecture.
- En 2026, les deux cohabitent : GQA reste le défaut, MLA est le choix des architectures qui poussent le long contexte — y compris comme couche globale d'[[Architectures hybrides LLM|architectures hybrides]] (Kimi Linear).

## Les maths, simplement

- Attention standard : cache par token et par couche $= 2 \, n_{\text{heads}}^{KV} \, d_{\text{head}}$ valeurs (les K et les V). GQA le ramène à $2 g \, d_{\text{head}}$ avec $g$ groupes.
- MLA : cache par token et par couche $= d_c \; (+\, d_r$ pour la partie RoPE découplée$)$, avec $d_c \ll 2 \, n_{\text{heads}} d_{\text{head}}$. Le nombre de têtes **disparaît** de la formule.
- La reconstruction est une factorisation de rang faible : $K \approx C W_K^{\uparrow}$, $V \approx C W_V^{\uparrow}$ où $C$ est la suite des latents. C'est la même intuition que la [[SVD|décomposition en valeurs singulières]] — l'information K/V d'un token vit approximativement dans un sous-espace de dimension $d_c$.
- Absorption : $q^\top K^\top = q^\top (C W_K^{\uparrow})^\top = \big(W_K^{\uparrow} q\big)^\top C^\top$ — on déplace la projection du côté requête, dont il n'y a qu'un exemplaire par pas de décodage, au lieu du côté cache, qui compte $n$ entrées.

## En pratique

- Choix d'**architecture**, pas de déploiement : on ne convertit pas un modèle GQA en MLA sans réentraînement (des travaux de transplantation existent — ACL 2025 — mais restent de la recherche).
- Ce qui compte à l'usage : un modèle MLA tiendra **plus de requêtes concurrentes à contexte égal**, ou un contexte plus long à mémoire égale. C'est directement le coût par utilisateur.
- Le support runtime est bon mais pas universel : [[Dev/Services/vLLM|vLLM]] et [[Dev/Services/SGLang|SGLang]] implémentent MLA avec les optimisations d'absorption ; une implémentation naïve (décompresser puis attention classique) annule tout le bénéfice mémoire.
- Piège de lecture des benchmarks : MLA améliore le **débit agrégé** et la concurrence, pas nécessairement la latence d'un utilisateur seul sur une machine vide.

## Approches voisines & alternatives

- [[Flash Attention and efficient attention]] — MQA/GQA y sont décrites : même objectif (réduire le cache), levier différent (partager les têtes plutôt que compresser le rang).
- [[Self-attention]] — MLA reste exactement ce mécanisme ; seule la représentation stockée change.
- [[Attention linéaire]] — approche opposée : **supprimer** le cache en le remplaçant par un état fixe, au prix du rappel exact.
- [[Architectures hybrides LLM]] — MLA sert souvent de couche d'attention globale dans ces piles.
- [[Positional encoding]] — la compatibilité avec RoPE impose le découplage décrit plus haut.
- [[Inference optimization]] — le KV-cache est le poste que MLA attaque ; à combiner avec paged attention et continuous batching.
- [[SVD]] — le socle mathématique de la compression de rang faible.
- [[Quantization]] — levier orthogonal : quantizer le cache réduit les **bits** par valeur, MLA réduit le **nombre** de valeurs. Cumulables.

## Pour aller plus loin

- DeepSeek-AI (2024) — *DeepSeek-V2* (introduction de MLA, low-rank joint compression + RoPE découplé).
- DeepSeek-AI (2024) — *DeepSeek-V3 Technical Report* (arXiv 2412.19437 — MLA à l'échelle, chiffres de cache).
- Ji et al. (2025) — *Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer* (ACL 2025 — transplantation sur modèles existants).
- Li et al. (2024) — *A Survey on LLM Acceleration based on KV Cache Management* (arXiv 2412.19442 — panorama des familles de compression).
