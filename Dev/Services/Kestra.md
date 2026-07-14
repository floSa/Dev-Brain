---
galaxie: dev
type: service
nom: Kestra
alias: [kestra]
pitch: "Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches."
categorie: data/orchestration
licence_type: open-source
hosted: both
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[Dev/Services/Airflow|Airflow]]", "[[Dev/Services/Dagster|Dagster]]", "[[Dev/Services/Prefect|Prefect]]", "[[Dev/Services/Mage|Mage]]", "[[Dev/Services/Temporal|Temporal]]"]
remplace_par: []
status: actif
tags: [orchestration, data-pipeline, declarative-config]
url_docs: https://kestra.io/docs
url_repo: https://github.com/kestra-io/kestra
---

# Kestra

## Pourquoi

Kestra est un orchestrateur **déclaratif**. Les workflows s'écrivent en **YAML** (déclencheurs, tâches, dépendances) et s'exécutent sur un moteur **JVM** event-driven, avec éditeur intégré et API. La logique d'orchestration est ainsi **découplée du langage des tâches** : une tâche peut lancer du Python, du SQL, un script shell, un conteneur… Kestra 1.0 (LTS, septembre 2025) en fait une plateforme prête pour l'entreprise.

## Quand l'utiliser

- Orchestration **indépendante du langage** : équipes hétérogènes, pas seulement Python.
- Préférence pour des workflows déclaratifs en YAML, versionnables et lisibles, plutôt que du code.
- Event-driven et planifié, à l'échelle, avec une UI et une API de première classe.
- Besoin d'un moteur robuste sur la JVM, déployable en cluster.

## Quand NE PAS l'utiliser

- Équipe 100 % Python préférant définir les pipelines en code → [[Dev/Services/Airflow|Airflow]], [[Dev/Services/Prefect|Prefect]] ou [[Dev/Services/Dagster|Dagster]].
- Modèle orienté **assets** data et lignage → [[Dev/Services/Dagster|Dagster]].
- Prototypage ELT visuel low-code → [[Dev/Services/Mage|Mage]].

## Déploiement & coût

- Open-source (Apache-2.0), auto-hébergeable : moteur JVM + base de métadonnées + file de messages, déployable en cluster distribué.
- Offres : Kestra Cloud (managé) et Kestra Enterprise Edition (RBAC, SSO, multi-tenant et fonctionnalités entreprise).

## Pièges

- La JVM tranche avec les orchestrateurs Python — autre stack à opérer et monitorer.
- Tout-YAML : la logique complexe peut devenir verbeuse → découper en sous-flows.
- Écosystème plus jeune qu'Airflow, même s'il croît vite.

## Alternatives

- [[Dev/Services/Airflow|Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dev/Services/Dagster|Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Dev/Services/Prefect|Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Dev/Services/Mage|Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Dev/Services/Temporal|Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

## Liens

- [[Comparatif - Orchestrateurs data]] — comparatif de la catégorie
- Doc : https://kestra.io/docs
