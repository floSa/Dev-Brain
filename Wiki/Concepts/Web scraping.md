---
galaxie: wiki
type: concept
nom: Web scraping
alias: [scraping, web scraping, crawling, extraction de données web, headless browsing]
categorie: concept/data
domaines: [data-eng]
tags: [web-scraping, data-pipeline]
---

# Web scraping

## Aperçu

- Extraire de façon automatisée des données depuis des pages web quand aucune API ne les expose. Première brique d'ingestion de nombreux jeux de données.
- Tension permanente : récupérer les données de façon fiable et **respectueuse** (charge, légalité, conditions d'usage) face à des sites qui changent et se défendent.

## Concepts clés

### HTTP statique vs rendu navigateur
- Beaucoup de pages se récupèrent par simple requête HTTP puis parsing du HTML (sélecteurs CSS / XPath). Rapide et léger.
- Les pages rendues côté client (JavaScript, SPA) exigent un **navigateur headless** ([[Dev/Services/Playwright|Playwright]], Selenium) qui exécute le JS avant extraction. Plus lourd, plus fragile.

### Authentification de session
- Accéder à du contenu derrière login : rejouer un formulaire, puis **réutiliser les cookies / tokens** de session sur les requêtes suivantes. Gérer l'expiration et le rafraîchissement.

### Anti-bot
- Défenses courantes : limites de fréquence, CAPTCHA, empreinte de navigateur (*fingerprinting*), challenges JS, blocage d'IP. Les contourner relève du jeu du chat et de la souris et soulève des questions légales et éthiques.
- Posture sobre : `User-Agent` honnête, respect de `robots.txt`, pas de surcharge — préférer une API ou un accord quand il en existe un.
- Côté outils (dans le cadre légal ci-dessus) : [[Dev/Services/curl_cffi|curl_cffi]] imite l'empreinte TLS/JA3 d'un navigateur, [[Dev/Services/cloudscraper|cloudscraper]] résout les défis JavaScript de Cloudflare, [[Dev/Services/Playwright|Playwright]] exécute un navigateur complet.

### Throttling et politesse
- Espacer les requêtes (délais, jitter), limiter la concurrence, respecter `Crawl-delay`, mettre en cache pour ne pas re-télécharger. Protège le site cible **et** la stabilité du scraper.

### Robustesse et maintenance
- Le HTML change : isoler les sélecteurs, valider la structure extraite, journaliser les échecs. Un scraper est un actif à maintenir, pas un script one-shot.

## En pratique

- Vérifier d'abord s'il existe une **API** ou un export : presque toujours préférable au scraping.
- Pile typique : `httpx` / `requests` (ou [[Dev/Services/curl_cffi|curl_cffi]] si l'empreinte est filtrée) + `BeautifulSoup` / [[Dev/Services/selectolax|selectolax]] pour le statique ; [[Dev/Services/Scrapy|Scrapy]] ou [[Dev/Services/Crawlee|Crawlee]] pour le crawl à l'échelle (pipelines, throttling intégré) ; [[Dev/Services/Playwright|Playwright]] pour le rendu JS ; [[Dev/Services/Scrapling|Scrapling]] quand les sélecteurs doivent survivre aux changements de page.
- Raccourcis « prêts à l'emploi » : [[Dev/Services/Firecrawl|Firecrawl]] (API site → Markdown pour LLM/RAG) et [[Dev/Services/Maxun|Maxun]] (plateforme no-code, robots enregistrés au navigateur) quand on veut éviter d'écrire et maintenir un scraper.
- Valider et typer la sortie (schéma le cas échéant), puis stocker dans une [[Bases de données|base]] ou un fichier ; profiler ce qui arrive avec une [[EDA automatisée & profiling|EDA]].
- Cadre légal et éthique : conditions d'utilisation, droit des bases de données, données personnelles (RGPD). Le « techniquement possible » n'est pas le « permis ».
- Pièges : sélecteurs fragiles, IP bannies faute de throttling, doublons traités trop tard (voir [[Fuzzy matching & similarité de chaînes]]).

## Approches voisines & alternatives

- [[Bases de données]] — où atterrissent les données collectées.
- [[EDA automatisée & profiling]] — profiler et contrôler la qualité d'un corpus scrapé.
- [[Fuzzy matching & similarité de chaînes]] — dédupliquer et rapprocher des enregistrements bruités.

## Pour aller plus loin

- [[Dev/Services/Scrapy|Scrapy]] — architecture, AutoThrottle, pipelines d'items.
- [[Dev/Services/Playwright|Playwright]] — automatisation de navigateur headless.
- [[Dev/Patterns/Comparatif - Scraping]] — les outils de scraping du brain, comparés.
