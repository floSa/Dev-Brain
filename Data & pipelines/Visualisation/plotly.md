---
role: brique
nom: plotly
alias: [plotly.py, px, plotly-express]
pitch: "Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash."
categorie: data/viz
famille: paquet
licence_type: open-source
maturite: production
langage: Python / JavaScript
alternatives: ["[[bokeh]]", "[[altair]]"]
complements: ["[[Dash]]"]
tags: [dataviz, interactive-viz]
url_docs: https://plotly.com/python/
url_repo: https://github.com/plotly/plotly.py
---

# plotly

<!-- AUTO:BANDEAU:START -->
> Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python / JavaScript | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-25 |
<!-- AUTO:BANDEAU:END -->

## Définition

Visualisation **interactive** : la figure est décrite en Python puis rendue dans le
navigateur par **plotly.js**, zoom, pan, survol et sélection compris, sans écrire une ligne
de JavaScript. Deux niveaux d'API : **Plotly Express** (`px`), un graphe par appel depuis un
DataFrame, et les **graph objects** (`go`) pour le contrôle fin — on commence par `px` et on
descend en `go` au besoin. Plus de trente types de graphes, dont les scientifiques, la 3D,
les cartes et le financier. Le moteur JavaScript embarqué se paie : les pages HTML
s'alourdissent dès qu'elles portent beaucoup de figures, et le rendu peine sur les nuages
denses — l'issue est l'agrégation ou le passage en WebGL (`scattergl`).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Graphiques interactifs à embarquer dans une page web, un notebook ou un rapport HTML | Poids de plotly.js embarqué : une page portant beaucoup de figures devient lourde |
| Exploration où le survol et le zoom apportent : séries denses, nuages, 3D, cartes | L'export d'image statique passe par une dépendance supplémentaire, **Kaleido** |
| Servir de brique de visualisation à une app analytique | Beaucoup de points : le rendu navigateur rame — agréger, ou basculer en `scattergl` |
| Export HTML autonome, partageable sans serveur | Deux API à connaître, `px` et `go`, dont la frontière n'est pas toujours nette |

## Mise en œuvre

- Installation — `uv add plotly` ; `kaleido` en plus pour l'export d'images statiques
- Point d'entrée — import Python, `import plotly.express as px` ou `plotly.graph_objects as go`
- Prérequis — Python côté génération, un navigateur côté rendu ; le cœur graphique est en JavaScript
- Exécution — dans le process appelant pour la génération, mono-nœud ; le graphe vit ensuite dans le navigateur
- Coût — gratuit, licence MIT ; l'éditeur vend séparément Dash Enterprise et Chart Studio, la bibliothèque reste libre

## Écosystème

### Alternatives

- [[bokeh]] — Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes.
- [[altair]] — Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré.

### Compléments

- [[Dash]] — Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask. — même éditeur, et plotly est le moteur de rendu des graphes d'une app Dash.

## Ressources

- Documentation — https://plotly.com/python/
- Dépôt — https://github.com/plotly/plotly.py

## Voir aussi

- [[Visualisation]] — le hub du dossier
- [[Comparatif - Visualisation]] — ce qui départage les bibliothèques du dossier
