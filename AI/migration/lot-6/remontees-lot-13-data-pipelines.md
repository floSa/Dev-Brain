---
role: meta
nom: remontees-lot-13-data-pipelines
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées du lot 13 : « Data & pipelines/ », niveau domaine

Périmètre : les **11** fiches `role: brique` posées directement dans « Data & pipelines/ »,
sans sous-dossier — Apache Iceberg, Avro, Faker, Flink, Mimesis, Parquet, SDV, connectorx,
missingno, sweetviz, ydata-profiling. Le compte annoncé par la table du brief est le compte
réel. Branche `claude/lot-13-data-pipelines-0bb213`.

Aucun fichier partagé touché, rien de régénéré, `cloturer-brain` non appelé.

## 1. Trois fiches sur onze sont membres d'une vue `.base` — huit ne le sont pas

Mesuré avec `AI/migration/scripts/mesure_membres_bases.py`, et recoupé à la main sur le
`.base` lui-même (filtre `role == "brique"` **et** `categorie == "data/eda"`) :

| Fiche | Membre d'une vue | Conséquence sur `Écarter si` |
|---|---|---|
| missingno, sweetviz, ydata-profiling | `Comparatif - Outils EDA - profiling` | bornes dures **seules** ; les renvois croisés vivent déjà au comparatif |
| Apache Iceberg, Avro, Parquet | aucune | les renvois **restent** en `Écarter si`, avec leur wikilink |
| Faker, Mimesis, SDV | aucune | idem |
| Flink | aucune | idem |
| connectorx | aucune | idem |

Le cas des huit n'est pas le cas 3 de la règle 2 (« la brique est membre, la cible ne l'est
pas ») mais le cas 1 : **aucun comparatif n'existe pour leur catégorie**. `check_brain` le dit
déjà de son côté, en R8a, pour `data/format` (3 briques) et `data/synthetique` (3 briques) —
deux avertissements qui préexistent au lot 13 et que la conversion ne referme pas.

Les trois membres, eux, sont l'application propre de la règle 2 : les renvois croisés
`ydata-profiling` / `sweetviz` / `missingno` sont portés mot pour mot par la section
« Ce qui départage » du comparatif, écrite au lot 5. Aucune de ces puces n'a été recopiée en
`Écarter si` ; **aucune n'a été perdue**.

Conséquence directe : **32 cellules `Écarter si` sur 53 ne portent aucun wikilink**. Dix
viennent des trois membres du comparatif — les quatre de missingno, les trois de sweetviz,
les trois de ydata-profiling, toutes des bornes dures sans renvoi. Les vingt-deux autres sont
les bornes dures des huit fiches sans comparatif, qui cohabitent dans la même colonne avec
leurs renvois. C'est la cession assumée du critère « un wikilink dans chaque cellule
`Écarter si` ».

## 2. `data/format` et `data/synthetique` méritent chacune un comparatif

Constat de conversion, pas de rangement. Les six fiches concernées se départagent sur **un
seul axe chacune**, énoncé identiquement des deux côtés :

- `data/format` — [[Parquet]] contre [[Avro]] : colonnaire contre ligne, et [[Apache Iceberg]]
  au-dessus des deux, qui n'est pas un format de fichier mais une sémantique de table. Trois
  briques, trois rôles distincts, dont aucun n'est vraiment l'alternative de l'autre.
- `data/synthetique` — [[Faker]] contre [[Mimesis]] : même mécanisme (tirage par règles),
  écosystème contre vitesse. [[SDV]] est ailleurs : il apprend une distribution.

Un comparatif de trois membres fermerait les deux R8a et permettrait de sortir six renvois
des cellules `Écarter si`. C'est un travail de **lot 5**, pas de lot 6 : je le signale, je ne
le fais pas (règle 1 — pas de comparatif).

## 3. `complements:` — une seule moitié de couple posée, et pourquoi les autres non

Une seule paire du périmètre passe le test de la règle 3 (appariement énoncé comme une
recommandation, dans les deux sens) :

| Fiche | Complément | Dossier de la cible | Lot qui fermera l'autre moitié |
|---|---|---|---|
| `connectorx` | [[Polars]] | Data & pipelines/DataFrames/ | **lot 12** |

`connectorx` énonce l'appariement : « c'est le moteur derrière `read_database(engine=
"connectorx")` ». La fiche `Polars` ne le mentionne nulle part — ni en corps, ni en
frontmatter. La moitié est donc posée de mon côté (`complements: ["[[Polars]]"]`) et
**inscrite ici** : c'est au lot 12, ou à l'intégration, d'écrire `complements:
["[[connectorx]]"]` sur Polars et de citer connectorx dans sa section `### Compléments`.

Trois appariements ont été examinés et **écartés**, chacun pour une raison qui vaut d'être
gardée :

- **Apache Iceberg / Parquet.** L'appariement est réel et mutuel — les données d'une table
  Iceberg vivent en Parquet, et Parquet gagne sa sémantique de table par Iceberg. Il est
  pourtant impossible à poser : sur **chacune** des deux pages, l'autre figure déjà en
  `Écarter si` (« un simple fichier sans sémantique de table → [[Parquet]] seul » ;
  « besoin de sémantique de table → [[Apache Iceberg]] »), et la règle 2 dit que ces puces
  y **restent** faute de comparatif d'accueil. Les poser aussi en `### Compléments` créerait
  la double citation que la règle 8 de la spec interdit *en dur*. **La règle 2 et le champ
  `complements:` sont donc en concurrence directe** dès que deux briques se départagent
  *et* se composent. C'est le premier cas mesuré ; il en viendra d'autres (Iceberg / Avro
  tombe exactement pareil).
- **Flink / Apache Iceberg.** Flink énonce Iceberg comme « cible d'écriture fréquente », mais
  Iceberg nomme quatre moteurs à égalité (Spark, Trino, Flink, DuckDB). C'est la forme
  exacte que la règle 3 exclut — le « MLflow s'intègre à PyTorch, Scikit-Learn, XGBoost,
  Optuna » du lot 5. Non posé.
- **Faker / pandas.** `AI/design/brain-v3.md` §6 donne ce couple en exemple du gabarit
  (« [[pandas]] — pour matérialiser les tirages en DataFrame »). La fiche Faker **ne
  mentionne pandas nulle part**. Poser le couple aurait été l'inventer. Non posé — et
  l'exemple de la spec reste, pour l'instant, sans source dans le vault.

## 4. Où sont parties les 40 puces de `Pièges`

Aucune supprimée. Décompte par destination :

| Destination | Puces |
|---|---|
| `Écarter si`, comme borne dure de la brique | 33 |
| `## Définition` (limite qui n'oriente pas un choix) | 4 |
| `## Mise en œuvre`, étiquette `Prérequis` | 3 |

Les quatre qui montent en `## Définition` sont celles qui décrivent **ce que la brique est**,
pas un cas où l'écarter : l'immutabilité d'un fichier Parquet, l'obligation d'évaluer la
fidélité d'un jeu SDV, le fait que connectorx charge sans écrire, le fait que missingno décrit
la nullité sans la traiter.

Les trois qui atterrissent en `Mise en œuvre` sont un cas que le brief ne prévoyait pas : ce
sont des **prérequis déguisés en pièges**, pas des limites. Ce sont, exactement — « les
versions de spec v1 / v2 / v3 ne sont pas également supportées par les moteurs » (Iceberg),
« la migration Flink 1.x → 2.0 n'est pas triviale » et « tuning mémoire JVM » (Flink). Leur
place naturelle est `Prérequis` : ce sont des choses à vérifier **avant** de s'engager, pas
des raisons d'écarter la brique. **Quatrième destination à ajouter à l'étape 3 du brief.**

Sept puces ont par ailleurs **fusionné** avec une cellule déjà écrite plutôt que d'ouvrir une
ligne à elles seules — « schémas JSON verbeux » rejoint « les règles de compatibilité se
respectent » sur Avro, « écosystème d'extensions plus restreint » rejoint « pas un
remplacement drop-in » sur Mimesis, et ainsi de suite. Elles sont comptées à leur destination,
pas perdues.

## 5. Cinq doubles citations, toutes de la même forme

| Fiche | Cible citée deux fois |
|---|---|
| Avro | [[Parquet]] |
| Parquet | [[Avro]] |
| Faker | [[Mimesis]] |
| Mimesis | [[Faker]] |
| connectorx | [[ADBC]] |

Toujours le même mécanisme : la cible est dans `alternatives:` — donc **R11 l'exige en dur**
dans `### Alternatives`, avec son pitch — et elle porte aussi le renvoi de `Écarter si`, que
la règle 2 y maintient faute de comparatif. Les deux contraintes sont dures et
contradictoires ; la règle 2 l'emporte, comme le brief le prévoit. À noter pour la réécriture
du critère au lot 8 : **la double citation n'est pas un accident de rédaction, elle est
structurelle** partout où une catégorie n'a pas de comparatif.

## 6. Treize cellules vides, jamais comblées

`Apache Iceberg`, `Faker`, `Flink`, `connectorx` — 2 chacune ; `Avro`, `Parquet`, `SDV`,
`sweetviz`, `ydata-profiling` — 1 chacune. `Mimesis` et `missingno` équilibrent le leur.

**Onze sont du côté `Prendre si`** : les huit fiches sans comparatif ont plus de limites
documentées que de cas d'usage, parce que leurs renvois vers un concurrent restent chez elles.
Les **deux** autres sont du côté `Écarter si`, sur `sweetviz` et `ydata-profiling` — les deux
seules fiches du lot qui ont quatre usages nets pour trois bornes propres. Rien n'a été
inventé pour équilibrer, dans un sens comme dans l'autre.

## 7. Trois fiches sans `alternatives:` — la prose hors brain a été gardée

`Apache Iceberg`, `Flink` et `SDV` ont `alternatives: []`. Leur ancienne section
`## Alternatives` ne portait pas des wikilinks mais **une phrase sur les concurrents hors
brain** — Delta Lake et Apache Hudi pour Iceberg, Spark Structured Streaming et Kafka Streams
pour Flink. Cette information n'a d'accueil nulle part ailleurs : elle est conservée telle
quelle, en une puce sous `### Alternatives`. La règle 6 (réinjection du pitch) ne s'y applique
pas — `check_brain` exempte explicitement les puces hors `alternatives:`.

C'est aussi ce qui déclenche la règle 4 du validateur (voisinage déclaré, souple) sur ces
trois fiches. Rien à corriger côté conversion.

## 8. `Apache Iceberg` porte un alias en doublon — hors périmètre de la conversion

`alias: [Iceberg, iceberg]` : `check_brain` le signale en R5 (« alias en doublon interne »),
avant comme après. C'est du **frontmatter**, et la consigne du lot 6 est de n'y toucher que
pour `complements:`. Non corrigé, signalé. Le correctif tient en un mot — supprimer
`iceberg` de la liste.

## 9. Le compte d'avertissements de la branche : 149 → 145

Quatre R15 fermés, et rien d'autre — vérifié par `diff` des deux relevés complets :
`Apache Iceberg`, `Avro`, `Parquet` et `connectorx` ne portaient **aucun** lien vers une
notion ou un hub en v2 ; le nouveau `## Voir aussi` en pose deux ou trois chacun. Les sept
autres fiches en portaient déjà un. Aucun avertissement ajouté, aucune violation dure,
`check_arbo` inchangé.

C'est la confirmation du point 5 du protocole : le nouveau gabarit **ferme** des R15, parce
que `## Voir aussi` force à nommer la notion parente au lieu de la laisser au hasard d'une
puce de `## Liens`.

## 10. `## Retours` créée nulle part

Conforme : aucune entrée datée dans les onze fiches. La seule du vault reste
`LLM & IA générative/Agents de code/t3code.md`, du ressort du lot 7.
