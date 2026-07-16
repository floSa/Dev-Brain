---
galaxie: wiki
type: concept
nom: Perceptron et MLP
alias: [Perceptron, MLP, Multi-Layer Perceptron, Perceptron multicouche, Réseau de neurones, Feedforward network, MLPClassifier]
categorie: concept/ml
domaines: [data-sci, ml-eng]
tags: [supervised, deep-learning, classification, regression]
---

# Perceptron et MLP

## Aperçu

- Le **perceptron** est le neurone artificiel originel (1958) : une somme pondérée des entrées passée dans une fonction seuil. Il ne sait tracer qu'une frontière linéaire — et bute sur le XOR, ce qui gela le domaine pendant quinze ans.
- Le **MLP** empile des couches de ces neurones avec une non-linéarité entre chaque. C'est ce qui débloque tout : le réseau apprend ses propres représentations au lieu de recevoir des variables prémâchées. Il est la brique de base dont dérivent [[CNN]] et [[Transformer architectures]].

## Concepts clés

### Du perceptron au MLP
- Un perceptron calcule $\hat{y} = \sigma(w^\top x + b)$ : c'est exactement une [[Régression logistique]] quand $\sigma$ est la sigmoïde.
- Empiler des couches **linéaires** ne sert à rien : la composition de deux fonctions linéaires reste linéaire. C'est la **non-linéarité** entre les couches qui crée la puissance, pas la profondeur seule.

### Les couches cachées
- Chaque couche transforme la représentation précédente. Les premières captent des motifs simples, les suivantes les combinent. La sortie n'est plus qu'un modèle linéaire appliqué à une représentation apprise.
- C'est le renversement fondamental face aux modèles classiques : on ne conçoit plus les variables ([[Ingénierie des caractéristiques]]), on les laisse émerger.

### Les fonctions d'activation
- **ReLU** $\max(0, z)$ — le défaut. Simple, gradient qui ne s'évanouit pas côté positif. Risque de « neurones morts » (bloqués à 0), d'où LeakyReLU / GELU.
- **Sigmoïde / tanh** — historiques, saturent aux extrêmes et tuent le gradient dans les réseaux profonds. À réserver aux couches de sortie.
- **Couche de sortie** : rien (régression), sigmoïde (binaire), softmax (multiclasse).

### La rétropropagation
- Le réseau apprend par [[Gradient descent|descente de gradient]]. La rétropropagation n'est que la règle de dérivation des fonctions composées appliquée efficacement, de la sortie vers l'entrée, en réutilisant les calculs intermédiaires.
- C'est un algorithme de **calcul du gradient**, pas d'optimisation — la mise à jour, elle, revient à [[Adam optimizer|Adam]] ou SGD.

### Les hyperparamètres qui comptent vraiment
- **Architecture** (`hidden_layer_sizes`) — nombre et largeur des couches. Commencer petit : une ou deux couches suffisent sur tabulaire.
- **Learning rate** — **le plus critique de tous**. Trop grand → divergence ; trop petit → stagnation. À régler avant tout le reste ([[Learning rate schedules]]).
- **Taille de batch** — compromis bruit / vitesse. Petit batch = gradient bruité, effet régularisant.
- **`alpha`** — pénalité L2 sur les poids ([[Régularisation]]).
- **Dropout / early stopping** — les régularisations qui comptent le plus en pratique.

### Théorème d'approximation universelle
- Une seule couche cachée suffisamment large peut approcher n'importe quelle fonction continue. Résultat célèbre et **trompeur** : il ne dit rien sur le nombre de neurones nécessaires, ni sur la capacité à *trouver* les bons poids par descente de gradient. En pratique, plusieurs couches étroites battent une couche énorme.

## Les maths, simplement

- Une couche : $h = \sigma(W x + b)$, avec $W$ la matrice de poids, $b$ le biais, $\sigma$ l'activation appliquée terme à terme.
- Un MLP à deux couches : $\hat{y} = W_2 \, \sigma(W_1 x + b_1) + b_2$. Sans $\sigma$, cela se réduit à $\hat{y} = (W_2 W_1) x + \text{const}$ — un simple modèle linéaire, quelle que soit la profondeur.
- Rétropropagation = règle de la chaîne : $\dfrac{\partial \mathcal{L}}{\partial W_1} = \dfrac{\partial \mathcal{L}}{\partial h} \cdot \dfrac{\partial h}{\partial W_1}$, propagée de couche en couche.
- Nombre de paramètres d'une couche $n_{\text{in}} \to n_{\text{out}}$ : $n_{\text{in}} \times n_{\text{out}} + n_{\text{out}}$. Il croît **quadratiquement** avec la largeur — d'où l'intérêt de la profondeur plutôt que de la largeur.

## En pratique

- **Sur tabulaire, il perd contre le boosting d'arbres.** Ce n'est pas une opinion : les benchmarks le montrent systématiquement à taille de données usuelle. Commencer par [[Gradient Boosting (GBDT)]] et ne sortir un MLP que si l'on a une raison précise ([[Types de données et choix de modèle]]).
- **Standardiser est obligatoire** : sans cela, les gradients explosent ou s'évanouissent selon les échelles, et l'entraînement ne converge pas ([[Mise à l'échelle]]).
- **Sa vraie place est ailleurs** : dès que les entrées sont des données non structurées ou des [[embeddings]], les représentations apprises deviennent imbattables. Le MLP survit d'ailleurs *à l'intérieur* des architectures modernes (les blocs feed-forward d'un [[Transformer architectures|Transformer]] sont des MLP).
- Toujours activer l'**early stopping** : le réseau surapprend vite, et c'est la régularisation la moins chère.
- **Non déterministe** : l'initialisation aléatoire fait varier le résultat d'un run à l'autre. Fixer les graines et vérifier la stabilité sur plusieurs runs avant de conclure à une amélioration.
- **Boîte noire** : aucune lecture directe des poids. Si la décision doit s'expliquer, passer par [[Explicabilité des modèles]] (SHAP) — ou choisir un [[GAM]] et s'épargner le problème.
- Outils : [[Dev/Services/Scikit-Learn|sklearn.neural_network.MLPClassifier]] pour un essai rapide ; [[Dev/Services/PyTorch|PyTorch]] / [[Dev/Services/Keras|Keras]] dès que le sujet est sérieux.

## Approches voisines & alternatives

- [[Régression logistique]] — le perceptron d'origine : un MLP sans couche cachée. La baseline à battre.
- [[Gradient Boosting (GBDT)]] — le concurrent qui gagne sur tabulaire ; le premier réflexe.
- [[CNN]] — un MLP à connexions locales et poids partagés, pour l'image.
- [[Transformer architectures]] — l'architecture dominante ; ses blocs feed-forward sont des MLP.
- [[Gradient descent]] / [[Adam optimizer]] — comment les poids sont réellement mis à jour.
- [[Régularisation]] — la pénalité `alpha`, le dropout, l'early stopping.
- [[Kolmogorov-Arnold Networks]] — alternative récente : apprendre les activations plutôt que les poids.
- [[Types de données et choix de modèle]] — quand un réseau se justifie.

## Pour aller plus loin

- Rosenblatt (1958) — *The Perceptron* ; Minsky & Papert (1969) — *Perceptrons* : le livre qui montra la limite du XOR et gela le domaine.
- Rumelhart, Hinton, Williams (1986) — *Learning representations by back-propagating errors*.
- Goodfellow, Bengio, Courville — *Deep Learning*, ch. 6 (Deep Feedforward Networks).
