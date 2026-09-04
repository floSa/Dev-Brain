---
role: brique
nom: JAX
alias: [jax, google-jax, jax-ml]
pitch: "Calcul numérique et différentiation automatique sur accélérateurs — NumPy compilé par XLA via jit/grad/vmap/pmap (GPU/TPU) ; socle des gros entraînements de recherche."
categorie: ml/apprentissage-profond
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[PyTorch]]", "[[TensorFlow]]"]
complements: ["[[Keras]]"]
tags: [deep-learning, gpu, autograd, array]
url_docs: https://docs.jax.dev/
url_repo: https://github.com/jax-ml/jax
---

# JAX

<!-- AUTO:BANDEAU:START -->
> Calcul numérique et différentiation automatique sur accélérateurs — NumPy compilé par XLA via jit/grad/vmap/pmap (GPU/TPU) ; socle des gros entraînements de recherche.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Une API quasi identique à celle de [[numpy]], rendue **composable et accélérable** par un jeu de transformations de fonctions : `grad` (différentiation automatique, forward et reverse, ordres supérieurs), `jit` (compilation XLA en noyaux fusionnés), `vmap` (vectorisation automatique), `pmap` et `shard_map` (parallélisme multi-appareils). Le prix de cette composition est un **style fonctionnel imposé** : fonctions pures, tableaux immuables (pas d'assignation en place, mais `x.at[idx].set(...)`), aléa explicite par clés `PRNGKey` à découper plutôt qu'un état global, et tout ce qui passe sous `jit` doit être **traçable** — une valeur Python qui branche le flux de contrôle devient une erreur de trace, à réécrire en `jax.lax.cond` ou en formes statiques. C'est ce qui le rend inconfortable pour du code impératif à effets de bord, et taillé pour le scaling.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche perf-critique : différentiation d'ordre supérieur, jacobiens et hessiens, méthodes scientifiques | Écosystème prêt à l'emploi, modèles pré-entraînés, prototypage impératif → [[PyTorch]] |
| TPU et très grands entraînements : `pmap` / `shard_map` combinés à `jit` | Déploiement industriel mobile / edge / serving clés en main → [[TensorFlow]] |
| Deep learning via l'écosystème : réseaux avec Flax ou Haiku, optimiseurs avec Optax | Effets de bord, état mutable, boucles Python dynamiques : le style fonctionnel et `jit` y sont contraignants |
| Code numérique vectorisé qu'on veut compiler sans réécrire en C++ | Données tabulaires classiques → [[Scikit-Learn]] |

## Mise en œuvre

- Installation — `uv add jax`, avec la roue correspondant à la cible (CPU, GPU, TPU)
- Point d'entrée — import Python, `import jax.numpy as jnp` puis les transformations `jit` / `grad` / `vmap`
- Prérequis — rien de lourd en CPU ; GPU NVIDIA ou TPU Google pour le passage à l'échelle
- Exécution — compilée par **XLA** (OpenXLA) dans le process appelant ; multi-appareils et multi-nœuds par sharding
- Coût — gratuit, Apache-2.0 ; développé par Google avec des contributions NVIDIA et communautaires

Versionné en 0.x : l'amont prévient « expect sharp edges », les dépréciations surviennent entre versions mineures et la version s'épingle — mais le cœur `grad` / `jit` / `vmap` est éprouvé à très grande échelle.

## Écosystème

### Alternatives

- [[PyTorch]] — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche.
- [[TensorFlow]] — Framework de deep learning de Google — graphe optimisé et déploiement industriel (Serving, Lite, TPU, JS) ; Keras 3 comme API multi-backend de haut niveau.

### Compléments

- [[Keras]] — API de deep learning de haut niveau, multi-backend (Keras 3) — le même code de modèle s'exécute sur JAX, TensorFlow ou PyTorch ; construire, entraîner et exporter un réseau vite, sans s'enfermer dans un framework. — le backend JAX est celui qu'on choisit pour la perf et le TPU.

## Ressources

- Documentation — https://docs.jax.dev/
- Dépôt — https://github.com/jax-ml/jax

## Voir aussi

- [[Apprentissage profond]] — le hub du domaine
- [[numpy]] — l'API de référence dont JAX reprend la sémantique, sur accélérateurs et en immuable
- [[HuggingFace]] — hub de modèles ; le backend JAX/Flax y est historiquement supporté, désormais minoritaire face à PyTorch
