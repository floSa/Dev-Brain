---
role: brique
nom: FlashRank
alias: [flashrank]
pitch: "Bibliothèque Python (Apache-2.0) de reranking léger sur CPU — modèles ONNX de 4 Mo (TinyBERT) à 150 Mo, sans Torch ni Transformers ; conçue pour le serverless et les démarrages à froid ; dernière release PyPI 0.2.10 en janvier 2025."
categorie: llm/rag
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[bge-reranker]]", "[[Cohere Rerank]]", "[[Jina Reranker]]"]
complements: []
tags: [retrieval, reranking, rag]
url_docs: https://github.com/PrithivirajDamodaran/FlashRank
url_repo: https://github.com/PrithivirajDamodaran/FlashRank
---

# FlashRank

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python (Apache-2.0) de reranking léger sur CPU — modèles ONNX de 4 Mo (TinyBERT) à 150 Mo, sans Torch ni Transformers ; conçue pour le serverless et les démarrages à froid ; dernière release PyPI 0.2.10 en janvier 2025.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque Python qui ajoute du **reranking** à un pipeline de recherche existant, sans
GPU. Elle se présente comme « lite & super-fast » : elle tourne sur CPU sans exiger Torch ni
Transformers, et le modèle par défaut, `ms-marco-TinyBERT-L-2-v2`, pèse environ 4 Mo. La
liste des modèles va du cross-encoder `ms-marco-MiniLM-L-12-v2` (~34 Mo, annoncé comme le
meilleur cross-encoder du lot) à `ms-marco-MultiBERT-L-12` (~150 Mo, 100+ langues), avec un
`rank-T5-flan` (~110 Mo) qui n'est pas un cross-encoder et un `rank_zephyr_7b_v1_full`
(~4 Go, GGUF quantifié en 4 bits) pour le reranking **listwise** par LLM. Licence Apache-2.0.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Reranker **sans GPU** : CPU, conteneur minuscule, démarrage à froid rapide (serverless) | Multilingue exigeant ou modèle plus récent recherché : la liste ne compte qu'un `MultiBERT` pour les 100+ langues → [[bge-reranker]] ; la qualité relative n'est pas mesurée dans cette fiche, à évaluer sur son corpus ([[RAG eval]]) |
| Ajouter un étage de reclassement en quelques lignes à un pipeline existant | Aucun modèle à héberger, un appel d'API suffit → [[Cohere Rerank]] |
| Environnement **contraint** : poste industriel, machine sans accès GPU, image légère | **Maintenance** ralentie : dernière release PyPI (0.2.10) en janvier 2025, dernière release GitHub (0.2.9) en novembre 2024 |
| Prototyper vite un gain de précision avant d'investir dans un modèle plus lourd | Le `max_length` se règle sur la taille des passages : une valeur trop grande (512 pour des passages courts) alourdit la latence sans gain |

## Mise en œuvre

- Installation — `uv add flashrank` ; extra `flashrank[listwise]` pour les rerankers listwise à base de LLM
- Point d'entrée — l'objet `Ranker` sur un modèle nommé, appelé avec la requête et la liste de passages
- Prérequis — Python ; les poids se téléchargent depuis Hugging Face (le dépôt indique avoir migré les modèles vers le Hub par mesure de sécurité)
- Exécution — CPU, en local ; ONNX, sans dépendance à Torch
- Coût — gratuit ; le coût réel est le temps CPU par candidat, à borner par la taille du top-k

## Écosystème

### Alternatives

- [[bge-reranker]] — Famille de rerankers cross-encoders ouverts du BAAI (FlagEmbedding, MIT ; poids v2 Apache-2.0) — bge-reranker-v2-m3 (0,6 B, multilingue), variantes plus lourdes sur base Gemma ; se charge avec FlagReranker ou CrossEncoder, tourne en local.
- [[Cohere Rerank]] — API de reranking managée de Cohere (propriétaire) — reclasse un top-k de documents par pertinence à la requête ; rerank-v4.0 pro et fast, v3.5 multilingue à 4096 tokens de contexte ; déploiement privé (VPC ou on-prem) proposé sur devis.
- [[Jina Reranker]] — Rerankers de Jina AI (Elastic) — v3 et v3.5 listwise 0,6 B à 131K tokens de contexte, v2 multilingue cross-encoder, m0 multimodal ; poids CC-BY-NC 4.0 sur HF, usage commercial par l'API, les places de marché cloud ou la licence Jina On-Prem.

## Ressources

- Documentation — https://github.com/PrithivirajDamodaran/FlashRank
- Dépôt — https://github.com/PrithivirajDamodaran/FlashRank

## Voir aussi

- [[Reranking]] — la notion qu'il met en œuvre
- [[sentence-transformers]] — l'autre voie pour un cross-encoder local, via Torch
- [[Hybrid retrieval]] — l'étage amont qui fournit le top-k
- [[Comparatif - Rerankers]] — ce qui départage les rerankers du dossier
