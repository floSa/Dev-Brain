---
role: brique
nom: PyTorch
alias: [torch, pytorch, libtorch]
pitch: "Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche."
categorie: ml/apprentissage-profond
famille: paquet
licence_type: open-source
maturite: production
langage: C++/Python
alternatives: ["[[TensorFlow]]", "[[JAX]]"]
complements: ["[[Keras]]", "[[PyTorch Lightning]]", "[[accelerate]]", "[[DeepSpeed]]", "[[pykan]]"]
tags: [deep-learning, gpu, autograd, distributed]
url_docs: https://docs.pytorch.org/
url_repo: https://github.com/pytorch/pytorch
---

# PyTorch

<!-- AUTO:BANDEAU:START -->
> Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++/Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-08 |
<!-- AUTO:BANDEAU:END -->

## Définition

Le type `Tensor` — un tableau N-dimensionnel à la NumPy, sur CPU ou GPU — et un moteur d'**autograd** qui enregistre les opérations au fil de l'exécution pour en calculer les gradients. Ce modèle **define-by-run** (le graphe se construit à l'exécution) rend le code pythonique et le débogage immédiat : c'est ce qui en a fait le standard de fait en recherche. Depuis la branche 2.x, `torch.compile` capture le graphe et le compile en noyaux fusionnés, sans réécrire le modèle — mais il retombe en mode eager (*graph breaks*) sur du code trop dynamique, ce qui se vérifie plutôt que se suppose. Corollaire du define-by-run : les modes entraînement et inférence sont un **état du module**, à poser explicitement (`model.eval()`, `torch.no_grad()`), faute de quoi BatchNorm et Dropout restent actifs et les gradients s'accumulent pour rien.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Recherche et prototypage : la majorité des papiers avec code et des modèles du Hub sont en PyTorch | Déploiement industriel mobile / edge / navigateur clés en main → [[TensorFlow]] (Lite, JS, Serving) |
| Entraînement GPU, multi-GPU, multi-nœuds : `DistributedDataParallel`, FSDP pour le sharding mémoire | Recherche centrée transformations fonctionnelles et compilation XLA sur TPU → [[JAX]] |
| Vision, audio, séquences, LLM : torchvision, torchaudio, et passerelle directe vers les modèles pré-entraînés | Données **tabulaires** structurées : un réseau de neurones est rarement le bon choix → [[XGBoost]], [[LightGBM]], [[Scikit-Learn]] |
| Du prototype à la prod : `torch.compile` pour la vitesse, ExecuTorch / TorchScript pour l'export | |

## Mise en œuvre

- Installation — `uv add torch`, en choisissant la roue qui correspond au driver et à la version CUDA de la machine : sinon le GPU n'est pas détecté
- Point d'entrée — import Python, `import torch` ; cœur C++/CUDA (libtorch, ATen) sous l'API
- Prérequis — un accélérateur si l'on entraîne : GPU NVIDIA (CUDA), AMD (ROCm) ou Apple Silicon (MPS) ; le CPU suffit pour apprendre
- Exécution — dans le process appelant ; passe à l'échelle en distribué (DDP, FSDP) sur cluster multi-nœuds
- Coût — gratuit, BSD-3-Clause, aucune limite d'usage ; gouverné par la **PyTorch Foundation** (Linux Foundation), donc neutre multi-acteurs

## Écosystème

### Alternatives

- [[TensorFlow]] — Framework de deep learning de Google — graphe optimisé et déploiement industriel (Serving, Lite, TPU, JS) ; Keras 3 comme API multi-backend de haut niveau.
- [[JAX]] — Calcul numérique et différentiation automatique sur accélérateurs — NumPy compilé par XLA via jit/grad/vmap/pmap (GPU/TPU) ; socle des gros entraînements de recherche.

### Compléments

- [[Keras]] — API de deep learning de haut niveau, multi-backend (Keras 3) — le même code de modèle s'exécute sur JAX, TensorFlow ou PyTorch ; construire, entraîner et exporter un réseau vite, sans s'enfermer dans un framework. — PyTorch en est l'un des trois backends.
- [[PyTorch Lightning]] — Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code. — pour ranger la boucle d'entraînement.
- [[accelerate]] — Couche HuggingFace qui rend une boucle PyTorch distribuée sans la réécrire — même script du laptop au cluster multi-GPU/multi-nœuds, précision mixte (jusqu'à fp8), FSDP et DeepSpeed à la config. — pour distribuer sans changer de framework.
- [[DeepSpeed]] — Bibliothèque Microsoft d'optimisation de l'entraînement (et de l'inférence) à grande échelle — ZeRO shardle les états entre GPU pour entraîner des modèles à des dizaines/centaines de milliards de paramètres, avec offload CPU/NVMe, 3D-parallelism et précision mixte. — quand FSDP ne suffit plus.
- [[pykan]] — Implémentation officielle de référence des Kolmogorov-Arnold Networks (sur PyTorch) — splines apprenables sur les arêtes, raffinement de grille, sparsification et extraction de formule symbolique ; orientée ML scientifique plus que performance. — une architecture de recherche bâtie dessus.

## Ressources

- Documentation — https://docs.pytorch.org/
- Dépôt — https://github.com/pytorch/pytorch

## Voir aussi

- [[Apprentissage profond]] — le hub du domaine
- [[Entraînement distribué]] — DDP et FSDP natifs (`torch.distributed`) pour passer l'entraînement à l'échelle
- [[Mixed precision]] — `torch.amp` (autocast + GradScaler) pour l'entraînement fp16/bf16
- [[Gradient checkpointing]] — `torch.utils.checkpoint` pour échanger du calcul contre de la mémoire d'activations
- [[Pruning]] — `torch.nn.utils.prune` pour l'élagage structuré ou non
- [[HuggingFace]] — hub de modèles et bibliothèques au-dessus de PyTorch (backend principal de transformers, diffusers, PEFT)
- [[Optuna]] — optimisation d'hyperparamètres, avec pruning intégré à PyTorch
- [[TorchServe]] — serveur de modèles PyTorch dédié, désormais non maintenu ; pour servir en prod, voir [[NVIDIA Triton]] et [[BentoML]]
