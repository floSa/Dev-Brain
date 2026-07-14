---
galaxie: dev
type: service
nom: pytorch-crf
alias: [torchcrf, pytorch crf, conditional random field pytorch]
pitch: "Couche CRF (champ aléatoire conditionnel) pour PyTorch — modélise les dépendances entre labels voisins et décode par Viterbi ; brique de sortie classique d'un tagger d'étiquetage de séquence."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [sequence-labeling, ner, deep-learning]
url_docs: https://pytorch-crf.readthedocs.io
url_repo: https://github.com/kmkurn/pytorch-crf
---

# pytorch-crf

## Pourquoi

Implémentation minimale et canonique d'une **couche CRF** (champ aléatoire conditionnel linéaire) pour [[Dev/Services/PyTorch|PyTorch]]. Posée en sortie d'un modèle de séquence (BiLSTM ou transformeur), elle calcule la **log-vraisemblance** des séquences de labels et **décode** la meilleure par Viterbi — pour que les labels prédits respectent les contraintes de transition (un `I-PER` ne suit pas un `O`).

## Quand l'utiliser

- Ajouter une tête **CRF** à un tagger d'[[NER et étiquetage de séquence|étiquetage de séquence]] (NER, POS, chunking).
- Quand les **dépendances entre labels voisins** comptent et qu'un softmax token-par-token produit des séquences incohérentes.

## Quand NE PAS l'utiliser

- Pipeline NER clé en main → [[Dev/Services/spaCy|spaCy]] ou [[Dev/Services/HuggingFace|HuggingFace]] (`token-classification`, souvent sans CRF explicite).
- Tâche sans structure séquentielle (classification de document) → tête linéaire simple.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite ; `uv add pytorch-crf`. S'utilise comme un `nn.Module`.
- **Single-node** ; suit le device du modèle PyTorch (CPU / GPU).

## Pièges

- **Très dormant** : dernière release en 2019 — fonctionne avec PyTorch récent, mais aucune évolution ; valider la compatibilité.
- Masquage des séquences de longueur variable à gérer soigneusement (padding, `mask`).
- Les gros transformeurs fine-tunés rendent souvent le CRF **optionnel** : mesurer le gain réel avant de l'ajouter.

## Alternatives

Pas de substitut direct dans le brain (brique de bas niveau). En pratique, l'alternative est de **se passer de CRF** avec une tête de token-classification sur transformeur ([[Dev/Services/HuggingFace|HuggingFace]], cf. *Liens*).

## Liens

- [[NER et étiquetage de séquence]] — CRF et Viterbi y sont décrits.
- [[Dev/Services/PyTorch|PyTorch]] — le framework hôte.
- [[Dev/Services/HuggingFace|HuggingFace]] — token-classification, souvent sans CRF.
- [[Dev/Patterns/Comparatif - NLP|Comparatif — NLP]]
- Doc : https://pytorch-crf.readthedocs.io
