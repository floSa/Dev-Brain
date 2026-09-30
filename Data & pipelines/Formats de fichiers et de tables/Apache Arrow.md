---
role: brique
nom: Apache Arrow
alias: [arrow, pyarrow]
pitch: "Format colonnaire en mémoire et bibliothèques multi-langages pour échanger des données entre moteurs sans copie ni conversion : spécification, IPC, Flight, C++ et pyarrow (Apache-2.0)."
categorie: data/format
famille: paquet
licence_type: open-source
maturite: production
langage: C++
alternatives: []
complements: ["[[ADBC]]", "[[Parquet]]", "[[pandas]]", "[[Polars]]", "[[Spark]]", "[[DuckDB]]"]
tags: [columnar, in-memory, interoperability, serialization]
url_docs: https://arrow.apache.org/docs/
url_repo: https://github.com/apache/arrow
---

# Apache Arrow

<!-- AUTO:BANDEAU:START -->
> Format colonnaire en mémoire et bibliothèques multi-langages pour échanger des données entre moteurs sans copie ni conversion : spécification, IPC, Flight, C++ et pyarrow (Apache-2.0).

| Nature | Licence | Exécution | Maturité | Fraîcheur |
|---|---|---|---|---|
| Librairie C++ | open-source | en bibliothèque, rien à héberger | production | amont non sondé |
<!-- AUTO:BANDEAU:END -->

## Définition

Deux choses sous un nom : une **spécification** du format colonnaire en mémoire (version 1.5
du format, avec son sérialiseur IPC, l'interface C de données et Flight RPC) et les
**bibliothèques** qui l'implémentent. Le dépôt `apache/arrow` porte C++, C GLib, Python
(`pyarrow`), R et Ruby ; Rust, Go, Java, JavaScript, Julia, .NET et Swift vivent dans des dépôts
séparés, comme [[ADBC]]. La valeur est la **frontière commune** : deux moteurs qui parlent Arrow
s'échangent des colonnes sans les recopier ni les convertir. Arrow n'est ni un format de fichier
durable (c'est [[Parquet]]) ni un moteur de requête, même si `pyarrow` embarque du calcul.

## Prendre si / Écarter si

| Prendre si | Écarter si |
|---|---|
| Passer des données entre [[pandas]], [[Polars]], [[DuckDB]] et [[Spark]] sans conversion coûteuse | Il faut stocker des données sur disque ou sur stockage objet → [[Parquet]], ou un format de table ([[Apache Iceberg]]) |
| Lire et écrire du Parquet en Python ou en C++ avec `pyarrow` | Le besoin est de requêter en SQL → [[DuckDB]] ou [[Trino]], qui utilisent Arrow mais ne se réduisent pas à lui |
| Servir des données colonnaires par réseau : Flight RPC et Flight SQL | Un seul outil de bout en bout suffit : l'interop Arrow n'apporte rien à une chaîne qui ne change jamais de moteur |
| Accéder à une base en colonnes avec [[ADBC]] | Une chaîne ligne à ligne en aval : l'avantage colonnaire s'évapore |

## Mise en œuvre

- Installation — `uv add pyarrow` ; C++ et bindings Ruby ou R par leurs gestionnaires. Constaté le 2026-09-30 : pyarrow 25.0.1 (2026-08-10), 17,2k étoiles sur `apache/arrow`, une majeure tous les 2 à 3 mois
- Point d'entrée — `pyarrow` en Python ; interfaces `__arrow_c_stream__` (PyCapsule) pour échanger sans dépendre de `pyarrow` ; API C/C++ pour les moteurs
- Prérequis — Python ≥ 3.10 pour `pyarrow` 25 ; depuis pandas 3.0, `pyarrow` n'est pas obligatoire, mais le type `str` par défaut s'appuie sur lui s'il est installé
- Exécution — en bibliothèque dans le process hôte ; rien à héberger. Polars a sa propre implémentation du format et échange par PyCapsule ; Spark 4 active Arrow par défaut pour PySpark (`pyarrow` ≥ 18)
- Coût — gratuit, Apache-2.0, projet de l'Apache Software Foundation : aucune édition payante. Environ 321 millions de téléchargements `pyarrow` par mois

## Écosystème

### Alternatives

- _Aucune alternative déclarée : le format colonnaire en mémoire n'a pas de concurrent interchangeable fiché dans le brain. [[Parquet]] (sur disque) et [[Avro]] (en lignes) répondent à d'autres besoins._

### Compléments

- [[ADBC]] — Standard d'accès aux bases nativement Arrow (Arrow Database Connectivity) — l'équivalent colonnaire d'ODBC/JDBC : un jeu de drivers qui renvoient directement des données Arrow. — l'accès aux bases en Arrow natif, dans un dépôt séparé (apache/arrow-adbc).
- [[Parquet]] — Format de fichier colonnaire sur disque : stockage par colonnes, encodage et compression par colonne, statistiques par row group pour le predicate / projection pushdown ; la lingua franca de l'analytique sur stockage objet. — le format sur disque que pyarrow lit et écrit vers des structures Arrow.
- [[pandas]] — DataFrames Python de référence : Series/DataFrame en mémoire, indexation riche, group-by, jointures et séries temporelles ; le pivot de l'écosystème data Python. — pandas 3.0 : DataFrame.from_arrow() et export par __arrow_c_stream__ ; le type str s'adosse à pyarrow s'il est installé.
- [[Polars]] — DataFrames haute performance écrits en Rust sur Apache Arrow : API lazy avec optimiseur de requêtes, exécution multi-thread et moteur streaming out-of-core. — implémentation propre du format, échange par PyCapsule sans dépendre de pyarrow.
- [[Spark]] — Moteur unifié de traitement de données à grande échelle (JVM) : SQL, DataFrames, streaming structuré et MLlib sur cluster, exécution en mémoire et API PySpark. — PySpark : Arrow activé par défaut depuis Spark 4.0 pour toPandas() et les pandas UDF.
- [[DuckDB]] — Base analytique colonnes embarquée — le « SQLite de l'OLAP », SQL local sans serveur. — interroge les tables et flux Arrow et exporte ses résultats en Arrow.

## Ressources

- Documentation — https://arrow.apache.org/docs/
- Dépôt — https://github.com/apache/arrow

## Voir aussi

- [[Formats de fichiers et de tables]] — le hub du dossier
- [[OLTP, OLAP et lakehouse]] — la notion : où Arrow se place entre moteurs et stockage
- [[Avro]] — voisin : format en lignes pour l'échange de messages, à l'opposé du colonnaire
