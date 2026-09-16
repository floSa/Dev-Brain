---
role: brique
nom: bge-m3
alias: [BGE-M3, BAAI/bge-m3, M3-Embedding]
pitch: "Modèle d'embedding multilingue du BAAI (MIT, 568 M) — 8 192 tokens, plus de 100 langues, vecteurs dense, sparse et multi-vecteur dans un seul modèle."
categorie: ml/embeddings
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Qwen3-Embedding]]"]
complements: ["[[sentence-transformers]]", "[[Text Embeddings Inference]]", "[[bge-reranker]]"]
tags: [embeddings, semantic-search, retrieval, hybrid-search, transformers]
url_docs: https://huggingface.co/BAAI/bge-m3
url_repo: https://github.com/FlagOpen/FlagEmbedding
---

# bge-m3

<!-- AUTO:BANDEAU:START -->
> Modèle d'embedding multilingue du BAAI (MIT, 568 M) — 8 192 tokens, plus de 100 langues, vecteurs dense, sparse et multi-vecteur dans un seul modèle.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Le modèle d'embedding du BAAI (Beijing Academy of Artificial Intelligence) qui tient trois
promesses dans un seul jeu de poids, d'où le « M3 » de l'article (arXiv 2402.03216) :
**multilingue** (plus de 100 langues), **multi-fonction** (une même passe produit un
vecteur **dense** de 1 024 dimensions, des poids **sparse** lexicaux et des vecteurs
**multi-vecteurs** de type ColBERT) et **multi-granularité** (de la phrase au document de
8 192 tokens). Base XLM-RoBERTa étendue à 8 192 positions, 567 à 568 M de paramètres selon
la source. Aucun préfixe de tâche à poser, et aucune réduction Matryoshka documentée sur la
carte. Les trois sorties ne s'obtiennent pas partout : le dense se charge avec
[[sentence-transformers]], les trois avec le toolkit FlagEmbedding. Publié le 2024-01-27 ;
la carte compte 35,7 millions de téléchargements sur trente jours et 3 747 mentions « j'aime »
le 2026-09-30.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un corpus **multilingue**, français compris, sans choisir un modèle par langue | Le **français seul** ou l'anglais seul, avec un budget mémoire serré : 568 M de paramètres et des poids lourds, pour un besoin qu'un modèle plus petit couvre |
| Des **documents longs**, jusqu'à 8 192 tokens, sans les découper finement | Une **réduction Matryoshka** pour alléger l'index : non documentée sur la carte → [[Qwen3-Embedding]] (dimension réglable) |
| De l'**hybride dense + sparse** (et ColBERT) avec un seul modèle, donc un seul calcul | Servir les trois sorties **par [[Text Embeddings Inference]]** : seul le dense est documenté côté serveur ; le sparse et le multi-vecteur passent par FlagEmbedding |
| Aucun préfixe à gérer : moins d'erreurs à l'indexation | Un **catalogue FastEmbed** : [[FastEmbed]] ne le propose pas dans les registres lus |
| Licence **MIT**, sans accès sur demande | La **licence des données** de fine-tuning compte : la carte publie le jeu (`Shitao/bge-m3-data`) sans en dire la licence |

## Mise en œuvre

- Installation — `uv add sentence-transformers` pour le dense ; `uv add FlagEmbedding` pour les trois sorties (`BGEM3FlagModel`)
- Point d'entrée — `SentenceTransformer("BAAI/bge-m3")` ; ou `BGEM3FlagModel("BAAI/bge-m3", use_fp16=True)`
- Prérequis — les poids, depuis le Hub (https://huggingface.co/BAAI/bge-m3) ; environ 13,7 Go de fichiers sur le Hub, pytorch et onnx confondus ; GPU recommandé, `use_fp16` allège au prix d'une légère dégradation annoncée
- Exécution — local, sans appel externe après le téléchargement ; Ollama et un GGUF communautaire existent, en dense seulement d'après ce qui a été lu
- Coût — gratuit, MIT ; le coût réel est celui du calcul

## Limites à connaître

- **Aucun score MTEB sur la carte** : les performances MIRACL, MKQA et MLDR n'y sont que des graphiques. Les seuls chiffres lus en texte viennent du tableau d'un concurrent, donc pas du BAAI : BEIR 48,8 et MIRACL 69,2 (carte de nomic-embed-text-v2-moe).
- **BM25 reste compétitif** sur certains documents longs, et le sparse est plus faible que le dense sans fine-tuning, selon la carte.
- **Ollama et GGUF** : le sparse et le multi-vecteur ne sont pas documentés dans ces formats.

## Écosystème

### Alternatives

- [[Qwen3-Embedding]] — Famille de modèles d'embedding d'Alibaba (Apache-2.0, 0,6 B, 4 B, 8 B) — 32K tokens, plus de 100 langues, dimension réglable, instructions de tâche. — l'autre grand modèle multilingue ouvert, à contexte plus long et à dimension réglable ; dense seulement.

### Compléments

- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi. — charge le modèle pour le dense.
- [[Text Embeddings Inference]] — Serveur d'inférence d'embeddings, de rerankers et de classifieurs de Hugging Face (Rust, Apache-2.0) — batching par tokens, images CPU et GPU, API HTTP et gRPC, mode hors-ligne ; v1.9.4 en septembre 2026. — le sert en dense, derrière une API.
- [[bge-reranker]] — Famille de rerankers cross-encoders ouverts du BAAI (FlagEmbedding, MIT ; poids v2 Apache-2.0) — bge-reranker-v2-m3 (0,6 B, multilingue), variantes plus lourdes sur base Gemma ; se charge avec FlagReranker ou CrossEncoder, tourne en local. — `bge-reranker-v2-m3` est bâti sur ce modèle : le reclassement du top-k qu'il a récupéré.

## Ressources

- Documentation — carte du modèle : https://huggingface.co/BAAI/bge-m3
- Dépôt — le toolkit FlagEmbedding : https://github.com/FlagOpen/FlagEmbedding
- Article — *M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation* (Chen et al., 2024) — https://arxiv.org/abs/2402.03216

## Voir aussi

- [[Choisir un modèle d'embedding]] — la notion : dense, sparse et multi-vecteur, et ce que les benchmarks ne disent pas
- [[Comparatif - Embeddings]] — ce qui départage les outils et les modèles du dossier
