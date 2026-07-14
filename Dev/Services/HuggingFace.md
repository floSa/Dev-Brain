---
galaxie: dev
type: service
nom: HuggingFace
alias: [hugging face, hf, huggingface, transformers, 🤗]
pitch: "Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes."
categorie: ml/framework
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: distributed
alternatives: []
remplace_par: []
status: actif
tags: [transformers, model-hub, fine-tuning, nlp, deep-learning, embeddings]
url_docs: https://huggingface.co/docs
url_repo: https://github.com/huggingface/transformers
---

# HuggingFace

## Pourquoi

HuggingFace n'est pas un framework de calcul mais une **couche au-dessus** d'eux. Deux briques : le **Hub** (huggingface.co — plus d'un million de modèles, de datasets et de Spaces pré-entraînés, versionnés en Git/LFS) et un ensemble de **bibliothèques** qui standardisent leur usage : `transformers` (modèles texte/vision/audio/multimodal), `datasets`, `tokenizers`, `accelerate` (entraînement distribué), `PEFT` (fine-tuning efficace type LoRA), `diffusers` (génératif image). Résultat : charger un modèle de l'état de l'art, le fine-tuner et le partager tiennent en quelques lignes. C'est le point d'entrée standard de l'IA appliquée.

## Quand l'utiliser

- **Partir d'un modèle pré-entraîné** plutôt que d'entraîner de zéro : NLP, vision, audio, multimodal.
- **Fine-tuning** sur ses données : `Trainer` + `PEFT` (LoRA/QLoRA) pour ajuster à moindre coût.
- **Datasets** : charger/streamer des jeux publics ou privés via `datasets`, sans réécrire de loaders.
- **Partager / déployer** : publier un modèle sur le Hub, démos via Spaces ([[Dev/Services/Gradio|Gradio]]), servir via TGI / endpoints.

## Quand NE PAS l'utiliser

- Définir et entraîner une architecture **sur mesure** de zéro : travailler directement avec [[Dev/Services/PyTorch|PyTorch]] (ou [[Dev/Services/JAX|JAX]]).
- Problème **tabulaire** : pas de transformeur, viser [[Dev/Services/XGBoost|XGBoost]], [[Dev/Services/LightGBM|LightGBM]], [[Dev/Services/Scikit-Learn|Scikit-Learn]].
- Contrainte stricte de licence/données : vérifier la licence de chaque modèle/dataset du Hub (variables, pas toutes commerciales).

## Déploiement & coût

- Bibliothèques open-source (Apache-2.0), gratuites ; `uv add transformers datasets accelerate`.
- Le **Hub** est une plateforme managée (huggingface.co) : usage public gratuit, offres payantes (stockage privé, Inference Endpoints, GPU pour Spaces).
- **PyTorch-first (2026)** : `transformers` s'est recentré sur [[Dev/Services/PyTorch|PyTorch]] ; le support natif [[Dev/Services/TensorFlow|TensorFlow]] et [[Dev/Services/JAX|JAX]] (Flax) est déprécié/retiré dans les versions récentes.
- Entraînement distribué via `accelerate` (multi-GPU, multi-nœuds).

## Pièges

- **Code de modèle distant** : `trust_remote_code=True` exécute du code arbitraire depuis le Hub — n'activer que pour des sources de confiance.
- **Poids volumineux** : le cache (`~/.cache/huggingface`) gonfle vite ; surveiller le disque, épingler les révisions (`revision=`) pour la reproductibilité.
- Compter sur un backend TF/JAX pour `transformers` : migrer vers PyTorch, le reste n'est plus maintenu.
- Licences hétérogènes des modèles : « open weights » ≠ usage commercial libre.

## Alternatives

Pas de concurrent direct référencé dans le brain : HuggingFace est une **couche hub** au-dessus des frameworks de calcul, pas un framework rival. Ses moteurs sous-jacents (et donc ses dépendances, pas ses substituts) sont listés dans *Liens*.

## Liens

- [[Dev/Services/PyTorch|PyTorch]] — backend principal de transformers/diffusers/PEFT.
- [[Dev/Services/TensorFlow|TensorFlow]] · [[Dev/Services/JAX|JAX]] — backends historiques, désormais minoritaires.
- Bibliothèques sœurs : [[Dev/Services/datasets|datasets]] (chargement de données), [[Dev/Services/accelerate|accelerate]] (entraînement distribué), [[Dev/Services/evaluate|evaluate]] (métriques).
- [[Dev/Services/Gradio|Gradio]] — démos interactives, technologie des Spaces.
- Doc : https://huggingface.co/docs
