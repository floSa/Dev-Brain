---
galaxie: wiki
type: concept
nom: Adam optimizer
alias: [Adam, AdamW, adaptive moment estimation, RMSprop, Adagrad, optimiseur adaptatif]
categorie: concept/dl
domaines: [data-sci, ml-eng]
tags: [optimization, gradient-descent, deep-learning, learning-rate]
---

# Adam optimizer

## Aperçu

- Variante adaptative de la [[Gradient descent|descente de gradient]] qui combine deux idées : le **momentum** (moyenne mobile des gradients) et un **pas par paramètre** mis à l'échelle par la taille récente des gradients.
- C'est l'**optimiseur par défaut** du deep learning : robuste au choix du pas, peu de réglage, convergence rapide sur des surfaces de perte bruitées et mal conditionnées.

## Concepts clés

### Les deux moments
- **Premier moment** $m_t$ : EMA du gradient → direction lissée (momentum).
- **Second moment** $v_t$ : EMA du gradient **au carré** → estime l'amplitude par paramètre.
- **Correction de biais** : $m_t, v_t$ démarrent à zéro, donc biaisés vers 0 ; on les corrige ($\hat{m}, \hat{v}$) pour ne pas sous-estimer les premiers pas.

### Le pas adaptatif par paramètre
- Chaque paramètre reçoit un pas effectif $\eta\,\hat{m}_t / (\sqrt{\hat{v}_t}+\varepsilon)$ : grand là où les gradients sont petits et stables, prudent là où ils sont grands et bruités. D'où la faible sensibilité au [[Learning rate schedules|taux d'apprentissage]] global.

### AdamW : le weight decay découplé
- L'Adam d'origine mélange régularisation L2 et pas adaptatif, ce qui affaiblit la [[Régularisation]]. **AdamW** applique le *weight decay* **séparément** de l'étape adaptative — c'est le standard de fait pour entraîner les transformeurs.

## Les maths, simplement

- $m_t = \beta_1 m_{t-1} + (1-\beta_1)\,g_t$ ; $v_t = \beta_2 v_{t-1} + (1-\beta_2)\,g_t^2$.
- Correction : $\hat{m}_t = m_t/(1-\beta_1^t)$, $\hat{v}_t = v_t/(1-\beta_2^t)$.
- Mise à jour : $\theta_{t+1} = \theta_t - \eta\,\hat{m}_t/(\sqrt{\hat{v}_t}+\varepsilon)$. Défauts usuels : $\beta_1=0.9$, $\beta_2=0.999$, $\varepsilon=10^{-8}$.

## En pratique

- Point de départ classique : $\eta \approx 3\!\times\!10^{-4}$, souvent couplé à un [[Learning rate schedules|schedule]] (warmup + cosine) pour les transformeurs.
- **Coût mémoire** : Adam stocke $m$ et $v$, soit $\approx 2\times$ le nombre de paramètres en plus — non négligeable pour les gros modèles (d'où 8-bit Adam, [[Distillation]] et [[Quantization]] côté déploiement).
- Sur la vision, **SGD + momentum** bien réglé **généralise** parfois mieux qu'Adam ; tester les deux quand la généralisation prime.
- Outils : `torch.optim.Adam` / `AdamW`, `optax.adam`.

## Approches voisines & alternatives

- [[Gradient descent]] — la méthode de base dont Adam est une variante adaptative à pas par paramètre.
- [[Learning rate schedules]] — la planification du pas $\eta$, complémentaire de l'adaptativité d'Adam.
- [[Loss landscape and saddle points]] — la géométrie que momentum et mise à l'échelle aident à traverser.
- [[Newton & quasi-Newton]] — autre manière d'exploiter la courbure ; $\sqrt{\hat{v}}$ d'Adam en est une approximation diagonale bon marché.
- [[Convexity]] — cadre où les garanties de convergence sont les plus nettes.

## Pour aller plus loin

- Kingma & Ba (2014) — *Adam: A Method for Stochastic Optimization*.
- Loshchilov & Hutter (2017) — *Decoupled Weight Decay Regularization* (AdamW).
- Reddi et al. (2018) — *On the Convergence of Adam and Beyond* (AMSGrad).
