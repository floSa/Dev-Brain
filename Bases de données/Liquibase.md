---
role: brique
nom: Liquibase
alias: [liquibase]
pitch: "Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD."
categorie: database/migration
famille: cli
licence_type: open-core
maturite: production
langage: Java
alternatives: ["[[Flyway]]", "[[Alembic]]"]
complements: []
tags: [migration, relational]
url_docs: https://docs.liquibase.com/
url_repo: https://github.com/liquibase/liquibase
---

# Liquibase

<!-- AUTO:BANDEAU:START -->
> Outil de migration de schéma piloté par changelog (XML/YAML/JSON/SQL), multi-SGBD et orienté CI/CD.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| CLI Java | open-core | en ligne de commande, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Gère l'évolution d'un schéma de base comme du code versionné. Les changements sont décrits
dans un **changelog** — XML, YAML, JSON ou SQL — où chaque `changeSet` est appliqué une seule
fois et tracé dans une table de contrôle. L'atout est l'abstraction : un même changelog
déclaratif s'applique à plusieurs SGBD, avec rollback, contextes et labels, et s'intègre à un
pipeline CI/CD.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Versionner le schéma et rejouer les migrations de façon déterministe entre environnements | L'abstraction XML/YAML ajoute une couche de traduction : sur un seul SGBD, le SQL brut est plus direct |
| Format abstrait (YAML, XML, JSON) portable entre plusieurs moteurs | Les rollbacks automatiques ne couvrent pas tous les changements : les DDL destructifs se testent avant de compter dessus |
| Pipeline CI/CD appliquant les migrations automatiquement au déploiement | Qualité et observabilité relèvent de l'édition Pro payante |

## Mise en œuvre

- Installation — CLI Java, plugins Maven ou Gradle, ou image Docker
- Point d'entrée — un changelog XML, YAML, JSON ou SQL, appliqué `changeSet` par `changeSet`
- Prérequis — une JVM
- Exécution — en local ou en CI ; rien à héberger
- Coût — cœur gratuit sous Apache 2.0 ; qualité et observabilité en édition Pro — c'est le modèle open-core

## Écosystème

### Alternatives

- [[Flyway]] — Migrations de base de données SQL-first par Redgate : versionnées, simples, intégrées au build.
- [[Alembic]] — Outil de migrations de schéma pour SQLAlchemy : scripts versionnés, autogénération du diff et exécution séquentielle.

## Ressources

- Documentation — https://docs.liquibase.com/
- Dépôt — https://github.com/liquibase/liquibase

## Voir aussi

- [[Migrations de schéma]] — la notion du dossier
- [[Comparatif - Migrations de schéma]] — ce qui départage les outils du dossier
