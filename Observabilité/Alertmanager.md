---
role: brique
nom: Alertmanager
alias: [alertmanager]
pitch: "Routeur d'alertes open-source (Apache-2.0, Go) du projet Prometheus — dédoublonne, regroupe, inhibe et met en silence les alertes reçues, puis les route vers le bon récepteur (courriel, PagerDuty, OpsGenie…) ; cluster haute disponibilité."
categorie: observability/supervision
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: distributed
alternatives: []
complements: ["[[Prometheus]]", "[[VictoriaMetrics]]"]
tags: [observability, alerting, self-hosted]
url_docs: https://prometheus.io/docs/alerting/latest/alertmanager/
url_repo: https://github.com/prometheus/alertmanager
---

# Alertmanager

<!-- AUTO:BANDEAU:START -->
> Routeur d'alertes open-source (Apache-2.0, Go) du projet Prometheus — dédoublonne, regroupe, inhibe et met en silence les alertes reçues, puis les route vers le bon récepteur (courriel, PagerDuty, OpsGenie…) ; cluster haute disponibilité.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Composant du projet Prometheus qui gère la **livraison** des alertes, et rien d'autre. Il ne lit aucune
métrique et n'évalue aucune règle : ce travail reste à [[Prometheus]], ou à `vmalert` côté
[[VictoriaMetrics]]. Il reçoit des alertes déjà déclenchées, les dédoublonne, les **regroupe** en une
seule notification quand plusieurs relèvent de la même panne, les **inhibe** quand une alerte plus large
est déjà active, les met en **silence** pour une durée donnée, puis les route vers le bon récepteur. Ce
qu'il achète est la fin de la tempête de notifications : pendant une panne étendue, une équipe reçoit un
message par groupe d'alertes, pas un par sonde.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Plusieurs alertes simultanées à regrouper en une notification | Évaluer des règles ou interroger des métriques : Alertmanager ne fait ni l'un ni l'autre, c'est le rôle de [[Prometheus]] |
| Couper les alertes filles quand une panne mère est déjà signalée (inhibition) | Suivi d'incident, astreinte et escalade : il route vers PagerDuty ou OpsGenie, il ne les remplace pas |
| Mettre des alertes en silence pendant une maintenance, depuis l'interface web | Parc réduit dont l'alerte est déjà couverte par l'alerting intégré de [[Grafana]] : un composant de moins à opérer |
| Haute disponibilité de la notification, par un cluster d'instances | |

## Mise en œuvre

- Installation — binaire Go statique, publié dans le dépôt du projet Prometheus
- Point d'entrée — fichier de configuration YAML des routes et des récepteurs ; silences par l'interface web ; les alertes arrivent depuis Prometheus par API
- Prérequis — une source d'alertes configurée pour l'appeler : [[Prometheus]], ou `vmalert` de [[VictoriaMetrics]] par son option `-notifier.url` ; les récepteurs (serveur SMTP, compte PagerDuty ou OpsGenie) à fournir
- Exécution — auto-hébergé ; plusieurs instances configurées en cluster pour la haute disponibilité
- Coût — gratuit, Apache-2.0

## Écosystème

### Alternatives

- *Aucune alternative déclarée : le voisin fonctionnel est l'alerting intégré de [[Grafana]], qui évalue et notifie dans le même outil — hors périmètre d'une brique de routage, pointé dans le tableau ci-dessus.*

### Compléments

- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — évalue les règles et envoie les alertes qu'Alertmanager livre.
- [[VictoriaMetrics]] — Base de séries temporelles et stockage long terme compatible Prometheus (Apache-2.0, Go) — binaire unique sans dépendance ou version cluster, ingestion remote write, requêtes PromQL et MetricsQL ; édition Enterprise et VictoriaMetrics Cloud. — son `vmalert` évalue les règles et s'appuie sur Alertmanager pour notifier.

## Ressources

- Documentation — https://prometheus.io/docs/alerting/latest/alertmanager/
- Dépôt — https://github.com/prometheus/alertmanager

## Voir aussi

- [[Observabilité]] — le hub du domaine
- [[SLO et alerting]] — la notion : quelles alertes valent un message, et lesquelles un ticket
