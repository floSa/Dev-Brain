---
galaxie: dev
type: service
nom: PyTorch
alias: [torch, pytorch, libtorch]
pitch: "Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: C++/Python
scaling: distributed
alternatives: ["[[Dev/Services/TensorFlow|TensorFlow]]", "[[Dev/Services/JAX|JAX]]"]
remplace_par: []
status: actif
tags: [deep-learning, gpu, autograd, distributed]
url_docs: https://docs.pytorch.org/
url_repo: https://github.com/pytorch/pytorch
---

# PyTorch

## Pourquoi

Framework de **deep learning** bâti sur un type `Tensor` (un tableau N-dimensionnel à la NumPy, mais sur GPU/CPU) et un moteur d'**autograd** qui enregistre dynamiquement les opérations pour calculer les gradients. Son modèle **define-by-run** (le graphe se construit à l'exécution) rend le code pythonique et le débogage immédiat — ce qui en a fait le standard de fait en recherche. Depuis la branche 2.x, `torch.compile` capture le graphe et le compile (fusion de noyaux) pour des gains de vitesse sans réécrire le modèle.

## Quand l'utiliser

- **Recherche et prototypage** de réseaux de neurones : la majorité des papiers avec code et des modèles du Hub [[Dev/Services/HuggingFace|HuggingFace]] sont en PyTorch.
- **Entraînement GPU / multi-GPU / multi-nœuds** : `DistributedDataParallel`, FSDP pour le sharding mémoire des gros modèles.
- **Vision, audio, séquences, LLM** : écosystème riche (torchvision, torchaudio) et passerelle directe vers les modèles pré-entraînés de [[Dev/Services/HuggingFace|HuggingFace]].
- **Du prototype à la prod** : `torch.compile` pour la vitesse, ExecuTorch / TorchScript pour l'export, serving via TorchServe ou des runtimes tiers (vLLM, TGI).

## Quand NE PAS l'utiliser

- Déploiement industriel mobile / edge / navigateur clés en main → [[Dev/Services/TensorFlow|TensorFlow]] (Lite, JS, Serving).
- Recherche centrée transformations fonctionnelles et compilation XLA (TPU) → [[Dev/Services/JAX|JAX]].
- Données **tabulaires** structurées : un réseau de neurones est rarement le bon choix → [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/Scikit-Learn|Scikit-Learn]].

## Déploiement & coût

- Bibliothèque open-source (BSD-3-Clause), gratuite ; `uv add torch`. Rien à héberger.
- Cœur C++/CUDA (libtorch, ATen) sous API Python ; CPU, GPU NVIDIA (CUDA), AMD (ROCm), Apple Silicon (MPS).
- Gouverné par la **PyTorch Foundation** (Linux Foundation) — neutralité multi-acteurs (Meta, AMD, AWS, Google, NVIDIA…).
- Passe à l'échelle en distribué (DDP, FSDP) pour l'entraînement des gros modèles.

## Pièges

- Versions liées à une build CUDA précise : installer la roue qui correspond au driver/CUDA, sinon GPU non détecté.
- `torch.compile` peut retomber en mode eager (graph breaks) sur du code dynamique : vérifier que la compilation tient vraiment.
- Oublier `model.eval()` / `torch.no_grad()` en inférence → BatchNorm/Dropout actifs et gradients accumulés inutilement.

## Alternatives

- [[Dev/Services/TensorFlow|TensorFlow]] — Framework de deep learning de Google — graphe optimisé et déploiement industriel (Serving, Lite, TPU, JS) ; Keras 3 comme API multi-backend de haut niveau.
- [[Dev/Services/JAX|JAX]] — Calcul numérique et différentiation automatique sur accélérateurs — NumPy compilé par XLA via jit/grad/vmap/pmap (GPU/TPU) ; socle des gros entraînements de recherche.

## Liens

- [[Dev/Services/HuggingFace|HuggingFace]] — hub de modèles et bibliothèques au-dessus de PyTorch (backend principal de transformers, diffusers, PEFT).
- [[Dev/Services/Optuna|Optuna]] — optimisation d'hyperparamètres avec intégration PyTorch (pruning).
- [[Dev/Services/TorchServe|TorchServe]] — serveur de modèles PyTorch dédié (désormais non maintenu) ; pour servir en prod, voir aussi [[Dev/Services/NVIDIA Triton|NVIDIA Triton]] et [[Dev/Services/BentoML|BentoML]].
- [[Dev/Services/PyTorch Lightning|PyTorch Lightning]] — surcouche qui organise le code d'entraînement PyTorch (Trainer, multi-GPU, mixed precision).
- [[Dev/Services/accelerate|accelerate]] — distribue une boucle PyTorch existante (multi-GPU, FSDP, DeepSpeed, précision mixte) sans la réécrire.
- [[Dev/Services/Keras|Keras]] — API de haut niveau multi-backend : Keras 3 tourne aussi sur backend PyTorch.
- [[Entraînement distribué]] — DDP et FSDP natifs (`torch.distributed`) pour passer l'entraînement à l'échelle.
- [[Mixed precision]] — `torch.amp` (autocast + GradScaler) pour l'entraînement fp16/bf16.
- [[Gradient checkpointing]] — `torch.utils.checkpoint` pour échanger calcul contre mémoire d'activations.
- [[Pruning]] — `torch.nn.utils.prune` pour l'élagage structuré / non structuré.
- Doc : https://docs.pytorch.org/
