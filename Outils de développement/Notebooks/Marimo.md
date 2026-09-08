---
role: brique
nom: Marimo
alias: [marimo]
pitch: "Notebook Python réactif stocké en `.py` pur — réexécution automatique des cellules dépendantes, pas d'état caché, déployable en app ou exécutable en script."
categorie: devtools/notebook
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: single-node
alternatives: [jupytext]
complements: []
tags: [notebook, reproducibility, data-app]
url_docs: https://docs.marimo.io/
url_repo: https://github.com/marimo-team/marimo
---

# Marimo

<!-- AUTO:BANDEAU:START -->
> Notebook Python réactif stocké en `.py` pur — réexécution automatique des cellules dépendantes, pas d'état caché, déployable en app ou exécutable en script.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Python | open-source | self-hébergé · mono-nœud | production | à jour · 2026-08-17 |
<!-- AUTO:BANDEAU:END -->

## Définition

Notebook **réactif** : Marimo lit le graphe de dépendances entre cellules et réexécute
automatiquement celles qui dépendent d'une variable modifiée. L'ordre d'exécution ne peut
donc plus diverger de l'ordre du code, et l'état caché — le défaut qui mine la
reproductibilité de Jupyter — devient impossible. La contrepartie est une contrainte de
modèle : une cellule ne peut pas redéfinir une variable déclarée dans une autre. Le notebook
est stocké en `.py` pur, sans JSON ni appariement à tenir : versionnable, lintable,
importable et exécutable comme un script. Le même fichier s'ouvre en éditeur, se sert en
application web interactive ou s'exécute en batch. Projet affilié NumFOCUS.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Environnement notebook reproductible par construction, sans discipline manuelle de *Restart & Run All* | Écosystème Jupyter en place qu'on veut garder, en n'ajoutant que le versionnage propre → [[jupytext]] |
| Construire une data-app interactive en Python pur depuis le fichier même de l'analyse | Exécution paramétrée d'un `.ipynb` existant en CI → [[papermill]] |
| Versionner des notebooks dans git nativement, sans outil d'appariement | Publication documentaire multi-format mise en page → [[Quarto]] |
| Exécuter le notebook en script paramétrable (`marimo run`) ou l'exporter | Dépendance à des extensions ou widgets Jupyter non portés : l'écosystème est plus jeune, et l'export `.ipynb` n'est pas un drop-in de l'API notebook |

## Mise en œuvre

- Installation — `uv add marimo`
- Point d'entrée — `marimo edit` pour l'éditeur, `marimo run` pour servir l'application ; le fichier édité est un `.py`
- Prérequis — Python ; du code écrit pour un flux séquentiel impératif demande une réorganisation avant de passer au modèle réactif
- Exécution — process Python (ASGI) pour l'application servie, ou export WASM pour tourner dans le navigateur sans serveur
- Coût — gratuit sous licence Apache 2.0

## Écosystème

### Alternatives

- [[jupytext]] — Apparie chaque notebook Jupyter à un fichier texte (`.py` ou `.md`) synchronisé — diff propre, revue en PR et versionnage git du code sans les sorties JSON.

## Ressources

- Documentation — https://docs.marimo.io/
- Dépôt — https://github.com/marimo-team/marimo

## Voir aussi

- [[Notebooks]] — le hub du dossier
- [[Notebooks-as-code]] — la notion du dossier, que Marimo pousse à l'extrême
