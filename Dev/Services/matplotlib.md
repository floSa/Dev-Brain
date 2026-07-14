---
galaxie: dev
type: service
nom: matplotlib
alias: [mpl, plt, pyplot]
pitch: "Socle de la visualisation Python : API impérative bas niveau pour des graphiques statiques entièrement contrôlables (PNG/SVG/PDF), base de presque tout l'écosystème viz."
categorie: tooling/viz
licence_type: open-source
hosted: self
maturite: production
langage: Python / C++
scaling: single-node
alternatives: ["[[Dev/Services/seaborn|seaborn]]"]
remplace_par: []
status: actif
tags: [dataviz, static-viz]
url_docs: https://matplotlib.org/stable/
url_repo: https://github.com/matplotlib/matplotlib
---

# matplotlib

## Pourquoi

Bibliothèque **fondatrice** de la visualisation Python. Deux interfaces : `pyplot` (style MATLAB, *stateful*, rapide à écrire) et l'API **orientée objet** (`Figure`/`Axes`, contrôle fin et reproductible). Rendu **statique** par défaut vers PNG/SVG/PDF via des backends (Agg en C++), plus des backends interactifs (Qt, Tk, notebook). Sa raison d'être : un contrôle **total** sur chaque élément du graphique. Quasi tout l'écosystème viz s'appuie dessus — [[Dev/Services/seaborn|seaborn]], le `.plot` de pandas, le rendu statique de nombreuses libs.

## Quand l'utiliser

- Graphiques *publication-ready* : figures composées, axes multiples, annotations, export vectoriel.
- Besoin de **contrôle au pixel** sur chaque composant (ticks, légendes, colorbars).
- Sortie statique pour rapports PDF/LaTeX, articles, slides.
- Socle d'une lib maison : produire des figures par programme sans dépendance web.

## Quand NE PAS l'utiliser

- Graphiques statistiques courants vite faits → [[Dev/Services/seaborn|seaborn]] (mêmes figures en une ligne).
- Interactivité web (zoom, survol, dashboards) → [[Dev/Services/plotly|plotly]], [[Dev/Services/bokeh|bokeh]] ou [[Dev/Services/altair|altair]].
- API verbeuse pour de l'exploratoire rapide → une surcouche haut niveau fait gagner du temps.

## Déploiement & coût

- Bibliothèque Python (`uv add matplotlib`) ; rien à héberger. Licence Matplotlib (style BSD/PSF), gratuit.
- **Single-node**, rendu local ; les extensions critiques (Agg) sont en C++.
- Sortie image (raster ou vectoriel) ou fenêtre interactive selon le backend choisi.

## Pièges

- Deux API mélangées (`pyplot` vs objet) : choisir l'API objet pour le code durable.
- État global de `pyplot` (figure courante) : source de surprises en scripts longs / boucles.
- Verbeux pour des graphes pourtant simples — d'où l'intérêt des surcouches.
- Penser à fermer les figures (`plt.close`) pour éviter les fuites en génération massive.

## Alternatives

- [[Dev/Services/seaborn|seaborn]] — Surcouche statistique de matplotlib : graphiques soignés en une ligne (distributions, relations, catégories) directement depuis un DataFrame pandas.

## Liens

- Surcouche statistique : [[Dev/Services/seaborn|seaborn]] — l'appelle sous le capot.
- Consommé par [[Dev/Services/pandas|pandas]] (`DataFrame.plot`).
- [[Dev/Patterns/Comparatif - Visualisation]] — matplotlib vs seaborn / plotly / altair / bokeh.
- Doc : https://matplotlib.org/stable/
