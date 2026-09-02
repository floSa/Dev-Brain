---
name: enrichir-brain
description: |
  Use this skill to capture knowledge into the DevBrain v3 (the tree of 20 domain
  folders at the vault root). Triggers: "ajoute <techno/sujet> au brain",
  "documente <X>", "ajoute la brique Y", "ajoute le concept Z", or, at the end of a
  conversation, "mets a jour DevBrain" / "enrichis le brain" (sweep mode). Carries
  the v3 PROPAGATION RULE: the radius of an insertion is the destination folder plus
  its parent hubs — the neighbourhood of a page is `ls` of its folder, never a guess.
  Creates the requested page AND updates the folder's comparatif, notion and peer
  bricks, wires links both ways, keeps alternatives and pitches in sync. CAPTURE
  ONLY: closing the write (regenerate, validate, commit) belongs to the companion
  skill `cloturer-brain`. Also owns the UPDATE path — "le pitch de X a change",
  "X est abandonne", "reclasse X", a rename or a deletion: propagate the side
  effects of a changed field to its consumers (see *Procedure — mode mise a jour*).
---

# Skill — enrichir-brain

Skill de **capture** du DevBrain v3. Implémente `AI/design/brain-v3.md` §10 (la règle de
propagation) et §12. Exigence cardinale de floSa, formulée telle quelle : **quand on ajoute
une base de données, tout ce qui doit lui répondre doit être mis à jour, sans rien oublier.**

En v2, c'était impossible à garantir : « quelles sont les pages connexes ? » n'avait aucune
réponse mécanique, le skill devait les deviner à partir des tags et de l'index. Sept étapes
sur onze ne laissaient aucune trace vérifiable, et les omissions constatées tombaient toutes
dedans (audit axe 3).

La v3 change ça, parce que **le dossier porte le domaine**.

---

## La règle de propagation — le cœur de ce skill

> **Le rayon de propagation d'une insertion est le dossier d'accueil, plus ses hubs parents.**

Le voisinage d'une page cesse d'être une intuition : c'est `ls` de son dossier. Insérer
Qdrant dans `Bases de données/Vectoriel/` détermine, sans rien deviner :

| # | À mettre à jour | Comment il est trouvé | Qui le fait |
|---|---|---|---|
| **P1** | Le hub du dossier — `Vectoriel/Vectoriel.md` | c'est le dossier d'accueil | **généré** (zone AUTO) + corps à relire |
| **P2** | Les hubs parents — `Bases de données/Bases de données.md` | remontée de chemin | **généré** (zone AUTO) + corps à relire |
| **P3** | Le comparatif du dossier — le `.base` du dossier | `ls <dossier>/*.base` | vue : **automatique** (filtre par `categorie`) ; « ce qui départage » : **à écrire** |
| **P4** | La notion du sujet | le `role: notion` du sujet (cf. *L'exception notion*) | **à écrire**, dans les deux sens |
| **P5** | Les briques pairs — les autres `role: brique` du dossier | `ls <dossier>/*.md` | **à écrire**, réciprocité obligatoire |
| **P6** | Les pitchs réinjectés chez les pairs | `alternatives:` / `complements:` des pairs | **à écrire**, pitch copié jamais retapé — vérifié par `[V1]` |

**Aucune de ces six lignes ne se saute en silence.** Une ligne sans objet se déclare sans
objet (« pas de `.base` dans ce dossier »), elle ne se tait pas. C'est ce que contrôle
l'étape 8 de la procédure ciblée.

### Trouver le dossier d'accueil — dérivation, pas décision

Personne ne choisit un dossier : il se **dérive** de `categorie:` (`AI/scripts/arbo.py`,
seule source de la dérivation ; `check_arbo.py` la vérifie). La commande, à lancer une fois
la catégorie arbitrée :

```bash
cat > /tmp/ou.py <<'PY'
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""Ou se range une categorie ? — derivation officielle, sur la population reelle."""
import sys, json, pathlib
sys.path.insert(0, "AI/scripts")
import arbo
cat = sys.argv[1]
idx = json.loads(pathlib.Path("AI/index/brain-index.json").read_text(encoding="utf-8"))
cats = [p.get("categorie") for p in idx["pages"]
        if p.get("role") == "brique" and p.get("categorie")]
# `+ [cat]` : la page a inserer COMPTE dans le seuil de promotion. Inserer la 5e page
# d'un sous-domaine cree son dossier — la derivation doit le voir avant l'ecriture.
print(arbo.dossier_attendu(cat, arbo.promotions(cats + [cat])))
PY
uv run /tmp/ou.py "database/vecteur"     # -> Bases de données/Vectoriel
```

Deux cas à connaître :

- **La sortie est `None`** → le préfixe de la catégorie n'est pas un domaine connu. Ce n'est
  pas un bug à contourner : c'est une catégorie à arbitrer dans
  `Documentation/general/taxonomie.md`. **Demander.**
- **La sortie nomme un sous-dossier qui n'existe pas encore** → l'insertion fait franchir le
  seuil de 5 pages à un sous-domaine, et **promeut** un dossier. Ce n'est plus une insertion,
  c'est une réorganisation : le dossier se crée, ses pages y descendent par `git mv`, il
  prend un hub à son nom, et son libellé doit être ajouté à `SUB_LABEL` dans `arbo.py`.
  **Le signaler à floSa avant de le faire** — et vérifier le plafond du seuil (un
  sous-domaine ne se promeut pas s'il ne laisse aucune page au niveau du domaine).

### Lister le rayon — une commande, une liste fermée

```bash
D="Bases de données/Vectoriel"          # sortie de /tmp/ou.py
ls -1 "$D"                              # P3, P4, P5 : le rayon, en clair
dirname "$D"                            # P2 : le parent ; remonter jusqu'à la racine
```

Ce que `ls` rend, ligne par ligne : le hub du dossier (`<Dossier>.md`), le ou les `.base`
(P3), et les autres `.md` — les pairs (P5). Il n'y a rien d'autre à chercher, et c'est tout
l'intérêt de l'arbre : **plus rien à déduire des tags.**

### L'exception notion — datée, et la seule

P4 est la seule ligne que `ls` ne rend pas encore. Les **297 notions** vivent toujours sous
`Wiki/Concepts/`, et c'est le **lot 4** qui les descendra dans l'arbre. Jusque-là, la notion
du sujet se trouve par l'index, pas par le dossier :

```bash
uv run AI/scripts/query_index.py --role notion --categorie "concept/<sous-domaine>" --fields nom,path
```

Le hub du dossier la nomme souvent déjà, et la section `## Liens` d'un pair aussi — les lire
est le chemin le plus court. Après le lot 4, cette ligne rentrera dans le `ls` comme les
autres, et ce paragraphe disparaîtra.

---

## Quand l'utiliser

- **Mode ciblé** : ajouter une brique ou une notion précise. « ajoute Weaviate », « ajoute le concept bases vectorielles ».
- **Mode balayage** : en fin de conversation, « mets à jour DevBrain » → repérer tout ce qui mérite une page et tout traiter.
- **Mode mise à jour** : une page existe déjà et un champ change. « le pitch de X a changé », « X est abandonné », « reclasse X en `<catégorie>` », un renommage, une suppression. C'est le cas le plus dangereux : la page a des **consommateurs**. Voir *Procédure — mode mise à jour*.

Distinct de :
- `planifier-projet` (consomme le brain pour cadrer un projet, n'écrit pas de fiches) ;
- `cloturer-brain` (clôt l'écriture : régénère, valide, commite — ce skill-ci ne commite pas).

## Pré-requis

Mode **brain** (cf. `CLAUDE.md`). Le réservoir v1 est **hors du vault** depuis le lot 3
(cf. `Documentation/perso/reservoir-v1.md`) — s'il réapparaît sous une forme ou une autre,
c'est de la référence en lecture seule.

**Une notion existante ne se modifie que sur demande explicite** : c'est la mémoire perso de
floSa. La *créer* dans le cadre d'une capture est normal — c'est la ligne P4. La *réécrire*
ne l'est pas : proposer, et attendre.

## Appuis (à lire AVANT d'écrire)

- `AI/index/brain-index.json` — catalogue courant (`path`, pitch, tags, alternatives, complements, categorie, famille, role, maturite). **Ne jamais le charger en entier** : l'interroger par tranches via `AI/scripts/query_index.py`. La sortie est bornée par le nombre de correspondances, pas par la taille du brain.
- `AI/scripts/arbo.py` — la dérivation `categorie:` → chemin, écrite une fois. Ne pas la réimplémenter de tête.
- `Documentation/general/taxonomie.md` — les **deux axes** de rangement : `categorie:` (le domaine, 94 valeurs, arbre D1→D14) et `famille:` (la nature technique, 9 valeurs fermées, arbre F1→F9). Les deux se **dérivent** par arbre de décision, ils ne se choisissent pas à l'intuition. La section *Axe `role:`* y donne le vocabulaire des rôles.
- `Documentation/general/tags.md` — vocabulaire de tags **fermé**. Piocher ici, ne jamais inventer.
- `Documentation/general/themes.md` — vocabulaire `domaines:`.
- `Templates/Service-Dev.md`, `Templates/Concept-Wiki.md` — gabarits stricts.
- `AI/design/brain-v3.md` §5 à §9 — les gabarits de page par `role:`.

## Conventions v3 non négociables

- **Le dossier se dérive, il ne se choisit pas.** `categorie:` donne le domaine, `arbo.py` donne le chemin. Un fichier posé « là où ça semble logique » fait échouer `check_arbo.py`.
- **Trois champs, trois questions distinctes.** `categorie:` = de quoi ça parle (le domaine) · `famille:` = ce que c'est techniquement (paquet ? plateforme ?) · `role:` = ce que la page **est** éditorialement (`brique`, `notion`, `pattern`, `rule`, `hub`). Un `role: hub`, `pattern` ou `rule` ne porte **pas** de `categorie:` : un hub *est* le rangement, un pattern enjambe les domaines par construction, une règle est transverse par définition.
- **Ton impersonnel** partout : ni « tu » ni « vous ». Phrases courtes, parties + bullets.
- **Frontmatter exact** selon le gabarit du `role:` : ni plus, ni moins de champs. C'est `role:` qui choisit le gabarit que `check_brain.py` applique.
- **Pitch unique, une seule convention de réinjection** : chaque page porte SON `pitch:` (une ligne), écrit une seule fois. Une donnée, trois usages (frontmatter, sections `Alternatives` des autres pages, propositions de `planifier-projet`). La convention, en trois clauses :
  1. cible listée dans le frontmatter `alternatives:` → la ligne **commence par** le `pitch:` courant de la cible, à la normalisation près (`**` retirés, espaces réduits, casse ignorée) ; **suffixe libre autorisé après** ;
  2. cible absente du frontmatter `alternatives:` → mention de voisinage, ligne libre mais **préfixée de `voisin :`** ;
  3. jamais de prose à la place du pitch d'une cible listée en `alternatives:` — soit la prose devient le suffixe (clause 1), soit la cible sort du frontmatter (clause 2).

  Le pitch se **copie** depuis la cible, il ne se retape jamais.
- **Liens nus, toujours** : `[[Qdrant]]`, jamais `[[Bases de données/Vectoriel/Qdrant|Qdrant]]`. Le pipe ne sert qu'à changer le texte affiché (`[[Qdrant|la base vectorielle]]`), jamais à porter un chemin — un chemin casse au premier `git mv`, et le lot 3 en a fait 682 sans toucher un lien. Contrepartie : **le nom de fichier d'une page nouvelle doit être unique dans le vault**, à la casse près (le système de fichiers de floSa est insensible à la casse). Vérifier avant de créer, y compris pour un hub à créer.
- **Catégorie ou tag manquant → demander**, jamais inventer. L'ajout se fait d'abord dans `Documentation/general/`.
- **Faits vérifiés sur le web, d'office (sans demander la permission)** : avant d'écrire une fiche, vérifier en ligne (WebSearch / WebFetch) les champs factuels — `licence_type`, `langage`, `maturite`, `hosted`, `scaling`, `url_docs` / `url_repo`, statut actuel (actif / déprécié / racheté). Ne jamais demander l'autorisation de vérifier : le faire directement. Info introuvable ou ambiguë → laisser le champ vide, ne pas inventer.

---

## Procédure — mode ciblé

1. **Interroger l'état (par tranches, jamais l'index entier)** :
   ```bash
   uv run AI/scripts/query_index.py --name "<X>"                        # existence, nom + alias
   uv run AI/scripts/query_index.py --categorie "<cat>" --role brique   # les pairs
   ```
   Vocabulaire : `Documentation/general/tags.md`, `taxonomie.md` (fichiers bornés).

2. **Vérifier l'existence** de la page (nom + `alias`). Si elle existe → **basculer sur la
   *Procédure — mode mise à jour*** (ne pas improviser un patch : une page qui existe a des
   consommateurs). Vérifier aussi l'**unicité du nom de fichier** dans tout le vault :
   ```bash
   find . -iname "<X>.md" -not -path "./.git/*"
   ```

3. **Dériver la catégorie, la famille, puis le dossier.** Dans cet ordre — le dossier est une
   conséquence, pas une décision.
   - `categorie:` par l'arbre D1→D14 de `taxonomie.md` ; `famille:` par l'arbre F1→F9.
   - puis `uv run /tmp/ou.py "<categorie>"` (cf. *Trouver le dossier d'accueil*).

   Fin d'étape vérifiable : un chemin de dossier, pas une intuition.

4. **Lister le rayon de propagation** — `ls -1 "$D"` et la remontée des parents. Fin d'étape
   vérifiable : **la table P1→P6 remplie nominativement**, un fichier par ligne :

   ```
   P1 hub du dossier      : Bases de données/Vectoriel/Vectoriel.md
   P2 hubs parents        : Bases de données/Bases de données.md
   P3 comparatif          : Bases de données/Vectoriel/Comparatif - Bases vectorielles.base
   P4 notion              : Wiki/Concepts/Bases de données vectorielles.md
   P5 briques pairs       : Annoy, Chroma, Faiss, LanceDB, Milvus, Pinecone, Qdrant,
                            ScaNN, Weaviate, hnswlib, pgvector  (11)
   P6 pitchs à réinjecter : chez les pairs retenus en alternatives — à l'étape 7
   ```

   « Les pages connexes » n'est pas une liste. Ceci en est une.

5. **Vérifier les faits sur le web (d'office), puis écrire la page** depuis le gabarit de son
   `role:` (`brain-v3.md` §6 pour `brique`, §7 pour `notion`). Le fichier va dans `$D`.

6. **Poser les tags** depuis `tags.md` uniquement. Besoin d'un tag absent → le proposer,
   l'ajouter au vocabulaire, puis l'utiliser.

7. **Dérouler P1 à P6, ligne par ligne.** C'est l'étape qui remplace le « identifier les
   pages connexes » de la v2, et c'est elle qui porte tout le travail :

   - **P1 / P2 — les hubs.** Leur zone `<!-- AUTO -->` est **générée** : ne pas l'éditer à la
     main, `cloturer-brain` la régénère. En revanche, **relire le corps** (`## Ce qu'il faut
     comprendre`, `## Choisir`), écrit à la main : une brique qui change la donne du dossier
     doit apparaître dans `## Choisir`, sinon le hub ment par omission. Fin d'étape : soit une
     ligne ajoutée au corps du hub, soit la raison explicite de ne pas en ajouter.
   - **P3 — le comparatif.** Si le `.base` filtre par `categorie` (le cas normal), la nouvelle
     brique **entre toute seule** dans la vue : rien à faire, le vérifier suffit. S'il filtre
     par liste de noms codée en dur ou par chemin, **elle n'entrera jamais** : le signaler
     (`check_brain` le sort en `[WARN] R8d`). Pas de `.base` dans le dossier et ≥ 2 briques de
     la catégorie → en proposer un (`check_brain` le réclame déjà en `[WARN] R8a`).
   - **P4 — la notion.** La brique cite sa notion dans `## Liens` ; la notion cite la brique
     dans `## Approches voisines`. Les **deux** sens, sinon `check_brain` sort `[WARN] R15`.
     Notion absente → la créer (c'est une capture, pas une incursion). Notion existante à
     modifier → **demander** (cf. *Pré-requis*).
   - **P5 — les briques pairs.** Choisir parmi les pairs listés à l'étape 4 celles qui sont
     de vraies alternatives. Pour chacune : `alternatives:` **des deux côtés** (si A cite B,
     B cite A — `check_brain` R12 est dur là-dessus), **et** la section `## Alternatives` des
     deux pages (R11). Un pair écarté est un choix, pas un oubli : le dire.
   - **P6 — les pitchs.** Chaque puce ajoutée réinjecte le `pitch:` **courant** de sa cible,
     copié depuis la cible (R1). Vérifier avec `[V1]` (ci-dessous) avant de passer à l'étape 8.

8. **Contrôle final — énumérer ce qu'on a touché, et le confronter au dossier.** Étape
   obligatoire, et c'est elle qui rend la propagation vérifiable plutôt que promise :

   ```bash
   git status --porcelain                    # ce qui a bougé, en fait
   ls -1 "$D"                                # ce qui aurait dû être considéré
   ```

   Confronter les deux listes, et **rendre compte des trois cas** :

   | Cas | Ce qu'on en fait |
   |---|---|
   | Fichier du dossier **touché** | normal, il est dans le rayon |
   | Fichier du dossier **non touché** | **déclarer pourquoi** (« pas une alternative de X »). Le silence n'est pas une réponse |
   | Fichier touché **hors du dossier** | légitime pour P2 (hubs parents) et P4 (notion) ; **suspect** partout ailleurs — l'expliquer ou le défaire |

   Un écart se **signale**, il ne se tait pas. C'est la sortie attendue de ce skill, pas une
   formalité : la v2 échouait précisément parce que cette confrontation n'existait pas.

9. **Clôturer** : invoquer le skill `cloturer-brain`. Il régénère les artefacts, fait passer
   `check_brain.py` **et** `check_arbo.py` au vert, vérifie la divergence avec `origin/main`,
   puis commet et intègre. La capture n'est pas finie tant que la clôture n'a pas tourné —
   mais elle ne fait pas partie de ce skill-ci.

**Sortie explicite attendue de ce skill** : la table P1→P6 remplie, le résultat du contrôle
de l'étape 8, et « la capture est faite, la clôture reste à lancer » — ou, si
`cloturer-brain` a déjà tourné, son résultat. Ne jamais laisser l'état implicite : c'est
ainsi qu'un index périmé survit à une session.

---

## Procédure — mode mise à jour

Déclencheurs : « enrichis la fiche X depuis cet article », « le pitch de X a changé »,
« X est abandonné », « reclasse X en `<catégorie>` », un renommage, une suppression — et
l'étape 2 de la procédure ciblée quand la page existe déjà. `CLAUDE-build.md` (workflow
général, point 5) renvoie ici.

**Règle d'or** : une modification de champ n'est pas finie quand la page est enregistrée.
Elle est finie quand ses **consommateurs** sont à jour et que la **commande de vérification**
de la table ci-dessous ne renvoie plus aucun écart. Une page qui existe a des consommateurs ;
une page qu'on crée n'en a pas. C'est toute la différence avec la procédure ciblée.

**La règle de propagation s'applique ici aussi, et elle borne le travail** : un champ modifié
se propage **au dossier de la page**, pas au vault entier. Le rayon est le même — P1 à P6 —
et la colonne *Rayon* de la table dit, champ par champ, laquelle de ces lignes bouge. Un seul
champ fait exception et sort du dossier : `categorie:`, qui **déplace la page** et lui fait
donc changer de rayon.

1. **Relever l'état avant**, avant toute écriture. Le chemin se lit dans l'index, il ne se
   suppose pas :
   ```bash
   uv run AI/scripts/query_index.py --name "<X>" --fields nom,path   # le chemin réel
   sed -n '/^---$/,/^---$/p' "<chemin>" | tee /tmp/avant-X.txt
   ```
   Fin d'étape vérifiable : le fichier contient la valeur d'origine de chaque champ.

2. **Déclarer les champs qui changent**, un par un, sous la forme `champ : avant → après`.
   Fin d'étape vérifiable : une liste explicite. Un champ absent de cette liste n'a pas le
   droit de bouger — l'étape 5 le contrôle.

3. **Dresser la liste nominative des consommateurs** : pour chaque champ déclaré, lire sa
   ligne dans la *table des effets de bord* et lancer sa **commande d'inventaire**. Fin
   d'étape vérifiable : une liste de **chemins de fichiers**, pas une intention. « Les
   citeurs de X » n'est pas une liste ; `Bases de données/Vectoriel/Milvus.md, …/Weaviate.md`
   en est une.

4. **Vérifier les faits sur le web (d'office)** si un champ factuel change (`maturite`,
   `licence_type`, `langage`, `url_docs`, `url_repo`). Fin d'étape vérifiable :
   source citée, ou champ laissé vide — jamais deviné.

5. **Patcher la page, section par section** — jamais de réécriture intégrale. Fin d'étape
   vérifiable :
   ```bash
   git diff --stat -- "<chemin>"   # un seul fichier, delta borné
   git diff -- "<chemin>"          # aucun champ hors de la liste de l'étape 2
   ```

6. **Propager chaque consommateur `[M]`** de la liste de l'étape 3. Le pitch se **copie**
   depuis la cible, il ne se retape pas. Fin d'étape vérifiable : chaque fichier de la liste
   de l'étape 3 apparaît dans `git diff --name-only`. Un fichier de la liste absent du diff =
   propagation oubliée.

7. **Lancer la commande de vérification de chaque champ modifié** (colonne *Vérification*
   de la table). Fin d'étape vérifiable : **0 écart** sur chacune. Ne pas passer à l'étape 8
   avec un écart restant — c'est exactement ainsi que naissent les pitchs périmés.

8. **Régénérer, puis contrôler que la régénération a bien pris** — ne pas la croire sur
   parole :
   ```bash
   uv run AI/scripts/build_index.py && uv run AI/scripts/build_mocs.py && uv run AI/scripts/build_links.py
   uv run AI/scripts/query_index.py --name "<X>" --fields nom,path,pitch,categorie,famille,role,maturite
   grep -rln "<X>" --include="*.md" . | grep -v "^\./\.git/"   # dont les hubs qui la citent
   ```
   Fin d'étape vérifiable : l'index renvoie les valeurs **après**, et la page apparaît dans
   les hubs attendus — et plus dans ceux qu'elle a quittés.

9. **Contrôle final, identique à l'étape 8 du mode ciblé** : `git status --porcelain`
   confronté au `ls` du dossier de la page. Le diff doit contenir exactement : la page, les
   fichiers de l'étape 3, les artefacts générés. Rien d'autre. Un fichier inattendu dans ce
   diff est une erreur, pas une surprise.

10. **Clôturer** : invoquer `cloturer-brain`. Il est idempotent, donc relancer la
    régénération ne coûte rien, et c'est lui qui porte la validation finale, la
    vérification de divergence et l'intégration.

### Table des effets de bord — champ modifié → consommateurs → vérification

Conventions de la colonne *Consommateurs* : **[M]** propagation manuelle obligatoire (rien
ne la fera à votre place) · **[G]** corrigé par relance d'un générateur · **[D]** déjà
couvert par une règle dure de `check_brain` ou `check_arbo` · **[!]** dérive silencieuse,
aucun contrôle n'existe encore. La colonne *Rayon* renvoie aux lignes P1→P6 de la règle de
propagation : c'est elle qui borne le travail.

| Champ modifié | Rayon | Consommateurs à repropager | Inventaire | Vérification (0 écart attendu) |
|---|---|---|---|---|
| `pitch:` | P5, P6 | **[M]** lignes `## Alternatives` des pages qui citent la cible · **[G]** zones AUTO des hubs · **[G]** `brain-index.json/.md` · vues `.base` : lecture directe, rien à faire | `[V1] <X>` **avant** l'édition : il liste exactement les puces qui réinjectent le pitch, et elles seules — un `grep` sur le nom ratisse trop large (corps et `## Liens` compris) | `[V1] <X>` **après** propagation : que des `OK` |
| `nom:` ou renommage du fichier | P1→P6 | **[M]** nom du fichier et champ `nom:` · **[D]** wikilinks du corps (R2) · **[!]** wikilinks du **frontmatter** (`alternatives:`, `complements:`) · **[M]** libellés des puces `## Alternatives` · **[!]** listes de noms codées en dur dans les `.base` · **[G]** index, hubs, liens | `grep -rn "<Ancien nom>" --include="*.md" --include="*.base" . \| grep -v "^\./\.git/"` | la même commande renvoie **0 ligne** ; puis `grep -rn "file.name ==" --include="*.base" .` et les deux validateurs |
| `categorie:` | **change de rayon** | **[D]** valeur présente dans `taxonomie.md` · **[D]** le chemin doit suivre : la page **déménage**, par `git mv` (jamais un copier-supprimer : l'historique se perd) · **[!]** entrée/sortie des comparatifs `.base` filtrés par catégorie · **[G]** hub quitté et hub d'accueil · **[M]** jeu d'alternatives pertinentes : les pairs de la **nouvelle** catégorie, et le retrait chez ceux de l'ancienne | `uv run /tmp/ou.py "<ancienne>"` puis `"<nouvelle>"` — les deux dossiers, donc les deux rayons ; `grep -rl 'categorie == "<ancienne>"' --include="*.base" .` | `uv run AI/scripts/check_arbo.py` (concordance chemin ↔ catégorie, **dure**) ; `check_brain.py` valide l'appartenance à la taxonomie — les valeurs légales viennent des blocs de code de `taxonomie.md`, pas de ses puces de prose : ne pas se fier à un `grep` ; le comparatif quitté garde **≥ 2 membres** (0 ou 1 = comparatif à vider ou refiltrer, `[WARN] R8b`) |
| `famille:` | — | **[D]** valeur ∈ énumération fermée du bloc de code `famille` de `taxonomie.md` (R14) · **[D]** conditionne `hosted:` et `scaling:` (R16) : les retirer si la famille cesse d'être `plateforme` / `saas` / `application` · **[D]** champ indexé, un consommateur machine filtre dessus | `uv run AI/scripts/query_index.py --famille <valeur> --fields nom,path` | `check_brain.py` ; la famille doit être **dérivée** de l'arbre F1→F9 (première réponse positive gagne), pas choisie — si deux branches conviennent, une règle de départage R1-R6 tranche ; si aucune ne tranche, laisser vide et demander |
| `tags:` | — | **[D]** tags présents dans `tags.md` · **[!]** entrée/sortie des comparatifs `.base` filtrés par tag · **[G]** index des tags de `liens.md` | `grep -rl '"<tag>"' --include="*.base" .` | `grep -c "<tag>" Documentation/general/tags.md` → ≥ 1 ; `check_brain.py` |
| `role:` | P1→P6 | **[D]** enum fermée (`brique`, `notion`, `pattern`, `rule`, `hub` ; `comparatif` arrive au lot 5) · **[D]** il choisit le **gabarit** que le validateur applique : changer `role:` change la liste des champs autorisés · **[D]** `pattern` et `rule` n'ont **pas** de `categorie:` et vivent dans `Patterns/` et `Rules/` — changer de rôle peut donc déménager la page · **[G]** index, hubs, liens, couleur du graphe | `uv run AI/scripts/query_index.py --role brique --categorie <cat>` | les deux validateurs — un champ hors gabarit sort en dur (R3) |
| `maturite:` | P3 | **[D]** enum fermée · **[!]** plusieurs `.base` filtrent `maturite != "deprecated"` ou `== "production"` — une page qui bascule sort de la vue sans bruit · **[D]** **indexé**, et c'est le SEUL critère éliminatoire depuis la suppression de `status:` : `planifier-projet` n'ouvre pas la fiche · **[M]** si `deprecated` : renseigner `alternatives:` (c'est lui qui dit quoi proposer à la place) **et** nommer le successeur dans le corps, pour le lecteur humain | `grep -rl 'maturite' --include="*.base" .` | `sed -n '/^maturite:/p;/^alternatives:/p' "<chemin>"` → une brique `deprecated` nomme ses successeurs ; `uv run AI/scripts/verifier_fraicheur.py` signale le contraire |
| `complements:` | P5 | **[D]** réciprocité, comme `alternatives:` : si A cite B, B cite A · **[M]** la section `## Alternatives` ne le couvre PAS — le lot 6 ouvrira une section `### Compléments` · **[G]** index | `grep -rn "complements:" --include="*.md" . \| grep -v "^\./\.git/"` | `check_brain.py` |
| `alias:` | — | **[!]** résolution des liens `[[alias]]` · **[!]** détection d'existence à l'étape 1 de la procédure ciblée · **[!]** unicité — 52 collisions connues dans le vault | `uv run AI/scripts/query_index.py --name "<alias>" --fields nom,path` | la même commande, après `build_index`, renvoie `"count": 1` |
| `domaines:` | P2 | **[G]** les 5 hubs de `Métiers/`, générés depuis ce champ · **[!]** appartenance au vocabulaire `themes.md` | `grep -c "<valeur>" Documentation/general/themes.md` | cette commande renvoie ≥ 1 ; `grep -rl "<X>" "Métiers/"` après `build_mocs` |
| `alternatives:` | P5, P6 | **[D]** réciprocité — si A cite B, B cite A (R12) · **[M]** la section `## Alternatives` liste les mêmes cibles (R11) · **[M]** la ligne de chaque cible suit la convention de réinjection (R1) | `grep -n "alternatives:" "<chemin>"` | `check_brain.py` pour la réciprocité, puis `[V1] <X>` et `[V1]` sur chaque cible ajoutée |
| `licence_type:`, `hosted:`, `scaling:`, `langage:` | — | **[D]** enums fermées, sauf `langage` · **[D]** `hosted:` et `scaling:` sont **conditionnels à `famille:`** : ils n'existent que pour `plateforme`, `saas`, `application` — les poser ailleurs sort en dur (R16) · **[!]** `hosted:` est une **liste** (`[self]`, `[managed]`, `[self, managed]`), jamais un scalaire · lus en direct par les vues `.base`, rien à propager | — | `check_brain.py` |
| `url_docs:`, `url_repo:` | — | **[!]** joignabilité, aucun contrôle en place | — | `curl -sS -o /dev/null -w '%{http_code}\n' -L --max-time 10 "<url>"` → 2xx/3xx ; 403 et 429 tolérés, 404 et NXDOMAIN non |
| **Suppression d'une page** | P1→P6 | **[D]** liens morts dans le corps des citeurs (R2) · **[!]** liens morts en **frontmatter** · **[D]** cible d'alternative absente de l'index → échec explicite (R12) · **[!]** un `.base` peut tomber à 0 membre · **[G]** index, hubs, liens | `grep -rn "<X>" --include="*.md" --include="*.base" . \| grep -v "^\./\.git/"` | la même commande renvoie **0 ligne** ; le `.base` du dossier garde **≥ 2 membres** ; les deux validateurs. **Aucun `rm` sur une page pendant la migration v3** : demander |

### `[V1]` — vérification de la réinjection du pitch

Contrôle les trois clauses de la convention de réinjection sur les sections
`## Alternatives` du vault. Avec un argument : une seule cible. Sans argument : balayage
complet. Lit les **fichiers**, pas l'index — donc utilisable avant toute régénération. Code
de retour 1 s'il reste une ligne à traiter.

```bash
cat > /tmp/verif_pitch.py <<'PY'
import re, sys, pathlib
cible = sys.argv[1] if len(sys.argv) > 1 else None
horspage = {'.git', '.claude', '.obsidian', 'AI', 'Documentation', 'Templates', 'docs'}
pages = sorted(p for p in pathlib.Path('.').rglob('*.md') if not (set(p.parts) & horspage))
txt = {p: p.read_text(encoding='utf-8') for p in pages}
fm = lambda t: t.split('---')[1] if t.startswith('---') else ''
pit = {p.stem: (re.search(r'^pitch:\s*"?(.*?)"?\s*$', fm(t), re.M) or [None, None])[1] for p, t in txt.items()}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('**', '')).strip().lower()
ko = 0
for p, t in txt.items():
    sec = re.search(r'^## Alternatives\s*$(.*?)(^## |\Z)', t, re.M | re.S)
    if not sec:
        continue
    for li in re.findall(r'^\s*[-*] .*$', sec.group(1), re.M):
        m = re.search(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', li)
        if not m:
            continue
        c = (m.group(2) or m.group(1)).split('/')[-1]
        if cible and c != cible:
            continue
        aff = re.sub(r'^\s*[-*] *\[\[[^\]]*\]\] *[—–:-]? *', '', li).strip()
        if not pit.get(c):
            etat = 'SANS-PITCH'                       # cible sans pitch: -> arbitrer
        elif c not in fm(t):
            etat = 'VOISIN' if aff.lower().startswith('voisin') else 'VOISIN-SANS-MARQUEUR'
        elif norm(aff).startswith(norm(pit[c])):
            etat = 'OK'                               # clause 1, suffixe libre inclus
        else:
            etat = 'DERIVE'                           # pitch perime, ou prose (clause 3)
        if etat != 'OK':
            ko += 1
            print(f'{etat:22} {p} -> {c}\n{"":22} affiche : {aff}\n{"":22} pitch   : {pit.get(c)}')
        elif cible:
            print(f'{etat:22} {p} -> {c}')
print(f'\n{ko} ligne(s) a traiter' + (f' pour {cible}' if cible else ' dans tout le vault'))
sys.exit(1 if ko else 0)
PY
python /tmp/verif_pitch.py "<Cible>"    # sans argument : balaye tout le vault
```

Le reste connu est documenté et une passe de contenu dédiée le balaiera. Une capture ou une
mise à jour ne doit pas **augmenter** ce compte : relever la valeur du balayage complet
**avant** d'écrire, la comparer après. C'est le seuil à ne pas dépasser, et c'est la seule
mesure qui vaille — un compte de référence recopié de mémoire ne prouve rien.

### Cas particulier — retour d'expérience daté

Un bug rencontré n'est pas une modification de champ : il s'écrit dans la section
`## Pièges` de la fiche concernée et **ne déclenche aucune propagation** — rayon nul.

- **Format** : `- YYYY-MM-DD — <symptôme> : <correctif>.` La date est ce qui distingue le
  vécu du piège documenté.
- **Imputation d'un incident né entre deux briques** : il s'inscrit **sous la brique qui a
  porté le correctif**, une seule fois, les autres briques nommées en clair dans la ligne.
  **La fiche de l'autre brique ne le mentionne pas** — une entrée dupliquée devient une
  seconde chose à synchroniser, c'est-à-dire le défaut même que cette procédure corrige. Le
  nom en clair suffit à la retrouver par `grep`.
- **Vérification** : `grep -n '^- [0-9]\{4\}-' "<chemin>"` renvoie l'entrée, et
  `check_brain.py` reste vert — la fiche ne doit pas franchir le seuil d'avertissement de
  taille.

---

## Procédure — mode sujet / balayage (plan d'abord, PUIS go)

Déclencheurs : « fais-moi les pages sur les statistiques », « ajoute le sujet RAG », ou en
fin de conversation « mets à jour DevBrain ».

1. **Cadrer le périmètre** → dresser la liste des pages candidates : notion(s) + briques /
   patterns. Pour chacune : nom, `role:`, `categorie:` pressentie, **dossier d'accueil
   dérivé**, tags pressentis (du vocabulaire), alternatives pressenties, et si elle existe
   déjà (`query_index.py`). **Grouper la liste par dossier d'accueil** : c'est le rayon
   commun, et deux pages du même dossier se traitent d'un seul rayon au lieu de deux.
2. **Présenter le plan et ATTENDRE le GO.** Ne rien créer avant validation. L'utilisateur
   ajoute / retire / renomme des pages. Signaler dans ce plan toute insertion qui
   **promeut un sous-dossier** (5e page d'un sous-domaine) : ce n'est plus une capture.
3. **Écrire la file validée** dans `AI/backlog.md` (une page par ligne, avec son dossier).
4. **Drainer la file une page à la fois**, chacune via la procédure ciblée — table P1→P6 et
   contrôle final compris. Cocher au fur et à mesure.
5. **Clôturer** : invoquer `cloturer-brain`. Repassable tant qu'il reste des items dans la
   file → rien d'oublié.

**Les notions déjà écrites ne se réécrivent pas en balayage** : les proposer à floSa, et
attendre. Une notion neuve, en revanche, se crée normalement (ligne P4).

## Anti-patterns

- **Écrire la page et s'arrêter là.** Le rayon n'est pas optionnel : une brique insérée sans P1→P6 dégrade la structure au lieu de l'enrichir, et c'est précisément ce que le lot 7 corrige.
- **Sauter une ligne de P1→P6 en silence.** Une ligne sans objet se déclare sans objet.
- **Deviner le dossier au lieu de le dériver.** `categorie:` → `arbo.py` → chemin. Un fichier posé à vue fait échouer `check_arbo.py`, et il le fait après coup.
- **Sauter le contrôle de l'étape 8.** Confronter `git status` au `ls` du dossier est ce qui transforme une intention en fait vérifié.
- Créer la page demandée mais oublier la notion (P4) ou la réciprocité des alternatives (P5).
- Inventer une catégorie, un tag, une famille ou un score (le score n'existe plus).
- Recopier un pitch divergent au lieu de réinjecter le `pitch:` de la cible.
- **Modifier un champ d'une page existante sans dérouler la table des effets de bord** : c'est l'origine mesurée des pitchs périmés du vault (constat C1 de l'audit axe 2).
- Substituer une prose comparative au pitch d'une cible listée en `alternatives:` (clause 3) — ou omettre le marqueur `voisin :` sur une puce dont la cible n'est pas dans `alternatives:`.
- Clore une mise à jour sur un écart restant de `[V1]`, ou en ayant augmenté le compte de référence.
- Éditer une zone `<!-- AUTO -->` de hub à la main : elle sera écrasée à la clôture.
- Écrire un wikilink qualifié par chemin : il casse au prochain `git mv`, et les lots 4 à 6 en feront encore.
- Réécrire une notion existante sans que floSa l'ait demandé.
- Dupliquer une entrée d'expérience datée sur les deux briques d'un incident inter-briques.
- Oublier d'invoquer `cloturer-brain`, ou clore soi-même à sa place : la régénération, la validation, la vérification de divergence et le commit y sont écrits une seule fois.

## Voir aussi

- `cloturer-brain` — la clôture mécanique, appelée en fin de chaque procédure. **Seul endroit du vault où la politique git est écrite**, à l'exception de la règle d'identité, qui est dans `CLAUDE.md` parce qu'elle doit être lue à chaque conversation.
- `planifier-projet` — consomme l'index produit par la clôture.
- `AI/design/brain-v3.md` §10 (la règle de propagation), §12 (l'impact sur ce skill), §5 à §9 (les gabarits par rôle).
- `AI/migration/lot-7-skills.md` — le lot qui a écrit cette version.
