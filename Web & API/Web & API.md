---
role: hub
nom: Web & API
alias: [web, api, http]
pitch: Exposer un service par HTTP et rendre des pages — le socle par lequel un modèle ou un pipeline devient utilisable.
domaines: [data-eng, mlops, ai-eng]
tags: [web-framework, api-client, hypermedia, templating]
---

# Web & API

> Exposer un service par HTTP et rendre des pages — le socle par lequel un modèle ou un pipeline devient utilisable.

## Ce qu'il faut comprendre

- Pour un profil data, ce domaine sert presque toujours la même chose : **mettre un modèle ou un traitement derrière une URL**. La question n'est donc pas « quel framework web » mais « ai-je besoin d'une API, d'une interface, ou des deux ».
- La ligne de partage entre [[FastAPI]] et [[Flask]] n'est pas l'ancienneté mais le **contrat**. FastAPI dérive la validation, la sérialisation et la documentation OpenAPI des annotations de type ([[Pydantic]]) : le schéma est le code. Flask ne présume rien et laisse tout choisir. Pour une API de service ML, le contrat automatique gagne.
- **Le framework n'est pas le serveur.** [[FastAPI]] est une application ASGI ; c'est [[Uvicorn]] qui l'exécute. Confondre les deux mène à des mises en production où le nombre de workers, les timeouts et l'arrêt gracieux n'ont jamais été réglés.
- **Le serveur n'est pas non plus ce qui reçoit le monde.** Devant [[Uvicorn]] ou [[Flask]], un reverse proxy termine le TLS, obtient les certificats, route par nom d'hôte et répartit la charge : [[Traefik]], [[Caddy]], [[Nginx]] ou [[HAProxy]]. Le piège est en aval : l'application ne voit plus que l'adresse du proxy, et ne lit `X-Forwarded-For` ou `X-Forwarded-Proto` que si on lui dit en quels proxys avoir confiance.
- L'**hypermédia** ([[HTMX]]) est l'alternative sobre au SPA : le serveur renvoie du HTML, le navigateur remplace un fragment de page. Combiné à [[Jinja2]], il couvre l'essentiel des interfaces internes sans introduire de chaîne de build JavaScript. Pour une démo de modèle, comparer avec [[Interfaces & apps data]].

## Choisir

- Une API de service, typée et documentée → [[FastAPI]], servi par [[Uvicorn]].
- Un petit service ou un besoin de contrôle total, écosystème mature → [[Flask]].
- Exposer plusieurs services derrière un nom d'hôte et un certificat → un reverse proxy : [[Traefik]] si les services sont des conteneurs qui bougent, [[Caddy]] pour un HTTPS sans y penser, [[Nginx]] pour la référence installée, [[HAProxy]] pour la répartition de charge TCP et HTTP.
- Rendre du HTML côté serveur → [[Jinja2]] ; le rendre interactif sans JavaScript de build → [[HTMX]].
- Une démo à monter en une heure plutôt qu'une API → [[Streamlit]] ou [[Gradio]], pas ce domaine.
- Chercher une API publique à consommer → [[public-apis]].

<!-- AUTO:START -->
### Briques
- [[Caddy]] — Serveur web et reverse proxy à HTTPS automatique : un Caddyfile de quelques lignes obtient et renouvelle ses certificats, publics par ACME ou internes par sa propre autorité (Apache-2.0, Go, ZeroSSL) — pas de découverte Docker native, et tout module tiers impose de recompiler le binaire.
- [[FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement.
- [[Flask]] — Micro-framework web Python (WSGI) minimaliste et extensible : noyau réduit (routage Werkzeug + templates Jinja2), tout le reste ajouté à la carte par extensions.
- [[HAProxy]] — Répartiteur de charge TCP et HTTP à haute performance, configuré dans un seul haproxy.cfg (GPL-2.0, C, HAProxy Technologies) — health checks actifs, stick-tables et rechargement sans coupure ; ne sert pas de fichiers statiques, ACME natif encore expérimental, WAF et synchronisation multi-nœuds réservés à l'édition Enterprise.
- [[HTMX]] — Bibliothèque hypermedia : des attributs HTML déclenchent des requêtes AJAX et remplacent des fragments de page renvoyés en HTML, pour de l'interactivité riche sans JavaScript lourd.
- [[Jinja2]] — Moteur de templates Python rapide et expressif : gabarits HTML avec héritage, échappement automatique et expressions proches de Python ; le moteur de templates de Flask.
- [[Nginx]] — Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24.
- [[public-apis]] — Annuaire communautaire d'APIs publiques et gratuites (MIT, maintenu depuis 2016) : de l'ordre de 1 700 entrées classées en 52 catégories, dans un seul README — pas un client d'API, pas de service, rien à installer.
- [[Traefik]] — Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub.
- [[Uvicorn]] — Serveur ASGI Python performant (uvloop/httptools) qui exécute les applications async comme FastAPI.
<!-- AUTO:END -->
