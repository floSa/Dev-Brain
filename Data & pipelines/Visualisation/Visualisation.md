---
role: hub
nom: Visualisation
alias: [dataviz, graphiques]
pitch: Rendre une donnée regardable — du graphique jetable d'exploration à la figure publiée.
domaines: [data-sci]
tags: [dataviz, static-viz, interactive-viz, statistical-viz]
---

# Visualisation

> Rendre une donnée regardable — du graphique jetable d'exploration à la figure publiée.

## Ce qu'il faut comprendre

- Le premier clivage est **statique ou interactif**, et il ne se rattrape pas : une figure destinée à un PDF ([[matplotlib]], [[seaborn]]) et un graphique destiné à un navigateur ([[plotly]], [[bokeh]], [[altair]]) ne se construisent pas de la même façon. Choisir la sortie avant la bibliothèque évite de tout réécrire.
- Le second est **impératif ou déclaratif**. En impératif ([[matplotlib]]), on donne les ordres de dessin un par un — contrôle total, verbosité totale. En déclaratif ([[altair]]), on décrit la correspondance entre variables et encodages (position, couleur, taille) et le rendu en découle. Le déclaratif est plus court et refuse ce qui ne rentre pas dans sa grammaire ; l'impératif accepte tout et se paie en lignes.
- [[matplotlib]] est le **socle**, pas un choix parmi d'autres : [[seaborn]] est une surcouche qui l'appelle, et beaucoup d'outils exportent vers lui. Savoir descendre au niveau `Axes` de matplotlib est ce qui permet de finir n'importe quelle figure — c'est l'investissement rentable du sous-domaine.
- Le troisième clivage est le **volume de points**. Au-delà de quelques dizaines de milliers, un rendu navigateur point par point s'effondre : il faut agréger côté serveur ([[bokeh]]) ou renoncer à l'interactivité.
- L'usage décide plus que l'esthétique. Un graphique d'**exploration** est jetable, doit sortir en une ligne, et [[seaborn]] est fait pour ça. Un graphique de **publication** est retravaillé pendant des heures dans [[matplotlib]]. Un graphique **livré dans une application** dépend du framework qui l'affiche — [[plotly]] pour [[Dash]], [[bokeh]] pour son propre serveur.

## Choisir

- Une figure à contrôler au pixel, pour un rapport ou un article → [[matplotlib]].
- Une distribution, une relation, une comparaison de groupes, en une ligne → [[seaborn]].
- De l'interactif dans un notebook ou une application web, avec une API haut niveau → [[plotly]].
- De l'interactif sur beaucoup de points, ou un dashboard servi en streaming → [[bokeh]].
- Une grammaire déclarative, des graphiques composables et reproductibles → [[altair]].
- Un tableau de bord complet plutôt qu'un graphique → [[Interfaces & apps data]].

<!-- AUTO:START -->
### Briques
- [[altair]] — Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré.
- [[bokeh]] — Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes.
- [[matplotlib]] — Socle de la visualisation Python : API impérative bas niveau pour des graphiques statiques entièrement contrôlables (PNG/SVG/PDF), base de presque tout l'écosystème viz.
- [[plotly]] — Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash.
- [[seaborn]] — Surcouche statistique de matplotlib : graphiques soignés en une ligne (distributions, relations, catégories) directement depuis un DataFrame pandas.

### Comparatifs
- [[Comparatif - Visualisation]]
<!-- AUTO:END -->
