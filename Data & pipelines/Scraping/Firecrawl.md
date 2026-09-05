---
role: brique
nom: Firecrawl
alias: [firecrawl]
pitch: "API de scraping qui transforme un site entier en Markdown prêt pour LLM (scrape, crawl, extraction structurée) — open source AGPL, self-host ou cloud managé."
categorie: data/scraping
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: TypeScript
scaling: distributed
alternatives: ["[[Maxun]]"]
complements: []
tags: [web-scraping, markdown-conversion]
url_docs: https://docs.firecrawl.dev/
url_repo: https://github.com/firecrawl/firecrawl
---

# Firecrawl

<!-- AUTO:BANDEAU:START -->
> API de scraping qui transforme un site entier en Markdown prêt pour LLM (scrape, crawl, extraction structurée) — open source AGPL, self-host ou cloud managé.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme TypeScript | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Service qui transforme des pages web en **Markdown ou en JSON structuré** directement
exploitable par un LLM. Un appel `scrape` traite une URL, `crawl` parcourt tout un site en
suivant les liens, et l'extraction structurée est guidée par un schéma. Le rendu JavaScript,
la pagination, les proxys, l'anti-bot et le nettoyage du HTML sont pris en charge : c'est la
brique « du web au contexte » plutôt qu'un framework de crawl bas niveau. Le cœur est sous
**AGPL-3.0**, les SDK sous MIT — une distinction qui commande le self-host.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Alimenter un RAG ou un agent : récupérer un site en Markdown propre sans écrire de parseur | Le cœur en AGPL-3.0 impose de publier ses modifications dès que le service est exposé : à vérifier avant tout usage fermé |
| Extraction structurée guidée par schéma sur des pages hétérogènes — prix, articles, fiches | Facturation à la page côté cloud : un crawl large consomme beaucoup de crédits, la profondeur et le périmètre se cadrent |
| Déléguer l'infrastructure de scraping — rendu, proxys, retries — à une API | En self-host, c'est une infrastructure à opérer (Redis, workers), pas une simple bibliothèque |

## Mise en œuvre

- Installation — stack Docker avec workers et Redis pour le self-host ; rien à installer côté cloud managé
- Point d'entrée — API HTTP `scrape` et `crawl`, avec SDK Python, Node et autres langages
- Prérequis — Docker et les services annexes en self-host ; une clé d'API en cloud
- Exécution — self-hébergé ou managé, distribué
- Coût — gratuit en self-host sous AGPL-3.0 ; le cloud est facturé à l'usage, en crédits par page

## Écosystème

### Alternatives

- [[Maxun]] — Plateforme no-code open source d'extraction web : on enregistre ses actions dans le navigateur pour créer des robots réutilisables qui transforment un site en API ou tableur, self-host.

## Ressources

- Documentation — https://docs.firecrawl.dev/
- Dépôt — https://github.com/firecrawl/firecrawl

## Voir aussi

- [[Web scraping]] — la notion du dossier : rendu, anti-bot, ingestion
- [[pdf-inspector]] — même éditeur, côté parsing de documents
- [[Comparatif - Scraping]] — ce qui départage les outils du dossier
