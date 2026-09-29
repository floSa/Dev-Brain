---
role: brique
nom: Jina Reranker
alias: [jina-reranker, jina-reranker-v3, jina-reranker-v2-base-multilingual, jina-reranker-m0]
pitch: "Rerankers de Jina AI (Elastic) — v3 et v3.5 listwise 0,6 B à 131K tokens de contexte, v2 multilingue cross-encoder, m0 multimodal ; poids CC-BY-NC 4.0 sur HF, usage commercial par l'API, les places de marché cloud ou la licence Jina On-Prem."
categorie: llm/rag
famille: modele
licence_type: source-available
maturite: production
alternatives: ["[[bge-reranker]]", "[[Cohere Rerank]]", "[[FlashRank]]"]
complements: ["[[sentence-transformers]]"]
tags: [retrieval, reranking, rag, embeddings]
url_docs: https://jina.ai/reranker/
url_repo: 
---

# Jina Reranker

<!-- AUTO:BANDEAU:START -->
> Rerankers de Jina AI (Elastic) — v3 et v3.5 listwise 0,6 B à 131K tokens de contexte, v2 multilingue cross-encoder, m0 multimodal ; poids CC-BY-NC 4.0 sur HF, usage commercial par l'API, les places de marché cloud ou la licence Jina On-Prem.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Modèle | source-available | à charger dans un runtime | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Famille de rerankers de Jina AI, désormais sous **Elastic**. La page produit liste :
`jina-reranker-v3.5` et `jina-reranker-v3` (0,6 B, contexte de 131K tokens, architecture
**listwise** : le modèle voit plusieurs documents à la fois au lieu de noter des paires),
`jina-reranker-m0` (multimodal, pour documents visuels, contexte de 10K),
`jina-reranker-v2-base-multilingual` (cross-encoder de 278 M, contexte de 1 024 tokens,
100+ langues annoncées sur la page produit, 26+ testées sur la carte) et `jina-colbert-v2`
(late interaction, hors sujet ici). Les modèles courants sont livrés sous **CC-BY-NC 4.0** :
libres pour un usage non commercial, licence commerciale requise pour la production. Les
modèles v1 restent sous Apache-2.0.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un reranker à **contexte long** : la v3 annonce 131K tokens, contre 1 024 pour la v2 de la même famille | Un usage **commercial** en local sans contrat : les poids sont CC-BY-NC, il faut l'API, une place de marché cloud ou la licence Jina On-Prem d'Elastic → [[bge-reranker]] (Apache-2.0) |
| Reranker **multimodal** sur des documents visuels (`m0`) | Prototype sans budget ni GPU → [[FlashRank]] |
| Un déploiement **on-prem** sous contrat : Elastic vend « Jina On-Prem » pour le self-managed et l'air-gapped | Aucun contrat souhaité, un appel d'API suffit avec un éditeur unique → [[Cohere Rerank]] |
| Évaluer un reranker listwise contre les cross-encoders par paires | Le chargement par `CrossEncoder` n'est documenté que pour la v2 ; la v3 est publiée pour `transformers` (métadonnées du Hub) |

## Mise en œuvre

- Installation — rien pour l'API ; `uv add transformers` pour charger les poids v3 ; `uv add sentence-transformers` pour la v2 (carte : https://huggingface.co/jinaai/jina-reranker-v2-base-multilingual)
- Point d'entrée — l'API de reranking Jina (jetons, paiement à l'usage), ou les poids Hugging Face : `CrossEncoder("jinaai/jina-reranker-v2-base-multilingual", trust_remote_code=True)` pour la v2
- Prérequis — pour les poids, `trust_remote_code=True` (code distant exécuté) ; pour l'API, une clé
- Exécution — API hébergée, places de marché AWS SageMaker, Azure et Google Cloud, conteneurs Docker sous licence commerciale, ou local sur les poids pour un usage non commercial
- Coût — facturation au jeton, palier gratuit à 100 requêtes par minute ; licence commerciale Elastic pour l'on-prem, tarif sur devis

## Écosystème

### Alternatives

- [[bge-reranker]] — Famille de rerankers cross-encoders ouverts du BAAI (FlagEmbedding, MIT ; poids v2 Apache-2.0) — bge-reranker-v2-m3 (0,6 B, multilingue), variantes plus lourdes sur base Gemma ; se charge avec FlagReranker ou CrossEncoder, tourne en local.
- [[Cohere Rerank]] — API de reranking managée de Cohere (propriétaire) — reclasse un top-k de documents par pertinence à la requête ; rerank-v4.0 pro et fast, v3.5 multilingue à 4096 tokens de contexte ; déploiement privé (VPC ou on-prem) proposé sur devis.
- [[FlashRank]] — Bibliothèque Python (Apache-2.0) de reranking léger sur CPU — modèles ONNX de 4 Mo (TinyBERT) à 150 Mo, sans Torch ni Transformers ; conçue pour le serverless et les démarrages à froid ; dernière release PyPI 0.2.10 en janvier 2025.

### Compléments

- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi. — le runtime de la v2 : la carte du modèle documente son chargement par `CrossEncoder`.

## Ressources

- Documentation — https://jina.ai/reranker/

## Voir aussi

- [[Reranking]] — la notion qu'il met en œuvre
- [[Late-interaction retrieval]] — `jina-colbert-v2`, l'autre approche de la famille Jina
- [[Hybrid retrieval]] — l'étage amont qui fournit le top-k
- [[Comparatif - Rerankers]] — ce qui départage les rerankers du dossier
