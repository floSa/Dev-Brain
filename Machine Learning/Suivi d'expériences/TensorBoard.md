---
role: brique
nom: TensorBoard
alias: [tensorboard, tb]
pitch: "Boîte à outils de visualisation d'entraînement de TensorFlow — courbes de scalaires, histogrammes, graphe du modèle, images et projecteur d'embeddings depuis des event files locaux ; branché à PyTorch via torch.utils.tensorboard."
categorie: ml/tracking
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[MLflow]]", "[[Weights & Biases]]"]
complements: []
tags: [experiment-tracking, deep-learning, dataviz]
url_docs: https://www.tensorflow.org/tensorboard
url_repo: https://github.com/tensorflow/tensorboard
---

# TensorBoard

<!-- AUTO:BANDEAU:START -->
> Boîte à outils de visualisation d'entraînement de TensorFlow — courbes de scalaires, histogrammes, graphe du modèle, images et projecteur d'embeddings depuis des event files locaux ; branché à PyTorch via torch.utils.tensorboard.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Python | open-source | self-hébergé · mono-nœud | production | à jour · 2026-06-29 |
<!-- AUTO:BANDEAU:END -->

## Définition

Boîte à outils de visualisation d'entraînement, issue de TensorFlow puis devenue agnostique au
framework. Le code écrit des *event files* dans un répertoire de logs ; le serveur
`tensorboard --logdir` les lit et rend des tableaux de bord — courbes de scalaires,
histogrammes de poids et de gradients, graphe du modèle, images et audio, projecteur
d'embeddings (PCA, t-SNE), profilage. Ce n'est pas un gestionnaire d'expériences : il affiche
des fichiers, et ne conserve ni artefacts ni métadonnées d'exécution au-delà des events.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Visualiser vite et localement un entraînement, sans compte ni service tiers | |
| Projet PyTorch, TensorFlow ou `transformers` : `SummaryWriter` ou le callback intégré suffit | Aucune authentification : ne pas exposer le serveur brut sur Internet, le placer derrière un reverse-proxy |
| Inspecter le graphe d'un modèle, des images générées, un projecteur d'embeddings | Comparaison d'exécutions limitée : pas de tableau d'hyperparamètres riche |
| Profiler l'usage GPU et le coût des étapes, via le plugin Profiler | Suivi ultra-léger de très nombreuses exécutions en self-host → [[Aim]] |
| | Recherche d'hyperparamètres orchestrée → [[Optuna]] |
| | TensorBoard.dev est fermé : partager suppose d'exposer son propre serveur, ou d'exporter |

## Mise en œuvre

- Installation — `uv add tensorboard`
- Point d'entrée — serveur web `tensorboard --logdir`, alimenté par des event files ; côté PyTorch, `torch.utils.tensorboard.SummaryWriter`
- Prérequis — un répertoire de logs sur disque ou sur stockage objet ; les event files y grossissent vite avec les histogrammes et les images, d'où une fréquence de log à cadrer et de vieux runs à purger
- Exécution — serveur local mono-nœud : il sert des fichiers, il ne stocke rien d'autre
- Coût — gratuit, Apache-2.0 ; TensorBoard.dev, l'hébergement public de logs, est fermé

## Écosystème

### Alternatives

- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud.
- [[Weights & Biases]] — Plateforme SaaS de suivi d'expériences et de visualisation — dashboards riches, sweeps d'hyperparamètres, artefacts et registre de modèles ; référence en R&D deep learning.

## Ressources

- Documentation — https://www.tensorflow.org/tensorboard
- Dépôt — https://github.com/tensorflow/tensorboard

## Voir aussi

- [[Suivi d'expériences]] — le hub du dossier
- [[PyTorch]] — `torch.utils.tensorboard.SummaryWriter` écrit ses logs nativement
- [[TensorFlow]] — le projet d'origine ; callback Keras intégré
- [[HuggingFace]] — le `Trainer` y journalise via `report_to`
- [[Comparatif - Suivi d'expériences ML]] — ce qui départage les briques du dossier
