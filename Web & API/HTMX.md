---
role: brique
nom: HTMX
alias: [htmx]
pitch: "Bibliothèque hypermedia : des attributs HTML déclenchent des requêtes AJAX et remplacent des fragments de page renvoyés en HTML, pour de l'interactivité riche sans JavaScript lourd."
categorie: web/frontend
famille: paquet
licence_type: open-source
maturite: production
langage: JavaScript
alternatives: []
complements: ["[[Jinja2]]", "[[FastAPI]]"]
tags: [hypermedia]
url_docs: https://htmx.org/
url_repo: https://github.com/bigskysoftware/htmx
---

# HTMX

<!-- AUTO:BANDEAU:START -->
> Bibliothèque hypermedia : des attributs HTML déclenchent des requêtes AJAX et remplacent des fragments de page renvoyés en HTML, pour de l'interactivité riche sans JavaScript lourd.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie JavaScript | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Petite bibliothèque JavaScript sans dépendance qui étend le HTML : des attributs — `hx-get`,
`hx-post`, `hx-target`, `hx-swap` — déclenchent une requête HTTP et **remplacent un fragment de
page par le HTML renvoyé** par le serveur. On obtient le chargement partiel, les formulaires
asynchrones, la pagination et le polling sans écrire de JavaScript ni gérer d'état côté client.
C'est l'approche *hypermedia* prise au mot : le serveur reste la source de vérité et renvoie de
l'HTML, pas du JSON. Écrit par Carson Gross, successeur d'intercooler.js ; la v2 est la ligne
stable, une v4 est en développement.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Ajouter de l'interactivité à une app déjà rendue côté serveur, sans pipeline JS | Chaque interaction est un aller-retour réseau : la **latence se ressent**, à mitiger par des fragments ciblés |
| Équipe back-end qui préfère renvoyer de l'HTML plutôt que maintenir un front JSON séparé | Le serveur doit savoir rendre des **fragments** distincts des pages complètes — discipline de templating à tenir |
| CRUD, dashboards internes, formulaires dynamiques où l'état vit côté serveur | UI à fort état client, hors-ligne, temps réel complexe, animations riches : frameworks SPA (React, Vue, Svelte), non fichés ici |
| | Application sans rendu HTML serveur — une API pure consommée par un client natif n'a rien à échanger avec HTMX |
| | Pousse à loger de la logique d'UI dans des attributs HTML peu testables si l'on en abuse |

## Mise en œuvre

- Installation — un seul fichier JS, chargé depuis un CDN ou servi en statique ; aucune étape de build
- Point d'entrée — des attributs `hx-*` posés directement dans le balisage
- Prérequis — un serveur capable de renvoyer des fragments HTML ; rien côté client
- Exécution — dans le navigateur ; suit le déploiement du serveur HTML, il n'y a pas de service à héberger
- Coût — gratuit, 0BSD, aucune limite d'usage

## Écosystème

### Alternatives

<!-- Aucune : les frameworks SPA (React, Vue, Svelte) ne sont pas fichés dans le brain. -->

### Compléments

- [[Jinja2]] — Moteur de templates Python rapide et expressif : gabarits HTML avec héritage, échappement automatique et expressions proches de Python ; le moteur de templates de Flask. — rend les fragments que HTMX vient injecter ; c'est la paire usuelle côté Python
- [[FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement. — le backend qui sert ces fragments ; le comparatif du dossier traite « FastAPI + HTMX » comme un couple, pas comme deux concurrents

## Ressources

- Documentation — https://htmx.org/
- Dépôt — https://github.com/bigskysoftware/htmx

## Voir aussi

- [[Web & API]] — le hub du domaine
- [[Comparatif - Frontends web légers]] — ce qui départage FastAPI + HTMX de Streamlit, Gradio et Dash
- [[Flask]] — l'autre serveur HTML du dossier, côté WSGI
