---
role: brique
nom: Stable-Baselines3
alias: [SB3, stable-baselines3, stable baselines 3, sb3]
pitch: "Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter."
categorie: ml/rl
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Acme]]", "[[TF-Agents]]", "[[RLax]]"]
complements: ["[[Gymnasium]]"]
tags: [reinforcement-learning, deep-learning]
url_docs: https://stable-baselines3.readthedocs.io/
url_repo: https://github.com/DLR-RM/stable-baselines3
---

# Stable-Baselines3

<!-- AUTO:BANDEAU:START -->
> Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Collection d'**implémentations de référence** d'algorithmes de [[Reinforcement learning|RL]] en
[[PyTorch]], pensées pour être fiables et reproductibles : code testé, couvert, documenté, et
surtout accompagné d'**hyperparamètres réglés par algorithme** — le « zoo ». C'est ce zoo, plus
que les valeurs par défaut, qui fait la différence de résultat. On instancie un algorithme
(`PPO`, `DQN`…), on lui passe un environnement [[Gymnasium]], puis `learn()` et `predict()`
font le reste, sur une API volontairement proche de scikit-learn. Le cœur couvre PPO, A2C,
DQN, SAC, TD3 et DDPG ; **SB3-Contrib** ajoute QR-DQN, TQC, TRPO, RecurrentPPO, Maskable PPO,
ARS et CrossQ. Successeur PyTorch de Stable Baselines, lui-même fork d'OpenAI Baselines.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Entraîner un agent sans réimplémenter : PPO, A2C, DQN, SAC, TD3, DDPG au cœur, variantes dans SB3-Contrib | RL **distribué à grande échelle** (milliers d'acteurs) : la parallélisation est celle des environnements vectorisés (`VecEnv`), pas un entraînement multi-nœuds → [[Acme]], ou RLlib hors brain |
| Baseline solide pour démarrer ou comparer un projet de contrôle, robotique, jeux | Recherche sur un algorithme **nouveau** ou très custom : le cadre impose sa boucle → [[RLax]] pour composer soi-même, ou une implémentation mono-fichier |
| Reproductibilité : hyperparamètres documentés (RL Baselines3 Zoo), seeds, évaluation standardisée | Post-training **RL des LLM** (RLHF, GRPO) : hors périmètre de la bibliothèque, qui vise le contrôle et les jeux |
| | Migration **Gym → Gymnasium** : les versions récentes attendent l'API [[Gymnasium]] (`terminated` / `truncated`), un code figé sur l'ancien `gym` ne passe pas tel quel |

## Mise en œuvre

- Installation — `uv add stable-baselines3` (Python 3.10+) ; `sb3-contrib` pour les variantes
- Point d'entrée — API Python type scikit-learn : instancier l'algorithme, `learn()`, `predict()` ; partir du zoo plutôt que des défauts
- Prérequis — un environnement [[Gymnasium]] ; vectoriser (`VecEnv`) et normaliser (`VecNormalize`) sous peine d'apprentissage lent ou instable
- Exécution — single-node, CPU ou GPU via [[PyTorch]] ; parallélisme par environnements vectorisés
- Coût — gratuit, MIT, rien à héberger ; maintenu par le DLR-RM (German Aerospace Center)

## Écosystème

### Alternatives

- [[Acme]] — Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022.
- [[TF-Agents]] — Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème.
- [[RLax]] — Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3.
- RLlib — RL distribué industriel de l'écosystème Ray (pas encore en fiche).
- CleanRL — implémentations mono-fichier pour la recherche (pas encore en fiche).
- Tianshou — bibliothèque RL PyTorch modulaire (pas encore en fiche).

### Compléments

- [[Gymnasium]] — Standard d'API pour les environnements de RL à agent unique (successeur d'OpenAI Gym, par la Farama Foundation) — interface reset/step uniforme + environnements de référence (classic control, Box2D, MuJoCo, Atari) ; le contrat commun entre agents et environnements — l'API d'environnements sur laquelle SB3 entraîne ses agents.

## Ressources

- Documentation — https://stable-baselines3.readthedocs.io/
- Dépôt — https://github.com/DLR-RM/stable-baselines3

## Voir aussi

- [[Reinforcement learning]] — la notion du dossier : agent, politique, récompense
- [[PyTorch]] — le framework de calcul sous-jacent
- [[PPO]] — l'algorithme on-policy phare de SB3
- [[Q-learning and DQN]] — la famille basée valeur (`DQN`, `QR-DQN`)
- [[Actor-Critic methods]] — socle de `A2C`, `SAC`, `TD3`, `DDPG`
- [[Comparatif - Reinforcement learning]] — ce qui départage les bibliothèques du dossier
