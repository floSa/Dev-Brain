---
role: brique
nom: DuckDB
alias: [duckdb]
pitch: "Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur."
categorie: database/analytique
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: ["[[ClickHouse]]"]
complements: ["[[pandas]]", "[[Polars]]"]
tags: [columnar, olap, embedded]
url_docs: https://duckdb.org/docs/
url_repo: https://github.com/duckdb/duckdb
---

# DuckDB

<!-- AUTO:BANDEAU:START -->
> Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur.

| Nature | Licence | Exécution | Maturité |
|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production |
<!-- AUTO:BANDEAU:END -->

## Définition

Base analytique **in-process**, le « SQLite de l'OLAP » : pas de serveur, elle tourne dans le
process hôte — Python, R, ou la ligne de commande. Stockage en **colonnes** et exécution
**vectorisée**, sans dépendance externe : un compilateur C++17 suffit à la bâtir. Elle
requête directement des fichiers Parquet, CSV et JSON, sans étape de chargement préalable, et
s'interface avec pandas, Polars et Arrow. La base est soit en mémoire, soit un fichier unique.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Analytique locale et exploration sur un poste : data science, notebooks | Un seul écrivain à la fois, comme SQLite : les écritures concurrentes transactionnelles ne passent pas |
| Requêter des fichiers Parquet, CSV ou JSON en SQL sans monter d'infra | Elle tient sur une machine : la RAM et le disque local bornent le volume |
| ETL léger et transformations au sein d'un pipeline Python | Elle n'est pas conçue pour servir des milliers de clients simultanés, ni pour la haute disponibilité |
| Tests et prototypes analytiques jetables | |

## Mise en œuvre

- Installation — `uv add duckdb` ; aucune dépendance externe à installer
- Point d'entrée — SQL depuis Python, R ou la CLI ; requêtes directes sur Parquet, CSV et JSON
- Prérequis — aucun serveur ; la base est en mémoire ou dans un fichier unique
- Exécution — dans le process appelant, single-node, mais tous les cœurs locaux sont exploités
- Coût — gratuit, licence MIT garantie à perpétuité par la DuckDB Foundation ; option managée via MotherDuck

## Écosystème

### Alternatives

- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence.

### Compléments

- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python. — intégration directe, dans les deux sens.
- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core. — intégration directe via Arrow.

## Ressources

- Documentation — https://duckdb.org/docs/
- Dépôt — https://github.com/duckdb/duckdb

## Voir aussi

- [[Bases de données]] — le hub du domaine
- [[Comparatif - Bases colonnes]] — ce qui départage les moteurs du dossier
