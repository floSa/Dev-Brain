---
galaxie: dev
type: service
nom: plotly
alias: [plotly.py, px, plotly-express]
pitch: "Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash."
categorie: tooling/viz
licence_type: open-source
hosted: self
maturite: production
langage: Python / JavaScript
scaling: single-node
alternatives: ["[[Dev/Services/bokeh|bokeh]]", "[[Dev/Services/altair|altair]]"]
remplace_par: []
status: actif
tags: [dataviz, interactive-viz]
url_docs: https://plotly.com/python/
url_repo: https://github.com/plotly/plotly.py
---

# plotly

## Pourquoi

Bibliothèque de visualisation **interactive** : les graphiques sont rendus dans le navigateur via **plotly.js** (HTML/JS). Deux niveaux : **Plotly Express** (`px`, haut niveau, un graphe par appel depuis un DataFrame) et **graph objects** (`go`, contrôle fin de la figure). Plus de 30 types de graphes : scientifiques, 3D, cartes, financiers. Interactivité native (zoom, pan, survol, sélection) sans écrire de JavaScript. C'est aussi le moteur de rendu de **Dash**, le framework d'apps analytiques du même éditeur.

## Quand l'utiliser

- Graphiques **interactifs** à embarquer dans une page web, un notebook ou un rapport HTML.
- Exploration où le survol / zoom apporte (séries denses, nuages, 3D, cartes).
- Brique de visualisation d'une app **Dash** (ou Streamlit, qui affiche des figures plotly).
- Export HTML autonome partageable sans serveur.

## Quand NE PAS l'utiliser

- Sortie statique pour PDF/print → [[Dev/Services/matplotlib|matplotlib]] / [[Dev/Services/seaborn|seaborn]] (l'export image plotly demande Kaleido).
- Approche déclarative concise type grammaire des graphiques → [[Dev/Services/altair|altair]].
- Streaming serveur / très gros volumes côté serveur → [[Dev/Services/bokeh|bokeh]] et son serveur.

## Déploiement & coût

- Bibliothèque Python (`uv add plotly`) ; cœur de rendu en JavaScript (plotly.js). MIT, gratuit.
- **Single-node** pour la génération ; le graphe vit ensuite dans le navigateur.
- L'éditeur propose des offres commerciales séparées (Dash Enterprise, Chart Studio) — la lib reste libre.

## Pièges

- Poids de plotly.js embarqué : pages HTML lourdes si beaucoup de figures.
- Export d'image statique = dépendance **Kaleido** supplémentaire.
- Beaucoup de points → le rendu navigateur rame ; agréger ou passer en WebGL (`scattergl`).
- Deux API (`px` vs `go`) : commencer par `px`, descendre en `go` au besoin.

## Alternatives

- [[Dev/Services/bokeh|bokeh]] — Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes.
- [[Dev/Services/altair|altair]] — Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré.

## Liens

- Alternatives interactives : [[Dev/Services/bokeh|bokeh]], [[Dev/Services/altair|altair]].
- Socle des apps Dash (même éditeur) ; figures affichables dans Streamlit.
- [[Dev/Patterns/Comparatif - Visualisation]] — plotly vs matplotlib / seaborn / altair / bokeh.
- Doc : https://plotly.com/python/
