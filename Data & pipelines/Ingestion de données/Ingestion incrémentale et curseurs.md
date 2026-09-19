---
role: notion
nom: Ingestion incrémentale et curseurs
alias: [ingestion incrémentale, incremental load, curseur, cursor, watermark, high-water mark, full refresh, attribution window, backfill incrémental]
categorie: data/ingestion
domaines: [data-eng]
tags: [data-ingestion, data-pipeline, idempotence]
---

# Ingestion incrémentale et curseurs

## Aperçu

- Charger une source **sans la relire entière** à chaque passage : le pipeline retient jusqu'où il a lu (un **curseur**) et ne demande, au passage suivant, que ce qui vient après. Le contraire est le **full refresh** : tout relire, puis remplacer ou ajouter.
- Le gain est le temps et la charge sur la source ; le prix est un **état** à conserver et une liste de cas que le curseur ne voit pas : suppressions, lignes modifiées sans que le curseur bouge, données qui arrivent après coup, reprise après un échec en cours de chargement.

## Concepts clés

### Full refresh, incrémental, et l'écriture côté cible
- Airbyte nomme un mode par deux choix : ce que la **source** lit (incrémental : « les enregistrements ajoutés depuis la dernière synchronisation » ; ou full refresh) et comment la **destination** écrit (*append*, *overwrite*, *append + dédoublonnage*). Cinq combinaisons existent ; l'incrémental ne supprime et ne modifie jamais un enregistrement existant sauf en *append + deduped*.
- Le full refresh reste juste pour une petite table, une source sans colonne fiable, ou un référentiel qu'on veut identique à la source. Il est aussi le seul mode qui « voit » une suppression sans journal.

### Curseur et état
- Un **curseur** est la valeur qui dit si une ligne est nouvelle (Airbyte : « a common example would be a timestamp from an `updated_at` column ») ; la **colonne curseur** est celle qui la porte. `dlt` en dit autant : `cursor_path`, `initial_value`, `last_value_func` (`max` par défaut).
- L'**état** est ce qu'on retient entre deux passages, et **où il vit** change l'exploitation : `dlt` le range dans la destination (table `_dlt_pipeline_state`), NiFi dans l'état du processeur (`QueryDatabaseTable`, portée cluster, colonnes à valeur maximale), Airbyte par des messages d'état (`STREAM` ou `GLOBAL`) que la plateforme persiste, Debezium dans des *offsets* (fichier, JDBC, Redis ou Kafka).
- Le mot **watermark** recouvre deux choses : la valeur maximale déjà lue (le curseur, ci-dessus) et, chez Debezium, les marques basse et haute qui encadrent un morceau de snapshot pour le recoller au flux du journal — idée de l'article DBLog (Netflix, 2020).

### Les bornes se chevauchent, à dessein
- `dlt` lit à partir de la dernière valeur **incluse** (`range_start="closed"`, défaut) : la ligne qui porte exactement la valeur du curseur revient, puis est écartée par la clé primaire ou par une empreinte du contenu. « On ne perd rien, mais on réacquiert des lignes » : c'est le principe. En borne ouverte (`"open"`), il n'y a plus de dédoublonnage.
- Airbyte, en *append*, donne une garantie « au moins une fois » : un même enregistrement peut apparaître plusieurs fois. Le dédoublonnage (*append + deduped*) trie par curseur et garde la dernière ligne par clé primaire.

### Suppressions
- Un curseur ne voit **pas** une ligne supprimée : elle n'est plus là pour porter une valeur. Airbyte le dit en creux : des enregistrements ne sont retirés en *deduped* que si la source émet des suppressions, « par exemple une source CDC ». NiFi lit les suppressions par `CaptureChangeMySQL`, jamais par `QueryDatabaseTable`. `dlt` propose un marquage `hard_delete` sur une colonne, alimenté par la source.
- Les options : journal (voir [[Change Data Capture (CDC)]], qui n'est pas répété ici), colonne de suppression logique côté source, ou full refresh périodique pour rattraper.

### Données tardives
- Trois cas différents : une ligne **modifiée** dont le curseur ne monte pas, une ligne **insérée après coup** avec un curseur ancien, et des pages **hors ordre** renvoyées par une API.
- La parade s'appelle **fenêtre d'attribution** (`lag` dans `dlt`) : « réacquérir toujours les 7 derniers jours » d'un rapport quotidien ; elle coûte une relecture, et `dlt` désactive alors le dédoublonnage par état : la cible doit fusionner par clé.
- Déclarer un ordre de lignes (`row_order`) accélère une lecture mais a un revers écrit dans la doc : si des éléments plus anciens arrivent hors ordre, la lecture s'arrête et ces éléments sont **manqués**.
- Cas propre aux bases : un `updated_at` posé au début d'une transaction et validé après une transaction plus récente laisse une ligne sous le curseur déjà avancé. Aucune des documentations lues ne le traite ; le mécanisme est décrit dans des billets d'ingénieurs (Celonis Engineering), dont le lien est redirigé et n'a pas été relu à la source.

### Reprise après échec
- L'état ne doit avancer **qu'après** le chargement réussi, sinon un plantage saute des lignes pour toujours. `dlt` reprend un pipeline interrompu au **paquet de chargement** en cours, sans doublon ; Airbyte checkpointe par messages d'état ; Debezium Engine livre « au moins une fois » et vide ses offsets toutes les 60 s par défaut.
- Le rejeu est donc normal : c'est à la cible de le supporter, par écriture par clé (`merge`, `upsert`) plutôt que par insertion aveugle — cf. [[ELT vs ETL & idempotence]].

### Backfill
- Recharger un intervalle passé sans toucher à l'état : `dlt` accepte un `end_value`, qui **désactive l'état** et permet un backfill parallèle à l'incrémental ; les gros intervalles se découpent en morceaux.

## En pratique

- Partir de la question « comment sait-on qu'une ligne a changé, et qu'une ligne a disparu ? » avant de choisir un outil : colonne fiable et monotone ? journal lisible ? clé primaire ? Sans colonne curseur, le full refresh ou le CDC sont les seules voies.
- Poser une petite fenêtre de recouvrement plutôt qu'un curseur strict, et fusionner par clé côté cible : c'est la combinaison qui absorbe à la fois les lignes tardives et les rejeux.
- Mesurer la **fraîcheur** et le **compte de lignes** contre la source, à intervalle régulier : un curseur qui a dérivé ne lève aucune erreur — voir [[Contrats de données & qualité]].
- Prévoir le full refresh de rattrapage : hebdomadaire ou à la demande, pour les suppressions et les corrections rétroactives.
- Pièges : curseur sur une colonne non monotone ; état avancé avant l'écriture ; suppressions oubliées ; borne ouverte sans clé unique ; fuseaux horaires mélangés dans un `updated_at`.

## Approches voisines & alternatives

- [[Change Data Capture (CDC)]] — la lecture du journal, qui règle les suppressions et l'ordre au prix d'un accès au log.
- [[ELT vs ETL & idempotence]] — la propriété qui rend un rejeu sans danger.
- [[Contrats de données & qualité]] — vérifier fraîcheur et volumétrie d'un chargement.
- [[Dagster]] et [[Airflow]] — les partitions et les intervalles de données qui servent d'unité de rejeu.
- [[dlt]] — curseurs, `lag`, `end_value`, état dans la destination.
- [[Airbyte]] — cinq modes de synchronisation, état par messages, CDC pour les suppressions.
- [[Debezium]] — offsets, snapshots incrémentaux à marques, livraison au moins une fois.
- [[Apache NiFi]] — colonnes à valeur maximale conservées dans l'état du processeur.

## Pour aller plus loin

- Airbyte, *Sync modes* — https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes (les cinq modes) ; *Incremental Sync - Append* et *Append + Deduped* dans la même section.
- dlt, *Cursor-based incremental loading* — https://dlthub.com/docs/general-usage/incremental/cursor et *Lag / Attribution window* — https://dlthub.com/docs/general-usage/incremental/lag
- Apache NiFi, processeur `QueryDatabaseTable` — https://nifi.apache.org/components/org.apache.nifi.processors.standard.QueryDatabaseTable/
- Debezium, *Debezium Server* et connecteur PostgreSQL (snapshots incrémentaux) — https://debezium.io/documentation/reference/stable/operations/debezium-server.html
- Andreas Andreakis et Ioannis Papapanagiotou (Netflix), *DBLog: A Watermark Based Change-Data-Capture Framework*, arXiv:2010.12597 (2020) — https://arxiv.org/abs/2010.12597
