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
- L'**hypermédia** ([[HTMX]]) est l'alternative sobre au SPA : le serveur renvoie du HTML, le navigateur remplace un fragment de page. Combiné à [[Jinja2]], il couvre l'essentiel des interfaces internes sans introduire de chaîne de build JavaScript. Pour une démo de modèle, comparer avec [[Interfaces & apps data]].

## Choisir

- Une API de service, typée et documentée → [[FastAPI]], servi par [[Uvicorn]].
- Un petit service ou un besoin de contrôle total, écosystème mature → [[Flask]].
- Rendre du HTML côté serveur → [[Jinja2]] ; le rendre interactif sans JavaScript de build → [[HTMX]].
- Une démo à monter en une heure plutôt qu'une API → [[Streamlit]] ou [[Gradio]], pas ce domaine.
- Chercher une API publique à consommer → [[public-apis]].

<!-- AUTO:START -->
### Briques
- [[FastAPI]] — Framework web Python asynchrone : API typées sur Starlette + Pydantic, doc OpenAPI générée automatiquement.
- [[Flask]] — Micro-framework web Python (WSGI) minimaliste et extensible : noyau réduit (routage Werkzeug + templates Jinja2), tout le reste ajouté à la carte par extensions.
- [[HTMX]] — Bibliothèque hypermedia : des attributs HTML déclenchent des requêtes AJAX et remplacent des fragments de page renvoyés en HTML, pour de l'interactivité riche sans JavaScript lourd.
- [[Jinja2]] — Moteur de templates Python rapide et expressif : gabarits HTML avec héritage, échappement automatique et expressions proches de Python ; le moteur de templates de Flask.
- [[public-apis]] — Annuaire communautaire d'APIs publiques et gratuites (MIT, maintenu depuis 2016) : de l'ordre de 1 700 entrées classées en 52 catégories, dans un seul README — pas un client d'API, pas de service, rien à installer.
- [[Uvicorn]] — Serveur ASGI Python performant (uvloop/httptools) qui exécute les applications async comme FastAPI.
<!-- AUTO:END -->
