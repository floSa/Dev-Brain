---
galaxie: wiki
type: concept
nom: Late-interaction retrieval
alias: [colbert, colbertv2, late interaction, interaction tardive, recherche multi-vecteur, plaid, maxsim]
categorie: concept/llm
domaines: [ai-eng]
tags: [retrieval, reranking, embeddings, semantic-search, information-retrieval, rag]
---

# Late-interaction retrieval

## Aperçu

- Représenter requête et document par **plusieurs vecteurs** — un par token, contextualisés — au lieu d'un seul vecteur global, puis comparer ces ensembles finement (**MaxSim**).
- Troisième voie entre le **bi-encoder** (rapide, grossier) et le **cross-encoder** (précis, cher) : on pré-calcule les embeddings du document (donc indexable, comme le dense) tout en gardant une interaction **token-à-token** (donc précis, proche du cross-encoder). Modèle phare : **ColBERT** (*Contextualized Late Interaction over BERT*).

## Concepts clés

### Multi-vecteur (token-level embeddings)
- Chaque token produit son propre embedding contextualisé. Un document = une **matrice** $(n_{\text{tokens}} \times d)$, pas un vecteur unique.
- D'où le nom *late* interaction : l'interaction requête↔document a lieu **tard**, au moment du score, pas au moment de l'encodage (qui reste indépendant).

### Bi-encoder vs cross-encoder vs late-interaction
- **Bi-encoder** (dense mono-vecteur) : un vecteur par texte, similarité cosinus. Pré-calculable, rapide, mais l'information est écrasée en un seul point.
- **Cross-encoder** : encode la paire (requête, document) ensemble → très précis, **non pré-calculable** → réservé au top-k ([[Reranking]]).
- **Late-interaction** : encodage indépendant **mais** multi-vecteur + MaxSim → pré-calculable *et* fin. Compromis qualité/scalabilité.

### ColBERTv2 & index PLAID
- Le multi-vecteur coûte cher en stockage (un vecteur par token). **ColBERTv2** compresse les embeddings (quantification résiduelle autour de centroïdes) et l'index **PLAID** accélère la recherche → la late-interaction devient utilisable comme **premier étage** (retriever), pas seulement comme reranker.

## Les maths, simplement

- Score MaxSim : $S(q,d) = \sum_{i \in q} \max_{j \in d} \mathbf{E}_{q_i} \cdot \mathbf{E}_{d_j}$ — pour **chaque** token de la requête, on prend sa **meilleure** correspondance parmi les tokens du document, puis on **somme**. $\mathbf{E}_{q_i}$, $\mathbf{E}_{d_j}$ sont les embeddings (normalisés) des tokens.
- À comparer au bi-encoder $\cos(\mathbf{e}_q, \mathbf{e}_d)$ (un seul produit scalaire) : MaxSim fait $|q| \times |d|$ produits, d'où sa finesse — et son coût de stockage/calcul.

## En pratique

- **Implémentations** : [[Dev/Services/RAGatouille|RAGatouille]] (wrapper simple au-dessus de colbert-ai), colbert-ai (référence Stanford), et des moteurs à support natif des multi-vecteurs comme [[Dev/Services/Vespa|Vespa]] ; [[Dev/Services/Qdrant|Qdrant]] et [[Dev/Services/Weaviate|Weaviate]] ont ajouté le multi-vecteur.
- **Deux usages** : retriever de premier étage (avec PLAID) **ou** reclasseur du top-k ([[Reranking]]).
- **Force** : meilleure **généralisation hors domaine** que le dense mono-vecteur, et bonne efficacité en données pour le fine-tuning.
- **Coût** : index plus volumineux et calcul de score plus lourd que le dense ; arbitrer selon le volume et la latence visée.

## Approches voisines & alternatives

- [[Recherche d'information]] — le cadre général (lexical / dense / hybride) ; la late-interaction en est la voie multi-vecteur.
- [[Reranking]] — la late-interaction peut tenir l'étage de précision, en alternative au cross-encoder.
- [[embeddings]] — le dense mono-vecteur que la late-interaction raffine en multi-vecteur.
- [[Hybrid retrieval]] — autre manière de dépasser le dense seul (fusion dense + lexical) ; SPLADE (sparse appris) en est un cousin.
- [[Dev/Services/RAGatouille|RAGatouille]] · [[Dev/Services/Vespa|Vespa]] — les implémentations côté Dev.

## Pour aller plus loin

- Khattab & Zaharia (2020) — *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT*.
- Santhanam et al. (2022) — *ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction*.
