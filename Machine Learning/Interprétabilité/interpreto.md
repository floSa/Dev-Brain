---
role: brique
nom: interpreto
alias: [Interpreto, FOR-sight interpreto]
pitch: "Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs."
categorie: ml/interpretabilite
famille: paquet
licence_type: open-source
maturite: experimental
langage: Python
alternatives: ["[[SHAP]]", "[[LIME]]", "[[Captum]]", "[[SAELens]]"]
complements: ["[[nnsight]]"]
tags: [explainability, llm, nlp]
url_docs: https://for-sight-ai.github.io/interpreto/
url_repo: https://github.com/FOR-sight-ai/interpreto
---

# interpreto

<!-- AUTO:BANDEAU:START -->
> Boîte à outils d'explicabilité post-hoc pour modèles de langage HuggingFace (BERT → LLM) — réunit attributions et méthodes à base de concepts sous une API unique, avec un pipeline concept de bout en bout (extraction d'activations → apprentissage → interprétation → scoring) rare ailleurs.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | experimental |
<!-- AUTO:BANDEAU:END -->

## Définition

Une bibliothèque d'explicabilité **post-hoc** dédiée aux modèles de langage HuggingFace, des encodeurs type BERT jusqu'aux LLM décodeurs. Elle réunit deux familles habituellement dispersées : les **attributions** — quel token a pesé sur la sortie — et les **méthodes à base de concepts** — quelles notions le modèle a encodées dans ses activations. Ce ne sont pas deux façons de répondre à la même question : une attribution explique **une prédiction**, un concept décrit **le modèle**. Sa différence revendiquée est le **pipeline concept de bout en bout** — extraction d'activations, apprentissage du dictionnaire, interprétation, puis scoring — là où la plupart des bibliothèques s'arrêtent aux attributions au niveau des variables ; elle couvre classification et génération sous la même API. Deux réserves de méthode : un dictionnaire appris (SAE, NMF) produit des **directions, pas des concepts nommés**, et l'étape d'interprétation reste une lecture humaine ou assistée, avec sa part d'arbitraire ; et une attribution dit ce qui **corrèle** avec la sortie, pas ce qui la cause. Projet des équipes FOR et DEEL de l'IRT Saint-Exupéry (Toulouse), soutenu par ANITI, avec Ampere, Renault Group, Thales, CentraleSupélec et l'IRIT.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Expliquer un modèle de langage HuggingFace déjà entraîné, en classification comme en génération | Modèles tabulaires — arbres, boosting, linéaires — hors périmètre → [[SHAP]], dont le TreeSHAP exact est imbattable, ou [[LIME]] |
| Aller au-delà de l'attribution par token : découvrir les concepts encodés (probes supervisés, dictionnaires NMF, ICA, SAE), les interpréter, les scorer | Vision : la bibliothèque cible les modèles de langage, pas les modèles d'image → [[Captum]] |
| Comparer plusieurs méthodes d'attribution sous une API unique, plutôt que d'assembler `shap`, `lime` et du code maison | Besoin de stabilité d'API : le projet est déclaré *Development Status :: 3 - Alpha* en 0.5.0, les signatures bougent encore |
| **Évaluer** la qualité des explications, pas seulement les produire : insertion/suppression pour les attributions, ConSim, reconstruction, parcimonie et stabilité pour les concepts | Modèle non HuggingFace : l'intégration passe par `transformers` et [[nnsight]] |
| Contexte industriel où l'exigence d'explicabilité est réglementaire ou contractuelle — c'est l'origine du projet | Travail centré sur les seuls SAE, à fond → [[SAELens]] |

## Mise en œuvre

- Installation — `uv add interpreto` ; Python ≥ 3.10, et **maturité alpha** malgré une documentation soignée et un papier — épingler la version en production
- Point d'entrée — import Python, API unique pour les deux familles (attributions et concepts)
- Prérequis — dépendances lourdes : `transformers`, `torch`, `nnsight`, plus `scikit-learn`, `scipy`, `einops`, `nltk`
- Exécution — single-node, sur la machine qui héberge le modèle ; GPU vivement conseillé dès que le modèle dépasse la taille d'un BERT
- Coût — gratuit, MIT ; le coût réel est le calcul — une rétropropagation par explication pour les méthodes par gradient, et un nombre de passes avant qui **explose avec la longueur du contexte** pour les méthodes par perturbation (KernelShap, LIME, Sobol)

## Écosystème

### Alternatives

- [[SHAP]] — Bibliothèque d'explicabilité fondée sur les valeurs de Shapley — attributions locales cohérentes (qui somment à la prédiction) pour n'importe quel modèle, avec un TreeSHAP exact et rapide pour les ensembles d'arbres.
- [[LIME]] — Explications locales model-agnostic par surrogate linéaire — perturbe autour d'un point et ajuste un modèle simple interprétable ; rapide et générique (tabulaire, texte, image), mais explications instables et purement locales ; dépôt sans commit depuis juillet 2021, dernière release en juin 2020 — préférer SHAP.
- [[Captum]] — Bibliothèque d'interprétabilité officielle de PyTorch (Meta) — une trentaine de méthodes d'attribution unifiées (Integrated Gradients, DeepLift, GradCAM, Shapley, TracIn) applicables à n'importe quel modèle PyTorch, entrées comme couches ou neurones.
- [[SAELens]] — Écosystème dédié aux sparse autoencoders sur modèles de langage — entraînement, catalogue de SAE pré-entraînés et outillage d'analyse des features, en intégration étroite avec TransformerLens.

### Compléments

- [[nnsight]] — Bibliothèque d'intervention sur les internes d'un réseau PyTorch — capture et modifie activations et gradients via un contexte à exécution différée, et sait exécuter ces interventions à distance sur des modèles trop gros pour la machine locale (infrastructure NDIF). — sa dépendance directe pour l'extraction d'activations.

## Ressources

- Documentation — https://for-sight-ai.github.io/interpreto/
- Dépôt — https://github.com/FOR-sight-ai/interpreto
- Papier — https://arxiv.org/abs/2512.09730 — *Interpreto: An Explainability Library for Transformers*

## Voir aussi

- [[Explicabilité des modèles]] — le concept parent : familles de méthodes, limites, et pourquoi une explication n'est pas une cause
- [[Attribution par gradient]] — sa moitié « attributions » : Saliency, Integrated Gradients, SmoothGrad, GradientShap
- [[Probing]] — ses sondes supervisées, linéaires et par centroïdes
- [[Sparse autoencoders]] — ses dictionnaires appris : Vanilla, TopK, JumpReLU, BatchTopK
- [[NMF]] · [[ICA]] — ses autres méthodes de dictionnaire, linéaires : les baselines honnêtes avant de sortir un SAE
- [[Interprétabilité mécaniste]] — le domaine dont relèvent ses méthodes à base de concepts
- [[Traitement du langage naturel]] · [[Classification de texte]] — le domaine visé, et la tâche la plus courante à expliquer
- [[Transformer architectures]] · [[Self-attention]] — les modèles instrumentés
- [[Comparatif - Explicabilité]] — ce qui départage les outils du dossier
- [[HuggingFace]] — l'écosystème de modèles requis
