---
role: meta
nom: remontees-pilote
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées de la conversation pilote

Périmètre : `build_bandeau.py`, puis « Bases de données/Vectoriel/ » (11 fiches) et
« Bases de données/Administration/ » (7). Branche `claude/lot-6-conversion-fiches-8ec828`.

Le pilote passe **seul** : il a donc corrigé les documents partagés que la règle 3 interdit
aux dix-sept conversations parallèles de toucher — le brief, `check_brain.py`. Les
conversations parallèles n'ont pas ce droit : elles écrivent ici, dans leur propre fichier.

## 1. Le brief était périmé de 71 lignes dans le worktree

La conversation a d'abord conclu que le protocole parallèle n'existait pas, sur la foi d'une
copie locale accrochée à `2103e2a` alors qu'`origin/main` portait déjà `6505991`. L'étape 0
du protocole de session — `git fetch` **avant** de lire, pas après — n'avait pas été faite.
Rien de cassé, le fast-forward était pur, mais une conclusion fausse a été énoncée.

> À faire tenir aux dix-sept : la première commande d'une conversation de conversion est
> `git fetch origin`, et la deuxième est la lecture du brief, pas l'inverse.

## 2. `check_brain.py` ne connaissait pas le nouveau gabarit — correctif appliqué

`ALT_SECTION_RE` ne reconnaissait que `## Alternatives`. Le gabarit v3 écrit
`### Alternatives` sous `## Écosystème` : les trois premières fiches converties ont fait
échouer R11 en **dur**, sur les quatre à six cibles de leur frontmatter.

Correctif : `r"\n#{2,3} Alternatives\n(.*?)(?=\n#{2,3} |\Z)"`. Les deux formes sont
acceptées, ce qui est indispensable — les deux coexisteront dans le vault pendant toute la
durée du lot, et sans cet élargissement **la première conversation qui convertit casse la
branche des seize autres**.

> Ce correctif est dans le commit du pilote. Une conversation parallèle qui verrait encore
> R11 échouer sur ce motif travaille sur une base antérieure : elle doit se rebaser, pas
> éditer le script.

## 3. La section « déploiement » porte trois noms, pas un

Le brief n'en nommait qu'un. Mesure du 2026-09-06 sur les 337 briques :

| Section | Fiches |
|---|---|
| `## Déploiement & coût` | 297 |
| `## Bases & plateformes` | 22 |
| `## Installation & plateformes` | 18 |

Les sept fiches d'Administration portaient `## Bases & plateformes`. Une conversation qui ne
cherche que le premier nom laisserait 40 fiches avec deux sections de mise en œuvre.
**Corrigé dans la table de correspondance du brief.**

## 4. La table du découpage laissait 11 fiches orphelines — corrigée

Défauts mesurés de la première rédaction en 14 lots : 11 fiches hors de tout lot (le niveau
domaine de « LLM & IA générative/ »), deux lots au-dessus du plafond de 25 (29 et 27), et un
total de 326 pour 337. **Table refaite en 17 lots**, vérifiée par script : couverture des
337, zéro orpheline, aucun lot au-dessus de 25, aucun dossier dans deux lots.

## 5. `complements:` reste vide sur les 18 — et c'est volontaire

Le brief demande de le remplir « quand le voisinage de la fiche est sous les yeux ». Cinq
paires sont sourcées dans les fiches du pilote, et **les cinq pointent hors du périmètre** :

| Fiche du pilote | Complément sourcé | Dossier de la cible | Lot qui le portera |
|---|---|---|---|
| `pgvector` | [[Postgres]] | Bases de données/Relationnel/ | lot 2 |
| `MongoDB Compass` | [[MongoDB]] | Bases de données/ (niveau domaine) | lot 1 |
| `MySQL Workbench` | [[MySQL]] | Bases de données/Relationnel/ | lot 2 |
| `Redis Insight` | [[Redis]] | Bases de données/ (niveau domaine) | lot 1 |
| `pgAdmin` | [[Postgres]] | Bases de données/Relationnel/ | lot 2 |

La réciprocité étant obligatoire, poser la moitié du couple aurait laissé les cinq fiches
cibles en faute. Elles sont donc **laissées vides et inscrites ici** : c'est aux lots 1 et 2
de fermer ces couples, dans les deux sens, quand ils convertiront les cibles.

> Cas général mesuré : la réciprocité traverse les frontières de dossier dans **66 arêtes sur
> 798** (8 %). Le cas n'est donc pas marginal, et le mécanisme — poser sa moitié seulement
> quand la cible est dans son périmètre, sinon remonter — vaut pour les dix-sept.

## 6. Sept fiches n'ont pas de `maturite:` — cellule laissée vide

`DataGrip`, `DBeaver`, `HeidiSQL`, `MongoDB Compass`, `MySQL Workbench`, `pgAdmin`,
`Redis Insight` : la colonne **Maturité** de leur bandeau affiche un tiret cadratin.
`build_bandeau.py` les nomme à chaque passage. Le champ est facultatif au gabarit, donc ce
n'est pas une faute de validateur — c'est un trou de donnée, et le combler est une décision
éditoriale de floSa, pas une déduction de conversion.

Ces sept fiches sont les sept `famille: application` du dossier Administration. Il est
possible que le champ n'ait jamais été rempli pour cette famille ; à vérifier sur les autres
domaines quand ils passeront.

## 7. Les puces « besoin → concurrent » étaient déjà dans le comparatif

Application de la remontée 20 du lot 5. Sur les 18 fiches, les sections
`## Quand NE PAS l'utiliser` contenaient **54 puces**, dont **48 de la forme
« besoin → [[concurrent]] »** — soit 89 %. En face, `## Pièges` en portait **52**.

Aucune des 48 n'a été recopiée en `Écarter si` : les onze lignes du
`Comparatif - Bases vectorielles` et les sept du `Comparatif - Clients de bases de données`,
écrites au lot 5, les portaient déjà. Leur destination est donc « le comparatif du dossier,
où elles sont déjà » — ce qui satisfait « aucune puce supprimée sans destination ».

Ce qui reste en `Écarter si` est une **borne dure de la brique seule** : index figé après
`build()` (Annoy), `max_elements` fixé à l'initialisation (hnswlib), métrique irréversible
(Qdrant, Pinecone), `maintenance_work_mem` (pgvector), licence SSPL non OSI (Redis Insight).

**Aucune cellule ne porte de wikilink**, et c'est délibéré : la règle dure nº 5 du lot 8 en
voudra un, mais elle est notée comme un défaut à trancher, et s'y conformer d'avance aurait
imposé de réécrire les bornes sous la forme comparative que la remontée 20 condamne.

### Recouvrement résiduel avec les comparatifs — à arbitrer

Trois faits apparaissent des deux côtés, parce qu'ils sont à la fois le discriminant du
comparatif et la borne dure de la brique :

| Fait | Fiche | Comparatif |
|---|---|---|
| index immuable après `build()` | Annoy, `Écarter si` | « immuable après `build()` » |
| monte mal en charge | Chroma, `Écarter si` | « elle monte mal en charge » |
| aucun paramètre d'index à régler | Pinecone, `Écarter si` | « la base décide » |

Trois sur 18 fiches. Les formulations diffèrent — la fiche dit ce qui va mordre, le
comparatif dit ce qui fait choisir — mais ce sont bien deux endroits à tenir d'accord. À
trancher pour les dix-sept : recouvrement toléré, ou fiche muette sur son propre
discriminant.

## 8. Deux puces génériques n'appartenaient à aucune des trois destinations

`Chroma` et `LanceDB` portaient la même puce en `Pièges` : « cohérence métrique / modèle
d'embedding à surveiller **comme pour tout vector store** ». Ce n'est ni une borne de la
brique, ni un retour d'expérience : c'est une propriété du domaine. Sa place est la notion
[[Bases de données vectorielles]], qu'une conversation de conversion **ne modifie pas**
(règle 1, et frontière `role: notion` de `CLAUDE.md`). Les deux puces sont donc consignées
ici, non reportées.

## 9. Cellules `Écarter si` laissées vides — le compte exact

Le tableau ne s'équilibre pas : quand une fiche a quatre raisons de la prendre et deux de
l'écarter, les deux cellules restantes sont vides. **17 cellules vides sur 13 fiches**, jamais
comblées. Détail : Weaviate, DataGrip, DBeaver, HeidiSQL — 2 chacune ; Chroma, LanceDB,
Milvus, pgvector, Pinecone, Qdrant, MongoDB Compass, MySQL Workbench, pgAdmin — 1 chacune.
Les cinq autres — Annoy, Faiss, hnswlib, ScaNN, Redis Insight — remplissent le leur.

`DBeaver` est le cas le plus net : ses trois exclusions d'origine étaient toutes de la forme
« besoin → concurrent », toutes déjà au comparatif. Il ne lui reste **qu'une** borne propre,
l'empreinte mémoire de l'application Java.

## 10. `## Retours` n'a été créée nulle part

Conforme au brief : la section n'existe que s'il y a une entrée datée. Mesure du 2026-09-06 —
une seule fiche du vault en porte une, `LLM & IA générative/Agents de code/t3code.md`, du
ressort du **lot 7**. Aucune dans le périmètre du pilote.

## 11. Trois fiches n'ont pas de `## Alternatives` dans le vault

334 sur 337. Hors périmètre du pilote, mais les lots concernés n'auront pas de
`### Alternatives` à écrire — et c'est la règle 4 du validateur, souple, qui les signale.
