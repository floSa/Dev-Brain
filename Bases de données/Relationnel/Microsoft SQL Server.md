---
role: brique
nom: Microsoft SQL Server
alias: [sql server, mssql, sqlserver, ms sql]
pitch: "SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche."
categorie: database/relationnel
famille: plateforme
licence_type: proprietary
hosted: [self, managed]
maturite: production
langage: C++
scaling: single-node
alternatives: ["[[Postgres]]", "[[MySQL]]", "[[MariaDB]]", "[[SQLite]]", "[[CockroachDB]]"]
complements: []
tags: [relational]
url_docs: https://learn.microsoft.com/en-us/sql/sql-server/
url_repo: 
---

# Microsoft SQL Server

<!-- AUTO:BANDEAU:START -->
> SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme C++ | propriétaire | self-hébergé ou managé · mono-nœud | production |
<!-- AUTO:BANDEAU:END -->

## Définition

SGBD relationnel d'entreprise de Microsoft, intégré en profondeur à l'écosystème **.NET /
Windows / Azure** : authentification Active Directory, pilotes de première classe, continuité
vers Azure SQL Database et Managed Instance. Son dialecte **T-SQL** est riche, et le produit
vient avec un outillage mûr qui couvre bien plus que la base — SSMS pour l'administration,
SSIS pour l'ETL, SSAS pour l'OLAP, SSRS pour le reporting. Côté moteur : Always On, colonnes
chiffrées, index columnstore. Il tourne sur Linux et en conteneur depuis 2017.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Environnement Microsoft établi (.NET, Active Directory, Azure) | Le coût de licence grimpe vite, sur un modèle par cœur : l'édition et les fonctions incluses sont à vérifier avant tout engagement |
| Besoin de l'outillage BI/ETL intégré (SSIS, SSAS, SSRS) et de T-SQL | Verrouillage T-SQL : le SQL écrit ici n'est pas portable vers un autre moteur sans réécriture |
| Exigences entreprise : support éditeur, sécurité avancée, conformité | Limites strictes de l'édition Express (taille de base, RAM, CPU) à anticiper dès la conception |
| Migration ou consolidation sur Azure SQL Database / Managed Instance | |

## Mise en œuvre

- Installation — installeur Windows, paquet Linux ou conteneur ; managé via Azure SQL Database et Managed Instance
- Point d'entrée — serveur SQL sur le port 1433, dialecte T-SQL ; SSMS, `sqlcmd`, pilotes ODBC/JDBC
- Prérequis — une licence adaptée à l'usage visé ; les services BI (SSIS, SSAS, SSRS) s'installent séparément
- Exécution — self-hébergé ou managé, un nœud plus des réplicas de lecture ; haute disponibilité via Always On Availability Groups
- Coût — licences par cœur ; édition Express gratuite avec limites de taille et de CPU, Developer gratuite hors production

## Écosystème

### Alternatives

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.

## Ressources

- Documentation — https://learn.microsoft.com/en-us/sql/sql-server/

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases relationnelles]] — ce qui départage les moteurs du dossier
