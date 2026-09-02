---
role: brique
nom: CockroachDB
alias: [cockroachdb, cockroach, crdb]
pitch: "Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région."
categorie: database/relationnel
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Postgres]]", "[[MySQL]]", "[[MariaDB]]", "[[SQLite]]", "[[Microsoft SQL Server]]"]
complements: []
tags: [relational, distributed]
url_docs: https://www.cockroachlabs.com/docs/
url_repo: https://github.com/cockroachdb/cockroach
---

# CockroachDB

## Pourquoi

Base **NewSQL** : la sémantique SQL relationnelle et les transactions ACID sérialisables d'un côté, le scale horizontal et la tolérance aux pannes d'un système distribué de l'autre. Réplication par consensus Raft, rééquilibrage automatique des données, survie à la perte de nœuds ou de zones. Parle le **protocole filaire de Postgres** : les pilotes pg fonctionnent tels quels.

## Quand l'utiliser

- Forte croissance ou volumétrie qui dépasse un seul nœud, tout en gardant du SQL transactionnel.
- Haute disponibilité et résilience multi-zone / multi-région exigées.
- Résidence des données par région (data domiciling) avec une seule base logique.
- Élasticité : ajouter des nœuds pour encaisser la charge en écriture.

## Quand NE PAS l'utiliser

- Besoin mono-nœud simple, sans complexité distribuée → [[Postgres]].
- Application embarquée locale → [[SQLite]].
- Écosystème d'extensions Postgres requis (PostGIS complet, pgvector…) → [[Postgres]].

## Déploiement & coût

- Self-host (cluster de nœuds, Docker/Kubernetes) ou managé (CockroachDB Cloud, serverless).
- Scaling horizontal natif : la capacité croît avec le nombre de nœuds.
- Licence **source-available** (CockroachDB Software License depuis 2024), pas open-source pur ; offre gratuite limitée, payant au-delà.

## Pièges

- La latence des transactions distribuées dépasse celle d'un mono-nœud : penser la localité des données.
- Compatibilité Postgres élevée mais incomplète (certaines extensions et fonctions absentes).
- Bien concevoir clés primaires et index pour éviter les hotspots de range.

## Alternatives

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

## Liens

- [[Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases relationnelles]] — comparatif des moteurs
- Doc : https://www.cockroachlabs.com/docs/
