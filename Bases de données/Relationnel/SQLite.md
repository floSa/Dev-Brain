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

<!-- AUTO:BANDEAU:START -->
> Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C | open-source | en bibliothèque, rien à héberger | production | à jour · 2026-08-12 |
<!-- AUTO:BANDEAU:END -->

## Définition

Moteur SQL **embarqué** : aucun serveur, aucun processus à administrer — la base entière tient
dans un seul fichier, lu et écrit en process par une bibliothèque C liée à l'application. Les
transactions sont ACID, le format de fichier est stable et portable d'une machine à l'autre.
C'est le moteur de base de données le plus déployé au monde : navigateurs, téléphones,
systèmes embarqués — partout où la donnée reste locale au process qui l'écrit.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Stockage local d'une application (desktop, mobile, CLI, embarqué) | Un seul écrivain à la fois, avec verrou sur toute la base : inadapté au write-heavy concurrent |
| Tests, prototypes, fixtures — une base jetable, sans infra | Typage dynamique (« type affinity ») laxiste : les contraintes sont plus souples qu'attendu |
| Fichier d'échange relationnel autonome, ou cache structuré sur disque | Aucune gestion d'utilisateurs ni de droits réseau — la sécurité se réduit aux droits du fichier |
| Charge à dominante lecture | |

## Mise en œuvre

- Installation — rien à installer côté Python, `sqlite3` est dans la bibliothèque standard ; ailleurs, une bibliothèque C à lier
- Point d'entrée — une base = un fichier `.db` ouvert en process ; SQL standard, CLI `sqlite3`
- Prérequis — aucun serveur, aucun compte, aucun port : les droits du fichier suffisent
- Exécution — dans le process appelant ; écritures sérialisées, le mode WAL améliore la lecture concurrente
- Coût — gratuit, code dans le domaine public ; variantes serveur/réseau par des projets tiers (Turso/libSQL, rqlite)

## Écosystème

### Alternatives

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[CockroachDB]] — Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

## Ressources

- Documentation — https://www.sqlite.org/docs.html
- Dépôt — https://github.com/sqlite/sqlite

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases relationnelles]] — ce qui départage les moteurs du dossier
