---
role: brique
nom: ColPali
alias: [colpali, colqwen, colqwen2, colqwen2.5, colpali-engine, vidore, colsmol]
pitch: "Recherche de pages de documents par leur image (ILLUIN, code MIT) — un modèle vision-langage encode chaque page en environ 1 030 vecteurs comparés à la requête par MaxSim, sans OCR ; colpali-engine est déprécié au profit de Sentence Transformers v6, et la licence des poids varie selon le modèle de base."
categorie: llm/rag
famille: paquet
licence_type: open-source
maturite: deprecated
langage: Python
alternatives: ["[[sentence-transformers]]"]
complements: ["[[Qdrant]]", "[[Weaviate]]", "[[LlamaIndex]]"]
tags: [retrieval, embeddings, vision-language, multimodal, rag, information-retrieval]
url_docs: https://github.com/illuin-tech/colpali
url_repo: https://github.com/illuin-tech/colpali
---

# ColPali

<!-- AUTO:BANDEAU:START -->
> Recherche de pages de documents par leur image (ILLUIN, code MIT) — un modèle vision-langage encode chaque page en environ 1 030 vecteurs comparés à la requête par MaxSim, sans OCR ; colpali-engine est déprécié au profit de Sentence Transformers v6, et la licence des poids varie selon le modèle de base.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | deprecated | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Méthode et bibliothèque d'ILLUIN Technology pour **retrouver des pages de documents sans
OCR** : un modèle vision-langage lit l'image de la page et en sort environ **1 030 vecteurs
de 128 dimensions** (1 024 patchs plus 6 jetons d'instruction) ; la requête devient aussi une
liste de vecteurs, et le score est **MaxSim** (cf. [[Late-interaction retrieval]]). Les
schémas, tableaux et plans restent donc dans l'index tels qu'ils sont dessinés. Le papier
(Faysse et al., *ColPali: Efficient Document Retrieval with Vision Language Models*, ICLR
2025, arXiv 2407.01449) a introduit le benchmark ViDoRe. **Le paquet `colpali-engine` n'est
plus recommandé** : son README le réserve à la recherche et aux projets existants, et préconise Sentence Transformers v6 (`MultiVectorEncoder`) pour tout
nouveau projet. Les poids ColPali, ColQwen et ColSmol continuent de se charger, par l'un ou
l'autre.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Les documents portent leur sens dans la **mise en page** — schémas, plans, tableaux, diapositives — et l'OCR en perd l'essentiel | Le corpus est du **texte courant** en colonnes simples : le parsing suit mieux, et ViDoRe v3 donne +13,2 points de nDCG@10 à un reranker textuel contre +0,2 à un visuel → [[Docling]], [[MinerU]] |
| Un GPU est disponible pour **indexer** (0,39 s par page sur un L4 selon le papier) et pour encoder les requêtes (environ 30 ms) | Un projet **neuf** est lancé sur `colpali-engine` : passer par [[sentence-transformers]] v6 |
| La licence des poids est lue **avant** de choisir le modèle (tableau ci-dessous) | Le stockage est contraint : environ **0,26 Mo par page** en fp16, soit 26 Go pour 100 000 pages (calcul : 1 030 × 128 × 2 octets) |
| Un moteur à vecteurs multiples est déjà en place : [[Qdrant]] (`max_sim` depuis la 1.10), [[Weaviate]] (depuis la 1.29), Vespa | Le corpus change souvent : chaque page ré-encodée coûte du GPU, là où un parseur sur CPU coûte peu |

Licence des poids, lue sur les cartes Hugging Face le 2026-10-01 :

| Poids | Carte | Modèle de base | Ce que la licence implique pour une ESN |
|---|---|---|---|
| ColQwen2 v1.0 | Apache-2.0 | Qwen2-VL-2B, Apache-2.0 | Aucune condition particulière : le choix le plus simple |
| ColPali v1.1 à v1.3 | MIT | PaliGemma-3B, licence **Gemma** | Usage commercial permis sous la politique d'usage de Google ; redistribuer ou **héberger comme service par API** vaut « distribution » et impose de transmettre les termes ; Google peut restreindre l'usage en cas de violation (cf. [[Gemma]]) |
| ColQwen2.5 v0.1 et v0.2 | MIT | Qwen2.5-VL-3B, **Qwen Research License** | **Non commercial** : un usage commercial exige l'accord d'Alibaba Cloud (cf. [[Qwen]]). Le champ MIT de la carte ne le dit pas, et le tableau du README annonce Apache-2.0 à tort |
| ColSmol-256M et 500M | MIT | SmolVLM, Apache-2.0 | Sans condition particulière ; retrait de précision à mesurer |

## Mise en œuvre

- Installation — `pip install colpali-engine` ; constat du 2026-10-01 : v0.3.18 du 2026-08-22 (PyPI), 2 823 étoiles, code MIT, environ 93 400 téléchargements PyPI sur 30 jours ; successeur : `pip install sentence-transformers` (6.1.0 du 2026-09-18), qui charge les mêmes configurations de modèle
- Point d'entrée — `ColPali` ou `ColQwen2` avec leur processeur : `process_images` pour les pages, `process_queries` pour les requêtes, `score_multi_vector` pour MaxSim. Byaldi, une surcouche d'AnswerDotAI à deux lignes (Apache-2.0), est **dormante** : v0.0.7 du 2024-11-13, index non compressé en mémoire
- Prérequis — un GPU pour l'indexation ; `flash-attn` est optionnel ; poids d'environ 6 Go en bf16 pour un modèle de 3 milliards de paramètres (calcul) ; Poppler pour convertir les PDF en images. Le papier et la doc ne garantissent pas des requêtes sur CPU (Vespa mesure environ 2,5 s par page sur un Mac M1)
- Exécution — en bibliothèque ; l'index se range dans un moteur à vecteurs multiples. Réduire le coût : pooling de patchs (×3 retire 66,7 % des vecteurs et garde 97,8 % des performances d'après le README), binarisation (environ 16 Ko par page, chiffres du billet de Vespa), ou premier étage poolé puis reclassement par les vecteurs d'origine (tutoriel de Qdrant)
- Coût — code gratuit sous MIT ; le coût est le GPU d'indexation et le stockage de l'index. Les scores ViDoRe du README (par exemple 84,8 pour ColPali v1.3, 89,4 pour ColQwen2.5 v0.2) sont annoncés par l'équipe, sur ViDoRe v1, que ses propres auteurs jugent saturé (plus de 90 % de nDCG@5) : lire plutôt la v3

## Écosystème

### Alternatives

- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi. Successeur désigné par le README de `colpali-engine`.
- voisin : [[RAGatouille]] — Bibliothèque (AnswerDotAI) qui rend les modèles de late-interaction ColBERT simples à entraîner et à utiliser dans un pipeline RAG — indexation PLAID, recherche et reranking par-dessus colbert-ai ; maintenance ralentie (dernière release 0.0.9.post2 en mai 2025). Le même MaxSim sur du texte (ColBERT), sans l'image.
- voisin : [[Docling]] — Bibliothèque de conversion de documents d'IBM Research : compréhension fine de la mise en page et des tableaux (PDF, DOCX, PPTX…), export Markdown / HTML / JSON et intégrations gen AI ; modèles légers exécutables en local. La voie du parsing : extraire le texte et la structure, puis indexer.

### Compléments

- [[Qdrant]] — Base vectorielle en Rust, ultra-rapide, filtrage payload puissant, self-host simple.
- [[Weaviate]] — Base vectorielle orientée production, recherche hybride dense+BM25, self-host ou managé.
- [[LlamaIndex]] — Framework orienté données pour le RAG et les agents — ingestion, indexation et récupération sur tes documents, puis interrogation par LLM ; le plus direct pour brancher un LLM sur une base de connaissances.

## Ressources

- Dépôt — https://github.com/illuin-tech/colpali (l'avis de dépréciation ouvre le README)
- Papier — https://arxiv.org/abs/2407.01449
- Papier — ViDoRe v3, nDCG@10 sur six langues : https://arxiv.org/abs/2601.08620
- Documentation — migration depuis colpali-engine : https://www.sbert.net/docs/migration_guide.html#migrating-from-colpali-engine
- Tutoriel — Qdrant, ColPali à grande échelle : https://qdrant.tech/documentation/tutorials-search-engineering/pdf-retrieval-at-scale/
- Article — Vespa, binarisation des vecteurs : https://blog.vespa.ai/scaling-colpali-to-billions/

## Voir aussi

- [[RAG visuel - retrouver des documents sans OCR]] — la notion : pourquoi l'OCR perd l'information, coût, évaluation, quand le parsing reste préférable
- [[Late-interaction retrieval]] — le mécanisme MaxSim, vu sur du texte
- [[RAG documentaire on-prem - clé en main ou assemblé]] — où placer cette voie dans un RAG documentaire on-prem
- [[bge-m3]] — la base textuelle contre laquelle le papier mesure ColPali
- [[RAG & retrieval]] — le hub du dossier
