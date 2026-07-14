---
galaxie: wiki
type: concept
nom: Ranking metrics
alias: [Métriques de ranking, métriques d'ordonnancement, NDCG, DCG, MAP, MRR, Precision@k, Recall@k, Hit Rate, learning-to-rank, métriques de recherche d'information]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [model-evaluation, ranking]
---

# Ranking metrics

## Aperçu

- Évaluent la **qualité d'un ordre** : un système qui classe des items par pertinence (recherche, recommandation, *learning-to-rank*, retriever d'un RAG).
- Ce qui compte n'est pas la valeur prédite mais le **rang** des bons items — idéalement en haut de la liste.

## Concepts clés

### Métriques @k (coupées au top-k)
- Precision@k et Recall@k = pertinents parmi les $k$ premiers / retrouvés dans les $k$ premiers. Hit Rate@k = au moins un pertinent dans le top-k. Le $k$ doit refléter ce que l'utilisateur voit réellement.

### MAP (Mean Average Precision)
- Moyenne, sur les requêtes, de l'*Average Precision* (précision relevée aux rangs de chaque pertinent). Récompense le fait de placer les pertinents tôt. Pertinence **binaire**.

### MRR (Mean Reciprocal Rank)
- Moyenne de $1/\text{rang}$ du **premier** item pertinent. Adaptée quand une seule bonne réponse compte (questions-réponses, navigation, déduplication).

### NDCG (Normalized Discounted Cumulative Gain)
- Gère la pertinence **graduée** (pas seulement 0/1) et escompte le gain selon la position (facteur logarithmique). Normalisé par l'ordre idéal → score dans $[0,1]$. Standard dès que la pertinence est multi-niveaux.

## Les maths, simplement

- $\text{DCG@}k=\sum_{i=1}^{k}\dfrac{2^{rel_i}-1}{\log_2(i+1)}$ ; $\text{NDCG@}k=\dfrac{\text{DCG@}k}{\text{IDCG@}k}$ (IDCG = DCG de l'ordre parfait).
- $\text{AP}=\dfrac{1}{|\text{pertinents}|}\sum_{k} P(k)\cdot \mathbb{1}[\,k\ \text{pertinent}\,]$ ; $\text{MAP}=\dfrac{1}{Q}\sum_{q}\text{AP}_q$.
- $\text{MRR}=\dfrac{1}{Q}\sum_{q}\dfrac{1}{\text{rang du 1}^{\text{er}}\ \text{pertinent}}$.

## En pratique

- Choisir selon la tâche : MRR (une seule bonne réponse), MAP (plusieurs, pertinence binaire), NDCG (pertinence graduée).
- Évaluer **par requête** puis moyenner ; la variance entre requêtes est informative.
- Cas central de l'évaluation d'un retriever RAG et des systèmes de recommandation.
- L'AUC de [[ROC-AUC & courbe PR]] est elle-même une métrique de rang (probabilité qu'un positif soit mieux classé qu'un négatif).
- Découper par requête / utilisateur en [[Validation croisée]] pour éviter qu'une même requête fuite entre train et test.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.metrics — ndcg_score, label_ranking_average_precision_score]], `pytrec_eval`, `ranx`.

## Approches voisines & alternatives

- [[ROC-AUC & courbe PR]] — l'AUC-ROC mesure la qualité d'un ordre global (paires bien classées).
- [[Classification metrics]] — Precision@k et Recall@k transposent précision et rappel à une liste tronquée.
- [[Validation croisée]] — découpage par requête pour estimer ces métriques sans fuite.

## Pour aller plus loin

- Järvelin & Kekäläinen (2002) — article d'origine de la (N)DCG.
- Liu (2009) — *Learning to Rank for Information Retrieval*.
