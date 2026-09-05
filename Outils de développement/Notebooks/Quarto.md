---
role: brique
nom: Quarto
alias: [quarto]
pitch: "Système de publication scientifique multi-format (HTML, PDF, Word, sites, slides) à partir de Markdown et de notebooks, bâti sur Pandoc, polyglotte (Python/R/Julia)."
categorie: devtools/notebook
famille: cli
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: []
complements: []
tags: [notebook, reproducibility]
url_docs: https://quarto.org/
url_repo: https://github.com/quarto-dev/quarto-cli
---

# Quarto

<!-- AUTO:BANDEAU:START -->
> Système de publication scientifique multi-format (HTML, PDF, Word, sites, slides) à partir de Markdown et de notebooks, bâti sur Pandoc, polyglotte (Python/R/Julia).

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| CLI TypeScript | open-source | en ligne de commande, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Système de publication scientifique et technique. À partir de Markdown enrichi (`.qmd`) ou
de notebooks Jupyter, Quarto **exécute** le code embarqué puis **rend** le document : HTML,
PDF par LaTeX, Word, présentations (reveal.js, Beamer, PowerPoint), sites web et livres.
Bâti sur **Pandoc**, il ajoute ce que l'écrit technique réclame et que Markdown n'a pas —
références croisées, figures numérotées, callouts, citations. Polyglotte : le même outil
sert Python, R, Julia et Observable JS. C'est un binaire autonome qui embarque Pandoc, pas
un module Python à importer, et le successeur unifié de R Markdown côté Posit. `.qmd` n'est
pas un notebook : c'est du Markdown source, et l'aller-retour avec `.ipynb` passe par les
formats Quarto, pas automatiquement.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Transformer une analyse — notebook ou `.qmd` — en rapport mis en page reproductible : HTML, PDF, slides | Versionner proprement le notebook source, objectif code et non publication → [[jupytext]] |
| Publier un site ou un livre technique à partir de sources Markdown et de code exécuté | Exécuter en masse des notebooks paramétrés pour produire des `.ipynb`, sans rendu documentaire → [[papermill]] |
| Mutualiser un pipeline de rendu entre Python et R dans une équipe polyglotte | Environnement notebook réactif au quotidien → [[Marimo]] |
| Régénérer la sortie à chaque build, pour que le document reflète le code courant | Application interactive à état et widgets serveur : Quarto produit un document, pas une web-app |
| | La chaîne PDF/LaTeX est lourde et ses erreurs sont cryptiques : préférer le HTML quand le PDF n'est pas requis |

## Mise en œuvre

- Installation — binaire autonome, ou via `uv tool` et conda
- Point d'entrée — ligne de commande : `quarto render` pour produire, `quarto preview` pour prévisualiser
- Prérequis — le rendu réexécute le code, donc un environnement épinglé ([[uv]], lockfile) conditionne la reproductibilité ; le PDF demande une distribution TeX (`quarto install tinytex`)
- Exécution — sur le poste ou en CI ; outil externe à provisionner explicitement dans l'image, ce n'est pas un module Python. Intégré à VS Code, RStudio et JupyterLab
- Coût — gratuit sous licence MIT

## Ressources

- Documentation — https://quarto.org/
- Dépôt — https://github.com/quarto-dev/quarto-cli

## Voir aussi

- [[Notebooks]] — le hub du dossier
- [[Notebooks-as-code]] — la notion du dossier : un rendu reproductible suppose un notebook exécutable de bout en bout
