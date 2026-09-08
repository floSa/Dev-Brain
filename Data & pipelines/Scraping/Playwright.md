---
role: brique
nom: Playwright
alias: [playwright, playwright-python]
pitch: "Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement."
categorie: data/scraping
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[curl_cffi]]", "[[cloudscraper]]", "[[Crawlee]]", "[[Scrapling]]"]
complements: ["[[selectolax]]", "[[Scrapy]]"]
tags: [web-scraping]
url_docs: https://playwright.dev/python/
url_repo: https://github.com/microsoft/playwright-python
---

# Playwright

<!-- AUTO:BANDEAU:START -->
> Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-07-31 |
<!-- AUTO:BANDEAU:END -->

## Définition

Pilote un **vrai navigateur** — Chromium, Firefox, WebKit — en mode headless derrière une API
unique. Le navigateur **exécute le JavaScript**, ce qu'aucune requête HTTP ne fait : c'est la
seule façon de voir le HTML d'une page rendue côté client. Les attentes sont **auto-résolues**,
l'API patientant jusqu'à ce qu'un élément soit prêt, ce qui supprime les `sleep` fragiles.
L'**état de session** (cookies, localStorage) se sauvegarde par `storage_state` et se rejoue,
ou se conserve dans un contexte persistant : on se connecte une fois, on réutilise ensuite.
Signé Microsoft ; la bibliothèque Python pilote un driver Node sous le capot. Le même outil sert de
framework de tests E2E.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Pages rendues en JavaScript, où le HTML utile n'apparaît qu'après exécution du script | Un navigateur complet par worker coûte cher en CPU et en RAM : sur de gros volumes, l'HTTP reste bien moins lourd |
| Scénarios derrière login, avec session à persister et à rejouer | Le headless est détectable (`navigator.webdriver`, fingerprint) : la furtivité n'est pas son objectif premier |
| Interactions nécessaires avant extraction : clics, scroll infini, formulaires | `playwright install` est obligatoire après l'installation du paquet, sinon aucun navigateur n'est disponible |
| Un seul outil pour le scraping et les tests E2E d'interface | |

## Mise en œuvre

- Installation — `uv add playwright`, puis `playwright install` pour télécharger les navigateurs
- Point d'entrée — API Python, synchrone ou asynchrone : navigateur, contexte, page
- Prérequis — les dépendances système des navigateurs ; en CI ou en Docker, l'image officielle `mcr.microsoft.com/playwright` les porte
- Exécution — mono-nœud ; paralléliser par contextes plutôt que par process, chaque navigateur consommant CPU et mémoire
- Coût — gratuit, Apache-2.0

## Écosystème

### Alternatives

- [[curl_cffi]] — Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests.
- [[cloudscraper]] — Module Python qui contourne la page anti-bot « I'm Under Attack » de Cloudflare en résolvant ses défis JavaScript, par-dessus l'API de requests.
- [[Crawlee]] — Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante.
- [[Scrapling]] — Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup.

### Compléments

- [[selectolax]] — Parseur HTML5 ultra-rapide en Python (binding C Lexbor/Modest) avec sélecteurs CSS — un ordre de grandeur plus rapide que BeautifulSoup pour extraire des données de gros volumes de pages. — parse le HTML une fois la page rendue récupérée.
- [[Scrapy]] — Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production. — via scrapy-playwright, quand un crawl structuré doit rendre le JS.

## Ressources

- Documentation — https://playwright.dev/python/
- Dépôt — https://github.com/microsoft/playwright-python

## Voir aussi

- [[Web scraping]] — la notion du dossier : rendu navigateur contre HTTP statique
- [[Comparatif - Scraping]] — ce qui départage les outils du dossier
