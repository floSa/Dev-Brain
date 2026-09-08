---
role: brique
nom: HuggingFace
alias: [hugging face, hf, huggingface, transformers, 🤗]
pitch: "Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes."
categorie: ml/hub
famille: saas
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: []
complements: ["[[datasets]]", "[[sentence-transformers]]", "[[spaCy]]"]
tags: [transformers, model-hub, fine-tuning, nlp, deep-learning, embeddings]
url_docs: https://huggingface.co/docs
url_repo: https://github.com/huggingface/transformers
---

# HuggingFace

<!-- AUTO:BANDEAU:START -->
> Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| SaaS | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-08-26 |
<!-- AUTO:BANDEAU:END -->

## Définition

Pas un framework de calcul, mais une **couche au-dessus** d'eux. Deux briques : le **Hub**
(huggingface.co — plus d'un million de modèles, datasets et Spaces, versionnés en Git/LFS) et
un ensemble de **bibliothèques** qui standardisent leur usage — `transformers` (texte, vision,
audio, multimodal), `datasets`, `tokenizers`, `accelerate` pour l'entraînement distribué,
`PEFT` pour le fine-tuning efficace type LoRA, `diffusers` pour le génératif image. Charger un
modèle de l'état de l'art, le fine-tuner et le partager tient alors en quelques lignes. Depuis
2026, `transformers` est **PyTorch-first** : le support natif de TensorFlow et de JAX/Flax est
déprécié ou retiré des versions récentes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Partir d'un modèle pré-entraîné plutôt que d'entraîner de zéro : NLP, vision, audio, multimodal | **Licences hétérogènes** des modèles et datasets du Hub : « open weights » n'est pas usage commercial libre, chaque poids est à vérifier |
| Fine-tuner sur ses données : `Trainer` et `PEFT` (LoRA, QLoRA) pour ajuster à moindre coût | `trust_remote_code=True` **exécute du code arbitraire** depuis le Hub — à n'activer que pour des sources de confiance |
| Charger ou streamer des jeux publics et privés sans réécrire de loaders | Compter sur un backend **TensorFlow ou JAX** pour `transformers` : le recentrage PyTorch a déprécié le reste → [[PyTorch]] |
| Publier un modèle sur le Hub, démos via Spaces ([[Gradio]]), servir via TGI ou endpoints | **Poids volumineux** : le cache `~/.cache/huggingface` gonfle vite, et la reproductibilité impose d'épingler `revision=` |
| | Définir et entraîner une architecture **sur mesure** de zéro → [[PyTorch]] ou [[JAX]] directement |
| | Problème **tabulaire** : aucun transformeur à y appliquer → [[XGBoost]], [[LightGBM]], [[Scikit-Learn]] |

## Mise en œuvre

- Installation — `uv add transformers datasets accelerate` ; `peft`, `diffusers` selon le besoin
- Point d'entrée — API Python (`AutoModel`, `AutoTokenizer`, `Trainer`) ; le Hub comme source de modèles et de datasets
- Prérequis — espace disque pour le cache des poids ; épingler `revision=` pour la reproductibilité
- Exécution — self-hébergé côté bibliothèques, managé côté Hub ; entraînement distribué multi-GPU et multi-nœuds via `accelerate`
- Coût — bibliothèques gratuites (Apache-2.0) ; Hub gratuit en usage public, payant pour le stockage privé, les Inference Endpoints et les GPU de Spaces

## Écosystème

### Alternatives

- Aucun concurrent direct référencé dans le brain : HuggingFace est une **couche hub** au-dessus des frameworks de calcul, pas un framework rival.

### Compléments

- [[datasets]] — Bibliothèque HuggingFace de chargement et traitement de datasets — backend Apache Arrow memory-mappé et mode streaming pour des jeux plus grands que la RAM, une ligne pour charger texte/image/audio depuis le Hub — la bibliothèque sœur côté données.
- [[sentence-transformers]] — Framework d'embeddings de phrases (SBERT) — encode textes et images en vecteurs pour la recherche sémantique, le clustering et le re-ranking ; bi-encoders et cross-encoders prêts à l'emploi — l'étage embeddings, servi depuis le Hub.
- [[spaCy]] — Bibliothèque NLP industrielle en Python — pipelines pré-entraînés multilingues (tokenisation, POS, dépendances, NER) rapides et prêts à l'emploi, intégrables avec les transformeurs — le pipeline linguistique, branché via `spacy-transformers`.

## Ressources

- Documentation — https://huggingface.co/docs
- Dépôt — https://github.com/huggingface/transformers

## Voir aussi

- [[Machine Learning]] — le hub du domaine
- [[PyTorch]] — le backend principal de `transformers`, `diffusers` et `PEFT`
- [[TensorFlow]] · [[JAX]] — les backends historiques, désormais minoritaires
- [[accelerate]] · [[evaluate]] — les bibliothèques sœurs, entraînement distribué et métriques
- [[sentencepiece]] — le tokeniseur que son `AutoTokenizer` charge de façon transparente
- [[Gradio]] — la technologie des Spaces, pour les démos interactives
