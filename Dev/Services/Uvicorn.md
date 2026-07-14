---
galaxie: dev
type: service
nom: Uvicorn
alias: [uvicorn]
pitch: "Serveur ASGI Python performant (uvloop/httptools) qui exécute les applications async comme FastAPI."
categorie: framework/backend
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [web-framework]
url_docs: https://uvicorn.dev
url_repo: https://github.com/Kludex/uvicorn
---

# Uvicorn

## Pourquoi

Serveur **ASGI** pour Python : il exécute les applications web asynchrones ([[Dev/Services/FastAPI|FastAPI]], Starlette, Django ASGI…) en parlant HTTP/1.1 et WebSockets. Implémentation rapide grâce à `uvloop` (event loop) et `httptools` (parsing HTTP), tous deux optionnels. Brique d'exécution standard de l'écosystème async Python. Maintenu par Marcelo Trylesinski (Kludex) — le projet a quitté l'organisation `encode` pour `Kludex/uvicorn`, docs sur `uvicorn.dev`.

## Quand l'utiliser

- Servir une app ASGI ([[Dev/Services/FastAPI|FastAPI]], Starlette) en dev (`--reload`) comme en prod.
- Besoin d'un serveur léger et rapide pour des charges I/O-bound asynchrones.
- En prod, souvent supervisé par Gunicorn (workers) ou en conteneur derrière un reverse proxy.

## Quand NE PAS l'utiliser

- App WSGI synchrone (Flask / Django classiques) → serveur WSGI (Gunicorn seul, uWSGI).
- Terminaison TLS, routage L7, fichiers statiques → déléguer à un reverse proxy (Nginx, Traefik) devant Uvicorn.

## Déploiement & coût

- Bibliothèque open-source (BSD-3-Clause), gratuite ; installée avec l'app (`uvicorn[standard]` pour uvloop/httptools).
- Un processus = single-node ; montée en charge via plusieurs workers/instances. Pas de supervision multi-process avancée native → Gunicorn pour gérer les workers.

## Pièges

- `uvicorn[standard]` (uvloop/httptools) est nettement plus rapide que l'install minimale — penser à l'extra.
- `uvloop` n'est pas disponible sous Windows : event loop asyncio standard par défaut.
- Repo et docs déplacés (`encode` → `Kludex`, `uvicorn.dev`) : d'anciens liens pointent encore vers `encode/uvicorn` / `uvicorn.org`.
- Retours d'expérience détaillés : `Dev/REX/REX - Uvicorn.md`.

## Alternatives

<!-- Pas d'autre serveur ASGI en brain. FastAPI est le framework compagnon, pas une alternative. -->

## Liens

- [[Dev/Services/FastAPI|FastAPI]] — framework ASGI typiquement servi par Uvicorn
- Doc : https://uvicorn.dev
