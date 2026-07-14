---
galaxie: dev
type: service
nom: Scrapy
alias: [scrapy]
pitch: "Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production."
categorie: data/scraping
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Crawlee|Crawlee]]", "[[Dev/Services/Scrapling|Scrapling]]"]
remplace_par: []
status: actif
tags: [web-scraping]
url_docs: https://docs.scrapy.org/
url_repo: https://github.com/scrapy/scrapy
---

# Scrapy

## Pourquoi

Framework Python complet et **mature** (plus de 15 ans, maintenu par Zyte) pour construire des crawlers structurés. Architecture éprouvée : **spiders** (logique de parcours), **items** (données typées), **pipelines** (nettoyage, validation, stockage) et **middlewares** (proxys, retries, cookies). Moteur de requêtes **asynchrone** (Twisted), throttling automatique (`AutoThrottle`), respect de `robots.txt` intégré. Gère nativement les cas pénibles : encodage, HTML malformé, retries, politesse. C'est l'outil de référence quand le scraping devient un actif de production, pas un script jetable.

## Quand l'utiliser

- **Crawl à l'échelle** d'un ou plusieurs sites : suivre les liens, paginer, dédupliquer, avec pipelines de traitement.
- Besoin de **structure** et de maintenabilité : séparation spider / items / pipelines, tests, réutilisation.
- Scraping HTTP statique performant (le moteur async abat un gros débit sans navigateur).

## Quand NE PAS l'utiliser

- Pages **rendues en JavaScript** : Scrapy ne rend pas le JS seul → coupler à [[Dev/Services/Playwright|Playwright]] (scrapy-playwright) ou choisir [[Dev/Services/Crawlee|Crawlee]].
- Petit besoin ponctuel (une poignée de pages) : le framework est surdimensionné — un client HTTP + parseur suffit.
- Sélecteurs qui doivent survivre aux changements de structure → [[Dev/Services/Scrapling|Scrapling]].

## Déploiement & coût

- Bibliothèque Python (`uv add scrapy`). BSD-3, gratuit.
- **Single-node** par défaut (ordonnanceur en mémoire). Passage à l'échelle horizontale via **scrapy-redis** (file de requêtes partagée sur Redis, workers multiples) ou déploiement des spiders comme workers conteneurisés (Docker/K8s).
- Zyte propose Scrapy Cloud (managé) pour l'exécution et l'ordonnancement.

## Pièges

- Ne rend pas le JavaScript : prévoir une intégration navigateur pour les SPA.
- Courbe d'apprentissage : l'architecture (Twisted, signals, middlewares) déroute au début.
- Un spider non throttlé peut faire bannir l'IP — régler `AutoThrottle` et la concurrence.

## Alternatives

- [[Dev/Services/Crawlee|Crawlee]] — Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante.
- [[Dev/Services/Scrapling|Scrapling]] — Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup.

## Liens

- [[Web scraping]] — le concept (crawl à l'échelle, throttling, politesse).
- [[Dev/Services/selectolax|selectolax]] — parseur HTML rapide utilisable dans les callbacks.
- [[Dev/Patterns/Comparatif - Scraping]]
- Doc : https://docs.scrapy.org/
