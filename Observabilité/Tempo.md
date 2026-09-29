---
role: brique
nom: Tempo
alias: [tempo, "Grafana Tempo"]
pitch: "Backend de traces distribuées open-source (AGPL-3.0, Go) de Grafana Labs — stockage sur object store sans index, accepte OTLP, Jaeger et Zipkin, requêté en TraceQL depuis Grafana ; mode monolithique ou microservices, Grafana Cloud Traces pour le managé."
categorie: observability/supervision
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: []
complements: ["[[Grafana]]", "[[Loki]]", "[[OpenTelemetry]]"]
tags: [observability, tracing, self-hosted]
url_docs: https://grafana.com/docs/tempo/latest/
url_repo: https://github.com/grafana/tempo
---

# Tempo

<!-- AUTO:BANDEAU:START -->
> Backend de traces distribuées open-source (AGPL-3.0, Go) de Grafana Labs — stockage sur object store sans index, accepte OTLP, Jaeger et Zipkin, requêté en TraceQL depuis Grafana ; mode monolithique ou microservices, Grafana Cloud Traces pour le managé.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Backend de traces distribuées de Grafana Labs, conçu dans le même esprit que [[Loki]] : ne pas indexer
pour payer moins. Les traces ne sont **pas indexées** — la page produit avance qu'on peut ainsi en garder « des
ordres de grandeur » de plus pour le même prix — et sont écrites en blocs Apache Parquet, un format
colonnaire, sur un stockage objet, seule dépendance de la pile. Il accepte les protocoles OTLP, Jaeger,
Zipkin et Kafka. Les traces se cherchent en **TraceQL**, un langage inspiré de LogQL et de PromQL, depuis
[[Grafana]]. Un composant, le *metrics-generator*, dérive des métriques RED et des cartes de dépendances
entre services à partir des traces. Une trace n'a pas de « fin » : interroger un identifiant renvoie les
*spans* déjà reçus pour lui.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Garder beaucoup de traces à faible coût, sans base à indexer : un stockage objet suffit | Aucun stockage objet à opérer en production : le backend `local` est réservé au développement et aux tests, et ne retrouve pas correctement les traces en déploiement distribué sans disque commun |
| Déjà [[Grafana]] et [[Loki]] : même interface, mêmes habitudes de requête, TraceQL calqué sur LogQL et PromQL | Traçage sans Grafana : Jaeger v2 (Apache-2.0, bâti sur le Collector OpenTelemetry) accepte Elasticsearch, OpenSearch, Cassandra ou ClickHouse comme stockage |
| Réutiliser des émetteurs existants : OTLP, Jaeger et Zipkin sont acceptés en entrée | Copyleft réseau à éviter : AGPL-3.0-only, avec des exceptions Apache-2.0 documentées dans `LICENSING.md` ; à faire qualifier avant de l'embarquer dans un produit livré à un client |
| Métriques RED et cartes de services tirées des traces par le *metrics-generator* | |

## Mise en œuvre

- Installation — mode monolithique : un processus, aucun Kafka requis ; mode microservices, qui exige en production un système compatible Kafka ; Grafana Cloud Traces pour l'offre managée
- Point d'entrée — ingestion OTLP, Jaeger, Zipkin ou Kafka ; requêtes TraceQL depuis [[Grafana]]
- Prérequis — un stockage objet, sur site compatible S3 avec [[MinIO]] (projet archivé, voir sa fiche), [[Garage]] ou [[Ceph]] — celui-là même que demande [[Loki]] ; des services instrumentés, par exemple par [[OpenTelemetry]] ; durée de rétention à fixer explicitement, la documentation d'architecture n'en donne pas de défaut
- Exécution — auto-hébergé ou managé ; monolithique pour commencer, microservices pour monter en charge
- Coût — gratuit, AGPL-3.0-only ; le poste de dépense est le stockage objet ; Grafana Cloud Traces propose des paliers gratuit et payant

## Écosystème

### Alternatives

- *Aucune alternative déclarée : le voisin fonctionnel, Jaeger, n'a pas de fiche dans le brain — Jaeger v1 est en fin de vie depuis le 2025-12-31, et Jaeger v2 est décrit dans le tableau ci-dessus. Tempo est retenu ici pour son prérequis commun avec Loki et son interface commune avec Grafana.*

### Compléments

- [[Grafana]] — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud. — l'interface de requête des traces, en TraceQL.
- [[Loki]] — Système open-source d'agrégation de logs (AGPLv3) inspiré de Prometheus — indexe des labels plutôt que le contenu, stocke des chunks compressés sur object store ; horizontalement scalable, requêté en LogQL et visualisé dans Grafana. — même stockage objet, mêmes habitudes ; les logs se lisent à côté des traces.
- [[OpenTelemetry]] — Cadre d'observabilité open-source (Apache-2.0, CNCF) neutre vis-à-vis des fournisseurs — spécification, protocole OTLP, SDK, instrumentation automatique et Collector qui reçoit, traite et exporte traces, métriques et logs ; n'est pas un backend. — l'instrumentation qui produit les traces reçues en OTLP.

## Ressources

- Documentation — https://grafana.com/docs/tempo/latest/
- Dépôt — https://github.com/grafana/tempo
- Article — https://grafana.com/oss/tempo/ (présentation : stockage objet, TraceQL, Cloud Traces)

## Voir aussi

- [[Observabilité]] — le hub du domaine
- [[Métriques, logs et traces]] — la notion : ce que la trace apporte que la métrique et le log ne disent pas
- [[Journalisation structurée et traçabilité]] — la notion : événements structurés, contexte, corrélation avec les traces, ce qu'il ne faut pas journaliser
