---
role: comparatif
nom: Comparatif - Bases NoSQL
categorie: database/cle-valeur
tags: [nosql]
---

# Comparatif - Bases NoSQL

> On tranche sur : ce qu'on stocke — un document, une structure en RAM, ou un flux d'écritures massif.

![[Comparatif - Bases NoSQL.base]]

## Ce qui départage

- [[MongoDB]] — documents BSON à schéma libre : l'objet métier se lit et s'écrit d'un bloc, et `$lookup` ne remplace pas une jointure.
- [[Redis]] — tout en RAM, chemin de commande mono-thread : sub-milliseconde, mais dépasser la mémoire déclenche l'éviction et une commande coûteuse bloque le serveur.
- [[Apache Cassandra]] — sans maître, réplication multi-datacenter et cohérence réglable par requête ; le modèle se pense par requête, pas par entité.
