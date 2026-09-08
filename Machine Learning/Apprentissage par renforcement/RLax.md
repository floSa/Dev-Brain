---
role: brique
nom: RLax
alias: [rlax, rl-ax, deepmind rlax]
pitch: "Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3."
categorie: ml/rl
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Stable-Baselines3]]", "[[Acme]]", "[[TF-Agents]]"]
complements: []
tags: [reinforcement-learning]
url_docs: https://rlax.readthedocs.io/
url_repo: https://github.com/google-deepmind/rlax
---

# RLax

<!-- AUTO:BANDEAU:START -->
> Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-06-12 |
<!-- AUTO:BANDEAU:END -->

## Définition

Pas un framework d'agents : une collection de **fonctions mathématiques pures** pour
construire des agents RL en [[JAX]]. Pertes TD (`q_learning`, `double_q_learning`,
`td_lambda`), calculs de retours (n-step, λ-returns), gradients de politique (REINFORCE,
surrogate clippé de PPO), RL distributionnel (C51, quantile), V-trace, transformations de
valeurs. Tout est composable avec `jit` / `vmap` / `grad` : RLax fournit les briques validées
et testées, la boucle d'entraînement, le réseau, le replay et l'exploration restent à la
charge de l'utilisateur. Les fonctions étant **sans état**, une erreur de plomberie — mauvais
stop-gradient, mauvaise cible — passe silencieusement, d'où l'usage de Chex pour les tester.
Membre de l'écosystème JAX de DeepMind, avec Optax, Flax/Haiku et Chex.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche : implémenter un agent custom ou une variante d'algorithme sans réécrire — ni risquer de fausser — les pertes de référence | Tout reste à écrire : ni agents, ni environnements, ni replay, ni boucle d'entraînement → [[Stable-Baselines3]] |
| Boucle d'entraînement JAX maison où chaque pièce doit être contrôlée et compilée (`jit`, `vmap` sur les batchs, `pmap` multi-device) |  |
| Pédagogie : des fonctions courtes, lisibles, qui collent aux équations des papiers | Équipe sur l'écosystème PyTorch sans bagage JAX : le coût d'entrée ne se justifie pas pour du RL applicatif |
| | Conventions de **shapes et de signes** à lire attentivement — perte à minimiser contre objectif à maximiser, batch contre unbatched avec `vmap` attendu |
| | Rythme de maintenance lent : toujours en 0.1.x depuis 2020, pas de presse à intégrer les algorithmes récents |

## Mise en œuvre

- Installation — `uv add rlax`
- Point d'entrée — import Python : fonctions pures à appeler dans sa propre boucle, aucune classe d'agent
- Prérequis — [[JAX]] et son écosystème (Optax, Flax ou Haiku, Chex pour les tests)
- Exécution — CPU / GPU / TPU via JAX ; single-node en soi, la distribution (`pmap`, multi-host) relève du code utilisateur
- Coût — gratuit, Apache-2.0, rien à héberger

## Écosystème

### Alternatives

- [[Stable-Baselines3]] — Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter.
- [[Acme]] — Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022.
- [[TF-Agents]] — Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème.
- CleanRL — agents mono-fichier à copier-modifier (pas encore en fiche).

## Ressources

- Documentation — https://rlax.readthedocs.io/
- Dépôt — https://github.com/google-deepmind/rlax

## Voir aussi

- [[Reinforcement learning]] — la notion du dossier
- [[JAX]] — le socle de calcul (`jit`, `vmap`, `grad`)
- [[Q-learning and DQN]] — les pertes TD et distributionnelles fournies
- [[Policy gradient]] · [[PPO]] — REINFORCE et le surrogate clippé, prêts à composer
- [[Actor-Critic methods]] — pertes acteur et critique séparées, à assembler
- [[Comparatif - Reinforcement learning]] — ce qui départage les bibliothèques du dossier
