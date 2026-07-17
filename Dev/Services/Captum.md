---
galaxie: dev
type: service
nom: Captum
alias: [captum, Captum.ai]
pitch: "Bibliothèque d'interprétabilité officielle de PyTorch (Meta) — une trentaine de méthodes d'attribution unifiées (Integrated Gradients, DeepLift, GradCAM, Shapley, TracIn) applicables à n'importe quel modèle PyTorch, entrées comme couches ou neurones."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/SHAP|SHAP]]", "[[Dev/Services/interpreto|interpreto]]", "[[Dev/Services/nnsight|nnsight]]"]
remplace_par: []
status: actif
tags: [explainability, deep-learning]
url_docs: https://captum.ai/
url_repo: https://github.com/pytorch/captum
---

# Captum

## Pourquoi

Bibliothèque d'interprétabilité **officielle de l'écosystème PyTorch**, maintenue par Meta. Elle réunit sous une API unique une trentaine d'algorithmes d'attribution — la famille par gradient (Integrated Gradients, Saliency, SmoothGrad, GradCAM, DeepLift) comme celle par perturbation (Shapley, Occlusion, Feature Ablation).

Sa particularité tient à la **granularité** : Captum n'attribue pas seulement aux entrées, mais aussi aux **couches** (Layer Conductance) et aux **neurones** (Neuron Conductance). Elle couvre également l'attribution aux **exemples d'entraînement** (TracIn, fonctions d'influence) — « quelle donnée d'entraînement a causé cette prédiction ? », une question que ni SHAP ni LIME ne posent.

C'est la référence de fait dès qu'on travaille en PyTorch et qu'on veut autre chose que du model-agnostic.

## Quand l'utiliser

- Modèle **PyTorch**, quel qu'il soit (vision, texte, tabulaire, multimodal) — c'est son terrain naturel.
- Besoin d'[[Attribution par gradient|attributions par gradient]] : une rétropropagation plutôt que des milliers de passes de perturbation. Nettement plus rapide que [[Dev/Services/SHAP|SHAP]] sur un réseau.
- Attribuer à autre chose que l'entrée : à une couche interne, à un neurone, ou aux **données d'entraînement** (TracIn).
- Comparer plusieurs méthodes d'attribution sans réécrire le code d'accroche à chaque fois.
- Évaluer la fidélité des attributions (`captum.metrics` : infidelity, sensitivity).

## Quand NE PAS l'utiliser

- **Modèle non PyTorch** : conçue autour de `torch.autograd`. Pour un ensemble d'arbres ou du scikit-learn, utiliser [[Dev/Services/SHAP|SHAP]] (dont le TreeSHAP exact est imbattable) ou [[Dev/Services/LIME|LIME]].
- **Interprétabilité mécaniste** : Captum attribue, elle ne rétro-conçoit pas de circuits. Pour ça, [[Dev/Services/TransformerLens|TransformerLens]] ou [[Dev/Services/nnsight|nnsight]].
- **Méthodes à base de concepts sur modèles de langage** : le pipeline concept de bout en bout est le terrain d'[[Dev/Services/interpreto|interpreto]]. Captum a bien TCAV, mais pas la chaîne complète.
- **Explication destinée à un métier** : elle produit des tenseurs, pas des rapports. La couche de restitution est à écrire.

## Déploiement & coût

- `pip install captum` — bibliothèque Python, aucun service à déployer. Gratuit (BSD-3-Clause).
- Dépendance principale : `torch`. Aucune autre lourde.
- Exécution **single-node**, sur la machine du modèle. Coût = calcul : Integrated Gradients demande 20 à 300 passes avant/arrière par explication ; les méthodes par perturbation davantage.
- GPU conseillé dès que le modèle est gros ; l'attribution reste bien plus légère qu'un entraînement.

## Pièges

- **Le choix de la baseline dicte le résultat.** Integrated Gradients répond toujours « important par rapport à quoi ? ». Baseline nulle par défaut — ce qui rend les entrées nulles invisibles par construction. À expliciter systématiquement ([[Attribution par gradient]]).
- **Ne pas vérifier la complétude** : la somme des attributions IG doit valoir $f(x) - f(\text{baseline})$. Un écart signale un nombre de pas insuffisant. Le contrôle est gratuit et presque toujours omis.
- **Attribution ≠ causalité, et ≠ correction du modèle.** Une carte montre où le modèle regarde, pas s'il a raison.
- **Sur du texte, agréger au niveau du mot** avant d'afficher : les attributions par token sont trompeuses quand la tokenisation découpe les mots ([[Tokenization]]).
- API bas niveau : Captum donne des tenseurs bruts. La visualisation (`captum.attr.visualization`) reste sommaire hors vision.

## Alternatives

- [[Dev/Services/SHAP|SHAP]] — Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres.
- [[Dev/Services/interpreto|interpreto]] — Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs.
- [[Dev/Services/nnsight|nnsight]] — Bibliothèque d'intervention sur les internes d'un réseau PyTorch — capture et modifie activations et gradients via un contexte à exécution différée, et sait exécuter ces interventions à distance sur des modèles trop gros pour la machine locale (infrastructure NDIF).

## Liens

- [[Attribution par gradient]] — le concept parent : Saliency, IG, SmoothGrad, et pourquoi la saturation impose IG.
- [[Explicabilité des modèles]] — le chapeau de la famille.
- [[Dev/Patterns/Comparatif - Explicabilité|Comparatif - Explicabilité]] — le tableau de la famille.
- [[Dev/Services/PyTorch|PyTorch]] — le socle requis.
- [[CNN]] — le terrain d'origine de GradCAM.
- [[Interprétabilité mécaniste]] — l'étage au-dessus, hors périmètre de Captum.
