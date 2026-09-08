---
role: brique
nom: Dagster
alias: [dagster]
pitch: "Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés."
categorie: data/orchestration
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Airflow]]", "[[Prefect]]", "[[Mage]]", "[[Kestra]]", "[[Temporal]]"]
complements: []
tags: [orchestration, data-pipeline]
url_docs: https://docs.dagster.io/
url_repo: https://github.com/dagster-io/dagster
---

# Dagster

<!-- AUTO:BANDEAU:START -->
> Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-09-03 |
<!-- AUTO:BANDEAU:END -->

## Définition

Orchestrateur **orienté assets**, écrit en Python par Dagster Labs. Plutôt que d'ordonnancer
des tâches opaques, on déclare des **software-defined assets** — les tables, fichiers ou
modèles que le pipeline doit produire — et l'outil en déduit le graphe, le **lignage** et
les rematérialisations à déclencher. Typage, tests de données et catalogue d'assets sont de
première classe, ce qui en fait un outil d'observabilité autant que d'ordonnancement. Les
`ops` et `jobs` impératifs restent disponibles pour les traitements dont l'unité utile n'est
pas une donnée produite. Les concepts ont été renommés plusieurs fois au fil des versions :
une documentation trouvée en ligne peut décrire une API qui n'existe plus.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Plateforme data dont l'unité utile est la **donnée produite** — table, dataset — et son lignage | Venir d'un ordonnanceur de tâches : penser en assets est un vrai changement de modèle mental, pas un changement d'API |
| Tests de données, typage et catalogue d'assets natifs | Traitements purement impératifs : le grain « asset » n'est pas toujours le bon, même si ops et jobs restent là |
| Boucle de développement local soignée et intégration dbt forte | Les concepts ont été renommés au fil des versions — la doc d'une version antérieure induit en erreur |
| Orchestration ELT moderne avec observabilité intégrée | |

## Mise en œuvre

- Installation — `uv add dagster dagster-webserver`
- Point d'entrée — définitions Python (assets, jobs, schedules) exposées à l'UI Dagster et à la CLI `dg`
- Prérequis — Python ; une base de métadonnées et un run launcher pour l'exécution hors du poste
- Exécution — self-hébergé (webserver + daemon + run launchers) ou managé ; distribué sur Kubernetes ou Celery
- Coût — gratuit en Apache-2.0 ; Dagster+ (ex-Dagster Cloud) est payant, à l'usage en crédits

## Écosystème

### Alternatives

- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- [[Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

## Ressources

- Documentation — https://docs.dagster.io/
- Dépôt — https://github.com/dagster-io/dagster

## Voir aussi

- [[Orchestration]] — le hub du dossier
- [[Comparatif - Orchestrateurs data]] — ce qui départage les orchestrateurs du dossier
