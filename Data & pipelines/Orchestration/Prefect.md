---
role: brique
nom: Prefect
alias: [prefect]
pitch: "Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer."
categorie: data/orchestration
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Airflow]]", "[[Dagster]]", "[[Mage]]", "[[Kestra]]", "[[Temporal]]"]
complements: []
tags: [orchestration, data-pipeline]
url_docs: https://docs.prefect.io/
url_repo: https://github.com/PrefectHQ/prefect
---

# Prefect

<!-- AUTO:BANDEAU:START -->
> Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Orchestrateur **Python natif** : les décorateurs `@flow` et `@task` transforment des
fonctions ordinaires en workflows observables, sans DAG statique à déclarer. Le graphe se
construit **à l'exécution**, ce qui rend naturelles les boucles et les branches
conditionnelles dont la forme dépend de la donnée — et interdit, symétriquement, de
visualiser un pipeline avant de l'avoir lancé. Prefect 3.0 (2024) ajoute des sémantiques
transactionnelles avec rollback et réduit fortement la surcharge par tâche de la v2. Point
de vigilance sur la documentation trouvée en ligne : Prefect 1 (« Core ») reposait sur un
DAG déclaré, les patterns d'avant la 2.0 ne s'appliquent plus.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Transformer vite des scripts Python existants en workflows orchestrés, retries et observabilité inclus | Sans DAG statique, on ne visualise pas un pipeline avant de l'exécuter |
| Pipelines **dynamiques** dont le graphe dépend de la donnée ou de la logique au runtime | Refonte majeure entre la v1 et les v2/v3 : la documentation et les patterns antérieurs sont obsolètes |
| Préférence pour du code impératif plutôt qu'un graphe déclaré d'avance | Work pools et workers sont à dimensionner à la main pour tenir la concurrence sous charge |
| Déploiement hybride : workers près de l'infra, plan de contrôle managé | |

## Mise en œuvre

- Installation — `uv add prefect`
- Point d'entrée — décorateurs `@flow` / `@task` sur des fonctions Python, déployés vers des work pools
- Prérequis — Python ; [[Dask]] ou Ray si le parallélisme intra-flow est visé
- Exécution — self-hébergé (serveur Prefect + workers) ou managé, distribué sur les workers rattachés aux pools
- Coût — gratuit en Apache-2.0 ; Prefect Cloud a un palier gratuit, le Pro démarre autour de 100 $/mois

## Écosystème

### Alternatives

- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- [[Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

## Ressources

- Documentation — https://docs.prefect.io/
- Dépôt — https://github.com/PrefectHQ/prefect

## Voir aussi

- [[Orchestration]] — le hub du dossier
- [[Comparatif - Orchestrateurs data]] — ce qui départage les orchestrateurs du dossier
