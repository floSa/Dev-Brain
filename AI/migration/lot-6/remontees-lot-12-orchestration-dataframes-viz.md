---
role: meta
nom: remontees-lot-12-orchestration-dataframes-viz
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées du lot 12

Périmètre : « Data & pipelines/Orchestration/ » (6), « Data & pipelines/DataFrames/ » (5)
et « Data & pipelines/Visualisation/ » (5). **16 fiches**, le compte annoncé par la table
du découpage, retrouvé exactement. Branche `claude/lot-12-data-pipelines-fce886`.

Aucun fichier partagé touché, aucune régénération, `cloturer-brain` non appelé.
`build_bandeau.py` lancé trois fois, borné à un dossier à chaque fois, jamais édité.

## 1. Les trois couples ouverts par le lot 1 sont fermés de mon côté

La remontée du lot 1 (`remontees-bdd-domaine.md`, branche
`claude/lot-6-databases-conversion-1209d0`) laissait trois moitiés pointant dans mon
périmètre. Elles sont posées, frontmatter **et** `### Compléments` :

| Ma fiche | `complements:` posé | Moitié déjà posée par |
|---|---|---|
| `Polars` | `[[ADBC]]`, `[[DuckDB]]` | lot 1, sur `ADBC` et `DuckDB` |
| `pandas` | `[[DuckDB]]` | lot 1, sur `DuckDB` |

Les deux couples sont donc **complets** dès que les deux branches sont intégrées. Rien à
faire pour l'intégration au-delà de la fusion.

## 2. Deux moitiés que j'ouvre à mon tour, cibles hors périmètre

| Ma fiche | Complément posé | Dossier de la cible | Lot qui refermera |
|---|---|---|---|
| `xarray` | `[[Dask]]` | Calcul distribué/ | lot 15 |
| `plotly` | `[[Dash]]` | Interfaces & apps data/ | lot 16 |

Les deux passent le test de la règle 3 — l'appariement est énoncé, et dans les deux sens :

- **xarray / Dask** — la fiche xarray recommande explicitement `chunks=...` comme *la* voie
  documentée pour dépasser la RAM, et le comparatif du dossier le redit. Réserve à signaler :
  la fiche `Dask` **ne nomme pas xarray** en retour, ni en corps ni en frontmatter. La
  réciprocité est donc sourcée d'un seul côté ; c'est au lot 15 de trancher s'il pose la
  sienne.
- **plotly / Dash** — plotly nomme Dash comme app dont il est la brique de visualisation ;
  `Dash.md` nomme plotly comme « moteur de rendu des graphes Dash (même éditeur) ».
  Réciprocité sourcée des deux côtés, et `plotly` n'est pas dans les `alternatives:` de Dash,
  donc aucun risque de double section quand le lot 16 posera sa moitié.

## 3. Trois appariements réels que je n'ai PAS posés — et pourquoi

Ils passeraient le test « la fiche énonce l'appariement », mais échouent sur autre chose.
Consignés pour que le lot 8 ou l'intégration décide, plutôt que tranchés en silence.

| Couple | Ce qui bloque |
|---|---|
| `Modin` / `Dask` | Dask **peut être le moteur d'exécution** de Modin — `Dask.md` l'écrit noir sur blanc (« Peut servir de moteur d'exécution à [[Modin]] »). Mais les deux fiches se déclarent mutuellement en `alternatives:`. Poser le complément mettrait la même cible dans deux sections. Le cas est réel : Modin et Dask sont **à la fois** concurrents et composables |
| `seaborn` / `matplotlib` | seaborn *est* une surcouche de matplotlib et sa sortie *est* une figure matplotlib — l'appariement est plus fort que la plupart de ceux du vault. Mais les deux sont l'unique `alternatives:` l'un de l'autre. Même blocage |
| `pandas` / `numpy` | pandas stocke ses colonnes dans des `ndarray`. Ce n'est pas une recommandation d'appariement, c'est une dépendance d'implémentation — et les deux se renvoient l'un vers l'autre dans le comparatif. Laissé en `## Voir aussi`, des deux côtés |

> Le motif commun mérite une décision générale : **un couple peut être à la fois
> alternative et complément** (Modin tourne *sur* Dask ; seaborn dessine *avec* matplotlib).
> Le gabarit v3 ne prévoit pas ce cas, et le critère « aucune cible dans deux sections »
> le rend inexprimable. Trois occurrences sur seize fiches, ce n'est pas marginal.

## 4. Deux appariements écartés parce qu'ils sont du positionnement

- `Airflow` / `Postgres` et `Temporal` / `Postgres` — les deux exigent *une* base de
  métadonnées, Postgres étant une option parmi Postgres, MySQL, Cassandra. C'est un
  prérequis d'exploitation, pas un appariement recommandé : le fait est resté en
  `## Mise en œuvre`, ligne *Prérequis*, avec son wikilink.
- `Prefect` / `Dask` — « intégrations Dask / Ray pour le parallélisme » est exactement le
  « s'intègre à » que la règle 3 refuse. Resté en *Prérequis*.

## 5. Règle 2 : les trois dossiers coïncident avec leur comparatif

Cas le plus favorable rencontré jusqu'ici, et il vaut d'être noté parce qu'il est rare :
les trois `.base` filtrent sur `role == "brique"` **et** une `categorie` unique, et chaque
categorie est exactement le contenu du dossier. Vérifié par
`AI/migration/scripts/mesure_membres_bases.py` :

| Vue | Membres | Briques du dossier |
|---|---|---|
| `Comparatif - Orchestrateurs data.base` | 6 | 6 |
| `Comparatif - Manipulation de données.base` | 5 | 5 |
| `Comparatif - Visualisation.base` | 5 | 5 |

Aucun des trois cas de figure que la règle 2 énumère (dossier sans comparatif, vue filtrée
par tag qui rate des briques) ne se présente. Le seul cas qui reste est le troisième — **la
brique est membre, la cible ne l'est pas** — et c'est lui qui commande tout le reste de ce
lot.

**Recoupement manuel avant usage en masse**, comme le lot 8 le demande : j'ai vérifié
`pandas -> [[Dask]]`. Dask vit dans `Calcul distribué/`, `categorie: compute/distribue` ;
la vue DataFrames filtre `categorie == "data/tableau"`. Dask n'est donc pas membre, et le
script ne le liste pas. Concordance exacte, aucun sur-comptage sur ce cas.

## 6. Les puces « besoin -> concurrent » : 40 partent au comparatif, 6 restent

Décompte sur les `## Quand NE PAS l'utiliser` d'origine des 16 fiches : **46 puces**, dont
**40 de la forme « besoin -> [[concurrent]] » dont la cible est membre de la même vue**.
Aucune n'a été recopiée : les trois pages `Ce qui départage`, écrites au lot 5, les portent
déjà — leur destination est « le comparatif du dossier, où elles sont déjà ».

Les **6 qui restent** ont une cible hors de la vue, donc aucun comparatif ne peut les
porter. Elles gardent leur wikilink en `Écarter si` :

| Fiche | Puce conservée | Cible, et son domaine |
|---|---|---|
| `Temporal` | traitement de flux temps réel | [[Flink]] — `data/streaming` |
| `pandas` | plus gros que la RAM, ou cluster | [[Dask]] — `compute/distribue` |
| `Polars` | distribué multi-nœuds | [[Dask]] — `compute/distribue` |
| `Modin` | pipeline déjà en graphes de tâches | [[Dask]] — `compute/distribue` |
| `numpy` | tableaux hors RAM, ou distribué | [[Dask]] — `compute/distribue` |
| `numpy` | accélération GPU, et autodiff | [[CuPy]], [[JAX]], [[PyTorch]] |

`Dask` concentre quatre des six. Il est l'alternative « à l'échelle » de tout le dossier
DataFrames sans jamais en être membre — sa `categorie` le range en calcul distribué. C'est
la démonstration la plus nette de la règle 2 : la brique est membre, la cible ne l'est pas,
et écarter la puce l'aurait purement supprimée.

## 7. Une puce ajoutée : le wikilink `[[Flink]]` sur Airflow

Un seul ajout de lien qui n'était pas dans la fiche d'origine, et je le signale plutôt que
de le laisser passer pour une évidence. `Airflow.md` portait « Streaming temps réel —
Airflow est un orchestrateur batch, pas un moteur de flux », **sans cible**. La fiche
`Temporal.md` du même dossier écrivait le même besoin avec sa cible : « Traitement de flux
temps réel -> [[Flink]] ». J'ai aligné Airflow sur la convention déjà écrite dans le
dossier. C'est de la navigation vers une brique existante, pas du contenu inventé — mais
c'est une décision, pas une conversion mécanique.

## 8. Le compte des cellules `Écarter si` — 56 sur 67 sans wikilink

Mesuré par script sur les 16 fiches converties :

| | Nombre |
|---|---|
| Cellules `Écarter si` | 67 |
| dont **vides** (le tableau ne s'équilibre pas) | 3 |
| dont sans wikilink (borne dure de la brique seule) | 56 |
| dont avec wikilink (cible hors de la vue) | 8 |

Le critère du brief « chaque cellule `Écarter si` contient un wikilink » est donc tenu à
**12 %**, et c'est la conséquence directe et assumée de la règle 2 : quand la cible est
membre de la même vue, la redirection appartient au comparatif, et ce qui reste sur la
fiche est une borne qui ne renvoie nulle part. Le pilote avait mesuré 0 % sur ses 18 ; le
chiffre remonte ici uniquement parce que `Dask` est hors vue.

Les 3 cellules vides, jamais comblées : `Dagster` (1), `Prefect` (1), `Temporal` (1).

## 9. Quatre cibles apparaissent dans deux sections — les quatre sont `Dask` ou `CuPy`

Mesuré par script :

| Fiche | Cible | Sections |
|---|---|---|
| `pandas` | `Dask` | `Écarter si` et `### Alternatives` |
| `Polars` | `Dask` | idem |
| `Modin` | `Dask` | idem |
| `numpy` | `Dask`, `CuPy` | idem |

Ce n'est pas un oubli, c'est l'intersection exacte des deux règles : `Dask` et `CuPy` sont
déclarés dans `alternatives:` du frontmatter — donc ils **doivent** figurer en
`### Alternatives`, R11 le contrôle en dur — et ils ne sont membres d'aucune vue commune
avec ces fiches — donc la règle 2 impose de **garder** la puce en `Écarter si`. Le critère
« aucune cible dans deux sections » ne peut pas être tenu ici sans perdre une information
ou casser le validateur. La règle 2 l'emporte, comme le brief le prévoit.

## 10. Aucune section `## Retours`, aucune cellule de bandeau vide

- Aucune entrée datée dans les 16 `## Pièges` d'origine — conforme à la mesure du lot 7,
  qui n'en trouve qu'une dans tout le vault. Aucune `## Retours` créée.
- `build_bandeau.py --check` sur les trois dossiers : 16 briques, **aucune** colonne à
  tiret cadratin. Contrairement aux sept `famille: application` du pilote, les 16 fiches
  d'ici portent un frontmatter complet — `maturite:` compris. L'hypothèse du pilote (le
  champ manquerait surtout à la famille `application`) n'est ni confirmée ni infirmée : ce
  périmètre n'a aucune `application` : il est fait de 6 `plateforme` (les six
  orchestrateurs) et de 10 `paquet` (DataFrames et Visualisation).

## 11. Écart des avertissements sur MA branche — 149 -> 133

| | Avertissements du vault | dont citant mes trois dossiers |
|---|---|---|
| Départ, `d8f81d6` | **149** | **16**, toutes R15 |
| Après les 16 conversions | **133** | **0** |

L'écart est de 16, et il vaut exactement les 16 R15 de mon périmètre : la conversion n'a
introduit **aucun** avertissement neuf, ni dans mes dossiers ni ailleurs dans le vault.
R15 exige un lien vers une `notion` ou un `hub` ; les 16 fiches d'origine ne pointaient
que vers leur comparatif, qui est un `role: comparatif`. La ligne `## Voir aussi` du
nouveau gabarit, qui nomme le hub du dossier, les ferme toutes.

> **Méthode, parce que je m'y suis trompé une fois.** Mon premier relevé disait 143, et il
> était faux : je l'avais pris **après** avoir converti Orchestration, pas avant. La
> mesure ci-dessus est reprise proprement — `git checkout d8f81d6 -- <mes trois dossiers>`,
> relevé, puis `git checkout HEAD -- <mes trois dossiers>` — mon travail étant déjà
> committé. À faire tenir aux conversations restantes : **relever la ligne de base avant
> la première écriture**, sinon elle n'est plus récupérable qu'au prix de cette
> gymnastique.

`check_arbo.py` est vert (chemin et catégorie concordent partout), `check_brain.py` ne
signale aucune violation dure, et `build_bandeau.py --check` sur les trois dossiers
confirme que les 16 bandeaux concordent avec leur frontmatter.

## 12. Ce que je n'ai pas touché, et qui reste ouvert

- Les trois hubs (`Orchestration.md`, `DataFrames.md`, `Visualisation.md`) et les trois
  comparatifs : hors périmètre, règle 1. Leurs zones AUTO seront régénérées à l'intégration.
- Les trois pages `Ce qui départage` restent **exactes** après conversion — je les ai
  relues, aucun discriminant n'a disparu des fiches ni changé de sens.
- Recouvrement fiche / comparatif assumé, comme la règle du 2026-09-06 l'autorise : par
  exemple la limite des 5000 lignes d'`altair`, la couverture d'API non totale de `Modin`,
  ou le déterminisme exigé par `Temporal` sont **à la fois** le discriminant du comparatif
  et la borne dure de la brique. Ils restent sur la fiche.
