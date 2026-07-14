---
galaxie: dev
type: service
nom: Keras
alias: [keras, keras 3, keras3, tf.keras]
pitch: "API de deep learning de haut niveau, multi-backend (Keras 3) — le même code de modèle s'exécute sur JAX, TensorFlow ou PyTorch ; construire, entraîner et exporter un réseau vite, sans s'enfermer dans un framework."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dev/Services/PyTorch Lightning|PyTorch Lightning]]"]
remplace_par: []
status: actif
tags: [deep-learning, gpu]
url_docs: https://keras.io/
url_repo: https://github.com/keras-team/keras
---

# Keras

## Pourquoi

API de **deep learning de haut niveau** centrée sur la productivité : on décrit un réseau couche par couche (`Sequential`, API fonctionnelle, sous-classement de `Model`) et `fit` / `evaluate` / `predict` prennent en charge la boucle d'entraînement. Depuis **Keras 3** (réécriture complète), c'est un framework **multi-backend** : le même code s'exécute au choix sur [[Dev/Services/JAX|JAX]], [[Dev/Services/TensorFlow|TensorFlow]] ou [[Dev/Services/PyTorch|PyTorch]] (OpenVINO en inférence seule), via une couche d'ops portable (`keras.ops`, qui réimplémente l'API NumPy). On choisit le backend par variable d'environnement, sans toucher au modèle.

## Quand l'utiliser

- **Prototyper vite** un réseau standard (vision, séquences, tabulaire) avec une API lisible et stable.
- **Portabilité de backend** : écrire un modèle une fois et le faire tourner sur JAX (TPU, perf), TensorFlow (déploiement) ou PyTorch (écosystème) selon le contexte.
- **Entraînement clés en main** : callbacks, métriques, checkpointing, `fit` multi-GPU sans réécrire la boucle.
- **Export / déploiement** : passerelle vers TF Serving, TF Lite, ONNX selon le backend.

## Quand NE PAS l'utiliser

- Contrôle fin de la boucle d'entraînement ou opérations exotiques → coder directement en [[Dev/Services/PyTorch|PyTorch]] (define-by-run) ou [[Dev/Services/JAX|JAX]].
- Écosystème de modèles pré-entraînés de recherche → [[Dev/Services/HuggingFace|HuggingFace]] (majoritairement PyTorch).
- Rester dans PyTorch tout en factorisant l'ingénierie d'entraînement → [[Dev/Services/PyTorch Lightning|PyTorch Lightning]] (mono-backend).
- Données **tabulaires** → un réseau est rarement le bon choix : [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/Scikit-Learn|Scikit-Learn]].

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add keras` + un backend (`jax`, `tensorflow` ou `torch`). Rien à héberger.
- Le backend porte le calcul GPU/TPU et le passage à l'échelle (distribué délégué : `tf.distribute`, sharding JAX, DDP PyTorch).
- Maintenu par l'équipe Keras (Google). Keras 3 est la version courante ; `tf.keras` reste la variante historique intégrée à TensorFlow.

## Pièges

- **Keras 3 vs Keras 2 / `tf.keras`** : depuis TensorFlow 2.16, `import tensorflow` tire Keras 3 ; du code Keras 2 peut casser (l'ancien comportement vit dans le paquet `tf-keras`).
- Le backend se fixe **avant** d'importer Keras (`KERAS_BACKEND`) ; en changer en cours de session ne prend pas.
- Tout n'est pas portable : appeler directement des ops TensorFlow/PyTorch fait perdre la portabilité — rester sur `keras.ops` pour le multi-backend.

## Alternatives

- [[Dev/Services/PyTorch Lightning|PyTorch Lightning]] — Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code.

Nuance : Keras est une API **multi-backend** complète (définition + entraînement) ; Lightning organise du code **PyTorch** que l'on écrit toujours soi-même.

## Liens

- [[Dev/Services/TensorFlow|TensorFlow]] — backend historique ; Keras en est l'API de haut niveau intégrée.
- [[Dev/Services/JAX|JAX]] — backend visé pour la perf et le TPU.
- [[Dev/Services/PyTorch|PyTorch]] — backend également supporté par Keras 3.
- Doc : https://keras.io/
