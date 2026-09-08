---
role: brique
nom: minim
alias: [minim]
pitch: "Bibliothèque Python d'interfaces vers les API musicales (Discogs, iTunes, Qobuz, Spotify, TIDAL, Deezer, Musixmatch) : récupération de métadonnées et tagging audio semi-automatisé."
categorie: data/scraping
famille: paquet
licence_type: open-source
maturite: beta
langage: Python
alternatives: []
complements: []
tags: [web-scraping]
url_docs: 
url_repo: https://github.com/bbye98/minim
---

# minim

<!-- AUTO:BANDEAU:START -->
> Bibliothèque Python d'interfaces vers les API musicales (Discogs, iTunes, Qobuz, Spotify, TIDAL, Deezer, Musixmatch) : récupération de métadonnées et tagging audio semi-automatisé.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | beta | à jour · 2026-04-09 |
<!-- AUTO:BANDEAU:END -->

## Définition

minim réunit sous une API Python unifiée des clients pour **sept plateformes musicales** —
Discogs, iTunes, Qobuz, Spotify, TIDAL, Deezer, Musixmatch — plus un module de tagging audio.
Deux registres y coexistent : les **API publiques officielles** (iTunes, Discogs) pour la
métadonnée légitime, et la **reproduction des requêtes des apps officielles** vers des API
privées (Qobuz, TIDAL, paroles Spotify) pour atteindre ce que les API publiques n'exposent pas
— paroles synchronisées, flux haute qualité. Le module `minim.audio` lit et écrit métadonnées
et pochettes sur plusieurs formats : MP3/ID3, FLAC et commentaires Vorbis, M4A/MP4. C'est le
seul du dossier qui ne parse pas de HTML.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Constituer un jeu de métadonnées musicales multi-sources sous une seule interface Python | Zone grise légale : reproduire les requêtes des apps officielles vers des API privées peut violer les CGU des plateformes — usage perso ou recherche, pas commercial |
| Automatiser le tagging d'une bibliothèque audio locale — titres, pochettes — sur des formats hétérogènes | API privées fragiles : un changement côté Qobuz, TIDAL ou Spotify casse le client sans préavis |
| Prototyper un accès aux données de streaming (paroles, qualités audio) pour un usage perso ou de recherche | v1 en mode maintenance, corrections critiques seulement ; la réécriture v2 est en cours sur la branche `dev` |
| | Faible surface de projet et un seul mainteneur : pérennité incertaine |
| | Cache de jetons d'authentification persisté sur disque : prudence sur le stockage des credentials |

## Mise en œuvre

- Installation — depuis le dépôt (`pip install -e .`) : il n'existe pas de paquet PyPI
- Point d'entrée — un client Python par plateforme, plus le module `minim.audio` pour le tagging
- Prérequis — Python 3.9 ou plus ; comptes et credentials propres à chaque plateforme visée
- Exécution — en local, en process, mono-nœud
- Coût — gratuit, GPL-3.0 ; l'accès aux services tiers dépend des comptes souscrits

## Écosystème

### Alternatives

- Aucune dans le brain : brique de niche, hors des domaines cœur. Pour le seul tagging audio, des bibliothèques dédiées comme Mutagen existent, hors périmètre.

## Ressources

- Dépôt — https://github.com/bbye98/minim

## Voir aussi

- [[Web scraping]] — la notion du dossier : la reproduction de requêtes et son cadre légal
- [[Comparatif - Scraping]] — ce qui départage les outils du dossier
