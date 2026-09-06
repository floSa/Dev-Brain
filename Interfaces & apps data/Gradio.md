---
role: brique
nom: Gradio
alias: [gradio]
pitch: "Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces."
categorie: ui/data-app
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Streamlit]]", "[[Dash]]", "[[Shiny for Python]]"]
complements: []
tags: [ml-demo, web-framework]
url_docs: https://gradio.app/docs
url_repo: https://github.com/gradio-app/gradio
---

# Gradio

<!-- AUTO:BANDEAU:START -->
> Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de démos de modèles ML édité par **Hugging Face**. Il ne part pas d'une application
mais d'une **fonction** : on l'enveloppe dans une `Interface` — ou dans un `Blocks` pour un
layout sur mesure — et Gradio mappe ses arguments et son retour sur des composants d'entrée et
de sortie typés : image, audio, texte, chat. La conséquence pratique est qu'un modèle devient
cliquable sans qu'on écrive d'interface. Deux mécanismes viennent avec, et ils comptent autant
que le mapping : une **file d'attente** pour absorber la concurrence, et le **streaming** pour
les sorties token par token des modèles génératifs. C'est le SDK de référence de Hugging Face
Spaces.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Exposer un modèle — classification, génération, ASR/TTS, vision, LLM — en interface cliquable, vite | Pensé pour la **démo** : en retrait dès qu'il faut un dashboard riche à plusieurs vues |
| Partager une démo publique sans infra : `share=True`, ou Hugging Face Spaces | Le lien `share=True` est un tunnel **temporaire**, quelques heures — ce n'est pas un hébergement |
| Interface de chat ou de streaming pour un modèle génératif (`ChatInterface`) | Surface d'API mouvante entre versions majeures — la 5 date de 2024, la ligne courante est la 6.x : épingler la version |

## Mise en œuvre

- Installation — `uv add gradio`
- Point d'entrée — `gradio app.py`, ou `demo.launch()` depuis le script
- Prérequis — une fonction Python dont les entrées et sorties se mappent sur des composants
- Exécution — application ASGI, montable dans un FastAPI et conteneurisable ; mono-nœud par app, avec la file d'attente intégrée pour la concurrence et la réplication pour l'échelle. Managé par **Hugging Face Spaces** (SDK `gradio`)
- Coût — gratuit, Apache-2.0 ; Spaces est gratuit ou payant selon le matériel demandé

## Écosystème

### Alternatives

- [[Streamlit]] — Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS.
- [[Dash]] — Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask.
- [[Shiny for Python]] — Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM).

## Ressources

- Documentation — https://gradio.app/docs
- Dépôt — https://github.com/gradio-app/gradio

## Voir aussi

- [[Interfaces & apps data]] — le hub du domaine
- [[Comparatif - Apps data & démos ML]] — ce qui départage les quatre frameworks du dossier
- [[Comparatif - Frontends web légers]] — le même choix élargi à l'option à la main, FastAPI + HTMX
