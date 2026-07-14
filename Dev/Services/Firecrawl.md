---
galaxie: dev
type: service
nom: Firecrawl
alias: [firecrawl]
pitch: "API de scraping qui transforme un site entier en Markdown prêt pour LLM (scrape, crawl, extraction structurée) — open source AGPL, self-host ou cloud managé."
categorie: data/scraping
licence_type: open-source
hosted: both
maturite: production
langage: TypeScript
scaling: distributed
alternatives: ["[[Dev/Services/Maxun|Maxun]]"]
remplace_par: []
status: actif
tags: [web-scraping, markdown-conversion]
url_docs: https://docs.firecrawl.dev/
url_repo: https://github.com/firecrawl/firecrawl
---

# Firecrawl

## Pourquoi

Service qui **transforme des pages web en Markdown ou JSON structuré directement exploitable par un LLM**, sans avoir à gérer soi-même le rendu JS, la pagination ou le nettoyage du HTML. Un seul appel `scrape` (une URL) ou `crawl` (tout un site en suivant les liens) renvoie du contenu propre, avec une extraction structurée guidée par schéma. Pensé pour l'ingestion RAG et les agents : c'est la brique « du web au contexte » plutôt qu'un framework de crawl bas niveau. Cœur open source sous AGPL-3.0 (SDK MIT), disponible en self-host ou en cloud managé avec proxys et anti-bot inclus.

## Quand l'utiliser

- Alimenter un **RAG** ou un agent : récupérer un site en Markdown propre sans écrire de parseur.
- Extraction **structurée** guidée par schéma (prix, articles, fiches) sur des pages hétérogènes.
- Éviter l'infrastructure de scraping (rendu, proxys, retries) en déléguant à une API.

## Quand NE PAS l'utiliser

- Contrôle fin du crawl (pipelines, middlewares, règles par domaine) → [[Dev/Services/Scrapy|Scrapy]] ou [[Dev/Services/Crawlee|Crawlee]].
- Interactions complexes sur la page (clics, scroll, formulaires) → [[Dev/Services/Playwright|Playwright]].
- Interface **visuelle sans code** pour non-développeurs → [[Dev/Services/Maxun|Maxun]].

## Déploiement & coût

- **Cloud managé** (firecrawl.dev) : facturation à l'usage (crédits par page), proxys et anti-bot gérés.
- **Self-host** (AGPL-3.0, gratuit) : stack Docker avec workers et Redis — orientée service distribué. L'AGPL impose de publier les modifications si le service est exposé.
- SDKs Python, Node, et autres langages pour appeler l'API.

## Pièges

- Coût à la page côté cloud : un crawl large peut consommer beaucoup de crédits — cadrer la profondeur et le périmètre.
- L'AGPL du cœur contraint les usages fermés en self-host exposé — vérifier la compatibilité de licence.
- Dépendance à un service : en self-host, c'est une infrastructure à opérer (Redis, workers), pas une simple lib.

## Alternatives

- [[Dev/Services/Maxun|Maxun]] — Plateforme no-code open source d'extraction web : on enregistre ses actions dans le navigateur pour créer des robots réutilisables qui transforment un site en API ou tableur, self-host.

## Liens

- [[Web scraping]] — le concept (rendu, anti-bot, ingestion).
- [[Dev/Patterns/Comparatif - Scraping]]
- Doc : https://docs.firecrawl.dev/
