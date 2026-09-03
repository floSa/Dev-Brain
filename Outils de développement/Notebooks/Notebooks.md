---
role: hub
nom: Notebooks
alias: [notebook, jupyter]
pitch: Exécuter du code par cellules, avec le résultat à côté — et le faire sans sacrifier le diff, la revue et le versionnage.
domaines: [data-sci, data-eng, ml-eng]
tags: [notebook, reproducibility, version-control]
---

# Notebooks

> Exécuter du code par cellules, avec le résultat à côté — et le faire sans sacrifier le diff, la revue et le versionnage.

## Ce qu'il faut comprendre

- Le notebook est un excellent outil d'**exploration** et un mauvais **format de fichier**. Un `.ipynb` est du JSON qui embarque les sorties : le diff est illisible, la revue en PR impossible, et le dépôt grossit d'images base64.
- Deux stratégies répondent au problème, et elles ne se ressemblent pas. **Apparier** un notebook à un fichier texte ([[jupytext]]) garde Jupyter et rend le code versionnable. **Changer de format** ([[Marimo]]) supprime le `.ipynb` : le notebook *est* un `.py`.
- L'**état caché** est l'autre défaut structurel : dans Jupyter, l'ordre d'exécution des cellules n'est pas celui de leur affichage, donc un notebook qui marche à l'écran peut ne pas se rejouer. [[Marimo]] le règle par un graphe de dépendances entre cellules ; [[papermill]] le contourne en n'exécutant que de haut en bas.
- Un notebook devient un **artefact de production** dès qu'on veut le rejouer avec des paramètres ([[papermill]]) ou le publier ([[Quarto]]). C'est là qu'il faut arrêter de le traiter comme un brouillon.
- La discipline qui tient tout ça ensemble a sa page : [[Notebooks-as-code]] — apparier, sortir les sorties du dépôt, linter et tester le pendant `.py`. Les briques de ce dossier en sont l'outillage.

## Choisir

- Rester sur Jupyter, mais versionner proprement → [[jupytext]], apparié en `.py:percent` ou `.md`.
- Repartir de zéro, sans état caché ni JSON → [[Marimo]], qui déploie aussi le notebook en application.
- Rejouer un notebook en CI ou à l'heure, avec des paramètres → [[papermill]].
- Publier en HTML, PDF, site ou slides, éventuellement multi-langages → [[Quarto]].
- Interroger une base ou du [[DuckDB]] depuis une cellule → [[jupysql]], et le SQL reste du SQL.

<!-- AUTO:START -->
### Notions
- [[Notebooks-as-code]] — domaines : data-sci, mlops

### Briques
- [[jupysql]] — SQL natif dans Jupyter via les magics `%sql` / `%%sql` — requêter une base ou DuckDB depuis un notebook, paramétrer, composer en CTE et tracer les résultats.
- [[jupytext]] — Apparie chaque notebook Jupyter à un fichier texte (`.py` ou `.md`) synchronisé — diff propre, revue en PR et versionnage git du code sans les sorties JSON.
- [[Marimo]] — Notebook Python réactif stocké en `.py` pur — réexécution automatique des cellules dépendantes, pas d'état caché, déployable en app ou exécutable en script.
- [[papermill]] — Paramètre et exécute des notebooks Jupyter par API ou CLI — injecte des paramètres dans une cellule taguée et produit un notebook exécuté, pour rejouer/planifier en CI.
- [[Quarto]] — Système de publication scientifique multi-format (HTML, PDF, Word, sites, slides) à partir de Markdown et de notebooks, bâti sur Pandoc, polyglotte (Python/R/Julia).
<!-- AUTO:END -->
