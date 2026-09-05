---
role: meta
nom: remontees-outils-dev
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées du lot 14 (Outils de développement)

Périmètre : « Outils de développement/ » en entier, `Notebooks/` compris — **20 fiches**
`role: brique`, exactement le compte annoncé par la table du découpage. Branche
`claude/lot-14-outils-dev-121856`.

Écart de `check_brain.py` sur cette branche : **149 → 133 avertissements**, zéro violation
dure d'un bout à l'autre. Les 16 fermés sont **exactement** les 16 R15 du périmètre — chaque
fiche gagne un `## Voir aussi` qui pointe le hub de son dossier. Aucun autre avertissement du
vault n'a bougé, ce qui est attendu : la branche ne touche que ces 20 fiches. `check_arbo.py`
reste vert, et `build_bandeau.py --check` concorde.

## 1. Trois `## Définition` redisaient le bandeau — corrigées après mesure

Le critère « `## Définition` ne recontient ni la famille, ni la licence, ni la maturité » ne
s'attrape pas à la relecture : il se scripte. Passé sur les 20 fiches, il a trouvé trois
fuites qu'aucune relecture n'avait vues.

| Fiche | Ce qui fuyait | Colonne du bandeau concernée |
|---|---|---|
| `hydra` | « licence MIT inchangée », dans le récit de la migration vers Hydra Ecosystem | Licence |
| `Postman` | « Plateforme de développement d'API » | Nature (`famille: saas`) |
| `Rich` | « le projet reste maintenu en open-source » | Licence |

Les trois sont réécrites sans perdre l'information : la migration d'hydra dit toujours « ni
fork, ni abandon », Rich dit toujours qui maintient le projet depuis la fermeture de
Textualize en mai 2025.

> Pour les lots qui suivent : le cas `hydra` est le piège. La licence n'y était pas une
> paraphrase du frontmatter, c'était un fait de gouvernance — ce qui n'a **pas** changé lors
> du transfert. Un humain la garde, le critère la refuse. La reformulation coûte une minute,
> encore faut-il savoir qu'il y a quelque chose à reformuler : lancer le test, ne pas relire.

## 2. « Aucune cible dans deux sections » n'est pas en tension avec la règle 2 — il est contredit par une règle DURE du validateur

Mesure : **16 cibles apparaissent dans deux sections** de la même page, sur 6 fiches. Pour 14
d'entre elles ce n'est même pas un arbitrage : c'est mécaniquement forcé.

**Le mécanisme.** `devtools/config` (4 briques) et `devtools/notebook` (5 briques) n'ont
**aucun** comparatif `.base` — `check_brain` le dit lui-même en R8a, sur `main`, avant toute
conversion. C'est le cas 1 de la règle 2 : les puces « besoin → concurrent » **restent** en
`Écarter si` avec leur wikilink. Or ces mêmes cibles sont déclarées dans `alternatives:`, et
**R11 est une violation dure** : la section `### Alternatives` doit couvrir toutes les cibles
du frontmatter. La cible est donc obligatoirement aux deux endroits.

| Fiche | Cibles en double | Sections |
|---|---|---|
| `dynaconf`, `hydra`, `Pydantic Settings`, `python-dotenv` | 3 chacune, soit 12 | `Écarter si` + `### Alternatives` |
| `jupytext` → `Marimo` et `Marimo` → `jupytext` | 2 | `Écarter si` + `### Alternatives` |
| `jupytext` ↔ `papermill` | 2 | `Écarter si` + `### Compléments` |

Les 14 premières ne se résolvent pas par du soin éditorial : il faudrait soit supprimer la
puce — la règle 2 l'interdit, rien ne peut la porter —, soit vider `alternatives:`, que R12
et la réciprocité interdisent. Le lot 8, qui doit réécrire ce critère, a ici la démonstration
que la formulation actuelle est **inatteignable** sur tout dossier sans comparatif, et pas
seulement inconfortable.

Les 2 dernières sont d'une autre nature et méritent leur propre décision : `papermill` est à
la fois une **redirection** depuis `jupytext` (« si vous ne voulez qu'exécuter en CI, prenez
papermill ») et un **complément** (« l'appariement versionne le source, papermill l'exécute »).
Les deux phrases sont vraies et ne disent pas la même chose. Choix fait : garder les deux.

## 3. Écarter si — le compte exact des cellules

79 lignes de tableau sur les 20 fiches.

| Mesure | Compte |
|---|---|
| Cellules `Écarter si` remplies | 77 |
| … dont porteuses d'un wikilink | 27 |
| … dont sans wikilink : borne dure, ou renvoi vers une brique non fichée | 50 |
| Cellules `Écarter si` laissées vides | 2 — `Bruno` seul |
| Cellules `Prendre si` laissées vides | 9, sur 9 fiches différentes |

Les 50 sans wikilink se répartissent en deux familles, et la seconde est celle que le lot 8
devra nommer : **la cible n'existe pas dans le vault**. Click, argparse, Fire, colorama,
prompt_toolkit, Textual, mypy, ty, unittest, conda, MkDocs, Docusaurus, attrs, cattrs,
marshmallow, Flake8, Black, isort, pylint — dix-neuf noms cités par les fiches d'origine,
zéro fiche en face. Un critère « un wikilink dans chaque cellule » les rendrait tous
obligatoires à ficher, ce qui n'est pas une décision de format.

`Bruno` est le seul à ne pas remplir son tableau : ses deux exclusions d'origine visaient
toutes deux `[[Postman]]`, toutes deux déjà portées par le comparatif. Il ne lui reste que
deux bornes propres — le format `.bru` non interopérable, et l'absence de couche plateforme.

## 4. Les six briques à comparatif : six redirections sur sept étaient déjà portées

Trois vues `.base` dans le domaine, **deux membres chacune** : `Bruno` et `Postman`
(`devtools/client-api`), `Rich` et `Typer` (`devtools/cli`), `pip` et `uv`
(`devtools/paquet`). Mesuré à la main sur les `categorie:`, puis recoupé par
`AI/migration/scripts/mesure_membres_bases.py`, qui donne exactement le même résultat. Pas de
sur-comptage ici : les trois vues filtrent sur une clause `categorie == …` unique,
entièrement évaluable hors ligne. Les 14 autres fiches ne sont membres d'aucune vue.

Sept redirections vont d'un membre vers un autre membre de la **même** vue — donc cas 1 de la
règle 2, la puce vit au comparatif. Vérifiées une par une contre la section
`## Ce qui départage` : **six y étaient déjà**.

**La septième manque, et c'est une remontée pour l'intégration.** `pip` portait « besoin de
vitesse en CI sur de grosses arborescences de dépendances → [[uv]] ». Le
`Comparatif - Gestionnaires de paquets Python` ne dit rien de la vitesse : sa puce `uv` parle
d'absorption d'outils et de `uv.lock`, pas de performance. Cette puce n'avait donc **aucune**
destination. Elle est reformulée en borne dure de pip seul — « résolveur strict depuis 2020,
mais lent sur de gros graphes de dépendances » —, ce qui conserve le fait sans écrire une
ligne de comparatif qu'une conversation de conversion n'a pas le droit d'écrire (règle 1).

> À trancher à l'intégration : ajouter la vitesse à la puce `uv` du comparatif, ou considérer
> que la borne portée par `pip` suffit.

`Rich` et `Typer` sont membres de la même vue sans se rediriger l'un vers l'autre : le
comparatif le dit lui-même, « deux couches, pas deux options ». Ils sont traités en
compléments (§ 5), pas en alternatives.

## 5. `complements:` — quatre couples posés, une moitié en attente

Ce sont les **premiers `complements:` non vides du vault** : la mesure du 2026-09-06 en
trouvait zéro sur les 337 fiches, le pilote ayant laissé les siens ouverts faute de cible
dans son périmètre.

| Couple | Ce qui le source, dans les deux fiches |
|---|---|
| `Typer` ↔ `Rich` | « le rendu enrichi de l'aide repose sur Rich : l'installer pour en profiter » / « utilisé par Typer pour l'aide et les erreurs enrichies » |
| `pytest` ↔ `testcontainers` | « voisin direct » / « les conteneurs jetables s'exposent en fixtures pytest » |
| `Pydantic` ↔ `Pydantic Settings` | « bâtie sur Pydantic », plus une consigne d'installation explicite : « installer `pydantic-settings` **en plus de** `pydantic` » |
| `jupytext` ↔ `papermill` | « complémentaire au pairing » / « souvent combinés » |

**La moitié en attente :** `jupysql` → `[[DuckDB]]` (« compagnon fréquent : SQL analytique
local dans le notebook »). `DuckDB` vit dans « Bases de données/ » au niveau domaine, donc
dans le périmètre du **lot 1**. Ma moitié est posée ; c'est au lot 1 de fermer l'autre. Rien
ne casse en attendant : aucune règle du validateur ne contrôle la réciprocité de
`complements:` — c'est `alternatives:` qui la porte, pas lui.

### Trois appariements refusés, et pourquoi

La règle 3 dit qu'« s'intègre à » n'ouvre pas de couple. Le domaine offre le cas d'école :

- `papermill` → `uv` et `Quarto` → `uv`, tous deux sous la forme « environnement épinglé qui
  rend l'exécution reproductible ». C'est une recommandation générale d'hygiène, pas un
  appariement : la retenir donnerait à `uv` un `complements:` qui grossirait avec chaque
  fiche Python du vault — exactement le bruit que la règle 3 cherche à éviter.
- `jupytext` → `Ruff` et `pytest` (« linter et tester le pendant `.py` »). Même raison, et la
  réciproque n'existe nulle part : ni `Ruff` ni `pytest` ne nomment jupytext.
- `Typer` → `FastAPI` (« même auteur »). C'est de la provenance, pas un appariement.

Les liens eux-mêmes ne sont pas perdus : ils restent dans `## Mise en œuvre` (uv chez Quarto)
ou dans une cellule `Prendre si` (Ruff et pytest chez jupytext).

## 6. Trois fiches n'ont aucune section `## Écosystème`

`Ruff`, `Obsidian` et `Quarto` : leur `alternatives:` est vide, aucun complément ne se
source, et toutes leurs redirections visent des outils non fichés, déjà portés par
`Écarter si`. Écrire une section vide, ou la remplir d'une note en italique « pas
d'alternative fichée », aurait ajouté du titre sans contenu — exactement ce que le lot 6
corrige. La section est donc omise.

C'est une décision de gabarit qui dépasse mon périmètre : **`## Écosystème` est-elle
obligatoire ?** Le lot 8 devrait le dire, dans un sens ou dans l'autre. En l'état, rien ne la
vérifie : `check_brain` ne contrôle `### Alternatives` que si `alternatives:` est non vide.

## 7. Trous de donnée dans le frontmatter — trois fiches, six cellules

`build_bandeau.py` les nomme à chaque passage, et le champ étant facultatif, ce n'est pas une
faute de validateur. C'est une décision éditoriale de floSa, pas une déduction de conversion.

| Fiche | Colonnes vides | Cause |
|---|---|---|
| `Bruno` | Maturité | `maturite:` absent |
| `Postman` | Exécution, Maturité | `maturite:` absent ; `famille: saas` ne lit pas `os:`, et `hosted:` est absent |
| `Obsidian` | Nature, Exécution, Maturité | **`famille:` absent**, donc rien à dériver ; `os:` est pourtant renseigné |

Le cas `Postman` étend la remontée 6 du pilote : ce ne sont pas seulement les
`famille: application` qui manquent de `maturite:`. Ici les trois fiches sans maturité sont
les trois seules non-Python du domaine à interface graphique ou service — les deux clients
d'API et Obsidian ; les 17 autres en portent une.

Le cas `Obsidian` est plus dur : `famille:` est une **règle dure** (R14) contrôlée sur une
énumération fermée… et un champ absent passe. Une brique sans `famille:` échappe donc à la
fois à R14 et à R16, et son bandeau perd deux colonnes sur quatre. À signaler au lot 8 :
`famille:` devrait être **requis**, pas seulement contraint quand il est présent.

## 8. `jupysql` porte un alias en doublon — non corrigé, hors mandat

`R5 — Outils de développement/Notebooks/jupysql.md : alias en doublon interne ['jupysql']` :
`nom: jupysql` et `alias: [JupySQL, jupysql]`. C'est le seul avertissement de mon périmètre
qui ne soit pas un R15, et le seul qui survit à la conversion — il est dans le frontmatter,
où la consigne n'autorise à toucher qu'à `complements:`. Correctif évident : retirer
`jupysql` de la liste d'alias. À faire par qui a le droit d'y toucher.

## 9. `## Retours` n'a été créée nulle part

Conforme. Aucune entrée datée dans les 20 fiches d'origine — la seule du vault est chez le
lot 7.

## 10. Aucune puce supprimée sans destination — le bilan

Les 20 fiches portaient **121 puces** à dissoudre : 57 en `## Quand NE PAS l'utiliser` (dont
34 avec un wikilink, donc de la forme « besoin → concurrent ») et 64 en `## Pièges`. Leurs
destinations :

- `Écarter si` **avec** wikilink — les 27 cellules du § 3 ;
- `Écarter si` **sans** wikilink — bornes dures, et renvois vers du non fiché ;
- `## Définition` — les limites qui n'orientent aucun choix : le modèle réactif de Marimo qui
  interdit de redéfinir une variable, la discipline en trois gestes de jupytext, les deux
  commandes distinctes de Ruff, la découverte par convention de pytest, l'aller-retour
  `.qmd` ↔ `.ipynb` de Quarto ;
- `## Mise en œuvre` — les prérequis déguisés en pièges, nombreux dans ce domaine : la
  distribution TeX de Quarto, le démon Docker de testcontainers, le kernel épinglé de
  papermill, le *Restart & Run All* de jupytext, le venv de pip ;
- **le comparatif du dossier**, pour six des sept redirections des briques membres (§ 4).

Aucune n'a été perdue, et la seule qui n'avait nulle part où aller est documentée au § 4.

> Le ratio mérite d'être noté pour les lots restants : **64 puces de `Pièges` pour 20 fiches**,
> et pas une seule datée. La majorité était soit un prérequis d'installation, soit une limite
> de conception — c'est-à-dire soit `## Mise en œuvre`, soit `Écarter si`. La règle du brief
> (« trois destinations ») tient, mais dans ce domaine la troisième — `## Retours` — n'a
> jamais servi, et la première — `## Définition` — a servi moins que `## Mise en œuvre`, qui
> n'est pas listée comme destination.
