---
galaxie: wiki
type: concept
nom: Extra Trees
alias: [ExtraTrees, Extremely Randomized Trees, Arbres extrêmement aléatoires, ExtraTreesClassifier, Extra-Trees]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, tree-based, ensemble, classification, regression]
---

# Extra Trees

## Aperçu

- Variante du [[Random Forest]] qui pousse l'aléatoire un cran plus loin : au lieu de chercher le **meilleur seuil** de découpage pour chaque variable, elle en tire un **au hasard** et garde le meilleur parmi ces candidats tirés.
- Le pari est contre-intuitif : renoncer à optimiser chaque coupe dégrade chaque arbre pris isolément, mais les décorrèle davantage — et la moyenne y gagne. Bonus : c'est nettement plus rapide, puisqu'on ne trie plus les valeurs.

## Concepts clés

### La seule différence qui compte
- [[Random Forest]] : à chaque nœud, tirer un sous-ensemble de variables, puis **chercher le seuil optimal** sur chacune (tri des valeurs, évaluation de l'impureté).
- Extra Trees : à chaque nœud, tirer un sous-ensemble de variables, puis **tirer un seuil au hasard** dans l'intervalle observé de chacune. On ne garde que la meilleure de ces coupes hasardeuses.
- Tout le reste est identique. C'est une seule ligne d'algorithme qui change.

### Pourquoi la vitesse
- Chercher le seuil optimal impose de trier les valeurs à chaque nœud : c'est **l'essentiel du coût** d'un arbre. Tirer un seuil au hasard supprime ce tri.
- En pratique, un entraînement souvent 2 à 5 fois plus rapide qu'un Random Forest équivalent, à même nombre d'arbres.

### Le troc biais-variance
- Des coupes aléatoires → chaque arbre est plus faible et plus biaisé, mais les arbres se ressemblent **beaucoup moins**. La variance de la moyenne chute plus fort que le biais ne monte.
- Le gain net dépend du jeu : Extra Trees l'emporte souvent quand le bruit est important (les coupes optimales sur du bruit sont du surapprentissage déguisé), et perd quand le signal est net et demande des seuils précis.

### Pas de bootstrap par défaut
- Différence pratique souvent ignorée : `bootstrap=False` par défaut dans sklearn — chaque arbre voit **tout** le jeu. L'aléatoire vient déjà des seuils, inutile d'en rajouter par rééchantillonnage.
- Conséquence : **pas de score OOB** disponible tant qu'on n'active pas `bootstrap=True`.

### Les hyperparamètres

| Paramètre | Ce qu'il fait | Sens du curseur |
|---|---|---|
| `n_estimators` | Nombre d'arbres | ↑ = toujours mieux puis plafonne ; ne surapprend pas |
| `max_features` | Variables candidates par nœud | Le levier principal, comme en Random Forest |
| `max_depth` | Profondeur | Laissé libre par défaut ; les arbres doivent rester forts |
| `min_samples_leaf` | Effectif minimal d'une feuille | ↑ = lisse ; le frein utile contre le bruit |
| `bootstrap` | Rééchantillonnage | **`False` par défaut** (≠ Random Forest). À passer à `True` pour obtenir l'OOB |

## Les maths, simplement

- Random Forest, à chaque nœud : $\text{seuil} = \arg\max_{s} \; \Delta I(s)$ — on balaie tous les seuils $s$ possibles et on prend celui qui réduit le plus l'impureté.
- Extra Trees : $s \sim \mathcal{U}(\min_j, \max_j)$ — un seuil tiré uniformément dans l'intervalle observé de la variable $j$. On ne compare que les quelques coupes ainsi tirées.
- Le mécanisme du gain reste celui du [[Bagging|bagging]] : pour $M$ arbres de variance $\sigma^2$ et de corrélation moyenne $\rho$, la variance de la moyenne vaut $\rho \sigma^2 + \dfrac{1 - \rho}{M}\sigma^2$. Quand $M$ grandit, seul le terme $\rho \sigma^2$ subsiste — **baisser $\rho$ est le seul vrai levier**, et c'est exactement ce que font les seuils aléatoires.

## En pratique

- **Le réflexe utile : l'essayer en même temps que le Random Forest.** C'est un changement d'une ligne (`ExtraTreesClassifier` au lieu de `RandomForestClassifier`), c'est plus rapide, et il gagne assez souvent pour que l'essai soit rentable.
- **Ni l'un ni l'autre ne bat un [[Gradient Boosting (GBDT)|boosting]] réglé** sur tabulaire. Leur intérêt est ailleurs : robustes quasi sans réglage, parallélisables trivialement, et sans risque de surapprentissage par excès d'arbres.
- **Attention à l'importance des variables** : comme pour tous les modèles à arbres, l'importance par impureté est biaisée vers les variables à forte cardinalité. Utiliser l'importance par permutation ([[Explicabilité des modèles]]).
- **Pas de standardisation nécessaire**, comme tout modèle à arbres ([[Types de données et choix de modèle]]).
- Les seuils aléatoires en font aussi une brique d'extraction de représentations (*random embeddings*, `RandomTreesEmbedding`).
- Outils : [[Dev/Services/Scikit-Learn|sklearn.ensemble]] — `ExtraTreesClassifier`, `ExtraTreesRegressor`, `RandomTreesEmbedding`.

## Approches voisines & alternatives

- [[Random Forest]] — le parent direct : mêmes ingrédients, seuils optimisés au lieu d'être tirés. Le comparatif de référence.
- [[Bagging]] — le mécanisme sous-jacent, et l'explication du gain par décorrélation.
- [[Arbres de décision]] — l'apprenant de base.
- [[Gradient Boosting (GBDT)]] — le concurrent qui plafonne plus haut sur tabulaire, au prix d'un réglage sérieux.
- [[Isolation Forest]] — le cousin non supervisé : lui aussi tire ses coupes au hasard, mais pour isoler des anomalies.
- [[Ensembling]] — la vue d'ensemble des méthodes d'agrégation.
- [[Compromis biais-variance]] — le troc que ce modèle incarne.

## Pour aller plus loin

- Geurts, Ernst, Wehenkel (2006) — *Extremely Randomized Trees* : l'article fondateur, qui détaille le troc biais-variance.
- Documentation scikit-learn — *Ensemble methods*, section *Extremely Randomized Trees*.
