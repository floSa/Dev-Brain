---
role: brique
nom: datasets
alias: [hf datasets, huggingface datasets, 🤗 datasets]
pitch: "Bibliothèque HuggingFace de chargement et traitement de datasets — backend Apache Arrow memory-mappé et mode streaming pour des jeux plus grands que la RAM, une ligne pour charger texte/image/audio depuis le Hub."
categorie: ml/hub
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[HuggingFace]]"]
tags: [out-of-core, streaming, nlp, deep-learning]
url_docs: https://huggingface.co/docs/datasets
url_repo: https://github.com/huggingface/datasets
---

# datasets

<!-- AUTO:BANDEAU:START -->
> Bibliothèque HuggingFace de chargement et traitement de datasets — backend Apache Arrow memory-mappé et mode streaming pour des jeux plus grands que la RAM, une ligne pour charger texte/image/audio depuis le Hub.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

La bibliothèque de l'écosystème [[HuggingFace]] pour **charger, traiter et partager** des jeux
de données ML. Son cœur est un backend **Apache Arrow** : les données vivent sur disque dans un
cache colonnaire **memory-mappé**, d'où des lectures *zero-copy* qui ne saturent pas la RAM,
même sur plusieurs centaines de Go. `load_dataset("nom")` récupère un jeu du Hub — texte,
image, audio, multimodal — en une ligne, et les transformations (`map`, `filter`, `cast`) sont
vectorisées et mises en cache automatiquement. Le mode **streaming** itère sans rien
télécharger entièrement, au prix de l'accès aléatoire : plus de `len()`, et le `shuffle` se
fait par buffer. Ce n'est pas un moteur de requête — ni jointures, ni group-by complexes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Charger un jeu public du Hub sans réécrire de loader : NLP, vision, audio | Manipulation tabulaire analytique — jointures, group-by complexes : ce n'est pas un moteur de requête → [[Polars]] ou [[pandas]] |
| Traiter **plus grand que la RAM** : Arrow memory-mappé et `map` batché, streaming pour l'out-of-core pur | |
| Alimenter un entraînement [[PyTorch]] ou `transformers` : `.with_format("torch")`, intégration directe au `Trainer` | En **streaming**, ni accès aléatoire ni `len()` : l'itération est séquentielle et le `shuffle` approximatif, par buffer |
| Publier et versionner un dataset privé ou public sur le Hub, en Git/LFS | `trust_remote_code=True` **exécute un script de chargement distant** — à n'activer que pour des sources de confiance |
| | Données qui tiennent en mémoire et restent dans un DataFrame métier : la couche Arrow est un coût sans contrepartie |
| | Pipeline ELT ou orchestration de données → [[Dagster]], [[Airflow]] |

## Mise en œuvre

- Installation — `uv add datasets`
- Point d'entrée — `load_dataset("nom")`, puis `map` / `filter` / `cast` ; passer `batched=True` et régler `num_proc`, un `map` non batché étant lent
- Prérequis — espace disque pour le cache memory-mappé (`~/.cache/huggingface/datasets`), qui grossit vite et n'est jamais purgé seul ; épingler une `revision=` pour la reproductibilité
- Exécution — single-node, appuyé sur PyArrow ; conversions sans copie vers [[pandas]], [[Polars]], NumPy, PyTorch
- Coût — gratuit, Apache-2.0, rien à héberger côté bibliothèque ; le Hub est gratuit en accès public, payant pour le stockage privé et les gros volumes

## Écosystème

### Alternatives

- Aucun substitut direct dans le brain : `datasets` couple un format (Arrow memory-mappé) à un hub de partage, créneau qu'aucune autre fiche n'occupe.

### Compléments

- [[HuggingFace]] — Hub et bibliothèques au-dessus des frameworks DL — 1M+ modèles/datasets pré-entraînés, transformers/datasets/accelerate/PEFT ; charger, fine-tuner et partager un modèle en quelques lignes — la même stack, dont `datasets` est la brique données.

## Ressources

- Documentation — https://huggingface.co/docs/datasets
- Dépôt — https://github.com/huggingface/datasets

## Voir aussi

- [[Machine Learning]] — le hub du domaine
- [[accelerate]] · [[evaluate]] — les bibliothèques sœurs, entraînement distribué et métriques
- [[PyTorch]] — `.with_format("torch")` pour alimenter un `DataLoader`
- [[Polars]] · [[pandas]] — les conversions Arrow sans copie
