---
galaxie: dev
type: service
nom: jupytext
alias: [Jupytext]
pitch: "Apparie chaque notebook Jupyter à un fichier texte (`.py` ou `.md`) synchronisé — diff propre, revue en PR et versionnage git du code sans les sorties JSON."
categorie: tooling/notebook
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: [Marimo]
remplace_par: []
status: actif
tags: [notebook, version-control, reproducibility]
url_docs: https://jupytext.readthedocs.io/
url_repo: https://github.com/mwouts/jupytext
---

# jupytext

## Pourquoi

Maintient une **paire** notebook ↔ fichier texte : un `.ipynb` reste l'artefact d'exécution, mais le **code et le markdown** vivent dans un `.py` (format `percent`, cellules `# %%`), un `.md` ou un `.qmd` synchronisé automatiquement. Le texte ne contient **pas les sorties** : le diff git devient lisible, mergeable et relisible en PR. On versionne le pendant texte et on **gitignore** le `.ipynb`. C'est l'implémentation canonique du [[Notebooks-as-code]] : le notebook redevient du vrai code, sans changer d'environnement Jupyter.

## Quand l'utiliser

- Versionner des notebooks dans git avec des **diffs propres** et des revues de PR exploitables.
- Garder Jupyter comme environnement d'édition tout en éditant le `.py` dans un IDE ([[Dev/Services/Ruff|Ruff]], complétion, refactor).
- Linter et tester le pendant `.py` ([[Dev/Services/pytest|pytest]]) comme un module ordinaire.
- Convertir en masse entre formats (`jupytext --to`) ou imposer un pairing via `jupytext.toml`.

## Quand NE PAS l'utiliser

- Repartir d'un environnement neuf sans état caché par construction → [[Dev/Services/Marimo|Marimo]] (notebook réactif en `.py` pur, sans pairing).
- Seulement exécuter/paramétrer un notebook headless en CI → [[Dev/Services/papermill|papermill]].
- Publier le notebook en HTML/PDF mis en page → [[Dev/Services/Quarto|Quarto]].
- Notebook jetable, non versionné : le pairing n'apporte rien.

## Déploiement & coût

- Bibliothèque Python (`uv add jupytext`) + extension Jupyter ; CLI `jupytext`. MIT, gratuit, single-node.
- Mise en place : `jupytext --set-formats ipynb,py:percent notebook.ipynb`, ou un `jupytext.toml` à la racine. Commiter le `.py`, gitignorer le `.ipynb`.
- Coût nul côté infra ; suit le kernel Jupyter de l'utilisateur.

## Pièges

- L'**état caché** (cellules exécutées dans le désordre) casse la reproductibilité du pendant texte : *Restart & Run All* avant de commiter.
- Le pairing ne nettoie pas un `.ipynb` déjà commité avec ses sorties → `nbstripout` en complément.
- Garder un seul format source de vérité : éditer simultanément le `.ipynb` et le `.py` sans resync provoque des conflits.
- Les métadonnées de cellule riches (widgets, tags spécifiques) peuvent ne pas survivre à un aller-retour texte.

## Alternatives

- [[Dev/Services/Marimo|Marimo]] — Notebook Python réactif stocké en `.py` pur — réexécution automatique des cellules dépendantes, pas d'état caché, déployable en app ou exécutable en script.

## Liens

- [[Notebooks-as-code]] — le concept que jupytext implémente concrètement.
- [[Dev/Services/papermill|papermill]] — exécution non interactive du notebook en CI, complémentaire au pairing.
- [[Dev/Services/Ruff|Ruff]] / [[Dev/Services/pytest|pytest]] — appliqués au pendant `.py`.
- Doc : https://jupytext.readthedocs.io/
