---
role: brique
nom: Kimai
alias: [kimai, Kimai 2, kimai2]
pitch: "Application web de suivi du temps à héberger (AGPL-3.0, PHP, Symfony) : feuilles de temps, clients et projets, tarifs, budgets, factures et API JSON, multi-utilisateur avec LDAP ou SAML."
categorie: devtools/projet
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: PHP
scaling: single-node
alternatives: []
complements: ["[[ActivityWatch]]"]
tags: [time-tracking, project-management, self-hosted]
url_docs: https://www.kimai.org/documentation/
url_repo: https://github.com/kimai/kimai
---

# Kimai

<!-- AUTO:BANDEAU:START -->
> Application web de suivi du temps à héberger (AGPL-3.0, PHP, Symfony) : feuilles de temps, clients et projets, tarifs, budgets, factures et API JSON, multi-utilisateur avec LDAP ou SAML.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application PHP | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Application web de suivi du temps **déclaré**, à installer sur son propre serveur. On y saisit du temps par client, projet et activité, avec un minuteur (plusieurs en parallèle, ou pointage arrivée-départ), des étiquettes, des tarifs par utilisateur, client ou projet, des **budgets** en temps et en argent, des rapports, des exports et des **factures**. Le cœur contient aussi une API JSON, des rôles et permissions par équipe, la double authentification (TOTP) et l'authentification par base, **LDAP** ou **SAML**. Plus de 30 traductions, selon le README.

Relevé le 2026-10-07 : **2.69.0** (2026-10-06), dépôt actif (dernier push le 2026-10-06), licence AGPL-3.0 (fichier `LICENSE`), versions publiées « toutes les quelques semaines » d'après le README.

**Licence et offre.** Le code est en **AGPL-3.0**. À côté, le projet vend une version hébergée (Kimai Cloud) et une **boutique de plugins**, gratuits et payants : au relevé, journal d'audit (49 €), champs personnalisés (99 €), gestion des notes de frais (99 €), planification de tâches (79 €), mode borne avec lecteur de code-barres ou RFID (199 €), temps de travail, congés et jours fériés. Les plugins sont destinés aux installations sur site ; certains sont aussi proposés dans la version cloud. Le cœur reste complet pour le suivi du temps et la facturation ; ces extensions sont des **ajouts payants séparés**. À décider selon le besoin : un client qui veut des champs personnalisés ou un journal d'audit devra les acheter.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Du temps à déclarer et facturer par client et par projet (ESN, indépendant), sur un serveur que l'on contrôle | Savoir où est passé le temps sans rien saisir : [[ActivityWatch]] le déduit de l'activité du poste |
| Plusieurs utilisateurs avec rôles, annuaire LDAP ou SAML d'entreprise | Un suivi de tickets, de tâches ou de méthode agile : [[Redmine]] ou [[Kanboard]] |
| Des factures et des budgets issus des saisies, avec une API pour brancher d'autres outils | Un besoin couvert seulement par des plugins payants (journal d'audit, champs libres, notes de frais) : le coût s'ajoute |
| Du solo à des entreprises de dizaines ou de centaines d'utilisateurs, d'après le README : l'outil vise toute cette plage | Une organisation qui interdit l'AGPL-3.0 : elle impose de proposer le code modifié aux utilisateurs distants d'un service, voir plus bas |

## Mise en œuvre

- Installation — images Docker (`kimai/kimai2`, variante FPM seule ou avec Apache), installation en SSH avec Git et Composer, ou une pile Docker Compose avec Caddy ; le projet documente aussi l'hébergement sur site
- Point d'entrée — l'interface web ; une API JSON pour scripter les saisies et lire les rapports
- Prérequis — PHP 8.2 au minimum (8.3, 8.4 et 8.5 pris en charge) ; MariaDB 10.6 ou plus, ou MySQL 8.4 ou plus ; un serveur web **avec un sous-domaine** : un sous-répertoire n'est pas pris en charge ; extensions PHP `gd`, `intl`, `json`, `mbstring`, `pdo`, `tokenizer`, `xml`, `xsl`, `zip`
- Exécution — authentification locale, LDAP ou SAML ; mises à jour décrites version par version dans un guide
- Coût — gratuit pour le cœur ; la machine, la base, et au besoin des plugins payants

## Limites à connaître

- **Le temps est saisi.** Kimai ne déduit rien de l'activité ; sans discipline de saisie, les feuilles sont incomplètes. C'est la différence de fond avec [[ActivityWatch]].
- **Boutique de plugins payants.** Plusieurs fonctions attendues d'un suivi de temps d'entreprise (journal d'audit, champs libres, congés) sont des plugins vendus à part, d'après la boutique ; à chiffrer avant de promettre à un client.
- **AGPL-3.0 pour une ESN.** Utiliser Kimai en interne ou le déployer chez un client sans le modifier ne demande rien de plus ; une version **modifiée** proposée à des utilisateurs par le réseau doit en publier le code source modifié (clause réseau de l'AGPL). À relire avant de forker pour un client.
- **MariaDB ou MySQL seulement.** Aucune prise en charge de PostgreSQL n'apparaît dans les prérequis du README.

## Écosystème

### Compléments

- [[ActivityWatch]] — Application à installer sur le poste (MPL-2.0) qui enregistre en local l'application, la fenêtre, l'onglet de navigateur ou le fichier édité, pour savoir où passe le temps ; les données restent sur la machine. — le temps déduit de l'activité, à rapprocher du temps saisi dans Kimai pour remplir les feuilles sans les oublier.

## Ressources

- Documentation — https://www.kimai.org/documentation/
- Dépôt — https://github.com/kimai/kimai
- Documentation — plugins : https://www.kimai.org/store/

## Voir aussi

- [[Gestion de projet]] — le hub du dossier
- [[Mesurer un projet - DORA, coût des agents et temps passé]] — la notion : le temps passé, côté facturation et côté ESN.
- [[Redmine]] — voisin : saisit aussi du temps, par ticket, avec un rapport par personne, type ou activité.
