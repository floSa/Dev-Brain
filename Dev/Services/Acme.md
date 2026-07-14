---
galaxie: dev
type: service
nom: Acme
alias: [acme, dm-acme, deepmind acme]
pitch: "Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/Stable-Baselines3|Stable-Baselines3]]", "[[Dev/Services/TF-Agents|TF-Agents]]", "[[Dev/Services/RLax|RLax]]"]
remplace_par: []
status: actif
tags: [reinforcement-learning]
url_docs: https://dm-acme.readthedocs.io/
url_repo: https://github.com/google-deepmind/acme
---

# Acme

## Pourquoi

Framework de **recherche** RL de Google DeepMind : un agent se décompose en composants réutilisables — **acteurs** (interaction avec l'environnement), **learners** (mise à jour des réseaux), **replay** (via Reverb) — assemblables à l'identique en single-process ou en distribué (via Launchpad). La promesse : le même agent passe du prototype local à des centaines d'acteurs parallèles sans réécriture. Implémentations de référence d'agents DeepMind (D4PG, MPO, IMPALA, R2D2…), principalement en [[Dev/Services/JAX|JAX]] (avec les pertes de [[Dev/Services/RLax|RLax]]), historiquement aussi en TensorFlow.

## Quand l'utiliser

- **Recherche RL distribuée** : scaler la collecte d'expérience (acteurs parallèles + replay Reverb) sans réarchitecturer l'agent.
- **Reproduire des agents DeepMind** : D4PG, MPO, IMPALA, R2D2 et autres, tels que publiés.
- **Étudier une architecture d'agent** : code structuré et lisible, pensé comme matériel de référence.

## Quand NE PAS l'utiliser

- Entraîner vite un agent standard sur un problème classique → [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] (clé en main, maintenu).
- Projet de **long terme** : la maintenance est quasi arrêtée (dernière release v0.4.0 en février 2022, commits sporadiques depuis) — risque réel de dépendances cassées.
- Construire sa propre boucle JAX minimale plutôt qu'adopter un framework → [[Dev/Services/RLax|RLax]] directement.

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add dm-acme` (extras `[jax]`, `[tf]`, `[envs]`). Rien à héberger.
- Distribution via **Launchpad** et replay via **Reverb** — deux dépendances DeepMind **Linux uniquement**.
- **Distributed** par conception : du single-process aux centaines d'acteurs parallèles, sur le même code d'agent.

## Pièges

- **Maintenance très ralentie** : dernière release en 2022, pas de support des versions récentes de Python/JAX/TF garantie — prévoir d'épingler tout l'environnement, voire d'installer depuis le dépôt.
- Reverb et Launchpad ne tournent que sous **Linux** (ni Windows ni macOS natifs).
- Orienté recherche : pas de zoo d'hyperparamètres ni d'API « fit/predict » — la courbe d'apprentissage est nettement plus raide que SB3.
- Environnements au format **dm_env** par défaut ; prévoir les wrappers pour [[Dev/Services/Gymnasium|Gymnasium]].

## Alternatives

- [[Dev/Services/Stable-Baselines3|Stable-Baselines3]] — Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter.
- [[Dev/Services/TF-Agents|TF-Agents]] — Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème.
- [[Dev/Services/RLax|RLax]] — Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3.

Nuance : Acme est le framework **structurant** (composants d'agents distribués), RLax la boîte de briques sans structure imposée. En dehors du brain : RLlib (Ray, RL distribué industriel), CleanRL (implémentations mono-fichier).

## Liens

- [[Dev/Services/RLax|RLax]] — les pertes JAX que les agents Acme consomment.
- [[Dev/Services/JAX|JAX]] — le backend principal des implémentations actuelles.
- [[Reinforcement learning]] — le cadre général.
- [[Q-learning and DQN]] · [[Policy gradient]] · [[Actor-Critic methods]] — les familles d'algorithmes couvertes (R2D2, IMPALA, D4PG/MPO).
- [[Comparatif - Reinforcement learning]] — vue d'ensemble des libs RL.
- Doc : https://dm-acme.readthedocs.io/
