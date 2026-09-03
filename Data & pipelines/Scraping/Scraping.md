---
role: hub
nom: Scraping
pitch: Extraire de la donnée depuis des pages web — et tenir face à ce que le site oppose.
domaines: [data-eng]
tags: [web-scraping, data-pipeline]
---

# Scraping

> Extraire de la donnée depuis des pages web — et tenir face à ce que le site oppose.

## Ce qu'il faut comprendre

- Le premier arbitrage est **faut-il un navigateur**. Une page rendue côté serveur se lit avec un client HTTP et un parseur ([[selectolax]]) — quelques millisecondes. Une page rendue par JavaScript exige un navigateur headless ([[Playwright]]) — quelques secondes, et cent fois plus de ressources. Se tromper de côté coûte un ordre de grandeur, dans un sens ou dans l'autre. Cf. [[Web scraping]].
- Le second est **ce que le site oppose**. Contre un filtrage sur l'empreinte TLS et HTTP/2, un navigateur ne sert à rien : il faut imiter l'empreinte ([[curl_cffi]]). Contre une page de défi JavaScript, il faut la résoudre ([[cloudscraper]]). Ces deux problèmes n'ont ni la même cause ni la même solution, et un scraper qui échoue sans qu'on sache lequel des deux le bloque ne se répare pas.
- Le troisième est **l'échelle**, et c'est celui qui décide entre une bibliothèque et un framework. Extraire dix pages est une fonction. En extraire un million demande une file d'URLs persistante, de la déduplication, des reprises, un throttling et une rotation de proxys — [[Scrapy]] et [[Crawlee]] existent pour ça, et les réécrire soi-même est le piège classique du domaine.
- La **fragilité des sélecteurs** est le coût récurrent, pas le coût initial : un site refait sa mise en page et tout casse. [[Scrapling]] attaque ce point précis en re-localisant ses sélecteurs.
- Il existe deux **échappatoires au code** : une API managée qui rend du Markdown prêt pour un LLM ([[Firecrawl]]), et une plateforme où l'on enregistre ses clics ([[Maxun]]). Les deux échangent du contrôle contre du temps.

## Choisir

- Page statique, gros volume, priorité à la vitesse → [[selectolax]].
- Page rendue en JavaScript, ou session à authentifier → [[Playwright]].
- Bloqué par un filtrage d'empreinte TLS / JA3 → [[curl_cffi]].
- Bloqué par la page « I'm Under Attack » de Cloudflare → [[cloudscraper]].
- Crawl structuré à grande échelle, en production → [[Scrapy]].
- Même besoin avec HTTP et navigateur sous une API unique, en TypeScript ou Python → [[Crawlee]].
- Cible qui change souvent, sélecteurs à ne pas maintenir → [[Scrapling]].
- Du Markdown prêt pour un LLM, sans rien écrire → [[Firecrawl]].
- Un robot construit sans code, à faire tenir par un non-développeur → [[Maxun]].
- Des métadonnées musicales, déjà exposées par des API → [[minim]], et non du scraping.

<!-- AUTO:START -->
### Notions
- [[Web scraping]] — domaines : data-eng

### Briques
- [[cloudscraper]] — Module Python qui contourne la page anti-bot « I'm Under Attack » de Cloudflare en résolvant ses défis JavaScript, par-dessus l'API de requests.
- [[Crawlee]] — Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante.
- [[curl_cffi]] — Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests.
- [[Firecrawl]] — API de scraping qui transforme un site entier en Markdown prêt pour LLM (scrape, crawl, extraction structurée) — open source AGPL, self-host ou cloud managé.
- [[Maxun]] — Plateforme no-code open source d'extraction web : on enregistre ses actions dans le navigateur pour créer des robots réutilisables qui transforment un site en API ou tableur, self-host.
- [[minim]] — Bibliothèque Python d'interfaces vers les API musicales (Discogs, iTunes, Qobuz, Spotify, TIDAL, Deezer, Musixmatch) : récupération de métadonnées et tagging audio semi-automatisé.
- [[Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.
- [[Scrapling]] — Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup.
- [[Scrapy]] — Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production.
- [[selectolax]] — Parseur HTML5 ultra-rapide en Python (binding C Lexbor/Modest) avec sélecteurs CSS — un ordre de grandeur plus rapide que BeautifulSoup pour extraire des données de gros volumes de pages.

### Comparatifs
- [[Comparatif - Scraping]]
<!-- AUTO:END -->
