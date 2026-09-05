---
role: brique
nom: cloudscraper
alias: [cloudscraper]
pitch: "Module Python qui contourne la page anti-bot « I'm Under Attack » de Cloudflare en résolvant ses défis JavaScript, par-dessus l'API de requests."
categorie: data/scraping
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: ["[[curl_cffi]]", "[[Playwright]]"]
complements: []
tags: [web-scraping]
url_docs: https://github.com/VeNoMouS/cloudscraper
url_repo: https://github.com/VeNoMouS/cloudscraper
---

# cloudscraper

<!-- AUTO:BANDEAU:START -->
> Module Python qui contourne la page anti-bot « I'm Under Attack » de Cloudflare en résolvant ses défis JavaScript, par-dessus l'API de requests.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Module Python qui vise **une seule défense** : le mode « I'm Under Attack » (IUAM) de
Cloudflare, la page d'attente qui renvoie un 503 ou un 403 à `requests`. Il embarque un
interpréteur JavaScript et **résout le défi côté client**, sans qu'on ait à déobfusquer à la
main la logique de Cloudflare. Il est bâti par-dessus `requests` : on remplace
`requests.Session()` par `cloudscraper.create_scraper()` et le reste du code ne bouge pas.
C'est un contournement daté, engagé dans une course à l'armement que l'éditeur d'en face mène
en continu.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Cible protégée par le JS challenge classique de Cloudflare (IUAM), qui renvoie un 503 ou un 403 à requests | Course à l'armement : Cloudflare durcit ses défenses en continu, la cadence de publication du paquet est irrégulière, et le contournement peut cesser du jour au lendemain |
| Drop-in sur du code existant basé sur requests, sans monter un navigateur | Peu ou pas efficace contre Turnstile et les *managed challenges* récents |
| | Ne vise que les défenses Cloudflare : un blocage d'une autre origine n'est pas son sujet |
| | La latence de résolution des défis JS pèse sur de gros volumes |
| | Contourner une protection anti-bot peut violer les conditions d'usage de la cible : le cadre légal se vérifie avant |

## Mise en œuvre

- Installation — `uv add cloudscraper`
- Point d'entrée — `cloudscraper.create_scraper()`, en remplacement de `requests.Session()`
- Prérequis — un moteur ou interpréteur JavaScript pour résoudre les défis
- Exécution — en process, mono-nœud
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[curl_cffi]] — Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests.
- [[Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.

## Ressources

- Documentation — https://github.com/VeNoMouS/cloudscraper
- Dépôt — https://github.com/VeNoMouS/cloudscraper

## Voir aussi

- [[Web scraping]] — la notion du dossier : anti-bot, et la posture sobre sur le cadre légal
- [[Comparatif - Scraping]] — ce qui départage les outils du dossier
