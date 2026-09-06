---
role: brique
nom: Uvicorn
alias: [uvicorn]
pitch: "Serveur ASGI Python performant (uvloop/httptools) qui exécute les applications async comme FastAPI."
categorie: web/backend
famille: cli
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[FastAPI]]"]
tags: [web-framework]
url_docs: https://uvicorn.dev
url_repo: https://github.com/Kludex/uvicorn
---

# Uvicorn

<!-- AUTO:BANDEAU:START -->
> Serveur ASGI Python performant (uvloop/httptools) qui exécute les applications async comme FastAPI.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| CLI Python | open-source | en ligne de commande, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur **ASGI** pour Python : il parle HTTP/1.1 et WebSockets, et exécute les applications web
asynchrones — FastAPI, Starlette, Django en mode ASGI. Sa vitesse vient de deux dépendances
optionnelles, `uvloop` pour la boucle d'événements et `httptools` pour l'analyse HTTP, réunies
sous l'extra `standard`. C'est la brique d'exécution standard de l'écosystème async Python : le
framework décrit les routes, Uvicorn les sert. Il ne fait volontairement rien d'autre — ni TLS,
ni routage L7, ni supervision multi-processus avancée. Maintenu par Marcelo Trylesinski
(Kludex), le projet ayant quitté l'organisation `encode` pour `Kludex/uvicorn`.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Servir une application ASGI en développement (`--reload`) comme en production | Application WSGI synchrone (Flask, Django classique) : il faut un serveur WSGI, Gunicorn seul ou uWSGI |
| Charge I/O-bound asynchrone où un serveur léger et rapide suffit | Terminaison TLS, routage L7, fichiers statiques : à déléguer à un reverse proxy (Nginx, Traefik) placé devant |
| Accepter de superviser les workers par Gunicorn ou par le conteneur | Pas de supervision multi-processus avancée native : un processus = un nœud, le reste se réplique |
| | `uvloop` n'est pas disponible sous **Windows** — la boucle asyncio standard prend le relais, sans le gain de vitesse |
| | L'install minimale est nettement plus lente que `uvicorn[standard]` : oublier l'extra coûte des performances sans le dire |

## Mise en œuvre

- Installation — `uv add "uvicorn[standard]"` ; l'extra tire `uvloop` et `httptools`
- Point d'entrée — la commande `uvicorn module:app`, ou l'API Python `uvicorn.run()`
- Prérequis — une application ASGI ; `uvloop` exige un système POSIX
- Exécution — un processus par instance, en local ou en conteneur ; montée en charge par workers Gunicorn ou par réplication, derrière un reverse proxy
- Coût — gratuit, BSD-3-Clause, aucune limite d'usage

## Écosystème

### Alternatives

<!-- Aucune : aucun autre serveur ASGI n'est fiché dans le brain. FastAPI est le framework compagnon, pas un substitut. -->

### Compléments

- [[FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement. — l'application que ce serveur exécute ; c'est le couple par défaut de l'écosystème async Python

## Ressources

- Documentation — https://uvicorn.dev
- Dépôt — https://github.com/Kludex/uvicorn

## Voir aussi

- [[Web & API]] — le hub du domaine
