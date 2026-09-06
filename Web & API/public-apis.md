---
role: brique
nom: public-apis
alias: [public-apis/public-apis, awesome public apis]
pitch: "Annuaire communautaire d'APIs publiques et gratuites (MIT, maintenu depuis 2016) : de l'ordre de 1 700 entrées classées en 52 catégories, dans un seul README — pas un client d'API, pas de service, rien à installer."
categorie: web/api
famille: annuaire
domaines: [ai-eng, data-eng]
licence_type: open-source
os: 
langage: 
alternatives: []
complements: []
tags: []
url_docs: https://github.com/public-apis/public-apis
url_repo: https://github.com/public-apis/public-apis
---

# public-apis

<!-- AUTO:BANDEAU:START -->
> Annuaire communautaire d'APIs publiques et gratuites (MIT, maintenu depuis 2016) : de l'ordre de 1 700 entrées classées en 52 catégories, dans un seul README — pas un client d'API, pas de service, rien à installer.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Annuaire | open-source | rien à exécuter | — |
<!-- AUTO:BANDEAU:END -->

## Définition

**Nature de cette page, à lire en premier** : ce n'est ni un logiciel, ni un service, ni un
client d'API. C'est un annuaire de liens — un unique `README.md`. Rien ne s'installe, rien ne
se déploie, il n'y a pas de version à suivre. Ne pas le lire comme une brique choisissable.
Ce qu'il contient : de l'ordre de **1 700 entrées** réparties en **52 catégories** — météo,
finance, jeux vidéo, musique, transports, données ouvertes — chacune annotée de
l'authentification requise, du support HTTPS et du CORS. Maintenu depuis 2016. L'usage concret
est de trouver une source de données réelle pour un prototype, une démo, un jeu de test ou un
exercice, sans monter de backend.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Chercher une API gratuite pour alimenter un prototype ou une démo | Choisir une API pour de la **production** : rien ne garantit la disponibilité, les quotas ni la pérennité des entrées listées |
| Trouver un jeu de données vivant pour tester un pipeline d'ingestion ou une interface | Compter sur la fraîcheur : à cette échelle la liste contient des liens morts, et le backlog non trié est de l'ordre de 1 800 issues et autant de pull requests |
| Repérer, dans un domaine donné, quels fournisseurs exposent une API publique | Chercher un outil pour **appeler** ces API : ce n'en est pas un → [[Bruno]], [[Postman]] |
| | Consultation programmatique : ce sont des forks tiers qui offrent une API JSON et une recherche, pas le dépôt canonique |
| | Le nombre d'entrées bouge à chaque *merge* — ne figer aucun chiffre exact |

## Mise en œuvre

- Installation — aucune : une page GitHub, lisible en ligne ou clonée
- Point d'entrée — le `README.md` du dépôt
- Prérequis — aucun
- Exécution — rien à exécuter
- Coût — gratuit, MIT

## Écosystème

### Alternatives

<!-- Aucune : un annuaire de liens n'a pas d'équivalent fiché dans le brain, et un client d'API n'en est pas un substitut. -->

## Ressources

- Dépôt — https://github.com/public-apis/public-apis
- Documentation — le `README.md` du dépôt ; il n'existe pas de site séparé

## Voir aussi

- [[Web & API]] — le hub du domaine
