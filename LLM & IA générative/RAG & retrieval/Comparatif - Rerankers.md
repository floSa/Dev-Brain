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
- [[FlashRank]] — **le seul sans Torch ni GPU** : modèles ONNX de 4 à 150 Mo sur CPU, pour serverless et démarrages à froid. Le prix est un choix de modèles plus restreint et une maintenance ralentie (dernière release PyPI en janvier 2025).
- [[RAGatouille]] — **pas un cross-encoder** : ColBERT en late interaction, qui indexe *et* reclasse. Il entre dans la vue par son tag `reranking` ; c'est une autre voie vers l'étage de précision (cf. [[Late-interaction retrieval]]), à envisager quand on veut aussi remplacer le premier étage.

**Pas de fiche ici** : les rerankers à poids ouverts sont des modèles, et le brain ne décrit que des outils. Les deux cas courants se citent en texte simple. bge-reranker (BAAI) : code MIT, poids v2 en Apache-2.0, `v2-m3` multilingue de 0,6 B, qui se charge par `FlagReranker` ou par `CrossEncoder` de [[sentence-transformers]] ; il demande un GPU pour un débit correct. Jina Reranker : la v3 est listwise à 131K tokens de contexte ; poids CC-BY-NC 4.0, donc l'usage commercial passe par l'API, une place de marché cloud ou la licence Jina On-Prem d'Elastic.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
