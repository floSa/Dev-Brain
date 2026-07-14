---
galaxie: dev
service: "Postgres"
type: rex
created: 2026-06-08
modified: 2026-06-08
tags: [rex, bugs, postgres]
---

# REX — Postgres

> Retours d'expérience et bugs rencontrés avec [[Dev/Services/Postgres|Postgres]]. Triés par date décroissante. Format standard : Symptôme → Cause → Fix → Référence projet → Leçon.

---

## 2026-04-12 — Connection pool exhaustion en prod (exemple)

**Symptôme** : timeouts intermittents sous charge, logs `FATAL: remaining connection slots are reserved for non-replication superuser connections`.

**Cause racine** : pool sqlalchemy à 5 connexions, 8 workers gunicorn → 40 connexions max côté app, pic à 60 sous charge → dépassement de `max_connections=100` partagé avec d'autres services sur le même cluster.

**Fix** :
1. `max_connections` PG : 100 → 200
2. PgBouncer en transaction mode devant Postgres
3. Pool sqlalchemy : `pool_pre_ping=True` pour détecter les connexions mortes
4. Monitoring sur `pg_stat_activity` count

**Référence** : exemple — remplacer par le lien projet (`Projects/<projet>/Bugs#YYYY-MM-DD`)

**Leçon** : toujours dimensionner `max_connections × workers × pool_size` en amont. Penser à PgBouncer dès qu'on a > 4 workers. Documentation prod : afficher la formule dans le README du déploiement.

---

<!-- Ajoute tes propres REX ci-dessus, plus récent en haut. -->
