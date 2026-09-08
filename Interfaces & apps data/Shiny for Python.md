---
role: brique
nom: Shiny for Python
alias: [shiny, py-shiny, shiny-python]
pitch: "Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM)."
categorie: ui/data-app
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Streamlit]]", "[[Dash]]", "[[Gradio]]"]
complements: []
tags: [data-app, dashboard, web-framework]
url_docs: https://shiny.posit.co/py/
url_repo: https://github.com/posit-dev/py-shiny
---

# Shiny for Python

<!-- AUTO:BANDEAU:START -->
> Apps réactives à dépendances fines (Posit) : seuls les outputs dont les entrées changent se recalculent ; déployable côté serveur ou full-navigateur (WASM).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-07-29 |
<!-- AUTO:BANDEAU:END -->

## Définition

Port Python de **Shiny**, le framework d'apps réactives de **Posit** (ex-RStudio). Son cœur est
un moteur de réactivité à **dépendances fines** : avec `reactive.calc` et `reactive.effect`, un
output ne se recalcule que quand ses entrées amont changent — et le graphe de dépendances est
**déduit**, pas déclaré. C'est un troisième modèle, ni le re-run global d'un script, ni les
callbacks écrits à la main : on obtient le recalcul ciblé sans câbler quoi que ce soit, en
échange d'une notion — la réactivité — qu'il faut avoir comprise avant d'écrire. Deux API
coexistent, **Core** (UI et serveur séparés, contrôle fin) et **Express** (concise).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| App data où le re-run global coûte trop cher : le recalcul ciblé est natif | Courbe d'apprentissage de la réactivité — `@reactive.calc` contre `@reactive.effect`, dépendances implicites — plus raide que chez la concurrence |
| Dashboard structuré avec beaucoup d'interdépendances entre entrées et sorties | Écosystème Python **plus jeune que la version R** : exemples et composants tiers moins nombreux |
| Équipe déjà sous Shiny R, ou besoin d'une app full-navigateur sans serveur | **Shinylive** (WASM) ne charge que les paquets compatibles Pyodide : toutes les bibliothèques ne passent pas |

## Mise en œuvre

- Installation — `uv add shiny`
- Point d'entrée — deux API au choix, Core (UI et serveur séparés) ou Express (concise)
- Prérequis — un script Python ; pour Shinylive, des dépendances compatibles Pyodide
- Exécution — application ASGI servie par Uvicorn, conteneurisable ; mono-nœud, état réactif par session côté serveur, scaling par réplication. Option **serverless côté client** par Shinylive, qui exécute dans le navigateur via Pyodide, sans backend. Managé par **Posit Connect** / **Connect Cloud** (gratuit), **shinyapps.io**, ou Hugging Face Spaces
- Coût — gratuit, MIT ; les offres managées de Posit sont l'option payante

## Écosystème

### Alternatives

- [[Streamlit]] — Apps data en Python pur : le script se ré-exécute de haut en bas à chaque interaction, widgets et cache intégrés, zéro HTML/JS.
- [[Dash]] — Apps analytiques et dashboards multi-pages : composants réactifs liés par callbacks déclaratifs, rendu Plotly.js sur socle Flask.
- [[Gradio]] — Démos de modèles ML en quelques lignes (Hugging Face) : composants d'entrée/sortie, file d'attente et streaming intégrés, hébergement sur HF Spaces.

## Ressources

- Documentation — https://shiny.posit.co/py/
- Dépôt — https://github.com/posit-dev/py-shiny

## Voir aussi

- [[Interfaces & apps data]] — le hub du domaine
- [[Comparatif - Apps data & démos ML]] — ce qui départage les quatre frameworks du dossier
