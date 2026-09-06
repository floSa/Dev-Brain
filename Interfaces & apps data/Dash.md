---
role: brique
nom: Dash
alias: [dash, plotly-dash]
pitch: "Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask."
categorie: ui/data-app
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Streamlit]]", "[[Shiny for Python]]", "[[Gradio]]"]
complements: []
tags: [data-app, dashboard, web-framework]
url_docs: https://dash.plotly.com
url_repo: https://github.com/plotly/dash
---

# Dash

<!-- AUTO:BANDEAU:START -->
> Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de dashboards et d'apps analytiques édité par **Plotly**. On déclare une arborescence
de composants (`dash.html`, `dash.dcc`), puis on relie entrées et sorties par des **callbacks** :
un décorateur `@callback(Output, Input, State)` ne recalcule que ce qui dépend de l'élément
modifié. Il n'y a donc pas de re-run global, mais un graphe de dépendances que l'auteur écrit
lui-même, explicitement — c'est le compromis central de l'outil, plus de code en échange d'un
recalcul ciblé et d'apps multi-pages qui tiennent dans la durée. La pile est Flask pour le
serveur, React pour les composants, Plotly.js pour les graphes.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Dashboard analytique riche : pages multiples, filtres croisés, interactions fines entre composants | Verbosité : layout et callbacks demandent plus de code que la concurrence pour un résultat simple |
| App data destinée à durer, avec une vraie séparation entre layout et logique | Le graphe de callbacks se complique vite — dépendances circulaires et `prevent_initial_call` à surveiller |
| Visualisation interactive poussée, dans l'écosystème Plotly | L'état se partage par `dcc.Store` ou par un cache, **jamais par des globales** : le multi-worker ne pardonne pas |

## Mise en œuvre

- Installation — `uv add dash`
- Point d'entrée — import Python ; l'objet obtenu est une application Flask/WSGI
- Prérequis — un script Python ; les graphes passent par Plotly.js, embarqué
- Exécution — servie par Gunicorn ou en conteneur ; les callbacks étant sans état applicatif, le scaling horizontal est classique — plusieurs workers ou instances derrière un load balancer
- Coût — gratuit, MIT. **Dash Enterprise** est l'offre commerciale de Plotly (déploiement, auth, workspaces) ; il n'existe pas de cloud gratuit officiel de type Community Cloud

## Écosystème

### Alternatives

- [[Streamlit]] — Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS.
- [[Shiny for Python]] — Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM).
- [[Gradio]] — Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces.

## Ressources

- Documentation — https://dash.plotly.com
- Dépôt — https://github.com/plotly/dash

## Voir aussi

- [[Interfaces & apps data]] — le hub du domaine
- [[Comparatif - Apps data & démos ML]] — ce qui départage les quatre frameworks du dossier
- [[Comparatif - Frontends web légers]] — le même choix élargi à l'option à la main, FastAPI + HTMX
- [[plotly]] — le moteur de rendu des graphes, du même éditeur
