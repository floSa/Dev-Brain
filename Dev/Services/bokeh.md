---
galaxie: dev
type: service
nom: bokeh
alias: []
pitch: "Visualisation interactive pour le navigateur, du graphique au dashboard, avec un serveur Bokeh pour le streaming et les grands volumes."
categorie: tooling/viz
licence_type: open-source
hosted: self
maturite: production
langage: Python / TypeScript
scaling: single-node
alternatives: ["[[Dev/Services/plotly|plotly]]", "[[Dev/Services/altair|altair]]"]
remplace_par: []
status: actif
tags: [dataviz, interactive-viz]
url_docs: https://docs.bokeh.org/
url_repo: https://github.com/bokeh/bokeh
---

# bokeh

## Pourquoi

Bibliothèque de visualisation **interactive** pour le navigateur. Côté Python on décrit la figure ; le rendu se fait en JavaScript via **BokehJS**. Deux usages : générer du **HTML autonome** (graphe embarqué dans une page) ou lancer un **serveur Bokeh** qui relie les widgets Python aux callbacks — apps et **dashboards** réactifs sans écrire de JS. Conçu pour rester fluide sur de **gros volumes**, voire des données en **streaming**. Outils intégrés : pan, zoom, survol, sélection, liaison entre graphes.

## Quand l'utiliser

- **Dashboards** et apps de données interactives côté serveur (widgets ↔ callbacks Python).
- Visualisation de **gros jeux** ou de flux **streaming** à garder fluides.
- Graphes liés (sélection partagée, axes synchronisés) dans une page web.
- Sortie HTML interactive autonome sans dépendre d'un service tiers.

## Quand NE PAS l'utiliser

- Graphes statistiques rapides en une ligne → [[Dev/Services/seaborn|seaborn]].
- Sortie statique pour print/PDF → [[Dev/Services/matplotlib|matplotlib]].
- API plus immédiate pour l'interactif courant → [[Dev/Services/plotly|plotly]] (Plotly Express).
- Spécification déclarative concise → [[Dev/Services/altair|altair]].

## Déploiement & coût

- Bibliothèque Python (`uv add bokeh`) ; rendu BokehJS (TypeScript). BSD-3-Clause, gratuit.
- HTML autonome **sans serveur**, ou **serveur Bokeh** (`bokeh serve`) pour les apps réactives.
- **Single-node** ; le serveur tient des sessions, à dimensionner selon le nombre d'utilisateurs.

## Pièges

- Le modèle serveur (sessions, callbacks) a une courbe d'apprentissage plus raide que l'export statique.
- Deux niveaux d'API historiquement (bas niveau *models* vs `bokeh.plotting`) : s'en tenir à `plotting`.
- Pas d'export image natif simple (passe par des extras, p. ex. Selenium/geckodriver).
- Page plus lourde qu'un PNG : inadapté au print.

## Alternatives

- [[Dev/Services/plotly|plotly]] — Visualisation interactive pour le web (zoom, survol, 3D) via plotly.js ; API haut niveau Plotly Express et socle des apps Dash.
- [[Dev/Services/altair|altair]] — Visualisation déclarative fondée sur Vega-Lite : on décrit la correspondance données → encodages, le rendu interactif est généré.

## Liens

- Alternatives interactives : [[Dev/Services/plotly|plotly]], [[Dev/Services/altair|altair]].
- [[Dev/Patterns/Comparatif - Visualisation]] — bokeh vs matplotlib / seaborn / plotly / altair.
- Doc : https://docs.bokeh.org/
