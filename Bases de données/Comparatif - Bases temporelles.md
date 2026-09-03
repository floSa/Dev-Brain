---
role: comparatif
nom: Comparatif - Bases temporelles
categorie: database/series-temporelles
tags: [timeseries]
---

# Comparatif - Bases temporelles

> On tranche sur : a-t-on déjà du Postgres, et faut-il du SQL standard avec des jointures.

![[Comparatif - Bases temporelles.base]]

## Ce qui départage

- [[TimescaleDB]] — extension Postgres : l'hypertable partitionne par le temps en gardant SQL, jointures et ACID ; le multi-nœuds distribué est déprécié.
- [[InfluxDB]] — serveur temporel autonome, pensé append, avec rétention et downsampling automatiques ; la cardinalité des séries est son facteur de coût.
