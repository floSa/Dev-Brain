---
role: brique
nom: lakeFS
alias: [lakefs, lakeFS Community]
pitch: "Versionnage d'un dépôt d'objets à la manière de Git — branches, commits, merges atomiques, retour en arrière, hooks — au-dessus d'un stockage S3-compatible, sans copier les données ; serveur Go avec PostgreSQL, sous licence BSL 1.1 depuis la v1.87.0 (usage interne non modifié), édition libre limitée à un utilisateur."
categorie: data/fiabilite
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[DVC]]"]
complements: ["[[MinIO]]", "[[Ceph]]", "[[Postgres]]", "[[Spark]]", "[[Delta Lake]]", "[[MLflow]]", "[[Kubernetes]]"]
tags: [data-versioning, reproducibility, object-storage, s3-compatible, self-hosted]
url_docs: https://docs.lakefs.io
url_repo: https://github.com/treeverse/lakeFS
---

# lakeFS

<!-- AUTO:BANDEAU:START -->
> Versionnage d'un dépôt d'objets à la manière de Git — branches, commits, merges atomiques, retour en arrière, hooks — au-dessus d'un stockage S3-compatible, sans copier les données ; serveur Go avec PostgreSQL, sous licence BSL 1.1 depuis la v1.87.0 (usage interne non modifié), édition libre limitée à un utilisateur.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | source-available | self-hébergé ou managé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Couche de versionnage **au-dessus d'un stockage objet**. Un serveur sans état tient, dans une base, les
métadonnées d'un dépôt : les objets eux-mêmes restent dans le bucket, et un commit ne copie rien. Le
modèle est celui de Git — **branches**, commits, tags, merges, retour en arrière — appliqué à un dépôt de
fichiers et non à du texte. Il s'atteint par une API REST, par une **passerelle S3** (les outils existants
lisent `s3://dépôt/branche/chemin` sans changement), par `lakectl`, par des SDK Python et un client
Hadoop pour Spark. Des **hooks** (webhooks, scripts Lua embarqués, Airflow) s'exécutent avant un commit
ou un merge, donc une branche de transformation se valide avant d'être fusionnée en production. Pour
reproduire un entraînement : un commit ou un tag désigne l'état exact du jeu, et la lecture passe par
`s3://dépôt/<identifiant-du-commit>/chemin`. Pas de tables : les fichiers Delta, Iceberg ou Parquet y sont
stockés tels quels.

Relevé le 2026-09-30 : **v1.87.0** du 2026-09-22, dernier commit sur `master` le 2026-09-24, environ
5 500 étoiles, Go. **La licence a changé avec cette version** (voir plus bas).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des branches de données : tester une transformation sur une copie sans duplication, puis fusionner atomiquement ou abandonner | **Un fournisseur ou une ESN qui hébergerait lakeFS pour des clients** : la licence BSL n'autorise la production que pour un usage interne, sans aucun accès donné à un tiers |
| Un dépôt d'objets volumineux — images, documents, fichiers Parquet — que des outils S3 déjà en place doivent continuer à lire | Plus d'un utilisateur dans l'édition libre : elle n'en compte qu'un, l'administrateur ; rôles, groupes et SSO sont payants |
| Reproduire un entraînement à partir d'un état daté sans dépendre de Git ni de la taille des fichiers | Un projet sans stockage objet ni base à exploiter : il faut un stockage S3-compatible **et** PostgreSQL → [[DVC]], qui n'exige que Git et un dossier |
| Un stockage sur site déjà S3-compatible, avec PostgreSQL 11 ou plus à côté | Un besoin de tables versionnées interrogées en SQL → le time travel d'un format de table, [[Delta Lake]] ou [[Apache Iceberg]] |
| | Un environnement qui exige une licence reconnue comme open source : la BSL 1.1 n'en est pas une, et seules les versions jusqu'à la v1.86.0 sont en Apache-2.0 |

## Mise en œuvre

- Installation — binaire, image Docker ou chart Helm (`helm repo add lakefs https://charts.lakefs.io`) ; essai local par `pip install lakefs` puis `python -m lakefs.quickstart`
- Point d'entrée — l'API REST et la passerelle S3 ; `lakectl` en ligne de commande ; SDK Python `lakefs`
- Prérequis — un stockage S3-compatible (`blockstore.type: s3`, avec `force_path_style: true` pour MinIO et `discover_bucket_region: false` si le stockage n'implémente pas la découverte de région) et PostgreSQL 11 ou plus pour la production sur site ; la documentation d'architecture cite MinIO, Ceph et NetApp StorageGRID, et **ne cite ni SeaweedFS ni Garage**
- Exécution — serveur sans état, plusieurs instances derrière un équilibreur ; 512 Mo de mémoire et un CPU au minimum, environ 150 Mo de métadonnées par 100 000 écritures non commitées ; les statistiques anonymes et le rapport d'usage sont activés par défaut (à couper sur un réseau fermé)
- Coût — **Community gratuite sous BSL**, limitée à un utilisateur ; **Team** (5 utilisateurs, 500 Go, 500 requêtes par seconde, auto-hébergée) et **Enterprise** (sur devis, auto-hébergée ou lakeFS Cloud) sont payantes

## Licence et gouvernance

- **Business Source License 1.1 depuis la v1.87.0 (2026-09-22).** Le `LICENSE` porte Treeverse Labs Ltd. comme concédant et désigne « lakeFS 1.87.0 » comme œuvre ; la licence de conversion est **Apache-2.0**, quatre ans après la première mise à disposition publique de chaque version. Le journal des modifications de la v1.87.0 annonce le changement de licence en tête.
- **L'usage en production est permis à deux conditions** : le logiciel reste **non modifié** (configurer, utiliser les points d'extension documentés ou écrire un logiciel tiers par l'API publique ne compte pas comme une modification) et l'usage est **interne** — offrir, héberger ou donner accès à lakeFS à un tiers, payant ou non, est exclu ; les employés et les sous-traitants qui agissent pour l'organisation comptent comme internes. Un industriel qui exploite lakeFS chez lui est couvert ; une ESN qui l'installe pour un client doit faire valider le cas.
- **Les versions jusqu'à la v1.86.0 (2026-08-05) restent Apache-2.0**, mais sans correctifs à venir. La v1.86.0 corrige justement une faille de listage des dépôts par la passerelle S3.
- **La v1.87.0 retire aussi** la prise en charge des implémentations IAM branchables et du serveur de référence ACL : un déploiement qui s'en sert doit migrer avant de monter de version.
- **Ce que l'édition libre ne fait pas** : la page des éditions lui donne un seul utilisateur et un support communautaire ; le contrôle d'accès, l'audit, le catalogue Iceberg REST et le montage local figurent dans Team, le RBAC, le SSO (OIDC, SAML), SCIM et le journal d'audit sont marqués Enterprise dans la documentation — les deux pages ne concordent pas sur le découpage, mais tout cela est payant. Restent en libre : branches, commits, merges, retours en arrière, tags, import sans copie, passerelle S3, hooks, protection de branche, pull requests.
- **Propriétaire** : Treeverse, qui a aussi racheté DVC en novembre 2025 ; le billet de la licence cite ce rachat en contexte. Aucune fusion de Treeverse elle-même relevée.

## Limites à connaître

- **Fichiers et objets, pas de tables** : le versionnage est par commit sur un dépôt entier ; aucune sémantique de ligne ni de schéma.
- **Commits et merges concurrents sur une même branche** : la documentation recommande de les éviter (course et nouvelles tentatives).
- **Aucun lien avec Git** : le code et la donnée se relient à la main, en notant l'identifiant du commit lakeFS dans le run d'entraînement.
- **Les promesses d'échelle** (pétaoctets, milliers de branches) viennent du billet et de la page produit, pas d'un banc d'essai consulté ; le guide de dimensionnement ne chiffre que la grosse installation (plus de 100 branches actives, plus de 100 millions d'objets par commit).

## Écosystème

### Alternatives

- [[DVC]] — Versionnage de données et de modèles en ligne de commande, posé sur Git : des pointeurs `.dvc` dans le dépôt, le contenu dans un cache adressé par le hash et des remotes (S3 compatible, SSH, NAS), plus des pipelines reproductibles par `dvc repro` ; Apache-2.0, projet racheté par lakeFS en novembre 2025. — même propriétaire depuis novembre 2025 ; DVC passe par Git et des pointeurs, lakeFS par un serveur et une API S3, avec des branches côté stockage que DVC n'a pas.

### Compléments

- [[MinIO]] — Stockage objet S3-compatible auto-hébergé en Go, sous AGPLv3 : dépôt communautaire archivé et déclaré non maintenu par l'éditeur (2026-04-25), dernière release en octobre 2025 ; la suite est AIStor (propriétaire) ou un fork communautaire. — exemple de configuration de la page d'installation sur site ; la brique est non maintenue, préférer un autre stockage pour une nouvelle installation.
- [[Ceph]] — Plateforme de stockage distribué unifiée (objet, bloc, fichier) : l'API S3 via RADOS Gateway sur un cluster massivement scalable et auto-réparant, au prix d'une exploitation lourde. — cité par la page d'architecture comme stockage S3-compatible, avec NetApp StorageGRID.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — base de métadonnées exigée en production sur site (PostgreSQL 11 ou plus).
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark. — client Hadoop FS et ramasse-miettes Spark de lakeFS pour lire et nettoyer un dépôt depuis Spark.
- [[Delta Lake]] — Format de table ouvert pour le lakehouse, sous la Linux Foundation : un journal de transactions `_delta_log` au-dessus de fichiers Parquet, ACID, time travel, MERGE, évolution de schéma et Change Data Feed ; implémentations Spark, Rust (delta-rs) et Delta Kernel en Apache-2.0, avec des fonctions d'optimisation propres à Databricks hors de l'open source. — intégration listée par la documentation : les tables Delta se stockent et se versionnent comme n'importe quels fichiers du dépôt.
- [[MLflow]] — Plateforme open-source de cycle de vie ML (Linux Foundation) — tracking d'expériences, registre de modèles, packaging et déploiement, agnostique au framework et au cloud. — intégration officielle : le run journalise un jeu de données dont la source est `s3://dépôt/<commit>/…`, avec une branche par expérience.
- [[Kubernetes]] — Orchestrateur de conteneurs de référence (Apache-2.0, Go, CNCF) — déploie, replace, met à l'échelle et met à jour des applications sur un parc de machines ; réseau, stockage et ingress restent à choisir et à exploiter. — chart Helm documenté pour l'installation sur site.

## Ressources

- Documentation — https://docs.lakefs.io
- Dépôt — https://github.com/treeverse/lakeFS

## Voir aussi

- [[Fiabilité des données]] — le hub du dossier
- [[Versionnage de données]] — la notion : snapshot ou versionnage par contenu, fichiers, dépôt ou table
- [[Comparatif - Versionnage de données]] — ce qui départage lakeFS, DVC, Delta Lake et Apache Iceberg
- [[Stockage objet et API S3]] — ce que l'API S3 fixe, et ce qui change selon le stockage qui la sert
