---
galaxie: dev
type: service
nom: Gradio
alias: [gradio]
pitch: "Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces."
categorie: ui/ml-demo
licence_type: open-source
hosted: both
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Streamlit|Streamlit]]", "[[Dev/Services/Dash|Dash]]", "[[Dev/Services/Shiny for Python|Shiny for Python]]"]
remplace_par: []
status: actif
tags: [ml-demo, web-framework]
url_docs: https://www.gradio.app/docs
url_repo: https://github.com/gradio-app/gradio
---

# Gradio

## Pourquoi

Framework de **démos de modèles ML** édité par **Hugging Face** (acquisition de Gradio en 2021). On enveloppe une fonction Python dans une `Interface` (ou un `Blocks` pour des layouts custom) : Gradio mappe ses arguments et son retour sur des **composants d'entrée/sortie** (image, audio, texte, chat…) et génère une web app. **File d'attente** et **streaming** intégrés pour gérer la concurrence et les sorties token par token (chatbots). Licence **Apache-2.0**. C'est le SDK de référence pour publier une démo sur **Hugging Face Spaces**.

## Quand l'utiliser

- Exposer un modèle (classif, génération, ASR/TTS, vision, LLM) en interface cliquable, vite.
- Partager une démo publique sans infra : `share=True` (tunnel temporaire) ou Hugging Face Spaces.
- Interfaces de chat / streaming pour modèles génératifs (composant `ChatInterface`).

## Quand NE PAS l'utiliser

- App data généraliste / dashboard analytique, au-delà de la démo modèle → [[Dev/Services/Streamlit|Streamlit]] ou [[Dev/Services/Dash|Dash]].
- Dashboard multi-pages à interdépendances fines → [[Dev/Services/Dash|Dash]] / [[Dev/Services/Shiny for Python|Shiny for Python]].
- Besoin d'un modèle réactif fin pour une app complexe → [[Dev/Services/Shiny for Python|Shiny for Python]].

## Déploiement & coût

- Bibliothèque open-source (Apache-2.0), gratuite. Lancement : `gradio app.py` ou `demo.launch()`.
- Managé : **Hugging Face Spaces** (SDK `gradio`, hébergement gratuit ou payant selon le hardware).
- Self-host : app ASGI (montable dans FastAPI), conteneurisable ; `share=True` ouvre un tunnel public temporaire.
- **Single-node** par app ; file d'attente intégrée pour la concurrence ; scale par réplication / Spaces.

## Pièges

- Pensé pour la démo : moins adapté qu'une vraie app data à des dashboards riches multi-vues.
- Le lien `share=True` est temporaire (quelques heures) — pas un hébergement pérenne.
- Surface d'API mouvante entre versions majeures (la 5 date de 2024, la ligne actuelle est la 6.x) : épingler la version.
- Retours d'expérience détaillés : `Dev/REX/REX - Gradio.md`.

## Alternatives

- [[Dev/Services/Streamlit|Streamlit]] — Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS.
- [[Dev/Services/Dash|Dash]] — Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask.
- [[Dev/Services/Shiny for Python|Shiny for Python]] — Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM).

## Liens

- [[Dev/Patterns/Comparatif - Apps data & démos ML]] — Gradio vs Streamlit / Dash / Shiny.
- [[Dev/Patterns/Comparatif - Frontends web légers]] — face à FastAPI+HTMX, Streamlit, Dash.
- SDK de référence pour Hugging Face Spaces.
- Doc : https://www.gradio.app/docs
