---
role: brique
nom: Crawlee
alias: [crawlee, crawlee-python]
pitch: "Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante."
categorie: data/scraping
famille: paquet
licence_type: open-source
maturite: production
langage: TypeScript
alternatives: ["[[Scrapy]]", "[[Scrapling]]", "[[Playwright]]"]
complements: []
tags: [web-scraping]
url_docs: https://crawlee.dev/
url_repo: https://github.com/apify/crawlee
---

# Crawlee

<!-- AUTO:BANDEAU:START -->
> Framework de crawling d'Apify (Node.js et Python) à API unifiée HTTP + navigateur (Playwright/Puppeteer) : rotation de proxys, anti-fingerprint, autoscaling et file d'URLs persistante.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie TypeScript | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Framework de crawling d'**Apify**. Son idée centrale est l'**API unifiée** entre les crawlers
HTTP (Cheerio, BeautifulSoup, Parsel) et les crawlers **navigateur** (Playwright, Puppeteer) :
on change de moteur sans réécrire la logique d'extraction. Il embarque ce qu'un crawler de
production finit toujours par redévelopper — rotation de proxys, anti-fingerprint,
autoscaling selon les ressources de la machine, file d'URLs persistante pour reprendre après
un crash, retries et stockage de datasets. Historiquement Node.js / TypeScript ; le port
Python (`crawlee-python`) est stable depuis la v1.0, en septembre 2025. Positionné
explicitement pour l'extraction de données destinée aux LLM et au RAG.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Écosystème Node.js / TypeScript pour un crawler de production robuste | Deux implémentations, Node et Python, à parité proche mais non identique : vérifier la fonctionnalité voulue dans le port choisi |
| Basculer entre HTTP et navigateur selon les pages, avec une même base de code | Le mode navigateur reste coûteux en CPU et en RAM — préférer le crawler HTTP quand le JS n'est pas nécessaire |
| Crawls longs à reprendre après incident : file d'URLs persistante, retries | L'autoscaling est celui d'une seule machine : la vraie distribution multi-nœuds passe par la plateforme Apify, payante |
| Proxys et anti-fingerprint sans les recâbler à la main | |

## Mise en œuvre

- Installation — `npm i crawlee`, ou `uv add crawlee` pour le port Python
- Point d'entrée — classes de crawler HTTP ou navigateur, partageant la même API
- Prérequis — Node.js ou Python ; en mode navigateur, les dépendances système de Playwright ou Puppeteer
- Exécution — mono-nœud, avec autoscaling interne qui adapte la concurrence aux ressources ; l'ordonnancement managé passe par la plateforme Apify
- Coût — gratuit, Apache-2.0 ; la plateforme Apify est payante

## Écosystème

### Alternatives

- [[Scrapy]] — Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production.
- [[Scrapling]] — Framework de scraping Python adaptatif et furtif : les sélecteurs se re-localisent seuls quand la page change, fetchers anti-bot intégrés (Cloudflare) et API façon BeautifulSoup.
- [[Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.

## Ressources

- Documentation — https://crawlee.dev/
- Dépôt — https://github.com/apify/crawlee

## Voir aussi

- [[Web scraping]] — la notion du dossier : HTTP contre navigateur, anti-bot
- [[Comparatif - Scraping]] — ce qui départage les outils du dossier
