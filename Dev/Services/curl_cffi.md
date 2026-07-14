---
galaxie: dev
type: service
nom: curl_cffi
alias: [curl-cffi]
pitch: "Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests."
categorie: data/scraping
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/cloudscraper|cloudscraper]]", "[[Dev/Services/Playwright|Playwright]]"]
remplace_par: []
status: actif
tags: [web-scraping]
url_docs: https://curl-cffi.readthedocs.io/
url_repo: https://github.com/lexiforest/curl_cffi
---

# curl_cffi

## Pourquoi

Client HTTP Python qui **imite l'empreinte d'un vrai navigateur** au niveau **TLS/JA3** et **HTTP/2**. Binding (via cffi) vers le fork **curl-impersonate** de libcurl. Beaucoup d'anti-bots ne lisent pas le contenu mais le **fingerprint** de la connexion : `requests` / `httpx` ont une signature reconnaissable, curl_cffi se fait passer pour Chrome / Safari / Firefox (`impersonate="chrome"`). API **calquée sur requests** (`get`, `post`, `Session`), support asyncio, HTTP/2 et HTTP/3, WebSocket. Plus rapide que requests / httpx.

## Quand l'utiliser

- Cible qui bloque sur l'**empreinte TLS/HTTP** (403 alors que le navigateur passe) sans nécessiter d'exécuter du JS.
- Remplacement **drop-in** de requests pour ajouter la furtivité fingerprint.
- Volume élevé : reste un client HTTP léger là où un navigateur serait trop coûteux.

## Quand NE PAS l'utiliser

- Page **rendue en JavaScript** : curl_cffi ne rend rien → [[Dev/Services/Playwright|Playwright]].
- Défi **JS spécifique Cloudflare** (IUAM) à résoudre explicitement → [[Dev/Services/cloudscraper|cloudscraper]] (même si l'empreinte TLS suffit souvent).
- Aucun anti-bot sur fingerprint → `httpx` / `requests` standard suffisent (hors brain).

## Déploiement & coût

- Bibliothèque (`uv add curl_cffi`). Roues précompilées embarquant curl-impersonate. MIT, gratuit.
- **Single-node**, en process. Choisir une cible d'impersonation à jour (les versions de navigateur évoluent).

## Pièges

- L'empreinte imitée **vieillit** : épingler / mettre à jour la cible `impersonate` pour rester crédible.
- Ne **résout pas** les défis JS ni le rendu : c'est du transport, pas un navigateur.
- Un User-Agent incohérent avec l'empreinte TLS choisie trahit le bluff.

## Alternatives

- [[Dev/Services/cloudscraper|cloudscraper]] — Module Python qui contourne la page anti-bot « I'm Under Attack » de Cloudflare en résolvant ses défis JavaScript, par-dessus l'API de requests.
- [[Dev/Services/Playwright|Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.

## Liens

- [[Web scraping]] — section anti-bot / fingerprinting.
- [[Dev/Services/selectolax|selectolax]] — parser le HTML récupéré.
- [[Dev/Patterns/Comparatif - Scraping]]
- Doc : https://curl-cffi.readthedocs.io/
