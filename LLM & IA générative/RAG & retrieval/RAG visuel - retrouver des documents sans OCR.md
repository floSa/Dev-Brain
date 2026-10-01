---
role: notion
nom: RAG visuel - retrouver des documents sans OCR
alias: ["RAG visuel : retrouver des documents sans OCR", RAG visuel, visual RAG, visual document retrieval, recherche de pages par image]
categorie: llm/rag
domaines: [ai-eng, data-eng]
tags: [rag, retrieval, embeddings, vision-language, multimodal, ocr, document-parsing, information-retrieval]
---

# RAG visuel - retrouver des documents sans OCR

> Notion datée du 2026-10-01 : les chiffres cités viennent des articles et des cartes de modèles lus ce jour-là, et les scores de benchmark sont ceux des auteurs. Le mécanisme MaxSim est dans [[Late-interaction retrieval]], la décision d'architecture d'un RAG interne dans [[RAG documentaire on-prem - clé en main ou assemblé]] : ni l'un ni l'autre n'est repris ici.

## Aperçu

- **Indexer l'image de la page**, pas son texte : un modèle vision-langage encode chaque page en plusieurs vecteurs, et la requête est comparée à ces vecteurs sans passer par un OCR, une détection de mise en page ni un découpage.
- Utile quand le sens est **dans la mise en page** — schémas, plans, tableaux, diapositives, formulaires — et qu'un texte extrait n'en garde que des morceaux. Modèle de référence : [[ColPali]], introduit par Faysse et al. (ICLR 2025).

## Concepts clés

### Pourquoi l'OCR perd l'information

- La chaîne classique enchaîne détection de mise en page, OCR, légendage des figures, découpage, puis embedding. Chaque étape **jette du signal** : un tableau devient une suite de cellules sans leurs lignes, un schéma disparaît ou se réduit à une légende, la position d'un élément sur un plan n'a pas d'équivalent en texte.
- Les erreurs se **cumulent** d'étape en étape, et la chaîne est longue à régler : le papier de ColPali décrit ces processus comme longs et fragiles, et mesure leur recul sur le benchmark ViDoRe.
- L'OCR reste un pari raisonnable sur du texte propre ; il l'est moins sur des scans dégradés, des documents techniques ou des pages denses en figures.

### Recherche par image de page, en multi-vecteurs

- Le modèle (un VLM : PaliGemma, Qwen2-VL, SmolVLM selon la variante) découpe la page en patchs et sort **environ 1 030 vecteurs de 128 dimensions** par page ; la requête devient une liste de vecteurs de jetons, et le score est MaxSim. C'est la late interaction de [[Late-interaction retrieval]], appliquée à des patchs d'image plutôt qu'à des jetons de texte.
- Le même principe existe en vecteur unique par page : DSE (Ma et al., EMNLP 2024), qui donne un index bien plus petit pour une précision moindre.

### Coût de stockage et de calcul

- **Stockage** : environ 0,26 Mo par page en fp16, soit 26 Go pour 100 000 pages — plus de cent fois un embedding unique de 1 024 dimensions en fp16 (2 Ko).
- **Calcul** : un GPU pour indexer (le papier mesure 0,39 s par page sur un NVIDIA L4) ; l'encodage d'une requête prend de l'ordre de 30 ms sur GPU. Le CPU n'est pas garanti : Vespa mesure environ 2,5 s par page sur un Mac M1.
- **Réduire l'index** : le pooling de patchs (Clavié et al., 2024, arXiv 2409.14683) — ×3 retire 66,7 % des vecteurs pour 97,8 % des performances d'après le README de ColPali ; la binarisation, environ 16 Ko par page d'après un billet de Vespa ; ou un premier étage sur des vecteurs poolés (32 par page dans le tutoriel de Qdrant), puis un reclassement par les vecteurs complets.

### Licence des poids : un critère de choix

- Les poids ColPali ne portent pas tous la même licence : leur modèle de base décide. ColQwen2 repose sur une base Apache-2.0 ; ColPali v1.x sur PaliGemma, sous les conditions de Gemma ([[Gemma]]) ; ColQwen2.5 sur Qwen2.5-VL-3B, sous une licence de recherche **non commerciale** ([[Qwen]]). Le champ « MIT » de la carte ne dit que la licence des adaptateurs. Le tableau est dans [[ColPali]].

## Les maths, simplement

- Le score d'une page $d$ pour une requête $q$ est $S(q,d)=\sum_{i=1}^{n_q}\max_{1\le j\le n_d}\langle \mathbf{q}_i,\mathbf{d}_j\rangle$, où $\mathbf{q}_i$ sont les $n_q$ vecteurs de la requête, $\mathbf{d}_j$ les $n_d \approx 1030$ vecteurs de la page et $\langle\cdot,\cdot\rangle$ le produit scalaire : chaque jeton de requête va chercher le patch qui lui ressemble le plus, et on additionne.
- Le stockage vaut $N \times n_d \times 128 \times 2$ octets pour $N$ pages en fp16, soit environ 264 Ko par page : le coût est **linéaire en $n_d$**, ce qui explique que le pooling soit le levier principal.

## En pratique

- **Quand le visuel gagne** : documents riches en figures et en mise en page, corpus scannés de qualité variable, pas de chaîne de parsing maintenable. **Quand le parsing reste préférable** : texte courant en colonnes simples ([[Docling]], [[MinerU]], [[PaddleOCR]], [[olmOCR]]), besoin de texte exact (citation, extraction de champs, recherche lexicale), corpus qui change souvent (chaque page ré-encodée coûte du GPU), stockage ou GPU contraints.
- **Évaluer sur ses propres documents.** ViDoRe v1 (ColPali, 2024) est jugé saturé par ses auteurs ; ViDoRe v2 (Macé et al., 2025, arXiv 2505.17166) et v3 (Loison et al., 2026, arXiv 2601.08620 : 10 jeux, environ 26 000 pages, 3 099 requêtes vérifiées, 6 langues, nDCG@10) relèvent le niveau. Ce que dit v3 : les retrievers visuels devancent les textuels, mais un **reranker textuel** apporte +13,2 points de nDCG@10 contre un gain marginal pour un reranker visuel, et les tableaux, graphiques et requêtes multi-pages restent les cas difficiles.
- **Désaccord entre sources, laissé tel quel.** Most et al. (2025, arXiv 2505.05666) comparent ColPali à des chaînes OCR et trouvent que le visuel excelle sur les documents vus à l'entraînement, alors que l'OCR **généralise mieux** à des documents inconnus ; ViDoRe v3 donne l'avantage au visuel. Les corpus et les modèles diffèrent : seul un jeu de test maison tranche.
- **Hybride** : router par type de document, ou combiner un retriever visuel et un reranker textuel. La génération de la réponse demande ensuite un modèle capable de lire l'image de la page ([[Qwen]] et [[Gemma]] ont des variantes vision) ; v3 relève que des contextes hybrides ou visuels améliorent la qualité de la réponse.
- **Exploitation on-prem** : le GPU sert à l'indexation et aux requêtes, pas forcément à l'hébergement du moteur ; l'index se range dans un moteur à vecteurs multiples (documenté par [[Qdrant]], [[Weaviate]], Vespa). `colpali-engine` est déprécié au profit de [[sentence-transformers]] v6 : un projet neuf part de là. Byaldi, une surcouche à deux lignes, est dormante (dernière version en novembre 2024) et son index n'est pas compressé.
- **Pièges** : licence de la base du modèle lue après coup ; index qui gonfle sans pooling ; benchmarks publics à l'avantage du modèle qui les a vus ; images de pages produites à des résolutions différentes de celles de l'entraînement.

## Approches voisines & alternatives

- [[ColPali]] — la brique : méthode, famille de poids et licences, état de la bibliothèque.
- [[Late-interaction retrieval]] — le mécanisme MaxSim sur du texte (ColBERT), et [[RAGatouille]] pour l'employer.
- Le parsing puis l'indexation du texte : [[Docling]], [[MinerU]], [[PaddleOCR]], [[olmOCR]] — la voie de référence quand le texte suffit.
- [[RAG documentaire on-prem - clé en main ou assemblé]] — où ce choix se place dans une architecture de RAG interne.
- [[bge-m3]] et [[Qwen3-Embedding]] — les embeddings textuels, base de la chaîne de parsing contre laquelle le papier de ColPali se mesure (BGE-M3).
- [[Hybrid retrieval]] — la fusion lexical et dense, à croiser avec un retriever visuel.
- [[LlamaIndex]] — documente un reclassement ColPali (`ColPaliRerank`).

## Pour aller plus loin

- Faysse et al. (2024), *ColPali: Efficient Document Retrieval with Vision Language Models*, ICLR 2025 — https://arxiv.org/abs/2407.01449
- Macé, Loison, Faysse (2025), *ViDoRe Benchmark V2: Raising the Bar for Visual Retrieval* — https://arxiv.org/abs/2505.17166
- Loison et al. (2026), *ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios* — https://arxiv.org/abs/2601.08620
- Most et al. (2025), *Lost in OCR Translation? Vision-Based Approaches to Robust Document Retrieval* — https://arxiv.org/abs/2505.05666
- Clavié, Chaffin, Adams (2024), *Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling* — https://arxiv.org/abs/2409.14683
- Ma et al. (2024), *Unifying Multimodal Retrieval via Document Screenshot Embedding* — https://arxiv.org/abs/2406.11251
- Qdrant, *Multivector Document Retrieval with ColPali/ColQwen* — https://qdrant.tech/documentation/tutorials-search-engineering/pdf-retrieval-at-scale/
- Vespa, *Scaling ColPali to billions of PDFs* (2024-09-20) — https://blog.vespa.ai/scaling-colpali-to-billions/
