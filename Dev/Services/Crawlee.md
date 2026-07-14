---
galaxie: dev
type: service
nom: Crawlee
alias: [crawlee, crawlee-python]
pitch: "Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante."
categorie: data/scraping
licence_type: open-source
hosted: self
maturite: production
langage: TypeScript
scaling: single-node
alternatives: ["[[Dev/Services/Scrapy|Scrapy]]", "[[Dev/Services/Scrapling|Scrapling]]", "[[Dev/Services/Playwright|Playwright]]"]
remplace_par: []
status: actif
tags: [web-scraping]
url_docs: https://crawlee.dev/
url_repo: https://github.com/apify/crawlee
---

# Crawlee

## Pourquoi

Framework de crawling d'**Apify**, à **API unifiée** entre crawlers HTTP (Cheerio, BeautifulSoup, Parsel) et crawlers **navigateur** ([[Dev/Services/Playwright|Playwright]], Puppeteer) : on change de moteur sans réécrire la logique. Batteries incluses pour le scraping fiable : **rotation de proxys**, **anti-fingerprint** de navigateur, **autoscaling** selon les ressources, file d'URLs **persistante** (reprise après crash), retries et stockage de datasets. Historiquement Node.js/TypeScript ; le port **Python** (`crawlee-python`) est stable depuis la v1.0 (septembre 2025). Positionné explicitement pour l'extraction de données destinée aux LLM / RAG.

## Quand l'utiliser

- Écosystème **Node.js / TypeScript** pour un crawler de production robuste.
- Besoin de basculer entre **HTTP et navigateur** selon les pages, avec une même base de code.
- Crawls longs nécessitant reprise, proxys et anti-fingerprint sans tout recâbler à la main.

## Quand NE PAS l'utiliser

- Stack **Python** historique et matûre de préférence → [[Dev/Services/Scrapy|Scrapy]].
- Simple pilotage d'un navigateur pour quelques pages JS → [[Dev/Services/Playwright|Playwright]] seul suffit.
- Résilience des sélecteurs aux changements de page → [[Dev/Services/Scrapling|Scrapling]].

## Déploiement & coût

- Bibliothèque (`npm i crawlee` ou `uv add crawlee` pour Python). Apache-2.0, gratuit.
- **Single-node** avec autoscaling interne (adapte la concurrence aux ressources de la machine). Passage à l'échelle et ordonnancement managés via la **plateforme Apify** (payante).
- En navigateur : mêmes contraintes que Playwright/Puppeteer (dépendances système, CPU/RAM).

## Pièges

- Le mode navigateur reste coûteux en ressources — privilégier le crawler HTTP quand le JS n'est pas nécessaire.
- Deux implémentations (Node et Python) à parité proche mais non identique : vérifier la fonctionnalité voulue dans le port choisi.
- L'autoscaling « une machine » ne remplace pas une vraie distribution multi-nœuds (celle-ci passe par la plateforme Apify).

## Alternatives

- [[Dev/Services/Scrapy|Scrapy]] — Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production.
- [[Dev/Services/Scrapling|Scrapling]] — Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup.
- [[Dev/Services/Playwright|Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.

## Liens

- [[Web scraping]] — le concept (HTTP vs navigateur, anti-bot).
- [[Dev/Patterns/Comparatif - Scraping]]
- Doc : https://crawlee.dev/
