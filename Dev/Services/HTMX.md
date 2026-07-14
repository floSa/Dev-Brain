---
galaxie: dev
type: service
nom: HTMX
alias: [htmx]
pitch: "Bibliothèque hypermedia : des attributs HTML déclenchent des requêtes AJAX et remplacent des fragments de page renvoyés en HTML, pour de l'interactivité riche sans JavaScript lourd."
categorie: framework/frontend
licence_type: open-source
hosted: self
maturite: production
langage: JavaScript
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [hypermedia]
url_docs: https://htmx.org/
url_repo: https://github.com/bigskysoftware/htmx
---

# HTMX

## Pourquoi

Petite bibliothèque JavaScript (sans dépendance) qui étend le HTML : des attributs (`hx-get`, `hx-post`, `hx-target`, `hx-swap`) déclenchent des requêtes HTTP et **remplacent un fragment de page par le HTML renvoyé** par le serveur. L'interactivité d'une SPA — chargement partiel, formulaires asynchrones, pagination, polling — sans écrire de JavaScript ni gérer un état client. Concrétise l'approche *hypermedia* (HTML comme moteur d'état applicatif) : le serveur reste la source de vérité et renvoie de l'HTML, pas du JSON. Écrit par Carson Gross, successeur d'intercooler.js. Licence 0BSD (domaine public de fait).

## Quand l'utiliser

- App rendue côté serveur ([[Dev/Services/FastAPI|FastAPI]], [[Dev/Services/Flask|Flask]], Django) à qui l'on veut ajouter de l'interactivité sans pipeline JS.
- Équipe back-end qui préfère renvoyer de l'HTML (via [[Dev/Services/Jinja2|Jinja2]]) plutôt que maintenir un front JSON + framework JS séparé.
- CRUD, dashboards internes, formulaires dynamiques où l'état vit côté serveur.

## Quand NE PAS l'utiliser

- UI à fort état client, hors-ligne, temps réel complexe, animations riches → framework SPA (React, Vue, Svelte — hors brain).
- Application sans rendu HTML serveur (API pure consommée par un client natif).

## Déploiement & coût

- Un seul fichier JS chargé depuis un CDN ou servi en statique ; open-source (0BSD), gratuit. Aucune build step requise.
- Pas de service à héberger : s'exécute dans le navigateur, suit le déploiement du serveur HTML. La v2 est la ligne stable ; une v4 est en développement.

## Pièges

- L'interactivité reposant sur des allers-retours serveur, la **latence réseau** se ressent sur chaque interaction (mitiger par fragments ciblés, pas de full-page).
- Le serveur doit savoir renvoyer des **fragments** HTML partiels distincts des pages complètes — discipline de templating à tenir.
- Peut pousser à mettre de la logique d'UI dans des attributs HTML peu testables si l'on en abuse.
- Retours d'expérience détaillés : `Dev/REX/REX - HTMX.md`.

## Alternatives

<!-- Pas d'alternative dans le brain : les frameworks SPA (React, Vue, Svelte) ne sont pas documentés. -->

## Liens

- [[Dev/Patterns/Comparatif - Frontends web légers]] — FastAPI+HTMX vs Streamlit / Gradio / Dash.
- [[Dev/Services/Jinja2|Jinja2]] — rend les fragments HTML que HTMX vient injecter (paire usuelle)
- [[Dev/Services/FastAPI|FastAPI]] / [[Dev/Services/Flask|Flask]] — serveurs HTML côté back
- Doc : https://htmx.org/
