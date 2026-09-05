---
role: brique
nom: jupytext
alias: [Jupytext]
pitch: "Apparie chaque notebook Jupyter à un fichier texte (`.py` ou `.md`) synchronisé — diff propre, revue en PR et versionnage git du code sans les sorties JSON."
categorie: devtools/notebook
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: [Marimo]
complements: ["[[papermill]]"]
tags: [notebook, version-control, reproducibility]
url_docs: https://jupytext.readthedocs.io/
url_repo: https://github.com/mwouts/jupytext
---

# jupytext

<!-- AUTO:BANDEAU:START -->
> Apparie chaque notebook Jupyter à un fichier texte (`.py` ou `.md`) synchronisé — diff propre, revue en PR et versionnage git du code sans les sorties JSON.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Maintient une **paire** notebook ↔ fichier texte. Le `.ipynb` reste l'artefact d'exécution,
mais le code et le markdown vivent dans un `.py` au format `percent` — cellules `# %%` —, un
`.md` ou un `.qmd`, synchronisé automatiquement. Le pendant texte ne contient **pas les
sorties** : le diff git redevient lisible, mergeable et relisible en revue de PR. La
discipline qui va avec tient en trois gestes : versionner le texte, gitignorer le `.ipynb`,
et garder un seul format comme source de vérité — éditer les deux sans resynchroniser
provoque des conflits. C'est l'implémentation canonique du notebook-as-code, sans changer
d'environnement Jupyter.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Versionner des notebooks avec des diffs propres et des revues de PR exploitables | Repartir d'un environnement sans état caché par construction → [[Marimo]] |
| Garder Jupyter comme environnement d'édition tout en éditant le `.py` dans un IDE | Seulement exécuter ou paramétrer un notebook headless en CI → [[papermill]] |
| Linter et tester le pendant `.py` ([[Ruff]], [[pytest]]) comme un module ordinaire | Publier le notebook en HTML ou PDF mis en page → [[Quarto]] |
| Convertir en masse entre formats, ou imposer l'appariement par un `jupytext.toml` | L'appariement ne nettoie pas un `.ipynb` déjà commité avec ses sorties, et les métadonnées de cellule riches — widgets, tags — peuvent ne pas survivre à l'aller-retour |

## Mise en œuvre

- Installation — `uv add jupytext` ; extension Jupyter et CLI `jupytext` fournies
- Point d'entrée — `jupytext --set-formats ipynb,py:percent notebook.ipynb`, ou un `jupytext.toml` à la racine
- Prérequis — un kernel Jupyter ; faire *Restart & Run All* avant de commiter, sinon l'état caché casse la reproductibilité du pendant texte
- Exécution — dans l'environnement Jupyter de l'utilisateur ; rien à héberger
- Coût — gratuit sous licence MIT

## Écosystème

### Alternatives

- [[Marimo]] — Notebook Python réactif stocké en `.py` pur — réexécution automatique des cellules dépendantes, pas d'état caché, déployable en app ou exécutable en script.

### Compléments

- [[papermill]] — Paramètre et exécute des notebooks Jupyter par API ou CLI — injecte des paramètres dans une cellule taguée et produit un notebook exécuté, pour rejouer/planifier en CI. — l'appariement versionne le source, papermill l'exécute

## Ressources

- Documentation — https://jupytext.readthedocs.io/
- Dépôt — https://github.com/mwouts/jupytext

## Voir aussi

- [[Notebooks]] — le hub du dossier
- [[Notebooks-as-code]] — la notion que jupytext implémente concrètement
