---
role: brique
nom: Cohere Rerank
alias: [cohere-rerank, Rerank 3.5, Rerank 4, rerank-v4.0]
pitch: "API de reranking managée de Cohere (propriétaire) — reclasse un top-k de documents par pertinence à la requête ; rerank-v4.0 pro et fast, v3.5 multilingue à 4096 tokens de contexte ; déploiement privé (VPC ou on-prem) proposé sur devis."
categorie: llm/rag
famille: saas
licence_type: proprietary
hosted: [managed]
maturite: production
scaling: serverless
alternatives: ["[[bge-reranker]]", "[[FlashRank]]", "[[Jina Reranker]]"]
complements: []
tags: [retrieval, reranking, rag]
url_docs: https://docs.cohere.com/docs/rerank
url_repo: 
---

# Cohere Rerank

<!-- AUTO:BANDEAU:START -->
> API de reranking managée de Cohere (propriétaire) — reclasse un top-k de documents par pertinence à la requête ; rerank-v4.0 pro et fast, v3.5 multilingue à 4096 tokens de contexte ; déploiement privé (VPC ou on-prem) proposé sur devis.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | propriétaire | managé · serverless | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Endpoint de **reranking** de Cohere : on envoie une requête et une liste de documents, l'API
rend la liste **reclassée** par pertinence, prête à être tronquée avant le LLM. C'est le
deuxième étage d'un [[Reranking|pipeline en deux temps]], sans modèle à héberger. La
documentation liste cinq modèles : `rerank-v4.0-pro` et `rerank-v4.0-fast` (multilingues,
le second pour la latence et le débit), `rerank-v3.5` (multilingue) et les deux v3.0
`rerank-english-v3.0` et `rerank-multilingual-v3.0`. Les trois modèles v3 ont un contexte de
4096 tokens ; la documentation n'en donne pas pour les v4. La v4.0-pro accepte aussi des
documents semi-structurés (JSON). Rien à télécharger.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Ajouter un reranker à un pipeline sans GPU ni modèle à héberger : un appel d'API sur le top-k | Les documents **ne peuvent pas quitter** le réseau : l'API managée envoie le texte chez l'éditeur → [[bge-reranker]] en local |
| Corpus **multilingue**, ou documents JSON semi-structurés | Le volume de requêtes rend un service à l'appel plus cher qu'un GPU dédié : tarif non publié sur la page produit, à demander |
| Brancher un reranker par un connecteur de framework, sans code de modèle | Un modèle qu'on veut **figer** et rejouer à l'identique : les poids ne sont pas téléchargeables, seul l'éditeur tient les versions (aucune dépréciation annoncée dans la documentation consultée) |
| Un déploiement **privé** est acceptable : VPC ou on-prem, proposés par Cohere sur devis | Le budget est nul et la latence doit rester locale → [[FlashRank]] sur CPU |

## Mise en œuvre

- Installation — `uv add cohere` pour le SDK ; le service lui-même est provisionné côté éditeur
- Point d'entrée — l'endpoint `rerank` : requête + liste de documents, en retour les indices triés avec un score de pertinence
- Prérequis — une clé d'API Cohere ; le top-k vient d'un premier étage ([[Hybrid retrieval]] ou dense)
- Exécution — 100 % managé, à l'appel ; déploiement privé (VPC, on-prem) annoncé sur la page produit https://cohere.com/rerank, sur contrat
- Coût — à l'usage ; le tarif n'est pas affiché sur la page produit (« demander une démo »), donc non chiffré ici

## Écosystème

### Alternatives

- [[bge-reranker]] — Famille de rerankers cross-encoders ouverts du BAAI (FlagEmbedding, MIT ; poids v2 Apache-2.0) — bge-reranker-v2-m3 (0,6 B, multilingue), variantes plus lourdes sur base Gemma ; se charge avec FlagReranker ou CrossEncoder, tourne en local.
- [[FlashRank]] — Bibliothèque Python (Apache-2.0) de reranking léger sur CPU — modèles ONNX de 4 Mo (TinyBERT) à 150 Mo, sans Torch ni Transformers ; conçue pour le serverless et les démarrages à froid ; dernière release PyPI 0.2.10 en janvier 2025.
- [[Jina Reranker]] — Rerankers de Jina AI (Elastic) — v3 et v3.5 listwise 0,6 B à 131K tokens de contexte, v2 multilingue cross-encoder, m0 multimodal ; poids CC-BY-NC 4.0 sur HF, usage commercial par l'API, les places de marché cloud ou la licence Jina On-Prem.

## Ressources

- Documentation — https://docs.cohere.com/docs/rerank

## Voir aussi

- [[Reranking]] — la notion qu'il met en œuvre
- [[Hybrid retrieval]] — l'étage amont qui fournit le top-k
- [[RAG]] · [[Advanced RAG]] — le pipeline où il s'insère
- [[Comparatif - Rerankers]] — ce qui départage les rerankers du dossier
- [[Learning to rank]] — le cadre d'apprentissage du classement, dont le reranking est le second étage
