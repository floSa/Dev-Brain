---
galaxie: dev
type: outil
nom: Postman
alias: [postman]
pitch: "Plateforme d'API tout-en-un : collections, environnements, tests, mocks et doc — la référence du marché, cloud et collaborative."
categorie: tooling/api
domaines: [data-eng, ai-eng]
licence_type: proprietary
os: "Windows, macOS, Linux, Web"
langage: JavaScript (Electron)
status: actif
alternatives: ["[[Dev/Outils/Bruno|Bruno]]"]
tags: [api-client]
url_docs: https://learning.postman.com/docs/
url_repo: 
---

# Postman

## Pourquoi

Plateforme complète de développement d'API : composer et envoyer des requêtes HTTP/REST/GraphQL/gRPC, organiser en collections, gérer des environnements de variables, écrire des tests en JavaScript, générer de la doc, créer des mocks et des monitors. Outil le plus répandu, fortement orienté collaboration d'équipe via le cloud.

## Quand l'utiliser

- Travail d'équipe sur des API avec partage de collections, espaces de travail et historique synchronisés dans le cloud.
- Besoin de l'écosystème complet : mocks, monitoring, doc publiée, catalogue d'API, intégration CI/CD.
- Découverte et test ad hoc d'une API tierce, avec import OpenAPI/cURL.

## Quand NE PAS l'utiliser

- Collections versionnables dans git, 100 % local, sans compte ni cloud → [[Dev/Outils/Bruno|Bruno]].
- Refus du modèle propriétaire / freemium à quotas : depuis mars 2026 le plan gratuit est limité à **un seul utilisateur**, toute équipe ≥ 2 doit passer au payant → [[Dev/Outils/Bruno|Bruno]].

## Bases & plateformes

- Propriétaire, modèle freemium (Free 1 utilisateur, Basic, Professional, Enterprise). Plusieurs fonctions (collaboration, SSO, audit) sont derrière des paliers payants.
- Application desktop (Windows, macOS, Linux) et version web. Données et collections adossées au cloud Postman par défaut.

## Pièges

- Les collections vivent dans le cloud Postman par défaut : le versionnage git n'est pas natif et l'export de fichiers reste un format JSON peu lisible en diff.
- Plan gratuit restreint à un utilisateur (mars 2026) ; les quotas sont durs, pas des limites souples.
- Tendance à la « plateforme » : surface fonctionnelle large, plus lourde qu'un simple client de requêtes.

## Alternatives

- [[Dev/Outils/Bruno|Bruno]] — Client d'API git-native et open-source : collections en fichiers texte .bru versionnables, 100 % local, sans compte ni cloud.

## Liens

- [[Comparatif - Clients d'API]] — comparatif des clients d'API
- Doc : https://learning.postman.com/docs/
