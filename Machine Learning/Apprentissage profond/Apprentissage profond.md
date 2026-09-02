---
role: hub
nom: Apprentissage profond
alias: [deep learning, réseaux de neurones]
pitch: Les socles avec lesquels on entraîne un réseau de neurones — tenseurs, autograd, accélérateurs, et tout ce qui rend un gros entraînement tenable.
domaines: [ml-eng, data-sci]
tags: [deep-learning, gpu, autograd, transformers, attention, distributed-training, mixed-precision, quantization, model-compression]
---

# Apprentissage profond

> Les socles avec lesquels on entraîne un réseau de neurones — tenseurs, autograd, accélérateurs, et tout ce qui rend un gros entraînement tenable.

## Ce qu'il faut comprendre

- **Ce dossier ne range pas « tout ce qui est profond », il range les socles d'entraînement.** Un modèle de vision et un LLM sont profonds tous les deux ; ils ne sont pas ici. Une bibliothèque dont l'entrée est une image est dans [[Vision]], une bibliothèque de texte dans [[NLP]], un modèle de langage génératif dans [[LLM & IA générative]], une bibliothèque qui apprend par interaction dans [[Apprentissage par renforcement]]. Ce qui reste ici est la couche en dessous : celle qui donne des tenseurs, une différentiation automatique, des GPU et une boucle d'entraînement.
- **Le vrai choix est le framework, et il se fait une fois pour toutes** — c'est la décision la plus coûteuse à revenir dessus de tout le domaine. Elle porte sur l'écosystème disponible (modèles pré-entraînés, tutoriels, recrutement) bien plus que sur les performances brutes, qui se sont égalisées.
- **Un réseau, c'est une architecture plus une recette d'optimisation**, et les deux se documentent séparément. Côté architecture : [[Transformer architectures]] domine, construit sur la [[Self-attention]] et un encodage de position ([[Positional encoding]]) ; [[Attention Residuals]] explique ce que le flux résiduel transporte, [[Attention linéaire]] et [[Flash Attention and efficient attention]] attaquent son coût quadratique par deux voies opposées — changer la formule, ou changer l'implémentation sans changer le résultat. [[Multi-head Latent Attention]] compresse le cache, [[Mixture of Experts]] augmente les paramètres sans augmenter le calcul par token, [[State Space Models]] proposent une alternative séquentielle linéaire, [[Kolmogorov-Arnold Networks]] une rupture plus radicale. [[CNN]] et [[Architectures CNN]] restent la référence sur signal régulier, [[Graph Neural Networks]] la généralisation aux graphes.
- **Les familles génératives se confondent facilement, et leurs compromis sont opposés.** [[Autoencodeurs]] compressent et reconstruisent, [[GANs]] opposent deux réseaux et produisent vite mais s'entraînent mal, [[Diffusion models]] débruitent par étapes et ont gagné la partie sur la qualité au prix du temps d'inférence. Leurs applications : [[Image generation]], [[Video generation]], [[Speech models]], et [[Classification audio par spectrogramme]] pour le cas où l'audio redevient une image.
- **L'optimisation est le second métier**, et il ne s'improvise pas : [[Adam optimizer]] est le défaut de fait, [[Maximal Update Parametrization]] ce qui permet de transférer des hyperparamètres d'un petit modèle vers un grand au lieu de tout rechercher, [[Calculs adaptatifs]] l'idée de dépenser plus de calcul là où c'est utile.
- **Passer à l'échelle est un problème de mémoire avant d'être un problème de vitesse.** [[Entraînement distribué]] pose les stratégies de parallélisme ; [[Mixed precision]] et [[Gradient checkpointing]] sont les deux leviers qui font tenir un modèle sur le GPU dont on dispose — le premier réduit la taille des nombres, le second recalcule au lieu de stocker.
- **Compresser après l'entraînement est un sujet distinct**, avec ses trois familles : [[Quantization]] réduit la précision des poids, [[Pruning]] enlève des connexions, [[Distillation]] transfère le comportement vers un modèle plus petit. C'est ce qui rend un modèle servable — cf. [[Serving]].
- L'interprétabilité de ces réseaux est un domaine à part entière, outillé dans [[Interprétabilité]] : [[Interprétabilité mécaniste]], [[Sparse autoencoders]], [[Superposition]], [[Probing]], [[Attribution par gradient]].
- Enfin, un point de vocabulaire qui trompe régulièrement : [[Architectures hybrides LLM]] décrit les modèles qui mélangent attention et récurrence, et relève autant de ce dossier que de [[LLM & IA générative]].

## Choisir

- Un projet neuf, de la recherche au produit → [[PyTorch]] ; c'est l'écosystème par défaut, et celui que supposent la plupart des autres dossiers de ce domaine.
- Écrire moins de boucle d'entraînement, garder PyTorch dessous → [[PyTorch Lightning]].
- Une API de haut niveau, quitte à changer de backend plus tard → [[Keras]], qui tourne sur JAX, TensorFlow ou PyTorch.
- Des transformations fonctionnelles composables, du TPU, de la recherche à grande échelle → [[JAX]].
- Un existant industriel, du TPU Google ou un déploiement mobile / navigateur → [[TensorFlow]].
- Distribuer une boucle PyTorch déjà écrite, sans la réécrire → [[accelerate]].
- Entraîner un modèle qui ne tient pas en mémoire GPU → [[DeepSpeed]] et son sharding ZeRO.
- Expérimenter les Kolmogorov-Arnold Networks → [[pykan]].
- Un graphe en entrée → [[PyTorch Geometric]], au niveau du domaine.
- Récupérer un modèle pré-entraîné plutôt que d'en entraîner un → [[HuggingFace]], et [[timm]] pour les backbones vision.

<!-- AUTO:START -->
### Briques
- [[accelerate]] — Couche HuggingFace qui rend une boucle PyTorch distribuée sans la réécrire — même script du laptop au cluster multi-GPU/multi-nœuds, précision mixte (jusqu'à fp8), FSDP et DeepSpeed à la config.
- [[DeepSpeed]] — Bibliothèque Microsoft d'optimisation de l'entraînement (et de l'inférence) à grande échelle — ZeRO shardle les états entre GPU pour entraîner des modèles à des dizaines/centaines de milliards de paramètres, avec offload CPU/NVMe, 3D-parallelism et précision mixte.
- [[JAX]] — Calcul numérique et différentiation automatique sur accélérateurs — NumPy compilé par XLA via jit/grad/vmap/pmap (GPU/TPU) ; socle des gros entraînements de recherche.
- [[Keras]] — API de deep learning de haut niveau, multi-backend (Keras 3) — le même code de modèle s'exécute sur JAX, TensorFlow ou PyTorch ; construire, entraîner et exporter un réseau vite, sans s'enfermer dans un framework.
- [[pykan]] — Implémentation officielle de référence des Kolmogorov-Arnold Networks (sur PyTorch) — splines apprenables sur les arêtes, raffinement de grille, sparsification et extraction de formule symbolique ; orientée ML scientifique plus que performance.
- [[PyTorch]] — Framework de deep learning de référence — tensors GPU et autograd, API Python pythonique (define-by-run) ; torch.compile pour la perf, écosystème dominant en recherche.
- [[PyTorch Lightning]] — Surcouche d'organisation de PyTorch — sépare la logique du modèle de l'ingénierie d'entraînement (boucle, multi-GPU, mixed precision, checkpointing) via le Trainer ; moins de boilerplate, runs reproductibles, du laptop à 1000+ GPU sans changer le code.
- [[TensorFlow]] — Framework de deep learning de Google — graphe optimisé et déploiement industriel (Serving, Lite, TPU, JS) ; Keras 3 comme API multi-backend de haut niveau.
<!-- AUTO:END -->

## Notes
