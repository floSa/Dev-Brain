---
role: brique
nom: ClickHouse
alias: [clickhouse]
pitch: "SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence."
categorie: database/analytique
famille: plateforme
licence_type: open-source
hosted: [self, managed]
maturite: production
langage: C++
scaling: distributed
alternatives: ["[[DuckDB]]", "[[Snowflake]]"]
complements: []
tags: [columnar, olap, distributed]
url_docs: https://clickhouse.com/docs
url_repo: https://github.com/ClickHouse/ClickHouse
---

# ClickHouse

<!-- AUTO:BANDEAU:START -->
> SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence.

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Plateforme C++ | open-source | self-hébergé ou managé · distribué | production | à jour · 2026-09-06 |
<!-- AUTO:BANDEAU:END -->

## Définition

SGBD **orienté colonnes** conçu pour l'OLAP. Les données sont stockées et traitées par
colonne, fortement compressées, avec une exécution **vectorisée** : le moteur balaie des
centaines de millions de lignes par seconde. Il se distribue par sharding, pour le volume, et
par réplication, pour la disponibilité. Le choix du moteur de table — la famille MergeTree —
et des clés de tri est la décision structurante : il se fait avant l'ingestion et commande
les performances de toutes les requêtes qui suivront.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Analytique temps réel sur gros volumes : tableaux de bord, observabilité, événements | Mises à jour et suppressions fréquentes ligne à ligne : le modèle est pensé pour l'append, et les mutations sont asynchrones et coûteuses |
| Agrégations massives balayant beaucoup de lignes sur peu de colonnes | Lecture attendue juste après l'écriture : la cohérence de la réplication est éventuelle |
| Ingestion à fort débit de logs, métriques, télémétrie | OLTP transactionnel, beaucoup de petites écritures et de mises à jour ponctuelles → [[Postgres]] |
| Scale-out horizontal sur un cluster | |

## Mise en œuvre

- Installation — binaire ou cluster en self-host, ou managé sur ClickHouse Cloud
- Point d'entrée — SQL, depuis un client ou un pilote
- Prérequis — le moteur de table (famille MergeTree) et les clés de tri choisis avant l'ingestion
- Exécution — self-hébergé ou managé ; distribué, sharding pour le volume et réplication pour la disponibilité
- Coût — gratuit, licence Apache 2.0 ; le coût réel est l'exploitation du cluster

## Écosystème

### Alternatives

- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur.
- [[Snowflake]] — Entrepôt de données managé à stockage et calcul séparés, devenu plateforme : Snowpark exécute du Python dans le moteur, Cortex y ajoute des fonctions LLM en SQL, Snowflake ML l'entraînement et le registre de modèles ; aucun auto-hébergement. — la même analytique colonnes, mais sans cluster à opérer et sans possibilité d'auto-hébergement ; rangé en plateforme, pas en base, cf. la règle D-R8 de la taxonomie.

## Ressources

- Documentation — https://clickhouse.com/docs
- Dépôt — https://github.com/ClickHouse/ClickHouse

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases colonnes]] — ce qui départage les moteurs du dossier
