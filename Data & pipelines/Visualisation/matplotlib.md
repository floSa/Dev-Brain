---
role: brique
nom: matplotlib
alias: [mpl, plt, pyplot]
pitch: "Socle de la visualisation Python : API impérative bas niveau pour des graphiques statiques entièrement contrôlables (PNG/SVG/PDF), base de presque tout l'écosystème viz."
categorie: data/viz
famille: paquet
licence_type: open-source
maturite: production
langage: Python / C++
alternatives: ["[[seaborn]]"]
complements: []
tags: [dataviz, static-viz]
url_docs: https://matplotlib.org/stable/
url_repo: https://github.com/matplotlib/matplotlib
---

# matplotlib

<!-- AUTO:BANDEAU:START -->
> Socle de la visualisation Python : API impérative bas niveau pour des graphiques statiques entièrement contrôlables (PNG/SVG/PDF), base de presque tout l'écosystème viz.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python / C++ | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Bibliothèque fondatrice de la visualisation Python. Deux interfaces cohabitent : `pyplot`,
de style MATLAB, *stateful* et rapide à écrire, et l'API **orientée objet**
(`Figure` / `Axes`), qui seule donne du code reproductible — l'état global de `pyplot`, la
« figure courante », surprend dès qu'un script boucle ou s'allonge. Le rendu est **statique**
par défaut vers PNG, SVG et PDF via des backends (Agg, écrit en C++), avec des backends
interactifs Qt, Tk ou notebook. Sa raison d'être est le contrôle **total** de chaque élément
du graphique, ce qui explique sa verbosité. C'est le socle de presque tout l'écosystème :
[[seaborn]], le `.plot` de [[pandas]], le rendu statique de bien d'autres bibliothèques.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Figures *publication-ready* : axes multiples, annotations, composition, export vectoriel | Deux API mélangées, `pyplot` *stateful* contre l'API objet : le code durable impose de choisir l'API objet |
| Contrôle **au pixel** de chaque composant — ticks, légendes, colorbars | L'état global de `pyplot` produit des surprises en script long ou en boucle |
| Sortie statique pour rapport PDF ou LaTeX, article, slides | Verbeux même pour des graphes simples — c'est le coût du contrôle total |
| Servir de socle à une bibliothèque maison : produire des figures par programme, sans dépendance web | En génération massive, les figures doivent être fermées (`plt.close`) sous peine de fuite mémoire |

## Mise en œuvre

- Installation — `uv add matplotlib`
- Point d'entrée — import Python, `import matplotlib.pyplot as plt` ; API objet via `plt.subplots()`
- Prérequis — Python ; un backend interactif (Qt, Tk) seulement si l'on veut une fenêtre
- Exécution — dans le process appelant, mono-nœud ; rendu local, les extensions critiques sont en C++
- Coût — gratuit, licence Matplotlib de style BSD/PSF, aucune limite d'usage

## Écosystème

### Alternatives

- [[seaborn]] — Surcouche statistique de matplotlib : graphiques soignés en une ligne (distributions, relations, catégories) directement depuis un DataFrame pandas.

## Ressources

- Documentation — https://matplotlib.org/stable/
- Dépôt — https://github.com/matplotlib/matplotlib

## Voir aussi

- [[Visualisation]] — le hub du dossier
- [[pandas]] — consommateur direct : `DataFrame.plot` produit des figures matplotlib
- [[Comparatif - Visualisation]] — ce qui départage les bibliothèques du dossier
