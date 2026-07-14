---
galaxie: dev
type: service
nom: Playwright
alias: [playwright, playwright-python]
pitch: "Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement."
categorie: data/scraping
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/curl_cffi|curl_cffi]]", "[[Dev/Services/cloudscraper|cloudscraper]]", "[[Dev/Services/Crawlee|Crawlee]]", "[[Dev/Services/Scrapling|Scrapling]]"]
remplace_par: []
status: actif
tags: [web-scraping]
url_docs: https://playwright.dev/python/
url_repo: https://github.com/microsoft/playwright-python
---

# Playwright

## Pourquoi

Pilote un **vrai navigateur** (Chromium, Firefox, WebKit) en mode headless via une API Python unique. Le navigateur **exécute le JavaScript** : indispensable pour les pages rendues côté client (SPA) qu'une simple requête HTTP ne voit pas. Les attentes sont **auto-résolues** (l'API patiente jusqu'à ce qu'un élément soit prêt), ce qui supprime les `sleep` fragiles. L'**état de session** (cookies, localStorage) se sauvegarde (`storage_state`) et se rejoue, ou se conserve dans un **contexte persistant** — login une fois, réutilisé ensuite. Signé Microsoft ; le paquet Python pilote un driver Node sous le capot.

## Quand l'utiliser

- Pages **rendues en JavaScript** / SPA où le HTML utile n'apparaît qu'après exécution du JS.
- Scénarios derrière **login** avec session à persister et rejouer.
- Interactions nécessaires avant extraction : clics, scroll infini, formulaires.
- Aussi un framework de **tests E2E** : le même outil sert au scraping et aux tests d'interface.

## Quand NE PAS l'utiliser

- Pages **statiques** récupérables par simple HTTP → un client léger ([[Dev/Services/curl_cffi|curl_cffi]]) + un parseur ([[Dev/Services/selectolax|selectolax]]) est bien plus rapide.
- Blocage uniquement sur l'**empreinte TLS/HTTP** sans besoin de JS → [[Dev/Services/curl_cffi|curl_cffi]] suffit.
- Très **gros volumes** : un navigateur par page coûte cher en CPU/RAM — préférer l'HTTP quand c'est possible.

## Déploiement & coût

- Bibliothèque (`uv add playwright` puis `playwright install` pour télécharger les navigateurs). Apache-2.0, gratuit.
- **Single-node** ; chaque contexte / navigateur consomme CPU et mémoire — paralléliser via des contextes plutôt que des process.
- En CI / Docker : prévoir les dépendances système des navigateurs (ou l'image officielle `mcr.microsoft.com/playwright`).

## Pièges

- Lourd : un navigateur complet par worker — ne pas l'employer là où l'HTTP suffit.
- Headless détectable : certains sites repèrent l'automatisation (`navigator.webdriver`, fingerprint) — la furtivité n'est pas son objectif premier.
- `playwright install` obligatoire après le `pip`/`uv add`, sinon aucun navigateur disponible.

## Alternatives

- [[Dev/Services/curl_cffi|curl_cffi]] — Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests.
- [[Dev/Services/cloudscraper|cloudscraper]] — Module Python qui contourne la page anti-bot « I'm Under Attack » de Cloudflare en résolvant ses défis JavaScript, par-dessus l'API de requests.
- [[Dev/Services/Crawlee|Crawlee]] — Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante.
- [[Dev/Services/Scrapling|Scrapling]] — Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup.

## Liens

- [[Web scraping]] — rendu navigateur vs HTTP statique : son cas d'usage central.
- [[Dev/Services/selectolax|selectolax]] — parser le HTML une fois la page rendue récupérée.
- [[Dev/Patterns/Comparatif - Scraping]]
- Doc : https://playwright.dev/python/
