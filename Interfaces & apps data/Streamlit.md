---
role: brique
nom: Streamlit
alias: [streamlit]
pitch: "Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS."
categorie: ui/data-app
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Dash]]", "[[Shiny for Python]]", "[[Gradio]]"]
complements: []
tags: [data-app, web-framework]
url_docs: https://docs.streamlit.io
url_repo: https://github.com/streamlit/streamlit
---

# Streamlit

<!-- AUTO:BANDEAU:START -->
> Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework d'apps data en Python pur, bâti sur une seule idée : le script est linéaire, chaque
widget (`st.slider`, `st.selectbox`…) renvoie sa valeur, et **tout le script se ré-exécute de
haut en bas à chaque interaction**. Il n'y a donc ni HTML, ni callbacks, ni état explicite à
écrire — le modèle mental tient en une phrase, et c'est ce qui permet de transformer un
notebook en app partageable en quelques heures. Le coût de ce re-run global n'est pas éliminé,
il est déplacé sur deux mécanismes que l'auteur doit poser lui-même, `@st.cache_data` /
`@st.cache_resource` pour les calculs, `st.session_state` pour la mémoire. Édité par Snowflake
depuis le rachat de Streamlit Inc. en 2022.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Transformer un script d'analyse ou un notebook en app partageable en quelques heures | Le re-run complet à chaque interaction surprend : **sans `@st.cache_*`, les calculs et I/O lourds repartent à chaque clic** |
| Outils internes, prototypes, dashboards exploratoires où la vitesse de développement prime | `st.session_state` devient obligatoire dès qu'il faut conserver quoi que ce soit entre deux re-runs |
| Démo data/ML rapide en restant dans l'écosystème Python | Mise en page contrainte — flux vertical et colonnes : peu adapté aux layouts complexes ou très denses |

## Mise en œuvre

- Installation — `uv add streamlit`
- Point d'entrée — `streamlit run app.py`
- Prérequis — un script Python ; rien d'autre
- Exécution — mono-nœud, état par session en mémoire serveur ; montée en charge par réplication derrière un load balancer. Managé par **Streamlit Community Cloud** (gratuit, lié à GitHub, ressources limitées) ou **Streamlit in Snowflake** ; self-host en conteneur derrière un reverse proxy
- Coût — gratuit, Apache-2.0 ; le managé Snowflake est l'offre payante

## Écosystème

### Alternatives

- [[Dash]] — Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask.
- [[Shiny for Python]] — Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM).
- [[Gradio]] — Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces.

## Ressources

- Documentation — https://docs.streamlit.io
- Dépôt — https://github.com/streamlit/streamlit

## Voir aussi

- [[Interfaces & apps data]] — le hub du domaine
- [[Comparatif - Apps data & démos ML]] — ce qui départage les quatre frameworks du dossier
- [[Comparatif - Frontends web légers]] — le même choix élargi à l'option à la main, FastAPI + HTMX
- [[plotly]] — dont il affiche les figures, comme celles de matplotlib ou altair
