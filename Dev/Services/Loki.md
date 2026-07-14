---
galaxie: dev
type: service
nom: Loki
alias: [loki, "Grafana Loki"]
pitch: "Système open-source d'agrégation de logs (AGPLv3) inspiré de Prometheus — indexe des labels plutôt que le contenu, stocke des chunks compressés sur object store ; horizontalement scalable, requêté en LogQL et visualisé dans Grafana."
categorie: observability/log
licence_type: open-source
hosted: both
maturite: production
langage: Go
scaling: distributed
alternatives: []
remplace_par: []
status: actif
tags: [observability, logging, distributed]
url_docs: https://grafana.com/docs/loki/latest/
url_repo: https://github.com/grafana/loki
---

# Loki

## Pourquoi

Système d'**agrégation de logs** open-source de Grafana Labs (**AGPLv3**, écrit en **Go**), « comme Prometheus, mais pour les logs ». Son parti pris : **n'indexer que des labels** (un jeu d'étiquettes par flux de logs), pas le contenu — ce qui réduit fortement le coût de stockage face à un moteur plein-texte. Les logs sont compressés en **chunks** et déposés sur un **object store** (S3, GCS, ou le filesystem en dev). Multi-tenant, **horizontalement scalable** (architecture microservices : distributor, ingester, querier, query-frontend), requêté en **LogQL** (proche de PromQL) et exploré dans [[Dev/Services/Grafana|Grafana]].

## Quand l'utiliser

- Agréger des logs **à coût maîtrisé** grâce à l'indexation par labels + object store.
- Stack déjà sur **Grafana / Prometheus** : intégration naturelle, LogQL familier.
- Corréler logs et métriques dans un même tableau de bord [[Dev/Services/Grafana|Grafana]].

## Quand NE PAS l'utiliser

- Besoin de **recherche plein-texte** riche ou d'analytics sur le contenu des logs → [[Dev/Services/Elasticsearch|Elasticsearch]] (qui indexe le contenu).
- Logs **non structurés en labels** exploitables : sans labels pertinents, l'avantage de Loki s'effondre et les requêtes deviennent de simples scans.

## Déploiement & coût

- **Self-host** : binaire unique (mode monolithique) ou déploiement microservices distribué ; nécessite un object store. `scaling: distributed` (composants scalables indépendamment).
- **Grafana Cloud Logs** managé (`hosted: both`).
- **AGPLv3** gratuit.

## Pièges

- **Cardinalité des labels** : trop de valeurs distinctes (ex. un ID utilisateur en label) explose l'index et les coûts — modéliser les labels avec parcimonie.
- Pas d'index de contenu : les requêtes **scannent les chunks** (filtrage), peu adapté aux recherches arbitraires massives sur du texte.
- Confort d'exploration **dépendant de Grafana** (ou d'un client LogQL).

## Alternatives

- [[Dev/Services/Elasticsearch|Elasticsearch]] — approche concurrente par **indexation du contenu** (recherche plein-texte puissante, mais plus coûteuse) ; relève de `database/search`, pas de cette catégorie.

## Liens

- [[Dev/Services/Grafana|Grafana]] — visualisation et exploration des logs Loki (LogQL), même éditeur.
- [[Dev/Services/Elasticsearch|Elasticsearch]] — alternative par indexation plein-texte.
- Doc : https://grafana.com/docs/loki/latest/
