---
galaxie: dev
type: service
nom: RLax
alias: [rlax, rl-ax, deepmind rlax]
pitch: "Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Stable-Baselines3|Stable-Baselines3]]", "[[Dev/Services/Acme|Acme]]", "[[Dev/Services/TF-Agents|TF-Agents]]"]
remplace_par: []
status: actif
tags: [reinforcement-learning]
url_docs: https://rlax.readthedocs.io/
url_repo: https://github.com/google-deepmind/rlax
---

# RLax

## Pourquoi

Pas un framework d'agents : une bibliothèque de **fonctions mathématiques pures** pour construire des agents RL en [[Dev/Services/JAX|JAX]]. Pertes TD (`q_learning`, `double_q_learning`, `td_lambda`), calculs de retours (n-step, λ-returns), gradients de politique (REINFORCE, surrogate clippé de PPO), RL distributionnel (C51, quantile), V-trace, transformations de valeurs… Tout est composable avec `jit` / `vmap` / `grad` : la boucle d'entraînement, le réseau et le replay restent à la charge de l'utilisateur ; RLax fournit les briques validées et testées. Membre de l'écosystème JAX de DeepMind (avec Optax, Flax/Haiku, Chex).

## Quand l'utiliser

- **Recherche** : implémenter un agent custom ou une variante d'algorithme sans réécrire (ni risquer de fausser) les pertes de référence.
- Boucle d'entraînement **JAX maison** où chaque pièce doit être contrôlée et compilée (jit, vmap sur les batchs, pmap multi-device).
- **Pédagogie** : les fonctions sont courtes, lisibles, et collent aux équations des papiers.

## Quand NE PAS l'utiliser

- Entraîner un agent standard sans tout écrire soi-même → [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] : RLax ne fournit ni agents, ni environnements, ni replay, ni boucle.
- Vouloir une **structure** d'agent distribué prête (acteurs/learners/replay) → [[Dev/Services/Acme|Acme]], qui consomme justement RLax.
- Équipe sur l'écosystème PyTorch sans bagage JAX : le coût d'entrée JAX ne se justifie pas pour du RL applicatif.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add rlax`. Rien à héberger.
- CPU / GPU / TPU via [[Dev/Services/JAX|JAX]] ; **single-node** en soi — la distribution éventuelle (pmap, multi-host) relève du code utilisateur.
- Maintenance **minimale mais réelle** : toujours en 0.1.x depuis 2020, quelques releases espacées (0.1.8 en septembre 2025). Le périmètre — petites fonctions pures — vieillit bien malgré le rythme lent.

## Pièges

- Tout reste à écrire : target networks, exploration, replay, vectorisation des environnements — RLax n'est que la couche mathématique.
- Conventions de **shapes et de signes** des pertes à lire attentivement (loss vs objectif à maximiser, batch vs unbatched — `vmap` attendu).
- Rythme de maintenance lent : pas de presse à intégrer les algorithmes les plus récents.
- Fonctions pures sans état : les erreurs de plomberie (mauvais stop-gradient, mauvaise cible) sont silencieuses — tester avec Chex.

## Alternatives

- [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] — Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter.
- [[Dev/Services/Acme|Acme]] — Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022.
- [[Dev/Services/TF-Agents|TF-Agents]] — Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème.

Nuance : RLax est le **Lego** (fonctions à assembler), SB3/TF-Agents le **clé en main** (agents complets), Acme l'**architecture** (composants distribués). En dehors du brain : CleanRL (agents mono-fichier à copier-modifier).

## Liens

- [[Dev/Services/JAX|JAX]] — le socle de calcul (jit, vmap, grad).
- [[Dev/Services/Acme|Acme]] — le framework d'agents DeepMind construit sur ces briques.
- [[Reinforcement learning]] — le cadre général.
- [[Q-learning and DQN]] — les pertes TD et distributionnelles fournies.
- [[Policy gradient]] · [[PPO]] — REINFORCE et le surrogate clippé, prêts à composer.
- [[Actor-Critic methods]] — pertes acteur et critique séparées, à assembler.
- [[Comparatif - Reinforcement learning]] — vue d'ensemble des libs RL.
- Doc : https://rlax.readthedocs.io/
