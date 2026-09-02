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
complements: []
tags: [columnar, olap, embedded]
url_docs: https://duckdb.org/docs/
url_repo: https://github.com/duckdb/duckdb
---

# DuckDB

## Pourquoi

Base analytique **in-process** (embarquée), le « SQLite de l'OLAP ». Pas de serveur : elle tourne dans le process hôte (Python, R, CLI). Stockage **colonnes** et exécution **vectorisée**, sans dépendances (un compilateur C++17 suffit). Lit directement Parquet, CSV et JSON, et s'intègre à pandas, Polars et Arrow. Licence MIT, garantie à perpétuité par la DuckDB Foundation.

## Quand l'utiliser

- Analytique locale et exploration de données sur un poste (data science, notebooks).
- Requêter des fichiers Parquet / CSV / JSON en SQL sans monter d'infra.
- ETL léger et transformations au sein d'un pipeline Python.
- Tests et prototypes analytiques jetables.

## Quand NE PAS l'utiliser

- Service analytique multi-utilisateur, distribué, sur gros cluster → [[ClickHouse]].
- OLTP et écritures concurrentes transactionnelles → [[Postgres]].
- Volumes dépassant une machine ou besoin de haute disponibilité.

## Déploiement & coût

- Pas de déploiement : bibliothèque liée au process, base en mémoire ou fichier unique.
- Single-node, mais exploite tous les cœurs locaux.
- MIT, gratuit ; option managée cloud via MotherDuck.

## Pièges

- Pensée mono-process / un seul écrivain (comme SQLite côté concurrence).
- Pas conçue pour servir des milliers de clients simultanés.
- Tient sur une machine : la RAM et le disque local bornent le volume.

## Alternatives

- [[ClickHouse]] — SGBD colonnes distribué pour l'analytique temps réel : agrégations massives à très faible latence.

## Liens

- [[Bases de données]] — le concept (Wiki)
- [[Comparatif - Bases colonnes]] — comparatif des moteurs colonne / OLAP
- Doc : https://duckdb.org/docs/
