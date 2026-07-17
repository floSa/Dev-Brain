# Backlog enrichir-brain

## Sujet « Interprétabilité des réseaux » (2026-07-17) — LIVRÉ

File validée (GO utilisateur). Grappe révélée par l'ajout de [[Dev/Services/interpreto|interpreto]] : la fiche `Explicabilité des modèles` s'arrête aux méthodes tabulaires (permutation, MDI, Boruta, Shapley, surrogate local). Rien sur l'interprétabilité des réseaux, alors qu'`interpreto` implémente tout ce pan (attributions par gradient, probes, SAE, NMF/ICA).

Tags : tous pris dans le vocabulaire existant, aucun à créer.

### Lot 1 — le prérequis structurel
- [x] Autoencodeurs — encodeur/goulot/décodeur, AE vs VAE vs SAE. **Absent alors que 6 fiches le citent** (Réduction de dimension, Diffusion models, Time series anomaly detection, Apprentissage auto-supervisé en vision, PGA, Synthetic data generation). Sans lui, les SAE n'ont pas de parent. concept/dl, tags [deep-learning, unsupervised, representation-learning, dimensionality-reduction]

### Lot 2 — la grappe interprétabilité
- [x] Attribution par gradient — Saliency, InputxGradient, Integrated Gradients, SmoothGrad ; la contrepartie par gradient des méthodes par perturbation déjà fichées. concept/dl, tags [explainability, deep-learning]
- [x] Probing — entraîner un classifieur sur les activations pour savoir ce qu'une couche encode. concept/dl, tags [explainability, deep-learning, representation-learning]
- [x] Superposition — pourquoi un réseau encode plus de features qu'il n'a de neurones ; le phénomène qui justifie les SAE. concept/dl, tags [explainability, deep-learning, llm]
- [x] Sparse autoencoders — dictionnaire sur-complet et parcimonieux pour démêler la superposition. concept/dl, tags [explainability, deep-learning, llm, unsupervised]
- [x] Interprétabilité mécaniste — rétro-ingénierie des circuits ; le chapeau de la grappe. concept/dl, tags [explainability, deep-learning, llm]

### Lot 3 — les libs absentes
- [x] Captum — la référence PyTorch. Dev/Services, ml/framework, tags [explainability, deep-learning]
- [x] nnsight — dépendance directe d'interpreto, non fichée. Dev/Services, ml/framework, tags [explainability, llm]
- [x] TransformerLens — Dev/Services, ml/framework, tags [explainability, llm]
- [x] SAELens — Dev/Services, ml/framework, tags [explainability, llm]

### Lot 4 — les décompositions manquantes
- [x] ICA — `PCA.md:60` dit explicitement « ICA… hors brain ». Méthode de dictionnaire d'interpreto. concept/ml, tags [dimensionality-reduction, factor-analysis, unsupervised]
- [x] NMF — citée par `Matrix decompositions.md:59`. Idem. concept/ml, tags [dimensionality-reduction, factor-analysis, unsupervised]

### Liens à câbler
- [x] Autoencodeurs ↔ les 6 fiches qui le citent déjà sans lien
- [x] Explicabilité des modèles → Attribution par gradient, Probing, Interprétabilité mécaniste (le chapeau tabulaire s'ouvre sur le versant réseaux)
- [x] Interprétabilité mécaniste ↔ Superposition ↔ Sparse autoencoders ↔ Autoencodeurs
- [x] PCA → ICA, NMF (remplacer la mention « hors brain ») ; Matrix decompositions → NMF ; Réduction de dimension → ICA, NMF, Autoencodeurs
- [x] interpreto → les notions qu'il implémente ; réciprocité alternatives sur Captum/nnsight/TransformerLens/SAELens

### Clôture
- [x] build_index + build_mocs + build_links + check_brain (vert)
- [x] commit + push par lot

---

## Sujet « Vision par ordinateur » (2026-06-10) — LIVRÉ

> Soldé le 2026-07-17 : les 5 fiches et les 4 tags existent bien dans le vault, le backlog n'avait simplement jamais été coché.

File validée (GO utilisateur). 5 concepts `concept/dl`, galaxie wiki. Chapeau « Vision par ordinateur » lié aux 4 feuilles + ancres DL existantes. « Deep learning » = MOC existant `MOC/Concepts/Deep learning.md` → lien qualifié (pas de 6ᵉ page).

### Tags (créés dans Documentation/general/tags.md)
- [x] computer-vision, cnn, transfer-learning, data-augmentation

### Concepts — Wiki/Concepts (categorie concept/dl)
- [x] Vision par ordinateur — chapeau, tags [computer-vision, cnn, deep-learning]
- [x] CNN — convolution/pooling/champ réceptif, tags [cnn, computer-vision, deep-learning]
- [x] Architectures CNN — ResNet/MobileNet/EfficientNet/ConvNeXt, tags [cnn, computer-vision, deep-learning]
- [x] Transfer learning vision — tags [transfer-learning, fine-tuning, computer-vision, deep-learning]
- [x] Augmentation d'images — Mixup/CutMix/RandAugment, tags [data-augmentation, regularization, computer-vision, deep-learning]

### Liens
- [x] Chapeau ↔ 4 feuilles ; feuilles entre elles
- [x] Chapeau → ancres existantes : [[MOC/Concepts/Deep learning|Deep learning]], [[Transformer architectures]], [[Self-attention]], [[Vision Language Models]], [[Image generation]], [[Diffusion models]], [[Classification metrics]], [[Cross-entropy]], [[Dev/Services/PyTorch|PyTorch]], [[Dev/Services/Keras|Keras]], [[Dev/Services/HuggingFace|HuggingFace]]
- [x] Backlinks réciproques : Vision Language Models, Image generation, Transformer architectures

### Clôture
- [x] build_index + build_mocs + build_links + check_brain (vert)
- [x] commit + push + merge --ff-only main
