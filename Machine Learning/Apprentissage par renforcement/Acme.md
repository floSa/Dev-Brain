---
role: brique
nom: Acme
alias: [acme, dm-acme, deepmind acme]
pitch: "Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022."
categorie: ml/rl
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Stable-Baselines3]]", "[[TF-Agents]]", "[[RLax]]"]
complements: []
tags: [reinforcement-learning]
url_docs: https://dm-acme.readthedocs.io/
url_repo: https://github.com/google-deepmind/acme
---

# Acme

<!-- AUTO:BANDEAU:START -->
> Framework de recherche RL de Google DeepMind (JAX/TF) — composants modulaires (acteurs, learners, replay Reverb) pour prototyper puis distribuer des agents, du single-process au massivement parallèle ; maintenance très ralentie depuis 2022.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-01 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de **recherche** RL de Google DeepMind. Un agent s'y décompose en composants
réutilisables — **acteurs** (interaction avec l'environnement), **learners** (mise à jour des
réseaux), **replay** (via Reverb) — assemblables à l'identique en single-process ou en
distribué via Launchpad : le même agent passe du prototype local à des centaines d'acteurs
parallèles sans réécriture. Il embarque les implémentations de référence des agents DeepMind
(D4PG, MPO, IMPALA, R2D2), principalement en [[JAX]] avec les pertes de [[RLax]],
historiquement aussi en TensorFlow. Le projet est en sommeil : dernière release v0.4.0 en
février 2022, commits sporadiques depuis.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche RL distribuée : scaler la collecte d'expérience (acteurs parallèles, replay Reverb) sans réarchitecturer l'agent | Projet de long terme : la dernière release date de février 2022, aucune compatibilité garantie avec les Python / JAX / TF récents → [[Stable-Baselines3]] |
| Reproduire des agents DeepMind tels que publiés : D4PG, MPO, IMPALA, R2D2 | Reverb (replay) et Launchpad (distribution) ne tournent que sous **Linux** — ni Windows ni macOS natifs |
| Étudier une architecture d'agent : code structuré, pensé comme matériel de référence | Ni zoo d'hyperparamètres ni API `fit`/`predict` : la courbe d'apprentissage est nettement plus raide → [[Stable-Baselines3]] |
| Composer soi-même acteurs, learners et replay plutôt que subir une boucle figée | Environnements au format **dm_env** par défaut : les wrappers vers [[Gymnasium]] sont à prévoir |

## Mise en œuvre

- Installation — `uv add dm-acme` (extras `[jax]`, `[tf]`, `[envs]`) ; épingler tout l'environnement, voire installer depuis le dépôt
- Point d'entrée — import Python : agents assemblés depuis `acme.agents`, boucle d'environnement fournie
- Prérequis — Linux pour Reverb et Launchpad ; [[JAX]] pour les implémentations actuelles
- Exécution — CPU / GPU / TPU via JAX ; du single-process aux centaines d'acteurs parallèles sur le même code d'agent
- Coût — gratuit, Apache-2.0, rien à héberger ; le coût est celui du calcul mobilisé par les acteurs

## Écosystème

### Alternatives

- [[Stable-Baselines3]] — Implémentations fiables et testées d'algorithmes de RL en PyTorch (PPO, A2C, DQN, SAC, TD3, DDPG) — API homogène sur environnements Gymnasium ; la boîte à outils par défaut pour entraîner un agent sans réimplémenter.
- [[TF-Agents]] — Bibliothèque RL officielle de l'écosystème TensorFlow — agents prêts à l'emploi (DQN, PPO, SAC, REINFORCE), drivers et replay buffers sous une API homogène ; l'équivalent TensorFlow de Stable-Baselines3, en déclin avec son écosystème.
- [[RLax]] — Briques mathématiques de RL en pur JAX (DeepMind) — pertes TD, returns, policy gradients, RL distributionnel à composer dans sa propre boucle jit/vmap ; le Lego bas niveau du chercheur, à l'opposé du clé en main de Stable-Baselines3.
- RLlib — RL distribué industriel de l'écosystème Ray (pas encore en fiche).
- CleanRL — implémentations mono-fichier à copier-modifier pour la recherche (pas encore en fiche).

## Ressources

- Documentation — https://dm-acme.readthedocs.io/
- Dépôt — https://github.com/google-deepmind/acme

## Voir aussi

- [[Reinforcement learning]] — la notion du dossier
- [[JAX]] — le backend de calcul des implémentations actuelles
- [[Q-learning and DQN]] · [[Policy gradient]] · [[Actor-Critic methods]] — les familles d'algorithmes couvertes (R2D2, IMPALA, D4PG/MPO)
- [[Comparatif - Reinforcement learning]] — ce qui départage les bibliothèques du dossier
