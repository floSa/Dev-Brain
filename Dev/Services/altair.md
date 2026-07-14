---
galaxie: dev
type: service
nom: altair
alias: [vega-altair, alt]
pitch: "Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré."
categorie: tooling/viz
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/plotly|plotly]]", "[[Dev/Services/bokeh|bokeh]]"]
remplace_par: []
status: actif
tags: [dataviz, declarative-viz, interactive-viz]
url_docs: https://altair-viz.github.io/
url_repo: https://github.com/vega/altair
---

# altair

## Pourquoi

Bibliothèque de visualisation **déclarative** : au lieu de tracer pas à pas, on **décrit** le graphe — quelle colonne va sur quel encodage (`x`, `y`, `color`, `size`), quelle marque (`mark_bar`, `mark_line`, `mark_point`). Altair produit une spécification **Vega-Lite** (JSON) rendue de façon **interactive** dans le navigateur. La grammaire des graphiques rend le code concis et composable : superposition, facettes, sélections liées s'expriment par opérateurs. Entrée naturelle : un `DataFrame` [[Dev/Services/pandas|pandas]].

## Quand l'utiliser

- Exploration où l'on raisonne en **encodages** (grammaire des graphiques) plutôt qu'en primitives de dessin.
- Graphes composés déclaratifs : superposition, facettes, **sélections interactives** liées.
- Sortie interactive pour notebook / web, ou export de la **spec Vega-Lite** réutilisable ailleurs.
- Code de visualisation lisible et concis à maintenir.

## Quand NE PAS l'utiliser

- Très gros jeux : limite par défaut à 5000 lignes (`MaxRowsError`) — agréger ou activer un data server.
- Contrôle bas niveau de chaque pixel → [[Dev/Services/matplotlib|matplotlib]].
- Dashboards serveur / streaming gros volumes → [[Dev/Services/bokeh|bokeh]].
- Riche galerie de types prêts (3D, cartes avancées) → [[Dev/Services/plotly|plotly]].

## Déploiement & coût

- Bibliothèque Python (`uv add altair`) ; génère du Vega-Lite rendu côté navigateur. BSD-3-Clause, gratuit.
- **Single-node** : Altair produit la spec, le rendu est délégué à Vega-Lite/Vega.
- Aucun serveur à tenir ; la spec JSON est portable (web, doc, autre moteur Vega).

## Pièges

- Limite des **5000 lignes** par défaut : penser agrégation ou `alt.data_transformers`.
- Paradigme déclaratif : déroutant si l'on attend une API impérative type matplotlib.
- Le rendu dépend d'un moteur Vega-Lite (version embarquée) — épingler pour la repro.
- Personnalisation très fine parfois contrainte par ce que Vega-Lite expose.

## Alternatives

- [[Dev/Services/plotly|plotly]] — Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash.
- [[Dev/Services/bokeh|bokeh]] — Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes.

## Liens

- Alternatives interactives : [[Dev/Services/plotly|plotly]], [[Dev/Services/bokeh|bokeh]].
- Repose sur la spécification Vega-Lite ; consomme des DataFrames [[Dev/Services/pandas|pandas]].
- [[Dev/Patterns/Comparatif - Visualisation]] — altair vs matplotlib / seaborn / plotly / bokeh.
- Doc : https://altair-viz.github.io/
