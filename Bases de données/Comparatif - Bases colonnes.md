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
