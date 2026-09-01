---
galaxie: dev
type: service
nom: Beszel
alias: [beszel, henrygd/beszel]
pitch: "Hub de supervision de serveurs léger (Go, MIT) : CPU, mémoire, disque, réseau, température, statistiques des conteneurs Docker, historique et alertes, en architecture hub + agents."
categorie: observability/infra
famille: plateforme
licence_type: open-source
hosted: self
maturite: production
langage: Go
scaling: single-node
alternatives: []
remplace_par: []
status: actif
tags: [observability, metrics, self-hosted, dashboard, container]
url_docs: https://beszel.dev
url_repo: https://github.com/henrygd/beszel
---

# Beszel

## Pourquoi

Supervision de machines, réduite à l'essentiel. Deux binaires Go : un **hub** (application web bâtie sur PocketBase, qui stocke l'historique et sert l'interface) et un **agent** par machine surveillée, qui remonte CPU, mémoire, charge, disque, bande passante, température et santé S.M.A.R.T., plus les statistiques par conteneur Docker ou Podman. Licence MIT.

L'intérêt réel est le rapport valeur/effort. Une pile Prometheus + exporters + Grafana + Alertmanager demande quatre composants à configurer, à versionner et à maintenir. Beszel demande un conteneur pour le hub, un agent par hôte, et donne dans l'heure des graphes historisés et des alertes par seuil (CPU, mémoire, disque, bande passante, température, charge moyenne), routées vers une vingtaine de destinations (courriel, Slack, Telegram, Discord, webhook, MQTT, Gotify…).

Pour un profil solo qui auto-héberge chez un client, c'est le compromis honnête : voir l'état de trois à quinze machines et de leurs conteneurs sans y consacrer un projet d'infrastructure.

## Quand l'utiliser

- Surveiller quelques serveurs on-prem et leurs conteneurs, sans budget d'exploitation dédié.
- Répondre à « le serveur d'entraînement a-t-il saturé la RAM cette nuit ? » avec un historique, pas une intuition.
- Poser des alertes de seuil simples sur remplissage disque ou température, là où une pile complète serait disproportionnée.
- Donner à un client une page d'état lisible, avec comptes multiples et partage de systèmes.

## Quand NE PAS l'utiliser

- Métriques applicatives et instrumentation métier : Beszel collecte des métriques **d'hôte**, il n'ingère pas de métriques arbitraires ni de format Prometheus → pile Prometheus + [[Dev/Services/Grafana|Grafana]].
- Agrégation de logs : hors périmètre → [[Dev/Services/Loki|Loki]].
- Traces distribuées, requêtes analytiques sur les séries, tableaux de bord composables : hors périmètre.
- Surveillance de dérive de modèle ML : problème différent, voir la catégorie `ml/monitoring`.
- Parc de plusieurs centaines d'hôtes : le hub est mono-nœud, ce n'est pas une plateforme distribuée.

## Déploiement & coût

Auto-hébergé uniquement, aucune offre gérée. Hub en image Docker ou binaire ; agent en image Docker, binaire, paquet DEB ou script d'installation. Les binaires d'agent publiés couvrent Linux (amd64, arm64, armv5/6/7, riscv64, ppc64le, mips…), macOS, Windows, FreeBSD et OpenBSD — le déploiement sur Raspberry Pi ou NAS est un cas prévu.

Coût logiciel nul. Empreinte annoncée comme inférieure aux solutions de référence, sans chiffre officiel repris ici. Sauvegardes automatiques vers le disque ou un stockage compatible S3. Authentification par mot de passe, ou OAuth/OIDC. Version au 2026-08-17 : v0.18.8 — numérotation encore `0.x`, à prendre en compte.

## Pièges

- **Numérotation `0.x` et rythme de publication rapide** : lire les notes de version avant de monter de version, la compatibilité hub/agent n'est pas garantie entre versions éloignées.
- Les statistiques de conteneurs supposent que l'agent accède au socket Docker : c'est un accès privilégié, à peser plutôt qu'à accorder par réflexe.
- Certaines mesures dépendent du système : température et vitesse de ventilateur passent par `hwmon` sous Linux, S.M.A.R.T. exige les droits sur le périphérique.
- Le hub est mono-nœud et stocke tout dans PocketBase : sa sauvegarde est le seul filet, il faut la configurer dès l'installation.
- Ce n'est pas une source de vérité à long terme — la granularité de l'historique est agrégée, pas destinée à de l'analyse fine sur plusieurs années.
- Alertes par seuil seulement : pas de règles composées ni de langage de requête.

## Alternatives

Le champ reste vide faute de fiche réciproque dans la catégorie. Le comparable de référence est la pile Prometheus + [[Dev/Services/Grafana|Grafana]], plus puissante et plus coûteuse à exploiter ; hors brain, Netdata (temps réel très fin, plus verbeux), Zabbix (parc d'entreprise) et Glances (poste unique, terminal).

## Liens

- [[Dev/Services/Docker|Docker]] — le hub et les agents se déploient en conteneurs, et les statistiques par conteneur sont l'apport principal
- [[Dev/Services/Grafana|Grafana]] — l'échelon au-dessus, quand les métriques applicatives entrent en jeu
- [[Dev/Outils/Sniffnet|Sniffnet]] — complément côté trafic : Beszel dit comment va la machine, Sniffnet ce qui circule
- Docs : https://beszel.dev
- Repo : https://github.com/henrygd/beszel
