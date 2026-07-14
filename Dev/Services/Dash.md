---
galaxie: dev
type: service
nom: Dash
alias: [dash, plotly-dash]
pitch: "Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask."
categorie: ui/data-app
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Streamlit|Streamlit]]", "[[Dev/Services/Shiny for Python|Shiny for Python]]", "[[Dev/Services/Gradio|Gradio]]"]
remplace_par: []
status: actif
tags: [data-app, dashboard, web-framework]
url_docs: https://dash.plotly.com
url_repo: https://github.com/plotly/dash
---

# Dash

## Pourquoi

Framework de **dashboards et apps analytiques** édité par **Plotly**. On déclare une arborescence de composants (`dash.html`, `dash.dcc`) et on relie entrées et sorties par des **callbacks** : un décorateur `@callback(Output, Input, State)` recalcule seulement ce qui dépend de l'élément modifié — pas de re-run global du script. Bâti sur **Flask** (serveur) + **React** (composants) + **Plotly.js** (graphes). Licence **MIT**. Modèle plus verbeux que Streamlit mais qui passe à l'échelle des apps multi-pages structurées.

## Quand l'utiliser

- Dashboard analytique riche : pages multiples, filtres croisés, interactions fines entre composants.
- App data destinée à durer, avec une vraie séparation layout / logique (callbacks).
- Visualisation interactive poussée (on est dans l'écosystème [[Dev/Services/plotly|plotly]]).

## Quand NE PAS l'utiliser

- Prototype rapide / script analytique à exposer vite → [[Dev/Services/Streamlit|Streamlit]] (moins de code).
- Préférence pour un modèle réactif fin sans écrire de callbacks explicites → [[Dev/Services/Shiny for Python|Shiny for Python]].
- Simple démo entrée→sortie d'un modèle ML → [[Dev/Services/Gradio|Gradio]].

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite. App Flask/WSGI : servie par Gunicorn, conteneurisable.
- Managé : **Dash Enterprise** (offre commerciale Plotly — déploiement, auth, workspaces). Pas de cloud gratuit officiel type Community Cloud.
- Serveur **sans état applicatif** côté callbacks → **scaling horizontal** classique (plusieurs workers/instances derrière un load balancer).

## Pièges

- Verbosité : layout + callbacks demandent plus de code que Streamlit pour un résultat simple.
- Graphe de callbacks vite complexe ; circular dependencies et `prevent_initial_call` à surveiller.
- Partage d'état entre callbacks : passer par `dcc.Store` ou un cache, pas par des globales (multi-worker).
- Retours d'expérience détaillés : `Dev/REX/REX - Dash.md`.

## Alternatives

- [[Dev/Services/Streamlit|Streamlit]] — Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS.
- [[Dev/Services/Shiny for Python|Shiny for Python]] — Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM).
- [[Dev/Services/Gradio|Gradio]] — Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces.

## Liens

- [[Dev/Patterns/Comparatif - Apps data & démos ML]] — Dash vs Streamlit / Shiny / Gradio.
- [[Dev/Patterns/Comparatif - Frontends web légers]] — face à FastAPI+HTMX, Streamlit, Gradio.
- [[Dev/Services/plotly|plotly]] — moteur de rendu des graphes Dash (même éditeur).
- Doc : https://dash.plotly.com
