---
role: brique
nom: FastEmbed
alias: [fastembed, Qdrant FastEmbed, fastembed-gpu]
pitch: "Bibliothèque d'embeddings en process de Qdrant (Apache-2.0) — ONNX Runtime sans PyTorch, dense, sparse, late-interaction et rerankers ; CPU par défaut."
categorie: ml/embeddings
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[sentence-transformers]]", "[[Text Embeddings Inference]]", "[[Infinity]]"]
complements: ["[[Qdrant]]"]
tags: [embeddings, inference, semantic-search, reranking, hybrid-search]
url_docs: https://qdrant.github.io/fastembed/
url_repo: https://github.com/qdrant/fastembed
---

# FastEmbed

<!-- AUTO:BANDEAU:START -->
> Bibliothèque d'embeddings en process de Qdrant (Apache-2.0) — ONNX Runtime sans PyTorch, dense, sparse, late-interaction et rerankers ; CPU par défaut.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Une bibliothèque Python de Qdrant qui calcule des embeddings **sans PyTorch** : les modèles
sont des conversions ONNX, exécutées par ONNX Runtime, sur CPU par défaut ; le paquet
séparé `fastembed-gpu` ajoute CUDA. `TextEmbedding(...).embed(...)` rend un générateur de
vecteurs. Au-delà du dense, le même paquet sert des vecteurs creux (SPLADE++, BM25, BM42,
miniCOIL), de la late-interaction (ColBERT, answerai-colbert), des images (CLIP), ColPali
pour les documents images et des rerankers. Le catalogue est borné : ce sont les modèles
que Qdrant a convertis, pas le Hub entier, et **BGE-M3 n'y figure pas** dans les registres
lus. La bibliothèque n'entraîne ni ne distille rien. Version 0.8.1 le 2026-09-22, environ
3 200 étoiles et 4,8 millions de téléchargements PyPI sur trente jours, constatés le
2026-09-30.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des embeddings sur **CPU, sans PyTorch** : image légère, démarrage court | Un modèle **hors catalogue** : le registre est fermé → [[sentence-transformers]], qui charge le Hub |
| Du **sparse** ou du **ColBERT** dans la même API que le dense | [[bge-m3]] avec ses trois sorties → FlagEmbedding ou [[sentence-transformers]] |
| Déjà sur [[Qdrant]], dont c'est la pile d'embeddings native (`qdrant-client[fastembed]`) | Un **service partagé** à opérer → [[Text Embeddings Inference]] ou [[Infinity]] |
| Du code permissif : Apache-2.0 | Une **licence de modèle** qui compte : certains modèles embarqués sont sous CC-BY-NC ou sous licence Gemma (voir *Limites*) |
| Un cache de modèles qui peut se figer pour le hors-ligne | Un cache non volatil sans configuration : le cache par défaut est un dossier temporaire |

## Mise en œuvre

- Installation — `uv add fastembed` ; `uv add fastembed-gpu` pour CUDA 12
- Point d'entrée — import Python : `from fastembed import TextEmbedding`, puis `.embed(documents)`
- Prérequis — Python ≥ 3.10 ; dépendances légères (ONNX Runtime, `tokenizers`, `huggingface-hub`, `numpy`, `pillow`) ; **fixer `cache_dir` ou `FASTEMBED_CACHE_PATH`**, puis `local_files_only=True` pour n'appeler aucun serveur après le premier téléchargement
- Exécution — en bibliothèque, rien à héberger ; CPU, GPU avec le paquet dédié
- Coût — gratuit, Apache-2.0 pour le code

## Limites à connaître

- **Licences de modèles disparates.** Le code est Apache-2.0, mais chaque entrée du registre déclare la sienne. La plupart sont en MIT ou Apache-2.0 (BGE, GTE, nomic, multilingual-e5-large, Qwen3-Embedding-0.6B, potion, colbertv2). **Non commerciales** (CC-BY-NC-4.0) : `jina-embeddings-v3`, `jina-colbert-v2` et `jina-reranker-v2-base-multilingual`. **Licence Gemma** (conditions Google) : `embeddinggemma-300m` et `colpali-v1.3-fp16`. Le modèle par défaut, `BAAI/bge-small-en-v1.5`, est en MIT. Filtrer modèle par modèle.
- **Aucun chiffre de performance** publié : le README dit « fast » sans mesure ni méthode, et la documentation Qdrant n'en donne pas non plus.
- **Conversions, pas poids d'origine** : un écart numérique avec le modèle source est possible ; il n'a pas été mesuré ici.

## Écosystème

### Alternatives

- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi. — le généraliste sur PyTorch : tout le Hub, l'entraînement, des dépendances plus lourdes.
- [[Text Embeddings Inference]] — Serveur d'inférence d'embeddings, de rerankers et de classifieurs de Hugging Face (Rust, Apache-2.0) — batching par tokens, images CPU et GPU, API HTTP et gRPC, mode hors-ligne ; v1.9.4 en septembre 2026. — le service partagé, quand la bibliothèque en process ne suffit plus.
- [[Infinity]] — Serveur d'embeddings, de rerankers, de CLIP et de ColPali (MIT, Michael Feil) — API REST de type OpenAI, moteurs PyTorch, ONNX et CTranslate2 ; couverture large mais une seule version en douze mois et un mainteneur unique. — le service qui couvre aussi CLIP et ColPali.

### Compléments

- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple. — son éditeur ; l'intégration `qdrant-client[fastembed]` calcule les vecteurs à l'insertion.

## Ressources

- Documentation — https://qdrant.github.io/fastembed/
- Dépôt — https://github.com/qdrant/fastembed

## Voir aussi

- [[Choisir un modèle d'embedding]] — la notion : quel modèle charger, et ce que les benchmarks ne disent pas
- [[Comparatif - Embeddings]] — ce qui départage les outils et les modèles du dossier
