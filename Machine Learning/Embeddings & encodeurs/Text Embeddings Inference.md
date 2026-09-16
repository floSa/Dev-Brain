---
role: brique
nom: Text Embeddings Inference
alias: [TEI, text-embeddings-inference, HF TEI]
pitch: "Serveur d'inférence d'embeddings, de rerankers et de classifieurs de Hugging Face (Rust, Apache-2.0) — batching par tokens, images CPU et GPU, API HTTP et gRPC, mode hors-ligne ; v1.9.4 en septembre 2026."
categorie: ml/embeddings
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Rust
scaling: single-node
alternatives: ["[[sentence-transformers]]", "[[Infinity]]", "[[FastEmbed]]"]
complements: ["[[bge-m3]]", "[[Qwen3-Embedding]]", "[[bge-reranker]]"]
tags: [embeddings, model-serving, inference, semantic-search, reranking, self-hosted]
url_docs: https://huggingface.co/docs/text-embeddings-inference
url_repo: https://github.com/huggingface/text-embeddings-inference
---

# Text Embeddings Inference

<!-- AUTO:BANDEAU:START -->
> Serveur d'inférence d'embeddings, de rerankers et de classifieurs de Hugging Face (Rust, Apache-2.0) — batching par tokens, images CPU et GPU, API HTTP et gRPC, mode hors-ligne ; v1.9.4 en septembre 2026.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Rust | open-source | self-hébergé ou managé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Un serveur d'inférence, en Rust, pour les modèles qui **produisent des vecteurs ou des
scores** et non du texte : embeddings, rerankers, classifieurs. Son travail est celui d'un
serveur de modèle : regrouper des requêtes arrivées séparément en un seul passage, en
comptant en **tokens** (`--max-batch-tokens`) plutôt qu'en requêtes, et tokeniser en
parallèle. Il charge les poids depuis le Hub ou depuis un dossier local. La liste des
architectures est fermée : un modèle hors liste n'est pas servi, quelle que soit sa taille.
Il n'entraîne rien et ne quantifie pas. C'est le moteur des Inference Endpoints de Hugging
Face pour les embeddings, et un dépôt actif : v1.9.4 publiée le 2026-09-15, dernier commit le
2026-09-23, environ 5 100 étoiles le 2026-09-30.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un **service partagé** d'embeddings ou de reranking, appelé par plusieurs applications, avec métriques Prometheus et traces OpenTelemetry | Un script ou un batch qui encode un corpus une fois : [[sentence-transformers]] en process suffit, sans service à opérer |
| Les modèles sont de la liste : BERT, XLM-R, Qwen3, Gemma3, ModernBERT, Nomic, GTE, Mistral… | Il faut **ColBERT, ColPali ou CLIP** : absents de la doc → [[Infinity]] |
| Déployer **sans Internet** : poids clonés, volume monté, `--model-id /data/…` | Il faut du **sparse et du multi-vecteur de [[bge-m3]]** : la carte ne documente que le dense côté TEI → FlagEmbedding ou [[sentence-transformers]] |
| Du gRPC, ou une API compatible `/v1/embeddings` pour remplacer un appel à une API externe | Un parc de GPU **antérieurs à Turing** (V100) : non supportés |
| Licence sans ambiguïté : Apache-2.0 | Pas de GPU et pas d'envie de serveur : [[FastEmbed]] sur CPU, en process |

## Mise en œuvre

- Installation — image Docker, par exemple `ghcr.io/huggingface/text-embeddings-inference:cuda-1.9` (GPU) ; des tags CPU existent
- Point d'entrée — serveur : `docker run --gpus all -p 8080:80 -v $PWD/data:/data … --model-id Qwen/Qwen3-Embedding-0.6B`, puis `POST /embed`, `/rerank`, `/predict` ou `/v1/embeddings`
- Prérequis — un modèle d'une architecture supportée, en safetensors ou ONNX ; GPU NVIDIA Turing ou plus récent (Turing et Blackwell marqués expérimentaux dans la doc), ou CPU x86 / ARM64, Metal, ROCm
- Exécution — un processus ; l'échelle se prend par réplicas derrière un répartiteur
- Coût — gratuit, Apache-2.0 ; le calcul est le poste réel

## Limites à connaître

- **Licence en deux temps.** Les versions jusqu'à v1.2.0 étaient sous HFOIL v1.0, une licence restrictive dont le texte n'a pas été relu ici ; le passage à Apache-2.0 date du commit du 2024-04-08 et la v1.2.1 est la première à la porter. Une image ancienne reste sous l'ancienne licence.
- **Pas de quantification** documentée (INT8, INT4), et pas de late-interaction.
- **Des modèles attendus et manquants** dans les issues ouvertes : bge-m3 (ticket #141, ouvert depuis janvier 2024), jina-embeddings-v3 (#418), Qwen3-Reranker (#691).
- **Cadence irrégulière** : sept versions sur douze mois, avec un creux de cinq mois entre v1.8.3 (2025-10-30) et v1.9.0 (2026-02-17).

## Écosystème

### Alternatives

- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi. — la voie en process, sans serveur ni batching dynamique.
- [[Infinity]] — Serveur d'embeddings, de rerankers, de CLIP et de ColPali (MIT, Michael Feil) — API REST de type OpenAI, moteurs PyTorch, ONNX et CTranslate2 ; couverture large mais une seule version en douze mois et un mainteneur unique. — le seul des deux qui sert ColBERT, CLIP et ColPali.
- [[FastEmbed]] — Bibliothèque d'embeddings en process de Qdrant (Apache-2.0) — ONNX Runtime sans PyTorch, dense, sparse, late-interaction et rerankers ; CPU par défaut. — le calcul en bibliothèque, sans service.

### Compléments

- [[bge-m3]] — Modèle d'embedding multilingue du BAAI (MIT, 568 M) — 8 192 tokens, plus de 100 langues, vecteurs dense, sparse et multi-vecteur dans un seul modèle. — servi en dense.
- [[Qwen3-Embedding]] — Famille de modèles d'embedding d'Alibaba (Apache-2.0, 0,6 B, 4 B, 8 B) — 32K tokens, plus de 100 langues, dimension réglable, instructions de tâche. — cité dans l'exemple du README.
- [[bge-reranker]] — Famille de rerankers cross-encoders ouverts du BAAI (FlagEmbedding, MIT ; poids v2 Apache-2.0) — bge-reranker-v2-m3 (0,6 B, multilingue), variantes plus lourdes sur base Gemma ; se charge avec FlagReranker ou CrossEncoder, tourne en local. — le point d'appel `/rerank` sert les rerankers XLM-R.

## Ressources

- Documentation — https://huggingface.co/docs/text-embeddings-inference
- Dépôt — https://github.com/huggingface/text-embeddings-inference
- Documentation — modèles supportés : https://huggingface.co/docs/text-embeddings-inference/supported_models

## Voir aussi

- [[Choisir un modèle d'embedding]] — la notion : quel modèle servir, et ce que les benchmarks ne disent pas
- [[Comparatif - Embeddings]] — ce qui départage les outils et les modèles du dossier
- [[Serving]] — le domaine du serving de modèles, dont ce serveur est le cas spécialisé aux embeddings
