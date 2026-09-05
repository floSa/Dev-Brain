---
role: brique
nom: CuPy
alias: [cupy]
pitch: "NumPy/SciPy sur GPU : tableau ndarray compatible drop-in exécuté sur CUDA/ROCm, pour accélérer le calcul numérique existant sans réécrire le code."
categorie: compute/gpu
famille: paquet
licence_type: open-source
maturite: production
langage: Python / C++ / CUDA
alternatives: ["[[numpy]]"]
complements: []
tags: [gpu, array]
url_docs: https://docs.cupy.dev/
url_repo: https://github.com/cupy/cupy
---

# CuPy

<!-- AUTO:BANDEAU:START -->
> NumPy/SciPy sur GPU : tableau ndarray compatible drop-in exécuté sur CUDA/ROCm, pour accélérer le calcul numérique existant sans réécrire le code.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python / C++ / CUDA | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque de tableaux sur GPU dont l'API est un **drop-in de [[numpy]]**, et d'une
grande partie de SciPy : `import cupy as cp` à la place de `numpy` exécute les mêmes
opérations sur GPU NVIDIA (CUDA) ou AMD (ROCm), en s'appuyant sur les bibliothèques natives
cuBLAS, cuFFT, cuSOLVER, cuRAND, cuDNN et NCCL. C'est le seul du dossier qui ne distribue
rien : il **descend** le calcul sur le GPU d'une machine au lieu de l'étaler sur un cluster.
Échange zéro-copie avec les frameworks de deep learning, et possibilité d'écrire un noyau
CUDA depuis Python. CuPy v14 aligne la sémantique sur NumPy 2 et ajoute bfloat16.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Accélérer un code numpy/SciPy existant sur GPU avec un changement d'import minimal | Le **transfert CPU↔GPU** (`cp.asarray`, `.get()`) domine vite le temps total : minimiser les allers-retours |
| Calcul vectorisé massif — algèbre linéaire, FFT, simulations — où le GPU bat largement le CPU | Couverture numpy/SciPy large mais **incomplète** : certaines fonctions manquent ou diffèrent |
| Pont avec le deep learning : échange zéro-copie avec [[PyTorch]] et [[JAX]] via `__cuda_array_interface__` ou DLPack | Correspondance **CUDA/ROCm ↔ wheel stricte** : une mauvaise version, et l'import échoue |
| Écrire des noyaux CUDA depuis Python sans quitter l'écosystème numpy | L'allocation GPU passe par un memory pool : surveiller la VRAM, libérer avec `free_all_blocks` au besoin |
| | Pas de GPU disponible → [[numpy]] sur CPU reste la référence |
| | Besoin de différentiation automatique ou d'un graphe d'entraînement → [[JAX]] ou [[PyTorch]] |
| | Code non vectorisé, en boucles Python : le transfert annule le gain |

## Mise en œuvre

- Installation — `uv add cupy-cuda12x` (wheels par version CUDA), ou build ROCm
- Point d'entrée — import Python, `import cupy as cp` à la place de `numpy`
- Prérequis — un GPU, et un driver/toolkit CUDA ou ROCm compatible installé sur l'hôte
- Exécution — mono-nœud, dans le process appelant ; exploite plusieurs GPU d'une machine, mais le multi-nœuds passe par une couche externe
- Coût — gratuit, MIT ; le coût réel est le matériel GPU

## Écosystème

### Alternatives

- [[numpy]] — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.

## Ressources

- Documentation — https://docs.cupy.dev/
- Dépôt — https://github.com/cupy/cupy

## Voir aussi

- [[Calcul distribué]] — le hub du domaine
- [[Dask]] — peut orchestrer des chunks CuPy pour dépasser la VRAM ou le mono-nœud
- [[Comparatif - Calcul distribué]] — ce qui départage les moteurs du dossier
