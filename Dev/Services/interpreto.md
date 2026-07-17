---
galaxie: dev
type: service
nom: interpreto
alias: [Interpreto, FOR-sight interpreto]
pitch: "Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs."
categorie: ml/framework
licence_type: open-source
hosted: self
maturite: experimental
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/SHAP|SHAP]]", "[[Dev/Services/LIME|LIME]]"]
remplace_par: []
status: actif
tags: [explainability, llm, nlp]
url_docs: https://for-sight-ai.github.io/interpreto/
url_repo: https://github.com/FOR-sight-ai/interpreto
---

# interpreto

## Pourquoi

Bibliothèque d'explicabilité **post-hoc** dédiée aux modèles de langage HuggingFace, des encodeurs type BERT jusqu'aux LLM décodeurs. Elle réunit deux familles habituellement dispersées dans des outils séparés : les **attributions** (quel token a pesé sur la sortie) et les **méthodes à base de concepts** (quelles notions le modèle a-t-il encodées dans ses activations).

Sa différence revendiquée est le **pipeline concept de bout en bout** — extraction d'activations, apprentissage du dictionnaire de concepts, interprétation, puis scoring — là où la plupart des bibliothèques s'arrêtent aux attributions au niveau des variables. Elle couvre classification **et** génération sous la même API.

Projet des équipes FOR et DEEL de l'**IRT Saint-Exupéry** (Toulouse), soutenu par ANITI, avec Ampere, Renault Group, Thales, CentraleSupélec et l'IRIT. Papier : [arXiv 2512.09730](https://arxiv.org/abs/2512.09730).

## Quand l'utiliser

- Expliquer un modèle de langage HuggingFace **déjà entraîné**, en classification comme en génération.
- Aller **au-delà de l'attribution par token** : découvrir les concepts encodés dans les activations (probes supervisés, dictionnaires appris non supervisés — NMF, ICA, SAE), les interpréter et les scorer.
- Comparer plusieurs méthodes d'attribution sous une API unique plutôt que d'assembler `shap` + `lime` + du code maison.
- **Évaluer** la qualité des explications, pas seulement les produire : métriques d'insertion/suppression pour les attributions, ConSim / erreur de reconstruction / parcimonie / stabilité pour les concepts.
- Contexte industriel où l'exigence d'explicabilité est réglementaire ou contractuelle — c'est précisément l'origine du projet.

## Quand NE PAS l'utiliser

- **Modèles tabulaires** (arbres, boosting, linéaires) : hors périmètre. Utiliser [[Dev/Services/SHAP|SHAP]] — dont le TreeSHAP exact est imbattable sur les ensembles d'arbres — ou [[Dev/Services/LIME|LIME]].
- **Vision** : la bibliothèque cible les modèles de langage, pas les modèles d'image.
- **Besoin de stabilité d'API** : le projet est déclaré *Development Status :: 3 - Alpha* en version 0.5.0. Les signatures bougent encore.
- **Modèle non HuggingFace** : l'intégration passe par `transformers` et `nnsight`.

## Déploiement & coût

- `pip install interpreto` — bibliothèque Python pure, Python ≥ 3.10, aucun service à déployer. Gratuit (MIT).
- Dépendances lourdes : `transformers`, `torch`, `nnsight`, plus `scikit-learn`, `scipy`, `einops`, `nltk`.
- Exécution **single-node**, sur la machine qui héberge le modèle. Le coût réel est le **calcul** : les méthodes par gradient exigent une rétropropagation par explication, les méthodes par perturbation (KernelShap, LIME, Sobol) multiplient les passes avant. Sur un gros LLM, une explication n'est pas gratuite.
- GPU vivement conseillé dès que le modèle dépasse la taille d'un BERT.

## Pièges

- **Maturité alpha** : le classifier PyPI déclare `3 - Alpha` malgré une documentation soignée et un papier. Épingler la version en production.
- **Le pipeline concept n'est pas magique** : un dictionnaire appris (SAE, NMF) produit des directions, pas des concepts nommés. L'étape d'interprétation (TopKInputs, labels par LLM) reste une lecture humaine ou assistée, avec sa part d'arbitraire.
- **Attributions ≠ causalité** : une attribution dit ce qui corrèle avec la sortie, pas ce qui la cause. Piège commun à toute la famille ([[Explicabilité des modèles]]).
- **Coût des méthodes par perturbation** sur les séquences longues : le nombre de passes avant explose avec la taille du contexte.
- Ne pas confondre les deux `alpha` du domaine ni les familles : les attributions expliquent **une prédiction**, les concepts décrivent **le modèle**. Ce ne sont pas deux façons de répondre à la même question.

## Alternatives

- [[Dev/Services/SHAP|SHAP]] — Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres.
- [[Dev/Services/LIME|LIME]] — Explications locales model-agnostic par surrogate linéaire — perturbe autour d'un point et ajuste un modèle simple interprétable ; rapide et générique (tabulaire, texte, image), mais explications instables et purement locales.

## Liens

- [[Explicabilité des modèles]] — le concept parent : familles de méthodes, limites, et pourquoi une explication n'est pas une cause.
- [[Dev/Patterns/Comparatif - Explicabilité|Comparatif - Explicabilité]] — le tableau de la famille.
- [[Traitement du langage naturel]] — le domaine visé.
- [[Transformer architectures]] / [[Self-attention]] — les modèles que la bibliothèque instrumente.
- [[Classification de texte]] — la tâche la plus courante à expliquer.
- [[Dev/Services/HuggingFace|HuggingFace]] — l'écosystème de modèles requis.
- [[Dev/Services/PyTorch|PyTorch]] — le backend d'exécution.
- Papier : [arXiv 2512.09730](https://arxiv.org/abs/2512.09730) — *Interpreto: An Explainability Library for Transformers*.
