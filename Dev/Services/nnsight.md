---
galaxie: dev
type: service
nom: nnsight
alias: [NNsight, nnsight.net, NDIF]
pitch: "Bibliothèque d'intervention sur les internes d'un réseau PyTorch — capture et modifie activations et gradients via un contexte à exécution différée, et sait exécuter ces interventions à distance sur des modèles trop gros pour la machine locale (infrastructure NDIF)."
categorie: ml/framework
licence_type: open-source
hosted: both
maturite: beta
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/TransformerLens|TransformerLens]]", "[[Dev/Services/Captum|Captum]]"]
remplace_par: []
status: actif
tags: [explainability, llm]
url_docs: https://www.nnsight.net
url_repo: https://github.com/ndif-team/nnsight
---

# nnsight

## Pourquoi

Bibliothèque d'**intervention** sur les internes d'un modèle PyTorch : lire une activation, la modifier, récupérer un gradient — à n'importe quelle profondeur, sans réécrire le modèle ni poser des hooks à la main.

Son geste propre est l'**exécution différée** : le code écrit dans un bloc `trace` n'est pas exécuté immédiatement, il est capturé puis rejoué pendant la passe du modèle. On décrit *ce qu'on veut faire aux activations*, la bibliothèque se charge du reste.

Sa vraie singularité est ailleurs : **l'exécution distante** via l'infrastructure NDIF (Northeastern University). Le même code d'intervention peut cibler un modèle local ou un modèle de plusieurs centaines de milliards de paramètres hébergé ailleurs — ce qui met l'interprétabilité des très gros modèles à portée d'une machine ordinaire. C'est le point qu'aucune alternative n'offre.

## Quand l'utiliser

- **[[Interprétabilité mécaniste]]** : activation patching, ablation, steering — capturer et modifier les activations est exactement son objet.
- **Modèle trop gros pour la machine locale** : c'est le cas d'usage qui la distingue. Interventions envoyées à NDIF, résultats rapatriés.
- Extraire des activations pour entraîner un [[Probing|probe]] ou un [[Sparse autoencoders|SAE]].
- Travailler sur un modèle HuggingFace **quelconque**, sans dépendre d'un portage : elle enveloppe le modèle tel quel.
- Dépendance directe d'[[Dev/Services/interpreto|interpreto]], qui s'en sert pour son extraction d'activations.

## Quand NE PAS l'utiliser

- **Simple attribution** sur un modèle local : [[Dev/Services/Captum|Captum]] est plus direct, avec les méthodes déjà écrites.
- **Analyse de circuits sur GPT-2 ou modèles jouets** : [[Dev/Services/TransformerLens|TransformerLens]] expose des poids réécrits en notation canonique (têtes séparées, `W_Q`/`W_K`…), bien plus commode pour disséquer. nnsight, lui, garde le modèle HuggingFace tel quel.
- **Production** : c'est un outil de recherche. Pas de garantie de stabilité d'API.
- **Explication destinée à un métier** : hors sujet, ce n'est pas une bibliothèque d'explicabilité mais d'instrumentation.

## Déploiement & coût

- `pip install nnsight` — bibliothèque Python. Gratuit (MIT). Dépendance : `torch`, `transformers`.
- **Local** : exécution sur la machine, coût = le modèle lui-même.
- **Distant (NDIF)** : service académique gratuit, sur file d'attente. Modèles disponibles listés sur `nnsight.net/status`. Nécessite une clé d'API et une connexion sortante — **rédhibitoire en contexte on-prem ou air-gappé**, où seul le mode local est utilisable.
- Le mode distant implique que les données d'entrée **sortent du réseau**. À évaluer avant tout usage sur des données clients.

## Pièges

- **L'exécution différée déroute.** Le code dans un bloc `trace` ne s'exécute pas quand on le lit ; les valeurs n'existent qu'après `.save()` et sortie du contexte. Lire une variable trop tôt donne un proxy vide — l'erreur du débutant.
- **Ne pas confondre local et distant** : `remote=True` envoie les données à NDIF. Vérifier ce qu'on envoie.
- **Version 0.7.x, API mouvante** : plus de 110 releases. Épingler la version.
- **Pas de notation canonique** : contrairement à TransformerLens, les poids restent ceux de HuggingFace. Pour raisonner en têtes d'attention séparées, il faut faire le découpage soi-même.
- File d'attente NDIF : le mode distant n'est pas interactif, les temps de réponse varient.

## Alternatives

- [[Dev/Services/TransformerLens|TransformerLens]] — Bibliothèque de référence de l'interprétabilité mécaniste des Transformers — expose les activations et les poids en notation canonique (têtes séparées, flux résiduel décomposé) avec un système de hooks, pour rétro-concevoir les circuits appris.
- [[Dev/Services/Captum|Captum]] — Bibliothèque d'interprétabilité officielle de PyTorch (Meta) — une trentaine de méthodes d'attribution unifiées (Integrated Gradients, DeepLift, GradCAM, Shapley, TracIn) applicables à n'importe quel modèle PyTorch, entrées comme couches ou neurones.

## Liens

- [[Interprétabilité mécaniste]] — le concept parent : patching, ablation, steering.
- [[Probing]] — l'extraction d'activations qu'elle sert.
- [[Sparse autoencoders]] — les activations à collecter pour entraîner un SAE.
- [[Dev/Services/interpreto|interpreto]] — s'appuie dessus pour son extraction d'activations.
- [[Dev/Services/PyTorch|PyTorch]] / [[Dev/Services/HuggingFace|HuggingFace]] — le socle requis.
- [[Transformer architectures]] — l'objet instrumenté.
