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

## Pourquoi

**Nature de cette page, à lire en premier** : ce n'est ni un logiciel, ni un service, ni un client d'API. C'est un annuaire de liens — un unique `README.md`. C'est ce que dit son `famille: annuaire` : rien ne s'installe, rien ne se déploie, il n'y a pas de version à suivre. Ne pas le lire comme une brique choisissable. Son `categorie: tooling/api` porte le **sujet listé** (des API), pas sa nature — d'où le voisinage de [[Dev/Outils/Postman|Postman]] et [[Dev/Outils/Bruno|Bruno]], qui sont des clients d'API sur le même domaine et d'une autre famille.

Cela dit, c'est l'annuaire de référence : de l'ordre de **1 700 entrées** réparties en **52 catégories** (météo, finance, jeux vidéo, musique, transports, données ouvertes…), avec pour chacune l'authentification requise, le support HTTPS et le CORS. Maintenu depuis 2016 sous licence MIT.

Utilité concrète : trouver une source de données réelle pour un prototype, une démo, un jeu de test ou un exercice, sans monter un backend.

## Quand l'utiliser

- Chercher une API gratuite pour alimenter un prototype ou une démo.
- Trouver un jeu de données vivant pour tester un pipeline d'ingestion ou une interface.
- Repérer, dans un domaine donné, quels fournisseurs exposent une API publique.

## Quand NE PAS l'utiliser

- Choisir une API pour de la production : rien ne garantit la disponibilité, les quotas ni la pérennité des entrées listées.
- Compter sur la fraîcheur : à cette échelle, la liste contient forcément des liens morts, et le backlog de contributions non triées est de l'ordre de 1 800 issues et autant de pull requests.
- Chercher un outil pour appeler ces APIs : ce n'en est pas un → [[Dev/Outils/Bruno|Bruno]], [[Dev/Outils/Postman|Postman]].

## Installation & plateformes

Aucune installation : une page GitHub, lisible en ligne ou clonée. Pas de langage applicatif, pas de plateforme.

## Pièges

- **L'ancienne API communautaire `api.publicapis.org` n'est plus mise en avant** par le dépôt. Le champ `homepage` pointe désormais vers APILayer.com, avec des paramètres UTM de sponsoring : le lien « API officielle » a été remplacé par un lien commercial.
- Pour une consultation programmatique, ce sont des forks tiers qui proposent une API JSON et une recherche (`public-api-lists/public-api-lists`, `marcelscruz/public-apis`) — pas le dépôt canonique.
- Le nombre d'entrées bouge à chaque merge : ne pas figer un chiffre exact.
- **Aucun tag du vocabulaire fermé ne décrit honnêtement un annuaire de ressources** — la page est volontairement sans tag plutôt qu'étiquetée `api-client`, ce qui serait faux.
- Effet de bord assumé : `[[Comparatif - Clients d'API]]` filtre sur `categorie == "tooling/api"`, donc cette page y apparaîtra alors qu'elle n'est pas un client.

## Alternatives

- Aucune. Un annuaire de liens n'a pas d'équivalent fiché dans le brain, et les clients d'API n'en sont pas des substituts.

## Liens

- [[Dev/Outils/Bruno|Bruno]] — avec quoi appeler ce qu'on y trouve, en local et versionné
- [[Dev/Outils/Postman|Postman]] — l'équivalent cloud et collaboratif
- Repo : https://github.com/public-apis/public-apis
