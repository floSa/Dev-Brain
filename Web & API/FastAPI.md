---
role: brique
nom: FastAPI
alias: [fastapi]
pitch: "Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement."
categorie: web/backend
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Flask]]"]
complements: ["[[Uvicorn]]", "[[HTMX]]"]
tags: [web-framework, type-hints]
url_docs: https://fastapi.tiangolo.com
url_repo: https://github.com/fastapi/fastapi
---

# FastAPI

<!-- AUTO:BANDEAU:START -->
> Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework web Python centré sur les **API**, bâti sur **Starlette** (couche ASGI, routage) et
**Pydantic** (validation). Il déduit des annotations de type la validation des entrées et des
sorties, la sérialisation et la **documentation OpenAPI** — Swagger UI et ReDoc sont servies
sans une ligne de plus. Le modèle d'exécution est **asynchrone** : une route `async def` rend
la main pendant ses I/O, ce qui est exactement le régime des appels réseau, des bases async et
des services LLM. Il ne rend **aucune page** : c'est un backend d'API, la présentation se
branche ailleurs. Créé par Sebastián Ramírez (tiangolo), ligne 0.13x en 2026.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Exposer une API REST/JSON typée, surtout en contexte I/O-bound (réseau, base async, services LLM) | Une route déclarée `def` plutôt qu'`async def` qui fait de l'I/O bloque l'event loop sous charge |
| Vouloir la doc OpenAPI et la validation Pydantic sans code répétitif | Rendu de templates serveur classique, ou application surtout synchrone → [[Flask]] |
| Backend Python d'une app data/ML qui sert des modèles ou des pipelines | Besoin d'un cadre « batteries incluses » — admin, ORM, auth intégrés : Django, non fiché ici |
| | Dépendance forte à Pydantic : la migration v1 → v2 a changé l'API de validation |

## Mise en œuvre

- Installation — `uv add fastapi`
- Point d'entrée — import Python, `from fastapi import FastAPI` ; l'objet obtenu est une application ASGI
- Prérequis — Pydantic (v2 pour la ligne courante) et un serveur ASGI pour exécuter l'application
- Exécution — derrière Uvicorn, souvent supervisé par Gunicorn (workers) ou en conteneur ; sans état, donc réplicable horizontalement ou en serverless
- Coût — gratuit, MIT, aucune limite d'usage

## Écosystème

### Alternatives

- [[Flask]] — Micro-framework web Python (WSGI) minimaliste et extensible : noyau réduit (routage Werkzeug + templates Jinja2), tout le reste ajouté à la carte par extensions.

### Compléments

- [[Uvicorn]] — Serveur ASGI Python performant (uvloop/httptools) qui exécute les applications async comme FastAPI. — la brique d'exécution, sans laquelle l'application ne tourne pas
- [[HTMX]] — Bibliothèque hypermedia : des attributs HTML déclenchent des requêtes AJAX et remplacent des fragments de page renvoyés en HTML, pour de l'interactivité riche sans JavaScript lourd. — la couche d'interactivité quand ce backend doit aussi servir des pages

## Ressources

- Documentation — https://fastapi.tiangolo.com
- Dépôt — https://github.com/fastapi/fastapi

## Voir aussi

- [[Web & API]] — le hub du domaine
- [[Comparatif - Frontends web légers]] — ce qui départage FastAPI + HTMX de Streamlit, Gradio et Dash
- [[Pydantic]] — la validation dont FastAPI dérive tout son typage
