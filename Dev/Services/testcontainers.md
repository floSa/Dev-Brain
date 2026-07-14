---
galaxie: dev
type: service
nom: testcontainers
alias: [testcontainers-python, Testcontainers]
pitch: "Dépendances jetables (bases, brokers, navigateurs…) lancées en conteneurs Docker le temps d'un test, démarrées et nettoyées automatiquement."
categorie: tooling/test
licence_type: open-source
hosted: self
maturite: production
langage: Python
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [testing, container]
url_docs: https://testcontainers.com/
url_repo: https://github.com/testcontainers/testcontainers-python
---

# testcontainers

## Pourquoi

Bibliothèque qui fournit une API conviviale pour **lancer des conteneurs Docker dans les tests**. Au lieu de mocker une dépendance ou de maintenir une base partagée, chaque test (ou suite) démarre une **instance jetable et isolée** d'un service réel — Postgres, Redis, Kafka, un navigateur Selenium, n'importe quelle image — puis Testcontainers l'**arrête et la nettoie** à la fin (conteneur sentinelle *Ryuk*). Résultat : des tests d'intégration qui s'exécutent contre la vraie dépendance, reproductibles en local comme en CI. Portage Python d'un projet multi-langage (`testcontainers-python`), avec des modules prêts à l'emploi par technologie.

## Quand l'utiliser

- Tests d'intégration nécessitant une vraie base ou un vrai broker, sans dépendre d'un service partagé.
- Garantir l'isolation : chaque exécution part d'un état propre, pas de pollution entre tests.
- Reproduire en CI l'environnement de dépendances réelles, à l'identique du poste de dev.

## Quand NE PAS l'utiliser

- Tests unitaires purs sans I/O externe : un mock ou un fake suffit, le conteneur est un surcoût.
- Environnement sans démon Docker disponible (certains CI restreints) : Testcontainers en a besoin.
- Démarrage de conteneurs trop lent pour une boucle de feedback serrée : réserver aux tests d'intégration.

## Déploiement & coût

- Bibliothèque de développement (`uv add --dev testcontainers`). Apache-2.0, gratuit.
- Local et CI ; nécessite un **démon Docker** (ou compatible) accessible. Rien à héberger en propre.

## Pièges

- Dépendance dure à Docker : prévoir le cas des runners CI sans accès au socket Docker.
- Coût de démarrage des conteneurs : mutualiser via la portée des fixtures pour ne pas relancer à chaque test.
- Le nettoyage repose sur Ryuk ; si ce conteneur est bloqué (politiques de sécurité), gérer l'arrêt explicitement.

## Alternatives

- `docker-compose` orchestré à la main, bases en mémoire / fakes (SQLite, fakeredis), mocks — Testcontainers se distingue en lançant la **vraie** dépendance, isolée et auto-nettoyée. *(Pages dédiées non créées.)*

## Liens

- Voisin direct : [[Dev/Services/pytest|pytest]] — les conteneurs jetables s'exposent en fixtures pytest pour les tests d'intégration.
- Doc : https://testcontainers.com/
