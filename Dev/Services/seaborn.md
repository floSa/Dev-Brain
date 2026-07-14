---
galaxie: dev
type: service
nom: seaborn
alias: [sns]
pitch: "Surcouche statistique de matplotlib : graphiques soignés en une ligne (distributions, relations, catégories) directement depuis un DataFrame pandas."
categorie: tooling/viz
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/matplotlib|matplotlib]]"]
remplace_par: []
status: actif
tags: [dataviz, statistical-viz, static-viz]
url_docs: https://seaborn.pydata.org/
url_repo: https://github.com/mwaskom/seaborn
---

# seaborn

## Pourquoi

Surcouche **haut niveau** de [[Dev/Services/matplotlib|matplotlib]] orientée **statistiques**. Prend un `DataFrame` [[Dev/Services/pandas|pandas]] et produit des figures soignées en un appel : distributions (`histplot`, `kdeplot`), relations (`scatterplot`, `lmplot`), catégories (`boxplot`, `violinplot`), matrices (`heatmap`). Gère pour soi l'agrégation, les intervalles de confiance, le mapping couleur/facette. Depuis 0.12, l'interface **objects** (`seaborn.objects`, importée `so`) offre une grammaire des graphiques par couches. Le résultat reste une figure matplotlib, donc personnalisable à la main.

## Quand l'utiliser

- Visualisation **exploratoire statistique** rapide depuis un DataFrame.
- Graphes courants jolis par défaut, sans régler matplotlib à la main.
- Facettes (`FacetGrid`, `relplot`) pour décliner un graphe par sous-groupes.
- Intervalles de confiance / régressions tracés automatiquement (`lmplot`, `regplot`).

## Quand NE PAS l'utiliser

- Besoin de contrôle fin / figure composée sur mesure → [[Dev/Services/matplotlib|matplotlib]] directement.
- Interactivité web (zoom, survol, dashboards) → [[Dev/Services/plotly|plotly]], [[Dev/Services/bokeh|bokeh]] ou [[Dev/Services/altair|altair]].
- Très gros volumes à tracer point par point → échantillonner ou agréger en amont.

## Déploiement & coût

- Bibliothèque Python (`uv add seaborn`) ; tire matplotlib, pandas, numpy. BSD-3-Clause, gratuit.
- **Single-node**, rendu statique (hérité de matplotlib) ; scipy/statsmodels en option pour certaines stats.
- Projet quasi mono-mainteneur (M. Waskom) : cadence de release lente, mais socle stable et mûr.

## Pièges

- C'est un wrapper : pour la touche finale, on retombe sur l'API matplotlib (récupérer l'`Axes`).
- Deux API coexistent (fonctions historiques vs `seaborn.objects`) — choisir et s'y tenir.
- Les styles globaux (`set_theme`) modifient l'état matplotlib partagé.
- Pas d'interactivité : sortie image.

## Alternatives

- [[Dev/Services/matplotlib|matplotlib]] — Socle de la visualisation Python : API impérative bas niveau pour des graphiques statiques entièrement contrôlables (PNG/SVG/PDF), base de presque tout l'écosystème viz.

## Liens

- Bâtie sur [[Dev/Services/matplotlib|matplotlib]] ; consomme des DataFrames [[Dev/Services/pandas|pandas]].
- [[Dev/Patterns/Comparatif - Visualisation]] — seaborn vs matplotlib / plotly / altair / bokeh.
- Doc : https://seaborn.pydata.org/
