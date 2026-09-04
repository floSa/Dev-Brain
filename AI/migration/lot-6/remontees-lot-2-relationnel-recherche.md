---
role: meta
nom: remontees-lot-2-relationnel-recherche
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 / lot 2 — remontées : « Bases de données/Relationnel/ » et « Bases de données/Recherche/ »

Périmètre annoncé par la table du découpage : 12 fiches. **12 trouvées, 12 converties** —
`CockroachDB`, `MariaDB`, `Microsoft SQL Server`, `MySQL`, `Postgres`, `SQLite` d'un côté ;
`Elasticsearch`, `Marqo`, `Vespa`, `bm25s`, `rank-bm25`, `txtai` de l'autre. Le compte de la
table est juste.

Branche `claude/lot-2-databases-search-3a7ffa`. Aucune régénération d'index, aucun appel à
`cloturer-brain`, aucun fichier partagé modifié — `build_bandeau.py` a été **lancé**, borné aux
deux dossiers, jamais édité.

Écart des validateurs, mesuré avant et après sur cette branche : `check_brain.py` **0 dur,
149 avertissements** dans les deux cas, dont **aucun** sur les 15 fiches touchées ;
`check_arbo.py` vert dans les deux cas. La conversion n'a donc rien ouvert ni rien fermé côté
validateur, ce qui est attendu : elle ne touche qu'au corps.

## 1. Les cinq paires `complements:` du pilote — trois fermées, deux hors périmètre

La consigne reçue disait que ces deux dossiers ferment **les cinq** paires laissées ouvertes
par le pilote. Ce n'est pas le cas, et la table du pilote le dit déjà : deux des cinq visent
`MongoDB` et `Redis`, qui sont au **niveau domaine** de « Bases de données/ », c'est-à-dire le
**lot 1**. Le lot 2 en ferme trois.

| Paire | Statut | Où |
|---|---|---|
| `pgvector` ↔ `Postgres` | **fermée, dans les deux sens** | Vectoriel/ ↔ Relationnel/ |
| `pgAdmin` ↔ `Postgres` | **fermée, dans les deux sens** | Administration/ ↔ Relationnel/ |
| `MySQL Workbench` ↔ `MySQL` | **fermée, dans les deux sens** | Administration/ ↔ Relationnel/ |
| `MongoDB Compass` ↔ `MongoDB` | **ouverte** | Administration/ ↔ niveau domaine → **lot 1** |
| `Redis Insight` ↔ `Redis` | **ouverte** | Administration/ ↔ niveau domaine → **lot 1** |

Fermer « dans les deux sens » a demandé d'écrire dans **trois fiches hors des deux dossiers
assignés** — `pgvector.md`, `pgAdmin.md`, `MySQL Workbench.md` — ce que la règle 1 du protocole
parallèle interdit. C'est assumé, pour deux raisons : le pilote a explicitement délégué ces
couples aux lots 1 et 2 (« c'est aux lots 1 et 2 de fermer ces couples, dans les deux sens »),
et ses deux dossiers sont **clos et poussés** — aucune conversation parallèle ne les tient
ouverts. L'écriture s'y limite au champ `complements:` et au bloc `### Compléments` ; le reste
du corps n'a pas été touché.

> Effet de bord repéré en le faisant : `pgAdmin` et `MySQL Workbench` portaient déjà
> `[[Postgres]]` et `[[MySQL]]` en `## Voir aussi`. Poser la même cible en `### Compléments`
> aurait violé « aucune cible dans deux sections de la même page ». La ligne a donc été
> **déplacée**, pas dupliquée. Les lots qui fermeront `MongoDB Compass` et `Redis Insight`
> rencontreront exactement le même cas.

## 2. Le brief et le pilote se contredisent sur la moitié de couple — le pilote a été suivi

Le brief (étape 4, et la note sous la table du découpage) dit qu'une conversation qui vise une
fiche hors de son périmètre « pose sa moitié, et inscrit l'autre dans ses remontées ». Le
pilote a fait l'inverse et l'a justifié : « la réciprocité étant obligatoire, poser la moitié
du couple aurait laissé les cinq fiches cibles en faute ».

C'est le pilote qui a été suivi, pour l'unique paire concernée ici :

| Fiche | Complément sourcé | Dossier de la cible | Lot |
|---|---|---|---|
| `txtai` | [[sentence-transformers]] — « socle d'embeddings sous-jacent » | Machine Learning/ | lot 6 |

`txtai.complements` reste donc **vide**, et le couple est à fermer par le lot qui convertira
`sentence-transformers`. À trancher pour les seize autres conversations : c'est le brief ou le
pilote qui a raison, pas les deux. La réciprocité n'est **pas** contrôlée par `check_brain.py`
— rien ne rattrapera une moitié orpheline.

## 3. Où sont parties les puces — le compte

**36 puces `## Pièges`** (3 par fiche, sur les 12) : **36 en `Écarter si`**, aucune en
`## Définition`, **aucune datée** — donc aucune section `## Retours` créée, conformément au
brief.

**37 puces `## Quand NE PAS l'utiliser`** : **8 recopiées** en `Écarter si`, **29 laissées au
comparatif du dossier**, où elles étaient déjà. Le détail par dossier est net et vaut d'être
noté :

| Dossier | Puces d'exclusion | Recopiées | Laissées au comparatif |
|---|---|---|---|
| Relationnel/ | 18 | **0** | 18 (100 %) |
| Recherche/ | 19 | 8 | 11 (58 %) |

Les 18 de Relationnel sont **toutes** de la forme « besoin → concurrent », et les six lignes de
`Comparatif - Bases relationnelles` les portent toutes. Application directe de la remontée 7 du
pilote, et confirmation de sa mesure à 89 % : sur un dossier où les six briques sont
mutuellement alternatives, le taux monte à 100 %.

Les 8 recopiées de Recherche/ sont celles qui **pointent hors du dossier**, et que le
comparatif du dossier ne peut donc pas porter : [[ClickHouse]] et [[Postgres]] pour
`Elasticsearch`, [[Elasticsearch]] et [[sentence-transformers]] pour `bm25s` et `rank-bm25`,
plus la borne « stack non-Python » de `txtai` et « projet non maintenu » de `Marqo`.

> Conséquence méthodologique pour les seize autres : la question n'est pas « est-ce de la forme
> besoin → concurrent ? » mais « le comparatif **de ce dossier** la porte-t-il ? ». Une
> exclusion qui pointe vers une brique d'un autre dossier n'a **aucun** comparatif pour la
> recevoir, et doit être recopiée.

## 4. Wikilinks en `Écarter si` : 6 cellules sur 43

Le critère d'acceptation en veut un partout ; le pilote n'en a mis aucun et a expliqué pourquoi
(la règle dure nº 5 du lot 8 est notée comme un défaut à trancher, et s'y conformer d'avance
imposerait de réécrire les bornes sous la forme comparative que la remontée 20 condamne).

Ce lot atterrit à **6 sur 43, soit 14 %** — et l'écart avec le pilote n'est pas une divergence
de méthode : les 6 sont exactement les exclusions du point 3 qui pointent hors du dossier. Une
borne dure de la brique seule (« heap JVM gourmand », « verrou sur toute la base », « dormant
depuis 2022 ») n'a pas de cible vers laquelle pointer, par construction. **Le critère est donc
inatteignable tel qu'il est écrit**, et pas seulement inconfortable : il demande un lien là où
il n'y a personne à lier. À reformuler au lot 8 — par exemple « toute cellule `Écarter si` qui
nomme une alternative la porte en wikilink ».

## 5. Cellules laissées vides : 11

Le tableau ne s'équilibre pas, et n'a pas été comblé.

| Fiche | Cellule vide |
|---|---|
| CockroachDB, MariaDB, Microsoft SQL Server, MySQL, Postgres, SQLite, Vespa | `Écarter si` — 1 chacune |
| bm25s, Elasticsearch | `Prendre si` — 1 chacune |
| rank-bm25 | `Prendre si` — 2 |
| Marqo, txtai | aucune |

Les six de Relationnel ont la même cause, et c'est la même que celle du `DBeaver` du pilote :
leurs exclusions d'origine étaient toutes au comparatif, il ne reste que les trois bornes
propres tirées de `Pièges`, contre quatre raisons de les prendre. Le déséquilibre s'inverse
dans Recherche/, où les exclusions hors dossier viennent s'ajouter aux bornes.

## 6. Deux arbitrages de rédaction, à valider ou à corriger

**`Marqo` et la dépréciation.** Le critère « `## Définition` ne recontient ni la famille, ni la
licence, ni la **maturité** » entre en collision avec le fait le plus décisionnel de la fiche :
`maturite: deprecated`, que le bandeau affiche déjà. Choix fait — la `## Définition` décrit le
mécanisme et mentionne le pivot de l'éditeur sans reprendre le mot ; **la non-maintenance et
l'absence de correctifs de sécurité sont en première ligne d'`Écarter si`**, là où elles
décident. Le lecteur n'a pas à recouper le bandeau pour comprendre le risque. Si l'arbitrage
inverse est préféré, il vaudra pour toutes les fiches `deprecated` du vault.

**Deux comparatifs en `## Voir aussi` pour `bm25s` et `rank-bm25`.** Leurs `## Liens` d'origine
pointaient vers `[[Comparatif - NLP]]` et **pas** vers le comparatif de leur propre dossier,
alors que `Comparatif - Moteurs de recherche` les liste tous les deux. Les deux ont été mis, le
comparatif du dossier en premier. Ce n'est pas strictement du format — c'est un lien ajouté —
mais l'omission ressemblait à un reste d'avant le lot 3, quand ces deux fiches vivaient du côté
NLP.

## 7. Deux fiches avaient `url_docs` égal à `url_repo`

`Marqo` et `rank-bm25` : le dépôt GitHub est aussi la documentation. Rendre les deux étiquettes
aurait écrit deux fois la même URL sous deux noms. Une seule ligne `Dépôt` est posée, avec la
mention « il tient lieu de documentation ». Le cas se reproduira — beaucoup de petits paquets
sont dans ce cas. À arbitrer une fois pour toutes : ligne unique, ou deux lignes redondantes.

## 8. Aucune fiche sans `maturite:` dans le périmètre

Contrepoint à la remontée 6 du pilote, qui soupçonnait un trou lié à `famille: application` :
les 12 fiches de ce lot ont leurs quatre cellules de bandeau remplies, `Marqo` compris.
`build_bandeau --check` sur les deux dossiers ne signale **aucun** trou. L'hypothèse « le champ
n'a jamais été rempli pour la famille `application` » tient donc toujours — les 12 d'ici sont
6 `plateforme` et 6 `paquet`, aucune `application`.
