---
role: hub
nom: Observabilité
alias: [observabilite, observability, monitoring]
pitch: Savoir ce qu'un système fait en production — métriques, logs et traces, puis un endroit unique pour les regarder.
domaines: [mlops, infra-ops]
tags: [observability, logging, metrics, dashboard, self-hosted]
---

# Observabilité

> Savoir ce qu'un système fait en production — métriques, logs et traces, puis un endroit unique pour les regarder.

## Ce qu'il faut comprendre

- Trois signaux, trois usages, et on les confond souvent. Une **métrique** est un nombre agrégé dans le temps : elle dit *que* quelque chose va mal, à coût constant. Un **log** est un événement textuel : il dit *pourquoi*, mais son volume est proportionnel au trafic. Une **trace** suit une requête à travers les services : elle dit *où*. Alerter sur des logs quand une métrique suffirait est la façon la plus rapide de faire exploser une facture.
- Le domaine se lit en étages. **Produire** la télémétrie : [[OpenTelemetry]] standardise l'instrumentation et le transport, sans rien stocker. **Collecter et stocker** : [[Prometheus]] ou [[VictoriaMetrics]] pour les métriques, [[Loki]] pour les logs, [[Tempo]] pour les traces. **Alerter** : [[Alertmanager]], qui livre les alertes que d'autres évaluent. **Afficher** : [[Grafana]]. [[Grafana]] ne stocke rien : c'est une façade sur plus de 150 sources, et c'est ce qui en fait le point de convergence par défaut.
- L'idée qui a rendu [[Loki]] adoptable : **indexer les labels, pas le contenu**. On paye l'index sur quelques dimensions (service, environnement, niveau) et on garde les corps de logs en blocs compressés. Le compromis est assumé — la recherche plein texte y est lente, la recherche par label immédiate.
- Côté MLops, l'observabilité d'infrastructure ne suffit pas : la dérive de données et la dégradation d'un modèle ne se voient pas dans le CPU. C'est un sujet distinct, à traiter avec les briques de suivi de modèle.
- Deux notions tiennent le domaine : [[Métriques, logs et traces]] dit ce que chaque signal apporte et ce qu'il coûte ; [[SLO et alerting]] dit à partir de quel niveau de service réveiller quelqu'un, et pourquoi le symptôme prime sur la cause.
- Ne pas confondre : le [[Prometheus]] d'ici est le système de supervision ; [[Prometheus-Eval]], dans l'évaluation des LLM, est un modèle juge sans rapport.

## Choisir

- Un serveur ou une poignée de machines, à surveiller sans monter une pile → [[Beszel]], quelques mégaoctets, historique inclus ; ou [[Netdata]] pour le détail à la seconde, dont l'interface est sous licence propriétaire.
- Des métriques d'infrastructure et de services, collectées en *pull*, avec règles d'alerte → [[Prometheus]] ; pour garder longtemps l'historique ou dépasser un serveur, [[VictoriaMetrics]] reprend son API.
- Regrouper, inhiber et router les alertes au lieu de les recevoir une à une → [[Alertmanager]], derrière [[Prometheus]] ou [[VictoriaMetrics]].
- Instrumenter une fois, sans lier le code à un backend → [[OpenTelemetry]], dont le Collector n'est pas un stockage.
- Suivre une requête à travers les services → [[Tempo]], lu depuis [[Grafana]], sur le même stockage objet que [[Loki]] ; Jaeger n'a pas de fiche (v1 en fin de vie depuis le 2025-12-31, v2 bâti sur le Collector OpenTelemetry).
- Savoir si un service répond, vu de l'extérieur, et publier une page de statut → [[Uptime Kuma]].
- Un parc hétérogène sous un seul outil, réseau et SNMP compris, avec serveur, base et agents à opérer → [[Zabbix]].
- Des tableaux de bord et des alertes sur des sources existantes → [[Grafana]].
- Centraliser les logs de plusieurs services sans payer un index plein texte → [[Loki]], lu depuis [[Grafana]].
- Explorer et visualiser des logs déjà indexés dans [[Elasticsearch]] → [[Kibana]] ; il ne lit que cette source, là où [[Grafana]] en branche plus de 150.

<!-- AUTO:START -->
### Notions
- [[Métriques, logs et traces]] — domaines : infra-ops, mlops
- [[SLO et alerting]] — domaines : infra-ops, mlops

### Briques
- [[Alertmanager]] — Routeur d'alertes open-source (Apache-2.0, Go) du projet Prometheus — dédoublonne, regroupe, inhibe et met en silence les alertes reçues, puis les route vers le bon récepteur (courriel, PagerDuty, OpsGenie…) ; cluster haute disponibilité.
- [[Beszel]] — Hub de supervision de serveurs léger (Go, MIT) : CPU, mémoire, disque, réseau, température, statistiques des conteneurs Docker, historique et alertes, en architecture hub + agents.
- [[Grafana]] — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud.
- [[Kibana]] — Interface web de la suite Elastic (triple AGPL / SSPL / ELv2) — explore (Discover), visualise (Lens, dashboards) et alerte sur les données d'Elasticsearch ; ne fonctionne qu'avec lui.
- [[Loki]] — Système open-source d'agrégation de logs (AGPLv3) inspiré de Prometheus — indexe des labels plutôt que le contenu, stocke des chunks compressés sur object store ; horizontalement scalable, requêté en LogQL et visualisé dans Grafana.
- [[Netdata]] — Agent de supervision temps réel (GPLv3+, Go, C, Rust) — métriques à la seconde d'hôtes, conteneurs et applications sans configuration, tableau de bord local sur le port 19999, alertes locales ; interface sous licence propriétaire NCUL1, Netdata Cloud optionnel.
- [[OpenTelemetry]] — Cadre d'observabilité open-source (Apache-2.0, CNCF) neutre vis-à-vis des fournisseurs — spécification, protocole OTLP, SDK, instrumentation automatique et Collector qui reçoit, traite et exporte traces, métriques et logs ; n'est pas un backend.
- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif.
- [[Tempo]] — Backend de traces distribuées open-source (AGPL-3.0, Go) de Grafana Labs — stockage sur object store sans index, accepte OTLP, Jaeger et Zipkin, requêté en TraceQL depuis Grafana ; mode monolithique ou microservices, Grafana Cloud Traces pour le managé.
- [[Uptime Kuma]] — Surveillance de disponibilité auto-hébergée (MIT, Node.js) — sondes HTTP, TCP, ping, DNS, push et conteneurs Docker, notifications vers plus de 90 services, pages de statut publiques ; interface web, sonde de l'extérieur uniquement.
- [[VictoriaMetrics]] — Base de séries temporelles et stockage long terme compatible Prometheus (Apache-2.0, Go) — binaire unique sans dépendance ou version cluster, ingestion remote write, requêtes PromQL et MetricsQL ; édition Enterprise et VictoriaMetrics Cloud.
- [[Zabbix]] — Plateforme de supervision distribuée d'entreprise (AGPL-3.0 depuis la 7.0, C, PHP, Go) — serveur, agents actifs ou passifs, collecte sans agent (SNMP, IPMI), modèles, déclencheurs et tableaux de bord sur MySQL, MariaDB ou PostgreSQL ; proxies pour les sites distants.
<!-- AUTO:END -->
