---
role: brique
nom: testcontainers
alias: [testcontainers-python, Testcontainers]
pitch: "Dépendances jetables (bases, brokers, navigateurs…) lancées en conteneurs Docker le temps d'un test, démarrées et nettoyées automatiquement."
categorie: devtools/test
famille: paquet
licence_type: open-source
maturite: production
langage: Python
alternatives: []
complements: ["[[pytest]]"]
tags: [testing, container]
url_docs: https://testcontainers.com/
url_repo: https://github.com/testcontainers/testcontainers-python
---

# testcontainers

<!-- AUTO:BANDEAU:START -->
> Dépendances jetables (bases, brokers, navigateurs…) lancées en conteneurs Docker le temps d'un test, démarrées et nettoyées automatiquement.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie Python | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Lance des conteneurs Docker depuis le code de test. Plutôt que mocker une dépendance ou
maintenir une base partagée entre les développeurs, chaque test — ou chaque suite — démarre
une instance **jetable et isolée** d'un service réel : Postgres, Redis, Kafka, un navigateur
Selenium, n'importe quelle image. Un conteneur sentinelle, **Ryuk**, se charge de l'arrêt et
du nettoyage même si la suite meurt en cours de route. Les tests d'intégration tournent donc
contre la vraie dépendance, à l'identique sur le poste et en CI. C'est le portage Python
d'un projet multi-langage, avec des modules prêts à l'emploi par technologie.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Tests d'intégration contre une vraie base ou un vrai broker, sans service partagé | Tests unitaires purs, sans entrées-sorties : un mock ou un fake suffit, le conteneur est un surcoût |
| Isolation : chaque exécution part d'un état propre, aucune pollution entre tests | Runner CI sans accès au démon Docker : la dépendance est dure et il n'existe pas de repli |
| Reproduire en CI les dépendances réelles, à l'identique du poste de développement | Boucle de feedback serrée : le démarrage des conteneurs coûte, à mutualiser par la portée des fixtures |
| | Politique de sécurité qui bloque le conteneur Ryuk : il faut alors gérer l'arrêt explicitement |

## Mise en œuvre

- Installation — `uv add --dev testcontainers`
- Point d'entrée — import Python : un conteneur par technologie, ouvert en gestionnaire de contexte ou exposé en fixture
- Prérequis — un démon Docker, ou compatible, accessible depuis le process de test
- Exécution — sur le poste et en CI ; les conteneurs vivent le temps du test, rien à héberger en propre
- Coût — gratuit sous licence Apache-2.0

## Écosystème

### Compléments

- [[pytest]] — Framework de tests Python de référence : assertions natives, fixtures composables et large écosystème de plugins. — c'est par ses fixtures que les conteneurs se partagent et se libèrent

## Ressources

- Documentation — https://testcontainers.com/
- Dépôt — https://github.com/testcontainers/testcontainers-python

## Voir aussi

- [[Outils de développement]] — le hub du domaine
