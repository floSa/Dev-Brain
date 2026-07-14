---
galaxie: dev
type: service
nom: cloudscraper
alias: [cloudscraper]
pitch: "Module Python qui contourne la page anti-bot « I'm Under Attack » de Cloudflare en résolvant ses défis JavaScript, par-dessus l'API de requests."
categorie: data/scraping
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Dev/Services/curl_cffi|curl_cffi]]", "[[Dev/Services/Playwright|Playwright]]"]
remplace_par: []
status: actif
tags: [web-scraping]
url_docs: https://github.com/VeNoMouS/cloudscraper
url_repo: https://github.com/VeNoMouS/cloudscraper
---

# cloudscraper

## Pourquoi

Module Python qui **contourne la page anti-bot de Cloudflare** (mode « I'm Under Attack », IUAM) en **résolvant ses défis JavaScript** côté client. Construit par-dessus `requests` : on remplace `requests.Session()` par `cloudscraper.create_scraper()` et le reste du code ne bouge pas. Embarque un interpréteur JS pour passer les challenges sans déobfusquer à la main la logique de Cloudflare.

## Quand l'utiliser

- Cible protégée par le **JS challenge classique** de Cloudflare (IUAM) qui renvoie un 503/403 à `requests`.
- Besoin d'un **drop-in** sur du code existant basé sur requests, sans monter un navigateur.

## Quand NE PAS l'utiliser

- Défenses **modernes** (Turnstile, *managed challenge*, filtrage sur l'empreinte TLS) : l'approche par défis JS est souvent dépassée → [[Dev/Services/curl_cffi|curl_cffi]] (empreinte TLS) ou un vrai navigateur [[Dev/Services/Playwright|Playwright]].
- Blocage **non-Cloudflare** → cloudscraper ne vise que les défenses Cloudflare.
- Gros volume où la latence de résolution des défis JS pèse → repenser l'approche.

## Déploiement & coût

- Bibliothèque (`uv add cloudscraper`). MIT, gratuit. **Single-node**, en process.
- Nécessite un moteur / interpréteur JavaScript pour résoudre les défis.

## Pièges

- **Course à l'armement** : Cloudflare durcit ses défenses en continu, la cadence de publication du paquet est irrégulière et le contournement peut cesser de fonctionner du jour au lendemain.
- Peu ou pas efficace contre **Turnstile** et les *managed challenges* récents.
- Légalité / CGU : contourner une protection anti-bot peut violer les conditions d'usage — voir la posture sobre de [[Web scraping]].

## Alternatives

- [[Dev/Services/curl_cffi|curl_cffi]] — Client HTTP Python (binding curl-impersonate) qui imite l'empreinte TLS/JA3 et HTTP/2 d'un vrai navigateur — passe les anti-bots qui filtrent sur le fingerprint, avec une API façon requests.
- [[Dev/Services/Playwright|Playwright]] — Automatisation de navigateur headless (Chromium, Firefox, WebKit) via une API unique : exécute le JavaScript des pages, persiste l'état de session (cookies, storage) et attend le rendu automatiquement.

## Liens

- [[Web scraping]] — section anti-bot.
- [[Dev/Patterns/Comparatif - Scraping]]
- Doc : https://github.com/VeNoMouS/cloudscraper
