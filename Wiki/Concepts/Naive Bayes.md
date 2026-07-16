---
galaxie: wiki
type: concept
nom: Naive Bayes
alias: [Bayésien naïf, Classifieur bayésien naïf, GaussianNB, MultinomialNB, BernoulliNB, ComplementNB]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, classification, bayesian]
---

# Naive Bayes

## Aperçu

- Classifieur probabiliste qui applique le théorème de Bayes en supposant que **toutes les variables sont indépendantes conditionnellement à la classe**. C'est cette hypothèse, presque toujours fausse, qui lui vaut son nom.
- Le pari paie : l'hypothèse simplifie le calcul au point de le rendre trivial (un simple comptage), et le modèle reste étonnamment performant — notamment sur le texte, où il fut longtemps la référence anti-spam.

## Concepts clés

### Pourquoi « naïf »
- Estimer $P(x_1, …, x_d \mid y)$ conjointement est impossible : le nombre de combinaisons explose et aucun jeu ne les couvre.
- L'hypothèse naïve factorise le problème : $P(x_1, …, x_d \mid y) = \prod_j P(x_j \mid y)$. On passe d'une loi jointe à $d$ lois **univariées**, chacune estimable par un comptage.
- Dans un texte, cela revient à dire que « New » et « York » apparaissent indépendamment une fois le sujet connu. C'est faux. Le modèle fonctionne quand même.

### Pourquoi ça marche malgré tout
- Pour **classer**, seul l'ordre des probabilités compte, pas leur valeur. L'hypothèse naïve fausse gravement les probabilités mais préserve souvent l'**arg max**.
- Conséquence directe : bon classifieur, **mauvais estimateur de probabilité**. Ses scores sont typiquement écrasés vers 0 ou 1 par la multiplication de facteurs corrélés comptés plusieurs fois.

### Génératif, pas discriminant
- Il modélise $P(x \mid y)$ — comment les données sont engendrées dans chaque classe — puis retourne l'inférence par Bayes. Une [[Régression logistique]] modélise directement $P(y \mid x)$.
- Effet pratique : le génératif converge plus vite avec **peu de données** (il fait plus d'hypothèses), le discriminant le dépasse quand $n$ grandit (il en fait moins).

### Les variantes, selon le type de variable
- **MultinomialNB** — comptages (occurrences de mots). Le défaut sur du texte, avec [[TF-IDF]] ou des comptes bruts.
- **BernoulliNB** — variables binaires (mot présent / absent). Meilleur sur textes très courts.
- **GaussianNB** — variables continues, supposées gaussiennes dans chaque classe. L'hypothèse la plus fragile des trois.
- **ComplementNB** — variante conçue pour les classes déséquilibrées ; souvent meilleure que MultinomialNB sur corpus non équilibrés.

### Le lissage — paramètre `alpha`
- Un mot jamais vu dans une classe donne $P(\text{mot} \mid \text{classe}) = 0$, ce qui annule **tout le produit** : un seul terme inconnu suffit à disqualifier une classe.
- Le lissage de Laplace ajoute `alpha` à chaque compte pour interdire le zéro. `alpha=1` par défaut ; le baisser (0,01-0,1) aide sur gros vocabulaire. C'est le seul hyperparamètre réellement à régler.

## Les maths, simplement

- Théorème de Bayes : $P(y \mid x) = \dfrac{P(x \mid y)\, P(y)}{P(x)}$. Comme $P(x)$ est le même pour toutes les classes, il ne joue aucun rôle dans l'arg max — on peut l'ignorer.
- Avec l'hypothèse naïve : $\hat{y} = \arg\max_k \; P(y = k) \prod_{j=1}^{d} P(x_j \mid y = k)$.
- **En pratique on somme des logs** plutôt que multiplier : $\hat{y} = \arg\max_k \big[ \log P(y = k) + \sum_j \log P(x_j \mid y = k) \big]$. Multiplier des centaines de probabilités < 1 sous-déborde en flottant ; le log transforme le produit en somme et règle le problème.
- Lissage de Laplace : $P(x_j \mid y) = \dfrac{N_{jy} + \alpha}{N_y + \alpha \, d}$, où $N_{jy}$ = nombre de fois où $x_j$ apparaît dans la classe $y$.

## En pratique

- **Baseline texte imbattable en rapport qualité/effort** : [[TF-IDF]] + MultinomialNB, entraîné en une seconde sur des centaines de milliers de documents. Toujours l'essayer avant de sortir un [[Transformer architectures|Transformer]] ([[Classification de texte]]).
- **Ne jamais utiliser ses probabilités telles quelles** pour une décision seuillée ou une tarification : elles sont sur-confiantes par construction. Les calibrer ([[Calibration]]) ou changer de modèle.
- Entraînement en **une passe de comptage**, $O(n \cdot d)$, sans optimisation itérative. Il encaisse `partial_fit` (apprentissage incrémental) et les très grands vocabulaires sans broncher.
- **À l'aise quand $d \gg n$** : c'est le cas du texte, où le vocabulaire dépasse le nombre de documents. Là où [[k-NN]] s'effondre, lui tient.
- **Variables corrélées = son point faible.** Dupliquer une variable revient à compter son témoignage deux fois, et le modèle devient d'autant plus sûr de lui qu'il a tort. Retirer les redondances évidentes ([[Sélection de variables]]).
- GaussianNB sur des variables franchement non gaussiennes est à éviter — transformer d'abord, ou prendre un [[Gradient Boosting (GBDT)|GBDT]] qui ne suppose rien.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.naive_bayes]] (`MultinomialNB`, `BernoulliNB`, `GaussianNB`, `ComplementNB`), en `Pipeline` avec `TfidfVectorizer`.

## Approches voisines & alternatives

- [[Régression logistique]] — le pendant discriminant : plus lent à entraîner, mais probabilités calibrées et meilleur quand $n$ est grand. Le comparatif de référence.
- [[Inférence bayésienne]] — le cadre général dont Naive Bayes est l'application la plus dépouillée.
- [[Estimation MAP]] — le lissage de Laplace **est** un a priori de Dirichlet ; « ajouter alpha » est un geste bayésien déguisé.
- [[SVM]] — le concurrent historique sur texte, souvent meilleur, plus lent.
- [[Classification de texte]] — le terrain où il reste pertinent.
- [[TF-IDF]] — la vectorisation qui l'accompagne par défaut.
- [[Classification]] — le chapeau de la tâche.
- [[Types de données et choix de modèle]] — quand y recourir.

## Pour aller plus loin

- Ng & Jordan (2001) — *On Discriminative vs. Generative Classifiers* : la comparaison formelle avec la régression logistique.
- Rennie et al. (2003) — *Tackling the Poor Assumptions of Naive Bayes Text Classifiers* : l'origine de ComplementNB.
- Documentation scikit-learn — *Naive Bayes*.
