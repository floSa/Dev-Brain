---
role: comparatif
nom: Comparatif - Bases temporelles
categorie: database/series-temporelles
tags: [timeseries]
---

# Comparatif - Bases temporelles

> On tranche sur : a-t-on déjà du Postgres, faut-il du SQL standard avec des jointures, et le site a-t-il déjà un historien industriel.

![[Comparatif - Bases temporelles.base]]

## Ce qui départage

- [[TimescaleDB]] — extension Postgres : l'hypertable partitionne par le temps en gardant SQL, jointures et ACID ; le multi-nœuds distribué est déprécié.
- [[InfluxDB]] — serveur temporel autonome, pensé append, avec rétention et downsampling automatiques ; la cardinalité des séries est son facteur de coût.
- [[AVEVA PI System]] — l'**historien industriel** propriétaire : Data Archive plus Asset Framework, qui rattache chaque mesure à une hiérarchie d'équipements ; installé sur site, licence à paramètres (flux de données, haute disponibilité) et plateforme annoncée Windows. On le choisit quand le site l'a déjà, pas pour un projet neuf : il n'est pas un moteur à embarquer, et l'apprentissage relève d'un produit distinct d'AVEVA.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
