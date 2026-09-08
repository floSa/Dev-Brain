---
role: brique
nom: Scrapling
alias: [scrapling]
pitch: "Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup."
categorie: data/scraping
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: ["[[Scrapy]]", "[[Crawlee]]", "[[Playwright]]"]
complements: []
tags: [web-scraping]
url_docs: https://scrapling.readthedocs.io/
url_repo: https://github.com/D4Vinci/Scrapling
---

# Scrapling

<!-- AUTO:BANDEAU:START -->
> Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | à jour · 2026-08-23 |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de scraping Python qui attaque deux plaies du métier en même temps. La **fragilité
des sélecteurs** d'abord : son parseur **adaptatif** mémorise les éléments ciblés et les
**re-localise automatiquement** quand la structure de la page change, au lieu de casser.
L'**anti-bot** ensuite : ses fetchers **furtifs** passent des protections comme Cloudflare
Turnstile prêtes à l'emploi — empreinte navigateur, HTTP stealth — avec sessions et mode
headless. L'API est proche de BeautifulSoup ou de selectolax, et une API de spider façon
Scrapy couvre le crawl concurrent avec throttling par domaine.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Cibles qui changent souvent de structure : l'adaptatif évite de réécrire les sélecteurs à chaque refonte | Bibliothèque récente dont l'API et les comportements évoluent vite : verrouiller la version en production |
| Furtivité intégrée face à Cloudflare, sans assembler soi-même client stealth et navigateur | Le mode adaptatif réduit la casse mais ne dispense pas de valider la sortie extraite |
| Rester en Python, du simple `get` jusqu'au crawl concurrent | La furtivité anti-bot reste un jeu du chat et de la souris : efficace, jamais garantie dans le temps |
| | Les fetchers navigateur portent les coûts habituels en CPU et en RAM ; seuls les fetchers HTTP restent légers |

## Mise en œuvre

- Installation — `uv add scrapling`
- Point d'entrée — fetchers (HTTP ou navigateur) et sélecteurs adaptatifs, plus une API de spider pour le crawl concurrent
- Prérequis — Python ; les fetchers navigateur tirent les dépendances d'un navigateur
- Exécution — en process, mono-nœud
- Coût — gratuit, BSD-3

## Écosystème

### Alternatives

- [[Scrapy]] — Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production.
- [[Crawlee]] — Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante.
- [[Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.

## Ressources

- Documentation — https://scrapling.readthedocs.io/
- Dépôt — https://github.com/D4Vinci/Scrapling

## Voir aussi

- [[Web scraping]] — la notion du dossier : anti-bot, robustesse des sélecteurs
- [[Comparatif - Scraping]] — ce qui départage les outils du dossier
