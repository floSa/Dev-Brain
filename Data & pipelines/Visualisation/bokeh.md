---
role: brique
nom: bokeh
alias: []
pitch: "Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes."
categorie: data/viz
famille: paquet
licence_type: open-source
maturite: production
langage: Python / TypeScript
alternatives: ["[[plotly]]", "[[altair]]"]
complements: []
tags: [dataviz, interactive-viz]
url_docs: https://docs.bokeh.org/
url_repo: https://github.com/bokeh/bokeh
---

# bokeh

<!-- AUTO:BANDEAU:START -->
> Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python / TypeScript | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-02 |
<!-- AUTO:BANDEAU:END -->

## Définition

Visualisation **interactive** pour le navigateur : la figure se décrit en Python, le rendu
se fait en JavaScript via **BokehJS**. Deux usages distincts en découlent — produire du
**HTML autonome**, un graphe embarqué dans une page sans rien à héberger, ou lancer un
**serveur Bokeh** qui relie des widgets Python à des callbacks, ce qui donne des dashboards
réactifs sans écrire de JS. C'est ce second mode qui distingue la bibliothèque, et c'est
aussi ce qui coûte : sessions et callbacks forment un modèle à apprendre, et le serveur se
dimensionne selon le nombre d'utilisateurs. Le rendu est pensé pour rester fluide sur de
gros volumes, voire sur des données en **streaming**.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Dashboards et apps de données interactives côté serveur : widgets Python reliés à des callbacks | Le modèle serveur — sessions, callbacks — a une courbe d'apprentissage plus raide que l'export statique |
| Gros jeux de données ou flux **streaming** à garder fluides à l'affichage | Pas d'export d'image natif simple : il passe par des extras, Selenium ou geckodriver |
| Graphes liés dans une page : sélection partagée, axes synchronisés | Une page interactive pèse plus qu'un PNG — inadapté au print |
| Sortie HTML interactive autonome, sans dépendre d'un service tiers | Deux niveaux d'API historiquement, *models* bas niveau et `bokeh.plotting` : s'en tenir au second |

## Mise en œuvre

- Installation — `uv add bokeh`
- Point d'entrée — import Python, `from bokeh.plotting import figure` ; `bokeh serve` pour le mode app
- Prérequis — Python côté description, un navigateur côté rendu ; BokehJS est écrit en TypeScript
- Exécution — HTML autonome sans serveur, ou serveur Bokeh mono-nœud tenant les sessions
- Coût — gratuit, licence BSD-3-Clause, aucune limite d'usage

## Écosystème

### Alternatives

- [[plotly]] — Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash.
- [[altair]] — Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré.

## Ressources

- Documentation — https://docs.bokeh.org/
- Dépôt — https://github.com/bokeh/bokeh

## Voir aussi

- [[Visualisation]] — le hub du dossier
- [[Comparatif - Visualisation]] — ce qui départage les bibliothèques du dossier
