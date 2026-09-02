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
complements: []
tags: [out-of-core, streaming, nlp, deep-learning]
url_docs: https://huggingface.co/docs/datasets
url_repo: https://github.com/huggingface/datasets
---

# datasets

## Pourquoi

Bibliothèque de l'écosystème [[HuggingFace]] pour **charger, traiter et partager** des jeux de données ML. Le cœur est un backend **Apache Arrow** : les données sont stockées sur disque dans un cache colonnaire **memory-mappé**, ce qui donne des lectures *zero-copy* sans saturer la RAM, même sur des jeux de plusieurs centaines de Go. `load_dataset("nom")` récupère un dataset du Hub (texte, image, audio, multimodal) en une ligne ; les transformations (`map`, `filter`, `cast`) sont vectorisées et mises en cache automatiquement. Le mode **streaming** (`streaming=True`) itère sans rien télécharger entièrement — indispensable pour les corpus de pré-entraînement.

## Quand l'utiliser

- **Charger un jeu public** du Hub sans réécrire de loader : NLP, vision, audio.
- **Traiter plus grand que la RAM** : Arrow memory-mappé + `map` batché ; streaming pour l'out-of-core pur.
- **Alimenter un entraînement** [[PyTorch]] / `transformers` : `.with_format("torch")`, intégration directe avec le `Trainer`.
- **Publier / versionner** un dataset privé ou public sur le Hub (Git/LFS).

## Quand NE PAS l'utiliser

- Manipulation tabulaire analytique générale (jointures, group-by complexes) → [[Polars]] ou [[pandas]] (datasets n'est pas un moteur de requête).
- Données qui tiennent en mémoire et restent dans un DataFrame métier : un Arrow/HF dataset ajoute une couche inutile.
- Pipeline ELT / orchestration de données → [[Dagster]], [[Airflow]].

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite ; `uv add datasets`. Rien à héberger.
- S'appuie sur **PyArrow** ; conversions sans copie vers [[pandas]], [[Polars]], NumPy, PyTorch.
- Le **Hub** (huggingface.co) héberge les datasets : accès public gratuit, stockage privé et gros volumes sur offres payantes.
- Cache local (`~/.cache/huggingface/datasets`) memory-mappé : prévoir l'espace disque.

## Pièges

- Le **cache** grossit vite et n'est pas purgé seul ; surveiller le disque, épingler une `revision=` pour la reproductibilité.
- `trust_remote_code=True` sur certains datasets exécute un script de chargement distant — n'activer que pour des sources de confiance.
- `map` non batché est lent : passer `batched=True` et ajuster `num_proc` pour paralléliser.
- En streaming, pas d'accès aléatoire ni de `len()` : l'itération est séquentielle, le `shuffle` se fait par buffer.

## Alternatives

Pas de substitut direct dans le brain : `datasets` couple un format (Arrow memory-mappé) à un hub de partage, créneau qu'aucune autre fiche n'occupe. Pour la seule manipulation tabulaire, voir [[Polars]] / [[pandas]] (cités en *Liens*).

## Liens

- [[HuggingFace]] — bibliothèque sœur de `transformers` / `accelerate` dans la même stack.
- [[accelerate]] · [[evaluate]] — compléments entraînement et métriques de l'écosystème HF.
- [[PyTorch]] — `.with_format("torch")` pour alimenter un `DataLoader`.
- [[Polars]] · [[pandas]] — conversions Arrow sans copie.
- Doc : https://huggingface.co/docs/datasets
