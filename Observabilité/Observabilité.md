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
- Le domaine se lit en deux étages. Les briques qui **collectent et stockent** ([[Loki]] pour les logs, Prometheus pour les métriques) et celles qui **affichent** ([[Grafana]]). [[Grafana]] ne stocke rien : c'est une façade sur plus de 150 sources, et c'est ce qui en fait le point de convergence par défaut.
- L'idée qui a rendu [[Loki]] adoptable : **indexer les labels, pas le contenu**. On paye l'index sur quelques dimensions (service, environnement, niveau) et on garde les corps de logs en blocs compressés. Le compromis est assumé — la recherche plein texte y est lente, la recherche par label immédiate.
- Côté MLops, l'observabilité d'infrastructure ne suffit pas : la dérive de données et la dégradation d'un modèle ne se voient pas dans le CPU. C'est un sujet distinct, à traiter avec les briques de suivi de modèle.

## Choisir

- Un serveur ou une poignée de machines, à surveiller sans monter une pile → [[Beszel]], quelques mégaoctets, historique inclus.
- Des tableaux de bord et des alertes sur des sources existantes → [[Grafana]].
- Centraliser les logs de plusieurs services sans payer un index plein texte → [[Loki]], lu depuis [[Grafana]].

<!-- AUTO:START -->
### Briques
- [[Beszel]] — Hub de supervision de serveurs léger (Go, MIT) : CPU, mémoire, disque, réseau, température, statistiques des conteneurs Docker, historique et alertes, en architecture hub + agents.
- [[Grafana]] — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud.
- [[Loki]] — Système open-source d'agrégation de logs (AGPLv3) inspiré de Prometheus — indexe des labels plutôt que le contenu, stocke des chunks compressés sur object store ; horizontalement scalable, requêté en LogQL et visualisé dans Grafana.
<!-- AUTO:END -->
