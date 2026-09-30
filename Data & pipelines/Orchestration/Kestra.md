---
role: brique
nom: Kestra
alias: [kestra]
pitch: "Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches."
categorie: data/orchestration
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Airflow]]", "[[Dagster]]", "[[Prefect]]", "[[Mage]]", "[[Temporal]]"]
complements: ["[[dbt Core]]", "[[SQLMesh]]", "[[Airbyte]]", "[[dlt]]"]
tags: [orchestration, data-pipeline, declarative-config]
url_docs: https://kestra.io/docs
url_repo: https://github.com/kestra-io/kestra
---

# Kestra

<!-- AUTO:BANDEAU:START -->
> Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-09-07 |
<!-- AUTO:BANDEAU:END -->

## Définition

Orchestrateur **déclaratif** : les workflows — déclencheurs, tâches, dépendances —
s'écrivent en **YAML** et s'exécutent sur un moteur **JVM** event-driven, avec éditeur
intégré et API. La conséquence est le trait qui le distingue : la logique d'orchestration
est **découplée du langage des tâches**, une tâche pouvant lancer du Python, du SQL, un
script shell ou un conteneur. L'équipe n'a donc pas à être Python pour écrire des
pipelines. Le prix est une autre pile à opérer et à monitorer, et un YAML qui devient
verbeux dès que la logique se complique — le remède est le découpage en sous-flows.
Kestra 1.0 (LTS, septembre 2025) en fait une plateforme d'entreprise.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Équipes hétérogènes : orchestration **indépendante du langage** des tâches | Une pile JVM de plus à opérer et à monitorer, là où la catégorie est majoritairement Python |
| Workflows déclaratifs, versionnables et lisibles, plutôt que du code | Le tout-YAML devient verbeux sur une logique complexe — il faut découper en sous-flows |
| Event-driven et planifié à l'échelle, avec UI et API de première classe | Écosystème plus jeune que celui du standard historique, même s'il croît vite |
| Moteur robuste sur la JVM, déployable en cluster | |

## Mise en œuvre

- Installation — image Docker ou JAR autonome ; `docker compose` pour la pile complète
- Point d'entrée — fichiers de flow YAML, éditables dans l'UI intégrée ou poussés par l'API
- Prérequis — une JVM, une base de métadonnées et une file de messages pour le mode cluster
- Exécution — self-hébergé, mono-nœud ou distribué en cluster, ou managé
- Coût — gratuit en Apache-2.0 ; Kestra Cloud et l'Enterprise Edition (RBAC, SSO, multi-tenant) sont payantes

## Écosystème

### Alternatives

- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

### Compléments

- [[dbt Core]] — Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit). — le plugin dbt de Kestra (Apache-2.0) lance n'importe quelle commande dbt dans un conteneur par la tâche `DbtCLI` et parse les résultats ; il sait aussi déclencher un job dbt Cloud.
- [[SQLMesh]] — Framework de transformation SQL à environnements virtuels : plan/apply sur des modèles versionnés, lignage au niveau colonne, exécution incrémentale par intervalles suivis et audits (Apache-2.0, Python) ; sous gouvernance Linux Foundation depuis mars 2026 après le rachat de Tobiko par Fivetran. — Kestra figure dans la liste officielle des intégrations de SQLMesh, avec un plugin dédié ; l'intégration Airflow documentée, elle, exige Tobiko Cloud.
- [[Airbyte]] — Plateforme d'ingestion par catalogue de connecteurs : sources API, bases et fichiers vers entrepôts et lacs, synchronisations full refresh ou incrémentales (curseur ou CDC), interface, API et Connector Builder ; Elastic License 2.0 (source-available), déploiement Kubernetes. — Kestra publie un plugin Airbyte pour déclencher des synchronisations.
- [[dlt]] — Bibliothèque Python d'ingestion : des générateurs Python deviennent des tables typées chargées dans DuckDB, Postgres, ClickHouse ou des fichiers, avec schéma inféré, état et curseurs incrémentaux stockés dans la destination, sans serveur (Apache-2.0). — Kestra publie un plugin dlt.

## Ressources

- Documentation — https://kestra.io/docs
- Dépôt — https://github.com/kestra-io/kestra

## Voir aussi

- [[Orchestration]] — le hub du dossier
- [[Comparatif - Orchestrateurs data]] — ce qui départage les orchestrateurs du dossier
