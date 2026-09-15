---
role: comparatif
nom: Comparatif - Rerankers
categorie: llm/rag
tags: [reranking, retrieval, rag]
---

# Comparatif - Rerankers

> On tranche sur : où le modèle tourne — API managée, GPU local, CPU sans Torch — et sous quelle licence, car c'est elle qui décide d'un usage commercial ou on-prem. Un membre du lot n'est pas un cross-encoder mais un retriever à late interaction qui reclasse aussi.

![[Comparatif - Rerankers.base]]

## Ce qui départage

- [[Cohere Rerank]] — **le seul managé sans poids** : un appel d'API, aucun modèle à héberger, propriétaire. Multilingue (v4.0 pro et fast, v3.5), avec un déploiement privé VPC ou on-prem proposé sur devis. Le tarif n'est pas publié sur la page produit.
- [[bge-reranker]] — **le reranker ouvert et local par défaut** : code MIT, poids v2 en Apache-2.0, multilingue avec `v2-m3` (0,6 B), variantes Gemma plus lourdes. Se charge par `FlagReranker` ou par `CrossEncoder` de [[sentence-transformers]]. Demande un GPU pour un débit correct.
- [[FlashRank]] — **le seul sans Torch ni GPU** : modèles ONNX de 4 à 150 Mo sur CPU, pour serverless et démarrages à froid. Le prix est un choix de modèles plus restreint et une maintenance ralentie (dernière release PyPI en janvier 2025).
- [[Jina Reranker]] — **le seul listwise et à contexte long** : la v3 annonce 131K tokens, et `m0` traite des documents visuels. Piège de licence : poids CC-BY-NC 4.0, donc l'usage commercial passe par l'API, une place de marché cloud ou la licence Jina On-Prem d'Elastic.
- [[RAGatouille]] — **pas un cross-encoder** : ColBERT en late interaction, qui indexe *et* reclasse. Il entre dans la vue par son tag `reranking` ; c'est une autre voie vers l'étage de précision (cf. [[Late-interaction retrieval]]), à envisager quand on veut aussi remplacer le premier étage.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
