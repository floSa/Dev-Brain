---
role: comparatif
nom: Comparatif - Catalogues et lignage de données
categorie: data/catalogue
tags: [data-catalog, data-lineage]
---

# Comparatif - Catalogues et lignage de données

> On tranche sur : le rôle (catalogue complet ou spécification de lignage), le niveau de lignage (table ou colonne) et sa collecte, la gouvernance et les droits que l'édition libre contient, l'empreinte à héberger sur site, et la licence — dont deux sont open-core, avec les fonctions payantes nommées.

![[Comparatif - Catalogues et lignage de données.base]]

## Ce qui départage

- [[OpenMetadata]] — le **catalogue sans Kafka** : découverte, lignage table et colonne, glossaire, RBAC, tests de qualité et contrats de données dans l'édition libre (Apache-2.0), collecte tirée par workflows d'ingestion. Le prix : trois briques obligatoires (base SQL, Elasticsearch 9 ou OpenSearch 3, orchestrateur d'ingestion Airflow ou Jobs Kubernetes), des versions minimales récentes, un connecteur OpenLineage en bêta qui lit Kafka ou Kinesis, et l'IA, les demandes d'accès et la rétro-écriture réservées à Collate.
- [[DataHub]] — le **catalogue par événements** : lignage colonne, glossaire, contrats, politiques d'accès et récepteur OpenLineage en HTTP dans l'édition libre (Apache-2.0), collecte tirée par recettes ou poussée par SDK et Kafka. Le prix : Kafka, une base SQL et un moteur de recherche obligatoires (une quinzaine de conteneurs au démarrage rapide), et des moniteurs de qualité, des flux de gouvernance, la propagation de lignage et l'IA réservés à DataHub Cloud.
- [[OpenLineage]] — la **spécification**, pas un catalogue : des événements émis par Spark, Flink, dbt et Airflow, un graphe qu'un récepteur reconstruit. Le prix : rien à consulter par soi-même, un lignage colonne émis par peu d'intégrations, Dagster communautaire, Prefect et Kestra absents de la liste d'intégrations. Complète les deux autres, ne les remplace pas.

**Critère par critère**

**Rôle.** [[OpenMetadata]] et [[DataHub]] : catalogues, avec glossaire, propriétaires, recherche et interface. [[OpenLineage]] : spécification et clients (Python, Java, Go), sans stockage ni interface ; le récepteur reste à choisir.

**Lignage.** [[OpenMetadata]] : table et colonne dans l'édition libre ; le colonne vient du *Lineage Agent*, qui analyse le SQL, ou d'une saisie manuelle. [[DataHub]] : table et colonne dans Core, par dbt, Airflow, Spark, analyse SQL ou saisie. [[OpenLineage]] : la facette `ColumnLineageDatasetFacet` (dépendances directes et indirectes) décrit le colonne, mais Spark et dbt sont les émetteurs documentés.

**Collecte.** [[OpenMetadata]] : tirée, par workflows planifiés ; l'API pousse aussi. [[DataHub]] : tirée par recettes, poussée par SDK Python ou Java, REST et Kafka. [[OpenLineage]] : poussée uniquement, au moment de l'exécution. Le principe est dans [[Catalogue de données et lignage]].

**Réception d'OpenLineage.** [[DataHub]] : un point d'entrée HTTP (`POST /openapi/openlineage/api/v1/lineage`) sur le service de métadonnées, avec des plugins Airflow et Spark propres pour les cas fins. [[OpenMetadata]] : un connecteur qui lit les événements sur Kafka ou Kinesis, en bêta, annoncé intégré jusqu'à OpenLineage 1.7.0.

**Gouvernance et droits.** [[OpenMetadata]] : rôles et politiques, SSO Google, Okta, Azure, Auth0, Keycloak, LDAP, SAML — une méthode à la fois. [[DataHub]] : politiques de plateforme et de métadonnées avec les rôles Admin, Editor, Reader en libre ; le filtrage de recherche par domaine et les propositions de changement sont Cloud ; OIDC par variables d'environnement. [[OpenLineage]] : sans objet.

**Empreinte sur site.** [[OpenMetadata]] : serveur, MySQL 8.0.42+ ou PostgreSQL 15+, Elasticsearch 9 ou OpenSearch 3 (un maître et deux workers recommandés), Airflow 2.10.5 ou Jobs Kubernetes ; 6 Gio et 4 vCPU pour l'essai. [[DataHub]] : GMS, frontend, MySQL, PostgreSQL ou MariaDB, Elasticsearch 8 ou OpenSearch, Kafka avec registre de schémas ; 8 Gio et 2 CPU pour l'essai, aucun dimensionnement de production publié. [[OpenLineage]] : une bibliothèque dans chaque outil émetteur, rien à héberger.

**Licence.** Les trois dépôts sont sous Apache-2.0. [[OpenMetadata]] : open-core, l'éditeur Collate vend l'IA, les demandes d'accès, la rétro-écriture, un SLA et un support. [[DataHub]] : open-core, DataHub Cloud (l'ancien Acryl) vend les moniteurs, les flux de gouvernance, l'IA et un SLA. [[OpenLineage]] : aucune édition payante ; les fonctions commerciales sont chez les récepteurs.

**Pas de fiche ici**, faute d'être éprouvé ou faute d'apporter un choix de plus :

- **Marquez** — le récepteur de lignage du projet OpenLineage (LF AI & Data, Graduated, Apache-2.0). Relevé le 2026-09-30 : dernière version taguée 0.51.1 du 2025-03-27, dernière GitHub Release 0.50.0 du 2024-10-24, environ 2 280 étoiles, cinq commits en douze mois dont les deux derniers montent React. Pile légère (Java, PostgreSQL), mais sans glossaire ni droits relevés : dormant, écarté.
- **Amundsen** — **archivé** : l'avis en tête du README parle d'inactivité et de septembre 2026 ; aucune version depuis 2024-08 ; environ 4 780 étoiles. Écarté.
- **Apache Atlas** — maintenu (Apache-2.0, 2.5.0 publié en avril 2026, 2.6.0 en versions candidates, commits jusqu'au 2026-09-29, presque tous co-signés par des adresses Cloudera), mais son README le décrit comme des services de gouvernance « dans Hadoop », avec des crochets pour Hive, Kafka et HBase. Sans Hadoop, il n'apporte pas grand-chose ; la documentation de Dagster le cite parmi les récepteurs OpenLineage. Écarté pour un client sans Hadoop.
- **Autres projets vus, non évalués sur le fond** (seule leur activité a été relevée le 2026-09-30) : Apache Gravitino (Apache-2.0, projet de premier niveau de l'ASF, v1.3.1), Unity Catalog OSS (Apache-2.0, bac à sable LF AI & Data, 0.6.0), Egeria (Apache-2.0, Graduated, V6.1), Open Data Discovery (Apache-2.0, 0.29.0), Netflix Metacat (Apache-2.0, versions candidates). À creuser si un besoin précis l'appelle.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
- [[Data & pipelines]] — le hub du dossier.
- [[Catalogue de données et lignage]] — les principes : catalogue contre lignage contre glossaire, collecte tirée ou poussée.
- [[Contrats de données & qualité]] — ce qu'un catalogue affiche sans le produire.
- [[Comparatif - Qualité de données]] — les outils qui produisent les résultats de test qu'un catalogue affiche.
- [[Comparatif - Orchestrateurs data]] — les outils qui émettent les événements de lignage.
