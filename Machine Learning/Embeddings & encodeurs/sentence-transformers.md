---
role: brique
nom: sentence-transformers
alias: [sbert, sentence transformers, sentence-bert]
pitch: "Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi."
categorie: ml/embeddings
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[FastEmbed]]", "[[Text Embeddings Inference]]", "[[Infinity]]"]
complements: ["[[HuggingFace]]", "[[SetFit]]", "[[txtai]]", "[[bge-reranker]]", "[[Jina Reranker]]", "[[bge-m3]]", "[[Qwen3-Embedding]]"]
tags: [embeddings, semantic-search, retrieval, reranking, nlp]
url_docs: https://www.sbert.net
url_repo: https://github.com/huggingface/sentence-transformers
---

# sentence-transformers

<!-- AUTO:BANDEAU:START -->
> Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Le framework de référence pour produire des **embeddings de phrases** (SBERT). Il charge
des centaines de modèles pré-entraînés et encode du texte — depuis la 5.4, aussi des images,
de l'audio et de la vidéo — en vecteurs comparables, en quelques lignes. Il fournit quatre
familles qui ne se substituent pas : les **bi-encoders**, dont les vecteurs denses se
pré-calculent et s'indexent ; les **sparse encoders** (SPLADE, depuis la 5.0), dont les
vecteurs creux se posent sur un index inversé ; les **encodeurs multi-vecteurs** (ColBERT,
late interaction, depuis la 6.0) ; et les **cross-encoders**, qui notent une paire
requête-document sans rien pouvoir pré-calculer, et ne servent donc que sur le top-k d'un
[[Reranking|re-ranking]]. Il entraîne aussi (un `Trainer`, des pertes contrastives et
Matryoshka) et offre des backends ONNX et OpenVINO. Deux contraintes commandent l'usage :
normaliser les vecteurs, et indexer puis requêter avec le **même modèle** — deux modèles
donnent deux espaces incompatibles. Maintenu par Hugging Face ; dernière version stable 6.1.0
le 2026-09-18, environ 19 100 étoiles et 22,7 millions de téléchargements PyPI sur trente
jours, relevés le 2026-09-30.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Produire des [[embeddings]] de phrases ou de documents : recherche sémantique, [[RAG]], clustering, déduplication | Recherche purement **lexicale** sur mots exacts → [[rank-bm25]], ou un moteur comme [[Elasticsearch]] |
| Étage **dense** d'un pipeline de [[Recherche d'information]] | Un **cross-encoder ne se pré-calcule pas** : le réserver au top-k, jamais à l'indexation |
| Charger **n'importe quel modèle du Hub** : [[bge-m3]], [[Qwen3-Embedding]], et la plupart des autres | Un **service partagé** qui sert beaucoup d'appels concurrents → [[Text Embeddings Inference]] ou [[Infinity]], avec batching dynamique |
| [[Reranking]] avec un cross-encoder — [[bge-reranker]], [[Jina Reranker]] (v2), mxbai | Des embeddings sur **CPU, sans PyTorch**, image légère → [[FastEmbed]] |
| Fine-tuner un encodeur sur son domaine, par perte contrastive (`MultipleNegativesRankingLoss`) | Le modèle doit être **adapté à la langue et au domaine** : un multilingue générique dégrade sur un corpus spécialisé |
| | Embeddings **managés** par API : c'est une alternative d'infrastructure hors brain — OpenAI, Cohere, Voyage |
| | Génération de texte : c'est de l'encodage, pas un LLM génératif |

## Mise en œuvre

- Installation — `uv add sentence-transformers`
- Point d'entrée — API Python : `SentenceTransformer(...).encode(...)` pour les bi-encoders, `CrossEncoder` pour le re-ranking
- Prérequis — Python ≥ 3.10, PyTorch ≥ 2.2 et transformers ≥ 5.0 (obligatoire depuis la 6.0.0, qui a aussi rendu `similarity` une méthode et exige `trust_remote_code=True` pour les modules custom) ; un modèle du Hub adapté à la langue et au domaine, le même de bout en bout
- Exécution — single-node ; GPU recommandé pour encoder du volume, CPU possible sur petits jeux et petits modèles (backends ONNX et OpenVINO, embeddings statiques)
- Coût — gratuit, Apache-2.0, rien à héberger

## Écosystème

### Alternatives

- [[FastEmbed]] — Bibliothèque d'embeddings en process de Qdrant (Apache-2.0) — ONNX Runtime sans PyTorch, dense, sparse, late-interaction et rerankers ; CPU par défaut. — la voie légère, sur un catalogue de modèles converti et fermé.
- [[Text Embeddings Inference]] — Serveur d'inférence d'embeddings, de rerankers et de classifieurs de Hugging Face (Rust, Apache-2.0) — batching par tokens, images CPU et GPU, API HTTP et gRPC, mode hors-ligne ; v1.9.4 en septembre 2026. — le service partagé : la même tâche, derrière une API.
- [[Infinity]] — Serveur d'embeddings, de rerankers, de CLIP et de ColPali (MIT, Michael Feil) — API REST de type OpenAI, moteurs PyTorch, ONNX et CTranslate2 ; couverture large mais une seule version en douze mois et un mainteneur unique. — le service qui couvre aussi CLIP et ColPali.
- Embeddings managés par API — OpenAI, Cohere, Voyage : une alternative d'infrastructure, pas de bibliothèque (pas en fiche, et hors du critère on-prem).

### Compléments

- [[HuggingFace]] — Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes — le socle de modèles et le Hub d'où viennent les encodeurs.
- [[SetFit]] — Few-shot text classification sans prompt — fine-tuning contrastif d'un sentence-transformer puis tête de classification ; performant avec quelques dizaines d'exemples, sans LLM — bâti dessus, pour la classification few-shot.
- [[txtai]] — Base d'embeddings tout-en-un en Python (Apache-2.0, NeuML) — recherche sémantique, SQL et graphe sur un même index, plus orchestration de workflows LLM ; du notebook embarqué à l'API FastAPI. — l'index et les workflows qui se montent au-dessus des embeddings produits
- [[bge-reranker]] — Famille de rerankers cross-encoders ouverts du BAAI (FlagEmbedding, MIT ; poids v2 Apache-2.0) — bge-reranker-v2-m3 (0,6 B, multilingue), variantes plus lourdes sur base Gemma ; se charge avec FlagReranker ou CrossEncoder, tourne en local. — les poids que `CrossEncoder` charge pour reclasser un top-k.
- [[Jina Reranker]] — Rerankers de Jina AI (Elastic) — v3 et v3.5 listwise 0,6 B à 131K tokens de contexte, v2 multilingue cross-encoder, m0 multimodal ; poids CC-BY-NC 4.0 sur HF, usage commercial par l'API, les places de marché cloud ou la licence Jina On-Prem. — la v2 se charge par `CrossEncoder` ; poids non commerciaux sans licence.

- [[bge-m3]] — Modèle d'embedding multilingue du BAAI (MIT, 568 M) — 8 192 tokens, plus de 100 langues, vecteurs dense, sparse et multi-vecteur dans un seul modèle. — se charge par `SentenceTransformer` pour le dense.
- [[Qwen3-Embedding]] — Famille de modèles d'embedding d'Alibaba (Apache-2.0, 0,6 B, 4 B, 8 B) — 32K tokens, plus de 100 langues, dimension réglable, instructions de tâche. — déclare `sentence-transformers` comme bibliothèque sur le Hub.

## Ressources

- Documentation — https://www.sbert.net
- Dépôt — https://github.com/huggingface/sentence-transformers

## Voir aussi

- [[embeddings]] — la notion : ce qu'il produit
- [[Choisir un modèle d'embedding]] — la notion sœur : quel modèle charger, et ce que les benchmarks ne disent pas
- [[Comparatif - Embeddings]] — ce qui départage les outils et les modèles du dossier
- [[Recherche d'information]] · [[Reranking]] · [[RAG]] — ses usages
- [[PyTorch]] — le framework de calcul sous-jacent
- [[Comparatif - NLP]] — ce qui départage les outils de la chaîne texte
