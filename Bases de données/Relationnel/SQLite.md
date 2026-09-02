---
role: brique
nom: SQLite
alias: [sqlite, sqlite3]
pitch: "Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration."
categorie: database/relationnel
famille: paquet
licence_type: open-source
maturite: production
langage: C
alternatives: ["[[Postgres]]", "[[MySQL]]", "[[MariaDB]]", "[[CockroachDB]]", "[[Microsoft SQL Server]]"]
complements: []
tags: [relational, embedded]
url_docs: https://www.sqlite.org/docs.html
url_repo: https://github.com/sqlite/sqlite
---

# SQLite

## Pourquoi

Moteur SQL **embarqué** : pas de serveur, pas de processus à administrer — la base entière tient dans un seul fichier, lu et écrit en process par une bibliothèque C. Transactions ACID, très fiable, le moteur de base de données le plus déployé au monde (navigateurs, mobiles, embarqué). Code source dans le domaine public.

## Quand l'utiliser

- Stockage local d'une application (desktop, mobile, CLI, embarqué).
- Tests, prototypes, fixtures — une base jetable sans infra.
- Fichier d'échange relationnel autonome, ou cache structuré sur disque.
- Charge à dominante lecture, un seul écrivain à la fois.

## Quand NE PAS l'utiliser

- Accès concurrent en écriture par plusieurs clients réseau → [[Postgres]] ou [[MySQL]].
- Forte volumétrie distribuée ou haute disponibilité → [[CockroachDB]].
- Besoin d'un serveur central partagé entre services.

## Déploiement & coût

- Pas de déploiement : bibliothèque liée à l'application, base = fichier `.db` sur disque.
- Concurrence d'écriture sérialisée ; le mode WAL améliore la lecture concurrente.
- Gratuit, domaine public ; variantes serveur/réseau via projets tiers (Turso/libSQL, rqlite).

## Pièges

- Un seul écrivain à la fois : verrou sur toute la base, pas adapté au write-heavy concurrent.
- Typage dynamique (« type affinity ») laxiste — contraintes plus souples qu'attendu.
- Pas de gestion d'utilisateurs ni de droits réseau : sécurité = droits du fichier.

## Alternatives

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

## Liens

- [[Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases relationnelles]] — comparatif des moteurs
- Doc : https://www.sqlite.org/docs.html
