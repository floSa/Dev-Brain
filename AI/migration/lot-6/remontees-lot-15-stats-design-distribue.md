---
role: meta
nom: remontees-lot-15-stats-design-distribue
type: gouvernance
created: 2026-09-06
tags: [meta, migration, v3]
---

# Lot 6 — remontées du lot 15 (statistiques, design, calcul distribué)

Périmètre : « Statistiques & inférence/ » en entier (10 briques), « Design & diagrammes/ »
en entier (7) et « Calcul distribué/ » (7). **24 fiches, le compte annoncé par la table du
découpage — vérifié avant d'écrire.** Branche `claude/lot-15-stats-design-distribue-5f95ed`,
partie de `d8f81d6`.

Aucun hub, aucune notion, aucun comparatif, aucun script, aucun document partagé n'a été
touché : les 24 fichiers du diff portent tous `role: brique` (vérifié par script sur
`git diff --name-only origin/main..HEAD`).

## 1. Écart de validateurs : 149 → 139 avertissements, zéro violation dure

Mesure sur la branche seule, avant et après. La baisse est de **10 R15** — « aucun lien
vers une notion ou un hub » —, et elle est entièrement expliquée : les sept fiches de
« Design & diagrammes/ » et quatre des sept de « Calcul distribué/ » ne citaient aucune
notion ni aucun hub, parce que leur ancienne section `## Liens` ne portait que le
comparatif et des URLs. La section `## Voir aussi` du nouveau gabarit y met le hub du
dossier, ce qui ferme la règle sans rien inventer.

`check_arbo.py` reste vert. `build_bandeau.py --check` concorde sur les 24.

## 2. Le comparatif de « Calcul distribué/ » ne couvre que 4 briques sur 7

C'est le cas 2 de la règle 2 — la vue filtre par catégorie et rate des briques de son
propre dossier — et il est ici **structurel, pas accidentel** :

| Brique | `categorie:` | Membre de `Comparatif - Calcul distribué.base` |
|---|---|---|
| CuPy | `compute/gpu` | oui |
| Dask, Ray, Spark | `compute/distribue` | oui |
| Daytona, E2B, Modal | `compute/a-la-demande` | **non** |

Le `.base` filtre sur `compute/distribue` **ou** `compute/gpu`, et rien d'autre. Les trois
bacs à sable partagent donc un dossier avec les quatre moteurs sans partager leur vue.
Conséquence appliquée : **aucune** des puces « besoin → concurrent » de Daytona, E2B et
Modal n'est partie au comparatif — elles sont toutes restées en `Écarter si`, avec leur
wikilink, puisqu'aucun comparatif ne peut les porter.

`check_brain` le dit déjà de son côté : `R8a — categorie compute/a-la-demande : 3 briques,
aucun comparatif .base ne les réunit`. L'avertissement préexiste au lot 15, il n'est pas
né ici — mais c'est le même trou vu de deux endroits. **À trancher hors lot 6** : ouvrir un
`Comparatif - Bacs à sable d'agents`, ou élargir le filtre de la vue existante. Ce n'est
pas une décision de conversion.

## 3. Recoupement manuel du script de mesure — pas de sur-comptage constaté ici

Le brief signale un sur-comptage possible de `AI/migration/scripts/mesure_membres_bases.py`.
Les quatre vues du périmètre ont été recoupées à la main contre le `filters:` de chaque
`.base` et le frontmatter des pages : les comptes concordent exactement (10, 5, 2, 4). Le
cas « Calcul distribué » est celui qui aurait le plus prêté au sur-comptage — trois briques
du même dossier hors de la vue — et le script les exclut correctement.

## 4. Les deux critères qui cèdent : le compte exact

| Mesure | Valeur |
|---|---|
| Cellules `Écarter si` remplies | 132 |
| — dont portant un wikilink | 22 |
| — dont **sans** wikilink, borne dure de la brique seule | 110 |
| Cellules `Écarter si` laissées vides | 2 — `Stan`, `scipy.stats` |
| Cibles présentes en `Écarter si` **et** en `Écosystème` | 10 |

Les 110 sans wikilink ne sont pas des cellules appauvries : ce sont les bornes dures que la
règle 2 laisse sur la fiche quand la redirection concurrente est déjà au comparatif. Les
10 doublons de section sont tous du même moule — la cible est bien dans `alternatives:`,
mais elle n'est membre d'aucune vue commune avec la brique :

`CausalImpact → Diff-in-Diff` (la cible est une **notion**, et un `.base` filtre
`role == "brique"`), `CuPy → numpy`, `Dask → pandas`, `Dask → Polars`, `Dask → numpy`,
`Dask → Modin` (cibles dans « Data & pipelines/DataFrames/ »), `Daytona → E2B`,
`Daytona → Modal`, `E2B → Modal`, `Modal → E2B` (remontée 2 ci-dessus).

Le cas `CausalImpact → Diff-in-Diff` mérite d'être noté à part : c'est un quatrième cas de
« sinon », qui ne figure pas dans les trois listés au brief. La cible n'est pas hors de la
vue par accident de filtre — elle en est exclue **par construction**, la clause
`role == "brique"` du lot 4 écartant toute notion. Toute redirection d'une brique vers une
notion tombera donc toujours dans « sinon ».

## 5. Cellules `Écarter si` laissées vides — deux, et pourquoi

- `scipy.stats` — quatre raisons de le prendre, trois de l'écarter. Ses trois exclusions
  d'origine étaient toutes des redirections vers `statsmodels`, `pingouin` et `Prince`,
  toutes membres de la même vue, toutes déjà portées par `Comparatif - Outils stats`.
- `Stan` — quatre raisons de le prendre, trois bornes dures propres.

Aucune n'a été comblée. Le tableau ne s'équilibre pas, et c'est la forme honnête.

## 6. Sept fiches sans `maturite:` — tout « Design & diagrammes/ »

`Archify`, `draw.io`, `Excalidraw`, `FossFLOW`, `Mermaid`, `Figma`, `Penpot` : la colonne
**Maturité** de leur bandeau affiche un tiret cadratin, et `build_bandeau.py` les nomme à
chaque passage. C'est **tout le domaine**, pas une famille : `extension`, `application` et
`saas` sont concernées indifféremment.

Cela confirme et déplace la remontée 6 du pilote, qui soupçonnait un trou propre à
`famille: application`. Le trou n'est pas dans la famille, il est dans le **domaine** :
« Bases de données/Administration/ » et « Design & diagrammes/ » ont été saisis sans ce
champ. Le combler est une décision éditoriale de floSa, pas une déduction de conversion.

`Figma` a un **second** trou : `famille: saas` sans `hosted:`, donc la colonne **Exécution**
est vide elle aussi. `build_bandeau.py` ne retombe sur `os:` que pour
`famille: application` — et à raison, `os:` ne dit pas où un SaaS s'exécute. La valeur juste
serait `hosted: [managed]`, mais la poser est une écriture de frontmatter que la conversion
ne s'autorise pas sans demande.

## 7. `complements:` — deux couples posés, entièrement dans le périmètre

C'est la première fois qu'un lot referme ses couples des deux côtés, parce que les trois
fiches concernées sont dans le même dossier :

| Couple | Ce qui l'autorise |
|---|---|
| `ArviZ` ↔ `PyMC` | ArviZ : « se branche en aval de PyMC et Stan » ; PyMC : « PyMC les délègue à ArviZ (renvoie un `InferenceData`) » |
| `ArviZ` ↔ `Stan` | ArviZ : idem ; Stan : « Exploration des résultats : déléguée à ArviZ (CmdStanPy expose un `InferenceData`) » |

Les deux fiches énoncent l'appariement comme une recommandation, dans les deux sens : c'est
exactement le test de la règle 3. Rien d'autre n'a été posé.

### Quatre candidats écartés, et le motif

- `Dask` → `Modin`, `Ray` → `Modin` : « peut servir de moteur / backend d'exécution à
  Modin » est du **positionnement**, pas une recommandation d'appariement — et `Modin` est
  déjà dans `alternatives:` des deux, ce qui rendrait le couple contradictoire.
- `CuPy` → `Dask` : « Dask peut orchestrer des chunks CuPy » n'est énoncé que **d'un
  côté** ; la fiche Dask ne mentionne pas CuPy. L'information est conservée en
  `## Voir aussi`, pas promue en couple.
- `Ray` → `Ray Tune` / `Ray Serve` : relation de **famille de produit** (des bibliothèques
  bâties *sur* Ray), pas deux briques indépendantes qu'on recommande d'apparier. Si le
  vault veut représenter cette relation, il lui faut un champ, pas `complements:`.
- `Modal`, `E2B`, `Daytona` → `Hermes Agent`, `OpenHands` : « backend d'exécution proposé
  par » est du positionnement, et la moitié réciproque n'existe pas sur les fiches
  d'assistants. **À vérifier au lot 8** : si ces fiches-là énoncent l'appariement, le couple
  devient légitime et se pose à ce moment.

## 8. Trois `Définition` reformulées pour ne pas redire le bandeau

Le critère « `## Définition` ne recontient ni la famille, ni la licence, ni la maturité » a
été **vérifié par script**, cellule par cellule, contre le bandeau réellement rendu — et non
contre une liste de mots, sans quoi « MPL-2.0 » compterait pour une répétition de
« open-source ». Trois fiches ont dû être reformulées :

- `Figma` — « cloud propriétaire sans self-host » → « cloud fermé, sans self-host » (la
  cellule Licence dit déjà « propriétaire ») ;
- `Modal` — « Produit propriétaire, sans self-host. » → « Aucun self-host : ni version
  auto-hébergeable, ni dépôt public du cœur. » ;
- `Daytona` — « a basculé son code de production » → « a basculé le code de son produit »,
  parce que « production » est la valeur de sa cellule Maturité. Formulation équivalente ;
  aucune information perdue.

> Ce dernier cas est un faux positif d'un test par sous-chaîne, pas une vraie redite. Il est
> consigné parce que les seize autres lots le rencontreront : « en production »,
> « code de production », « librairie Python » et « open-source » sont des locutions
> courantes de prose qui collident avec les quatre cellules.

## 9. Trois `### Alternatives` sans aucune cible — la forme retenue

`lifelines`, `ArviZ` et `CausalImpact` portent `alternatives: []`. Le brief signale trois
fiches du vault sans `## Alternatives` du tout ; ce n'est pas ce cas-ci — celles-là ont la
section, remplie d'une phrase honnête plutôt que d'un lien.

La forme retenue est une puce unique qui dit **pourquoi** il n'y a rien : « Aucune dans le
brain : lifelines est la seule bibliothèque d'analyse de survie répertoriée, et son pendant
ML, scikit-survival, n'y figure pas encore. » R11 ne se déclenche pas (`front_alts` vide) et
l'information — le concurrent existe, il n'est simplement pas dans le vault — n'est pas
perdue. À reprendre telle quelle si un autre lot rencontre le cas.

## 10. Deux redirections vers une cible absente du vault

`lifelines` renvoyait vers **scikit-survival** et `Prince` vers
`sklearn.decomposition.PCA`. La seconde se résout en `[[Scikit-Learn]]`, lien nu. La
première n'a pas de page : la borne est restée en `Écarter si` **sans wikilink**, en
nommant l'outil en clair. Aucune puce supprimée, aucun lien inventé.

## 11. `## Retours` n'a été créée nulle part

Conforme : aucune des 24 fiches ne portait d'entrée datée. Les `## Pièges` du périmètre
étaient à 100 % des limites de conception, réparties entre `Écarter si` et `## Définition`.

## 12. Une puce générique, non reportée

`Spark` portait en `Quand NE PAS l'utiliser` : « Données qui tiennent sur une machine →
Polars / DuckDB (souvent plus rapides, sans cluster) ». Elle est restée en `Écarter si` —
ni Polars ni DuckDB ne sont membres de la vue. Mais la même idée est le premier réflexe de
tout le domaine : « ne distribuez pas ce qui tient en mémoire ». Sa place naturelle est le
**corps du hub `Calcul distribué`**, section « Ce qu'il faut comprendre », qu'une
conversation de conversion ne touche pas (règle 1). Consignée ici, non reportée.
