---
role: brique
nom: OpenTelemetry
alias: [opentelemetry, otel, OTLP, OpenTelemetry Collector]
pitch: "Cadre d'observabilité open-source (Apache-2.0, CNCF) neutre vis-à-vis des fournisseurs — spécification, protocole OTLP, SDK, instrumentation automatique et Collector qui reçoit, traite et exporte traces, métriques et logs ; n'est pas un backend."
categorie: observability/supervision
famille: plateforme
licence_type: open-source
hosted: [self]
maturite: production
langage: Go
alternatives: []
complements: ["[[Tempo]]", "[[Prometheus]]"]
tags: [observability, metrics, logging, tracing, self-hosted]
url_docs: https://opentelemetry.io/docs/
url_repo: https://github.com/open-telemetry/opentelemetry-collector
---

# OpenTelemetry

<!-- AUTO:BANDEAU:START -->
> Cadre d'observabilité open-source (Apache-2.0, CNCF) neutre vis-à-vis des fournisseurs — spécification, protocole OTLP, SDK, instrumentation automatique et Collector qui reçoit, traite et exporte traces, métriques et logs ; n'est pas un backend.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Projet de la CNCF né de la fusion d'OpenTracing et d'OpenCensus. Il standardise la **production** et le
**transport** de la télémétrie, et s'interdit d'en être le stockage : la documentation le dit « pas un
backend ». Ses pièces sont une spécification, le protocole **OTLP**, des conventions sémantiques qui
nomment les attributs de la même façon partout, des API et des SDK par langage, une instrumentation
automatique sans modification du code, et le **Collector** — un processus qui reçoit, traite et exporte.
Quatre signaux sont pris en charge : traces, métriques, logs et *baggage* ; les événements et les profils
sont encore en développement ou en proposition. Ce que le cadre achète : instrumenter une fois, puis
changer de backend sans réécrire le code.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Instrumenter une fois et garder le choix du backend, sans dépendance à un fournisseur | Un endroit où stocker et regarder les données : OpenTelemetry ne stocke ni n'affiche → [[Prometheus]], [[Tempo]], [[Loki]], [[Grafana]] |
| Un point unique — le Collector — pour les tentatives, le regroupement, le chiffrement et le filtrage de données sensibles | Un seul service, un seul signal, déjà instrumenté avec la bibliothèque du backend : envoyer directement au backend suffit, la doc le décrit comme le moyen d'obtenir de la valeur vite |
| Traces, métriques et logs sous des conventions communes, corrélables entre eux | Profils ou événements comme fondation de production : signaux encore en développement, d'après la documentation |
| Équipe qui garde la main sur son pipeline de télémétrie, sur site | |

## Mise en œuvre

- Installation — SDK par langage dans le code, ou instrumentation automatique ; Collector en binaire ou en image, avec cinq distributions officielles (core, contrib, Kubernetes, OTLP, profilage eBPF) et le *Collector Builder* (OCB) pour construire la sienne, que la documentation recommande en production
- Point d'entrée — configuration du Collector, en pipelines de récepteurs, de processeurs et d'exporteurs
- Prérequis — un backend par signal ; pour [[Prometheus]], activer explicitement son récepteur OTLP (`--web.enable-otlp-receiver`), désactivé par défaut ; binaire du Collector encore publié en `0.x` (0.162.0, 2026-09-28)
- Exécution — auto-hébergé ; un Collector à côté de chaque service (mode agent) ou une passerelle centrale (mode *gateway*), la documentation recommandant un Collector à côté du service en production
- Coût — gratuit, Apache-2.0 ; le coût réel est le choix et la maintenance des composants du Collector

## Écosystème

### Alternatives

- *Aucune alternative déclarée : les SDK et agents propriétaires des éditeurs jouent le même rôle mais enferment dans un backend, ce qui est précisément ce que le cadre écarte.*

### Compléments

- [[Tempo]] — Backend de traces distribuées open-source (AGPL-3.0, Go) de Grafana Labs — stockage sur object store sans index, accepte OTLP, Jaeger et Zipkin, requêté en TraceQL depuis Grafana ; mode monolithique ou microservices, Grafana Cloud Traces pour le managé. — reçoit les traces en OTLP.
- [[Prometheus]] — Système de supervision et base de séries temporelles open-source (Apache-2.0, Go) — scrape les métriques exposées en HTTP, modèle de données à labels, requêtes PromQL, règles d'alerte transmises à Alertmanager ; stockage local mono-nœud, sans cluster natif. — reçoit les métriques OTLP depuis un récepteur à activer.

## Ressources

- Documentation — https://opentelemetry.io/docs/
- Dépôt — https://github.com/open-telemetry/opentelemetry-collector
- Article — https://opentelemetry.io/docs/concepts/observability-primer/ (définitions : logs, métriques, traces, spans)

## Voir aussi

- [[Observabilité]] — le hub du domaine
- [[Métriques, logs et traces]] — la notion : les trois signaux que le cadre transporte
- [[LLM observability]] — la même instrumentation appliquée aux applications LLM
