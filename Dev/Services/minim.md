---
galaxie: dev
type: service
nom: minim
alias: [minim]
pitch: "Bibliothèque Python d'interfaces vers les API musicales (Discogs, iTunes, Qobuz, Spotify, TIDAL, Deezer, Musixmatch) : récupération de métadonnées et tagging audio semi-automatisé."
categorie: data/scraping
licence_type: open-source
hosted: self
maturite: beta
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [web-scraping]
url_docs: 
url_repo: https://github.com/bbye98/minim
---

# minim

## Pourquoi

minim réunit sous une API Python unifiée des clients pour sept plateformes musicales (Discogs, iTunes, Qobuz, Spotify, TIDAL, Deezer, Musixmatch) plus un module de tagging audio. Deux registres coexistent : les **API publiques officielles** (iTunes, Discogs) pour la métadonnée légitime, et la **reproduction de requêtes navigateur/app** vers des API privées (Qobuz, TIDAL, paroles Spotify) pour atteindre des données absentes des API publiques (paroles synchronisées, flux haute qualité). Le module `minim.audio` lit et écrit métadonnées et pochettes à travers plusieurs formats (MP3/ID3, FLAC/commentaires Vorbis, M4A/MP4).

## Quand l'utiliser

- Constituer un jeu de **métadonnées musicales** multi-sources sous une seule interface Python.
- Automatiser le **tagging** d'une bibliothèque audio locale (titres, pochettes) sur des formats hétérogènes.
- Prototyper un accès à des données de streaming (paroles, qualités audio) pour un usage perso ou de recherche.

## Quand NE PAS l'utiliser

- Scraping web généraliste (HTML, anti-bot) → [[Dev/Services/Scrapy|Scrapy]], [[Dev/Services/Firecrawl|Firecrawl]].
- Usage en production ou à l'échelle : v1 en maintenance, API privées instables, et contraintes de licence / CGU des plateformes.

## Déploiement & coût

- Bibliothèque Python (GPL-3.0), Python 3.9+. Installation depuis le dépôt (`pip install -e .`), pas de paquet PyPI. Single-node, exécution locale.
- Gratuit ; l'accès aux services tiers dépend des comptes et credentials propres à chaque plateforme.
- v1 en **mode maintenance** (corrections critiques seulement) ; réécriture v2 en cours sur la branche `dev`.

## Pièges

- **Zone grise légale** : reproduire les requêtes des apps officielles vers des API privées peut violer les CGU des plateformes — cantonner à un usage perso / recherche, pas commercial.
- API privées **fragiles** : un changement côté Qobuz / TIDAL / Spotify casse le client sans préavis.
- Cache de jetons d'authentification persisté sur disque : prudence sur le stockage des credentials.
- Faible surface de projet (~104 stars, un seul mainteneur) : pérennité incertaine, v2 non stabilisée.

## Alternatives

- Pas d'équivalent référencé dans le brain : brique de niche, hors des domaines cœur. Pour le seul tagging audio, des bibliothèques dédiées comme Mutagen existent (hors brain).

## Liens

- Repo : https://github.com/bbye98/minim
