---
role: notion
nom: Rétropropagation et différentiation automatique
alias: [Rétropropagation, rétropropagation du gradient, backpropagation, backprop, différentiation automatique, automatic differentiation, autodiff, mode inverse, reverse-mode AD, mode avant, forward-mode AD, gradients qui disparaissent, gradients qui explosent, vanishing gradient, exploding gradient, gradient clipping, torch.autograd, jax.grad, no_grad, detach, produit hessienne-vecteur]
categorie: ml/apprentissage-profond
domaines: [ml-eng, data-sci]
tags: [autograd, deep-learning, gradient-descent]
---

# Rétropropagation et différentiation automatique

## Aperçu

- La **rétropropagation** calcule le gradient de la perte par rapport à **tous** les paramètres d'un réseau en une seule passe arrière, par la règle de la chaîne. La **différentiation automatique** (AD) est la famille de techniques, plus générale, dont elle est un cas particulier : Baydin et al. la décrivent comme « similaire mais plus générale que la rétropropagation ».
- C'est ce calcul qui rend la [[Gradient descent|descente de gradient]] praticable sur des millions de paramètres. Rumelhart, Hinton et Williams (1986) l'ont fait connaître comme procédure qui ajuste les poids pour minimiser l'écart entre sortie obtenue et sortie voulue, et dont les unités cachées finissent par représenter des traits utiles de la tâche. La technique est plus ancienne : Baydin et al. citent Linnainmaa (1970, 1976) comme la première description publiée du mode inverse, que Werbos (1974) reformule avec des variables à temps discret triées selon leurs dépendances.
- L'AD n'est ni de la **différentiation numérique** (différences finies : erreurs de troncature et d'arrondi, $2mn$ évaluations pour un jacobien) ni de la **différentiation symbolique** (expressions qui enflent de façon exponentielle) : elle applique la règle de la chaîne **aux opérations élémentaires du programme**, et donne la dérivée exacte à la précision machine près.

## Concepts clés

### Graphe de calcul et règle de la chaîne
- Une perte est une composition d'opérations élémentaires : $L = f_K \circ \dots \circ f_1(x, \theta)$. Le **graphe de calcul** mémorise ces opérations et leurs entrées.
- Le gradient s'obtient en multipliant les jacobiens locaux le long du graphe. Le **mode inverse** les multiplie **de la sortie vers l'entrée**, sous forme de produits vecteur-jacobien : à chaque nœud, un seul vecteur ($\partial L/\partial h$) est propagé, jamais une matrice.

### Mode avant contre mode inverse
- **Mode avant** : propage avec chaque valeur sa dérivée dans une direction donnée (un produit jacobien-vecteur, ou *jvp*). Les **nombres duaux** en donnent le modèle : $f(v + \dot v\,\varepsilon) = f(v) + f'(v)\,\dot v\,\varepsilon$ avec $\varepsilon^2 = 0$.
- **Mode inverse** : évalue d'abord la fonction en gardant les valeurs intermédiaires, puis remonte (produit vecteur-jacobien, ou *vjp*).
- Pour $f : \mathbb{R}^n \to \mathbb{R}^m$, Baydin et al. donnent le coût d'un jacobien complet : $n\,c\,\mathrm{ops}(f)$ en mode avant, $m\,c\,\mathrm{ops}(f)$ en mode inverse, avec une constante $c < 6$, typiquement entre 2 et 3 (Griewank et Walther, 2008). Le mode inverse l'emporte quand $m \ll n$. Pour une perte scalaire ($m = 1$), **une seule** passe inverse donne le gradient entier, contre $n$ passes en mode avant : c'est pour cela que l'entraînement utilise le mode inverse.
- La doc JAX chiffre l'autre côté : un *jvp* coûte environ 3× la fonction seule et sa **mémoire ne dépend pas de la profondeur** ; en mode inverse, les FLOPs sont raisonnables mais la **mémoire croît avec la profondeur**.

### Le coût mémoire de la passe arrière
- La passe arrière a besoin des valeurs intermédiaires de la passe avant (les *activations*). Les stocker est ce qui fait croître la mémoire avec la profondeur et la taille du lot.
- Le **checkpointing** échange du calcul contre de la mémoire : ne pas garder toutes les activations, en recalculer une partie à la demande. Baydin et al. citent Gruslys et al. (2016) : jusqu'à 95 % de mémoire économisée pour 33 % de calcul en plus, dans un cas de rétropropagation à travers le temps sur un réseau récurrent. Détail et réglage dans [[Gradient checkpointing]] ; côté outils : `torch.utils.checkpoint`, `jax.checkpoint` (alias `remat`).

### Gradients qui disparaissent ou explosent
- Le gradient d'une couche profonde est un **produit de jacobiens**. Hochreiter (thèse de diplôme, 1991) l'écrit comme un produit de facteurs qui décroît ou croît de façon exponentielle avec la profondeur (ou la longueur de la séquence), ce qui rend la descente de gradient très difficile. Bengio, Simard et Frasconi (1994) montrent pourquoi l'apprentissage de dépendances longues par descente de gradient devient de plus en plus difficile à mesure que leur durée augmente.
- Pascanu, Mikolov et Bengio (2013), pour les réseaux récurrents : une **condition nécessaire** pour que les gradients croissent est que le rayon spectral de la matrice récurrente dépasse 1. Leur remède contre l'explosion est le **clipping de la norme** : si $\lVert \hat g \rVert \ge \text{seuil}$, alors $\hat g \leftarrow (\text{seuil} / \lVert \hat g \rVert)\, \hat g$. Le seuil est un hyperparamètre auquel l'entraînement est peu sensible (6 et 45 dans leurs expériences).
- Les leviers qui agissent sur l'échelle des signaux en amont (normalisation, initialisation) sont dans [[Normalisation et initialisation des réseaux]].

### `torch.autograd` : un graphe refait à chaque itération
- PyTorch enregistre les opérations **pendant** la passe avant : le graphe est recréé de zéro à chaque itération, ce qui autorise du flot de contrôle Python arbitraire (« ce qu'on exécute est ce qu'on différencie »).
- `requires_grad` vaut faux par défaut, sauf pour un `nn.Parameter`. `backward()` **accumule** les gradients dans les feuilles (d'où le `zero_grad()` entre deux pas). Le graphe est libéré après `backward` sauf `retain_graph=True`.
- Chaque tenseur porte un **compteur de version** : une modification en place d'un tenseur sauvegardé pour la passe arrière est détectée, et une erreur est levée plutôt que de calculer un gradient faux.

### `no_grad`, `inference_mode`, `detach`, `eval()`
- **`torch.no_grad()`** : les calculs ne sont jamais enregistrés, même si une entrée a `requires_grad=True` ; leurs sorties restent utilisables ensuite dans du code différentiable.
- **`torch.inference_mode()`** : version « extrême » du précédent, plus rapide, mais les tenseurs créés dedans ne peuvent plus entrer dans un calcul enregistré après la sortie du mode.
- **`.detach()`** sort un tenseur du graphe : il n'est plus différentiable à partir de ce point. Le gradient ne le traverse pas (cible fixe, métrique à journaliser).
- **`model.eval()` ne coupe pas les gradients** : il change le comportement de certaines couches (normalisation, dropout). La doc PyTorch le signale expressément, parce que le nom prête à confusion avec les trois précédents.

### `jax.grad` et `jax.jit` : des transformations de fonctions
- JAX traite la différentiation comme une **transformation composable** de fonctions : `jax.grad` renvoie la fonction gradient, `jax.jvp` et `jax.vjp` exposent les deux modes, `jax.jit` compile (XLA), `jax.vmap` vectorise. `grad` s'applique à sa propre sortie, donc **tout ordre de dérivée** s'obtient par composition.
- Contrepartie : `jit`, `grad` et `vmap` exigent des fonctions **pures**. Les effets de bord et l'état global ne sont pas fiables (l'état global est figé à la première compilation) et les tableaux sont immuables.

### Second ordre
- Un **produit hessienne-vecteur** $Hv$ s'obtient sans former la hessienne, en $O(n)$. Deux compositions sont décrites, et les sources ne retiennent pas la même. Baydin et al. (d'après Pearlmutter, 1994) : *reverse-on-forward*, le mode inverse appliqué à la dérivée directionnelle calculée en mode avant ; ils précisent que le surcoût d'enregistrement varie selon la configuration et l'implémentation. Le cookbook JAX : *forward-over-reverse*, un *jvp* appliqué au gradient, `jvp(grad(f), ...)`, qu'il donne comme le plus efficace pour le hessien complet.
- PyTorch : `backward(create_graph=True)` construit le graphe de la dérivée elle-même, ce qui permet de la redériver. Usage typique : les méthodes qui différencient **à travers** une mise à jour de gradient, comme MAML dans [[Méta-apprentissage et few-shot learning]].

## Les maths, simplement

- Pour des couches $h_l = f_l(h_{l-1}, \theta_l)$ et une perte $L(h_K)$, avec $J_l = \partial h_l / \partial h_{l-1}$ :
  $$\frac{\partial L}{\partial \theta_l} = \frac{\partial L}{\partial h_K}\, J_K\, J_{K-1} \cdots J_{l+1}\; \frac{\partial h_l}{\partial \theta_l}$$
- Le mode inverse évalue ce produit **de gauche à droite** : $\delta_K = \partial L/\partial h_K$, puis $\delta_{l-1}^{\top} = \delta_l^{\top} J_l$. Chaque étape est un vecteur ligne multiplié par une matrice, jamais un produit de deux matrices.
- Les gradients disparaissent ou explosent quand $\lVert J_K \cdots J_{l+1} \rVert$ tend exponentiellement vers 0 ou vers l'infini avec $K - l$ : c'est la forme précise du « produit de facteurs » ci-dessus.

## En pratique

- Entraînement : mode inverse. Jacobien d'une fonction à **peu d'entrées et beaucoup de sorties** : mode avant.
- Évaluation et inférence : `torch.no_grad()` ou `torch.inference_mode()`, pour ne pas stocker un graphe dont personne ne se sert. Ne pas confondre avec `model.eval()`.
- Mémoire insuffisante en entraînement : réduire le lot, [[Gradient checkpointing|recalculer les activations]], ou passer en [[Mixed precision|précision mixte]] (le *loss scaling* y existe précisément parce que de petits gradients tombent à zéro en fp16).
- Explosion de la perte sur des séquences ou des réseaux profonds : clipper la norme du gradient avant le pas de l'optimiseur.
- Modification en place d'un tenseur nécessaire à la passe arrière : l'erreur du compteur de version est le comportement voulu, pas un bug à contourner.

## Approches voisines & alternatives

- [[Gradient descent]] — ce que le gradient calculé ici alimente.
- [[Adam optimizer]] — consomme le gradient ; sa mémoire (deux moments par paramètre) s'ajoute à celle des activations.
- [[Loss landscape and saddle points]] — la géométrie de la perte, dont la hessienne (accessible par produit hessienne-vecteur) mesure la courbure.
- [[Newton & quasi-Newton]] — les méthodes de second ordre qui exploitent ces produits hessienne-vecteur.
- [[Gradient checkpointing]] — le levier mémoire de la passe arrière.
- [[Mixed precision]] — la passe arrière en fp16/bf16 et son *loss scaling*.
- [[Perceptron et MLP]] — le réseau le plus simple sur lequel la rétropropagation se calcule à la main.
- [[Attribution par gradient]] — réutilise le même moteur, mais dérive par rapport à l'**entrée** plutôt qu'aux poids.
- [[Normalisation et initialisation des réseaux]] — l'autre moitié du problème des gradients qui disparaissent ou explosent.
- [[Méta-apprentissage et few-shot learning]] — MAML différencie à travers une boucle de gradient : le second ordre en usage.
- [[PyTorch]] — `torch.autograd`, graphe dynamique, `torch.func` pour les transformations à la JAX.
- [[JAX]] — `grad`, `jvp`, `vjp`, `jit` comme transformations composables de fonctions pures.
- [[TensorFlow]] et [[Keras]] — l'autre grande pile de différentiation automatique, derrière une API de plus haut niveau.
- **Au-delà de la rétropropagation** : Hinton (2022) propose le *Forward-Forward*, deux passes avant (données positives et négatives) où chaque couche optimise sa propre fonction de « qualité » ; Baydin et al. (2022) proposent des *forward gradients*, un estimateur non biaisé du gradient en une passe avant, avec un entraînement annoncé jusqu'à deux fois plus rapide dans certains cas. Aucun des deux ne remplace la rétropropagation pour l'entraînement courant.

## Pour aller plus loin

- Rumelhart, Hinton & Williams (1986) — [*Learning representations by back-propagating errors*](https://www.nature.com/articles/323533a0), Nature 323, 533-536.
- Baydin, Pearlmutter, Radul & Siskind (2018) — [*Automatic differentiation in machine learning: a survey*](https://arxiv.org/abs/1502.05767), JMLR 18(153), 1-43.
- Hochreiter (1991) — *Untersuchungen zu dynamischen neuronalen Netzen*, thèse de diplôme, TU München.
- Bengio, Simard & Frasconi (1994) — *Learning long-term dependencies with gradient descent is difficult*, IEEE Trans. Neural Networks 5(2), 157-166.
- Pascanu, Mikolov & Bengio (2013) — [*On the difficulty of training Recurrent Neural Networks*](https://arxiv.org/abs/1211.5063).
- Hinton (2022) — [*The Forward-Forward Algorithm: Some Preliminary Investigations*](https://arxiv.org/abs/2212.13345).
- Baydin, Pearlmutter, Syme, Wood & Torr (2022) — [*Gradients without Backpropagation*](https://arxiv.org/abs/2202.08587).
- Documentation PyTorch — [Autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd.html) ; documentation JAX — [The autodiff cookbook](https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html) et [Common gotchas](https://docs.jax.dev/en/latest/notebooks/Common_Gotchas_in_JAX.html).
