---
galaxie: dev
type: service
nom: Flask
alias: [flask]
pitch: "Micro-framework web Python (WSGI) minimaliste et extensible : noyau réduit (routage Werkzeug + templates Jinja2), tout le reste ajouté à la carte par extensions."
categorie: framework/backend
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/FastAPI|FastAPI]]"]
remplace_par: []
status: actif
tags: [web-framework]
url_docs: https://flask.palletsprojects.com
url_repo: https://github.com/pallets/flask
---

# Flask

## Pourquoi

Micro-framework web Python **synchrone (WSGI)**. « Micro » ne veut pas dire limité : le cœur est volontairement réduit (routage et utilitaires HTTP via **Werkzeug**, templates via **Jinja2**), et tout le reste — ORM, formulaires, authentification, admin — s'ajoute à la carte par **extensions** (Flask-SQLAlchemy, Flask-Login…). On garde le contrôle de l'architecture, sans conventions imposées. Maintenu par l'organisation **Pallets** (créé en 2010 par Armin Ronacher), licence BSD-3-Clause. Très stable : version 3.1.x (3.1.3, févr. 2026), et de loin le framework web Python le plus téléchargé (~70 M/mois). Des vues `async` sont possibles depuis la 2.0, mais le modèle d'exécution reste WSGI synchrone.

## Quand l'utiliser

- Petite ou moyenne app web, microservice, prototype : démarrage immédiat, peu de cérémonie.
- Besoin de **contrôle** sur la structure et les briques (choisir son ORM, sa validation) plutôt qu'un cadre imposé.
- Rendu de pages côté serveur (Jinja2) autant qu'API JSON.
- Écosystème d'extensions mûr et abondant déjà connu de l'équipe.

## Quand NE PAS l'utiliser

- API JSON typée, fort I/O async (BDD async, appels LLM) avec doc OpenAPI automatique → [[Dev/Services/FastAPI|FastAPI]].
- Besoin d'un framework « batteries incluses » (ORM, admin, auth intégrés) → Django.
- Charge fortement concurrente I/O-bound où l'async natif change la donne → pile ASGI.

## Déploiement & coût

- Bibliothèque open-source (BSD-3-Clause), gratuite. Le serveur de dev intégré n'est **pas** pour la production : servir via un serveur WSGI (Gunicorn, uWSGI, waitress), souvent derrière Nginx ou en conteneur.
- Sans état : montée en charge par **workers** (processus/threads d'un serveur WSGI) et plusieurs instances derrière un load balancer → scaling single-node par réplication.

## Pièges

- Le serveur de développement (`flask run`) est mono-thread par défaut et inadapté à la prod — oubli classique.
- Modèle **synchrone** : une vue qui bloque sur de l'I/O monopolise un worker ; dimensionner les workers, ne pas compter sur l'`async` comme sur une pile ASGI.
- « Micro » = beaucoup de choix laissés à l'intégrateur : sans discipline, les extensions et patterns divergent d'un projet à l'autre.
- Retours d'expérience détaillés : `Dev/REX/REX - Flask.md`.

## Alternatives

- [[Dev/Services/FastAPI|FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement.

## Liens

- [[Dev/Services/FastAPI|FastAPI]] — l'alternative async/API-first la plus directe
- Doc : https://flask.palletsprojects.com
