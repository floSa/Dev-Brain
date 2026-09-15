---
role: brique
nom: Uptime Kuma
alias: [uptime-kuma, uptime kuma, kuma]
pitch: "Surveillance de disponibilité auto-hébergée (MIT, Node.js) — sondes HTTP, TCP, ping, DNS, push et conteneurs Docker, notifications vers plus de 90 services, pages de statut publiques ; interface web, sonde de l'extérieur uniquement."
categorie: observability/supervision
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: JavaScript
alternatives: []
complements: []
tags: [observability, uptime, alerting, dashboard, self-hosted]
url_docs: https://github.com/louislam/uptime-kuma/wiki
url_repo: https://github.com/louislam/uptime-kuma
---

# Uptime Kuma

<!-- AUTO:BANDEAU:START -->
> Surveillance de disponibilité auto-hébergée (MIT, Node.js) — sondes HTTP, TCP, ping, DNS, push et conteneurs Docker, notifications vers plus de 90 services, pages de statut publiques ; interface web, sonde de l'extérieur uniquement.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application JavaScript | open-source | self-hébergé | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de surveillance de **disponibilité**, en boîte noire : il sonde un service de l'extérieur, comme le
ferait un utilisateur, et prévient quand la réponse manque. Les sondes couvrent HTTP(S), mot-clé, requête
JSON, WebSocket, TCP, ping, enregistrement DNS, *push* et conteneurs Docker. Les notifications partent vers
plus de 90 services (Telegram, Discord, Gotify, Slack, Pushover, courriel SMTP), et plusieurs pages de
statut, liables à des noms de domaine, se publient depuis la même interface. Ce qu'il ne fait pas est
l'autre moitié de la supervision : il ne dit rien de l'intérieur du service — CPU, saturation, latence par
route. Le livre SRE de Google range ce type de sonde côté « symptômes », et la supervision par métriques
internes côté défaillances imminentes et débogage.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Savoir si un service répond, vu du dehors, avec une alerte à la première panne | Métriques internes — CPU, mémoire, saturation, latence par route : l'outil ne fait que de la sonde externe → [[Prometheus]] |
| Publier une page de statut, ou plusieurs, pour des clients ou des équipes | Système de fichiers NFS pour le stockage : non supporté, le volume doit être local |
| Un petit parc, monté en un conteneur Docker, sans pile à assembler | Plateformes non supportées : FreeBSD, OpenBSD, NetBSD, Replit et Heroku |
| Notifier vers l'outil de messagerie de l'équipe, parmi plus de 90 services | |

## Mise en œuvre

- Installation — Docker (Compose ou commande) ; hors Docker, Node.js 20.4 minimum, Git et PM2
- Point d'entrée — interface web ; sondes *push* et badges pour les intégrations ; les métriques de l'outil s'exposent à [[Prometheus]] avec une clé d'API
- Prérequis — un volume local pour les données ; base SQLite, MariaDB possible en v2 ; depuis la v2, plus de sauvegarde ou restauration JSON — sauvegarder le volume ; nouvelles sondes créées sans nouvelle tentative par défaut
- Exécution — auto-hébergé uniquement ; distributions Linux courantes et Windows 10 ou Server 2012 R2 et suivants
- Coût — gratuit, MIT

## Écosystème

### Alternatives

- [[Zabbix]] — voisin : la supervision d'entreprise couvre aussi les sites web, mais avec un serveur, une base et des agents à opérer.
- [[Netdata]] — voisin : des vérifications synthétiques existent à côté de la supervision des hôtes, mais l'outil est pensé pour l'intérieur des machines.

### Compléments

- *Aucun complément déclaré : les métriques de l'outil s'exposent à [[Prometheus]], mais ce lien est une intégration, pas un couple d'outils.*

## Ressources

- Documentation — https://github.com/louislam/uptime-kuma/wiki
- Dépôt — https://github.com/louislam/uptime-kuma
- Documentation — https://github.com/louislam/uptime-kuma/wiki/Migration-From-v1-To-v2 (changements de rupture v1 vers v2)

## Voir aussi

- [[Observabilité]] — le hub du domaine
- [[SLO et alerting]] — la notion : la sonde externe est la mesure du côté symptôme
