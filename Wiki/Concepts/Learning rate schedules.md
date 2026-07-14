---
galaxie: wiki
type: concept
nom: Learning rate schedules
alias: [Learning rate schedules, Planification du taux d'apprentissage, LR schedule, Warmup, Cosine decay, Cyclical learning rate]
categorie: concept/math
domaines: [ml-eng, ai-eng]
tags: [optimization, learning-rate]
---

# Learning rate schedules

## Aperçu

- Le pas $\eta$ de la [[Gradient descent]] est l'hyperparamètre le plus déterminant. Une **planification** le fait varier au fil de l'entraînement : grand au début pour avancer vite, petit à la fin pour se poser.
- Bien réglé, un schedule accélère la convergence et améliore la généralisation ; mal réglé, il fait diverger ou stagner.

## Concepts clés

### Les profils usuels
- **Constant** : référence simple.
- **Step / exponentiel** : on divise $\eta$ par paliers ou en continu.
- **Cosine annealing** : décroissance douce, éventuellement avec **restarts** (repartir haut pour explorer un autre bassin).
- **Warmup** : démarrer très bas et monter progressivement — crucial pour les transformeurs et Adam, dont les estimations de moments sont bruitées au début.
- **1cycle** : montée puis descente du pas sur un seul cycle (Smith).
- **ReduceLROnPlateau** : baisser $\eta$ quand la perte de validation stagne.

### Schedule vs optimiseur adaptatif
- Adam/RMSprop adaptent un pas **par paramètre**, mais un schedule global (warmup + cosine) reste bénéfique par-dessus.

## Les maths, simplement

- Trop grand → l'itération diverge ; trop petit → convergence interminable. Le bon $\eta$ dépend du conditionnement du [[Loss landscape and saddle points|paysage]].
- Cosine : $\eta_t = \eta_{\min} + \tfrac12(\eta_{\max}-\eta_{\min})\big(1+\cos(\pi t/T)\big)$.
- Le warmup évite l'instabilité initiale quand gradients et statistiques d'optimiseur sont encore peu fiables.

## En pratique

- Régler d'abord le pas de base (LR range test), **puis** choisir le profil.
- Défaut solide en deep learning / LLM : **warmup + cosine decay**.
- Entraînement ML classique : **ReduceLROnPlateau** suffit souvent.
- La sélection du profil et de $\eta_{\max}$ relève de l'[[Optimisation d'hyperparamètres]], validée par [[Validation croisée]].
- Outils : `torch.optim.lr_scheduler` (CosineAnnealingLR, OneCycleLR, ReduceLROnPlateau).

## Approches voisines & alternatives

- [[Gradient descent]] — le pas $\eta$ que ces schedules planifient.
- [[Convexity]] — sur problème convexe, un pas décroissant simple garantit déjà la convergence.
- [[Loss landscape and saddle points]] — la géométrie qui dicte le pas à chaque phase.
- [[Optimisation d'hyperparamètres]] — le LR est l'hyperparamètre numéro un à régler.

## Pour aller plus loin

- Loshchilov & Hutter (2017) — *SGDR*: cosine annealing avec restarts.
- Smith (2017) — *Cyclical Learning Rates* et la politique 1cycle.
