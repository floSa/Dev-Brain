---
role: brique
nom: curl_cffi
alias: [curl-cffi]
pitch: "Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests."
categorie: data/scraping
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[cloudscraper]]", "[[Playwright]]"]
complements: ["[[selectolax]]"]
tags: [web-scraping]
url_docs: https://curl-cffi.readthedocs.io/
url_repo: https://github.com/lexiforest/curl_cffi
---

# curl_cffi

<!-- AUTO:BANDEAU:START -->
> Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-09-02 |
<!-- AUTO:BANDEAU:END -->

## Définition

Client HTTP Python qui **imite l'empreinte d'un vrai navigateur** au niveau **TLS/JA3** et
**HTTP/2**. C'est un binding, via cffi, vers **curl-impersonate**, le fork de libcurl qui
reproduit ces signatures. Beaucoup d'anti-bots ne lisent pas le contenu de la page mais le
**fingerprint de la connexion** : `requests` et `httpx` ont une signature reconnaissable,
curl_cffi se fait passer pour Chrome, Safari ou Firefox via `impersonate="chrome"`. L'API est
calquée sur requests (`get`, `post`, `Session`), avec asyncio, HTTP/2, HTTP/3 et WebSocket, et
se substitue donc à requests sans réécriture. Il ne rend rien : c'est du transport, pas un
navigateur.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Cible qui répond 403 à requests alors que le navigateur passe : le blocage porte sur l'empreinte TLS ou HTTP | Ne résout aucun défi JavaScript et ne rend aucune page — le contenu d'une SPA lui reste invisible |
| Remplacement drop-in de requests pour ajouter la furtivité fingerprint | L'empreinte imitée vieillit : la cible `impersonate` s'épingle et se met à jour pour rester crédible |
| Volume élevé, où un navigateur serait trop coûteux : reste un client HTTP léger | Un User-Agent incohérent avec l'empreinte TLS choisie trahit le bluff |
| | Sans anti-bot sur le fingerprint, `httpx` ou `requests` standard suffisent — hors brain |

## Mise en œuvre

- Installation — `uv add curl_cffi`
- Point d'entrée — API façon requests : `get`, `post`, `Session(impersonate=...)`
- Prérequis — roues précompilées embarquant curl-impersonate ; aucune dépendance système
- Exécution — en process, mono-nœud
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[cloudscraper]] — Module Python qui contourne la page anti-bot « I'm Under Attack » de Cloudflare en résolvant ses défis JavaScript, par-dessus l'API de requests.
- [[Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.

### Compléments

- [[selectolax]] — Parseur HTML5 ultra-rapide en Python (binding C Lexbor/Modest) avec sélecteurs CSS — un ordre de grandeur plus rapide que BeautifulSoup pour extraire des données de gros volumes de pages. — parse le HTML que curl_cffi récupère.

## Ressources

- Documentation — https://curl-cffi.readthedocs.io/
- Dépôt — https://github.com/lexiforest/curl_cffi

## Voir aussi

- [[Web scraping]] — la notion du dossier : anti-bot et fingerprinting
- [[Comparatif - Scraping]] — ce qui départage les outils du dossier
