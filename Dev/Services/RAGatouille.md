---
galaxie: dev
type: service
nom: RAGatouille
alias: [ragatouille]
pitch: "Bibliothèque (AnswerDotAI) qui rend les modèles de late-interaction ColBERT simples à entraîner et à utiliser dans un pipeline RAG — indexation PLAID, recherche et reranking par-dessus colbert-ai ; maintenance ralentie (0.0.9, février 2025)."
categorie: llm/framework
licence_type: open-source
hosted: self
maturite: beta
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [retrieval, reranking, rag, nlp]
url_docs: https://github.com/AnswerDotAI/RAGatouille
url_repo: https://github.com/AnswerDotAI/RAGatouille
---

# RAGatouille

## Pourquoi

Bibliothèque Python (AnswerDotAI, Ben Clavié, Apache-2.0) dont le but est de rendre la **[[Late-interaction retrieval|recherche par late-interaction]] (ColBERT)** simple à utiliser dans un pipeline RAG. Elle enveloppe l'implémentation de référence **colbert-ai** (Stanford) et expose en quelques lignes : **indexation** compressée et persistée sur disque (index **PLAID**), **recherche**, et **entraînement / fine-tuning** (traitement des données, *hard negative mining*). Argument central : les modèles ColBERT **généralisent mieux hors domaine** que les embeddings denses mono-vecteur et sont **économes en données**. À noter : la **maintenance a ralenti** (dernière release **0.0.9**, février 2025) ; le projet reste l'entrée la plus simple vers ColBERT.

## Quand l'utiliser

- Tester rapidement **ColBERT / late-interaction** comme retriever ou reranker, sans manipuler colbert-ai à la main.
- Corpus **spécialisé / out-of-domain** où le dense mono-vecteur généralise mal.
- **Fine-tuner** un modèle ColBERT sur son domaine (peu de données annotées) avec le minage de négatifs intégré.
- Brancher la late-interaction dans [[Dev/Services/LangChain|LangChain]] / [[Dev/Services/LlamaIndex|LlamaIndex]] (intégrations fournies).

## Quand NE PAS l'utiliser

- Reranking simple sur un top-k → un **cross-encoder** via [[Dev/Services/sentence-transformers|sentence-transformers]] (BGE-reranker…) est plus léger ([[Reranking]]).
- Retrieval dense mono-vecteur classique → [[Dev/Services/sentence-transformers|sentence-transformers]] + une [[Bases de données vectorielles|base vectorielle]].
- Mise à l'échelle de la late-interaction en production exigeante → moteur à support natif des multi-vecteurs ([[Dev/Services/Vespa|Vespa]]).
- Besoin de garanties de maintenance à jour → vérifier l'activité du dépôt avant de s'engager.

## Déploiement & coût

- `uv add ragatouille` ; Apache-2.0, gratuit. **Single-node**, **GPU** recommandé (encodage + index).
- S'appuie sur **colbert-ai**, [[Dev/Services/PyTorch|PyTorch]], faiss-cpu et [[Dev/Services/sentence-transformers|sentence-transformers]] — dépendances lourdes.
- Coût caché : l'index multi-vecteur (un vecteur par token) est **plus volumineux** qu'un index mono-vecteur ; PLAID le compresse.

## Pièges

- **Maintenance ralentie** (0.0.9, fév. 2025) : surveiller la compatibilité des dépendances avant un usage durable.
- Index **multi-vecteur volumineux** : prévoir le stockage ; PLAID atténue mais ne supprime pas le surcoût.
- ColBERT ≠ cross-encoder : c'est un retriever/scorer multi-vecteur, pas un simple reranker de paire — calibrer l'usage.
- Retours d'expérience détaillés : `Dev/REX/REX - RAGatouille.md`.

## Alternatives

Pas de substitut direct dans le brain pour la late-interaction « clé en main » : RAGatouille est le wrapper de référence au-dessus de **colbert-ai** (la lib Stanford, plus bas niveau). Pour le **reranking** classique par cross-encoder, voir [[Dev/Services/sentence-transformers|sentence-transformers]] (catégorie `ml/framework`) ; pour exécuter la late-interaction **à l'échelle**, [[Dev/Services/Vespa|Vespa]] la supporte nativement.

## Liens

- Met en œuvre le concept [[Late-interaction retrieval]] (ColBERT, MaxSim, index PLAID).
- [[Reranking]] · [[Recherche d'information]] — ses rôles dans le pipeline (retriever ou reclasseur).
- [[RAG]] — contexte d'usage.
- [[Dev/Services/sentence-transformers|sentence-transformers]] — l'alternative mono-vecteur / cross-encoder.
- [[Dev/Services/Vespa|Vespa]] — la late-interaction à l'échelle, en serving.
- Doc : https://github.com/AnswerDotAI/RAGatouille
