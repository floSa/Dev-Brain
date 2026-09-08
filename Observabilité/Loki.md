---
role: brique
nom: Loki
alias: [loki, "Grafana Loki"]
pitch: "Système open-source d'agrégation de logs (AGPLv3) inspiré de Prometheus — indexe des labels plutôt que le contenu, stocke des chunks compressés sur object store ; horizontalement scalable, requêté en LogQL et visualisé dans Grafana."
categorie: observability/supervision
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: []
complements: ["[[Grafana]]"]
tags: [observability, logging, distributed]
url_docs: https://grafana.com/docs/loki/latest/
url_repo: https://github.com/grafana/loki
---

# Loki

<!-- AUTO:BANDEAU:START -->
> Système open-source d'agrégation de logs (AGPLv3) inspiré de Prometheus — indexe des labels plutôt que le contenu, stocke des chunks compressés sur object store ; horizontalement scalable, requêté en LogQL et visualisé dans Grafana.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-08-27 |
<!-- AUTO:BANDEAU:END -->

## Définition

Système d'agrégation de logs de Grafana Labs — « comme Prometheus, mais pour les logs ».
Son parti pris tient en une phrase : **n'indexer que des labels**, un jeu d'étiquettes
par flux de logs, et jamais le contenu, ce qui effondre le coût de stockage face à un
moteur plein-texte. Les lignes sont compressées en *chunks* déposés sur un object store,
et l'architecture est découpée en composants — distributor, ingester, querier,
query-frontend — dimensionnables séparément, multi-tenant. Les requêtes s'écrivent en
**LogQL**, proche de PromQL. La conséquence directe du modèle est le seul vrai paramètre
de conception : la **cardinalité des labels**. Un identifiant utilisateur posé en label
fait exploser l'index et la facture ; les labels se modélisent avec parcimonie.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Agréger des logs à coût maîtrisé, par indexation de labels et stockage objet | Recherche plein-texte riche, ou analytique sur le contenu des lignes → [[Elasticsearch]], qui indexe le contenu |
| Stack déjà sur Grafana et Prometheus : intégration native, LogQL déjà familier | Logs sans labels discriminants : l'avantage s'effondre et toute requête redevient un scan de chunks |
| Corréler logs et métriques dans un même tableau de bord | Recherches arbitraires et massives sur du texte : il n'y a pas d'index de contenu à interroger |
| Monter en charge par composant : distributor, ingester et querier se dimensionnent séparément | Exploration hors Grafana ou d'un client LogQL : le confort de requêtage en dépend entièrement |

## Mise en œuvre

- Installation — binaire unique en mode monolithique, ou déploiement par composants (Helm) pour le mode distribué ; Grafana Cloud Logs pour l'offre managée
- Point d'entrée — API HTTP d'ingestion et de requêtage ; LogQL depuis un tableau de bord ou `logcli`
- Prérequis — un object store (S3, GCS, Azure Blob) ; le filesystem ne convient qu'en développement
- Exécution — auto-hébergé ou managé ; composants scalables indépendamment les uns des autres
- Coût — gratuit, AGPL-3.0 ; Grafana Cloud Logs facturé à l'usage

## Écosystème

### Alternatives

- *Aucune alternative déclarée : le voisin fonctionnel, Elasticsearch, relève de `database/recherche` et non de cette catégorie — il est pointé dans le tableau ci-dessus.*

### Compléments

- [[Grafana]] — Plateforme open-source de dashboards et d'observabilité (AGPL-3.0) — visualise métriques, logs et traces depuis 150+ sources (Prometheus, Loki, InfluxDB, Postgres…) ; alerting intégré, self-host ou Grafana Cloud. — même éditeur, et l'interface de requêtage LogQL de fait

## Ressources

- Documentation — https://grafana.com/docs/loki/latest/
- Dépôt — https://github.com/grafana/loki

## Voir aussi

- [[Observabilité]] — le hub du domaine
