---
role: brique
nom: seaborn
alias: [sns]
pitch: "Surcouche statistique de matplotlib : graphiques soignés en une ligne (distributions, relations, catégories) directement depuis un DataFrame pandas."
categorie: data/viz
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[matplotlib]]"]
complements: []
tags: [dataviz, statistical-viz, static-viz]
url_docs: https://seaborn.pydata.org/
url_repo: https://github.com/mwaskom/seaborn
---

# seaborn

## Pourquoi

Surcouche **haut niveau** de [[matplotlib]] orientée **statistiques**. Prend un `DataFrame` [[pandas]] et produit des figures soignées en un appel : distributions (`histplot`, `kdeplot`), relations (`scatterplot`, `lmplot`), catégories (`boxplot`, `violinplot`), matrices (`heatmap`). Gère pour soi l'agrégation, les intervalles de confiance, le mapping couleur/facette. Depuis 0.12, l'interface **objects** (`seaborn.objects`, importée `so`) offre une grammaire des graphiques par couches. Le résultat reste une figure matplotlib, donc personnalisable à la main.

## Quand l'utiliser

- Visualisation **exploratoire statistique** rapide depuis un DataFrame.
- Graphes courants jolis par défaut, sans régler matplotlib à la main.
- Facettes (`FacetGrid`, `relplot`) pour décliner un graphe par sous-groupes.
- Intervalles de confiance / régressions tracés automatiquement (`lmplot`, `regplot`).

## Quand NE PAS l'utiliser

- Besoin de contrôle fin / figure composée sur mesure → [[matplotlib]] directement.
- Interactivité web (zoom, survol, dashboards) → [[plotly]], [[bokeh]] ou [[altair]].
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

- [[matplotlib]] — Socle de la visualisation Python : API impérative bas niveau pour des graphiques statiques entièrement contrôlables (PNG/SVG/PDF), base de presque tout l'écosystème viz.

## Liens

- Bâtie sur [[matplotlib]] ; consomme des DataFrames [[pandas]].
- [[Comparatif - Visualisation]] — seaborn vs matplotlib / plotly / altair / bokeh.
- Doc : https://seaborn.pydata.org/
