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

**Fait au 2026-09-04 — 15 domaines sur 20.** Le pilote, puis les 14 plus petits en une
session : `Outils de développement` (20 pages), `Signal & audio` (3), `Design & diagrammes`
(7), `Calcul distribué` (7), `Web & API` (6), `Stockage` (6), `Automatisation no-code` (5),
`Médias` (4), `Interfaces & apps data` (4), `Sécurité` (3), `Observabilité` (3), `Réseau`
(2), `Documents` (2), `DevOps` (2). Restent `Machine Learning`, `LLM & IA générative`,
`Data & pipelines`, `Statistiques & inférence` et `Mathématiques` — les 5 gros, et les
seuls à porter des notions à recatégoriser au lot 4.

### Pour chaque domaine

1. Créer l'arborescence du domaine et ses sous-dossiers.
2. `git mv` chaque page vers son dossier dérivé de `categorie:`.
3. Créer la page `hub` de chaque dossier créé, avec sa zone `<!-- AUTO -->` vide.
4. Faire du **hub de domaine** le descendant de ce qui jouait déjà son rôle, par `git mv` :
   - la notion chapeau homonyme quand elle existe — le seul cas est
     `Wiki/Concepts/Bases de données.md`, fusionnée avec `MOC/Categories/Bases de données.md` ;
     son corps écrit à la main devient le corps du hub, la liste générée devient la zone `AUTO` ;
   - sinon, et c'est le cas général, `MOC/Categories/<Domaine>.md` elle-même : son
     frontmatter passe `type: moc` -> `role: hub`, son corps est réécrit au gabarit §9.
     Cf. remontée 6.
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

État au 2026-09-04, après le pilote et les 14 plus petits domaines (**15 sur 20**).

- [ ] `Dev/`, `Wiki/` et `MOC/` n'existent plus — *5 domaines restants (Machine
      Learning, LLM & IA générative, Data & pipelines, Statistiques & inférence,
      Mathématiques) ; 524 pages encore sous `Dev/` et `Wiki/`.*
- [x] Le chemin de chaque page concorde avec son `categorie:` — vérifié en dur par
      `AI/scripts/check_arbo.py`, vert sur les 121 pages migrées dans 15 domaines.
- [x] Chaque dossier porte une page `role: hub` à son nom — 23 hubs, contrôlé par
      `check_arbo.py` à tous les niveaux du chemin, pas seulement la feuille.
- [x] Aucun wikilink cassé — `check_brain.py` vert (0 violation dure),
      `build_links.py` : 0 lien non résolu sur 668 pages.
- [x] `build_mocs.py` remplit les zones `AUTO` des 23 hubs — et ne crée plus la MOC
      d'un domaine migré, les boucles `MOC/` filtrant sur `Dev/` et `Wiki/`.
      `MOC/Categories/` ne garde que les 5 domaines restants.
- [x] Aucun fichier perdu — 796 fichiers `.md`/`.base` avant le lot, 803 après :
      −1 fusion documentée (`MOC/Categories/Bases de données.md`), +8 hubs de
      sous-domaine. Les 14 autres MOC de domaine ne disparaissent pas, elles
      **deviennent** les hubs de domaine par `git mv`.

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

**Conséquence pour les domaines suivants** : avant de créer une page, vérifier que son
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

C'est le point à ne pas oublier dans les conversations suivantes : un comparatif dont
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
- ~~**`Wiki/Outils/Obsidian.md`** va dans « Outils de développement/ »~~ — **fait** le
  2026-09-04 avec le domaine, via `arbo.DOM_RATTACHE` ; cf. remontée 9.
- **Les 9 comparatifs sans filtre `categorie`** restent dans `Dev/Patterns/` : leur
  domaine se pose à la main, aucun n'appartient à « Bases de données ». 3 d'entre eux
  ont été traités depuis — cf. remontée 7, qui montre que leur filtre de chemin **casse**
  quand leurs membres descendent, et qu'attendre n'est donc pas neutre.

## Remontées — les 14 plus petits domaines, 2026-09-04

74 pages et 9 comparatifs, du domaine « Outils de développement » (20 pages) au domaine
« DevOps » (2 pages). La méthode du pilote a tenu sans retouche ; ce qui suit est ce
qu'elle n'avait pas rencontré.

### 6. Une MOC de domaine ne disparaît pas, elle DEVIENT le hub

Le pilote avait un cas particulier : une notion chapeau homonyme existait
(`Wiki/Concepts/Bases de données.md`), c'est elle qui a été déplacée vers le hub, et
`MOC/Categories/Bases de données.md` a disparu dans la fusion. Aucun des 14 domaines
suivants n'a de notion chapeau. La MOC de domaine y est donc le **seul ancêtre** du hub.

Elle est déplacée par `git mv` vers `<Domaine>/<Domaine>.md`, puis son frontmatter passe
`type: moc` -> `role: hub` et son corps est réécrit au gabarit §9. Trois raisons :

1. C'est ce qu'annonce la spec (§4, « `MOC/Categories/*` → les pages `hub` de domaine »).
2. L'historique git du fichier est conservé.
3. Aucun `rm` — et le compte de fichiers reste lisible : +1 par sous-dossier créé, 0 par
   domaine. Sans ce `git mv`, il aurait fallu supprimer 14 MOC devenues fausses, ou les
   laisser mentir : `build_mocs.py` cesse de les régénérer dès que leurs pages quittent
   `Dev/`, mais il ne les vide pas.

À faire pour chacun des 5 domaines restants.

### 7. Le piège des `.base` a une SECONDE forme, invisible au script de migration

La remontée 3 du pilote décrivait des comparatifs filtrant sur
`file.path.startsWith("Dev/Services/")` **plus** une `categorie ==`. Ceux-là,
`migrate_lot3_arbo.py` les voit : il les déplace avec leur domaine, et on retire la clause
de chemin.

Neuf comparatifs ne filtrent sur **aucune** `categorie:` — ils croisent le chemin avec un
tag ou une liste de noms. Le script ne peut pas les voir, ils restent dans `Dev/Patterns/`,
et leur vue **se vide au fur et à mesure que leurs membres descendent dans l'arbre**. Deux
l'ont fait sous nos yeux : `Comparatif - Traitement du signal` est tombé de 3 membres à 0,
`Comparatif - Frameworks CLI` de 1 à 0. Rien ne le signale dans Obsidian ; seul `R8b` de
`check_brain` le voit, et seulement en dessous de 2 membres.

Traitement des trois comparatifs dont nos domaines déplaçaient les membres :

| Comparatif | Clause de chemin remplacée par | Effet |
|---|---|---|
| Traitement du signal | `role == "brique"` | 3 membres, ensemble identique à avant — les 5 notions `concept/signal` portent le même tag et n'ont jamais eu à entrer dans un comparatif. Déplacé dans « Signal & audio/ ». |
| Frameworks CLI | `categorie == "devtools/cli"` | 2 membres (Typer, Rich). `file.hasTag("cli")` ne tenait que par le filtre de dossier : hors de `Dev/Services/`, le tag ramasse aussi croc (transfert de fichiers) et trois agents de code. Déplacé dans « Outils de développement/ ». L'avertissement R8b « 1 membre » disparaît. |
| Frontends web légers | `role == "brique"` | 5 membres inchangés, la liste de noms sélectionnant seule. **Reste dans `Dev/Patterns/`** : il enjambe « Web & API » (FastAPI, HTMX) et « Interfaces & apps data » (Streamlit, Gradio, Dash). |

`role == "brique"` est la traduction fidèle de ce que le chemin disait — un comparatif
compare des briques — et elle ne bouge pas avec l'arbre. C'est la substitution à faire
par défaut.

**Les 6 comparatifs sans `categorie:` qui restent** (Boosting, Détection & segmentation,
Détection d'anomalies, Forecasting, NLP, Réduction de dimension) portent tous des membres
de « Machine Learning ». Leur clause de chemin cassera au moment où ce domaine descendra.
À traiter dans cette conversation-là, pas avant.

### 8. Le seuil de promotion peut capturer 100 % d'un domaine

« Stockage » a 6 pages, toutes en `storage/objet`. « Automatisation no-code » en a 5,
toutes en `automation/no-code`. Le seuil de 5 promeut donc le sous-domaine, et le dossier
de domaine se retrouve **sans aucune page à son niveau**, avec un unique fils qui le
redouble : `Stockage/Stockage objet/`, `Automatisation no-code/No-code/`.

La règle 2 de `brain-v3.md` §4 est mécanique et ne prévoit pas ce cas. Elle est appliquée
telle quelle — aucun arbitrage n'est permis au lot 3, et `check_arbo.py` l'exige de toute
façon. Les deux dossiers sont des places réservées : ils prendront leur sens le jour où le
domaine gagne un second sous-domaine (`storage/bloc`, `storage/fichier`, `automation/rpa`).

**À trancher hors lot 3**, en une ligne dans `arbo.py` si la réponse est oui : plafonner la
promotion quand elle capture la totalité du domaine, ou l'assumer.

### 9. `skill/*` n'est pas un domaine — l'exception est nommée, pas absorbée

`Wiki/Outils/Obsidian.md` porte `categorie: skill/knowledge`, qui n'est pas un des 20
préfixes de `DOM_LABEL`. L'arbitrage de floSa du 2026-09-04 l'envoie dans
« Outils de développement/ ».

Deux façons de l'écrire, et la première est mauvaise : ajouter `"skill"` à `DOM_LABEL`
ferait mentir le commentaire qui en fait la copie conforme de `CAT_LABEL`, et rendrait
l'arbitrage indistinguable d'un vrai domaine. La table `arbo.DOM_RATTACHE` a donc été
créée pour ça : les préfixes qui ne sont pas des domaines et qu'une décision explicite
rattache quand même à un dossier, avec la date de la décision en commentaire.
`arbo.domaine()` consulte les deux ; `migrate_lot3_arbo.py` accepte désormais un préfixe
rattaché (`uv run … skill`) au lieu de refuser tout ce qui n'est pas dans `DOM_LABEL`.

`Wiki/Outils/` est maintenant vide. Le dossier reste sur le disque mais git ne le suit
plus. Le scaffold annoncé par `CLAUDE.md` pour la remigration v1 est donc à recréer le
jour où cette remigration a lieu — ou, plus probablement, à ne pas recréer du tout, la
v3 n'ayant plus de galaxie `Wiki/`.

### 10. Une MOC de sous-hub wiki reste en arrière, vidée sans être régénérée

`MOC/Concepts/Gestion des connaissances.md` (`indexe: skill/knowledge`) ne listait
qu'Obsidian. Obsidian ayant quitté `Wiki/`, `build_mocs.py` ne construit plus ce groupe
et ne repasse donc jamais sur la page : sa zone `AUTO` garde la liste d'avant.

Le contenu est resté juste par chance (la fiche n'a pas changé) et le lien nu résout
toujours, donc aucun validateur ne bronche. Ce n'est pas une raison de la laisser : c'est
la même mécanique que la remontée 6, sur l'étage `MOC/Concepts/`. La différence est
qu'aucun dossier ne porte ce nom, donc aucun hub ne l'accueille — elle disparaîtra avec
`MOC/`, en fin de lot 3. Notée pour qu'on ne s'étonne pas de la trouver là.

### 11. Trois écarts entre `v3-arborescence.md` et la population réelle

Le tableau par domaine de `v3-arborescence.md` a été mesuré avant le lot 2. Trois écarts
sont apparus, tous du même genre, et aucun n'est une contradiction à trancher :

- **« Signal & audio » : 3 pages migrées, pas 8.** Le document liste 7 pages dans un
  sous-dossier `Traitement/`, dont 5 notions ([[Traitement du signal]],
  [[Filtrage numérique]], [[Transformée de Fourier]], [[STFT et spectrogramme]],
  [[Ondelettes]]). Ces 5 portent `concept/signal`, pas `signal/traitement` : leur
  recatégorisation est le **lot 4**. Le sous-dossier n'existe donc pas encore — le seuil
  de 5 n'est pas atteint par les 2 briques restantes. C'est exactement l'écart déjà
  signalé pour `Bases de données vectorielles` dans la remontée 5 : le document décrit
  l'état visé **après** le lot 4. C'est le seul domaine des 14 concerné.
- **`Wiki/Outils/Obsidian.md` n'est dans aucun tableau** — cf. remontée 9.
- **Les libellés de sous-dossier manquants** ont été lus dans le document et ajoutés à
  `SUB_LABEL` : `Notebooks`, `Diagrammes`, `Stockage objet`, `No-code`. Le garde-fou a
  fonctionné comme prévu — le script s'arrête plutôt que d'inventer un nom.

### 12. Le vocabulaire des tags est une règle DURE, y compris sur un hub

Trois hubs ont été refusés par `check_brain` sur des tags inventés (`tooling`, `python`,
`jupyter`, `audio`, `literate-programming`, `test`). `tags:` est contrôlé contre les 319
valeurs de `Documentation/general/tags.md`, sans exception pour `role: hub`.

De même, R5 a signalé une collision d'alias entre deux hubs : `Automatisation no-code`
portait l'alias `no-code`, qui est le `nom:` du hub de sous-domaine `No-code`. Deux pages
d'aiguillage que le même jeton désigne se disputent la résolution d'un lien nu. L'alias a
été retiré du parent.

À retenir pour les 5 domaines restants : écrire le frontmatter d'un hub en lisant
`tags.md`, et ne pas donner au hub de domaine un alias qui est le nom d'un de ses
sous-hubs.

## Prompt à coller dans une conversation neuve — les 5 domaines restants

Restent « Machine Learning » (241), « LLM & IA générative » (131), « Data & pipelines »
(46), « Statistiques & inférence » (47) et « Mathématiques » (27). Ce sont eux qui portent
les 205 notions non catégorisées, et le lot 4 devra repasser derrière — d'où l'ordre :
les deux moyens d'abord, `Machine Learning` et `LLM` en dernier.

La passe de dénudage des liens est faite une fois pour toutes : ne pas la rejouer.

```
Lis AI/design/brain-v3.md, AI/design/v3-arborescence.md puis
AI/migration/lot-3-arborescence.md — dont les DEUX séries de Remontées.

Applique le lot 3 pour le domaine « <DOMAINE> » uniquement, et arrête-toi là.

Méthode, rodée sur 15 domaines :
  uv run AI/migration/scripts/migrate_lot3_arbo.py <prefixe> --dry-run
  puis sans --dry-run. Si le script s'arrête sur un sous-domaine sans libellé,
  le lire dans v3-arborescence.md et l'ajouter à SUB_LABEL de AI/scripts/arbo.py.

Puis, dans cet ordre :
  - `git mv MOC/Categories/<Domaine>.md` vers `<Domaine>/<Domaine>.md`, passer son
    frontmatter en `role: hub` et réécrire son corps au gabarit §9 (remontée 6) ;
  - créer les hubs des sous-dossiers promus, en lisant `Documentation/general/tags.md`
    pour les `tags:` — c'est une règle dure (remontée 12) ;
  - citer les nouveaux hubs dans `Home.md`, sinon R7 les déclare inatteignables ;
  - retirer le filtre `file.path.startsWith("Dev/...")` des .base déplacés, ET
    des comparatifs SANS filtre `categorie` dont ce domaine emporte les membres
    (remontée 7 — le script ne les voit pas et leur vue se vide en silence) ;
  - régénérer build_index / build_mocs / build_links, vérifier avec check_brain.py
    ET check_arbo.py.

Aucun rm : uniquement git mv. Clôture avec le skill cloturer-brain.
```
