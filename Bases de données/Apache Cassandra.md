---
role: brique
nom: Apache Cassandra
alias: [cassandra, apache cassandra]
pitch: "Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter."
categorie: database/cle-valeur
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: Java
scaling: distributed
alternatives: ["[[MongoDB]]", "[[Redis]]"]
complements: []
tags: [nosql, wide-column, distributed]
url_docs: https://cassandra.apache.org/doc/
url_repo: https://github.com/apache/cassandra
---

# Apache Cassandra

<!-- AUTO:BANDEAU:START -->
> Base NoSQL wide-column distribuée, sans maître : écritures massives et haute dispo multi-datacenter.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Plateforme Java | open-source | self-hébergé ou managé · distribué | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base NoSQL **wide-column** conçue pour le volume et la disponibilité. L'architecture est
**sans maître**, de pair à pair : tous les nœuds sont égaux, il n'y a pas de point unique de
défaillance, et ajouter des nœuds augmente la capacité de façon quasi linéaire. La
réplication multi-datacenter est native et la cohérence se règle **par requête**, de `ONE` à
`QUORUM` ou `ALL`. Le modèle de données se pense autour des requêtes : on dénormalise et on
modélise par pattern d'accès, pas par entité.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Écritures massives et continues : télémétrie, logs, IoT, séries d'événements | Modéliser par entité plutôt que par requête produit des partitions inexploitables |
| Haute disponibilité « always-on », déploiement multi-région ou multi-datacenter | Requêtes ad hoc, jointures, agrégations imprévues → [[Postgres]] ; ici, `ALLOW FILTERING` est une porte ouverte aux scans |
| Volumes dépassant un seul nœud, avec un scale-out linéaire attendu | Partitions trop larges ou « hot partitions » : elles dégradent tout le cluster |
| Patterns de lecture connus d'avance et stables | Exploitation JVM exigeante : compaction, repair et tombstones à surveiller en continu |
| | Petit volume tenant sur un nœud : la complexité opérationnelle du cluster ne se rembourse pas → [[Postgres]] |

## Mise en œuvre

- Installation — cluster de nœuds en self-host, ou managé (DataStax Astra, Amazon Keyspaces)
- Point d'entrée — CQL, depuis un client ou un pilote
- Prérequis — une JVM à régler, et un modèle pensé par requête avant la première écriture
- Exécution — self-hébergé ou managé ; distribué, scaling horizontal par ajout de nœuds, réplication réglable par datacenter
- Coût — gratuit, licence Apache 2.0 ; le coût réel est l'exploitation du cluster — compaction, repair, tuning JVM

## Écosystème

### Alternatives

- [[MongoDB]] — Base NoSQL orientée documents (BSON/JSON) : schéma souple et scale horizontal natif par sharding.
- [[Redis]] — Store clé-valeur en mémoire ultra-rapide : cache, sessions, files et broker pub/sub.

## Ressources

- Documentation — https://cassandra.apache.org/doc/
- Dépôt — https://github.com/apache/cassandra

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases NoSQL]] — ce qui départage les moteurs du dossier
