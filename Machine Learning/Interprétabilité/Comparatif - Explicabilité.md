---
role: comparatif
nom: Comparatif - Explicabilité
categorie: ml/interpretabilite
tags: [explainability, transformers, model-evaluation]
---

# Comparatif - Explicabilité

> On tranche sur : ce qu'on explique — une prédiction, un modèle ou un circuit —, le framework du modèle, et s'il tient sur la machine.

![[Comparatif - Explicabilité.base]]

## Ce qui départage

- [[SHAP]] — des attributions **additives qui somment à la prédiction**, donc agrégeables du local au global ; et `TreeSHAP`, exact et rapide sur les ensembles d'arbres, que rien d'autre n'égale. KernelSHAP, lui, devient prohibitif hors des arbres.
- [[LIME]] — un surrogate linéaire ajusté sur des perturbations : générique et léger, mais **instable d'un tirage à l'autre** et purement local. Dépôt sans commit depuis juillet 2021, dernière release en juin 2020.
- [[Captum]] — attributions **par gradient** (une rétropropagation au lieu de milliers de perturbations), et la seule à descendre jusqu'à la couche, au neurone, et jusqu'aux **exemples d'entraînement** (TracIn). Fermée à `torch.autograd`.
- [[TransformerLens]] — réécrit les poids en **notation canonique** : têtes d'attention séparées, flux résiduel décomposé. C'est ce qui rend le raisonnement en circuits praticable, au prix d'un chargement entièrement local et gourmand en mémoire.
- [[nnsight]] — la même famille d'interventions, mais en **exécution différée** et surtout **à distance** via NDIF : le seul par lequel un très gros modèle s'instrumente depuis une machine ordinaire. Il garde le modèle HuggingFace tel quel, sans notation canonique.
- [[SAELens]] — ne fait que des sparse autoencoders, et c'est son **catalogue de SAE déjà entraînés** qui compte : entraîner coûte des millions d'activations, charger prend trois lignes.
- [[interpreto]] — le seul à porter le pipeline concept de bout en bout (extraction, dictionnaire, interprétation, scoring) et à le **scorer** ; limité aux modèles de langage HuggingFace, et déclaré alpha en 0.5.0.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
