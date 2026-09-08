---
role: brique
nom: Keras
alias: [keras, keras 3, keras3, tf.keras]
pitch: "API de deep learning de haut niveau, multi-backend (Keras 3) — le même code de modèle s'exécute sur JAX, TensorFlow ou PyTorch ; construire, entraîner et exporter un réseau vite, sans s'enfermer dans un framework."
categorie: ml/apprentissage-profond
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[PyTorch Lightning]]"]
complements: ["[[PyTorch]]", "[[TensorFlow]]", "[[JAX]]"]
tags: [deep-learning, gpu]
url_docs: https://keras.io/
url_repo: https://github.com/keras-team/keras
---

# Keras

<!-- AUTO:BANDEAU:START -->
> API de deep learning de haut niveau, multi-backend (Keras 3) — le même code de modèle s'exécute sur JAX, TensorFlow ou PyTorch ; construire, entraîner et exporter un réseau vite, sans s'enfermer dans un framework.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-07-29 |
<!-- AUTO:BANDEAU:END -->

## Définition

Une API de deep learning centrée sur la productivité : on décrit un réseau couche par couche (`Sequential`, API fonctionnelle, sous-classement de `Model`) et `fit` / `evaluate` / `predict` prennent en charge la boucle d'entraînement, les callbacks, les métriques et le checkpointing. Depuis **Keras 3** (réécriture complète), le même code s'exécute au choix sur [[JAX]], [[TensorFlow]] ou [[PyTorch]] — OpenVINO en inférence seule — grâce à une couche d'ops portable, `keras.ops`, qui réimplémente l'API NumPy. Deux conséquences dictent l'usage : le backend se fixe **avant** l'import (`KERAS_BACKEND`) et n'en change pas en cours de session ; et la portabilité ne survit pas à un appel direct aux ops du backend — rester sur `keras.ops` en est le prix. Le calcul GPU/TPU et le passage à l'échelle restent délégués au backend (`tf.distribute`, sharding JAX, DDP PyTorch).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Prototyper vite un réseau standard (vision, séquences, tabulaire) avec une API lisible et stable | Contrôle fin de la boucle d'entraînement ou opérations exotiques → coder directement en [[PyTorch]] (define-by-run) ou [[JAX]] |
| Portabilité de backend : écrire un modèle une fois, le faire tourner sur [[JAX]] (TPU), [[TensorFlow]] (déploiement) ou [[PyTorch]] (écosystème) | Rester dans PyTorch en factorisant seulement l'ingénierie d'entraînement → [[PyTorch Lightning]], qui n'écrit pas le modèle à votre place |
| Entraînement clés en main : callbacks, métriques, checkpointing, `fit` multi-GPU sans réécrire la boucle | Écosystème de modèles pré-entraînés de recherche → [[HuggingFace]], majoritairement PyTorch |
| Export et déploiement : passerelle vers TF Serving, TF Lite, ONNX selon le backend | Données **tabulaires** : un réseau est rarement le bon choix → [[XGBoost]], [[Scikit-Learn]] |

## Mise en œuvre

- Installation — `uv add keras`, plus un backend (`jax`, `tensorflow` ou `torch`) ; depuis TensorFlow 2.16, `import tensorflow` tire déjà Keras 3, où du code Keras 2 peut casser (l'ancien comportement vit dans `tf-keras`)
- Point d'entrée — import Python, après avoir posé `KERAS_BACKEND` dans l'environnement
- Prérequis — le backend choisi, et lui seul : c'est lui qui porte CUDA, le TPU ou MPS
- Exécution — dans le process appelant ; le distribué est celui du backend
- Coût — gratuit, Apache-2.0 ; maintenu par l'équipe Keras (Google), Keras 3 étant la version courante et `tf.keras` la variante historique

## Écosystème

### Alternatives

- [[PyTorch Lightning]] — Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code.

### Compléments

- [[PyTorch]] — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche. — backend supporté par Keras 3.
- [[TensorFlow]] — Framework de deep learning de Google — graphe optimisé et déploiement industriel (Serving, Lite, TPU, JS) ; Keras 3 comme API multi-backend de haut niveau. — le backend historique, et la porte vers Serving et Lite.
- [[JAX]] — Calcul numérique et différentiation automatique sur accélérateurs — NumPy compilé par XLA via jit/grad/vmap/pmap (GPU/TPU) ; socle des gros entraînements de recherche. — le backend visé pour la perf et le TPU.

## Ressources

- Documentation — https://keras.io/
- Dépôt — https://github.com/keras-team/keras

## Voir aussi

- [[Apprentissage profond]] — le hub du domaine
