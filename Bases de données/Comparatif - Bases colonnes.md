---
role: comparatif
nom: Comparatif - Bases colonnes
categorie: database/analytique
tags: [columnar, olap]
---

# Comparatif - Bases colonnes

> On tranche sur : un cluster ou un seul process, et la tolérance aux écritures en place.

![[Comparatif - Bases colonnes.base]]

## Ce qui départage

- [[DuckDB]] — in-process, sans serveur : elle tourne dans le process hôte et requête Parquet, CSV et JSON directement ; la RAM et le disque local bornent le volume.
- [[ClickHouse]] — distribuée par sharding et réplication, mais updates et deletes sont des mutations asynchrones coûteuses : le modèle est pensé pour l'append.
- [[Snowflake]] — **absent de la vue ci-dessus, et c'est voulu** : il est rangé en `ml/plateforme` et non en `database/analytique`, parce que son concurrent réel en clientèle est une plateforme et non un moteur (règle D-R8 de la taxonomie). Il départage pourtant les deux autres sur le seul axe qui compte ici : rien à opérer, mais rien à auto-héberger non plus, et un enfermement qui commence dès qu'on écrit une fonction Cortex en SQL.

## Voir aussi

- [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
