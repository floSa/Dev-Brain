---
galaxie: meta
nom: lot-3-arborescence
type: gouvernance
created: 2026-09-04
tags: [meta, migration, v3]
---

# Lot 3 — Déplacement des fichiers vers l'arbre unique

Effort : **une session par groupe de domaines**. C'est le lot le plus visible et le plus
mécanique. Il doit tourner **seul** : aucun autre lot ne touche des fichiers en même temps.

Prérequis : lot 2 fait, validateur au vert.

## Contexte

`Dev/Services` porte 297 fichiers à plat, `Wiki/Concepts` 299. Aucun sous-dossier nulle part.
Le volet fichiers d'Obsidian est donc inutilisable pour se repérer, et le seul découpage
existant — `Services/` contre `Outils/` — a été mesuré non discriminant.

La v3 remplace les deux galaxies par **un arbre de domaines**. La nature de la page, elle, est
déjà portée par `role:` depuis le lot 2.

Arbre complet, page par page : [[AI/design/v3-arborescence|v3-arborescence]].

## Périmètre

- Déplacement de 682 fichiers par `git mv`.
- Création des dossiers et des pages `hub`.
- Suppression de `MOC/` (39 pages), absorbé par les hubs.
- `build_mocs.py`, qui cesse de générer `MOC/` et génère les zones `AUTO` des hubs.

**Hors périmètre** : le corps des fiches, la recatégorisation des notions, les comparatifs.

## Règle de rangement — mécanique, aucun arbitrage

1. Un dossier par domaine, nommé avec son libellé français (table `DOM_LABEL` de la spec,
   reprise de `CAT_LABEL` de `build_mocs.py`).
2. Un sous-dossier dès qu'un sous-domaine atteint **5 pages**. En-dessous, les pages restent au
   niveau du domaine.
3. Le chemin se **dérive** de `categorie:`. Personne ne choisit un dossier.
4. Tout dossier porte une page à son nom, `role: hub`.

## Procédure

### Ordre des domaines

Commencer par **Bases de données** : 47 pages, quatre sous-dossiers propres, **zéro notion à
arbitrer**. C'est le domaine qui valide la méthode au moindre risque.

Ensuite, par taille croissante de difficulté : `Data & pipelines`, `Outils de développement`,
les 15 petits domaines, puis `LLM` et `Machine Learning` en dernier — ce sont eux qui portent
les notions non catégorisées, et le lot 4 devra repasser derrière.

### Pour chaque domaine

1. Créer l'arborescence du domaine et ses sous-dossiers.
2. `git mv` chaque page vers son dossier dérivé de `categorie:`.
3. Créer la page `hub` de chaque dossier créé, avec sa zone `<!-- AUTO -->` vide.
4. Fusionner la notion chapeau homonyme dans le hub quand elle existe — cas
   `Wiki/Concepts/Bases de données.md` et `MOC/Categories/Bases de données.md`, qui sont la
   **seule collision de nom du vault** et listent les mêmes briques. Le corps écrit à la main
   de la notion devient le corps du hub ; la liste générée devient la zone `AUTO`.
5. Relancer `build_mocs.py` pour remplir les zones `AUTO`.
6. Vérifier qu'aucun wikilink n'est cassé.

### Les wikilinks — **tranché le 2026-09-04 : le nu, partout, en une passe**

Arbitrage de floSa, appliqué **avant** le premier `git mv` et non domaine par domaine.
Mesures prises sur `e2e1bc2` : 4 347 liens nus contre 4 489 qualifiés — la convention
qualifiée n'était suivie qu'une fois sur deux, et la raison qui l'avait posée (collisions
de nom entre le réservoir v1 et la v2) est périmée. Ne convertir que les 670 liens qui
cassaient sur « Bases de données » aurait laissé 3 819 liens à recasser vingt fois.

Fait : `AI/migration/scripts/migrate_lot3_liens_nus.py`, 4 477 liens dénudés dans
551 fichiers, corps **et** frontmatter. Zéro lien qualifié restant dans les 646 pages.
La convention est réécrite dans `CLAUDE.md` et dans le skill `enrichir-brain`.

Contrepartie, désormais la seule contrainte : **un nom de fichier doit être unique dans
le vault**, à la casse près. Voir la première remontée.

## Critères d'acceptation

État au 2026-09-04, après le domaine pilote « Bases de données » (1 domaine sur 20).

- [ ] `Dev/`, `Wiki/` et `MOC/` n'existent plus — *19 domaines restants ; 598 pages
      encore sous `Dev/` et `Wiki/`.*
- [x] Le chemin de chaque page concorde avec son `categorie:` — vérifié en dur par
      `AI/scripts/check_arbo.py`, vert sur les 47 pages migrées.
- [x] Chaque dossier porte une page `role: hub` à son nom — 5 hubs, contrôlé par
      `check_arbo.py` à tous les niveaux du chemin, pas seulement la feuille.
- [x] Aucun wikilink cassé — `check_brain.py` vert (0 violation dure),
      `build_links.py` : 0 lien non résolu sur 650 pages.
- [x] `build_mocs.py` remplit les zones `AUTO` des hubs — et ne crée plus la MOC du
      domaine migré, les boucles `MOC/` filtrant sur `Dev/` et `Wiki/`. `MOC/` survit
      pour les 19 domaines restants, comme prévu.
- [x] Aucun fichier perdu — 796 fichiers `.md`/`.base` avant, 799 après : −1 fusion
      documentée (`MOC/Categories/Bases de données.md`), +4 hubs de sous-domaine.

## Interdictions

- **Aucun `rm`.** Un `git mv` déplace, il ne supprime pas. Les seules disparitions autorisées
  sont les fusions de l'étape 4, et chacune s'écrit dans les *Remontées*.
- Ne pas modifier le corps des fiches, sauf le corps du hub issu de la fusion.
- Ne pas recatégoriser une notion — c'est le lot 4. Une notion sans sous-domaine reste au
  niveau de son domaine, en attente.


## Remontées — domaine pilote « Bases de données », 2026-09-04

### 1. Le vault portait DEUX collisions de nom, pas une — corrigée avant le lot

Ce document annonçait `Wiki/Concepts/Bases de données.md` contre
`MOC/Categories/Bases de données.md` comme **seule collision du vault**. La mesure qui
l'établissait était sensible à la casse et en a raté une : `Dev/Services/hdbscan.md`
(la bibliothèque, nom du paquet PyPI) contre `Wiki/Concepts/HDBSCAN.md` (la notion).

Ce n'était pas une gêne de confort. Le lot 4 recatégorise les notions vers l'arbre des
domaines : les deux pages allaient atterrir dans le même dossier, et le vault vit sur
**Windows + OneDrive**, dont le système de fichiers ne distingue pas la casse. Les deux
fichiers n'y coexistent pas — le `git mv` aurait échoué, au lot 3 ou au lot 4.

Réglé avant la passe de dénudage : la **notion** est renommée
`Clustering hiérarchique par densité` (une notion se nomme par le concept ; « hdbscan »
est le nom du paquet, fixé par le monde extérieur). Aucun alias « HDBSCAN » n'est posé
sur elle — le jeton appartient à la brique, un alias rouvrirait la collision côté
résolution. Les 14 liens concernés (10 nus, 4 qualifiés) sont retargetés un par un :
les 14 parlaient de la méthode, jamais du paquet.

**Conséquence pour les 19 domaines suivants** : avant de créer une page, vérifier que son
nom de fichier est unique dans le vault, à la casse près. C'est la contrepartie du lien nu,
et elle est maintenant écrite dans `CLAUDE.md` et dans le skill `enrichir-brain`.

### 2. La fusion de l'étape 4 — une disparition, documentée

`MOC/Categories/Bases de données.md` disparaît. C'est la seule disparition du lot, et elle
est prévue par l'étape 4.

`Wiki/Concepts/Bases de données.md` est déplacée par `git mv` vers
`Bases de données/Bases de données.md` — son corps écrit à la main devient le corps du hub,
son historique git est conservé. Son frontmatter passe `role: notion` -> `role: hub` et perd
`categorie: concept/data` : **un hub ne se range pas, il EST le rangement**. La liste générée
que portait la MOC est reproduite par `build_mocs.py` dans la zone `AUTO` du hub — elle n'est
pas recopiée, elle est régénérée.

Le corps de la notion n'est pas restructuré au gabarit `hub` de la spec §9 (« Ce qu'il faut
comprendre » / « Choisir ») : c'est un travail de gabarit, donc le lot 6. Il en résulte une
redite temporaire entre sa section « Approches voisines & alternatives » et la zone `AUTO`.
Assumée, et à résorber au lot 6.

### 3. Les `.base` portaient un filtre de chemin qui cassait au déplacement

Les 47 comparatifs filtrent sur `file.path.startsWith("Dev/Services/")` (33) ou
`("Dev/Outils/")` (4) en plus de leur `categorie ==`. Ce chemin devient faux au `git mv` :
la vue se vide sans rien signaler.

Le filtre de chemin est **retiré** des 10 comparatifs déplacés. Il était de toute façon
redondant : `categorie == "database/vecteur"` ne peut désigner qu'une brique, les notions
portant `concept/*`. Les 37 autres seront traités au fil de leur domaine.

C'est le point à ne pas oublier dans les 19 conversations suivantes : un comparatif dont
la vue est vide ne lève aucune alerte, seul `check_brain` R8b le voit — et seulement s'il
tombe sous 2 membres.

### 4. Outillage — sept scripts touchés

`Dev/` et `Wiki/` étaient codés en dur. Le remplacement n'est pas une liste de domaines à
tenir à jour mais une **négative** : tout dossier de la racine qui n'est pas de l'outillage
porte des pages. Le jour où `Dev/` et `Wiki/` disparaissent, rien à changer.

| Script | Ce qui a changé |
|---|---|
| `build_index.py` | balaye la racine ; le réservoir v1 est un fait de `Wiki/`, plus de « hors `Dev/` » |
| `build_links.py` | idem ; résolvait déjà par nom de fichier, donc indifférent au dénudage |
| `build_mocs.py` | émet des liens nus ; remplit les zones `AUTO` des pages `role: hub`, périmètre = le DOSSIER |
| `check_brain.py` | gabarit `role: hub` ; R7 accepte hub, MOC et `Home.md` ; R15 accepte notion **ou** hub |
| `verifier_fraicheur.py` | reconnaissait une citation de fiche par `"[[Dev/" in ligne` — ne trouvait plus rien après dénudage |
| **`arbo.py`** *(nouveau)* | la dérivation `categorie:` -> chemin, écrite une seule fois |
| **`check_arbo.py`** *(nouveau)* | vérifie concordance chemin/catégorie, seuil de promotion, hub par dossier |

Le piège du réservoir v1 mérite d'être nommé : `is_active_v2` testait « pas sous `Dev/` »,
et `maturite` est un marqueur v1. Toute brique descendue dans l'arbre aurait été classée
réservoir et **sortie de l'index en silence**.

### 5. Ce que le lot 3 ne fait pas, et qui reste à faire

- **Les notions du domaine ne sont pas descendues.** `Bases de données vectorielles`,
  `Index ANN — internes`, `Migrations de schéma`, `ORM` sont dans la liste « Hors arbre »
  de `v3-arborescence.md` et portent `concept/data` : les recatégoriser est le lot 4.
  L'arbre de « Bases de données » ne porte donc aujourd'hui que des briques.
  Note : `brain-v3.md` §4 montre `Bases de données vectorielles.md` dans `Vectoriel/` —
  c'est l'état visé **après** le lot 4, pas après le lot 3.
- **Les 4 sous-hubs sont écrits à la main, le hub de domaine non.** Les cases
  « hub écrit » de `v3-arborescence.md` sont cochées pour les sous-domaines ; le hub de
  domaine garde le corps de la notion fusionnée, à réécrire au gabarit §9 au lot 6.
- **`Wiki/Outils/Obsidian.md`** (`categorie: skill/knowledge`, hors des 20 préfixes de
  `DOM_LABEL`) va dans « Outils de développement/ » — tranché par floSa le 2026-09-04.
  `v3-arborescence.md` ne l'assigne à aucun domaine : il est muet, il ne contredit pas.
  À appliquer dans la conversation « Outils de développement », pas ici.
- **Les 9 comparatifs sans filtre `categorie`** restent dans `Dev/Patterns/` : leur
  domaine se pose à la main, aucun n'appartient à « Bases de données ».

## Prompt à coller dans une conversation neuve — domaines suivants

La passe de dénudage des liens est faite une fois pour toutes : ne pas la rejouer.

```
Lis AI/design/brain-v3.md, AI/design/v3-arborescence.md puis
AI/migration/lot-3-arborescence.md — dont les Remontées du domaine pilote.

Applique le lot 3 pour le domaine « <DOMAINE> » uniquement, et arrête-toi là.

Méthode, déjà rodée sur « Bases de données » :
  uv run AI/migration/scripts/migrate_lot3_arbo.py <prefixe> --dry-run
  puis sans --dry-run. Si le script s'arrête sur un sous-domaine sans libellé,
  le lire dans v3-arborescence.md et l'ajouter à SUB_LABEL de AI/scripts/arbo.py.

Puis : créer les pages hub des dossiers créés, retirer le filtre
file.path.startsWith("Dev/...") des .base déplacés, régénérer, et vérifier avec
check_brain.py ET check_arbo.py.

Aucun rm : uniquement git mv. Clôture avec le skill cloturer-brain.
```
