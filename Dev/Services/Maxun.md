---
galaxie: dev
type: service
nom: Maxun
alias: [maxun]
pitch: "Plateforme no-code open source d'extraction web : on enregistre ses actions dans le navigateur pour créer des robots réutilisables qui transforment un site en API ou tableur, self-host."
categorie: data/scraping
licence_type: open-source
hosted: both
maturite: beta
langage: TypeScript
scaling: single-node
alternatives: ["[[Dev/Services/Firecrawl|Firecrawl]]"]
remplace_par: []
status: actif
tags: [web-scraping, low-code]
url_docs: https://docs.maxun.dev/
url_repo: https://github.com/getmaxun/maxun
---

# Maxun

## Pourquoi

Plateforme **no-code** open source d'extraction web. Au lieu d'écrire du code, on **enregistre ses actions** dans le navigateur (mode Recorder) pour fabriquer un **robot** réutilisable qui rejoue le parcours et extrait les données ; un mode IA permet aussi de décrire en langage naturel ce qu'on veut extraire. Les robots transforment un site en **API ou tableur**, gèrent la pagination et le crawl multi-pages, et s'exécutent de façon planifiée. Cible les utilisateurs non-développeurs ou les extractions récurrentes qu'on ne veut pas maintenir en code. Open source AGPLv3, self-hostable via Docker.

## Quand l'utiliser

- Extractions **récurrentes** montées vite, sans écrire ni maintenir de scraper en code.
- Utilisateurs **non-développeurs** : construction visuelle par enregistrement d'actions.
- Transformer un site en **API / tableur** structuré avec planification intégrée.

## Quand NE PAS l'utiliser

- Contrôle programmatique fin et intégration dans un pipeline code → [[Dev/Services/Scrapy|Scrapy]], [[Dev/Services/Crawlee|Crawlee]].
- Ingestion de contenu en **Markdown pour LLM/RAG** via API → [[Dev/Services/Firecrawl|Firecrawl]].
- Sites très défendus ou logique d'extraction complexe : le no-code atteint vite ses limites.

## Déploiement & coût

- **Self-host** (AGPLv3, gratuit) : stack Docker (interface web + navigateur d'exécution). L'AGPL contraint les usages fermés si le service est exposé.
- Une offre **cloud managée** (maxun.dev) existe en complément.
- Projet **en beta** : fonctionnalités et modèle en cours de stabilisation.

## Pièges

- **Maturité** : plateforme en beta, évolue vite — valider sur ses cas avant un usage critique.
- Le no-code plafonne sur les sites complexes ou fortement anti-bot : prévoir un repli code.
- Exécution navigateur : coûts CPU/RAM et fragilité aux changements de page comme tout scraper visuel.

## Alternatives

- [[Dev/Services/Firecrawl|Firecrawl]] — API de scraping qui transforme un site entier en Markdown prêt pour LLM (scrape, crawl, extraction structurée) — open source AGPL, self-host ou cloud managé.

## Liens

- [[Web scraping]] — le concept (extraction, robustesse, cadre légal).
- [[Dev/Patterns/Comparatif - Scraping]]
- Doc : https://docs.maxun.dev/
