---
role: brique
nom: TensorFlow
alias: [tensorflow, tf, tf.keras]
pitch: "Framework de deep learning de Google — graphe optimisé et déploiement industriel (Serving, Lite, TPU, JS) ; Keras 3 comme API multi-backend de haut niveau."
categorie: ml/apprentissage-profond
famille: paquet
licence_type: open-source
maturite: production
langage: C++/Python
alternatives: ["[[PyTorch]]", "[[JAX]]"]
complements: ["[[Keras]]"]
tags: [deep-learning, gpu, autograd, distributed]
url_docs: https://www.tensorflow.org/
url_repo: https://github.com/tensorflow/tensorflow
---

# TensorFlow

<!-- AUTO:BANDEAU:START -->
> Framework de deep learning de Google — graphe optimisé et déploiement industriel (Serving, Lite, TPU, JS) ; Keras 3 comme API multi-backend de haut niveau.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++/Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-03-06 |
<!-- AUTO:BANDEAU:END -->

## Définition

Le framework de deep learning de Google, pensé dès l'origine pour le **passage en production** : graphe de calcul optimisable, déploiement multi-cibles (serveurs, mobile, navigateur, microcontrôleurs), accélération native **TPU**. Son API de haut niveau est [[Keras]], devenue multi-backend à la version 3 — ce qui déplace la question : on peut garder l'API sans garder TensorFlow. Deux ruptures structurent le code existant et se paient au moment de reprendre un projet : le passage de TF1 (sessions et graphes statiques) à TF2 (eager plus `tf.function`), deux paradigmes qui ne se mélangent pas ; et depuis TF 2.16, `import tensorflow` tire Keras 3, où du code Keras 2 peut casser (l'ancien comportement vit dans le paquet `tf-keras`). Son mindshare en recherche a reculé face à PyTorch, sa place en industrie et sur l'embarqué beaucoup moins.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Mise en production à grande échelle : TF Serving (API d'inférence versionnée), pipelines TFX bout-en-bout | Recherche et prototypage rapides, suivre l'état de l'art → [[PyTorch]], dont l'écosystème et les publications dominent |
| Edge et embarqué : TensorFlow Lite (mobile, microcontrôleurs), TensorFlow.js (navigateur, Node) | Transformations fonctionnelles et compilation XLA pures → [[JAX]] |
| TPU : entraînement et inférence sur les accélérateurs Google Cloud, support de première classe | On ne veut que l'API de haut niveau, sans s'attacher à TF : Keras 3 tourne aussi sur backend [[PyTorch]] ou [[JAX]] |
| API de haut niveau stable pour construire et entraîner vite, backend interchangeable | Données **tabulaires** → [[XGBoost]], [[Scikit-Learn]] |

## Mise en œuvre

- Installation — `uv add tensorflow`, qui installe Keras 3 ; matrice de compatibilité versions ↔ CUDA/cuDNN stricte, à suivre à la lettre
- Point d'entrée — import Python, `import tensorflow as tf` ; cœur C++ sous l'API
- Prérequis — CPU pour apprendre, GPU NVIDIA (CUDA) ou TPU pour entraîner
- Exécution — dans le process appelant ; distribué via `tf.distribute` (multi-GPU, multi-nœuds, TPU pods)
- Coût — gratuit, Apache-2.0 ; la force de l'écosystème est l'outillage de déploiement (Serving, Lite, JS, TFX), pas la licence

## Écosystème

### Alternatives

- [[PyTorch]] — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche.
- [[JAX]] — Calcul numérique et différentiation automatique sur accélérateurs — NumPy compilé par XLA via jit/grad/vmap/pmap (GPU/TPU) ; socle des gros entraînements de recherche.

### Compléments

- [[Keras]] — API de deep learning de haut niveau, multi-backend (Keras 3) — le même code de modèle s'exécute sur JAX, TensorFlow ou PyTorch ; construire, entraîner et exporter un réseau vite, sans s'enfermer dans un framework. — son API de haut niveau, et le backend par défaut de Keras.

## Ressources

- Documentation — https://www.tensorflow.org/
- Dépôt — https://github.com/tensorflow/tensorflow

## Voir aussi

- [[Apprentissage profond]] — le hub du domaine
- [[TensorFlow Serving]] — le serveur d'inférence dédié aux `SavedModel` TensorFlow/Keras
- [[HuggingFace]] — hub de modèles ; le support natif TensorFlow y est désormais minoritaire, `transformers` étant passé PyTorch-first
