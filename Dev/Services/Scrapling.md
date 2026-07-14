---
galaxie: dev
type: service
nom: Scrapling
alias: [scrapling]
pitch: "Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup."
categorie: data/scraping
licence_type: open-source
hosted: self
maturite: beta
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/Scrapy|Scrapy]]", "[[Dev/Services/Crawlee|Crawlee]]", "[[Dev/Services/Playwright|Playwright]]"]
remplace_par: []
status: actif
tags: [web-scraping]
url_docs: https://scrapling.readthedocs.io/
url_repo: https://github.com/D4Vinci/Scrapling
---

# Scrapling

## Pourquoi

Framework de scraping Python qui vise deux plaies du métier : la **fragilité des sélecteurs** et l'**anti-bot**. Son parseur **adaptatif** mémorise les éléments ciblés et les **re-localise automatiquement** quand la structure de la page change, au lieu de casser. Côté récupération, ses **fetchers furtifs** passent des protections comme Cloudflare Turnstile prêtes à l'emploi (empreinte navigateur, HTTP stealth), avec sessions (cookies/état) et mode headless. API familière (proche de BeautifulSoup / selectolax) et **API de spider façon Scrapy** pour le crawl concurrent avec throttling par domaine. Projet récent mais en forte croissance.

## Quand l'utiliser

- Cibles qui **changent souvent** de structure : l'adaptatif évite de réécrire les sélecteurs à chaque refonte.
- Besoin de **furtivité intégrée** (anti-bot Cloudflare) sans assembler soi-même client stealth + navigateur.
- Rester en **Python** avec une API simple, du simple `get` jusqu'au crawl concurrent.

## Quand NE PAS l'utiliser

- Production critique exigeant un socle **éprouvé de longue date** → [[Dev/Services/Scrapy|Scrapy]] (Scrapling est plus jeune).
- Écosystème **Node.js / TypeScript** → [[Dev/Services/Crawlee|Crawlee]].
- Interactions navigateur riches et tests E2E → [[Dev/Services/Playwright|Playwright]].

## Déploiement & coût

- Bibliothèque Python (`uv add scrapling`). BSD-3, gratuit.
- **Single-node**, en process. Les fetchers navigateur ont les coûts habituels (CPU/RAM) ; les fetchers HTTP restent légers.
- Projet jeune et à évolution rapide : épingler la version.

## Pièges

- **Maturité** : bibliothèque récente, API et comportements évoluent vite — verrouiller la version en production.
- Le mode adaptatif réduit la casse mais ne dispense pas de **valider la sortie** extraite.
- La furtivité anti-bot reste un jeu du chat et de la souris : efficace mais non garantie dans le temps.

## Alternatives

- [[Dev/Services/Scrapy|Scrapy]] — Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production.
- [[Dev/Services/Crawlee|Crawlee]] — Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante.
- [[Dev/Services/Playwright|Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.

## Liens

- [[Web scraping]] — le concept (anti-bot, robustesse des sélecteurs).
- [[Dev/Patterns/Comparatif - Scraping]]
- Doc : https://scrapling.readthedocs.io/
