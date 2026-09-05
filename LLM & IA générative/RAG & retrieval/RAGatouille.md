---
role: brique
nom: RAGatouille
alias: [ragatouille]
pitch: "Bibliothèque (AnswerDotAI) qui rend les modèles de late-interaction ColBERT simples à entraîner et à utiliser dans un pipeline RAG — indexation PLAID, recherche et reranking par-dessus colbert-ai ; maintenance ralentie (dernière release 0.0.9.post2 en mai 2025)."
categorie: llm/rag
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: []
complements: []
tags: [retrieval, reranking, rag, nlp]
url_docs: https://github.com/AnswerDotAI/RAGatouille
url_repo: https://github.com/AnswerDotAI/RAGatouille
---

# RAGatouille

<!-- AUTO:BANDEAU:START -->
> Bibliothèque (AnswerDotAI) qui rend les modèles de late-interaction ColBERT simples à entraîner et à utiliser dans un pipeline RAG — indexation PLAID, recherche et reranking par-dessus colbert-ai ; maintenance ralentie (dernière release 0.0.9.post2 en mai 2025).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque d'AnswerDotAI (Ben Clavié) dont le but est de rendre la
[[Late-interaction retrieval|recherche par late-interaction]] ColBERT simple à utiliser dans
un pipeline RAG. Elle enveloppe l'implémentation de référence **colbert-ai** (Stanford) et
expose en quelques lignes l'indexation compressée et persistée sur disque (index **PLAID**),
la recherche, et l'entraînement ou le fine-tuning avec préparation des données et *hard
negative mining*. Son argument central : les modèles ColBERT généralisent mieux hors domaine
que les embeddings denses mono-vecteur, et demandent moins de données annotées. Des
intégrations sont fournies pour [[LangChain]] et [[LlamaIndex]].

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tester rapidement ColBERT et la late-interaction comme retriever ou comme reranker, sans manipuler colbert-ai à la main | Mettre la late-interaction à l'échelle en production exigeante → [[Vespa]], qui supporte nativement les multi-vecteurs |
| Corpus spécialisé ou hors domaine, où le dense mono-vecteur généralise mal | Maintenance ralentie — 0.0.9.post2 en mai 2025, aucun commit depuis : vérifier la compatibilité des dépendances avant de s'engager sur la durée |
| Fine-tuner un modèle ColBERT sur son domaine avec peu de données annotées, minage de négatifs compris | Index multi-vecteur volumineux — un vecteur par token : prévoir le stockage, PLAID atténue le surcoût sans le supprimer |
| Brancher la late-interaction dans un pipeline LangChain ou LlamaIndex, intégrations fournies | ColBERT n'est pas un cross-encoder : c'est un retriever et scorer multi-vecteur, pas un reclasseur de paire — calibrer l'usage en conséquence |

## Mise en œuvre

- Installation — `uv add ragatouille`
- Point d'entrée — API Python : indexation PLAID, recherche, entraînement et fine-tuning
- Prérequis — GPU recommandé pour l'encodage et l'indexation ; dépendances lourdes — colbert-ai, [[PyTorch]], faiss-cpu, [[sentence-transformers]]
- Exécution — mono-nœud, bibliothèque importée dans l'app
- Coût — gratuit sous Apache-2.0 ; le coût caché est l'index multi-vecteur, plus volumineux qu'un index mono-vecteur

## Écosystème

### Alternatives

Aucun substitut direct dans le brain pour la late-interaction clé en main : RAGatouille est le
wrapper de référence au-dessus de **colbert-ai**, la bibliothèque Stanford, plus bas niveau.
Les deux voisinages sont ailleurs — le reranking classique par cross-encoder chez
[[sentence-transformers]], la late-interaction à l'échelle chez [[Vespa]].

## Ressources

- Documentation — https://github.com/AnswerDotAI/RAGatouille
- Dépôt — https://github.com/AnswerDotAI/RAGatouille

## Voir aussi

- [[Late-interaction retrieval]] — la notion qu'elle met en œuvre (ColBERT, MaxSim, index PLAID)
- [[RAG]] — le contexte d'usage
- [[Reranking]] · [[Recherche d'information]] — ses deux rôles possibles dans le pipeline
- [[Comparatif - Frameworks LLM]] · [[Comparatif - NLP]] — les deux vues qui la comparent
