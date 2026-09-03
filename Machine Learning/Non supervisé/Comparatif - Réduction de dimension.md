---
role: comparatif
nom: Comparatif - Réduction de dimension
categorie: ml/non-supervise
tags: [dimensionality-reduction, manifold, factor-analysis]
---

# Comparatif - Réduction de dimension

> On tranche sur : des axes qu'on interprète ou une variété qu'on apprend, et ce que la projection doit préserver — le voisinage local ou la forme d'ensemble.

![[Comparatif - Réduction de dimension.base]]

## Ce qui départage

- [[Scikit-Learn]] — PCA, `KernelPCA`, `FastICA` et `NMF` dans la **même grammaire** `fit`/`transform` que le reste du pipeline, sans dépendance de plus ; tout reste en mémoire single-node, et la PCA est sensible à l'échelle.
- [[umap-learn]] — variété apprise, plus rapide que t-SNE, et le seul de la famille manifold à savoir **projeter des points nouveaux** (`transform`) et à accepter des labels en mode supervisé. Très sensible à `n_neighbors` et `min_dist`.
- [[PaCMAP]] — trois familles de paires dont les **mid-near** : la structure globale est préservée en même temps que la locale, et le résultat est plus robuste au choix d'hyperparamètres. API encore sous la 1.0, écosystème restreint.
- [[Prince]] — toute la famille factorielle, pas seulement la PCA : CA, MCA, FAMD, MFA, GPA, sur DataFrames pandas indexés, avec lignes et colonnes supplémentaires.
- [[Fanalysis]] — les **aides à l'interprétation** façon FactoMineR (contributions, cos², valeurs-tests) plutôt que les coordonnées seules ; limité à PCA/CA/MCA, aucun commit depuis le 4 juin 2018, resté en v0.0.1.
