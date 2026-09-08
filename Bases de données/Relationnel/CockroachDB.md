---
role: brique
nom: CockroachDB
alias: [cockroachdb, cockroach, crdb]
pitch: "Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région."
categorie: database/relationnel
famille: plateforme
licence_type: source-available
hosted: [self, managed]
maturite: production
langage: Go
scaling: distributed
alternatives: ["[[Postgres]]", "[[MySQL]]", "[[MariaDB]]", "[[SQLite]]", "[[Microsoft SQL Server]]"]
complements: []
tags: [relational, distributed]
url_docs: https://www.cockroachlabs.com/docs/
url_repo: https://github.com/cockroachdb/cockroach
---

# CockroachDB

<!-- AUTO:BANDEAU:START -->
> Relationnel distribué (NewSQL) compatible Postgres : scale horizontal et forte cohérence multi-région.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme Go | source-available | self-hébergé ou managé · distribué | production | à jour · 2026-09-02 |
<!-- AUTO:BANDEAU:END -->

## Définition

Base **NewSQL** : la sémantique SQL relationnelle et des transactions ACID sérialisables d'un
côté, le scale horizontal et la tolérance aux pannes d'un système distribué de l'autre. Les
données sont découpées en ranges répliqués par consensus Raft, rééquilibrés automatiquement, et
le cluster survit à la perte de nœuds ou de zones entières. Elle parle le **protocole filaire
de Postgres** : les pilotes pg fonctionnent tels quels, ce qui rend la bascule peu coûteuse
côté application.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Volumétrie ou croissance qui dépasse un seul nœud, tout en gardant du SQL transactionnel | La latence des transactions distribuées dépasse celle d'un mono-nœud : la localité des données est à penser |
| Haute disponibilité et résilience multi-zone ou multi-région exigées | Compatibilité Postgres élevée mais incomplète — certaines extensions et fonctions manquent |
| Résidence des données par région (data domiciling) avec une seule base logique | Clés primaires et index à concevoir avec soin, sous peine de hotspots de range |
| Élasticité : ajouter des nœuds pour encaisser la charge en écriture | |

## Mise en œuvre

- Installation — binaire, image Docker ou opérateur Kubernetes ; managé via CockroachDB Cloud, y compris en serverless
- Point d'entrée — protocole filaire Postgres sur le port 26257 ; les pilotes pg et le client `cockroach sql`
- Prérequis — un cluster d'au moins trois nœuds pour que le consensus Raft ait un quorum
- Exécution — self-hébergé ou managé, distribué : la capacité croît avec le nombre de nœuds, le rééquilibrage est automatique
- Coût — CockroachDB Software License depuis 2024, source-available et non open-source ; offre gratuite limitée, payant au-delà

## Écosystème

### Alternatives

- [[Postgres]] — SGBD relationnel-objet open-source avancé : très extensible, standard de fait du backend moderne.
- [[MySQL]] — SGBD relationnel open-source ultra-répandu, simple et éprouvé pour le web.
- [[MariaDB]] — Fork communautaire de MySQL, 100 % open-source, gouvernance indépendante d'Oracle.
- [[SQLite]] — Moteur relationnel embarqué, sans serveur — une base = un fichier, zéro administration.
- [[Microsoft SQL Server]] — SGBD d'entreprise Microsoft, intégré à l'écosystème .NET/Azure, T-SQL et outillage riche.

## Ressources

- Documentation — https://www.cockroachlabs.com/docs/
- Dépôt — https://github.com/cockroachdb/cockroach

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases relationnelles]] — ce qui départage les moteurs du dossier
