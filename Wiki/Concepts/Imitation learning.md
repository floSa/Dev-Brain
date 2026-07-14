---
galaxie: wiki
type: concept
nom: Imitation learning
alias: [imitation learning, apprentissage par imitation, behavioral cloning, BC, learning from demonstration, inverse RL, IRL, GAIL]
categorie: concept/rl
domaines: [ml-eng, ai-eng]
tags: [reinforcement-learning, imitation-learning, supervised]
---

# Imitation learning

## Aperçu

- Apprendre une politique **à partir de démonstrations d'expert** plutôt que d'une récompense : on observe des trajectoires « état → action » jugées bonnes et on cherche à les reproduire.
- Utile quand la **récompense est difficile à spécifier** mais qu'on sait **montrer** le comportement voulu : conduite, robotique, et — côté LLM — le [[SFT]], qui est exactement un clonage des réponses de référence.

## Concepts clés

### Behavioral cloning (BC)
- L'approche la plus directe : traiter l'imitation comme de l'**apprentissage supervisé**. Chaque état est une entrée, l'action de l'expert est l'étiquette ; on entraîne $\pi_\theta(a\mid s)$ par classification/régression.
- Simple et stable, mais souffre du **compounding error** : une petite erreur amène l'agent dans un état **jamais montré** par l'expert, où sa prédiction est encore pire — les erreurs se cumulent et la trajectoire dérive. C'est une violation de l'hypothèse i.i.d. (les états visités dépendent de la politique).

### DAgger — corriger la dérive
- *Dataset Aggregation* : faire rouler la politique courante, puis **demander à l'expert** quelle action il aurait prise **sur les états réellement visités**, et ré-entraîner sur le dataset agrégé.
- Résout le compounding error en couvrant la distribution d'états induite par l'agent — au prix d'un **expert disponible en boucle** (annotation coûteuse).

### Inverse RL (IRL) — récupérer la récompense
- Au lieu de copier les actions, **inférer la fonction de récompense** que l'expert semble optimiser, puis faire du RL classique dessus.
- Avantage : généralise mieux (on apprend l'**intention**, pas le geste) ; inconvénient : mal posé (plusieurs récompenses expliquent le même comportement) et coûteux (une boucle RL imbriquée).
- **GAIL** (*Generative Adversarial Imitation Learning*) court-circuite l'IRL : un **discriminateur** apprend à distinguer trajectoires de l'agent vs de l'expert, et sert de signal (façon GAN) à un [[Policy gradient|gradient de politique]].

## Les maths, simplement

- Behavioral cloning : $\min_\theta\;\mathbb{E}_{(s,a)\sim\mathcal{D}_{\text{exp}}}\big[-\log \pi_\theta(a\mid s)\big]$ — maximum de vraisemblance des actions de l'expert. Strictement de la classification supervisée.
- Compounding error : pour une erreur par pas $\varepsilon$ sur un horizon $T$, le regret de BC croît en $O(\varepsilon T^2)$ (vs $O(\varepsilon T)$ pour DAgger) — d'où la dérive quadratique sur les longues trajectoires.

## En pratique

- **BC d'abord** : si l'on a beaucoup de démonstrations propres et des épisodes courts, le clonage suffit souvent et c'est imbattable de simplicité.
- Passer à **DAgger** si la dérive apparaît et qu'un expert reste interrogeable ; à **IRL/GAIL** si l'on veut généraliser hors des démonstrations ou transférer l'intention.
- Souvent combiné au RL : **initialiser** par BC puis affiner par RL (le SFT avant le [[RL for LLMs|RL]] pour les LLM en est l'exemple canonique).
- Pièges : démonstrations de qualité inégale, états sous-couverts (compounding error), et le fait que l'imitation **plafonne au niveau de l'expert** (sans dépassement, contrairement au RL pur).

## Approches voisines & alternatives

- [[Reinforcement learning]] — l'alternative quand on a une récompense plutôt que des démonstrations ; l'imitation s'en passe.
- [[Offline RL]] — comme l'imitation, apprend sans interaction ; mais raisonne sur la **valeur** des actions, là où le behavioral cloning copie sans juger.
- [[Reward modeling]] — l'IRL en est un cousin : récupérer une récompense à partir de comportements observés (ici l'expert, là des préférences).
- [[Policy gradient]] — le moteur d'optimisation derrière GAIL et l'affinage RL post-imitation.
- [[SFT]] — le fine-tuning supervisé des LLM **est** du behavioral cloning sur des réponses de référence.

## Pour aller plus loin

- Pomerleau (1988) — *ALVINN* (le behavioral cloning historique, conduite autonome).
- Ross et al. (2011) — *DAgger* (analyse du compounding error et correction).
- Ng & Russell (2000) — *Algorithms for Inverse Reinforcement Learning*.
- Ho & Ermon (2016) — *Generative Adversarial Imitation Learning (GAIL)*.
