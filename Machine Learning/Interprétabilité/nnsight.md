---
role: brique
nom: nnsight
alias: [NNsight, nnsight.net, NDIF]
pitch: "Bibliothèque d'intervention sur les internes d'un réseau PyTorch — capture et modifie activations et gradients via un contexte à exécution différée, et sait exécuter ces interventions à distance sur des modèles trop gros pour la machine locale (infrastructure NDIF)."
categorie: ml/interpretabilite
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[TransformerLens]]", "[[Captum]]"]
complements: ["[[interpreto]]"]
tags: [explainability, llm]
url_docs: https://www.nnsight.net
url_repo: https://github.com/ndif-team/nnsight
---

# nnsight

<!-- AUTO:BANDEAU:START -->
> Bibliothèque d'intervention sur les internes d'un réseau PyTorch — capture et modifie activations et gradients via un contexte à exécution différée, et sait exécuter ces interventions à distance sur des modèles trop gros pour la machine locale (infrastructure NDIF).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta |
<!-- AUTO:BANDEAU:END -->

## Définition

Lire une activation, la modifier, récupérer un gradient — à n'importe quelle profondeur d'un modèle PyTorch, sans le réécrire ni poser des hooks à la main. Son geste propre est l'**exécution différée** : le code écrit dans un bloc `trace` n'est pas exécuté immédiatement, il est capturé puis rejoué pendant la passe du modèle. On décrit *ce qu'on veut faire aux activations*, la bibliothèque s'occupe du reste — ce qui déroute d'abord, puisque les valeurs n'existent qu'après `.save()` et sortie du contexte, et que lire une variable trop tôt donne un proxy vide. Sa vraie singularité est ailleurs : l'**exécution distante** via l'infrastructure NDIF (Northeastern University). Le même code d'intervention cible un modèle local ou un modèle de plusieurs centaines de milliards de paramètres hébergé ailleurs, ce qui met l'interprétabilité des très gros modèles à portée d'une machine ordinaire. Aucune alternative n'offre ce point — et il a un prix : `remote=True` fait **sortir les données d'entrée du réseau**.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| [[Interprétabilité mécaniste]] : activation patching, ablation, steering — capturer et modifier les activations est son objet | Analyse de circuits sur GPT-2 ou modèles jouets : elle garde les poids HuggingFace tels quels, sans notation canonique → [[TransformerLens]] |
| Modèle trop gros pour la machine locale : les interventions partent chez NDIF, les résultats reviennent | Simple attribution sur un modèle local : les méthodes sont déjà écrites ailleurs → [[Captum]] |
| Extraire des activations pour entraîner une sonde ([[Probing]]) ou un [[Sparse autoencoders]] | Contexte on-prem ou air-gappé : le mode distant exige une clé d'API et une connexion sortante — seul le mode local reste utilisable |
| Travailler sur un modèle HuggingFace quelconque, sans dépendre d'un portage : elle l'enveloppe tel quel | Production : outil de recherche, sans garantie de stabilité d'API |
| | Explication destinée à un métier : ce n'est pas une bibliothèque d'explicabilité mais d'instrumentation |

## Mise en œuvre

- Installation — `uv add nnsight` ; version 0.7.x, plus de 110 releases et une API mouvante, épingler la version
- Point d'entrée — import Python : un bloc `trace` sur le modèle, et `.save()` sur ce qu'on veut récupérer
- Prérequis — `torch` et `transformers` en local ; une clé d'API NDIF et une connexion sortante pour le mode distant
- Exécution — locale, coût égal au modèle lui-même ; ou distante sur NDIF, service académique gratuit **sur file d'attente**, donc non interactif et à temps de réponse variable (modèles disponibles listés sur `nnsight.net/status`)
- Coût — gratuit, MIT ; le vrai coût du mode distant n'est pas financier, il est la sortie des données — à évaluer avant tout usage sur des données clients

## Écosystème

### Alternatives

- [[TransformerLens]] — Bibliothèque de référence de l'interprétabilité mécaniste des Transformers — expose les activations et les poids en notation canonique (têtes séparées, flux résiduel décomposé) avec un système de hooks, pour rétro-concevoir les circuits appris.
- [[Captum]] — Bibliothèque d'interprétabilité officielle de PyTorch (Meta) — une trentaine de méthodes d'attribution unifiées (Integrated Gradients, DeepLift, GradCAM, Shapley, TracIn) applicables à n'importe quel modèle PyTorch, entrées comme couches ou neurones.

### Compléments

- [[interpreto]] — Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs. — elle s'appuie sur nnsight pour son extraction d'activations.

## Ressources

- Documentation — https://www.nnsight.net
- Dépôt — https://github.com/ndif-team/nnsight

## Voir aussi

- [[Comparatif - Explicabilité]] — ce qui départage les outils du dossier
- [[HuggingFace]] — les modèles qu'elle enveloppe sans les retoucher
- [[Transformer architectures]] — l'objet instrumenté
