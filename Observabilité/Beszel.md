---
role: brique
nom: Beszel
alias: [beszel, henrygd/beszel]
pitch: "Hub de supervision de serveurs léger (Go, MIT) : CPU, mémoire, disque, réseau, température, statistiques des conteneurs Docker, historique et alertes, en architecture hub + agents."
categorie: observability/supervision
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: single-node
alternatives: []
complements: []
tags: [observability, metrics, self-hosted, dashboard, container]
url_docs: https://beszel.dev
url_repo: https://github.com/henrygd/beszel
---

# Beszel

<!-- AUTO:BANDEAU:START -->
> Hub de supervision de serveurs léger (Go, MIT) : CPU, mémoire, disque, réseau, température, statistiques des conteneurs Docker, historique et alertes, en architecture hub + agents.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · mono-nœud | production | à jour · 2026-09-03 |
<!-- AUTO:BANDEAU:END -->

## Définition

Supervision de machines réduite à l'essentiel, en deux binaires Go : un **hub** —
application web bâtie sur PocketBase, qui stocke l'historique et sert l'interface — et un
**agent** par machine surveillée, qui remonte CPU, mémoire, charge, disque, bande
passante, température, santé S.M.A.R.T. et les statistiques par conteneur Docker ou
Podman. Les alertes sont des seuils simples, routés vers une vingtaine de destinations
(courriel, Slack, Telegram, Discord, webhook, MQTT, Gotify). Ce que l'outil achète est un
rapport valeur/effort : un conteneur pour le hub, un agent par hôte, et des graphes
historisés dans l'heure — là où une pile Prometheus, exporters, visualisation et
Alertmanager demande quatre composants à configurer, à versionner et à maintenir.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Surveiller quelques serveurs on-prem et leurs conteneurs, sans budget d'exploitation dédié | Métriques applicatives ou instrumentation métier : Beszel collecte des métriques d'**hôte** et n'ingère aucun format Prometheus → [[Grafana]] au-dessus d'une pile Prometheus |
| Répondre avec un historique, et non une intuition, à « le serveur d'entraînement a-t-il saturé la RAM cette nuit ? » | Agrégation de logs, traces distribuées, tableaux de bord composables : hors périmètre → [[Loki]] pour les logs |
| Poser des alertes de seuil sur remplissage disque ou température, là où une pile complète serait disproportionnée | Parc de plusieurs centaines d'hôtes : le hub est mono-nœud, ce n'est pas une plateforme distribuée |
| Donner à un client une page d'état lisible, avec comptes multiples et partage de systèmes | Source de vérité à long terme : la granularité de l'historique est agrégée, pas destinée à l'analyse fine sur plusieurs années |
| Superviser un Raspberry Pi ou un NAS : les agents sont publiés jusqu'en armv5, riscv64 et mips | Règles d'alerte composées ou langage de requête : il n'y a que des seuils |

## Mise en œuvre

- Installation — hub en image Docker ou binaire ; agent en image Docker, binaire, paquet DEB ou script d'installation. Numérotation encore `0.x` et publications rapprochées : lire les notes de version avant de monter, la compatibilité hub/agent n'est pas garantie entre versions éloignées
- Point d'entrée — interface web du hub ; authentification par mot de passe ou OAuth/OIDC
- Prérequis — un agent par hôte (Linux amd64, arm64, armv5/6/7, riscv64, ppc64le, mips ; macOS, Windows, FreeBSD, OpenBSD) ; accès au socket Docker pour les statistiques de conteneurs, qui est un privilège à peser et non à accorder par réflexe ; `hwmon` sous Linux pour la température, droits sur le périphérique pour S.M.A.R.T.
- Exécution — auto-hébergé uniquement, hub mono-nœud, tout l'historique dans PocketBase ; les sauvegardes automatiques (disque ou stockage compatible S3) sont le seul filet et se configurent dès l'installation
- Coût — gratuit, MIT, aucune offre gérée

## Écosystème

### Alternatives

- *Aucune alternative déclarée : le comparable de référence est une pile Prometheus et Grafana, plus puissante et plus coûteuse à exploiter, pointée dans le tableau ci-dessus. Hors brain : Netdata (temps réel très fin, plus verbeux), Zabbix (parc d'entreprise), Glances (poste unique, terminal).*

## Ressources

- Documentation — https://beszel.dev
- Dépôt — https://github.com/henrygd/beszel

## Voir aussi

- [[Observabilité]] — le hub du domaine
- [[Sniffnet]] — l'autre face de la question : Beszel dit comment va la machine, Sniffnet ce qui circule
- [[Docker]] — le hub et les agents se déploient en conteneurs, et les statistiques par conteneur sont l'apport principal
