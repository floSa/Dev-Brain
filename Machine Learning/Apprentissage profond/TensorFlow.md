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
complements: []
tags: [deep-learning, gpu, autograd, distributed]
url_docs: https://www.tensorflow.org/
url_repo: https://github.com/tensorflow/tensorflow
---

# TensorFlow

## Pourquoi

Framework de **deep learning** de Google, pensé dès l'origine pour le **passage en production** : graphe de calcul optimisable, déploiement multi-cibles (serveurs, mobile, navigateur, microcontrôleurs), accélération native **TPU**. L'API de haut niveau est **Keras**, qui depuis Keras 3 est **multi-backend** (TensorFlow, mais aussi [[JAX]] et [[PyTorch]]). TF reste très présent en industrie et sur l'embarqué, même si son mindshare en recherche a reculé face à PyTorch.

## Quand l'utiliser

- **Mise en production à grande échelle** : TF Serving (API d'inférence versionnée), pipelines TFX bout-en-bout.
- **Edge & embarqué** : TensorFlow Lite (mobile, microcontrôleurs), TensorFlow.js (navigateur / Node).
- **TPU** : entraînement et inférence sur les accélérateurs Google Cloud, support de première classe.
- **API haut niveau stable** : Keras pour construire/entraîner vite, avec la possibilité de changer de backend.

## Quand NE PAS l'utiliser

- Recherche et prototypage rapides, suivre l'état de l'art → [[PyTorch]] (écosystème et publications dominants).
- Transformations fonctionnelles et compilation XLA pures → [[JAX]].
- Juste l'API Keras sans s'attacher à TF → Keras 3 tourne aussi sur backend [[PyTorch]] ou [[JAX]].
- Données **tabulaires** → [[XGBoost]], [[Scikit-Learn]].

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add tensorflow` (installe Keras 3).
- Cœur C++ sous API Python ; CPU, GPU NVIDIA (CUDA), TPU.
- Outils de déploiement : Serving, Lite, JS, TFX — c'est la force historique de l'écosystème.
- Distribué via `tf.distribute` (multi-GPU, multi-nœuds, TPU pods).

## Pièges

- **Keras 3 vs `tf.keras`** : depuis TF 2.16, `pip install tensorflow` installe Keras 3 ; du code Keras 2 peut casser (l'ancien comportement vit dans le paquet `tf-keras`).
- Compatibilité versions ↔ CUDA/cuDNN stricte : suivre la matrice officielle.
- Migration mentale TF1 (sessions/graphes statiques) → TF2 (eager + `tf.function`) : ne pas mélanger les deux paradigmes.

## Alternatives

- [[PyTorch]] — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche.
- [[JAX]] — Calcul numérique et différentiation automatique sur accélérateurs — NumPy compilé par XLA via jit/grad/vmap/pmap (GPU/TPU) ; socle des gros entraînements de recherche.

## Liens

- [[HuggingFace]] — hub de modèles ; le support natif TensorFlow y est désormais minoritaire (transformers est passé PyTorch-first).
- [[TensorFlow Serving]] — serveur d'inférence dédié aux modèles TensorFlow/Keras (`SavedModel`).
- [[Keras]] — son API de haut niveau (Keras 3, multi-backend) ; backend TensorFlow par défaut.
- Doc : https://www.tensorflow.org/ · Keras : https://keras.io/
