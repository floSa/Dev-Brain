---
role: brique
nom: OpenMetadata
alias: [openmetadata, Open Metadata]
pitch: "Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate)."
categorie: data/catalogue
famille: plateforme
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[DataHub]]"]
complements: ["[[OpenLineage]]", "[[Airflow]]", "[[Kafka]]", "[[Postgres]]", "[[MySQL]]", "[[ClickHouse]]", "[[Elasticsearch]]", "[[OpenSearch]]", "[[Kubernetes]]", "[[Keycloak]]", "[[Apache NiFi]]"]
tags: [data-catalog, data-lineage, data-governance, data-quality]
url_docs: https://docs.open-metadata.org/
url_repo: https://github.com/open-metadata/OpenMetadata
---

# OpenMetadata

<!-- AUTO:BANDEAU:START -->
> Catalogue de métadonnées open source : découverte, lignage table et colonne, glossaire, propriétaires, RBAC, tests de qualité et contrats de données sur plus de 130 connecteurs ; un serveur, une base SQL et un moteur de recherche à héberger (Apache-2.0, éditeur commercial Collate).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Java | open-core | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Catalogue de métadonnées open source. Un **serveur** tient un modèle unifié — tables, tableaux de
bord, pipelines, topics, modèles ML, conteneurs — dans une base SQL, l'indexe dans un moteur de
recherche et l'expose par une interface et une API : découverte, glossaire, classification,
propriétaires, lignage table et colonne, tests de qualité, contrats de données. Les métadonnées
arrivent par des **workflows d'ingestion** (collecte tirée, planifiée par Airflow ou, depuis la
1.12, par des Jobs Kubernetes) ; l'API et le SDK servent à pousser.

Relevé le 2026-09-30 : **2.0.3** du 2026-09-30 (la branche 1.13.x reste maintenue : 1.13.6 du
2026-09-11), environ 15 400 étoiles, plus de 130 connecteurs annoncés, dépôt en Apache-2.0.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Un catalogue complet — découverte, lignage colonne, glossaire, RBAC, qualité, contrats — sous Apache-2.0 et sans Kafka | Un simple lignage à alimenter par événements : la spécification suffit ([[OpenLineage]]) et la pile est disproportionnée pour quelques tables |
| Beaucoup de sources hétérogènes à inventorier : bases, tableaux de bord, brokers (Kafka, Redpanda), pipelines | Le lignage arrive surtout par OpenLineage depuis Spark ou Airflow : le connecteur lit Kafka ou Kinesis, il est en bêta et la page l'annonce intégré « jusqu'à la 1.7.0 » ([[DataHub]] expose un point d'entrée HTTP) |
| Un SSO d'entreprise documenté : Keycloak, Okta, Azure, Auth0, LDAP, SAML | Plusieurs méthodes d'authentification en même temps : la documentation dit qu'elles ne sont pas prises en charge |
| Un Kubernetes déjà en place : chart Helm, ingestion en Jobs sans Airflow | Des agents IA, des demandes d'accès ou la rétro-écriture des métadonnées vers les sources : ils sont réservés à Collate |

## Mise en œuvre

- Installation — `docker compose` pour l'essai (6 Gio de mémoire et 4 vCPU au moins, d'après la page de démarrage), chart Helm et guide « on-prem » avec stockage NFS pour la production
- Point d'entrée — l'interface web, l'API et un SDK ; les connecteurs tournent comme workflows d'ingestion planifiés
- Prérequis — MySQL 8.0.42 ou plus, ou PostgreSQL 15 ou plus ; Elasticsearch 9.x ou OpenSearch 3.x ; Java 21 au minimum ; Airflow 2.10.5 pour l'ingestion classique, ou l'orchestrateur Kubernetes natif (Jobs et CronJobs, GA depuis la 1.12). La page des prérequis ne cite pas Kafka
- Exécution — dimensionnement de production indiqué : serveur 4 vCPU et 16 Gio, base 4 vCPU et 16 Gio, moteur de recherche 2 vCPU et 8 Gio par nœud avec un maître et deux workers, Airflow 4 vCPU et 16 Gio
- Coût — gratuit ; l'exploitation est le prix : trois briques à opérer (serveur, base, recherche) plus l'ordonnanceur d'ingestion, avec des versions minimales récentes

## Licence et gouvernance

- **Apache-2.0** : un seul commit touche le fichier `LICENSE` (2021-08-01), aucun changement de licence depuis.
- **Éditeur commercial : Collate**, fondé par les auteurs du projet. D'après sa page de comparaison, seul Collate ajoute : AI Analytics, AI Studio et automatisations, agents IA (documentation, qualité, tier), AI Governance Studio (préversion), *Reverse Metadata* (renvoi des tags, descriptions et propriétaires vers les sources), demandes d'accès aux données, SLA 99,9 % et support 24x7. Le lignage, la qualité et la gouvernance figurent dans les deux colonnes.
- **Ce que la documentation libre ne dit pas** : elle ne dresse aucune liste « Collate seulement » ; le tableau détaillé de la page de comparaison n'est pas lisible sans JavaScript. Le lignage colonne, le RBAC et les contrats de données sont décrits dans la documentation libre, aucune page relevée ne les réserve.
- **Gouvernance** : projet d'une entreprise, sans fondation. Collate a levé 10 M$ en série A (juillet 2025) et a rejoint la Linux Foundation comme membre Silver le 2026-03-26 — une adhésion, pas un transfert du projet.

## Limites à connaître

- **Pile lourde** : serveur, base, moteur de recherche à trois nœuds recommandés, plus l'ordonnanceur d'ingestion ; la 2.0 relève les versions minimales (Elasticsearch 9, OpenSearch 3, PostgreSQL 15).
- **Rupture de la 2.0** : la documentation publie une page « Breaking Changes 1.13 to 2.0 » ; l'image d'ingestion se fixe à la version du serveur, jamais `latest`.
- **OpenLineage en bêta** : le connecteur consomme Kafka ou Kinesis, pas de récepteur HTTP relevé ; fonctions listées : pipelines, lignage, usage — ni statut, ni propriétaires, ni tags.
- **Lignage colonne par analyse SQL** : le *Lineage Agent* le déduit des requêtes, l'édition manuelle complète ; la qualité de l'analyse dépend du dialecte.
- **Une seule authentification à la fois**, et le profileur passe par défaut à l'échantillonnage dynamique en 2.0.

## Écosystème

### Alternatives

- [[DataHub]] — Catalogue de métadonnées open source né chez LinkedIn : lignage table et colonne, glossaire, domaines, propriétaires, contrats de données et politiques d'accès, alimenté par recettes d'ingestion ou par événements ; Kafka, une base SQL et un moteur de recherche à héberger (Apache-2.0, offre commerciale DataHub Cloud). — le même métier de catalogue ; DataHub passe par Kafka et reçoit OpenLineage en HTTP, OpenMetadata n'exige pas Kafka et porte le lignage colonne, le RBAC et les contrats dans l'édition libre.

### Compléments

- [[OpenLineage]] — Spécification ouverte d'événements de lignage — jobs, runs, jeux de données et facettes, dont le lignage colonne — avec des clients Python, Java et Go et des intégrations Spark, Flink, dbt et Airflow ; un standard qu'un catalogue consomme, pas un catalogue (Apache-2.0, LF AI & Data). — le connecteur OpenLineage lit les événements sur Kafka ou Kinesis ; il est en bêta et la page l'annonce intégré jusqu'à la 1.7.0.
- [[Airflow]] — Ordonnanceur de DAGs de référence : tâches définies en Python, planification cron et vaste écosystème de connecteurs ; le standard historique de l'orchestration data. — orchestrateur d'ingestion classique (Airflow 2.10.5 dans les prérequis) ; Airflow figure aussi parmi les connecteurs de pipeline.
- [[Kafka]] — Journal d'événements distribué, partitionné et répliqué : messages conservés et rejouables par offset, groupes de consommateurs, exactly-once de Kafka vers Kafka, Kafka Connect et Kafka Streams livrés ; KRaft sans ZooKeeper depuis la 4.0 (Apache-2.0). — connecteur de messagerie listé (Redpanda aussi) ; sert de transport au connecteur OpenLineage.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — base du serveur (PostgreSQL 15 ou plus) et connecteur de base.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web. — base du serveur (MySQL 8.0.42 ou plus) et connecteur de base.
- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence. — connecteur de base listé.
- [[Elasticsearch]] — Moteur de recherche et d'analytique distribué : indexation full-text et logs à grande échelle. — moteur de recherche obligatoire (9.x, recommandé 9.3.0).
- [[OpenSearch]] — Moteur de recherche et d'analytique distribué (Apache-2.0) — fork d'Elasticsearch 7.10.2 : full-text, k-NN et recherche hybride, visualisé dans OpenSearch Dashboards. — autre moteur de recherche accepté (3.x, recommandé 3.3.0).
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — chart Helm, guide de déploiement sur site et orchestrateur d'ingestion natif (Jobs et CronJobs, GA depuis la 1.12).
- [[Keycloak]] — Fournisseur d'identité complet : OIDC, OAuth 2.0 et SAML 2.0, fédération LDAP et Active Directory, courtage vers d'autres fournisseurs, MFA (TOTP, WebAuthn, passkeys) et plusieurs realms (Apache-2.0, Java sur Quarkus, CNCF incubating) — aucune fonction gardée en édition payante, mais une JVM et une base SQL à exploiter. — SSO listé parmi les fournisseurs de la page de sécurité, avec Okta, Azure, Auth0 et l'OIDC générique.
- [[Apache NiFi]] — Plateforme de flux de données à interface graphique : des centaines de processeurs (fichiers, SFTP, JDBC, MQTT, syslog, Kafka…) reliés par des files avec contre-pression, provenance de chaque donnée et livraison garantie ; Apache-2.0, JVM, sans broker. — connecteur de pipeline listé.

## Ressources

- Documentation — https://docs.open-metadata.org/
- Dépôt — https://github.com/open-metadata/OpenMetadata

## Voir aussi

- [[Data & pipelines]] — le hub du dossier
