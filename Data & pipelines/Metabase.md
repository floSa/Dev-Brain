---
role: brique
nom: Metabase
alias: [metabase]
pitch: "BI auto-hébergée orientée utilisateurs métier : questions sans code et SQL natif, tableaux de bord, alertes, en un seul conteneur Java ; AGPL-3.0 avec SSO avancé, droits par ligne et embedding complet réservés aux éditions payantes."
categorie: data/bi
famille: application
licence_type: open-core
hosted: [self, managed]
maturite: production
langage: Clojure
alternatives: ["[[Apache Superset]]"]
complements: ["[[Postgres]]", "[[MySQL]]", "[[ClickHouse]]"]
tags: [bi, dashboard, self-hosted]
url_docs: https://www.metabase.com/docs/latest/
url_repo: https://github.com/metabase/metabase
---

# Metabase

<!-- AUTO:BANDEAU:START -->
> BI auto-hébergée orientée utilisateurs métier : questions sans code et SQL natif, tableaux de bord, alertes, en un seul conteneur Java ; AGPL-3.0 avec SSO avancé, droits par ligne et embedding complet réservés aux éditions payantes.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Application Clojure | open-core | self-hébergé ou managé | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Outil de **BI** à déployer chez soi : on branche une base, on construit des « questions » au
constructeur sans code ou en SQL natif, on les assemble en tableaux de bord et en alertes.
Conçu pour l'utilisateur métier qui n'écrit pas de SQL, avec un éditeur SQL pour les autres.
Un seul conteneur (ou JAR) sur JVM, plus une base de métadonnées PostgreSQL. Le dépôt porte
**deux licences** : AGPL-3.0 partout sauf dans `enterprise/`, sous licence commerciale (code lisible,
usage soumis à une clé).

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Des équipes métier doivent explorer et partager des tableaux de bord sans écrire de SQL | SAML, JWT, OIDC, LDAP avancé, permissions par ligne et par colonne, audit : édition Pro (517,50 $/mois pour 10 utilisateurs, tarif public du 2026-09-30) ou Enterprise, sur devis |
| Mise en route minimale : un conteneur, une base PostgreSQL | Embedding interactif, SDK React, marque blanche : payant ; l'embedding statique signé reste libre avec le bandeau « Powered by Metabase » |
| Sources classiques : PostgreSQL, MySQL, SQL Server, Oracle, ClickHouse, BigQuery, Snowflake, Presto et Starburst en drivers officiels | Trino ou DuckDB attendus en driver officiel : absents de la liste, donc communautaires |
| Alertes e-mail, Slack et webhook dans l'édition libre | Metabase embarqué dans un produit livré à des tiers, sans licence commerciale ni conformité AGPL réseau |
| | Droits par ligne, embedding et SSO OAuth / LDAP sans édition payante → [[Apache Superset]] |

## Mise en œuvre

- Installation — `docker run metabase/metabase` (image AGPL ; l'image `metabase-enterprise` est sous licence commerciale) ou JAR avec systemd. Constaté le 2026-09-30 : 0.63.19 (Docker Hub, 2026-09-30 ; tag GitHub v0.63.18, 2026-09-16), 49,5k étoiles, une version mineure par mois
- Point d'entrée — interface web sur le port 3000 ; constructeur de questions, éditeur SQL, tableaux de bord
- Prérequis — Java 25 pour le JAR ; base de métadonnées PostgreSQL (MySQL ≥ 8.4 ou MariaDB ≥ 10.6 acceptés) : le H2 par défaut est déconseillé en production
- Exécution — self-hébergé ou Metabase Cloud ; processus JVM unique (heap à environ 80 % de la RAM, non vérifié à la source) ; le multi-instance en édition libre n'est pas documenté. Pas de chart Helm officiel trouvé
- Coût — édition libre gratuite. **Licence** : AGPL-3.0 (hors `enterprise/`). Une ESN peut déployer l'édition libre chez un client pour son usage interne. Embarquer Metabase dans un produit livré à des tiers relève de l'AGPL réseau, de la licence d'embedding avec attribution ou d'une licence commerciale : à faire valider par un juriste. Les fonctions payantes (voir Écarter si) exigent une clé, et chaque client final d'un produit livré doit en avoir une

## Écosystème

### Alternatives

- [[Apache Superset]] — BI auto-hébergée Apache-2.0 tournée vers l'exploration : SQL Lab, constructeur de graphiques, tableaux de bord, droits par ligne, alertes et embedding sans édition payante ; exploitation plus lourde (base de métadonnées, Redis, Celery). — tout est dans la distribution Apache-2.0 (droits par ligne, embedding, alertes), au prix d'une exploitation plus lourde.

### Compléments

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne. — base de métadonnées recommandée en production, et source la plus courante.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web. — source supportée ; accepté aussi comme base de métadonnées (MySQL ≥ 8.4, MariaDB ≥ 10.6).
- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence. — driver officiel : tableaux de bord sur des données d'événements à forte volumétrie.

## Ressources

- Documentation — https://www.metabase.com/docs/latest/
- Dépôt — https://github.com/metabase/metabase

## Voir aussi

- [[Comparatif - BI auto-hébergée]] — ce qui départage les outils de BI du dossier
- [[Data & pipelines]] — le hub du domaine
- [[OLTP, OLAP et lakehouse]] — la notion : d'où viennent les données qu'une BI interroge
- [[Grafana]] — voisin : tableaux de bord de métriques et de séries techniques, pas d'analyse métier
- [[Streamlit]] — voisin : application de données écrite en Python, pas un outil servi
