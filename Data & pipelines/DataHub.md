---
role: brique
nom: DataHub
alias: [datahub, DataHub Core, Acryl DataHub, DataHub Cloud]
pitch: "Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud)."
categorie: data/catalogue
famille: plateforme
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[OpenMetadata]]"]
complements: ["[[OpenLineage]]", "[[Kafka]]", "[[Airflow]]", "[[Great Expectations]]", "[[Spark]]", "[[Postgres]]", "[[MySQL]]", "[[ClickHouse]]", "[[Apache Iceberg]]", "[[Elasticsearch]]", "[[OpenSearch]]", "[[Kubernetes]]", "[[Keycloak]]", "[[Apache NiFi]]"]
tags: [data-catalog, data-lineage, data-governance, data-contract]
url_docs: https://docs.datahub.com/
url_repo: https://github.com/datahub-project/datahub
---

# DataHub

<!-- AUTO:BANDEAU:START -->
> Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-core | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Catalogue de métadonnées open source, publié par LinkedIn puis porté par la société qui s'appelait
Acryl Data et s'appelle aujourd'hui DataHub. Le **service de métadonnées** (GMS) stocke les
entités et leurs aspects dans une base SQL, les indexe dans un moteur de recherche et diffuse
chaque changement sur **Kafka** ; une interface web permet la découverte, le glossaire, les
domaines, les propriétaires et le lignage. Les métadonnées arrivent par des **recettes
d'ingestion** (collecte tirée, en ligne de commande ou planifiée depuis l'interface) ou sont
**poussées** par le SDK Python ou Java, l'API REST ou Kafka.

Relevé le 2026-09-30 : **v1.7.0.1** du 2026-09-03 (la 1.6.0.3, correctif de sécurité de l'ancienne
branche, est sortie plus tard, le 2026-09-25 ; la 1.8.0 est en versions candidates), environ 12 800
étoiles, 140 à 150 connecteurs selon la page, dépôt en Apache-2.0.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un catalogue orienté événements : chaque changement passe par Kafka, les intégrations poussent leur lignage | Aucun Kafka à exploiter ni envie d'en monter un : la doc décrit Kafka dans tous les schémas de déploiement, aucun mode sans lui n'a été trouvé → [[OpenMetadata]] |
| Recevoir du lignage par OpenLineage en HTTP : un point d'entrée `POST /openapi/openlineage/api/v1/lineage` sur GMS | Un déploiement léger : le démarrage rapide lance une quinzaine de conteneurs et demande 8 Gio de mémoire |
| Un lignage colonne, des contrats de données, un glossaire et des politiques d'accès sans licence produit | Des contrôles de fraîcheur, de volume ou de schéma, la propagation de lignage, la documentation générée par IA : ils sont réservés à DataHub Cloud |
| Des intégrations à des outils de données déjà présents : Spark, Airflow, dbt, Great Expectations | Des montées de version sans contrainte : la doc impose de passer par la 1.6.0 avant la 1.7.0.1 |

## Mise en œuvre

- Installation — démarrage rapide en `docker compose` via la CLI Python (Docker Compose v2, Python 3.10+, configuration testée de 2 CPU, 8 Go de mémoire et 13 Go de disque), ou deux charts Helm, `datahub-prerequisites` et `datahub`, sur Kubernetes
- Point d'entrée — l'interface web, l'API GraphQL et REST, la CLI `datahub` et ses recettes YAML
- Prérequis — MySQL, PostgreSQL ou MariaDB ; Elasticsearch 8.x ou OpenSearch 2.x/3.x (Elasticsearch 7 abandonné à la 1.7.0) ; Kafka avec registre de schémas ; l'index de graphe passe par Elasticsearch, Neo4j restant en option. GMS est du Java (Spring), les consommateurs MAE et MCE sont optionnels
- Exécution — quatre composants applicatifs (GMS, frontend, deux consommateurs optionnels) plus les trois dépendances ; aucun dimensionnement de production n'est publié
- Coût — gratuit ; l'exploitation est le prix, avec Kafka en plus de ce que demande [[OpenMetadata]]

## Licence et gouvernance

- **Apache-2.0** (fichier `LICENSE`, copyright LinkedIn) ; aucun changement de licence relevé.
- **Éditeur commercial** : Acryl Data s'est rebaptisé « DataHub » (série B de 35 M$ le 2025-05-22, menée par Bessemer, 65 M$ levés au total selon la presse). L'offre payante s'appelle **DataHub Cloud** ; la page officielle « Core vs Cloud » liste ce qu'elle ajoute : contrôles d'accès fins et *Search Access Controls*, flux de gouvernance (propositions de changement, demandes d'accès, formulaires de conformité), moniteurs de qualité (fraîcheur, volume, schéma, SQL) et détection d'anomalies, propagation de lignage, documentation générée par IA, serveur MCP hébergé, SLA de 99,5 %.
- **Dans Core** : lignage colonne et analyse d'impact, glossaire, propriétaires, contrats de données, gestion d'incidents, et les politiques de plateforme et de métadonnées (rôles Admin, Editor, Reader). Deux pages se contredisent en apparence sur le « contrôle d'accès fin » : le tableau le range côté Cloud, la page des politiques le dit disponible en libre ; seuls le filtrage de recherche par domaine et quelques privilèges (propositions, partage) sont réservés à Cloud.
- **Stratégie** : le dépôt met désormais en avant un agent d'analyse et l'intégration MCP ; les fonctions d'IA et d'observabilité sont côté Cloud. Aucun rachat trouvé.

## Limites à connaître

- **Kafka partout** : il porte les événements de métadonnées (MCE, MAE) ; le retirer n'est pas un mode documenté.
- **Trois lignes de version actives** en septembre 2026 avec de nombreuses versions candidates : lire la note de version avant de monter, le chemin passe par la 1.6.0.
- **OpenLineage par HTTP, avec réserves** : l'endpoint ne porte pas tout le `PathSpec` ; pour Spark et Airflow la doc recommande le plugin DataHub plutôt que le récepteur générique.
- **Connecteurs de maturité inégale** : Apache Iceberg et Flink en bêta, Airbyte et SQLMesh en alpha, d'après la page des intégrations ; Kestra et Debezium n'y figurent pas.
- **SSO** : OIDC par variables `AUTH_OIDC_*` ; la doc cite Okta, Google, Azure AD, Keycloak (ce dernier en lien de référence, sans guide dédié).

## Écosystème

### Alternatives

- [[OpenMetadata]] — Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate). — le même métier de catalogue, sans Kafka obligatoire ; ses fonctions payantes sont surtout l'IA et l'automatisation (Collate), là où DataHub Cloud garde des moniteurs de qualité et des flux de gouvernance.

### Compléments

- [[OpenLineage]] — Spécification ouverte d'événements de lignage — jobs, runs, jeux de données et facettes, dont le lignage colonne — avec des clients Python, Java et Go et des intégrations Spark, Flink, dbt et Airflow ; un standard qu'un catalogue consomme, pas un catalogue (Apache-2.0, LF AI & Data). — point d'entrée `POST /openapi/openlineage/api/v1/lineage` sur GMS ; le plugin Spark de DataHub ajoute PathSpec, lignage colonne et patch à l'écouteur OpenLineage.
- [[Kafka]] — Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0). — obligatoire : bus des événements de métadonnées, avec un registre de schémas déployé par le chart de prérequis.
- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data. — le plugin Airflow de DataHub est recommandé, plutôt que le récepteur OpenLineage, pour un couplage plus fin ; source listée en GA.
- [[Great Expectations]] — Cadre de validation de données en Python : des Expectations groupées en suites, exécutées par des Checkpoints sur des tables SQL, pandas ou Spark, avec rapports HTML Data Docs (GX Core, Apache-2.0) ; dépôt repris par Fivetran en 2026. — source listée en GA sur la page des intégrations.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark. — agent Spark propre à DataHub ; source listée en GA.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — base du serveur (MySQL, PostgreSQL ou MariaDB) et source listée en GA.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web. — base du serveur et source listée en GA.
- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence. — source listée en GA.
- [[Apache Iceberg]] — Format de table ouvert pour le lakehouse : transactions ACID, time travel, évolution de schéma et de partitionnement au-dessus de fichiers Parquet / ORC / Avro sur stockage objet ; lu par tous les moteurs (Spark, Trino, Flink, DuckDB). — source listée, en bêta.
- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle. — moteur de recherche en 8.x ; l'index de graphe s'y appuie aussi, Neo4j restant en option.
- [[OpenSearch]] — Moteur de recherche et d'analytique distribué (Apache-2.0) — fork d'Elasticsearch 7.10.2 : full-text, k-NN et recherche hybride, visualisé dans OpenSearch Dashboards. — autre moteur de recherche accepté (2.x ou 3.x).
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — deux charts Helm, `datahub-prerequisites` et `datahub`.
- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter. — OIDC : la documentation le cite en lien de référence, sans guide dédié.
- [[Apache NiFi]] — Plateforme de flux de données à interface graphique : des centaines de processeurs (fichiers, SFTP, JDBC, MQTT, syslog, Kafka…) reliés par des files avec contre-pression, provenance de chaque donnée et livraison garantie ; Apache-2.0, JVM, sans broker. — source listée en GA.

## Ressources

- Documentation — https://docs.datahub.com/
- Dépôt — https://github.com/datahub-project/datahub

## Voir aussi

- [[Data & pipelines]] — le hub du dossier
