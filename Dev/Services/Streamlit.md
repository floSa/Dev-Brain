---
galaxie: dev
type: service
nom: Streamlit
alias: [streamlit]
pitch: "Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS."
categorie: ui/data-app
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Dash|Dash]]", "[[Dev/Services/Shiny for Python|Shiny for Python]]", "[[Dev/Services/Gradio|Gradio]]"]
remplace_par: []
status: actif
tags: [data-app, web-framework]
url_docs: https://docs.streamlit.io
url_repo: https://github.com/streamlit/streamlit
---

# Streamlit

## Pourquoi

Framework d'**apps data en Python pur** : on écrit un script linéaire, chaque widget (`st.slider`, `st.selectbox`…) renvoie sa valeur, et **tout le script se ré-exécute de haut en bas à chaque interaction**. Pas de HTML, de callbacks ni de gestion d'état explicite à écrire. Le coût du re-run global est maîtrisé par `@st.cache_data` / `@st.cache_resource` et `st.session_state`. Édité par **Snowflake** (rachat de Streamlit Inc. en 2022), licence **Apache-2.0**, très actif.

## Quand l'utiliser

- Transformer un script d'analyse ou un notebook en app partageable en quelques heures.
- Outils internes, prototypes, dashboards exploratoires où la vitesse de développement prime.
- Démo data/ML rapide quand on reste dans l'écosystème Python (pandas, plotly, modèles).

## Quand NE PAS l'utiliser

- Dashboard analytique multi-pages à composants finement liés → [[Dev/Services/Dash|Dash]].
- Besoin de recalcul réactif ciblé (sans re-run global) sur app lourde → [[Dev/Services/Shiny for Python|Shiny for Python]].
- Démo d'un modèle ML centrée entrée→sortie, hébergée sur HF → [[Dev/Services/Gradio|Gradio]].

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite. Lancement : `streamlit run app.py`.
- Managé : **Streamlit Community Cloud** (gratuit, lié à GitHub, ressources limitées) et **Streamlit in Snowflake** (offre entreprise).
- Self-host : conteneur Docker / VPS derrière un reverse proxy.
- **Single-node** : état par session en mémoire serveur ; montée en charge par réplication derrière un load balancer.

## Pièges

- Le re-run complet à chaque interaction surprend : sans `@st.cache_*`, les calculs et I/O lourds repartent à chaque clic.
- `st.session_state` est nécessaire dès qu'on veut conserver un état entre les re-runs.
- Mise en page contrainte (flux vertical, colonnes) : peu adapté aux layouts complexes ou très denses.
- Retours d'expérience détaillés : `Dev/REX/REX - Streamlit.md`.

## Alternatives

- [[Dev/Services/Dash|Dash]] — Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask.
- [[Dev/Services/Shiny for Python|Shiny for Python]] — Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM).
- [[Dev/Services/Gradio|Gradio]] — Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces.

## Liens

- [[Dev/Patterns/Comparatif - Apps data & démos ML]] — Streamlit vs Dash / Shiny / Gradio.
- [[Dev/Patterns/Comparatif - Frontends web légers]] — face à FastAPI+HTMX, Gradio, Dash.
- Affiche les figures [[Dev/Services/plotly|plotly]], matplotlib, altair, etc.
- Doc : https://docs.streamlit.io
