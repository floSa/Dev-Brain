---
role: brique
nom: Prometheus
alias: [prometheus]
pitch: "Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif."
categorie: observability/supervision
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
scaling: single-node
alternatives: ["[[VictoriaMetrics]]", "[[Zabbix]]"]
complements: ["[[Alertmanager]]", "[[Grafana]]", "[[OpenTelemetry]]", "[[Traefik]]", "[[Caddy]]", "[[Nginx]]", "[[HAProxy]]"]
tags: [observability, metrics, alerting, self-hosted]
url_docs: https://prometheus.io/docs/introduction/overview/
url_repo: https://github.com/prometheus/prometheus
---

# Prometheus

<!-- AUTO:BANDEAU:START -->
> Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé · mono-nœud | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Serveur de supervision du projet Prometheus, distinct du modèle juge [[Prometheus-Eval]]. Il **va chercher**
(*scrape*) à intervalle régulier les métriques que les applications et les exporters exposent en HTTP,
les range dans une base locale sous forme de séries identifiées par un nom et des **labels**, et les
interroge en **PromQL**. Chaque serveur est autonome, sans stockage distribué : la documentation en tire
la fiabilité en cas de panne d'infrastructure, et en énonce le prix — le stockage local n'est ni
clusterisé ni répliqué, et « se gère comme n'importe quelle base mono-nœud ». Le serveur évalue lui-même
les règles d'alerte et envoie les alertes à [[Alertmanager]], qui s'occupe de leur livraison. Le seul vrai
paramètre de conception est la **cardinalité** des labels : le nombre de séries est le produit du nombre
de valeurs de chaque label.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Métriques numériques d'infrastructure et de services, collectées en *pull* avec découverte de services | Exactitude à 100 % exigée, par exemple une facturation à la requête : la documentation écarte elle-même Prometheus, dont les données ne sont pas assez complètes |
| Requêtes dimensionnelles (PromQL) et règles d'alerte au même endroit | Rétention longue ou réplication native : le stockage local n'est pas clusterisé → [[VictoriaMetrics]], ou l'écriture distante (*remote write*) vers un stockage long terme |
| Un composant par rôle — serveur, exporters, Alertmanager — en binaires Go statiques | Logs ou traces : Prometheus ne stocke que des métriques → [[Loki]], [[Tempo]] |
| Instrumentation par bibliothèques clientes, avec la cardinalité des labels sous contrôle | Cibles éphémères qu'on ne peut pas scraper : le Pushgateway existe, mais il est réservé aux jobs de courte durée |

## Mise en œuvre

- Installation — binaire Go statique du serveur ; un composant distinct par exporter et par Alertmanager
- Point d'entrée — fichier de configuration YAML (`prometheus.yml`) des cibles de scrape et des règles ; requêtes PromQL par l'API HTTP, en pratique depuis [[Grafana]]
- Prérequis — des cibles qui exposent leurs métriques en HTTP (bibliothèques clientes ou exporters) ; un disque local à dimensionner, avec 15 jours de rétention par défaut et un journal d'écriture (WAL) découpé en segments de 128 Mo ; [[Alertmanager]] à déployer à part pour notifier ; récepteur OTLP désactivé par défaut (`--web.enable-otlp-receiver`), conversion *delta vers cumulatif* expérimentale
- Exécution — auto-hébergé ; un serveur, une base mono-nœud à sauvegarder comme toute base ; conservation longue par écriture distante
- Coût — gratuit, Apache-2.0 ; aucune offre gérée par le projet

## Écosystème

### Alternatives

- [[VictoriaMetrics]] — Base de séries temporelles et stockage long terme compatible Prometheus (Apache-2.0, Go) — binaire unique sans dépendance ou version cluster, ingestion remote write, requêtes PromQL et MetricsQL ; édition Enterprise et VictoriaMetrics Cloud. — reprend la configuration de scrape et l'API de Prometheus, avec un stockage qui monte en charge là où le sien s'arrête.
- [[Zabbix]] — Plateforme de supervision distribuée d'entreprise (AGPL-3.0 depuis la 7.0, C, PHP, Go) — serveur, agents actifs ou passifs, collecte sans agent (SNMP, IPMI), modèles, déclencheurs et tableaux de bord sur MySQL, MariaDB ou PostgreSQL ; proxies pour les sites distants. — tout-en-un : serveur, agents, modèles, alertes et tableaux de bord, sans assembler exporters et visualisation.

### Compléments

- [[Alertmanager]] — Routeur d'alertes open-source (Apache-2.0, Go) du projet Prometheus — dédoublonne, regroupe, inhibe et met en silence les alertes reçues, puis les route vers le bon récepteur (courriel, PagerDuty, OpsGenie…) ; cluster haute disponibilité. — reçoit les alertes que Prometheus évalue, et les regroupe, les inhibe et les route.
- [[Grafana]] — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud. — la source de données par défaut pour visualiser les métriques.
- [[OpenTelemetry]] — Cadre d'observabilité open-source (Apache-2.0, CNCF) neutre vis-à-vis des fournisseurs — spécification, protocole OTLP, SDK, instrumentation automatique et Collector qui reçoit, traite et exporte traces, métriques et logs ; n'est pas un backend. — Prometheus peut recevoir des métriques OTLP, à activer explicitement.
- [[Traefik]] — Reverse proxy à configuration dynamique : il découvre ses routes dans les labels Docker, dans Kubernetes (Ingress, IngressRoute, Gateway API) ou dans des fichiers (MIT, Go, Traefik Labs) — ACME, tableau de bord et métriques intégrés ; OIDC, JWT, WAF et Let's Encrypt multi-instance sont réservés à l'offre commerciale Traefik Hub. — métriques exposées nativement.
- [[Caddy]] — Serveur web et reverse proxy à HTTPS automatique : un Caddyfile de quelques lignes obtient et renouvelle ses certificats, publics par ACME ou internes par sa propre autorité (Apache-2.0, Go, ZeroSSL) — pas de découverte Docker native, et tout module tiers impose de recompiler le binaire. — option globale `metrics`, sur le port d'administration.
- [[Nginx]] — Serveur web et reverse proxy de référence, configuré à la main dans nginx.conf (BSD-2-Clause, C, F5) — le plus déployé, HTTP/3 et ACME en module ; health checks actifs, API dynamique et JWT réservés à NGINX Plus, l'offre payante ; le contrôleur communautaire ingress-nginx pour Kubernetes est archivé depuis le 2026-03-24. — par `nginx-prometheus-exporter`, qui lit `stub_status`.
- [[HAProxy]] — Répartiteur de charge TCP et HTTP à haute performance, configuré dans un seul haproxy.cfg (GPL-2.0, C, HAProxy Technologies) — health checks actifs, stick-tables et rechargement sans coupure ; ne sert pas de fichiers statiques, ACME natif encore expérimental, WAF et synchronisation multi-nœuds réservés à l'édition Enterprise. — export intégré, sans exporteur séparé.

## Ressources

- Documentation — https://prometheus.io/docs/introduction/overview/
- Dépôt — https://github.com/prometheus/prometheus
- Article — https://prometheus.io/docs/practices/alerting/ (philosophie d'alerte : symptômes plutôt que causes)
- Article — https://prometheus.io/docs/practices/instrumentation/ (cardinalité des labels, types de métriques)

## Voir aussi

- [[Observabilité]] — le hub du domaine
- [[Métriques, logs et traces]] — la notion : ce que mesure une métrique, et ce qu'elle ne dit pas
- [[SLO et alerting]] — la notion : de la règle d'alerte au budget d'erreur
- [[Prometheus-Eval]] — homonyme sans rapport : un modèle juge de LLM, pas ce système de supervision
