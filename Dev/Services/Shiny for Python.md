---
galaxie: dev
type: service
nom: Shiny for Python
alias: [shiny, py-shiny, shiny-python]
pitch: "Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM)."
categorie: ui/data-app
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Streamlit|Streamlit]]", "[[Dev/Services/Dash|Dash]]", "[[Dev/Services/Gradio|Gradio]]"]
remplace_par: []
status: actif
tags: [data-app, dashboard, web-framework]
url_docs: https://shiny.posit.co/py/
url_repo: https://github.com/posit-dev/py-shiny
---

# Shiny for Python

## Pourquoi

Port Python de **Shiny**, le framework d'apps réactives de **Posit** (ex-RStudio). Cœur du modèle : un **moteur de réactivité à dépendances fines** — `reactive.calc`, `reactive.effect`, et des outputs qui se recalculent **uniquement quand leurs entrées amont changent**. Ni re-run global du script (Streamlit) ni callbacks à câbler à la main (Dash) : le graphe de dépendances est déduit. Deux API : **Core** (UI/serveur séparés, contrôle fin) et **Express** (concis). Licence **MIT**.

## Quand l'utiliser

- App data où le re-run global de Streamlit coûte trop cher : recalcul ciblé natif.
- Dashboard structuré avec beaucoup d'interdépendances entre entrées et sorties.
- Équipe déjà sous Shiny R, ou besoin d'une app **full-navigateur** sans serveur (Shinylive / WASM).

## Quand NE PAS l'utiliser

- Prototype ultra-rapide depuis un script, sans réfléchir à la réactivité → [[Dev/Services/Streamlit|Streamlit]].
- Écosystème graphes Plotly et tooling dashboard Plotly → [[Dev/Services/Dash|Dash]].
- Simple démo entrée→sortie d'un modèle ML → [[Dev/Services/Gradio|Gradio]].

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite. App **ASGI** servie par Uvicorn ; conteneurisable.
- Managé : **Posit Connect** / **Connect Cloud** (gratuit), **shinyapps.io** ; déploiement possible sur Hugging Face Spaces.
- **Single-node** : état réactif par session côté serveur ; scale par réplication.
- Option **serverless / client-side** via **Shinylive** (exécution dans le navigateur par Pyodide/WASM, sans backend).

## Pièges

- Courbe d'apprentissage de la réactivité (`@reactive.calc` vs `@reactive.effect`, dépendances implicites) plus raide que Streamlit.
- Écosystème Python plus jeune que la version R : exemples et composants tiers moins nombreux.
- Shinylive (WASM) ne charge que les paquets compatibles Pyodide — toutes les libs ne passent pas.
- Retours d'expérience détaillés : `Dev/REX/REX - Shiny for Python.md`.

## Alternatives

- [[Dev/Services/Streamlit|Streamlit]] — Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS.
- [[Dev/Services/Dash|Dash]] — Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask.
- [[Dev/Services/Gradio|Gradio]] — Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces.

## Liens

- [[Dev/Patterns/Comparatif - Apps data & démos ML]] — Shiny vs Streamlit / Dash / Gradio.
- Doc : https://shiny.posit.co/py/
