---
galaxie: wiki
type: concept
nom: Mutual information
alias: [Information mutuelle, MI, mutual info, information mutuelle ponctuelle, PMI]
categorie: concept/math
domaines: [data-sci, ml-eng]
tags: [information-theory, mutual-information]
---

# Mutual information

## Aperçu

- Quantifie la **dépendance** entre deux variables aléatoires : combien connaître l'une réduit l'incertitude sur l'autre. Nulle ssi les variables sont indépendantes.
- Capte **toute** forme de dépendance, linéaire ou non — là où la corrélation de Pearson ne voit que le linéaire. C'est sa force comme critère de sélection de variables.

## Concepts clés

### Réduction d'incertitude
- $I(X;Y) = H(Y) - H(Y\mid X)$ : l'incertitude sur $Y$, moins celle qui reste une fois $X$ connu. Symétrique : $I(X;Y) = I(Y;X)$.
- $\ge 0$ toujours ; $= 0$ ssi $X \perp Y$. Pas de borne supérieure universelle (bornée par $\min(H(X), H(Y))$).

### Une KL déguisée
- $I(X;Y) = D_{KL}\big(p(x,y)\,\|\,p(x)p(y)\big)$ : la [[KL divergence|divergence KL]] entre la loi conjointe et le produit des marges. L'information mutuelle mesure « à quel point la conjointe s'écarte de l'indépendance ».

### PMI (information mutuelle ponctuelle)
- Version par événement : $\text{pmi}(x,y) = \log\dfrac{p(x,y)}{p(x)p(y)}$. Beaucoup utilisée en NLP (collocations, anciens embeddings type word2vec ≈ factorisation d'une matrice PMI).

## Les maths, simplement

- $I(X;Y) = \sum_{x,y} p(x,y)\log\dfrac{p(x,y)}{p(x)p(y)}$ — espérance du PMI.
- Décompositions équivalentes : $I = H(X) + H(Y) - H(X,Y) = H(X) - H(X\mid Y)$.
- Cas gaussien bivarié : $I = -\tfrac12\log(1-\rho^2)$, fonction du coefficient de corrélation $\rho$ — pont explicite entre MI et corrélation.

## En pratique

- **Sélection de variables** : classer les features par MI avec la cible capte les liens non linéaires que le filtre par corrélation rate — `mutual_info_classif` / `mutual_info_regression` ([[Dev/Services/Scikit-Learn|sklearn.feature_selection]]). Cf. [[Sélection de variables]].
- **Estimation délicate en continu** : sensible au binning et à la dimension ; préférer les estimateurs k-NN (Kraskov) ou neuronaux (MINE) plutôt qu'un histogramme naïf.
- Apprentissage de représentations : objectifs contrastifs (InfoNCE) maximisent une borne inférieure de la MI entre vues (cf. [[embeddings]]).
- Sert aussi en analyse de clustering (information mutuelle ajustée, AMI) pour comparer deux partitions.

## Approches voisines & alternatives

- [[Shannon entropy]] — la MI est une différence d'entropies ($H(Y) - H(Y\mid X)$).
- [[KL divergence]] — la MI est la KL entre loi conjointe et produit des marges.
- [[Jensen-Shannon divergence]] — s'interprète comme la MI entre échantillon et indicateur de source.
- [[Sélection de variables]] — la MI y sert de filtre sensible aux dépendances non linéaires.
- [[embeddings]] — les méthodes contrastives maximisent une borne sur la MI entre vues.

## Pour aller plus loin

- Cover & Thomas — *Elements of Information Theory*, chapitre information mutuelle.
- Kraskov, Stögbauer & Grassberger (2004) — estimation de la MI par plus proches voisins.
