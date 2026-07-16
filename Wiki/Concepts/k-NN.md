---
galaxie: wiki
type: concept
nom: k-NN
alias: [KNN, k plus proches voisins, k-Nearest Neighbors, Plus proches voisins, KNeighborsClassifier, Apprentissage paresseux, Lazy learning]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, classification, regression]
---

# k-NN

## Aperçu

- Le modèle supervisé le plus simple qui soit : pour prédire, on cherche les `k` observations les plus proches dans les données d'entraînement et on prend leur avis — vote majoritaire en [[Classification]], moyenne en [[Régression]].
- **Aucun apprentissage** : le modèle « mémorise » le jeu d'entraînement, tout le travail est repoussé à la prédiction. D'où son surnom d'apprentissage *paresseux*, et son coût inversé : entraînement instantané, prédiction lente.

## Concepts clés

### Le paramètre `k`
- `k` **petit** (1) → frontière très découpée, le modèle épouse chaque point y compris le bruit : variance maximale, surapprentissage. Avec $k=1$ l'erreur d'entraînement est nulle — et ne veut rien dire.
- `k` **grand** → on moyenne sur un large voisinage, la frontière se lisse : biais qui augmente. À l'extrême, $k = n$ prédit toujours la classe majoritaire.
- C'est le curseur [[Compromis biais-variance|biais-variance]] le plus lisible de tout le ML. Prendre `k` impair en binaire évite les égalités.

### La distance **est** le modèle
- Euclidienne par défaut ; Manhattan sur données hétérogènes ; cosinus sur du texte et des [[embeddings]] (où seule l'orientation compte, pas la norme).
- Changer de distance change le modèle plus profondément que changer `k`.

### Pondération des voisins
- `uniform` : les `k` voisins pèsent pareil, même celui qui est trois fois plus loin.
- `distance` : chaque voisin pèse $1/d$. Souvent meilleur, et rend le choix de `k` moins critique.

### Le fléau de la dimension
- C'est la limite structurelle du modèle. En grande dimension, les distances **se concentrent** : le point le plus proche et le plus lointain finissent à peu près à la même distance. La notion de « voisin » perd son sens, et le modèle avec.
- En pratique, k-NN se dégrade vite au-delà de quelques dizaines de variables. Réduire d'abord ([[PCA]], [[Réduction de dimension]]) ou changer de famille.

### Coût à la prédiction
- Prédire un point = calculer sa distance à **tous** les points d'entraînement : $O(n \cdot d)$ par prédiction. Ce qui est gratuit à l'entraînement se paie à chaque appel, indéfiniment.
- Les structures d'index (`kd_tree`, `ball_tree`) accélèrent en basse dimension et deviennent inutiles en haute. À grande échelle, c'est le domaine des [[Index ANN — internes|index ANN approchés]].

## Les maths, simplement

- Distance euclidienne : $d(x, x') = \sqrt{\sum_{j=1}^{d} (x_j - x'_j)^2}$. La somme est dominée par les variables de grande amplitude — **d'où l'obligation de standardiser**.
- Prédiction en régression : $\hat{y}(x) = \frac{1}{k} \sum_{i \in N_k(x)} y_i$, où $N_k(x)$ = les `k` plus proches voisins. En classification : la classe majoritaire dans $N_k(x)$.
- Version pondérée : $\hat{y}(x) = \dfrac{\sum_{i \in N_k(x)} w_i \, y_i}{\sum_{i \in N_k(x)} w_i}$ avec $w_i = 1 / d(x, x_i)$.
- Résultat théorique remarquable : quand $n \to \infty$, l'erreur du 1-NN est **au pire le double** de l'erreur du classifieur optimal de Bayes. Un modèle sans aucun apprentissage n'est jamais plus de deux fois pire que l'optimum — de quoi justifier son statut de baseline.

## En pratique

- **Standardiser est obligatoire.** Sans cela, une variable en euros écrase une variable en années et les voisins n'ont aucun sens ([[Mise à l'échelle]]).
- **Excellente baseline, rarement un modèle final.** Il donne en trois lignes une borne de ce qu'un modèle local peut extraire. S'il bat un [[Gradient Boosting (GBDT)|GBDT]] réglé, c'est le GBDT qui a un problème.
- Régler `k` par [[Validation croisée|validation croisée]] : la courbe erreur vs `k` est le meilleur support pédagogique du [[Compromis biais-variance|dilemme biais-variance]].
- **Sensible au déséquilibre** : si une classe est rare, les voisins d'un point rare sont majoritairement de la classe fréquente et il est systématiquement mal classé ([[Imbalanced classification]]).
- **N'extrapole pas et ne gère pas les NaN.** Sa vraie force aujourd'hui n'est plus la classification tabulaire mais la **recherche par similarité** sur [[embeddings]] — c'est le même calcul, passé à l'échelle ([[Bases de données vectorielles]]).
- Variante utile : `KNNImputer`, qui impute une valeur manquante par la moyenne de ses voisins ([[Imputation des valeurs manquantes]]).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.neighbors]] (`KNeighborsClassifier`, `KNeighborsRegressor`, `KNNImputer`) ; à l'échelle : [[Dev/Services/Faiss|Faiss]], [[Dev/Services/hnswlib|hnswlib]], [[Dev/Services/Annoy|Annoy]].

## Approches voisines & alternatives

- [[k-médoïds (PAM)]] — même logique de distance, mais non supervisée : former des groupes autour de points représentatifs.
- [[SVM]] — l'autre modèle à distance ; global et optimisé, là où k-NN est local et paresseux.
- [[Arbres de décision]] — l'alternative non paramétrique qui, elle, ne demande aucune standardisation.
- [[Index ANN — internes]] — comment le calcul du plus proche voisin passe à des millions de points.
- [[Bases de données vectorielles]] — l'usage industriel du k-NN aujourd'hui, sur [[embeddings]].
- [[Réduction de dimension]] — le préalable qui le sauve en grande dimension.
- [[Classification]] / [[Régression]] — les chapeaux des deux tâches.
- [[Types de données et choix de modèle]] — quand y recourir, et quand s'abstenir.

## Pour aller plus loin

- Cover & Hart (1967) — *Nearest Neighbor Pattern Classification* : la borne du facteur 2.
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*, ch. 13.3.
- Documentation scikit-learn — *Nearest Neighbors*.
