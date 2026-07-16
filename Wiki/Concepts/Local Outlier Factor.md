---
galaxie: wiki
type: concept
nom: Local Outlier Factor
alias: [LOF, Facteur d'aberration locale, LocalOutlierFactor, Densité locale]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, unsupervised]
---

# Local Outlier Factor

## Aperçu

- Détecteur d'anomalies qui compare la **densité locale** d'un point à celle de ses voisins. Un point est anormal non pas parce qu'il est loin de tout, mais parce qu'il est **nettement plus isolé que son entourage immédiat**.
- C'est le seul de la famille à capter les anomalies **contextuelles** : un point de densité moyenne, parfaitement normal à l'échelle globale, mais aberrant au milieu d'un amas dense. C'est exactement l'angle mort d'[[Isolation Forest]].

## Concepts clés

### Local, et c'est tout le sujet
- Un jeu réel contient souvent des régions de densités très différentes : un amas serré ici, un nuage diffus là. Un seuil **global** de densité déclare alors toute la région diffuse anormale — ce qui est faux, c'est juste sa nature.
- LOF normalise : chaque point est comparé **à ses propres voisins**, jamais à une référence globale. Un point du nuage diffus est jugé parmi les points diffus.

### Distance d'accessibilité
- Une astuce de lissage : au lieu de la distance brute entre $A$ et $B$, on prend $\max(\text{distance à } B, \; \text{distance du }k\text{-ième voisin de } B)$.
- Effet : à l'intérieur d'un amas dense, toutes les distances sont écrasées à la même valeur, ce qui stabilise l'estimation de densité et empêche le bruit de micro-distances de produire des faux positifs.

### Le score, et sa lecture
- $\text{LOF} \approx 1$ → le point a la même densité que ses voisins : **normal**.
- $\text{LOF} \gg 1$ → le point est bien plus isolé que ses voisins : **anomalie**.
- $\text{LOF} < 1$ → le point est *plus dense* que son voisinage : cœur d'amas.
- Contrairement à [[Isolation Forest]], le score n'est **pas borné** : il n'y a pas de seuil universel, sa valeur dépend du jeu. C'est une faiblesse pratique réelle — un LOF de 1,5 est une anomalie franche sur un jeu, du bruit sur un autre.

### Détection vs nouveauté
- Piège d'API classique en sklearn : par défaut (`novelty=False`), LOF **n'a pas de `predict`**. Il ne sait que scorer le jeu sur lequel il a été ajusté (`fit_predict`), parce que la densité locale se calcule par rapport aux points présents.
- Pour scorer des points *nouveaux*, il faut `novelty=True` — et alors on perd `fit_predict`. Les deux modes s'excluent.

### Les hyperparamètres

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `n_neighbors` | Taille du voisinage de référence | **Le seul qui compte vraiment.** ↓ = très local, sensible au bruit. ↑ = lisse, rate les petits amas d'anomalies. Défaut 20, souvent correct |
| `contamination` | Proportion d'anomalies supposée | Ne change pas les scores, seulement le seuil. `'auto'` ou valeur métier |
| `metric` | Distance employée | Euclidienne par défaut ; cosinus sur [[embeddings]] |
| `novelty` | Scorer des points nouveaux | `False` = `fit_predict` seul ; `True` = `predict` sur du neuf. Mutuellement exclusifs |

- Règle empirique sur `n_neighbors` : le prendre au moins égal à la taille du plus petit groupe d'anomalies que l'on veut détecter. Si les fraudes vont par paquets de 10, un `n_neighbors=5` les verra comme un amas normal.

## Les maths, simplement

- Distance d'accessibilité de $A$ vers $B$ : $\text{reach-dist}_k(A, B) = \max\big(\text{k-distance}(B), \; d(A, B)\big)$, où $\text{k-distance}(B)$ est la distance de $B$ à son $k$-ième voisin.
- Densité locale d'accessibilité — l'inverse d'une distance moyenne, donc bien une densité : $\text{lrd}_k(A) = \left( \dfrac{\sum_{B \in N_k(A)} \text{reach-dist}_k(A, B)}{|N_k(A)|} \right)^{-1}$.
- Le score, enfin — un simple **rapport de densités** : $\text{LOF}_k(A) = \dfrac{\sum_{B \in N_k(A)} \frac{\text{lrd}_k(B)}{\text{lrd}_k(A)}}{|N_k(A)|}$. On divise la densité moyenne des voisins par celle du point. C'est cette division qui rend la mesure **locale** — toute échelle globale se simplifie.
- Complexité : $O(n^2)$ en naïf, ramenée à $O(n \log n)$ par index spatial en basse dimension. C'est le facteur limitant face à [[Isolation Forest]], linéaire en $n$.

## En pratique

- **Standardiser est obligatoire** : c'est un modèle à distance, comme [[k-NN]] ([[Mise à l'échelle]]).
- **À réserver aux $n$ modérés** (quelques dizaines de milliers). Au-delà, le $O(n^2)$ devient rédhibitoire et [[Isolation Forest]] s'impose.
- **Souffre du fléau de la dimension**, pour la même raison que [[k-NN]] : au-delà de quelques dizaines de variables, les distances se concentrent et la densité locale perd son sens. Réduire d'abord ([[PCA]]).
- **Le bon réflexe : LOF et Isolation Forest sont complémentaires, pas concurrents.** Les faire tourner tous les deux et regarder les désaccords est souvent plus instructif que de choisir. Ce qu'ils flaggent tous les deux est robuste ; ce que seul LOF flagge est contextuel.
- **Le score n'étant pas borné**, ne pas s'accrocher à un seuil : trier par score et faire trancher un expert sur le haut du classement.
- Ne gère ni les NaN ni les catégorielles brutes : imputer et encoder en amont.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.neighbors.LocalOutlierFactor]] ; [[Dev/Services/PyOD|PyOD]] pour comparer une dizaine de détecteurs sous une API commune.

## Approches voisines & alternatives

- [[Isolation Forest]] — le concurrent direct : linéaire en $n$, sans standardisation, mais aveugle aux anomalies **locales**. La comparaison de référence.
- [[Détection d'outliers multivariée]] — le chapeau : toutes les familles de détecteurs et leurs hypothèses.
- [[One-Class SVM]] — l'approche par frontière : apprend l'enveloppe du normal plutôt que sa densité.
- [[k-NN]] — la même mécanique de voisinage, en supervisé.
- [[DBSCAN]] — même intuition de densité, mais pour former des clusters ; ses points « bruit » sont de fait des outliers.
- [[Détection d'outliers univariée]] — quand une seule variable suffit ; à essayer d'abord.
- [[Apprentissage non supervisé]] — le cadre englobant.

## Pour aller plus loin

- Breunig, Kriegel, Ng, Sander (2000) — *LOF: Identifying Density-Based Local Outliers* : l'article fondateur, remarquablement clair sur le « pourquoi local ».
- Documentation scikit-learn — *Novelty and Outlier Detection* : le comparatif visuel où l'écart LOF / Isolation Forest saute aux yeux.
