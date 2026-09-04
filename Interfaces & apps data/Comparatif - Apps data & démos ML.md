---
role: comparatif
nom: Comparatif - Apps data & démos ML
categorie: ui/data-app
tags: [data-app, dashboard, ml-demo, web-framework]
---

# Comparatif - Apps data & démos ML

> On tranche sur : ce qui se recalcule à chaque interaction — tout le script, un callback qu'on a déclaré, ou seulement ce qui dépend de l'entrée modifiée.

![[Comparatif - Apps data & démos ML.base]]

## Ce qui départage

- [[Streamlit]] — un script linéaire en Python pur, où **tout se ré-exécute de haut en bas à chaque interaction** : ni HTML, ni callbacks, ni état explicite à écrire. Le prix est assumé et il se paie — sans `@st.cache_data` / `@st.cache_resource` les calculs et I/O lourds repartent à chaque clic, `st.session_state` devient obligatoire dès qu'il faut retenir quelque chose, et la mise en page reste un flux vertical.
- [[Dash]] — l'inverse exact : un arbre de composants déclaré, et des **callbacks explicites** (`@callback(Output, Input, State)`) qui ne recalculent que la dépendance touchée, sur Flask + React + Plotly.js. Plus de code que Streamlit pour un résultat simple, un graphe de callbacks qui se complique vite (dépendances circulaires, `prevent_initial_call`), et un état à partager par `dcc.Store` plutôt que par des globales.
- [[Shiny for Python]] — un troisième modèle, ni l'un ni l'autre : le graphe de dépendances est **déduit** au lieu d'être déclaré (`reactive.calc`, `reactive.effect`), donc le recalcul est ciblé sans écrire un seul callback. Courbe d'apprentissage de la réactivité plus raide, écosystème Python plus jeune que la version R, et Shinylive (WASM) ne charge que les paquets compatibles Pyodide.
- [[Gradio]] — le seul qui ne part pas d'une app mais d'une **fonction** : on l'enveloppe dans une `Interface`, ses arguments et son retour se mappent sur des composants typés (image, audio, chat…), avec **file d'attente et streaming** intégrés — c'est le SDK de Hugging Face Spaces. Pensé pour la démo, donc en retrait sur un dashboard multi-vues ; le lien `share=True` ne dure que quelques heures, et la surface d'API bouge entre versions majeures.
