---
role: meta
nom: remontees-bdd-domaine
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6-1 — remontées de la conversion « Bases de données », niveau domaine

Périmètre : les **17** `role: brique` posées directement dans « Bases de données/ » — ADBC,
Alembic, Apache Cassandra, ClickHouse, DuckDB, Flyway, InfluxDB, Liquibase, MongoDB,
Nebula Graph, Neo4j, Prisma, Redis, SQLAlchemy, SQLModel, TimescaleDB, psycopg2. Ni les
sous-dossiers (`Vectoriel/`, `Administration/`, `Relationnel/`, `Recherche/`), ni le hub, ni
les deux notions du dossier, ni les six comparatifs.

Branche `claude/lot-6-databases-conversion-1209d0`, sur `main` = `90d46a2`.

Écart mesuré sur cette branche : `check_brain.py` passe de **149 à 147 avertissements**,
aucune violation dure, aucun avertissement nouveau. Les deux fermés sont R15 sur `ADBC` et
`psycopg2` — leur ancienne section `## Liens` ne pointait vers aucune notion ni aucun hub,
leur `## Voir aussi` pointe désormais le hub du domaine. `check_arbo.py` inchangé, vert.

## 1. Les trois noms de la section déploiement : 17 sur 17 portent le premier

Les trois ont été cherchés par script, avant et après.

| Section | Fiches du périmètre |
|---|---|
| `## Déploiement & coût` | **17** |
| `## Bases & plateformes` | 0 |
| `## Installation & plateformes` | 0 |

Le dossier est donc homogène, et la vigilance de la remontée 3 du pilote n'a rien attrapé
ici. Elle reste justifiée : c'est de l'avoir cherchée qui permet de l'affirmer, pas de
l'avoir supposé.

## 2. Les puces « besoin → concurrent » : 39 sur 48, soit 81 %

Mesure sur les 17 fiches avant conversion : `## Quand NE PAS l'utiliser` portait **48**
puces, dont **39 de la forme « besoin → [[concurrent]] »**. En face, `## Pièges` en portait
**53**.

Aucune des 39 n'a été recopiée telle quelle en `Écarter si`. La grande majorité est déjà
portée par l'un des **six comparatifs du dossier** — Bases NoSQL, Bases colonnes, Bases
graphes, Bases temporelles, Migrations de schéma, ORM — écrits au lot 5. Ce qui reste en
`Écarter si` est une **borne dure de la brique seule**, formulée sans redirection.

**Aucun wikilink dans les cellules `Écarter si`**, comme au pilote et pour la même raison :
la règle dure nº 5 du lot 8 en voudra un, mais s'y conformer d'avance imposerait de réécrire
les bornes sous la forme comparative que la remontée 20 du lot 5 condamne. Le critère
d'acceptation « chaque cellule `Écarter si` contient un wikilink » du brief est donc
**délibérément non tenu**, et c'est le seul.

### 2 bis. Cinq redirections n'avaient de destination nulle part

Ce sont des redirections **inter-familles**, qui disent « ce n'est pas une base de ce
type-là ». Elles ne sont ni une borne de la brique, ni un discriminant d'un comparatif du
dossier : aucun comparatif du vault n'oppose les familles de bases entre elles.

| Fiche | Puce d'origine |
|---|---|
| `InfluxDB` | Données relationnelles, jointures et transactions ACID → [[Postgres]] |
| `InfluxDB` | Analytique colonne haute cardinalité non strictement temporelle → [[ClickHouse]] |
| `Nebula Graph` | Données peu connectées, modèle tabulaire et transactions classiques → [[Postgres]] |
| `Neo4j` | Données tabulaires peu reliées, transactions classiques → [[Postgres]] |
| `TimescaleDB` | Analytique colonne massive non temporelle → [[ClickHouse]] |

Elles sont **consignées ici, non reportées** — même traitement que la remontée 8 du pilote :
leur place serait le hub « Bases de données » ou un comparatif transverse des familles, et
une conversation de conversion ne touche ni l'un ni l'autre (règle 1).

> **À trancher pour la suite** : le vault n'a aucun comparatif qui départage les *familles*
> de bases — relationnel, document, clé-valeur, colonne, graphe, temporel, vectoriel. Chaque
> comparatif départage les moteurs *à l'intérieur* d'une famille. Le choix de famille est
> pourtant la première décision, et il est aujourd'hui dispersé en redirections
> « → [[Postgres]] » sur huit fiches. C'est un chantier de contenu, pas de format : hors
> lot 6.

## 3. Destination des 53 puces de `## Pièges` — aucune supprimée

- **48** vers la colonne `Écarter si` : ce sont des bornes dures, formulées sans redirection.
- **5** vers `## Définition`, parce qu'elles n'orientent aucun choix mais structurent la
  compréhension : la chaîne colonnaire de bout en bout (`ADBC`), le moteur de table MergeTree
  et les clés de tri (`ClickHouse`), « schéma libre n'est pas absence de schéma » (`MongoDB`),
  « penser table plutôt que relation » (`Neo4j`), le dimensionnement de l'intervalle de chunk
  (`TimescaleDB`).
- **0** vers `## Retours` : aucune entrée datée dans le périmètre, conforme au brief. La seule
  du vault est du ressort du lot 7.

## 4. Cellules laissées vides — le compte exact

Le tableau ne s'équilibre pas, et il n'a pas été rempli pour l'équilibrer.

| Colonne | Cellules vides | Fiches |
|---|---|---|
| `Écarter si` | **7** | ClickHouse (2), puis ADBC, DuckDB, MongoDB, Prisma, TimescaleDB (1 chacune) |
| `Prendre si` | **4** | Apache Cassandra, Nebula Graph, SQLAlchemy, SQLModel (1 chacune) |

`ClickHouse` est le cas le plus net : sur trois exclusions d'origine, deux étaient de la forme
« besoin → concurrent » et sont au `Comparatif - Bases colonnes` ; il ne lui reste que deux
bornes propres, les mutations asynchrones et la cohérence éventuelle de la réplication.

Les quatre cellules `Prendre si` vides sont l'inverse : quatre fiches ont plus de raisons de
les écarter que de les prendre — les deux bases distribuées, dont l'exploitation du cluster
est le vrai coût, et les deux ORM Python, qui portent chacun quatre bornes techniques.

## 5. `complements:` — huit fiches ouvertes, six moitiés de couple à refermer

Quatre couples sont **entièrement dans le périmètre** et donc posés dans les deux sens :

| Fiche | Complément posé | Sens inverse |
|---|---|---|
| `Alembic` | [[SQLAlchemy]], [[SQLModel]] | posé sur les deux |
| `SQLAlchemy` | [[Alembic]], [[psycopg2]] | posé sur les deux |
| `psycopg2` | [[SQLAlchemy]] | posé |
| `SQLModel` | [[Alembic]] | posé |

Six pointent **hors du périmètre**. La moitié est posée sur ma fiche ; **l'autre moitié
reste à poser**, par le lot qui convertira la cible :

| Fiche du lot 1 | Complément posé | Dossier de la cible | Lot qui refermera |
|---|---|---|---|
| `MongoDB` | [[MongoDB Compass]] | Bases de données/Administration/ | **pilote — déjà converti** |
| `Redis` | [[Redis Insight]] | Bases de données/Administration/ | **pilote — déjà converti** |
| `TimescaleDB` | [[Postgres]] | Bases de données/Relationnel/ | lot 2 |
| `psycopg2` | [[Postgres]] | Bases de données/Relationnel/ | lot 2 |
| `ADBC` | [[Polars]] | Data & pipelines/DataFrames/ | lot 12 |
| `DuckDB` | [[pandas]], [[Polars]] | Data & pipelines/DataFrames/ | lot 12 |

> **Cas particulier, à traiter à l'intégration.** Les deux premières lignes ferment les
> couples que la remontée 5 du pilote laissait ouverts pour le lot 1 — mais les cibles
> `MongoDB Compass` et `Redis Insight` sont **déjà converties**, avec `complements: []`, et
> elles vivent dans `Administration/`, hors de mon périmètre : la règle 1 m'interdit d'y
> écrire. Aucun lot restant ne les reprendra. C'est donc à la **conversation d'intégration**
> de poser ces deux moitiés — ce sont les deux seules arêtes du vault dont aucun lot n'est
> propriétaire.

Les deux moitiés vers `Postgres` restent du ressort du lot 2, avec les trois que le pilote
lui a déjà laissées : `pgvector`, `MySQL Workbench`, `pgAdmin`.

## 6. `SQLAlchemy` est à la fois le socle et l'alternative de `SQLModel`

SQLModel est bâti **sur** SQLAlchemy — c'est un complément au sens strict — et s'utilise
**à sa place** — c'est une alternative, déclarée comme telle dans le frontmatter depuis le
lot 2, et le `Comparatif - ORM` la départage. Le critère « aucune cible n'apparaît dans deux
sections de la même page » tranche : SQLAlchemy reste **en alternative seulement**, sur les
deux fiches, et le rapport de dépendance est dit dans la `## Définition` de SQLModel, en
texte nu.

C'est le seul endroit du périmètre où les deux axes d'`alternatives:` et de `complements:` se
recouvrent réellement. Le cas se reposera : une brique construite sur une autre et capable de
la remplacer n'est pas rare.

## 7. Recouvrement assumé entre la fiche et le comparatif du dossier

Application de l'arbitrage demandé : un fait qui est à la fois le discriminant du comparatif
et une borne dure de la brique **reste sur la fiche**. Treize cas dans le périmètre.

| Fait | Fiche, `Écarter si` | Comparatif |
|---|---|---|
| mutations asynchrones, modèle pensé append | ClickHouse | Bases colonnes |
| RAM et disque local bornent le volume | DuckDB | Bases colonnes |
| `$lookup` ne remplace pas une jointure | MongoDB | Bases NoSQL |
| mono-thread, une commande coûteuse bloque | Redis | Bases NoSQL |
| Community mono-instance, montée en charge verticale | Neo4j | Bases graphes |
| partitions figées à la création | Nebula Graph | Bases graphes |
| multi-nœuds distribué abandonné | TimescaleDB | Bases temporelles |
| cardinalité des séries, facteur de coût | InfluxDB | Bases temporelles |
| autogénération qui ne détecte pas tout | Alembic | Migrations de schéma |
| undo réservé aux éditions payantes | Flyway | Migrations de schéma |
| couche d'abstraction en plus | Liquibase | Migrations de schéma |
| pré-1.0, n'expose qu'une partie de l'API | SQLModel | ORM |
| client Python communautaire | Prisma | ORM |

Treize sur 17 fiches — bien au-delà des 3 sur 18 du pilote. La raison est structurelle : le
dossier porte **six** comparatifs pour 17 fiches, contre un seul pour onze au pilote. Plus un
dossier est comparé finement, plus le discriminant et la borne coïncident. Les formulations
restent distinctes — la fiche dit ce qui va mordre, le comparatif dit ce qui fait choisir —
mais ce sont bien treize endroits à tenir d'accord.

## 8. Les bandeaux sont complets — aucun trou de frontmatter

`build_bandeau.py`, lancé borné aux 17 fichiers, n'a signalé **aucune cellule vide** : les 17
portent `famille:`, `licence_type:`, de quoi dériver l'exécution, et `maturite:`.

Contraste net avec la remontée 6 du pilote, où les sept `famille: application`
d'`Administration/` n'avaient pas de `maturite:`. L'hypothèse du pilote — « le champ n'a
peut-être jamais été rempli pour cette famille » — n'est **pas** contredite ici : le périmètre
ne contient aucune `famille: application`. La vérification reste à faire par les lots qui en
portent.

## 9. `psycopg2` porte une `## Alternatives` sans cible déclarée

`alternatives: []` au frontmatter, et une section qui dit en toutes lettres que le successeur
`psycopg 3` et l'alternative async `asyncpg` ne sont pas encore fichés. La phrase est
conservée telle quelle sous `### Alternatives`. Ce n'est pas l'un des trois cas de la
remontée 11 du pilote — la section existe, c'est la liste du frontmatter qui est vide — et
R11 le tolère, n'ayant aucune cible à couvrir.

Deux fiches à créer y sont donc nommées : **psycopg 3** et **asyncpg**. C'est du contenu, pas
du format : à verser au backlog d'enrichissement, hors lot 6.
