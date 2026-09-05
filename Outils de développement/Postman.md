---
role: brique
nom: Postman
alias: [postman]
pitch: "Plateforme d'API tout-en-un : collections, environnements, tests, mocks et doc — la référence du marché, cloud et collaborative."
categorie: devtools/client-api
famille: saas
domaines: [data-eng, ai-eng]
licence_type: proprietary
os: "Windows, macOS, Linux, Web"
langage: JavaScript (Electron)
alternatives: ["[[Bruno]]"]
complements: []
tags: [api-client]
url_docs: https://learning.postman.com/docs/
url_repo: 
---

# Postman

<!-- AUTO:BANDEAU:START -->
> Plateforme d'API tout-en-un : collections, environnements, tests, mocks et doc — la référence du marché, cloud et collaborative.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| SaaS | propriétaire | — | — |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de développement d'API, et non simple client de requêtes : on compose et envoie
du HTTP, REST, GraphQL et gRPC, on range en collections, on gère des environnements de
variables, on écrit des tests en JavaScript, puis on publie de la documentation, on monte
des mocks et on branche des monitors. Tout cela est adossé à son **cloud** par défaut :
c'est lui qui porte la synchronisation, les espaces de travail partagés et les services.
L'export de fichiers existe, mais il produit un JSON conçu pour la machine.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Partager collections, espaces de travail et historique dans une équipe | Depuis mars 2026 le plan gratuit est limité à un seul utilisateur, et les quotas sont durs |
| Besoin de la couche plateforme : mocks, monitors, doc publiée, catalogue d'API, intégration CI/CD | Le versionnage git n'est pas natif : l'export est un JSON peu lisible en diff |
| Découvrir et tester une API tierce, avec import OpenAPI ou cURL | Surface fonctionnelle large, plus lourde qu'un simple client de requêtes |

## Mise en œuvre

- Installation — application de bureau Windows, macOS et Linux, ou version web sans installation
- Point d'entrée — client de requêtes HTTP, REST, GraphQL et gRPC, organisé en collections et environnements
- Prérequis — un compte Postman : les collections sont adossées à son cloud par défaut
- Exécution — le client tourne sur le poste ou dans le navigateur ; la synchronisation, les mocks et les monitors tournent dans le cloud Postman
- Coût — freemium : Free limité à un utilisateur depuis mars 2026, puis Basic, Professional et Enterprise ; collaboration, SSO et audit sont derrière des paliers payants

## Écosystème

### Alternatives

- [[Bruno]] — Client d'API git-native et open-source : collections en fichiers texte .bru versionnables, 100 % local, sans compte ni cloud.

## Ressources

- Documentation — https://learning.postman.com/docs/

## Voir aussi

- [[Outils de développement]] — le hub du domaine
- [[Comparatif - Clients d'API]] — ce qui départage les clients du dossier
