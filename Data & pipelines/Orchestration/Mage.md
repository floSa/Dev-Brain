---
role: brique
nom: Mage
alias: [mage, Mage AI, mage-ai]
pitch: "Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation."
categorie: data/orchestration
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: single-node
alternatives: ["[[Airflow]]", "[[Dagster]]", "[[Prefect]]", "[[Kestra]]", "[[Temporal]]"]
complements: []
tags: [orchestration, data-pipeline, low-code]
url_docs: https://docs.mage.ai/
url_repo: https://github.com/mage-ai/mage-ai
---

# Mage

<!-- AUTO:BANDEAU:START -->
> Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Orchestrateur **ELT low-code**. Un pipeline s'assemble par **blocs** — data loader,
transformer, exporter — dans une UI type notebook, chaque bloc restant du vrai code Python,
SQL ou R éditable, avec prévisualisation des données à la sortie de chaque étape. La
promesse est un démarrage rapide sans la charge opérationnelle d'un orchestrateur
distribué. Deux contreparties viennent avec : l'UI par blocs masque des conventions de
structure de projet qu'il faut finir par comprendre, et le développement open-source avance
moins vite depuis le virage vers l'offre managée Mage Pro — la vélocité du dépôt est à
surveiller avant de l'installer pour dix ans.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Démarrer vite un pipeline ELT avec éditeur visuel et prévisualisation de la donnée par bloc | Positionnement mono-nœud par défaut : l'orchestration distribuée mission-critique n'est pas le terrain de l'outil |
| Petite équipe, ou analystes à l'aise en notebook, sans vouloir opérer un cluster | Vélocité de l'open-source en retrait depuis le virage vers l'offre managée Mage Pro |
| Intégration et transformation avec dbt et les connecteurs courants | Catalogue de connecteurs et écosystème nettement plus étroits que ceux du standard de la catégorie |
| | L'UI par blocs masque une structure de projet générée qu'il faut de toute façon apprendre |

## Mise en œuvre

- Installation — `uv add mage-ai`, ou image Docker pour la pile complète
- Point d'entrée — UI web par blocs (loader / transformer / exporter), chaque bloc étant du code Python, SQL ou R
- Prérequis — Python ; Kubernetes et ses executors si l'on veut répartir les tâches
- Exécution — self-hébergé en application unique avec scheduler intégré, mono-nœud par défaut, ou managé
- Coût — gratuit en Apache-2.0 ; Mage Pro (RBAC, multi-environnements, monitoring, assistance IA) est payant

## Écosystème

### Alternatives

- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.
- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- [[Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

## Ressources

- Documentation — https://docs.mage.ai/
- Dépôt — https://github.com/mage-ai/mage-ai

## Voir aussi

- [[Orchestration]] — le hub du dossier
- [[Comparatif - Orchestrateurs data]] — ce qui départage les orchestrateurs du dossier
