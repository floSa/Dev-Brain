---
role: brique
nom: Maxun
alias: [maxun]
pitch: "Plateforme no-code open source d'extraction web : on enregistre ses actions dans le navigateur pour créer des robots réutilisables qui transforment un site en API ou tableur, self-host."
categorie: data/scraping
famille: application
licence_type: open-source
hosted: [self, managed]
maturite: beta
langage: TypeScript
scaling: single-node
alternatives: ["[[Firecrawl]]"]
complements: []
tags: [web-scraping, low-code]
url_docs: https://docs.maxun.dev/
url_repo: https://github.com/getmaxun/maxun
---

# Maxun

<!-- AUTO:BANDEAU:START -->
> Plateforme no-code open source d'extraction web : on enregistre ses actions dans le navigateur pour créer des robots réutilisables qui transforment un site en API ou tableur, self-host.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application TypeScript | open-source | self-hébergé ou managé · mono-nœud | beta | à jour · 2026-08-25 |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme **no-code** d'extraction web. Au lieu d'écrire du code, on **enregistre ses
actions** dans le navigateur — mode Recorder — pour fabriquer un **robot** réutilisable qui
rejoue le parcours et extrait les données ; un mode IA permet aussi de décrire en langage
naturel ce qu'on veut extraire. Les robots transforment un site en **API ou en tableur**,
gèrent la pagination et le crawl multi-pages, et s'exécutent de façon planifiée. La cible est
l'utilisateur non-développeur, ou l'extraction récurrente qu'on ne veut pas maintenir en code.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Extractions récurrentes montées vite, sans écrire ni maintenir de scraper en code | Plateforme en beta : fonctionnalités et modèle en cours de stabilisation, à valider sur ses cas avant un usage critique |
| Utilisateurs non-développeurs : construction visuelle par enregistrement d'actions | Le no-code plafonne sur les sites complexes ou fortement défendus : prévoir un repli code |
| Transformer un site en API ou en tableur structuré, avec planification intégrée | Exécution navigateur : coûts CPU et RAM, et fragilité aux changements de page, comme tout scraper visuel |
| | AGPLv3 : un service exposé contraint les usages fermés |

## Mise en œuvre

- Installation — self-host par stack Docker : interface web et navigateur d'exécution
- Point d'entrée — interface web : Recorder d'actions, robots, planification ; les robots exposent une API ou un tableur
- Prérequis — Docker pour le self-host ; aucune compétence de développement pour construire un robot
- Exécution — self-hébergé ou managé (maxun.dev), mono-nœud
- Coût — gratuit en self-host sous AGPLv3 ; l'offre cloud managée est payante

## Écosystème

### Alternatives

- [[Firecrawl]] — API de scraping qui transforme un site entier en Markdown prêt pour LLM (scrape, crawl, extraction structurée) — open source AGPL, self-host ou cloud managé.

## Ressources

- Documentation — https://docs.maxun.dev/
- Dépôt — https://github.com/getmaxun/maxun

## Voir aussi

- [[Web scraping]] — la notion du dossier : extraction, robustesse, cadre légal
- [[Comparatif - Scraping]] — ce qui départage les outils du dossier
