---
role: notion
nom: Flash Attention and efficient attention
alias: [Flash Attention, FlashAttention, attention efficace, multi-query attention, MQA, grouped-query attention, GQA, sparse attention, sliding window attention, attention différentielle, Differential Transformer, DIFF Transformer, bruit d'attention]
categorie: concept/dl
domaines: [ml-eng, mlops, ai-eng]
tags: [attention, inference-optimization, gpu, transformers]
---

# Flash Attention and efficient attention

## Aperçu

- La [[Self-attention|self-attention]] coûte **O(n²)** en calcul et en mémoire sur la longueur de séquence : c'est le goulot des longs contextes. Cette famille de techniques en réduit le coût **sans changer (ou en approximant) la sortie**.
- Deux leviers distincts : rendre l'attention **exacte mais économe** (FlashAttention) ou **changer sa structure** pour casser la quadratique (MQA/GQA, attention creuse).

## Concepts clés

### FlashAttention : exact, IO-aware
- L'attention naïve **matérialise** la matrice n×n des scores en mémoire haute du GPU (HBM), lente. **FlashAttention** (Dao, 2022) la calcule **par tuiles** dans la mémoire rapide (SRAM), avec un softmax en ligne, sans jamais écrire la matrice complète.
- Résultat **numériquement identique**, mais mémoire en **O(n)** au lieu de O(n²) et bien plus rapide car *IO-bound* : on lit moins la HBM. FA-2 et FA-3 poussent l'occupation des cœurs GPU.

### Réduire les têtes Key/Value : MQA / GQA
- **Multi-Query Attention** (MQA) : toutes les têtes partagent **une seule** Key/Value → KV-cache bien plus petit, decode plus rapide.
- **Grouped-Query Attention** (GQA) : compromis — des **groupes** de têtes partagent leurs K/V. Standard des LLM récents (Llama 2/3, Mistral) : presque la qualité du multi-head, le coût du multi-query.

### Casser la quadratique : attention creuse
- **Fenêtre glissante** (Longformer, Mistral) : chaque token n'attend que ses voisins proches → coût linéaire. **Block-sparse**, attention dilatée, et **approximations linéaires** (Performer, [[Attention linéaire|Linear Attention]]) visent le même but avec une perte de qualité variable.

### Nettoyer l'attention plutôt que l'accélérer : attention différentielle
- Problème distinct du coût : le **bruit d'attention**. Sur un long contexte, le softmax distribue une masse de probabilité non négligeable sur des tokens sans rapport ; la vraie information se noie. Mesure parlante : un Transformer standard n'alloue que **3 à 9 %** de son attention au passage contenant la réponse.
- **Différential Transformer** (Microsoft, ICLR 2025) calcule **deux** cartes d'attention softmax indépendantes et **soustrait** la seconde de la première, pondérée par un scalaire appris $\lambda$ : $\text{DiffAttn} = \big(\text{softmax}(Q_1K_1^\top) - \lambda\,\text{softmax}(Q_2K_2^\top)\big)V$.
- Le raisonnement est celui d'un montage différentiel en électronique : le bruit est **corrélé** entre les deux cartes (les deux voient le même contexte parasite), le signal ne l'est pas. La soustraction annule le commun et laisse le pertinent.
- Effets mesurés : attention allouée au passage-réponse portée à **27-40 %**, rapport signal/bruit de 0,31 contre 0,03, et rappel long contexte de **85 % contre 55 %** pour la baseline. Bénéfice secondaire utile : moins de valeurs aberrantes dans les activations, ce qui facilite la [[Quantization|quantization]].
- À noter : cette famille **ne réduit pas** le coût quadratique — elle améliore la **qualité** du rappel à coût comparable. C'est un levier orthogonal aux autres de cette page.

## Les maths, simplement

- Attention exacte : mémoire $O(n^2)$ pour la matrice de scores. **FlashAttention** garde le **même résultat** mais une empreinte mémoire $O(n)$ grâce au softmax en ligne (running max + somme) calculé tuile par tuile.
- KV-cache : taille $\propto n_{\text{heads}}$. MQA fixe $n_{\text{heads}}^{KV} = 1$, GQA le met à $g$ groupes → cache divisé par $n_{\text{heads}}/g$, levier direct de débit à l'[[Inference optimization|inférence]].
- Fenêtre glissante de largeur $w$ : coût $O(n\,w)$ au lieu de $O(n^2)$ — linéaire en $n$ pour $w$ fixe.

## En pratique

- FlashAttention est **activé par défaut** dans [[PyTorch]] (`scaled_dot_product_attention`) et les runtimes de serving — surtout ne pas réécrire le noyau d'attention soi-même.
- GQA se choisit à l'**architecture** du modèle ; pour un modèle existant, c'est déjà fixé. La fenêtre glissante demande de vérifier l'impact sur les dépendances longue portée de la tâche.
- Ces techniques sont au cœur des runtimes : [[vLLM]], [[SGLang]], [[TGI]] — cf. [[Inference optimization]].

## Approches voisines & alternatives

- [[Self-attention]] — le mécanisme exact que ces techniques accélèrent ou approchent.
- [[Inference optimization]] — Flash Attention, MQA/GQA et le KV-cache sont les briques de l'inférence LLM efficace.
- [[Transformer architectures]] — le choix d'attention (multi-head, MQA, GQA, fenêtre) est un paramètre d'architecture.
- [[Multi-head Latent Attention]] — troisième voie sur le KV-cache : compresser le **rang** de l'information au lieu de partager les têtes.
- [[Attention linéaire]] — rupture plus radicale : abandonner le softmax et le cache pour un état de taille fixe.
- [[Architectures hybrides LLM]] — combine les deux mondes ; les couches d'attention globale y restent servies par ces noyaux.
- [[Speculative decoding]] — autre levier d'accélération, orthogonal (plusieurs tokens par passe).

## Pour aller plus loin

- Dao et al. (2022) — *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness* ; Dao (2023) — *FlashAttention-2*.
- Shazeer (2019) — *Multi-Query Attention* ; Ainslie et al. (2023) — *GQA*.
- Beltagy et al. (2020) — *Longformer* (attention à fenêtre glissante).
- Ye et al. (2024-2025, Microsoft) — *Differential Transformer* (arXiv 2410.05258, ICLR 2025 — soustraction de deux cartes softmax, annulation du bruit d'attention).
