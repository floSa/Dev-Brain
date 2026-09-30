---
role: brique
nom: Apache Superset
alias: [superset]
pitch: "BI auto-hébergée Apache-2.0 tournée vers l'exploration : SQL Lab, constructeur de graphiques, tableaux de bord, droits par ligne, alertes et embedding sans édition payante ; exploitation plus lourde (base de métadonnées, Redis, Celery)."
categorie: data/bi
famille: application
licence_type: open-source
hosted: [self]
maturite: production
langage: Python
scaling: distributed
alternatives: ["[[Metabase]]"]
complements: ["[[Trino]]", "[[Postgres]]", "[[Redis]]"]
tags: [bi, dashboard, self-hosted, distributed]
url_docs: https://superset.apache.org/docs/intro
url_repo: https://github.com/apache/superset
---

# Apache Superset

<!-- AUTO:BANDEAU:START -->
> BI auto-hébergée Apache-2.0 tournée vers l'exploration : SQL Lab, constructeur de graphiques, tableaux de bord, droits par ligne, alertes et embedding sans édition payante ; exploitation plus lourde (base de métadonnées, Redis, Celery).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Python | open-source | self-hébergé · distribué | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Plateforme de **BI**, projet de l'Apache Software Foundation. Elle couvre les mêmes
usages que Metabase — graphiques, tableaux de bord, alertes — avec plus de prise pour
l'analyste : **SQL Lab**, un éditeur SQL libre accordé par le rôle `sql_lab`, à côté du
constructeur de graphiques. Tout est dans une seule distribution **Apache-2.0** : pas
d'édition payante côté projet. Le prix est l'exploitation : une application Flask, une base de
métadonnées, un cache Redis et des workers Celery.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des analystes SQL veulent explorer librement (SQL Lab) et publier des tableaux de bord | Une équipe qui veut une mise en route en dix minutes et aucune pièce à exploiter → [[Metabase]] |
| Droits par ligne (RLS), rôles, alertes et rapports, embedding par SDK et jeton invité, sans licence commerciale | SAML natif non documenté dans les pages lues ; OAuth / OIDC et LDAP passent par Flask AppBuilder, à configurer à la main |
| Livrer ou embarquer la BI dans un produit : Apache-2.0, pas de clause réseau ni de clé | Pas de capacité à tenir Redis, Celery, un navigateur headless pour les rapports et la base de métadonnées |
| Une très grande variété de sources : tout dialecte SQLAlchemy, dont [[Trino]] | Déploiement Kubernetes sur le chart Helm : déprécié, l'opérateur Kubernetes officiel le remplace |

## Mise en œuvre

- Installation — `pip install apache-superset` ou images Docker ; le Docker Compose officiel n'est ni supporté ni recommandé en production (un hôte, sans haute disponibilité). Constaté le 2026-09-30 : 6.1.0 (2026-05-13), 75k étoiles, un majeur ou mineur tous les 5 à 6 mois, 11 CVE publiées en 2025-2026 dans la doc
- Point d'entrée — interface web : SQL Lab, constructeur de graphiques, tableaux de bord ; rôles Admin, Alpha, Gamma, `sql_lab`
- Prérequis — base de métadonnées [[Postgres]] ou MySQL (SQLite exclu en production) ; [[Redis]] pour le cache et comme broker ; worker et beat Celery pour les alertes, rapports, requêtes asynchrones ; navigateur headless pour les captures
- Exécution — self-hébergé, distribué : web, workers, beat, cache. Pour [[Kubernetes]], l'opérateur officiel `apache/superset-kubernetes-operator` ; le chart Helm `helm/superset` est marqué déprécié.
- Coût — gratuit, Apache-2.0, polices Inter et Fira Code sous SIL OFL-1.1. **Aucune fonction payante dans la distribution du projet** : une ESN peut déployer chez un client, modifier et embarquer dans un produit livré, en conservant les mentions de licence et le fichier NOTICE. Le coût réel est l'exploitation

## Écosystème

### Alternatives

- [[Metabase]] — BI auto-hébergée orientée utilisateurs métier : questions sans code et SQL natif, tableaux de bord, alertes, en un seul conteneur Java ; AGPL-3.0 avec SSO avancé, droits par ligne et embedding complet réservés aux éditions payantes. — mise en route minimale et usage sans code, mais SSO avancé, droits par ligne et embedding complet sont payants (open-core, AGPL-3.0).

### Compléments

- [[Trino]] — Moteur de requête SQL distribué et fédéré, séparé du stockage : une requête interactive joint des tables Iceberg, Delta ou Hive et des bases (PostgreSQL, MySQL…) sans rien stocker lui-même ; Apache-2.0, coordinateur et workers en Java. — dialecte SQLAlchemy cité au README : BI sur un lac interrogé par Trino.
- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — base de métadonnées testée ; SQLite est exclu en production.
- [[Redis]] — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub. — cache et broker des workers Celery.

## Ressources

- Documentation — https://superset.apache.org/docs/intro
- Dépôt — https://github.com/apache/superset

## Voir aussi

- [[Comparatif - BI auto-hébergée]] — ce qui départage les outils de BI du dossier
- [[Data & pipelines]] — le hub du domaine
- [[OLTP, OLAP et lakehouse]] — la notion : d'où viennent les données qu'une BI interroge
- [[Grafana]] — voisin : tableaux de bord de métriques et de séries techniques
- [[Streamlit]] — voisin : application de données écrite en Python
