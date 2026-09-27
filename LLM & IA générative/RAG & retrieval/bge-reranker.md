---
role: brique
nom: bge-reranker
alias: [FlagEmbedding, BGE reranker, bge-reranker-v2-m3, BAAI reranker]
pitch: "Famille de rerankers cross-encoders ouverts du BAAI (FlagEmbedding, MIT ; poids v2 Apache-2.0) — bge-reranker-v2-m3 (0,6 B, multilingue), variantes plus lourdes sur base Gemma ; se charge avec FlagReranker ou CrossEncoder, tourne en local."
categorie: llm/rag
famille: modele
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Cohere Rerank]]", "[[FlashRank]]", "[[Jina Reranker]]"]
complements: ["[[sentence-transformers]]", "[[bge-m3]]", "[[Text Embeddings Inference]]"]
tags: [retrieval, reranking, rag, embeddings]
url_docs: https://bge-model.com
url_repo: https://github.com/FlagOpen/FlagEmbedding
---

# bge-reranker

<!-- AUTO:BANDEAU:START -->
> Famille de rerankers cross-encoders ouverts du BAAI (FlagEmbedding, MIT ; poids v2 Apache-2.0) — bge-reranker-v2-m3 (0,6 B, multilingue), variantes plus lourdes sur base Gemma ; se charge avec FlagReranker ou CrossEncoder, tourne en local.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle Python | open-source | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Les **cross-encoders** du BAAI (Beijing Academy of Artificial Intelligence), publiés avec le
toolkit **FlagEmbedding** — « One-Stop Retrieval Toolkit For Search and RAG », qui porte
aussi les modèles d'embeddings BGE. Un reranker prend la requête et le document **ensemble**
et rend directement un score de pertinence, pas un vecteur : le score brut se normalise par
une sigmoïde pour tomber entre 0 et 1. La famille compte `bge-reranker-base` et `-large`
(chinois et anglais), puis les v2 multilingues : `bge-reranker-v2-m3` (0,6 B, bâti sur
bge-m3), `bge-reranker-v2-gemma` (3 B, base Gemma-2b), `bge-reranker-v2-minicpm-layerwise`
et `bge-reranker-v2.5-gemma2-lightweight`. Le dépôt est sous licence MIT ; les cartes
Hugging Face de `v2-m3` et `v2-gemma` déclarent Apache-2.0. Les cartes des autres variantes
n'ont pas été relues ici.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un reranker **local**, sans donnée qui quitte le réseau : cas nominal d'un déploiement on-prem | Pas de GPU et une latence stricte : `v2-m3` et surtout les variantes Gemma demandent du calcul → [[FlashRank]] sur CPU |
| Corpus **multilingue** : `v2-m3` est le point de départ | Aucune envie d'héberger un modèle → [[Cohere Rerank]], un appel d'API |
| Licence **permissive** (MIT pour le code, Apache-2.0 pour les poids v2 relus) | Le reranker ne corrige pas un top-k qui ne contient pas le bon passage : soigner d'abord [[Hybrid retrieval]] et [[Chunking strategies]] |
| Rester dans l'écosystème [[sentence-transformers]] : le modèle se charge par `CrossEncoder` | Le domaine est très spécialisé : un reranker générique dégrade, un fine-tuning est prévu par le dépôt |

## Mise en œuvre

- Installation — `uv add FlagEmbedding` ; ou rien de plus que [[sentence-transformers]] ou `transformers` pour charger les poids seuls
- Point d'entrée — `FlagReranker('BAAI/bge-reranker-v2-m3', use_fp16=True)` sur des paires (requête, passage) ; la carte donne aussi les usages `transformers` (`AutoModelForSequenceClassification`) et `sentence-transformers`
- Prérequis — les poids, téléchargés depuis le Hub (carte : https://huggingface.co/BAAI/bge-reranker-v2-m3) ; un top-k déjà récupéré (la carte l'évalue sur les 100 premiers résultats d'un premier étage)
- Exécution — local ; GPU recommandé, `use_fp16` pour alléger
- Coût — gratuit ; le coût réel est celui du calcul, par requête et par candidat

## Écosystème

### Alternatives

- [[Cohere Rerank]] — API de reranking managée de Cohere (propriétaire) — reclasse un top-k de documents par pertinence à la requête ; rerank-v4.0 pro et fast, v3.5 multilingue à 4096 tokens de contexte ; déploiement privé (VPC ou on-prem) proposé sur devis.
- [[FlashRank]] — Bibliothèque Python (Apache-2.0) de reranking léger sur CPU — modèles ONNX de 4 Mo (TinyBERT) à 150 Mo, sans Torch ni Transformers ; conçue pour le serverless et les démarrages à froid ; dernière release PyPI 0.2.10 en janvier 2025.
- [[Jina Reranker]] — Rerankers de Jina AI (Elastic) — v3 et v3.5 listwise 0,6 B à 131K tokens de contexte, v2 multilingue cross-encoder, m0 multimodal ; poids CC-BY-NC 4.0 sur HF, usage commercial par l'API, les places de marché cloud ou la licence Jina On-Prem.

### Compléments

- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi. — le runtime : sa classe `CrossEncoder` charge ces poids et les applique au top-k.
- [[bge-m3]] — Modèle d'embedding multilingue du BAAI (MIT, 568 M) — 8 192 tokens, plus de 100 langues, vecteurs dense, sparse et multi-vecteur dans un seul modèle. — le premier étage : `bge-reranker-v2-m3` est bâti sur lui et reclasse le top-k qu'il a récupéré.
- [[Text Embeddings Inference]] — Serveur d'inférence d'embeddings, de rerankers et de classifieurs de Hugging Face (Rust, Apache-2.0) — batching par tokens, images CPU et GPU, API HTTP et gRPC, mode hors-ligne ; v1.9.4 en septembre 2026. — sert les rerankers XLM-R par `/rerank`, derrière une API.

## Ressources

- Documentation — https://bge-model.com
- Dépôt — https://github.com/FlagOpen/FlagEmbedding

## Voir aussi

- [[Reranking]] — la notion qu'il met en œuvre
- [[embeddings]] — le premier étage bi-encoder que ce cross-encoder corrige
- [[Hybrid retrieval]] — l'étage amont qui fournit le top-k
- [[Comparatif - Rerankers]] — ce qui départage les rerankers du dossier
- [[Learning to rank]] — le cadre d'apprentissage dont un cross-encoder est le cas pointwise
