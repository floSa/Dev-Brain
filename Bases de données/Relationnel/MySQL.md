---
role: brique
nom: MySQL
alias: [mysql]
pitch: "SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web."
categorie: database/relationnel
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: C/C++
scaling: single-node
alternatives: ["[[Postgres]]", "[[MariaDB]]", "[[SQLite]]", "[[CockroachDB]]", "[[Microsoft SQL Server]]"]
complements: ["[[MySQL Workbench]]"]
tags: [relational]
url_docs: https://dev.mysql.com/doc/
url_repo: https://github.com/mysql/mysql-server
---

# MySQL

<!-- AUTO:BANDEAU:START -->
> SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C/C++ | open-source | self-hébergé ou managé · mono-nœud | production | à jour · 2026-07-28 |
<!-- AUTO:BANDEAU:END -->

## Définition

Le SGBD relationnel le plus déployé du web, pilier historique de la stack LAMP. Le moteur de
stockage par défaut, InnoDB, est transactionnel et éprouvé ; le reste du produit privilégie la
simplicité de mise en route sur la richesse fonctionnelle. Son vrai atout est l'écosystème :
hébergement managé, outillage et documentation sont disponibles partout, pour toutes les
versions. Détenu par Oracle, qui en publie une édition Community et une édition Enterprise
commerciale.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Application web classique, CMS (WordPress…), besoin relationnel standard | Défauts historiques laxistes : `utf8mb4` et un `sql_mode` strict sont à forcer à la main |
| Chercher le plus large écosystème d'hébergement, d'outillage et de tutoriels | Divergences fonctionnelles avec MariaDB : la compatibilité n'est pas garantie à 100 % |
| Charge en lecture intensive avec réplicas, sur un schéma simple et stable | Gouvernance Oracle : certaines fonctionnalités restent réservées à l'édition Enterprise |
| Un existant ou un hébergeur qui impose MySQL | |

## Mise en œuvre

- Installation — paquet système ou image Docker ; managé partout (RDS, Cloud SQL, Aurora MySQL)
- Point d'entrée — serveur SQL sur le port 3306 ; client `mysql`, pilotes standard
- Prérequis — un serveur à administrer ; le moteur InnoDB pour tout ce qui doit être transactionnel
- Exécution — un primaire plus des réplicas de lecture ; sharding applicatif, ou Vitess pour l'échelle
- Coût — édition Community gratuite sous GPL ; édition Enterprise payante (support, outillage)

## Écosystème

### Alternatives

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

### Compléments

- [[MySQL Workbench]] — Outil graphique officiel MySQL d'Oracle : modélisation, requêtes SQL et administration du serveur. — la modélisation et l'administration graphiques du serveur

## Ressources

- Documentation — https://dev.mysql.com/doc/
- Dépôt — https://github.com/mysql/mysql-server

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases relationnelles]] — ce qui départage les moteurs du dossier
