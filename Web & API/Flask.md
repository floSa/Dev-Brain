---
role: brique
nom: Flask
alias: [flask]
pitch: "Micro-framework web Python (WSGI) minimaliste et extensible : noyau réduit (routage Werkzeug + templates Jinja2), tout le reste ajouté à la carte par extensions."
categorie: web/backend
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[FastAPI]]"]
complements: []
tags: [web-framework]
url_docs: https://flask.palletsprojects.com
url_repo: https://github.com/pallets/flask
---

# Flask

<!-- AUTO:BANDEAU:START -->
> Micro-framework web Python (WSGI) minimaliste et extensible : noyau réduit (routage Werkzeug + templates Jinja2), tout le reste ajouté à la carte par extensions.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-02-19 |
<!-- AUTO:BANDEAU:END -->

## Définition

Micro-framework web Python **synchrone (WSGI)**. « Micro » ne dit pas limité : le cœur est
volontairement réduit — routage et utilitaires HTTP par **Werkzeug**, gabarits par
**Jinja2** — et tout le reste (ORM, formulaires, authentification, admin) s'ajoute à la carte
par **extensions** (Flask-SQLAlchemy, Flask-Login…). On garde donc le contrôle de
l'architecture, sans convention imposée, et on paie ce contrôle en décisions à prendre. Des
vues `async` existent depuis la 2.0, mais le modèle d'exécution reste WSGI synchrone : une vue
occupe un worker du début à la fin. Maintenu par l'organisation **Pallets** (créé en 2010 par
Armin Ronacher), ligne 3.1.x, et de loin le framework web Python le plus téléchargé.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Petite ou moyenne app web, microservice, prototype : démarrage immédiat, peu de cérémonie | API JSON typée, fort I/O async, doc OpenAPI automatique → [[FastAPI]] |
| Vouloir choisir soi-même ses briques (ORM, validation) plutôt qu'un cadre imposé | Modèle synchrone : une vue qui bloque sur de l'I/O monopolise un worker — dimensionner les workers, ne pas compter sur `async` |
| Rendre des pages côté serveur (Jinja2) autant que servir du JSON | Le serveur de développement (`flask run`) est mono-thread par défaut et inadapté à la production |
| Écosystème d'extensions mûr, déjà connu de l'équipe | Besoin d'un cadre « batteries incluses » — admin, ORM, auth intégrés : Django, non fiché ici |
| | « Micro » laisse les choix à l'intégrateur : sans discipline, extensions et patterns divergent d'un projet à l'autre |

## Mise en œuvre

- Installation — `uv add flask`
- Point d'entrée — import Python, `from flask import Flask` ; l'objet obtenu est une application WSGI
- Prérequis — Werkzeug et Jinja2, tirés comme dépendances ; rien d'autre n'est imposé
- Exécution — un serveur WSGI de production (Gunicorn, uWSGI, waitress), souvent derrière Nginx ou en conteneur ; montée en charge par workers puis par réplication
- Coût — gratuit, BSD-3-Clause, aucune limite d'usage

## Écosystème

### Alternatives

- [[FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement.

## Ressources

- Documentation — https://flask.palletsprojects.com
- Dépôt — https://github.com/pallets/flask

## Voir aussi

- [[Web & API]] — le hub du domaine
- [[Jinja2]] — le moteur de gabarits que Flask embarque par défaut
