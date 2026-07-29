---
galaxie: wiki
type: concept
nom: Architectures hybrides LLM
alias: [hybrid attention, architecture hybride, hybrid linear attention, ratio 3:1, Kimi Linear, Qwen3-Next, Nemotron-3, Jamba, MiniMax-01, interleaved attention]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [attention, state-space-model, transformers, inference-optimization]
---

# Architectures hybrides LLM

## Aperçu

- Constat de départ : l'[[Attention linéaire|attention linéaire]] est peu coûteuse mais incapable de rappel exact ; l'[[Self-attention|attention softmax]] rappelle parfaitement mais coûte cher en long contexte. Aucune des deux ne gagne seule.
- L'architecture hybride **empile les deux** : la majorité des couches sont linéaires (ou [[State Space Models|SSM]]), et quelques couches d'attention complète sont **intercalées** pour restaurer le rappel exact. Ratio typique **3:1** ou **4:1**.
- C'est le **pattern dominant de 2026** : Qwen3-Next, Kimi Linear, Nemotron-3, MiniMax-01, Jamba. Un modèle 100 % Transformer vanilla est devenu l'exception côté poids ouverts.

## Concepts clés

### Pourquoi mélanger fonctionne

- Le rappel exact d'un fait précis n'a pas besoin d'être disponible à **toutes** les couches : il suffit que **quelques** couches puissent consulter le contexte intégralement. Les autres travaillent sur des représentations déjà enrichies.
- Autrement dit, la capacité de « base de données exacte » se comporte comme une ressource **partageable en profondeur** plutôt que comme une propriété à répliquer partout. C'est le résultat empirique qui rend l'hybride possible.
- Conséquence sur les coûts : la croissance du KV-cache et le coût quadratique ne sont portés que par la **fraction** de couches d'attention complète. À ratio 3:1, cela retire mécaniquement ~75 % du cache.

### Le ratio, et ce qu'il arbitre

- **3:1** (trois couches linéaires pour une couche globale) est le point d'équilibre convergent de Qwen3-Next et Kimi Linear. Monter à 7:1 continue d'économiser mais fait décrocher le rappel ; descendre à 1:1 ramène le coût du Transformer.
- Le ratio n'est **pas** un hyperparamètre de déploiement : il est figé à l'entraînement. En lisant une fiche de modèle, c'est ce chiffre qui prédit son comportement en long contexte.
- Variante de placement : couches globales réparties uniformément, ou concentrées en fin de pile. La littérature 2026 ne tranche pas définitivement ; l'entrelacement régulier domine en pratique.

### Ce que chaque camp apporte concrètement

- **Côté linéaire** : Gated DeltaNet (Qwen3-Next), KDA (Kimi Linear), Mamba-2 (Nemotron-3, Jamba). C'est là que vit le mécanisme d'oubli et d'écriture (gating, règle delta).
- **Côté global** : rarement de la multi-head attention brute — plutôt de la GQA, de la *gated attention*, ou de la [[Multi-head Latent Attention|MLA]] (choix de Kimi Linear). On empile donc **deux** leviers d'économie : moins de couches globales, et des couches globales déjà compressées.
- Certains hybrides ajoutent un troisième axe orthogonal : le [[Mixture of Experts|MoE]] sur les FFN. Nemotron-3 et Jamba cumulent Mamba + attention + MoE ; ce sont trois économies indépendantes (séquence, cache, calcul par token).

### Ce que ça change à l'usage

- Les chiffres publiés parlent de long contexte, pas de moyenne : DeepSeek V4-Pro descend à **27 %** des FLOP d'inférence et **10 %** du KV-cache de V3.2 à 1M de tokens. Kimi Linear affiche jusqu'à **~6×** sur le décodage à 1M.
- À contexte court (quelques milliers de tokens), l'hybride n'apporte presque rien : le régime quadratique n'a pas encore mordu. Tout le bénéfice est dans la queue.

## Les maths, simplement

- Sur $L$ couches dont une fraction $\rho$ en attention complète (ratio 3:1 $\Rightarrow \rho = 1/4$), le KV-cache passe de $\Theta(L \, n \, d)$ à $\Theta(\rho L \, n \, d) + \Theta((1-\rho) L \, d^2)$ : le terme qui croît avec $n$ est **divisé par $1/\rho$**, le reste est constant.
- Coût de calcul de la partie séquence : $\rho L \cdot \Theta(n^2 d) + (1-\rho) L \cdot \Theta(n d^2)$. Le terme quadratique survit — l'hybride ne le supprime pas, il en **réduit le coefficient**. À $n$ suffisamment grand, il redevient dominant.
- Lecture utile : l'hybride repousse le mur du long contexte d'un facteur $1/\rho$, il ne l'abolit pas. Seul un modèle 100 % linéaire serait vraiment sous-quadratique — au prix du rappel.

## En pratique

- Pour choisir un modèle : un hybride est le bon défaut dès que le **contexte dépasse ~32k** et que la charge est du décodage long (agents, résumé de gros documents, sessions longues). En dessous, un dense ou un MoE classique reste plus simple et aussi rapide.
- **Vérifier le rappel avant de bâtir un RAG dessus** : l'hybride est conçu pour préserver le rappel, mais avec un budget réduit. Tester needle-in-a-haystack et rappel multi-hop **sur son propre corpus**, pas se fier au score annoncé.
- Côté serving, le support n'est pas uniforme : [[Dev/Services/vLLM|vLLM]] et [[Dev/Services/SGLang|SGLang]] gèrent les principales familles hybrides, mais chaque nouvelle variante de couche linéaire demande son noyau. Vérifier la version du runtime avant de promettre un débit.
- Le mélange complique la **gestion du cache** : deux types d'état à conserver (KV-cache classique + état récurrent). Le *prefix caching* et la reprise de session ne se comportent pas comme sur un Transformer pur.

## Approches voisines & alternatives

- [[Attention linéaire]] — la moitié « bon marché » de l'hybride, et l'explication du problème qu'il résout.
- [[State Space Models]] — l'autre lignée de couches linéaires utilisée en pratique (Mamba-2, Mamba-3).
- [[Self-attention]] — la moitié « rappel exact », conservée en minorité.
- [[Multi-head Latent Attention]] — souvent le choix retenu pour les couches globales, pour compresser aussi ce qui reste.
- [[Flash Attention and efficient attention]] — les couches globales de l'hybride restent servies par ces noyaux.
- [[Mixture of Experts]] — troisième levier, orthogonal : économise le calcul par token, pas la séquence ni le cache.
- [[Inference optimization]] — l'hybride est un choix d'architecture qui agit sur les mêmes goulots (cache, décodage memory-bound).
- Alternative : rester **100 % attention** et n'optimiser que l'exécution (FlashAttention + GQA + [[Quantization|quantization]]) — plus simple, plafonné plus bas en contexte.

## Pour aller plus loin

- Lieber et al. (2024) — *Jamba* (le premier hybride Mamba + attention + MoE à l'échelle).
- Kimi Team (2025) — *Kimi Linear* (arXiv 2510.26692 — hybride 3:1 KDA / MLA).
- Qwen (2025) — *Qwen3-Next* (hybride 3:1 Gated DeltaNet / gated attention).
- NVIDIA (2025-2026) — *Nemotron 3* (arXiv 2512.20856, 2604.12374 — hybride Mamba-Transformer MoE).
