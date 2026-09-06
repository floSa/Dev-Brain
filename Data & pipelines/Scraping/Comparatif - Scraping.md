---
role: comparatif
nom: Comparatif - Scraping
categorie: data/scraping
tags: [web-scraping, document-parsing, low-code]
---

# Comparatif - Scraping

> On tranche sur : l'étage — récupérer, rendre, parser, orchestrer — puis ce qui bloque en face, l'empreinte de la connexion, le JavaScript ou la refonte de la page.

![[Comparatif - Scraping.base]]

## Ce qui départage

- [[Scrapy]] — le framework de crawl **structuré** : spiders, items, pipelines et middlewares séparés, moteur asynchrone Twisted, `AutoThrottle` et `robots.txt` intégrés. C'est l'outil quand le scraping devient un actif de production plutôt qu'un script. Il ne rend **pas** le JavaScript, et l'architecture déroute au début.
- [[Crawlee]] — la même ambition côté **Node / TypeScript**, avec l'**API unifiée** entre crawler HTTP et crawler navigateur : on change de moteur sans réécrire la logique, rotation de proxys, anti-fingerprint et file d'URLs persistante comprises. Deux implémentations, Node et Python, à parité proche mais **non identique**.
- [[Playwright]] — le **vrai navigateur** (Chromium, Firefox, WebKit) : le JS s'exécute, les attentes sont auto-résolues — plus de `sleep` fragiles — et l'état de session se sauvegarde puis se rejoue. Un navigateur par worker coûte cher en CPU/RAM, le headless est détectable, et `playwright install` est obligatoire après l'installation du paquet.
- [[curl_cffi]] — aucun rendu, mais l'**imitation de l'empreinte TLS/JA3 et HTTP/2** d'un vrai navigateur : c'est ce qu'il faut quand l'anti-bot lit la connexion et non le contenu. L'empreinte imitée **vieillit**, donc `impersonate` s'épingle et se met à jour, et un User-Agent incohérent avec elle trahit le bluff.
- [[cloudscraper]] — une seule défense visée, le **JS challenge IUAM de Cloudflare**, résolu côté client en drop-in de `requests`. Course à l'armement perdue d'avance sur les défenses récentes : peu ou pas efficace contre Turnstile et les *managed challenges*, avec une cadence de publication irrégulière.
- [[Scrapling]] — les deux plaies attaquées ensemble : un parseur **adaptatif** qui **re-localise** un élément quand la structure de la page change, et des fetchers **furtifs** qui passent Cloudflare Turnstile clés en main. Bibliothèque récente dont l'API évolue vite — verrouiller la version en production.
- [[selectolax]] — l'étage **parsing** seul : binding Cython vers Lexbor, un ordre de grandeur plus rapide que BeautifulSoup ou lxml, pour une empreinte mémoire faible. N'est **pas** un client HTTP — il faut un fetcher en amont — et son API est **CSS uniquement**, sans XPath.
- [[Firecrawl]] — l'angle **LLM** : `scrape` et `crawl` rendent du Markdown propre ou du JSON guidé par schéma, rendu JS, proxys et anti-bot compris, sans écrire de parseur. Cœur en **AGPL-3.0**, ce qui contraint un self-host exposé ; coût à la page côté cloud ; et le self-host est une infrastructure à opérer (Redis, workers), pas une lib.
- [[Maxun]] — le seul **no-code** : on enregistre ses actions dans le navigateur pour fabriquer un robot rejouable et planifié, qui transforme un site en API ou en tableur. Plateforme en beta qui évolue vite, et le no-code plafonne sur les sites complexes ou fortement défendus.
- [[minim]] — le seul qui ne scrape pas du HTML : sept plateformes musicales sous une API Python unique, dont des **API privées** reproduites depuis les requêtes des apps officielles, plus un module de tagging audio. **Zone grise légale** assumée, clients qui cassent sans préavis quand la plateforme bouge, v1 en maintenance et un seul mainteneur — usage perso ou recherche, pas production.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
