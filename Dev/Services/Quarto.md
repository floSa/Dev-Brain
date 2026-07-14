---
galaxie: dev
type: service
nom: Quarto
alias: [quarto]
pitch: "Système de publication scientifique multi-format (HTML, PDF, Word, sites, slides) à partir de Markdown et de notebooks, bâti sur Pandoc, polyglotte (Python/R/Julia)."
categorie: tooling/notebook
licence_type: open-source
hosted: self
maturite: production
langage: TypeScript
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [notebook, reproducibility]
url_docs: https://quarto.org/
url_repo: https://github.com/quarto-dev/quarto-cli
---

# Quarto

## Pourquoi

Système de **publication scientifique et technique** : à partir de Markdown enrichi (`.qmd`) ou de notebooks Jupyter, Quarto **exécute le code** embarqué puis **rend** le document en HTML, PDF (LaTeX), Word, présentations (reveal.js, Beamer, PowerPoint), sites web et livres. Bâti sur **Pandoc**, il ajoute les références croisées, figures numérotées, callouts, citations et mises en page propres à l'écrit technique. **Polyglotte** : le même outil sert Python, R, Julia et Observable JS. C'est un **CLI standalone** (binaire, embarque Pandoc) — pas une bibliothèque Python à importer — successeur unifié de R Markdown côté Posit.

## Quand l'utiliser

- Transformer une analyse (notebook ou `.qmd`) en **rapport mis en page** reproductible : HTML, PDF, slides.
- Publier un **site ou un livre** technique (documentation, blog, cours) à partir de sources Markdown + code exécuté.
- Mutualiser un pipeline de rendu entre **Python et R** dans une équipe polyglotte.
- Régénérer la sortie à chaque build pour garantir que le document reflète le code courant.

## Quand NE PAS l'utiliser

- Versionner proprement le notebook source en git (objectif code, pas publication) → [[Dev/Services/jupytext|jupytext]].
- Paramétrer et exécuter en masse des notebooks pour produire des artefacts `.ipynb`, sans rendu documentaire → [[Dev/Services/papermill|papermill]].
- Environnement notebook réactif au quotidien → [[Dev/Services/Marimo|Marimo]].
- Application interactive (widgets serveur, état) : Quarto produit du document, pas une web-app dynamique.

## Déploiement & coût

- CLI à installer (binaire standalone, ou via `uv tool`/conda) ; rendu local par `quarto render`, prévisualisation par `quarto preview`. MIT, gratuit, single-node.
- Le rendu PDF requiert une distribution **TeX** (`quarto install tinytex`) ; le HTML/Word n'en a pas besoin.
- Intégré à VS Code, RStudio, JupyterLab. Coût nul côté licence ; le build tourne sur la machine ou en CI.

## Pièges

- Le rendu **réexécute le code** : un environnement non épinglé ([[Dev/Services/uv|uv]], lockfile) casse la reproductibilité du document.
- Chaîne PDF/LaTeX lourde et source d'erreurs cryptiques : préférer le HTML quand le PDF n'est pas requis.
- Outil externe (binaire), pas un module Python : à provisionner explicitement en CI / image Docker.
- `.qmd` ≠ notebook : c'est du Markdown source ; l'aller-retour avec `.ipynb` se fait via les formats Quarto, pas automatiquement.

## Alternatives

- _Pas d'autre système de publication multi-format fiché à ce jour. `jupyter nbconvert` couvre un rendu plus simple sans la couche Pandoc/références croisées (non fiché)._

## Liens

- [[Notebooks-as-code]] — le rendu reproductible suppose un notebook exécutable de bout en bout.
- [[Dev/Services/papermill|papermill]] — exécution paramétrée en amont d'un rendu Quarto dans un pipeline.
- [[Dev/Services/uv|uv]] — environnement épinglé qui rend le `quarto render` reproductible.
- Doc : https://quarto.org/
