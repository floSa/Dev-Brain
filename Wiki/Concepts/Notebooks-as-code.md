---
galaxie: wiki
type: concept
nom: Notebooks-as-code
alias: [notebooks as code, jupytext, pairing de notebooks, notebook pairing, notebooks reproductibles, nbstripout]
categorie: concept/data
domaines: [data-sci, mlops]
tags: [notebook, reproducibility, version-control]
---

# Notebooks-as-code

## Aperçu

- Traiter les notebooks comme du **vrai code** : versionnés, relus, testés, reproductibles — au lieu de blobs `.ipynb` qu'on s'échange.
- [[Dev/Services/jupytext|jupytext]] apparie chaque notebook à un fichier texte (`.py` ou `.md`) synchronisé : on édite l'un ou l'autre, le `.ipynb` redevient un simple artefact.

## Concepts clés

### Le problème du .ipynb
- Un `.ipynb` est un **JSON** mêlant code, sorties, métadonnées et compteurs d'exécution. Diff illisible, conflits de merge sur les sorties, secrets et gros outputs committés par accident. Revue de code quasi impossible.

### Pairing jupytext
- [[Dev/Services/jupytext|jupytext]] maintient une **paire** notebook ↔ script. Le `.py` (format `percent`, cellules `# %%`) ou le `.md` ne contient **que le code et le markdown**, pas les sorties → diff propre, mergeable, relisible en PR. On versionne le texte et on **ignore** le `.ipynb`.

### Sorties hors du dépôt
- Corollaire : les sorties ne vivent pas dans git, on les régénère à l'exécution. `nbstripout` (filtre git) ou le pairing garantissent que les cellules de sortie ne polluent pas l'historique.

### Notebook → module
- Le pendant `.py` se **lint** ([[Dev/Services/Ruff|Ruff]]), se **teste** ([[Dev/Services/pytest|pytest]]) et s'importe comme un module. L'exécution non interactive ([[Dev/Services/papermill|papermill]], `jupyter nbconvert --execute`) permet de paramétrer et de rejouer un notebook en CI.

## Les maths, simplement

- Pas de maths : c'est une discipline d'outillage. L'invariant visé est l'**idempotence** à environnement figé — même entrée + même env épinglé ([[Dev/Services/uv|uv]], lockfile) → même sortie. Le pendant côté **données** est traité par [[Versionnage de données]].

## En pratique

- **Mise en place** : `jupytext --set-formats ipynb,py:percent notebook.ipynb`, ou un `jupytext.toml` ; activer le pairing dans Jupyter. Committer le `.py`, gitignore le `.ipynb`.
- **Revue** : la PR montre un diff Python lisible — on relit la logique, pas du JSON.
- **CI** : exécuter le notebook headless ([[Dev/Services/papermill|papermill]] / nbconvert) pour vérifier qu'il tourne de bout en bout ; échouer si une cellule lève.
- **Pièges** : l'**état caché** (cellules exécutées dans le désordre) casse la reproductibilité → *Restart & Run All* avant de committer. Les gros notebooks gagnent à voir leur cœur extrait en modules `.py` importés.
- **Alternatives d'outil** : [[Dev/Services/Quarto|Quarto]] (publication multi-format), [[Dev/Services/Marimo|Marimo]] (notebook réactif stocké en `.py` pur, sans état caché par construction).

## Approches voisines & alternatives

- [[Dev/Services/jupytext|jupytext]] — l'implémentation canonique du pairing notebook ↔ texte.
- [[Dev/Services/Marimo|Marimo]] — notebook réactif en `.py` pur : état caché impossible par construction.
- [[Dev/Services/papermill|papermill]] — exécution paramétrée et rejouable d'un notebook (CI, orchestration).
- [[Dev/Services/Quarto|Quarto]] — rendu publication multi-format (HTML/PDF/slides) d'un notebook reproductible.
- [[Versionnage de données]] — versionner le **code** d'un notebook ne versionne pas les **données** qu'il consomme ; complémentaire.
- [[Dev/Services/uv|uv]] — l'environnement épinglé (lockfile) qui rend l'exécution reproductible.
- [[Dev/Services/Ruff|Ruff]] / [[Dev/Services/pytest|pytest]] — appliqués au pendant `.py` du notebook.
- [[ELT vs ETL & idempotence]] — même exigence d'idempotence, côté pipelines de données.

## Pour aller plus loin

- [[Dev/Services/jupytext|jupytext]] — formats `percent` / `light` / `myst`, pairing, `jupytext.toml`.
- `nbstripout`, [[Dev/Services/papermill|papermill]], `nbconvert` — nettoyage et exécution non interactive.
- [[Dev/Services/Marimo|Marimo]], [[Dev/Services/Quarto|Quarto]] — approches notebook orientées reproductibilité / publication.
