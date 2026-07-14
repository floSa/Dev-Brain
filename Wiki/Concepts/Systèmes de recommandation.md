---
galaxie: wiki
type: concept
nom: Systèmes de recommandation
alias: [recommender systems, recsys, filtrage collaboratif, collaborative filtering, factorisation matricielle, matrix factorization, two-tower]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [recommender-systems, ranking, embeddings, retrieval]
---

# Systèmes de recommandation

## Aperçu

- Prédire l'affinité entre un **utilisateur** et un **item** (produit, vidéo, article) pour ordonner ce qui sera proposé. Cœur des plateformes de contenu et d'e-commerce.
- Deux sources d'information : le **contenu** des items (features) et le **comportement** collectif (qui a interagi avec quoi). Le filtrage collaboratif exploite le second, le plus prédictif à grande échelle.

## Concepts clés

### Filtrage collaboratif
- Hypothèse : des utilisateurs aux goûts proches dans le passé le resteront. Recommander à partir des **co-occurrences** d'interactions, sans connaître le contenu.
- Voisinage (*memory-based*) : similarité user-user ou item-item (cosinus, Pearson) sur la matrice d'interactions. Simple, interprétable, coûteux en ligne.
- Démarrage à froid (*cold start*) : un nouvel utilisateur ou item sans historique n'a pas de voisins → recourir au contenu ou à des features.

### Factorisation matricielle
- Approcher la matrice creuse $R$ (utilisateurs × items) par un produit de deux matrices de **facteurs latents** : $R \approx P Q^\top$. Chaque utilisateur et chaque item devient un vecteur de dimension $k$.
- Apprise par moindres carrés alternés (ALS) ou descente de gradient, pas par [[SVD]] exacte (la matrice est trouée). Parenté algébrique avec la [[Réduction de dimension]] et les [[Matrix decompositions]].
- Variante implicite : pondérer les interactions par une confiance (clics, vues) plutôt que par des notes explicites.

### Modèles two-tower
- Deux encodeurs — une tour utilisateur, une tour item — projettent chacun dans le **même espace d'[[embeddings]]**. Le score est le produit scalaire des deux vecteurs.
- Les embeddings item se calculent hors ligne ; à la requête, seul l'embedding utilisateur est calculé puis confronté à un index ANN ([[Bases de données vectorielles]]). Passage à des catalogues massifs.
- Entraînement contrastif sur paires positives/négatives — même logique que le [[Metric learning & ré-identification|metric learning]].

### Retrieval puis ranking
- Architecture industrielle en deux étages : un **retrieval** rapide ramène quelques centaines de candidats (two-tower + ANN), un **ranking** fin les ordonne avec un modèle riche en features. Même découpage que la [[Recherche d'information]].

## Les maths, simplement

- Score de factorisation : $\hat r_{ui} = \mathbf{p}_u \cdot \mathbf{q}_i$, vecteurs latents de l'utilisateur $u$ et de l'item $i$.
- Objectif (feedback explicite) : $\min_{P,Q} \sum_{(u,i)\in\mathcal{K}} (r_{ui} - \mathbf{p}_u\cdot\mathbf{q}_i)^2 + \lambda(\lVert\mathbf{p}_u\rVert^2 + \lVert\mathbf{q}_i\rVert^2)$ — la pénalité $\lambda$ est de la [[Régularisation]].
- Two-tower : $s(u,i) = f_\theta(u)\cdot g_\phi(i)$, deux encodeurs entraînés à rapprocher les paires observées.

## En pratique

- Commencer par une baseline de popularité, puis filtrage collaboratif item-item (souvent un baseline redoutable), avant les modèles latents ou neuronaux.
- Le **feedback implicite** (clics, temps passé) est abondant mais biaisé (un non-clic n'est pas un rejet) ; pondérer plutôt que traiter comme du négatif franc.
- Évaluer en ordre, pas en erreur de note : [[Ranking metrics]] (NDCG, MAP, MRR, recall@k), et valider en ligne par [[A-B testing|tests A/B]] — l'offline sous-estime les effets de boucle de rétroaction.
- Pièges : biais de popularité (les têtes écrasent la longue traîne), cold start, fuite temporelle (toujours évaluer en respectant l'ordre chronologique).
- Outils Python : `implicit` (ALS feedback implicite), `LightFM` (hybride contenu + collaboratif), `Surprise` (factorisation explicite), TensorFlow Recommenders (two-tower).

## Approches voisines & alternatives

- [[embeddings]] — la représentation dense utilisateurs/items au cœur des modèles latents et two-tower.
- [[Bases de données vectorielles]] — le retrieval ANN des candidats à l'échelle.
- [[Recherche d'information]] — même architecture retrieval → ranking, pour des requêtes textuelles.
- [[Ranking metrics]] — l'évaluation d'un ordre de recommandations.
- [[SVD]], [[Matrix decompositions]], [[Réduction de dimension]] — la parenté algébrique de la factorisation matricielle.
- [[Metric learning & ré-identification]] — l'entraînement contrastif des espaces d'embeddings.
- [[Multi-armed bandits]] — l'exploration des items peu vus, contre le biais de popularité.
- [[Graph Neural Networks]] — recommandation sur le graphe biparti utilisateurs-items.

## Pour aller plus loin

- Koren, Bell & Volinsky (2009) — *Matrix Factorization Techniques for Recommender Systems* (leçon du prix Netflix).
- Covington, Adams & Sargin (2016) — *Deep Neural Networks for YouTube Recommendations* (retrieval/ranking, two-tower).
- Hu, Koren & Volinsky (2008) — *Collaborative Filtering for Implicit Feedback Datasets*.
