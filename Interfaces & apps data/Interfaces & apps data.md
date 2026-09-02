---
role: hub
nom: Interfaces & apps data
alias: [apps data, data app, demo ml]
pitch: Donner une interface à un modèle ou à un jeu de données en quelques dizaines de lignes de Python, sans écrire de front.
domaines: [data-sci, ml-eng, ai-eng]
tags: [data-app, ml-demo, dashboard, interactive-viz]
---

# Interfaces & apps data

> Donner une interface à un modèle ou à un jeu de données en quelques dizaines de lignes de Python, sans écrire de front.

## Ce qu'il faut comprendre

- Ces quatre briques répondent à la même demande — « montre-moi ce que fait ton modèle » — et leur **modèle d'exécution** est ce qui les sépare. [[Streamlit]] réexécute tout le script à chaque interaction : trivial à écrire, coûteux dès que le calcul est lourd, d'où le recours au cache. [[Dash]] et [[Shiny for Python]] déclarent des dépendances explicites entre entrées et sorties : seul ce qui doit se recalculer se recalcule. [[Gradio]] ne modélise pas une application mais une **fonction** : des entrées, des sorties, un widget par type.
- Le bon critère de choix est donc la **durée de vie** de ce qu'on construit. Une démo jetable ou une interface de recherche appelle [[Streamlit]] ou [[Gradio]]. Un tableau de bord qu'une équipe consultera pendant deux ans appelle [[Dash]] ou [[Shiny for Python]], parce que le recalcul fin et la structure du code y tiennent dans le temps.
- Ces outils **ne sont pas des frameworks web** et ne doivent pas en tenir lieu. Dès qu'il faut des routes, de l'authentification par rôle, un contrat d'API ou un rendu partagé, on est dans [[Web & API]] — voir aussi [[Comparatif - Frontends web légers]].

## Choisir

- Une démo ou un outil interne, écrit vite, en pur Python → [[Streamlit]].
- Exposer un modèle comme une fonction, avec une API et un lien partageable → [[Gradio]].
- Un tableau de bord analytique durable, mise en page maîtrisée → [[Dash]].
- Le même besoin avec des dépendances réactives fines, ou une équipe venue de R → [[Shiny for Python]].

<!-- AUTO:START -->
### Briques
- [[Dash]] — Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask.
- [[Gradio]] — Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces.
- [[Shiny for Python]] — Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM).
- [[Streamlit]] — Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS.

### Comparatifs
- [[Comparatif - Apps data & démos ML]]
- [[Comparatif - Frontends web légers]]
<!-- AUTO:END -->
