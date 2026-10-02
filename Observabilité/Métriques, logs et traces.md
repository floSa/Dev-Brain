---
role: notion
nom: Métriques, logs et traces
alias: [three pillars, trois piliers, télémétrie, telemetry, signaux d'observabilité, métriques logs traces]
categorie: observability/supervision
domaines: [infra-ops, mlops]
tags: [observability, metrics, logging, tracing]
---

# Métriques, logs et traces

## Aperçu

- Trois types de télémétrie aux propriétés différentes : la **métrique** agrège des nombres dans le temps, le **log** enregistre un événement, la **trace** suit une requête à travers les services. Chacun répond à une question que les deux autres posent mal.
- L'**observabilité** est la propriété qui en découle : comprendre un système de l'extérieur, en posant des questions sans connaître son fonctionnement interne (définition de la documentation OpenTelemetry).
- Le découpage « trois piliers » simplifie. OpenTelemetry prend en charge quatre signaux — traces, métriques, logs et *baggage* — et en prépare deux autres, événements et profils, encore en développement ou en proposition.

## Concepts clés

### La métrique
- Une agrégation de données numériques sur une période : taux d'erreur, utilisation du processeur. Peter Bourgon la décrit comme un « atome » qui se compose en une jauge, un compteur ou un histogramme sur une durée.
- Prometheus distingue quatre types : le compteur, qui ne fait que monter (et retombe à zéro au redémarrage d'un processus), la jauge, l'histogramme et le résumé. Règle de la documentation : si la valeur peut baisser, c'est une jauge.
- Le coût suit le **nombre de séries**, pas le trafic : c'est la cardinalité. Une série est un nom de métrique plus une combinaison de valeurs de labels ; ajouter un label à 10 000 valeurs multiplie le nombre de séries par 10 000. Ce qu'en dit la documentation d'instrumentation de Prometheus : garder la cardinalité d'une métrique sous 10, et chercher une autre solution au-delà de 100.
- Ce que la métrique dit bien : **que** quelque chose va mal, à coût constant. Ce qu'elle ne dit pas : pourquoi, ni pour quelle requête.

### Le log
- Un message horodaté émis par un service ; il n'est pas nécessairement lié à une requête (documentation OpenTelemetry). Bourgon le range du côté des événements discrets : messages applicatifs, pistes d'audit.
- Le coût suit le **trafic** : un log par requête donne un volume proportionnel à la charge. Bourgon le note : les logs ont tendance à être accablants en ressources, là où les métriques en demandent le moins.
- [[Loki]] a rendu ce coût supportable en n'indexant que des labels, et pas le contenu des lignes.

### La trace et le span
- Une trace enregistre le chemin d'une requête à travers plusieurs services ; elle se compose de **spans**, organisés en arbre, chacun portant un nom, des durées et des attributs (méthode HTTP, chemin, statut).
- Le modèle vient de Dapper, l'infrastructure de traçage de Google (Sigelman et coll., 2010) : faible surcoût, transparence pour l'application, déploiement partout — obtenus par l'**échantillonnage** et par l'instrumentation des seules bibliothèques courantes.
- Une trace n'a pas de « fin » : interroger un identifiant renvoie les spans déjà reçus pour lui (documentation de [[Tempo]]).
- Ce que la trace dit bien : **où**, dans quel service et à quelle étape, le temps ou l'erreur se sont produits.

### Trois signaux ne sont utiles qu'assemblés
- Bourgon les place dans un diagramme de Venn : les métriques sont définies par l'agrégation, les logs par l'événement discret, les traces par ce qui est borné à une requête. Une partie des métriques et des logs reste orthogonale à toute requête — le cycle de vie d'un processus, par exemple — et n'a pas de place dans une trace.
- L'usage pratique est d'enchaîner : la **métrique** déclenche l'alerte, la **trace** localise le service, le **log** donne la cause. [[Grafana]] rassemble les trois sources sur un même tableau de bord.

## Les maths, simplement

- Nombre de séries d'une métrique = produit du nombre de valeurs de chaque label : $N = \prod_i |V_i|$.
- Exemple : trois labels de 5, 20 et 10 000 valeurs donnent $5 \times 20 \times 10\,000 = 10^6$ séries pour une seule métrique. Le label à 10 000 valeurs, souvent un identifiant d'utilisateur, fait presque tout le coût.
- Les logs et les traces n'ont pas d'équivalent : leur volume dépend du trafic, et l'échantillonnage — garder une requête sur $k$ — divise le coût par $k$ au prix d'un angle mort sur les autres.

## En pratique

- Une règle de la documentation de Prometheus pour ne pas doubler le travail : pour chaque ligne de code qui écrit un log, incrémenter aussi un compteur. Le compteur est bon marché et agrégeable ; le log garde le détail.
- Une chaîne sur site : instrumenter avec [[OpenTelemetry]], stocker les métriques dans [[Prometheus]] ou [[VictoriaMetrics]], les logs dans [[Loki]], les traces dans [[Tempo]], et regarder le tout dans [[Grafana]]. [[Loki]] et [[Tempo]] demandent le même stockage objet ([[Garage]], [[SeaweedFS]] ou [[Ceph]] sur site ; [[MinIO]] est archivé depuis le 2026-04-25).
- Pour les traces, le choix est ouvert. Jaeger v2 est bâti sur le Collector OpenTelemetry, sous Apache-2.0, avec Elasticsearch, OpenSearch, Cassandra ou ClickHouse en stockage ; Jaeger v1 est en fin de vie depuis le 2025-12-31. Tempo demande un stockage objet, s'interroge depuis Grafana, et est sous AGPL-3.0. Les faits relevés ne les départagent pas sur la technique : la décision porte sur le stockage déjà disponible, l'interface et la licence.
- Alerter sur une métrique quand elle suffit : alerter sur des logs quand une métrique le fait aussi bien fait exploser le coût, puisque le log suit le trafic.
- Ne pas confondre cette pile avec le suivi d'un modèle : la dérive de données et la dégradation d'un modèle ne se voient pas dans le processeur — c'est [[Monitoring de modèle en production]].

## Approches voisines & alternatives

- [[SLO et alerting]] — ce qu'on décide à partir des métriques : quel niveau de service, et quand réveiller quelqu'un.
- [[LLM observability]] — la même notion de trace et de span, appliquée aux appels d'un modèle de langage.
- [[Monitoring de modèle en production]] — la dérive d'un modèle, qui ne se lit pas dans les signaux d'infrastructure.
- [[Zabbix]] et [[Netdata]] — des outils de supervision d'hôtes qui rassemblent collecte, stockage et tableau de bord, sans séparer les signaux en trois briques.

## Pour aller plus loin

- OpenTelemetry — *Observability primer*, https://opentelemetry.io/docs/concepts/observability-primer/ (définitions : observabilité, télémétrie, logs, métriques, traces, spans).
- OpenTelemetry — *Signals*, https://opentelemetry.io/docs/concepts/signals/ (signaux pris en charge, événements et profils en développement).
- Peter Bourgon, *Metrics, tracing, and logging*, 21 février 2017, https://peter.bourgon.org/blog/2017/02/21/metrics-tracing-and-logging.html
- Benjamin H. Sigelman, Luiz André Barroso, Mike Burrows, Pat Stephenson, Manoj Plakal, Donald Beaver, Saul Jaspan, Chandan Shanbhag, *Dapper, a Large-Scale Distributed Systems Tracing Infrastructure*, Google, 2010, https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/
- Prometheus — *Instrumentation*, https://prometheus.io/docs/practices/instrumentation/ (types de métriques, cardinalité des labels).
- Google — *Site Reliability Engineering*, chapitre « Monitoring Distributed Systems », https://sre.google/sre-book/monitoring-distributed-systems/ (les quatre signaux d'or : latence, trafic, erreurs, saturation).
