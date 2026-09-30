---
role: notion
nom: Choisir un modèle d'embedding
alias: [choix d'un modèle d'embedding, sélectionner un modèle d'embeddings, MTEB, limites de MTEB]
categorie: ml/embeddings
domaines: [data-sci, ai-eng]
tags: [embeddings, semantic-search, retrieval, hybrid-search, benchmark, quantization, self-hosted]
---

# Choisir un modèle d'embedding

## Aperçu

- Choisir un modèle d'[[embeddings]] revient à **fixer des contraintes qui éliminent**, puis à **mesurer sur ses propres documents** ceux qui restent. Les critères qui éliminent se lisent sur une carte de modèle : langues, contexte, dimension, forme des vecteurs, licence, poids. Ce qui classe entre les survivants ne se lit pas dans un classement public.
- Un classement comme MTEB est un point de départ pour constituer une liste courte, pas un verdict : ses mainteneurs reconnaissent que des modèles bien classés peuvent l'être en s'entraînant sur ses tâches (cf. *Limites des benchmarks*). Sur site, le critère de plus est de servir le modèle sans API externe ; les briques du dossier sont [[sentence-transformers]], [[FastEmbed]], [[Text Embeddings Inference]] et [[Infinity]].

## Concepts clés

### Langues et domaine
- Un modèle « multilingue » ne l'est pas également partout. L'article MMTEB (Enevoldsen et al., ICLR 2025 : plus de 500 tâches, plus de 250 langues) rapporte que `multilingual-e5-large-instruct`, à 560 M de paramètres, dépasse `e5-mistral-7b-instruct` et `GritLM-7B` sur MTEB(Multilingual), surtout sur les langues moyennement ou peu dotées : la taille ne fait pas le score.
- Pour le français, MTEB-French (Ciancone et al., 2024 : 15 jeux existants et 3 nouveaux, 51 modèles) conclut qu'aucun modèle n'est meilleur partout. Le guide d'usage du classement français ajoute que ses neuf premiers modèles sont statistiquement équivalents à p = 0,05.
- Un corpus de domaine (juridique, technique, code) et des requêtes dans le jargon de l'entreprise sont ce que les jeux publics couvrent le moins.

### Longueur de contexte
- Les encodeurs plafonnent vers 8 000 tokens ; LongEmbed (Zhu et al., EMNLP 2024) étend à 32 000 **sans réentraînement** par interpolation des positions, et constate que les positions rotatives (RoPE) s'étendent mieux que les positions absolues. ModernBERT (Warner et al., 2024) est natif à 8 192 positions ; ce n'est pas lui un modèle d'embedding, mais une base.
- Dans le brain : [[bge-m3]] à 8 192 tokens, [[Qwen3-Embedding]] à 32K. Un contexte long ne dispense pas de découper : un vecteur unique sur dix pages dilue les passages utiles.

### Dimension et Matryoshka
- La dimension du vecteur fixe le coût de l'index. **Matryoshka Representation Learning** (Kusupati et al., NeurIPS 2022) entraîne le modèle pour que les premières coordonnées suffisent : on tronque sans réentraîner. Dans la documentation de sentence-transformers, un modèle entraîné ainsi garde 98,37 % de sa performance à 8,3 % de la taille, contre 96,46 % pour un modèle standard tronqué — sur un seul jeu, STSBenchmark, donc un exemple, non une garantie.
- [[Qwen3-Embedding]] règle la dimension de 32 jusqu'au maximum ; [[bge-m3]] ne documente pas Matryoshka sur sa carte.
- **La dimension a une limite théorique.** Weller et al. (ICLR 2026) montrent que le nombre de sous-ensembles « top-k » qu'une requête peut isoler est borné par la dimension, et que leur jeu LIMIT met en échec les modèles actuels sur des requêtes simples. Leur conclusion est que le paradigme mono-vecteur a des limites intrinsèques.

### Dense, sparse, multi-vecteur
- **Dense** : un vecteur par texte, comparé au cosinus. Le cas général, compact, sémantique.
- **Sparse** : un poids par terme, appris (SPLADE, Formal et al., SIGIR 2021) ; se pose sur un index inversé, compétitif avec le dense selon l'article, et plus lisible, puisque les termes actifs se voient.
- **Multi-vecteur** (ColBERT, Khattab et Zaharia, SIGIR 2020) : un vecteur par token, comparés par « late interaction ». Les documents se pré-calculent ; l'article annonce une latence cent fois plus basse et dix mille fois moins d'opérations par requête que des rerankers BERT. Le prix est un index beaucoup plus gros.
- BEIR (Thakur et al., 2021) rappelle que BM25 reste une référence robuste et que les modèles denses généralisent moins bien hors de leur domaine : d'où l'intérêt de l'**hybride**. [[bge-m3]] produit les trois formes d'un seul calcul ; [[FastEmbed]] et [[sentence-transformers]] servent aussi le sparse.

### Licence
- La licence du **code** n'est pas celle des **poids**, ni celle des **données**. Lues dans le dossier : [[bge-m3]] en MIT, [[Qwen3-Embedding]] en Apache-2.0.
- Des modèles courants sont restreints : `jina-embeddings-v3` est en CC-BY-NC-4.0 (non commercial), `embeddinggemma-300m` est sous licence Gemma, d'après le registre de [[FastEmbed]]. Vérifier le champ `license` de la carte, **par modèle**, avant tout déploiement.

### Instructions et préfixes
- Beaucoup de modèles exigent un texte d'accompagnement : une instruction côté requête pour [[Qwen3-Embedding]] (gain annoncé de 1 à 5 %), des préfixes `search_query:` et `search_document:` pour Nomic, des préfixes pour E5. L'oublier dégrade la qualité sans aucune erreur.
- Ces réglages sont une source documentée d'écarts : en migrant les scores auto-déclarés vers une vérification centralisée, les mainteneurs de MTEB ont relevé six problèmes de reproductibilité, dont les préfixes E5 et les prompts de tâche Nomic (Chung et al., 2025).

### Coût de serving
- **Mémoire du modèle** : environ deux octets par paramètre en BF16 — [[Qwen3-Embedding]] en 0,6 B tient sur un CPU, le 8 B demande un GPU (estimation tirée du nombre de paramètres, la carte ne donne pas d'exigence).
- **Stockage des vecteurs** : voir *Les maths*. Quantifier les vecteurs (binaire, int8) divise la mémoire par 32 ou par 4 pour une perte modérée sur le cas publié.
- **Outil de service** : en process pour un batch, serveur pour un usage partagé — [[Comparatif - Embeddings]].

## Les maths, simplement

- **Cosinus** entre deux vecteurs $\mathbf{a}, \mathbf{b} \in \mathbb{R}^d$ : $\cos(\mathbf{a},\mathbf{b}) = \dfrac{\mathbf{a}\cdot\mathbf{b}}{\lVert\mathbf{a}\rVert\,\lVert\mathbf{b}\rVert}$. Sur des vecteurs normalisés, c'est le produit scalaire.
- **Matryoshka** : pour des dimensions emboîtées $\mathcal{M} = \{d_1 < d_2 < \dots < d_k = d\}$, la perte est une somme pondérée $\mathcal{L} = \sum_{m \in \mathcal{M}} c_m\, \mathcal{L}_m\!\left(f(x)_{1:m}\right)$ : chaque préfixe du vecteur doit, seul, servir à la tâche. Tronquer est alors légitime, à condition de renormaliser.
- **Taille de l'index** : pour $N$ textes, $N \times d \times b$ octets, avec $b = 4$ en float32, $1$ en int8, et $d/8$ octets par vecteur en binaire. Pour $N = 41 \times 10^6$ et $d = 1\,024$ : environ 168 Go en float32, 42 Go en int8, 5,2 Go en binaire. Le billet de Hugging Face sur la quantification (Shakir, Aarsen, Lee, 2024) mesure 5,2 Go de RAM pour le binaire sur 41 M de textes de Wikipédia ; pour le float32 il donne 200 Go, là où l'arithmétique seule en donne 168.
- **Ce que la quantification coûte**, sur un seul modèle testé (`mxbai-embed-large-v1`) : environ 99,3 % de la performance en int8, environ 96 % en binaire avec une seconde passe de rescoring sur des vecteurs plus précis, environ 92,5 % sans.

## En pratique

- **Éliminer d'abord** : langues du corpus, longueur des documents, licence des poids, poids et GPU disponibles, nécessité d'un sparse ou d'un multi-vecteur. Cela ramène la liste à deux ou trois modèles.
- **Mesurer ensuite, sur ses données** : quelques dizaines de vraies requêtes avec leurs passages pertinents, un rappel@k ou un NDCG@10, le même découpage pour chaque candidat. Le guide du classement français recommande la même démarche avec deux ou trois candidats ; un article de 2026 à auteur unique (Baidya) écrit que le modèle en tête d'un classement est rarement le meilleur choix pour un déploiement donné — résumé lu seulement.
- **Poser les instructions et préfixes dans le code d'indexation et de requête**, et les versionner avec le modèle.
- **Ne jamais mélanger deux modèles** dans un même index : deux espaces incompatibles. Changer de modèle, c'est ré-indexer, donc choisir aussi en fonction du coût d'un calcul complet du corpus.
- **Le choix d'outil est séparé du choix de modèle** : un même modèle se charge en bibliothèque ou se sert par un serveur ; [[Text Embeddings Inference]] ne lit que ses architectures, [[FastEmbed]] que son registre.
- **Un reranker corrige un top-k, pas un premier étage mal choisi** : [[bge-reranker]], [[Reranking]].

### Limites des benchmarks publics
- **Un agrégat.** MTEB classe par un comptage de Borda (MMTEB) ; un écart de quelques dixièmes de point entre modèles de tête n'est pas nécessairement significatif (neuf modèles équivalents en français).
- **Le « zero-shot » est défini par un ratio, non vérifié.** Les mainteneurs le calculent en $1 - n_{\text{entraînement}} / n_{\text{total}}$ sur les tâches du benchmark (exemple cité : `e5-mistral-7b-instruct` à 95 % sur MTEB anglais v2) et écrivent que des modèles bien classés peuvent l'être parce qu'ils s'entraînent sur les tâches du benchmark, alors que des modèles moins bien classés pourraient mieux généraliser. MMTEB reconnaît une fuite possible par des traductions humaines non filtrées, sans analyse chiffrée.
- **Désaccord non tranché.** Dans la discussion publique sur la définition du zero-shot (2025), un commentateur juge le zero-shot invérifiable pour une entreprise et le classement trompeur ; les mainteneurs répondent qu'un filtre strict et un filtre permissif seront proposés, sans retirer de modèle, et que MTEB eng-beta exclut MS MARCO.
- **La robustesse du rang est contestée.** HTEB (Frank et Afli, préimpression, EMNLP 2026) rapporte qu'un modèle passe de la première à la quatrième place après des transformations de requêtes générées par un LLM, avec un tau de Kendall de 0,555 en anglais ; une préimpression très récente, dont seul le résumé a été lu.
- **Auto-déclaré.** Beaucoup de scores viennent des cartes de modèles, et la vérification centralisée a révélé des écarts (préfixes, normalisation, paramètres d'encodage). Les scores de ce brain tirés d'une carte sont signalés « auto-déclarés ».
- **Non trouvé** : une étude d'ampleur qui chiffre la fuite des jeux de test dans l'entraînement des modèles d'embedding, et une étude contrôlée de la corrélation entre MTEB et la performance en production.

## Approches voisines & alternatives

- [[Comparatif - Embeddings]] — ce qui départage les outils et les modèles du dossier.
- [[embeddings]] — la notion de base : ce qu'est un vecteur appris et à quoi il sert.
- [[sentence-transformers]], [[FastEmbed]], [[Text Embeddings Inference]], [[Infinity]] — les outils qui calculent ou servent les embeddings.
- [[bge-m3]], [[Qwen3-Embedding]] — les deux modèles du dossier : multilingue à trois sorties, et famille à contexte long et dimension réglable.
- [[bge-reranker]] — le second étage, cross-encoder, qui reclasse le top-k.
- [[Bases de données vectorielles]] — où s'indexent les vecteurs, et où la dimension se paie.
- **nomic-embed-text** n'a pas de fiche ici : Apache-2.0, anglais seulement en v1.5 (137 M, contexte de 8 192 tokens, Matryoshka), multilingue en v2-moe (contexte de 512), préfixes obligatoires, servi par Ollama ; écarté de la capture par le plafond de pages, non par manque de pertinence.

## Pour aller plus loin

- Muennighoff, Tazi, Magne, Reimers (2022, EACL 2023) — *MTEB: Massive Text Embedding Benchmark* — https://arxiv.org/abs/2210.07316
- Enevoldsen et al. (2025, ICLR 2025) — *MMTEB: Massive Multilingual Text Embedding Benchmark* — https://arxiv.org/abs/2502.13595
- Chung, Kerboua, Kardos, Solomatin, Enevoldsen (2025) — *Maintaining MTEB: Towards Long Term Usability and Reproducibility of Embedding Benchmarks* — https://arxiv.org/abs/2506.21182
- Defining zero-shot for MTEB (discussion GitHub, 2025-01-11) — https://github.com/embeddings-benchmark/mteb/discussions/2351
- Frank, Afli (2026) — *The Harder Text Embedding Benchmark (HTEB): Beyond One-dimensional Static Robustness* — https://arxiv.org/abs/2605.28190 (préimpression, résumé lu)
- Ciancone, Kerboua, Schaeffer, Siblini (2024) — *MTEB-French: Resources for French Sentence Embedding Evaluation and Analysis* — https://arxiv.org/abs/2405.20468
- Ciancone et al. (2024-03-13) — *MTEB Leaderboard: User Guide and Best Practices* — https://huggingface.co/blog/lyon-nlp-group/mteb-leaderboard-best-practices
- Thakur, Reimers, Rücklé, Srivastava, Gurevych (2021) — *BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models* — https://arxiv.org/abs/2104.08663
- Kusupati et al. (2022, NeurIPS 2022) — *Matryoshka Representation Learning* — https://arxiv.org/abs/2205.13147
- sentence-transformers — *Matryoshka Embeddings* — https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html
- Formal, Piwowarski, Clinchant (2021, SIGIR 2021) — *SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking* — https://arxiv.org/abs/2107.05720
- Khattab, Zaharia (2020, SIGIR 2020) — *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT* — https://arxiv.org/abs/2004.12832
- Chen, Xiao, Zhang, Luo, Lian, Liu (2024) — *M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation* — https://arxiv.org/abs/2402.03216
- Zhu et al. (2024, EMNLP 2024) — *LongEmbed: Extending Embedding Models for Long Context Retrieval* — https://arxiv.org/abs/2404.12096
- Warner et al. (2024) — *Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference* (ModernBERT) — https://arxiv.org/abs/2412.13663
- Shakir, Aarsen, Lee (2024-03-22) — *Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval* — https://huggingface.co/blog/embedding-quantization
- Weller, Boratko, Naim, Lee (2026, ICLR 2026) — *On the Theoretical Limitations of Embedding-Based Retrieval* — https://arxiv.org/abs/2508.21038
- Darrin, Formont, Ben Ayed, Cheung, Piantanida (2024) — *When is an Embedding Model More Promising than Another?* — https://arxiv.org/abs/2406.07640
- Baidya (2026) — *Choosing a Text Embedding Model: A Practical Benchmarking and Decision Framework* — https://arxiv.org/abs/2607.23507 (auteur unique, résumé lu)

> Désaccord entre les sources, non tranché : la pertinence du « zero-shot » de MTEB, jugé invérifiable par un contributeur de la discussion GitHub et défendu par les mainteneurs par des filtres à venir. Non vérifié : l'analyse de HTEB et celle de Baidya (résumés seulement) ; la date et les résultats de MTEB v2 (le blog de Hugging Face sur MTEB v2 n'a pas été ouvert).
