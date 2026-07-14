---
galaxie: dev
type: service
nom: sentence-transformers
alias: [sbert, sentence transformers, sentence-bert]
pitch: "Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [embeddings, semantic-search, retrieval, reranking, nlp]
url_docs: https://www.sbert.net
url_repo: https://github.com/huggingface/sentence-transformers
---

# sentence-transformers

## Pourquoi

Framework de référence pour produire des **embeddings de phrases** (SBERT). Charge des centaines de modèles pré-entraînés et encode du texte (ou des images) en vecteurs denses comparables au cosinus, en quelques lignes. Fournit aussi les **cross-encoders** pour le [[Reranking|re-ranking]]. Maintenu par Hugging Face.

## Quand l'utiliser

- Produire des [[embeddings]] de phrases/documents pour recherche sémantique, [[RAG]], clustering, déduplication.
- Étage **dense** d'un pipeline de [[Recherche d'information]].
- [[Reranking]] avec un cross-encoder (BGE-reranker, mxbai…).
- Fine-tuner un encodeur sur son domaine (perte contrastive, MultipleNegativesRankingLoss).

## Quand NE PAS l'utiliser

- Recherche purement **lexicale** sur mots exacts → [[Dev/Services/rank-bm25|rank-bm25]] ou un moteur ([[Dev/Services/Elasticsearch|Elasticsearch]]).
- Génération de texte : c'est de l'encodage, pas un LLM génératif.
- Embeddings **managés** via API → fournisseurs cloud (OpenAI, Cohere, Voyage).

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add sentence-transformers`.
- **Single-node** ; GPU recommandé pour encoder du volume, CPU possible sur petits jeux.
- S'appuie sur [[Dev/Services/HuggingFace|HuggingFace]] / [[Dev/Services/PyTorch|PyTorch]] ; modèles tirés du Hub.

## Pièges

- **Normaliser** les vecteurs (cosinus) et utiliser le **même modèle** pour indexer et requêter — espaces incompatibles sinon.
- Choisir un modèle adapté à la **langue** et au domaine (multilingue vs anglais).
- Cross-encoder ≠ bi-encoder : le premier ne se pré-calcule pas → réservé au top-k ([[Reranking]]).

## Alternatives

Pas de substitut direct dans le brain : c'est la voie open-source de référence pour les embeddings locaux. Les embeddings **managés** (API OpenAI, Cohere, Voyage) sont une alternative d'infrastructure, hors brain.

## Liens

- [[embeddings]] — ce qu'il produit.
- [[Recherche d'information]] · [[Reranking]] · [[RAG]] — ses usages.
- [[Dev/Services/HuggingFace|HuggingFace]] — socle modèles / Hub.
- [[Dev/Services/SetFit|SetFit]] — few-shot classification bâti dessus.
- [[Dev/Patterns/Comparatif - NLP|Comparatif — NLP]]
- Doc : https://www.sbert.net
