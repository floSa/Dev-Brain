---
galaxie: wiki
type: concept
nom: Isolation Forest
alias: [iForest, Forêt d'isolement, IsolationForest]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [anomaly-detection, unsupervised, tree-based, ensemble]
---

# Isolation Forest

## Aperçu

- Détecteur d'anomalies non supervisé qui renverse la logique habituelle : au lieu de modéliser ce qui est **normal** puis de mesurer l'écart, il cherche directement ce qui est **facile à isoler**.
- L'intuition : en découpant l'espace au hasard, un point atypique se retrouve seul dans sa région après **très peu de coupes**. Un point noyé dans la masse en demande beaucoup. La profondeur d'isolement devient le score d'anomalie.

## Concepts clés

### Isoler plutôt que modéliser
- Les méthodes classiques ([[Gaussian Mixture Models (GMM)|GMM]], distance de Mahalanobis) apprennent la densité du normal — coûteux et fragile en grande dimension.
- Isolation Forest ne modélise rien. Il exploite le fait que les anomalies sont **peu nombreuses et différentes** : ces deux propriétés suffisent à les rendre séparables plus vite que les autres.

### Construction d'un arbre d'isolement
- À chaque nœud : tirer une variable **au hasard**, puis un seuil **au hasard** entre le min et le max observés. Répéter jusqu'à isoler chaque point ou atteindre la profondeur limite.
- Aucun critère d'impureté, aucune cible, aucune optimisation. C'est cette absence totale d'apprentissage qui rend la méthode aussi rapide.

### Le score, c'est la profondeur
- La profondeur moyenne d'un point sur l'ensemble des arbres mesure sa difficulté d'isolement. Profondeur **courte** = anomalie ; profondeur **longue** = normal.
- On normalise par la profondeur moyenne attendue dans un arbre aléatoire, pour obtenir un score borné entre 0 et 1 comparable d'un jeu à l'autre.

### Les paramètres qui comptent
- **`contamination`** — la proportion d'anomalies supposée. **Le seul paramètre vraiment critique** : il ne change pas les scores, seulement le seuil où l'on coupe. Le mettre à `'auto'` ou le fixer selon la connaissance métier ; c'est une hypothèse, pas une découverte.
- **`n_estimators`** — nombre d'arbres (100 par défaut, suffisant presque toujours).
- **`max_samples`** — nombre de points par arbre, **256 par défaut et volontairement petit**. Contre-intuitif mais essentiel : sur un gros échantillon, les anomalies se retrouvent noyées et masquées par les points normaux (*swamping* et *masking*). Sous-échantillonner les rend visibles.
- **`max_features`** — variables tirées par arbre ; à baisser en très grande dimension.

## Les maths, simplement

- Profondeur moyenne attendue pour isoler un point parmi $n$ dans un arbre binaire aléatoire : $c(n) = 2H(n-1) - \frac{2(n-1)}{n}$, où $H(i) \approx \ln(i) + 0{,}577$ est le nombre harmonique. C'est la référence de normalisation.
- Score d'anomalie : $s(x, n) = 2^{-\frac{\mathbb{E}[h(x)]}{c(n)}}$, où $\mathbb{E}[h(x)]$ est la profondeur moyenne de $x$ sur tous les arbres.
- Lecture : $s \to 1$ quand la profondeur est très courte → **anomalie franche**. $s \to 0$ → point normal. $s \approx 0{,}5$ → aucune structure d'anomalie décelable dans le jeu.
- Complexité **linéaire** en $n$ et faible en mémoire, puisque chaque arbre ne voit que 256 points : c'est là son avantage décisif sur les méthodes à distance en $O(n^2)$.

## En pratique

- **Pas besoin de standardiser** : comme tous les modèles à base d'arbres, les coupes sont invariantes par transformation monotone. Avantage net sur les détecteurs à distance ([[k-NN]], LOF) qui l'exigent ([[Mise à l'échelle]]).
- **Le défaut raisonnable sur tabulaire** quand $n$ est grand : linéaire, peu de réglage, robuste en dimension moyenne.
- **`contamination` détermine tout le résultat** et n'est pas apprenable. Le fixer trop haut fabrique de faux positifs ; trop bas rate les vraies anomalies. En l'absence d'étiquettes, préférer trier par score et faire trancher un expert sur le haut du classement plutôt que de croire un seuil.
- **Faiblesse : les anomalies locales.** Un point aberrant *à l'intérieur* d'un cluster dense — normal globalement, anormal dans son contexte — lui échappe. C'est précisément le terrain du LOF (*Local Outlier Factor*).
- **Ne gère ni les NaN ni les données catégorielles brutes** (contrairement à [[Gradient Boosting (GBDT)|LightGBM]]) : imputer et encoder en amont.
- Attention aux variables non pertinentes : les coupes étant tirées au hasard, du bruit dilue le signal. Sélectionner en amont aide ([[Sélection de variables]]).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.ensemble.IsolationForest]] ; [[Dev/Services/PyOD|PyOD]] pour comparer une dizaine de détecteurs sous une API commune ; [[Dev/Services/River|River]] en flux.

## Approches voisines & alternatives

- [[Détection d'outliers multivariée]] — le chapeau : toutes les familles de détecteurs et leurs hypothèses.
- [[Détection d'outliers univariée]] — quand une seule variable suffit (z-score, IQR) ; plus simple, à essayer d'abord.
- [[Random Forest]] — même brique d'arbres, mais supervisée et avec des coupes optimisées, non aléatoires.
- [[Gaussian Mixture Models (GMM)]] — l'approche par densité : modélise le normal explicitement, plus interprétable, plus coûteuse.
- [[Time series anomaly detection]] — quand les points sont ordonnés dans le temps, ce modèle ne s'applique pas tel quel.
- [[Apprentissage non supervisé]] — le cadre englobant.
- [[Imbalanced classification]] — l'alternative supervisée, si l'on dispose d'étiquettes d'anomalies.
- [[Types de données et choix de modèle]] — l'aiguillage amont.

## Pour aller plus loin

- Liu, Ting, Zhou (2008) — *Isolation Forest* : l'article fondateur, très lisible, qui explique le choix de `max_samples=256`.
- Liu, Ting, Zhou (2012) — *Isolation-Based Anomaly Detection* : la version étendue et les propriétés théoriques.
- Documentation scikit-learn — *Novelty and Outlier Detection* : le comparatif visuel des détecteurs sur données jouets.
