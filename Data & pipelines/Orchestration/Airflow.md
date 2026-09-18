---
role: brique
nom: Airflow
alias: [airflow, Apache Airflow]
pitch: "Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data."
categorie: data/orchestration
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Dagster]]", "[[Prefect]]", "[[Mage]]", "[[Kestra]]", "[[Temporal]]"]
complements: ["[[Keycloak]]", "[[Authentik]]", "[[dbt Core]]", "[[Great Expectations]]"]
tags: [orchestration, data-pipeline, scheduler]
url_docs: https://airflow.apache.org/docs/
url_repo: https://github.com/apache/airflow
---

# Airflow

<!-- AUTO:BANDEAU:START -->
> Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Python | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-08-29 |
<!-- AUTO:BANDEAU:END -->

## Définition

Ordonnanceur de workflows de l'Apache Software Foundation. Un pipeline s'écrit comme un
**DAG** de tâches en Python ; un scheduler en planifie l'exécution — cron ou intervalle —
et gère dépendances, reprises et back-fills. Sa force est le catalogue d'**operators /
providers**, plusieurs centaines de connecteurs vers les bases, les clouds et les outils
data. Deux comportements structurent l'écriture des DAGs : la `logical_date`
(ex-`execution_date`) désigne le **début de l'intervalle**, pas l'instant d'exécution, et
le fichier du DAG est ré-importé à chaque parse, donc le code au niveau module doit rester
léger. Airflow 3.0 (GA avril 2025) sépare client et serveur via une Task Execution API et
ajoute l'Edge Executor pour l'exécution distante.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Pipelines batch planifiés — ETL/ELT, entraînements, rapports — avec dépendances complexes | Orchestrer un traitement de flux continu : Airflow planifie des lots, il n'exécute pas de streaming → [[Flink]] |
| Le plus large catalogue de connecteurs prêts à l'emploi de la catégorie | Plusieurs composants à opérer soi-même — scheduler, webserver, workers, broker, base de métadonnées : le self-host est lourd |
| Écosystème mûr et compétences répandues : c'est le standard de fait | XCom transporte des métadonnées, pas du volume — le passage de données entre tâches doit passer par un stockage externe |
| Exécution distribuée via CeleryExecutor, KubernetesExecutor ou Edge Executor | Existant en 2.x : la migration vers 3.0 change l'architecture et l'API, elle n'est pas triviale |

## Mise en œuvre

- Installation — `uv add apache-airflow`, ou image Docker / chart Helm pour un déploiement complet
- Point d'entrée — DAGs Python déposés dans le dossier de DAGs, pilotés par le webserver et l'API
- Prérequis — une base de métadonnées ([[Postgres]] recommandé) et, en CeleryExecutor, un broker de messages
- Exécution — self-hébergé (scheduler + webserver + workers) ou managé ; distribué via Celery, Kubernetes ou Edge Executor
- Coût — gratuit en Apache-2.0 ; les offres managées Amazon MWAA, Google Cloud Composer et Astronomer sont payantes

## Écosystème

### Alternatives

- [[Dagster]] — Orchestrateur orienté assets : on déclare les données à produire (software-defined assets) et non que les tâches ; lignage, typage et tests de données intégrés.
- [[Prefect]] — Orchestrateur Python natif : des décorateurs transforment fonctions en flows et tasks ; workflows dynamiques et résilients, sans DAG statique à déclarer.
- [[Mage]] — Orchestrateur ELT hybride low-code : pipelines assemblés par blocs dans une UI type notebook, de l'ingestion à la transformation.
- [[Kestra]] — Orchestrateur déclaratif : workflows en YAML, moteur JVM event-driven ; la logique d'orchestration est découplée du langage des tâches.
- [[Temporal]] — Moteur de workflows durables : le code applicatif (Go, Java, Python, TypeScript…) s'exécute de façon résiliente, l'état est persisté à chaque étape et reprend automatiquement après panne, retry ou redémarrage.

### Compléments

- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter. — fournisseur `keycloak` de la liste OAuth du provider FAB, et un *auth manager* Keycloak déclaré alpha.
- [[Authentik]] — Fournisseur d'identité à flux configurables : OIDC, SAML, LDAP, SCIM, RADIUS et proxy avec forward auth pour Traefik, Caddy et Nginx, sur PostgreSQL seul (MIT, Python, Authentik Security) — audit renforcé, PAM, mTLS et synchronisation Entra ou Google sont réservés à l'édition Enterprise, 5 $ par utilisateur et par mois. — fournisseur `authentik` de la liste OAuth du provider FAB.
- [[dbt Core]] — Transformation SQL par modèles versionnés : un SELECT par fichier, graphe déduit des ref(), tests, snapshots et matérialisations (vue, table, incrémental) exécutés dans le moteur ; v1 en Python (Apache-2.0), v2 réécrite en Rust (code Apache-2.0, distribution complète sous licence produit). — le paquet distinct `astronomer-cosmos` (Apache-2.0, 1.15.1 du 2026-08-04) rend un projet dbt en DAG ou en groupe de tâches Airflow, une tâche par modèle, avec reprises et tests lancés juste après chaque modèle ; Airflow 2.9 à 3.3 et dbt Core 1.8 à 1.12 d'après la politique de compatibilité de la branche principale.
- [[Great Expectations]] — Cadre de validation de données en Python : des Expectations groupées en suites, exécutées par des Checkpoints sur des tables SQL, pandas ou Spark, avec rapports HTML Data Docs (GX Core, Apache-2.0) ; dépôt repris par Fivetran en 2026. — provider officiel `airflow-provider-great-expectations` (1.0.0, 2026-01-28, Apache-2.0, maintenu par Astronomer avec GX) : trois opérateurs, pour un DataFrame pandas ou Spark en mémoire, pour des données externes par une Batch Definition, et pour un Checkpoint.

## Ressources

- Documentation — https://airflow.apache.org/docs/
- Dépôt — https://github.com/apache/airflow

## Voir aussi

- [[Orchestration]] — le hub du dossier
- [[Comparatif - Orchestrateurs data]] — ce qui départage les orchestrateurs du dossier
