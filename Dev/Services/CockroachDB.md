---
galaxie: dev
type: service
nom: CockroachDB
alias: [cockroachdb, cockroach, crdb]
pitch: "Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région."
categorie: database/relational
licence_type: source-available
hosted: both
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Dev/Services/Postgres|Postgres]]", "[[Dev/Services/MySQL|MySQL]]", "[[Dev/Services/MariaDB|MariaDB]]", "[[Dev/Services/SQLite|SQLite]]", "[[Dev/Services/Microsoft SQL Server|Microsoft SQL Server]]"]
remplace_par: []
status: actif
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

- Besoin mono-nœud simple, sans complexité distribuée → [[Dev/Services/Postgres|Postgres]].
- Application embarquée locale → [[Dev/Services/SQLite|SQLite]].
- Écosystème d'extensions Postgres requis (PostGIS complet, pgvector…) → [[Dev/Services/Postgres|Postgres]].

## Déploiement & coût

- Self-host (cluster de nœuds, Docker/Kubernetes) ou managé (CockroachDB Cloud, serverless).
- Scaling horizontal natif : la capacité croît avec le nombre de nœuds.
- Licence **source-available** (CockroachDB Software License depuis 2024), pas open-source pur ; offre gratuite limitée, payant au-delà.

## Pièges

- La latence des transactions distribuées dépasse celle d'un mono-nœud : penser la localité des données.
- Compatibilité Postgres élevée mais incomplète (certaines extensions et fonctions absentes).
- Bien concevoir clés primaires et index pour éviter les hotspots de range.
- Retours d'expérience détaillés : `Dev/REX/REX - CockroachDB.md`.

## Alternatives

- [[Dev/Services/Postgres|Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[Dev/Services/MySQL|MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[Dev/Services/MariaDB|MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[Dev/Services/SQLite|SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[Dev/Services/Microsoft SQL Server|Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

## Liens

- [[Wiki/Concepts/Bases de données|Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases relationnelles]] — comparatif des moteurs
- `Dev/REX/REX - CockroachDB.md` — retours d'expérience
- Doc : https://www.cockroachlabs.com/docs/
