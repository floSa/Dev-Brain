---
galaxie: dev
type: service
nom: selectolax
alias: [selectolax]
pitch: "Parseur HTML5 ultra-rapide en Python (binding C Lexbor/Modest) avec sélecteurs CSS — un ordre de grandeur plus rapide que BeautifulSoup pour extraire des données de gros volumes de pages."
categorie: data/scraping
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [web-scraping, document-parsing]
url_docs: https://selectolax.readthedocs.io/
url_repo: https://github.com/rushter/selectolax
---

# selectolax

## Pourquoi

Parseur **HTML5 ultra-rapide** : binding Python (Cython) vers les moteurs C **Lexbor** (par défaut) et **Modest**. On charge le HTML, on interroge avec des **sélecteurs CSS** (`tree.css(...)`, `css_first(...)`) et on extrait texte ou attributs. Sur de gros volumes de pages, il est **un ordre de grandeur plus rapide** que BeautifulSoup ou lxml, pour une empreinte mémoire faible. C'est l'étape de **parsing** : il ne récupère pas les pages (pas de client HTTP), il les découpe.

## Quand l'utiliser

- Extraire des données d'un **grand nombre** de pages HTML où le parsing est le goulot.
- Pipeline de scraping qui privilégie la **vitesse** et la frugalité mémoire.
- Sélection par **CSS** suffisante (cas le plus courant) après récupération du HTML.

## Quand NE PAS l'utiliser

- Petit volume, lisibilité avant tout → BeautifulSoup, plus permissif et documenté (hors brain).
- Besoin de **XPath** riche ou de XSLT → lxml (hors brain).
- Récupérer les pages (HTTP, anti-bot, JS) : selectolax ne fait que parser — voir [[Dev/Services/curl_cffi|curl_cffi]] ou [[Dev/Services/Playwright|Playwright]] en amont.

## Déploiement & coût

- Bibliothèque (`uv add selectolax`). Roues précompilées pour les plateformes courantes.
- **Single-node**, en process. Licence : binding MIT ; moteur Lexbor Apache-2.0, Modest LGPL-2.1.

## Pièges

- N'est **pas** un client HTTP : à coupler avec un fetcher en amont.
- API **CSS uniquement** (pas de XPath) ; cas tordus → lxml.
- Deux backends : Lexbor (défaut, recommandé) vs Modest (legacy — moteur C non maintenu en amont).

## Alternatives

<!-- selectolax est un parseur, complémentaire des fetchers — pas un substitut. Voir Liens. -->
- Aucune dans le brain : comparer à BeautifulSoup / lxml (hors périmètre).

## Liens

- [[Web scraping]] — l'étape parsing du pipeline.
- [[Dev/Services/curl_cffi|curl_cffi]] · [[Dev/Services/Playwright|Playwright]] — récupèrent les pages que selectolax parse.
- [[Dev/Patterns/Comparatif - Scraping]]
- Doc : https://selectolax.readthedocs.io/
