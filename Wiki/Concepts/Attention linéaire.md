---
role: notion
nom: Attention linéaire
alias: [linear attention, attention sans softmax, DeltaNet, Gated DeltaNet, GDN, KDA, règle delta, delta rule, mémoire associative, RWKV, Transformers are RNNs]
categorie: concept/dl
domaines: [ml-eng, ai-eng]
tags: [attention, state-space-model, transformers, inference-optimization]
---

# Attention linéaire

## Aperçu

- Retirer le softmax de l'[[Self-attention|attention]] change la **nature** du calcul : au lieu de comparer chaque token à tous les précédents, le modèle entretient un **état de taille fixe** qu'il met à jour token par token. Coût linéaire en longueur de séquence, mémoire constante au décodage.
- Le prix est structurel : cet état est une **compression avec perte** du passé, là où l'attention softmax est une base de données exacte consultable intégralement. D'où la formule qui résume la famille : *efficace mais amnésique*.
- C'est le **cadre unificateur** de tout ce qui concurrence le [[Transformer architectures|Transformer]] sur le coût : Mamba, DeltaNet, RWKV et les [[State Space Models|SSM]] sont la même idée vue depuis des angles différents (automatique, RNN, noyaux).

## Concepts clés

### Le tour de passe-passe algébrique

- L'attention softmax calcule $\text{softmax}(QK^\top)V$. Le softmax **couple** toutes les paires : impossible de factoriser, il faut matérialiser (ou tuiler, cf. [[Flash Attention and efficient attention|FlashAttention]]) une matrice $n \times n$.
- L'attention linéaire remplace le poids $\exp(q_i^\top k_j)$ par un **noyau factorisable** $\varphi(q_i)^\top \varphi(k_j)$. L'associativité du produit matriciel permet alors de calculer $\varphi(K)^\top V$ **d'abord** : une matrice $d \times d$ dont la taille ne dépend **plus** de la longueur de séquence.
- Cette matrice est l'**état**. Elle se met à jour de façon récurrente à chaque token — le Transformer devient un RNN à l'inférence. C'est le résultat fondateur de Katharopoulos et al. (2020), *Transformers are RNNs*.

### L'état comme mémoire associative : lire et écrire

- Vu autrement, l'état $S$ est un **dictionnaire clé → valeur compressé** dans une matrice. Lire, c'est projeter : $S^\top k$ retourne la valeur actuellement associée à la clé $k$. Toute la famille se distingue par sa **règle d'écriture**.
- **Écriture additive** (attention linéaire d'origine) : $S \leftarrow S + v k^\top$. Les associations s'empilent sans jamais s'effacer ; les clés voisines **interfèrent**, l'état sature, et le rappel se dégrade à mesure que le contexte grandit.
- **Règle delta** (DeltaNet) : au lieu d'empiler, **corriger l'erreur**. On calcule ce que l'état répond déjà pour la clé ($S^\top k$), on mesure l'écart avec la valeur voulue, et on ne corrige que cet écart. C'est la règle de Widrow-Hoff — un pas de descente de gradient en ligne. Gain net sur le rappel associatif : l'écriture devient chirurgicale au lieu d'être aveugle.
- **Gating** (Mamba, Gated DeltaNet) : ajouter une **décroissance apprise** $S \leftarrow \alpha S + \dots$ avec $\alpha$ fonction de l'entrée, pour **oublier** activement. Sans oubli, un état fini finit toujours par saturer.
- Le raffinement 2026 : *Gated DeltaNet-2* (NVIDIA, mai 2026) **découple effacement et écriture** — jusque-là un seul paramètre contrôlait les deux, forçant à choisir entre « oublier vite » et « écrire fort ». Côté Kimi, **KDA** (Kimi Delta Attention) remplace la porte scalaire (une valeur par tête) de Gated DeltaNet par un gating **par canal**, dimension par dimension.

### Le paradoxe : bon en moyenne, mauvais sur le détail

- Un état de taille fixe ne peut pas stocker un contexte arbitrairement long sans perte — c'est de l'information théorique, pas un défaut d'implémentation. L'échec est donc **caractéristique**, toujours le même : retrouver un fait précis dans un long contexte (*needle in a haystack*), recopier une longue séquence à l'identique, rappeler une association vue une seule fois.
- Piège d'évaluation : la **perplexité** moyenne reste bonne alors que le rappel s'écroule. Le modèle prédit bien « en général » et rate le détail exact. Les benchmarks de connaissance et de rappel long contexte sont les seuls à révéler l'écart.
- Corollaire industriel : **personne ne livre du 100 % linéaire**. La réponse est de mélanger — cf. [[Architectures hybrides LLM]].

## Les maths, simplement

- Attention causale softmax pour le token $i$ : $o_i = \dfrac{\sum_{j \le i} \exp(q_i^\top k_j)\, v_j}{\sum_{j \le i} \exp(q_i^\top k_j)}$. Chaque nouveau token doit relire **tous** les précédents : coût $\Theta(i)$ par token, cache $\Theta(i)$ qui grandit sans fin.
- Avec un noyau factorisable, la somme se réorganise : $o_i = \varphi(q_i)^\top S_i$ où $S_i = \sum_{j \le i} \varphi(k_j) v_j^\top$, soit la **récurrence** $S_i = S_{i-1} + \varphi(k_i) v_i^\top$. Coût $\Theta(d^2)$ par token — **indépendant de $i$** — et état $\Theta(d^2)$ constant.
- Bilan sur une séquence de longueur $n$ : attention exacte en $\Theta(n^2 d)$ calcul / $\Theta(nd)$ cache ; attention linéaire en $\Theta(n d^2)$ calcul / $\Theta(d^2)$ état. Le croisement se situe vers $n \approx d$ : en dessous, la linéarité ne rapporte rien ; très au-dessus, elle change l'ordre de grandeur.
- Règle delta : $S_i = S_{i-1}\big(I - \beta_i k_i k_i^\top\big) + \beta_i v_i k_i^\top$ — exactement un pas de gradient de taille $\beta_i$ sur $\tfrac{1}{2}\lVert S^\top k_i - v_i \rVert^2$. Le terme $(I - \beta k k^\top)$ **retire** l'ancienne association avant d'écrire la nouvelle : c'est là que naît le gain de rappel.

## En pratique

- Le gain réel se mesure sur le **décodage long**, pas sur le prefill : à 1M de tokens, Kimi Linear affiche un KV-cache réduit d'environ **75 %** et un décodage jusqu'à **~6× plus rapide**. À 4k tokens, l'intérêt est nul.
- Ne pas confondre avec [[Flash Attention and efficient attention|FlashAttention]] : celle-ci garde un résultat **numériquement identique** et n'optimise que les entrées/sorties mémoire. L'attention linéaire **change le mécanisme** — et donc la sortie et les capacités du modèle.
- Le choix se fait à l'**architecture**, pas au déploiement : un modèle à attention softmax ne se convertit pas en linéaire (des travaux de *distillation* existent, mais c'est un réentraînement).
- Côté outillage, les noyaux vivent dans `flash-linear-attention` ; les variantes livrées en production sont Gated DeltaNet (Qwen3-Next), KDA (Kimi Linear), Mamba-2 (Nemotron-3).
- Sur un projet applicatif, ce concept sert surtout à **lire une fiche de modèle** : « hybride 3:1 Gated DeltaNet / attention complète » indique un modèle qui tiendra le long contexte à faible coût mais qu'il faut tester sur le rappel exact avant de l'utiliser pour du RAG à gros contexte.

## Approches voisines & alternatives

- [[State Space Models]] — la même famille dérivée de l'automatique (équation d'état continue discrétisée) plutôt que des noyaux ; Mamba en est le représentant.
- [[Self-attention]] — le mécanisme exact que l'attention linéaire approxime en échangeant le rappel contre le coût.
- [[Flash Attention and efficient attention]] — l'autre voie : garder l'attention exacte et n'optimiser que son exécution (plus MQA/GQA, attention creuse).
- [[Architectures hybrides LLM]] — la réponse industrielle au paradoxe : mélanger couches linéaires et couches d'attention globale.
- [[Multi-head Latent Attention]] — approche opposée sur le même problème : rester en softmax et **compresser le cache** au lieu de le supprimer.
- [[Inference optimization]] — l'état de taille constante supprime la croissance du KV-cache, principal poste mémoire du décodage long.
- [[Positional encoding]] — un état récurrent porte la position **implicitement** (par l'ordre des mises à jour), là où l'attention doit l'injecter explicitement.
- [[Attention Residuals]] — même geste (remplacer un mécanisme figé par de l'attention apprise) mais appliqué à la **profondeur** au lieu de la séquence.

## Pour aller plus loin

- Katharopoulos et al. (2020) — *Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention* (le résultat fondateur).
- Yang et al. (2024) — *Parallelizing Linear Transformers with the Delta Rule over Sequence Length* (DeltaNet entraînable à l'échelle).
- Yang et al. (2024) — *Gated Delta Networks: Improving Mamba2 with Delta Rule* (GDN).
- NVIDIA (2026) — *Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention* (arXiv 2605.22791).
- Kimi Team (2025) — *Kimi Linear: An Expressive, Efficient Attention Architecture* (arXiv 2510.26692, KDA + hybride 3:1).
