---
role: brique
nom: selectolax
alias: [selectolax]
pitch: "Parseur HTML5 ultra-rapide en Python (binding C Lexbor/Modest) avec sélecteurs CSS — un ordre de grandeur plus rapide que BeautifulSoup pour extraire des données de gros volumes de pages."
categorie: data/scraping
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[curl_cffi]]", "[[Playwright]]", "[[Scrapy]]"]
tags: [web-scraping, document-parsing]
url_docs: https://selectolax.readthedocs.io/
url_repo: https://github.com/rushter/selectolax
---

# selectolax

<!-- AUTO:BANDEAU:START -->
> Parseur HTML5 ultra-rapide en Python (binding C Lexbor/Modest) avec sélecteurs CSS — un ordre de grandeur plus rapide que BeautifulSoup pour extraire des données de gros volumes de pages.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-07-15 |
<!-- AUTO:BANDEAU:END -->

## Définition

Parseur HTML5 : binding Cython vers les moteurs C **Lexbor** (par défaut) et **Modest**. On
charge le HTML, on l'interroge avec des **sélecteurs CSS** (`tree.css(...)`,
`css_first(...)`), on en extrait texte ou attributs. Sur de gros volumes de pages, il est **un
ordre de grandeur plus rapide** que BeautifulSoup ou lxml, pour une empreinte mémoire faible.
C'est l'étage de **parsing** seul : il ne récupère pas les pages, il les découpe — un fetcher
lui est donc nécessaire en amont.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Extraire des données d'un grand nombre de pages HTML, où le parsing est le goulot | N'est pas un client HTTP : ne récupère ni ne rend aucune page |
| Pipeline de scraping qui privilégie la vitesse et la frugalité mémoire | API CSS uniquement, sans XPath ni XSLT : les cas tordus demandent lxml, hors brain |
| Sélection par CSS suffisante, ce qui est le cas le plus courant | Petit volume où la lisibilité prime : BeautifulSoup est plus permissif et mieux documenté, hors brain |
| | Deux backends : Lexbor est le défaut recommandé, Modest est legacy — son moteur C n'est plus maintenu en amont |

## Mise en œuvre

- Installation — `uv add selectolax`
- Point d'entrée — chargement du HTML, puis `tree.css(...)` et `css_first(...)`
- Prérequis — roues précompilées pour les plateformes courantes ; aucune dépendance système
- Exécution — en process, mono-nœud
- Coût — gratuit ; binding MIT, moteur Lexbor Apache-2.0, moteur Modest LGPL-2.1

## Écosystème

### Alternatives

- Aucune dans le brain : la comparaison se fait avec BeautifulSoup et lxml, hors périmètre.

### Compléments

- [[curl_cffi]] — Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests. — récupère les pages que selectolax parse.
- [[Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement. — récupère les pages rendues en JavaScript, que selectolax parse ensuite.
- [[Scrapy]] — Framework Python mature de crawling à grande échelle : spiders, pipelines, middlewares et requêtes asynchrones — la référence historique du scraping structuré en production. — l'appelle depuis ses callbacks quand le parsing devient le goulot.

## Ressources

- Documentation — https://selectolax.readthedocs.io/
- Dépôt — https://github.com/rushter/selectolax

## Voir aussi

- [[Web scraping]] — la notion du dossier : l'étape parsing du pipeline
- [[Comparatif - Scraping]] — ce qui départage les outils du dossier
