---
galaxie: dev
type: service
nom: JAX
alias: [jax, google-jax, jax-ml]
pitch: "Calcul numérique et différentiation automatique sur accélérateurs — NumPy compilé par XLA via jit/grad/vmap/pmap (GPU/TPU) ; socle des gros entraînements de recherche."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/PyTorch|PyTorch]]", "[[Dev/Services/TensorFlow|TensorFlow]]"]
remplace_par: []
status: actif
tags: [deep-learning, gpu, autograd, array]
url_docs: https://docs.jax.dev/
url_repo: https://github.com/jax-ml/jax
---

# JAX

## Pourquoi

JAX expose une API quasi identique à [[Dev/Services/numpy|numpy]], mais rend les programmes **composables et accélérables** par un jeu de transformations de fonctions : `grad` (différentiation automatique, forward/reverse, ordres supérieurs), `jit` (compilation XLA en noyaux fusionnés), `vmap` (vectorisation/batching automatique), `pmap` / `shard_map` (parallélisme multi-appareils). Le tout vise GPU et **TPU** via XLA. Approche **fonctionnelle** (fonctions pures, tableaux immuables) qui se prête à la composition et au scaling — d'où son adoption pour l'entraînement de gros modèles en recherche.

## Quand l'utiliser

- **Recherche perf-critique** : différentiation d'ordre supérieur, jacobiens/hessiens, méthodes scientifiques (physique, optimisation).
- **TPU et très grands entraînements** : `pmap`/`shard_map` + `jit` pour le parallélisme de données et de modèle.
- **Deep learning via l'écosystème** : réseaux avec Flax ou Haiku, optimiseurs avec Optax — JAX est le cœur, les libs ajoutent les couches.
- **Code numérique vectorisé** qu'on veut compiler sans réécrire en C++.

## Quand NE PAS l'utiliser

- Écosystème prêt à l'emploi, modèles pré-entraînés, prototypage impératif → [[Dev/Services/PyTorch|PyTorch]].
- Déploiement industriel mobile / edge / serving clés en main → [[Dev/Services/TensorFlow|TensorFlow]].
- Besoin d'effets de bord / état mutable / boucles Python dynamiques : le style fonctionnel et `jit` y sont contraignants.
- Données tabulaires classiques → [[Dev/Services/Scikit-Learn|Scikit-Learn]].

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add jax` (roues spécifiques CPU/GPU/TPU).
- Pur Python compilé par **XLA** (OpenXLA) ; CPU, GPU NVIDIA, TPU Google.
- Développé par Google avec contributions NVIDIA/communauté. Versionné en 0.x : API encore mouvante, l'amont prévient « expect sharp edges » — mais le cœur (grad/jit/vmap) est éprouvé à très grande échelle.

## Pièges

- **Tableaux immuables** : pas d'assignation en place, utiliser `x.at[idx].set(...)`.
- Tout ce qui passe sous `jit` doit être **traçable** : les valeurs Python branchant le flux de contrôle deviennent des erreurs de trace (`jax.lax.cond`, formes statiques).
- Reproductibilité : l'aléa est **explicite** via des clés `PRNGKey` à découper (`split`), pas d'état global comme NumPy.
- API 0.x : des dépréciations surviennent entre versions mineures, épingler la version.

## Alternatives

- [[Dev/Services/PyTorch|PyTorch]] — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche.
- [[Dev/Services/TensorFlow|TensorFlow]] — Framework de deep learning de Google — graphe optimisé et déploiement industriel (Serving, Lite, TPU, JS) ; Keras 3 comme API multi-backend de haut niveau.

## Liens

- [[Dev/Services/numpy|numpy]] — API de référence dont JAX reprend la sémantique (sur accélérateurs, immuable).
- [[Dev/Services/HuggingFace|HuggingFace]] — hub de modèles ; backend JAX/Flax historiquement supporté (désormais minoritaire face à PyTorch).
- [[Dev/Services/Keras|Keras]] — API de haut niveau multi-backend : Keras 3 tourne sur backend JAX (TPU, perf).
- Doc : https://docs.jax.dev/
