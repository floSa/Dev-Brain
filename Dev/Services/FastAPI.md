---
galaxie: dev
type: service
nom: FastAPI
alias: [fastapi]
pitch: "Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement."
categorie: framework/backend
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Flask|Flask]]"]
remplace_par: []
status: actif
tags: [web-framework, type-hints]
url_docs: https://fastapi.tiangolo.com
url_repo: https://github.com/fastapi/fastapi
---

# FastAPI

## Pourquoi

Framework web Python **asynchrone** centré sur les API. Bâti sur Starlette (couche ASGI / routage) et [[Dev/Services/Pydantic|Pydantic]] (validation), il déduit des annotations de type la validation des entrées/sorties, la sérialisation et la **documentation OpenAPI** (Swagger UI / ReDoc). DX forte : autocomplétion, erreurs détectées tôt, peu de code répétitif. Créé par Sebastián Ramírez (tiangolo), très actif (0.13x en 2026).

## Quand l'utiliser

- Exposer une API REST/JSON typée, surtout en contexte I/O-bound (réseau, BDD async, services LLM).
- Profiter de la doc OpenAPI automatique et de la validation Pydantic sans code répétitif.
- Backend Python d'une app data/ML servant des modèles ou des pipelines.

## Quand NE PAS l'utiliser

- App surtout synchrone ou rendu de templates serveur classique → framework WSGI (Django, Flask).
- Besoin d'un framework « batteries incluses » (admin, ORM, auth intégrés) → Django.

## Déploiement & coût

- Bibliothèque open-source (MIT), gratuite. S'exécute derrière un serveur ASGI ([[Dev/Services/Uvicorn|Uvicorn]]), souvent supervisé par Gunicorn (workers) ou en conteneur.
- Sans état : montée en charge horizontale (plusieurs instances derrière un load balancer) ou serverless ; scaling par processus → single-node.

## Pièges

- Une route déclarée `def` (et non `async def`) qui fait de l'I/O bloque l'event loop sous charge → la basculer en `async def` ou la déporter dans un threadpool.
- Dépendance forte à Pydantic : la migration Pydantic v1 → v2 a changé l'API de validation.
- Retours d'expérience détaillés : `Dev/REX/REX - FastAPI.md`.

## Alternatives

- [[Dev/Services/Flask|Flask]] — Micro-framework web Python (WSGI) minimaliste et extensible : noyau réduit (routage Werkzeug + templates Jinja2), tout le reste ajouté à la carte par extensions.

## Liens

- [[Dev/Patterns/Comparatif - Frontends web légers]] — FastAPI+HTMX vs Streamlit / Gradio / Dash.
- [[Dev/Services/Uvicorn|Uvicorn]] — serveur ASGI qui exécute l'application
- [[Dev/Services/Pydantic|Pydantic]] — validation des données dont FastAPI dépend
- Doc : https://fastapi.tiangolo.com
