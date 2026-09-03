---
role: comparatif
nom: Comparatif - Bases relationnelles
categorie: database/relationnel
tags: [relational]
---

# Comparatif - Bases relationnelles

> On tranche sur : serveur ou fichier embarqué, un nœud ou plusieurs, licence et écosystème.

![[Comparatif - Bases relationnelles.base]]

## Ce qui départage

- [[Postgres]] — l'extensibilité : PostGIS, [[pgvector]] et TimescaleDB s'ajoutent au même moteur ; VACUUM et le coût des connexions sont le prix.
- [[SQLite]] — embarqué, une base tient dans un fichier, sans serveur : un seul écrivain à la fois, avec verrou sur toute la base.
- [[CockroachDB]] — NewSQL : transactions sérialisables réparties par Raft et protocole filaire Postgres, mais compatibilité incomplète et latence distribuée.
- [[MySQL]] — le plus déployé du web, l'écosystème d'hébergement le plus large ; ses défauts historiques se forcent à la main (`utf8mb4`, `sql_mode` strict).
- [[MariaDB]] — fork 100 % open-source de MySQL, gouvernance hors Oracle, moteurs propres (ColumnStore, Galera) ; la divergence avec MySQL croît.
- [[Microsoft SQL Server]] — le seul propriétaire : T-SQL et l'outillage BI intégré, contre une licence par cœur et un SQL non portable.
