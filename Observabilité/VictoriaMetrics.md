---
role: brique
nom: VictoriaMetrics
alias: [victoriametrics, MetricsQL]
pitch: "Base de séries temporelles et stockage long terme compatible Prometheus (Apache-2.0, Go) — binaire unique sans dépendance ou version cluster, ingestion remote write, requêtes PromQL et MetricsQL ; édition Enterprise et VictoriaMetrics Cloud."
categorie: observability/supervision
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Prometheus]]"]
complements: ["[[Grafana]]", "[[Alertmanager]]"]
tags: [observability, metrics, self-hosted]
url_docs: https://docs.victoriametrics.com/
url_repo: https://github.com/VictoriaMetrics/VictoriaMetrics
---

# VictoriaMetrics

<!-- AUTO:BANDEAU:START -->
> Base de séries temporelles et stockage long terme compatible Prometheus (Apache-2.0, Go) — binaire unique sans dépendance ou version cluster, ingestion remote write, requêtes PromQL et MetricsQL ; édition Enterprise et VictoriaMetrics Cloud.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Base de séries temporelles pensée comme stockage de métriques et, d'abord, comme stockage long terme de
[[Prometheus]]. Elle existe en deux versions sous Apache-2.0 : un **binaire unique** sans dépendance
externe, et une version cluster. Elle parle l'API de Prometheus — elle peut lire un fichier
`prometheus.yml` de scrape, recevoir de l'écriture distante, et se branche dans [[Grafana]] comme une
source Prometheus — et ajoute **MetricsQL**, qui prolonge PromQL. Le projet affirme, dans ses propres
benchmarks, stocker les données avec sept fois moins d'espace que Prometheus, Thanos ou Cortex, et qu'une
instance unique remplace des clusters de taille moyenne d'autres solutions : des chiffres d'éditeur, à
mesurer sur ses propres séries avant d'en dépendre.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Conserver longtemps les métriques d'un ou plusieurs Prometheus, par écriture distante, sans changer d'API | Fonctions d'entreprise — détection d'anomalies, sauvegarde automatisée, rétentions multiples, sous-échantillonnage : elles sont réservées à l'édition Enterprise, sous licence |
| Monter en charge d'abord verticalement sur un seul binaire, et passer au cluster seulement ensuite | Logs ou traces : cette fiche ne couvre que le stockage de métriques → [[Loki]], [[Tempo]] |
| Reprendre un `prometheus.yml` existant et ses tableaux de bord [[Grafana]] sans les réécrire | |
| Ingérer aussi des protocoles hérités : InfluxDB line protocol, Graphite, OpenTSDB | |

## Mise en œuvre

- Installation — exécutable unique sans dépendance externe, image Docker (Docker Hub ou Quay) ou chart Helm
- Point d'entrée — API compatible Prometheus sur le port 8428 (PromQL ou MetricsQL), branchée dans [[Grafana]] comme une source Prometheus
- Prérequis — rétention par défaut de un mois (`-retentionPeriod`, minimum 24 h) à fixer ; `vmagent` pour collecter, `vmalert` pour évaluer les règles, avec [[Alertmanager]] à déployer pour notifier, `vmbackup` et `vmrestore` pour la sauvegarde
- Exécution — auto-hébergé, en version mono-nœud ou cluster, ou VictoriaMetrics Cloud pour le managé
- Coût — cœur gratuit, Apache-2.0 ; édition Enterprise sur licence, avec essai gratuit ; VictoriaMetrics Cloud à partir de 200 $ par mois d'après la page produit consultée le 2026-09-29

## Écosystème

### Alternatives

- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — la référence de l'écosystème, dont VictoriaMetrics reprend l'API ; son stockage local n'est pas clusterisé.

### Compléments

- [[Grafana]] — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud. — se branche sur VictoriaMetrics comme sur une source Prometheus.
- [[Alertmanager]] — Routeur d'alertes open-source (Apache-2.0, Go) du projet Prometheus — dédoublonne, regroupe, inhibe et met en silence les alertes reçues, puis les route vers le bon récepteur (courriel, PagerDuty, OpsGenie…) ; cluster haute disponibilité. — `vmalert` lui envoie les alertes qu'il évalue.

## Ressources

- Documentation — https://docs.victoriametrics.com/
- Dépôt — https://github.com/VictoriaMetrics/VictoriaMetrics

## Voir aussi

- [[Observabilité]] — le hub du domaine
- [[Métriques, logs et traces]] — la notion : ce que stocke une base de métriques, et ce qu'elle coûte en cardinalité
