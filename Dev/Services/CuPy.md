---
galaxie: dev
type: service
nom: CuPy
alias: [cupy]
pitch: "NumPy/SciPy sur GPU : tableau ndarray compatible drop-in exécuté sur CUDA/ROCm, pour accélérer le calcul numérique existant sans réécrire le code."
categorie: compute/distributed
licence_type: open-source
hosted: self
maturite: production
langage: Python / C++ / CUDA
scaling: single-node
alternatives: ["[[Dev/Services/numpy|numpy]]"]
remplace_par: []
status: actif
tags: [gpu, array]
url_docs: https://docs.cupy.dev/
url_repo: https://github.com/cupy/cupy
---

# CuPy

## Pourquoi

Bibliothèque de **tableaux sur GPU** dont l'API est un **drop-in de [[Dev/Services/numpy|numpy]]** (et d'une grande partie de SciPy) : `import cupy as cp` à la place de `numpy` exécute les mêmes opérations sur GPU NVIDIA (**CUDA**) ou AMD (**ROCm**), via les bibliothèques natives (cuBLAS, cuFFT, cuSOLVER, cuRAND, cuDNN, NCCL). Maintenue par Preferred Networks. Permet d'accélérer du calcul numérique vectorisé **sans réécrire le code**, et de descendre au CUDA custom (`RawKernel`, fusion de noyaux) quand il faut. CuPy v14 aligne la sémantique sur NumPy 2 et ajoute bfloat16.

## Quand l'utiliser

- Accélérer un code **numpy/SciPy existant** sur GPU avec un changement d'import minimal.
- Calcul **vectorisé massif** (algèbre linéaire, FFT, simulations) où le GPU bat largement le CPU.
- Pont avec le deep learning : échange zéro-copie avec [[Dev/Services/PyTorch|PyTorch]] / [[Dev/Services/JAX|JAX]] via le protocole `__cuda_array_interface__` / DLPack.
- Écrire des **noyaux CUDA** depuis Python sans quitter l'écosystème numpy.

## Quand NE PAS l'utiliser

- Pas de GPU disponible → [[Dev/Services/numpy|numpy]] (CPU) reste la référence.
- Besoin de **différentiation automatique** ou d'un graphe d'entraînement → [[Dev/Services/JAX|JAX]] / [[Dev/Services/PyTorch|PyTorch]].
- Données **plus grandes que la VRAM** ou calcul **multi-nœuds** → [[Dev/Services/Dask|Dask]] (qui peut piloter des chunks CuPy) plutôt que CuPy seul.
- Code non vectorisé (boucles Python) : le transfert CPU↔GPU annule le gain.

## Déploiement & coût

- Bibliothèque open-source (MIT), `uv add cupy-cuda12x` (wheels par version CUDA) ou build ROCm.
- **Single-node** ; exploite plusieurs GPU d'une machine, mais le multi-nœuds passe par une couche externe ([[Dev/Services/Dask|Dask]], MPI).
- Coût = le matériel GPU ; la bibliothèque est gratuite.
- Dépend d'un **driver / toolkit CUDA (ou ROCm)** compatible installé sur l'hôte.

## Pièges

- Le **transfert mémoire** CPU↔GPU (`cp.asarray` / `.get()`) domine vite le temps : minimiser les allers-retours.
- Couverture numpy/SciPy **large mais incomplète** : certaines fonctions manquent ou diffèrent légèrement.
- Compatibilité **CUDA/ROCm ↔ wheel** stricte : une mauvaise version CUDA = échec d'import.
- L'allocation GPU est mise en cache par un memory pool : surveiller la VRAM, libérer (`free_all_blocks`) si besoin.

## Alternatives

- [[Dev/Services/numpy|numpy]] — Socle du calcul numérique Python : tableau N-dimensionnel (ndarray) contigu et opérations vectorisées en C ; la fondation de pandas, scikit-learn et tout l'écosystème scientifique.

## Liens

- [[Comparatif - Calcul distribué]] — comparatif de la catégorie
- Équivalent CPU dont il copie l'API : [[Dev/Services/numpy|numpy]].
- Multi-nœuds / hors VRAM : [[Dev/Services/Dask|Dask]] peut orchestrer des chunks CuPy.
- GPU avec autodiff : [[Dev/Services/JAX|JAX]], [[Dev/Services/PyTorch|PyTorch]].
- Doc : https://docs.cupy.dev/
