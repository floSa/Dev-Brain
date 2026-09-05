---
role: brique
nom: Scrapy
alias: [scrapy]
pitch: "Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production."
categorie: data/scraping
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[Crawlee]]", "[[Scrapling]]"]
complements: ["[[Playwright]]", "[[selectolax]]"]
tags: [web-scraping]
url_docs: https://docs.scrapy.org/
url_repo: https://github.com/scrapy/scrapy
---

# Scrapy

<!-- AUTO:BANDEAU:START -->
> Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de crawling Python maintenu par Zyte depuis plus de quinze ans. L'architecture
sépare quatre pièces : les **spiders** portent la logique de parcours, les **items** les
données typées, les **pipelines** le nettoyage, la validation et le stockage, les
**middlewares** les proxys, les retries et les cookies. Le moteur de requêtes est asynchrone
(Twisted), avec throttling automatique (`AutoThrottle`) et respect de `robots.txt` intégrés.
Il absorbe sans code maison les cas pénibles du métier — encodage, HTML malformé, retries,
politesse. Il ne rend pas le JavaScript : le HTML utile d'une application rendue côté client
lui reste invisible.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Crawl à l'échelle d'un ou de plusieurs sites : suivre les liens, paginer, dédupliquer | Ne rend pas le JavaScript seul — le contenu d'une SPA lui est invisible |
| Le scraping devient un actif de production plutôt qu'un script jetable : spiders, items et pipelines séparés, testables, réutilisables | L'architecture (Twisted, signals, middlewares) déroute au début : la courbe d'apprentissage est réelle |
| Scraping HTTP statique performant — le moteur asynchrone abat un gros débit sans navigateur | Un besoin ponctuel de quelques pages est surdimensionné : un client HTTP et un parseur suffisent |
| | Un spider non throttlé fait bannir l'IP : `AutoThrottle` et la concurrence sont à régler |

## Mise en œuvre

- Installation — `uv add scrapy`
- Point d'entrée — CLI `scrapy` (`startproject`, `crawl`) et classes `Spider` en Python
- Prérequis — Python ; le moteur asynchrone repose sur Twisted
- Exécution — mono-nœud par défaut, ordonnanceur en mémoire ; l'échelle horizontale passe par scrapy-redis (file de requêtes partagée sur Redis) ou par des spiders conteneurisés
- Coût — gratuit, BSD-3 ; Zyte propose Scrapy Cloud, managé et payant, pour l'exécution et l'ordonnancement

## Écosystème

### Alternatives

- [[Crawlee]] — Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante.
- [[Scrapling]] — Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup.

### Compléments

- [[Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement. — via scrapy-playwright, pour les pages qui n'existent qu'après exécution du JS.
- [[selectolax]] — Parseur HTML5 ultra-rapide en Python (binding C Lexbor/Modest) avec sélecteurs CSS — un ordre de grandeur plus rapide que BeautifulSoup pour extraire des données de gros volumes de pages. — utilisable dans les callbacks quand le parsing devient le goulot.

## Ressources

- Documentation — https://docs.scrapy.org/
- Dépôt — https://github.com/scrapy/scrapy

## Voir aussi

- [[Web scraping]] — la notion du dossier : crawl à l'échelle, throttling, politesse
- [[Comparatif - Scraping]] — ce qui départage les outils du dossier
