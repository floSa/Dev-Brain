---
galaxie: dev
type: service
nom: Marimo
alias: [marimo]
pitch: "Notebook Python réactif stocké en `.py` pur — réexécution automatique des cellules dépendantes, pas d'état caché, déployable en app ou exécutable en script."
categorie: tooling/notebook
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: [jupytext]
remplace_par: []
status: actif
tags: [notebook, reproducibility, data-app]
url_docs: https://docs.marimo.io/
url_repo: https://github.com/marimo-team/marimo
---

# Marimo

## Pourquoi

Notebook **réactif** nouvelle génération : Marimo lit le graphe de dépendances entre cellules et **réexécute automatiquement** celles qui dépendent d'une variable modifiée. Conséquence directe — **pas d'état caché** : l'ordre d'exécution ne peut plus diverger de l'ordre du code, le défaut qui mine la reproductibilité de Jupyter. Le notebook est **stocké en `.py` pur** (pas de JSON, pas de pairing à gérer comme avec [[Dev/Services/jupytext|jupytext]]) : versionnable, lintable, importable et exécutable comme un script. Le même fichier se lance en éditeur, se déploie en **application web** interactive (sliders, tables, plots) ou s'exécute en batch. Projet affilié NumFOCUS.

## Quand l'utiliser

- Vouloir un environnement notebook **reproductible par construction**, sans discipline manuelle de *Restart & Run All*.
- Construire une **data-app** interactive en Python pur depuis le même fichier que l'analyse (alternative à Streamlit).
- Versionner des notebooks en git nativement, sans outil de pairing.
- Exécuter le notebook comme script paramétrable (`marimo run`, CLI) ou l'exporter.

## Quand NE PAS l'utiliser

- Écosystème Jupyter déjà en place qu'on veut garder, en ajoutant seulement le versionnage propre → [[Dev/Services/jupytext|jupytext]].
- Dépendance forte à des extensions/widgets de l'écosystème Jupyter classique non portés sous Marimo.
- Simple exécution paramétrée d'un notebook `.ipynb` existant en CI → [[Dev/Services/papermill|papermill]].
- Publication documentaire multi-format mise en page → [[Dev/Services/Quarto|Quarto]].

## Déploiement & coût

- Bibliothèque Python (`uv add marimo`) ; `marimo edit` pour l'éditeur, `marimo run` pour servir l'app. Apache 2.0, gratuit, single-node.
- Déploiement app : process Python (uvicorn/ASGI sous le capot) ou export WASM pour exécuter dans le navigateur sans serveur.
- Coût nul côté licence ; l'app servie suit la taille du process Python.

## Pièges

- Modèle mental réactif différent de Jupyter : une cellule ne peut pas **redéfinir** une variable d'une autre cellule (contrainte qui garantit justement l'absence d'état caché).
- Pas de cellules « out of order » : du code conçu pour un flux séquentiel impératif peut demander une réorganisation.
- Écosystème plus jeune que Jupyter : moins d'extensions tierces, intégrations en cours de maturation.
- L'export en `.ipynb` existe mais Marimo n'est pas un drop-in de l'API notebook Jupyter.

## Alternatives

- [[Dev/Services/jupytext|jupytext]] — Apparie chaque notebook Jupyter à un fichier texte (`.py` ou `.md`) synchronisé — diff propre, revue en PR et versionnage git du code sans les sorties JSON.

## Liens

- [[Notebooks-as-code]] — Marimo pousse le principe à l'extrême : `.py` pur, état caché impossible.
- [[Dev/Services/jupytext|jupytext]] — l'autre voie (pairing) pour le même objectif de versionnage propre.
- Doc : https://docs.marimo.io/
