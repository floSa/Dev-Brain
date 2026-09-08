---
galaxie: meta
nom: lot-9-brainkit
type: gouvernance
created: 2026-09-08
modified: 2026-09-08
tags: [meta, migration, brainkit]
---

# Lot 9 — Le DevBrain devient une instance de BrainKit

> [!info] **Ce lot n'appartient pas à la migration v3**, close le 2026-09-06. Il appartient au
> plan de lots de **BrainKit** (`design/00-cadrage.md` §6 du dépôt voisin), dont il est le
> neuvième et le **premier autorisé à écrire ici**. Il est rangé dans `AI/migration/` parce que
> c'est la place du journal de lot dans ce vault, et parce que le manifeste **pointe** vers ce
> dossier : « le journal de lot n'est pas remplaçable par de la configuration ».

Le pendant côté kit — le diff commenté, les arbitrages et les remontées destinées à BrainKit —
est dans `design/09-migration-devbrain.md` du dépôt BrainKit. Ce fichier-ci dit ce qui a changé
**dans le vault**, et ce qu'un futur lot de ce vault doit savoir.

## Ce que le lot fait, en une phrase

Le DevBrain cesse de porter son outillage et le **lit** dans BrainKit, piloté par un manifeste
`brain.yml` posé à sa racine — sans qu'une seule page change.

---

## 1. Avant d'écrire — la vérification de divergence

Faite en premier, avant toute lecture de code, parce que c'est la règle du vault et qu'elle est
née d'une session qui a travaillé des heures sur une base obsolète (2026-07-29).

```
git fetch origin
git log HEAD..origin/main --oneline    -> vide
git merge-base HEAD origin/main        -> 8aaa257
git rev-parse HEAD origin/main main    -> 8aaa257, trois fois
```

**Aucune divergence** : `main`, `origin/main` et la branche de travail partent du même commit.
Les **32 arbres de travail** du dépôt ont été balayés un par un — `git status --porcelain` vide
sur les 32, dont le principal.

Le travail s'est fait sur la branche dédiée **`claude/brainkit-lot9-devbrain-8463bb`**, dans son
worktree. `main` n'a pas été touchée.

L'identité git a été **lue**, pas posée : `git config --local user.name` → `floSa`,
`user.email` → l'adresse perso, `core.hooksPath` → `.githooks`. Rien n'a été passé en
`-c user.email`, en `--author`, ni en variable d'environnement.

---

## 2. Ce qui a été posé — `brain.yml`

Un fichier, à la racine, **identique à l'octet** à `exemples/devbrain.brain.yml` du dépôt
BrainKit (sha256 vérifié). C'est ce que le lot 2 de BrainKit a passé au test de fidélité, et ce
que les lots 3, 4 et 8 ont fait tourner en lecture seule sur ce vault : même verdict règle par
règle, 413 artefacts sur 414 identiques à l'octet, et les comptes de mesure retrouvés.

Ce que le manifeste porte, et que le code ne porte plus :

| Ce qui vivait en dur dans `AI/scripts/` | Où c'est maintenant |
|---|---|
| `DOM_LABEL` (20 préfixes), `DOM_RATTACHE`, `SUB_LABEL` (47 sous-libellés) | `axes.rangement.prefixes` / `rattachements` — **avec le motif de chaque libellé** |
| `SEUIL = 5` et son plafond | `axes.rangement.seuil_promotion` / `plafond_promotion` |
| `REQUIRED` / `ALLOWED` par rôle, les énumérations, les champs conditionnels | `roles[].champs` |
| Les 6 titres du corps d'une brique, les étiquettes fermées | `roles[].corps` |
| `NATURE`, `LICENCE`, `EXECUTION_FAMILLE`, `HOSTED` du bandeau | `bandeau.colonnes` |
| `THEME_LABEL`, `HUBS_TRANSVERSES` | `axes.transverses` |
| `NON_PAGES`, dupliqué dans les quatre générateurs | `genere.non_pages`, **une fois** |
| Les dix règles et leur sévérité | `regles[]`, chacune avec sa mesure datée |

**Conséquence pratique, et c'est la seule qui change une habitude** : le libellé d'un
sous-domaine promu s'ajoute désormais dans `brain.yml`, sous
`axes.rangement.prefixes[].sous` — **plus dans `SUB_LABEL`**. Le skill `enrichir-brain` dit
encore l'ancien endroit ; voir la remontée 1.

---

## 3. Ce qui a été remplacé — `AI/scripts/`

Six scripts et une bibliothèque sont devenus des **ponts** : une vingtaine de lignes qui
résolvent la racine du kit, chargent `brain.yml`, et appellent BrainKit. **Aucune ligne du kit
n'est copiée ici.** Les 1 159 lignes de règles de `check_brain.py`, écrites entre le lot 2 et le
lot 8 de la migration v3, ont été réécrites dans le kit et branchées sur le manifeste — le lot 3
de BrainKit l'a prouvé par le verdict, pas par la ressemblance du code.

| Fichier | Lignes avant → après | Ce qu'il appelle |
|---|---|---|
| `check_brain.py` | 1 159 → 64 | `brainkit valider` — le verdict entier |
| `check_arbo.py` | 163 → 88 | `brainkit valider`, restreint à `chemin_categorie`, `hub_par_niveau`, `frontmatter_lisible` |
| `build_index.py` | 221 → 64 | `brainkit generer --quoi index` |
| `build_mocs.py` | 365 → 56 | `brainkit generer --quoi hubs` |
| `build_links.py` | 180 → 50 | `brainkit generer --quoi liens` |
| `build_bandeau.py` | 361 → 60 | `brainkit generer --quoi bandeau` |
| `arbo.py` | 268 → 107 | `brainkit.valider.chemins` — bibliothèque, pas script |
| `_pont_kit.py` | — → 133 | **nouveau** : où vit le kit, et rien d'autre |

**2 677 lignes retirées, 553 posées** dans `AI/scripts/`, `README.md` compris —
comptes de `git diff --stat`. Ce qui a disparu au passage n'est pas que du volume : `V1_MARKERS` et `is_active_v2()` de `check_brain.py`, `MOC_CONCEPT` / `WIKI_LABEL` /
`wiki_group()` de `build_mocs.py`, le jeu `V1` de `build_links.py`, `arbo.LEGACY` — des branches
mortes pour des dossiers supprimés à la clôture du lot 4. Le kit ne les hérite pas, et aucune
instance future ne les héritera.

### Pourquoi des ponts, et pas la commande du kit

C'est la décision principale du lot, et elle a deux motifs mesurables.

**Le premier est un contrat.** `cloturer-brain`, `enrichir-brain`, `.claude/settings.json` et le
hook `Stop` nomment tous `AI/scripts/<script>.py`. Ces quatre fichiers pilotent l'écriture dans
le vault et sont lus à chaque session. Le critère d'acceptation du lot est *aucun contenu de
page modifié* ; le tenir tout en cassant ce qui écrit les pages aurait été une victoire de
comptable. Le pont rend les deux vrais en même temps : rien à réapprendre, rien à réécrire.

**Le second est un octet.** `genere.index.signature` vaut `AI/scripts/build_index.py`, et cette
chaîne est **dans l'artefact versionné** — `generated_by` du catalogue, en-tête du document
humain. Tant que le fichier lancé porte ce nom, la signature reste exacte et les deux fichiers
d'index ne bougent pas. Basculer vers `brainkit generer` aurait réécrit deux artefacts pour ne
rien gagner.

### Comment ce vault atteint le kit — la remontée 5 du lot 7, tranchée

`kit.mode: branche` dit que le code vit ailleurs, **sans dire où**. Le lot 7 de BrainKit avait
mesuré la conséquence : ni `brainkit valider` ni `uv run brainkit valider` ne résolvent depuis
le dossier d'une instance, alors que les fichiers écrits par le semis donnent ces commandes
telles quelles. Deux propositions y étaient posées, aucune tranchée — un champ `kit.racine:` au
manifeste, ou une étape d'installation qui met le kit sur le PATH.

**Ni l'une ni l'autre n'est prise ici**, et le motif compte :

- un `kit.racine:` serait un **chemin absolu de poste** dans un fichier versionné, partagé entre
  trois machines (cf. `Documentation/perso/machines.md`) — et il ferait diverger `brain.yml` de
  `exemples/devbrain.brain.yml`, donc perdre la fidélité prouvée au lot 2 ;
- mettre `brainkit` sur le PATH est une étape d'installation, donc du lot 10 — et une étape
  d'installation qu'on oublie est un outillage qui ne tourne plus.

La résolution vit dans `AI/scripts/_pont_kit.py`, en trois pistes essayées dans l'ordre :

1. **`$BRAINKIT_RACINE`**, si la variable est posée — l'échappatoire explicite ;
2. **`AI/scripts/brainkit/`** — une instance **figée**, où `brainkit freeze` a copié le kit dans
   le vault. Ce cas passe avant le suivant, et c'est délibéré : une instance figée ne doit plus
   jamais lire un kit du dehors, c'est toute sa raison d'être ;
3. le **voisinage** : `<parent>/BrainKit`, en remontant depuis la racine du vault. Le cas
   nominal — les deux dépôts côte à côte sous `Projets/` — répond au premier parent ; un
   worktree, qui vit trois niveaux plus bas sous `.claude/worktrees/`, répond au quatrième.

Si aucune ne répond, les ponts **sortent en 2** et impriment les trois pistes. Ils ne devinent
pas : un kit deviné est un verdict rendu par un code qu'on n'a pas choisi.

### Ce que `check_arbo.py` a perdu, et ce qu'il garde

Le kit n'a **qu'un** validateur : `check_brain` et `check_arbo` y sont fusionnés. Les deux
entrées survivent parce que `cloturer-brain` les lance toutes les deux et parce que sa mise en
garde reste vraie — *ne lancer que `check_brain` et croire le vault validé*. Un verdict de 111
avertissements où l'on cherche à l'œil les trois lignes de structure n'est pas le même outil
qu'un verdict de structure.

Ce qui est perdu, et qu'il faut savoir : le pont **ne propose plus le `git mv` en toutes
lettres**. Le kit nomme le dossier attendu, ce qui est la même information ; la phrase, elle,
n'a pas survécu à la réécriture. Son en-tête a changé aussi — il compte les pages du vault et
les dossiers de premier niveau, là où l'ancien comptait les « pages migrées ». La ligne de
sortie que les outils lisent, elle, est inchangée : `[FAIL]` par violation,
`OK — chemin et catégorie concordent partout.` à la fin.

### La dérivation, vérifiée page par page

`arbo.py` garde son API — `domaine()`, `promotions()`, `dossier_attendu()` — et la comparaison
avec l'ancienne implémentation, sur la population réelle du vault, donne :

```
SEUIL : 5 = 5
promotions identiques : True — 45 promus
dossiers attendus différents : 0 / 765
```

Une différence de vocabulaire, sans conséquence mesurée : `ROLES_SANS_CATEGORIE` et
`ROLES_HORS_SEUIL` sont maintenant **dérivés du manifeste** et contiennent donc `hub`, que
l'ancien code écartait par un `if` séparé. C'est plus juste — un hub ne porte pas de catégorie
et ne pèse pas sur le seuil — et aucun consommateur ne s'en sert autrement.

---

## 4. Le seul artefact qui a bougé — et pourquoi c'était le moment

La clé **`scanned`** de `AI/index/brain-index.json` perd deux entrées :

```diff
   "scanned": [
-    ".githooks",
     "Automatisation no-code",
     …
-    "Web & API",
-    "obsidian_outer_backup_20260907"
+    "Web & API"
   ],
```

C'est la remontée 1 du lot 4 de BrainKit, confirmée par la remontée 2 du lot 5, et **les deux
avaient conclu que l'issue se prend ici** — premier moment où changer la clé ne coûte pas le
critère d'acceptation d'un lot antérieur.

Le fait : `scanned` publiait **tout** dossier de premier niveau hors `non_pages`, suivi par git
ou non. Un artefact **versionné** portait donc du contenu non suivi, et cessait d'être
reproductible — deux machines qui génèrent le même commit produisaient deux catalogues
différents. Ce vault en portait la preuve : son catalogue committé annonçait
`obsidian_outer_backup_20260907`, une sauvegarde locale qui **n'existe plus sur le disque**.
C'est cette seule ligne qui faisait sortir `generer --check` en 2, sans qu'aucune page ait bougé.

Le correctif, posé dans le kit (`brainkit/generer/corpus.py`) : **`scanned` ne publie que les
dossiers qui portent au moins une page.** Ce qui n'est pas suivi par git ne porte pas de page
indexée, donc ne s'annonce plus — la clé devient exacte et reproductible d'un coup. `.githooks`
sort par la même règle : c'est de l'outillage, il ne porte rien.

L'autre issue possible — supprimer la clé, dérivable de `genere.non_pages` — n'a pas été prise :
elle aurait retiré du catalogue une information que ses consommateurs peuvent lire, pour
corriger un défaut qui tenait à sa définition, pas à son existence.

**Aucun des 413 autres artefacts n'a bougé** : 337 bandeaux, 74 zones AUTO de hub, la carte des
liens et le document humain de l'index sont identiques à l'octet.

---

## 5. Les vérifications

| Contrôle | Commande | Résultat |
|---|---|---|
| Contenu | `uv run AI/scripts/check_brain.py` | **0 violation dure, 111 avertissements** — le compte du lot 8, inchangé |
| Structure | `uv run AI/scripts/check_arbo.py` | **OK — chemin et catégorie concordent partout** |
| Artefacts | `uv run --project ../BrainKit brainkit generer --check` | **OK — les 414 artefacts concordent**, sortie 0 |
| Mesure | `uv run --project ../BrainKit brainkit mesurer` | **identique à l'octet** à la mesure d'avant la bascule, hors ligne d'en-tête |
| Pages | `git diff --stat` | aucune page du vault |

Le détail des 111, règle par règle : 62 `voisinage_declare`, 13 `collision_alias`, 13 + 11 + 1 +
1 `couverture_des_vues`, 5 `etiquettes_fermees/Ressources`, 4 `anti_repetition`, 1
`vocabulaire_ferme/axe_vide`. Ce sont exactement les comptes du lot 8.

---

## 6. Ce que le lot n'a PAS fait, et c'est volontaire

- **Aucune page touchée.** Ni les 337 briques, ni les 47 comparatifs, ni les 74 hubs, ni — sous
  aucun prétexte — les **297 notions**.
- **Aucune règle durcie, aucune sévérité changée, aucune règle nouvelle.** Le lot 8 a mesuré et
  proposé ; appliquer n'est le travail d'aucun lot à ce jour.
- **Aucune faute de contenu corrigée au passage** : les 8 sections `Alternatives` vides, les 3
  briques sans nature, les 5 valeurs `skill/*` orphelines, les 39 bandeaux à cellule vide, les 2
  sections mortes du gabarit (`brique.Retours`, `hub.Notes`) et les 2 champs vestigiaux
  (`brique.os`, `brique.domaines`) sont **toujours là**. `brainkit mesurer` les liste ; ce lot
  les regarde et n'y touche pas.
- **Rien n'a été poussé.** La branche reste locale, `main` est intacte.

---

## Remontées

*Ce qui a été trouvé hors du périmètre du lot, et qui ne s'y corrige pas. Une remontée nomme le
fait, dit ce qu'il coûte, et propose — elle ne tranche pas.*

**1 — Les deux skills du vault décrivent un outillage qui n'existe plus.** *(mesuré)*
`enrichir-brain/SKILL.md` cite `AI/scripts/arbo.py` comme « seule source de la dérivation » et
dit qu'un libellé de sous-domaine promu « doit être ajouté à `SUB_LABEL` dans `arbo.py` » — la
table est dans `brain.yml` depuis ce lot. Il donne aussi un `/tmp/ou.py` qui importe `arbo` :
celui-là **fonctionne toujours**, vérifié par exécution, parce que le pont garde l'API. Deux
autres phrases sont périmées : `check_brain.py` décrit comme le porteur des gabarits, et
`taxonomie.md` comme la source machine des énumérations (c'est le manifeste, et
`taxonomie.md` devient un document généré au sens du kit). Côté `cloturer-brain`, les sept
commandes sont **exactes** et tournent. Coût : un lecteur qui suit le skill à la lettre ira
modifier une table qui n'existe plus, ne verra pas d'erreur, et croira avoir déclaré un
libellé. Non corrigé : les skills sont hors du périmètre du lot, et le lot 7 de BrainKit les
**génère** depuis le manifeste — c'est là que la correction est structurelle, pas dans un patch
à la main. À trancher : régénérer les trois skills du vault depuis `brain.yml`, ou les corriger
à la main en attendant.

**2 — `.claude/settings.json` autorise une commande qui a changé de nature.** *(lot 10)*
La liste d'autorisations porte `Bash(uv run AI/scripts/check_brain.py)`, et le hook `Stop`
lance `stop_check_brain.py`, qui lance ce même fichier. Les deux **tournent** — vérifié par
exécution, sortie 0 et `OK — aucune violation dure. (111 avertissement(s))`. Mais la commande
a maintenant besoin que BrainKit soit atteignable, ce que la déclaration ne dit pas : sur une
machine où le kit manque, le hook rapportera une sortie 2 avec les trois pistes au lieu d'un
verdict. C'est le comportement voulu du pont, et c'est quand même une surprise pour qui lit
`settings.json`. Proposition : une ligne dans `Documentation/perso/machines.md` disant que le
vault a désormais une dépendance de poste, et laquelle.

**3 — Les sept scripts PowerShell parlent encore la v2.** *(hors kit)*
`audit-vault.ps1`, `report-ghosts.ps1`, `find-connexes.ps1`, `discover-links.ps1`,
`audit-links.ps1`, `add-wikilinks.ps1` et `gen-stubs-batch.ps1` raisonnent sur des « galaxies »,
sur `Services/` et sur `Wiki/` — un vocabulaire et une arborescence disparus à la clôture du
lot 4 de la migration v3, il y a trois jours. Leur `README` a été réécrit par ce lot et le dit ;
les scripts, non. Coût : `audit-vault.ps1` classe aujourd'hui les 765 pages en « sans galaxie ».
Ils ne sont dans le périmètre d'aucun lot de BrainKit — le kit ne les remplace pas, il ne les
connaît pas. Trois issues : les réécrire sur `brain-index.json`, les déclarer obsolètes en
tête de fichier, ou les retirer. La deuxième coûte cinq minutes et arrête le plus gros du
dommage.

**4 — Le manifeste et le vault se recopient l'un l'autre, sans contrôle.**
`brain.yml` est aujourd'hui identique à l'octet à `exemples/devbrain.brain.yml` du dépôt
BrainKit, et **rien ne le vérifie**. Le jour où l'un des deux bouge seul, le kit continuera de
tourner sans rien dire, et le test de fidélité du lot 2 cessera d'être reproductible en
silence. Coût : nul aujourd'hui, entier au premier correctif de manifeste. Proposition : ou
l'exemple du kit devient une **copie déclarée** de l'instance (un pointeur, pas un fichier), ou
le jeu d'épreuve du kit compare les deux sha256 et échoue s'ils divergent. La seconde est de
loin la moins chère.

**5 — `AI/design/brain-v3.md` et `AI/design/v3-arborescence.md` décrivent l'ancien monde.**
*(constat, pas urgence)* La spec de référence du vault nomme `check_brain.py` et `arbo.py`
comme les porteurs des règles et de la dérivation, et son §10 énonce les dix règles comme si
elles vivaient dans le code du vault. Ce n'est plus vrai depuis aujourd'hui. Ces documents
restent **justes sur le fond** — la v3 est ce que le manifeste décrit — et faux sur le *où*.
Non corrigé : réécrire une spec de 1 000 lignes n'est pas un effet de bord acceptable pour un
lot d'outillage. Proposition : un encart en tête de `brain-v3.md` renvoyant à `brain.yml` pour
tout ce qui est valeur, et laisser le corps tel quel — il documente le raisonnement, que le
manifeste ne porte pas.

**6 — `Archive-v1.zip` et `Documents/` méritent une décision, pas un silence.** *(mineur)*
Le premier est un binaire de 1 fichier à la racine d'un vault Obsidian ; le second est un
dossier de domaine à **3 pages**, le plus petit du vault, qui n'apparaît dans aucun des 20
préfixes sous ce nom-là (il vient de `docs/*`). Aucun des deux n'est un défaut : le zip est une
archive assumée, et un domaine à 3 pages est légal. Ils sont nommés ici parce que le lot les a
regardés en établissant le nouveau `scanned` et qu'il valait mieux l'écrire que de les
retrouver plus tard sans savoir s'ils avaient été vus.

---

## Ce que floSa doit lancer pour intégrer

Le lot **n'a rien poussé** : la branche est locale, `main` est intacte, l'intégration est sa
décision.

```bash
git fetch origin
git log main..origin/main --oneline          # doit être vide
git switch main
git merge --ff-only claude/brainkit-lot9-devbrain-8463bb
git push origin main
```

Et, côté BrainKit — dépôt sans remote, rien à pousser : les trois commits du lot 9 y sont déjà
sur `main`.
