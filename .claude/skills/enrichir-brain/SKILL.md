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
  skill `cloturer-brain`. Also owns the NEW CATEGORY VALUE procedure (brain.yml + taxonomie.md + tags.md, same commit as the pages) and the UPDATE path — "le pitch de X a change",
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
| **P3** | Le comparatif du dossier — la **page** `role: comparatif`, et le `.base` qu'elle embarque | `ls "<dossier>"/'Comparatif - '*` — les deux fichiers portent le même nom | vue : **automatique** (le `.base` filtre par `categorie`) ; puce de « Ce qui départage » dans la **page** : **à écrire**. Si le comparatif est **créé**, il a un consommateur de plus : le hub `Comparatifs/Comparatifs.md` — zone AUTO **générée**, et son `## Voir aussi` **à écrire** |
| **P4** | La notion du sujet | le `role: notion` du sujet (cf. *L'exception notion*) | **à écrire**, dans les deux sens |
| **P5** | Les briques pairs — les autres `role: brique` du dossier | `ls <dossier>/*.md` | **à écrire**, réciprocité obligatoire |
| **P6** | Les pitchs réinjectés chez les pairs | `alternatives:` / `complements:` des pairs | **à écrire**, pitch copié jamais retapé — vérifié par la règle dure `reinjection_du_resume` (R1·R22) |

**Aucune de ces six lignes ne se saute en silence.** Une ligne sans objet se déclare sans
objet (« pas de comparatif dans ce dossier »), elle ne se tait pas. C'est ce que contrôle
l'étape 8 de la procédure ciblée.

### Trouver le dossier d'accueil — dérivation, pas décision

Personne ne choisit un dossier : il se **dérive** de `categorie:`. La dérivation vit dans le
kit (`AI/scripts/brainkit/valider/chemins.py`), que `AI/scripts/arbo.py` expose et que
`check_arbo.py` applique ; **les libellés, le seuil et les rôles qui pèsent dessus sont dans
`brain.yml`** (bloc `axes.rangement` et `roles[].pese_sur_le_seuil`), pas dans le code. La
commande, à lancer une fois la catégorie arbitrée — le script est versionné à côté de ce
fichier :

```bash
uv run .claude/skills/enrichir-brain/ou.py "database/vecteur"
#   stdout : Bases de données/Vectoriel        (le dossier, seul — utilisable dans D=$(...))
#   stderr : le diagnostic (pages pesantes avant/après, seuil, plafond, issue)
uv run .claude/skills/enrichir-brain/ou.py "data/catalogue" --role notion   # le rôle de la page à insérer
```

Ce que le script garantit, parce que l'ancien (un `role == "brique"` écrit en dur, lu dans
l'index) ne le garantissait pas — mesuré : il rendait le dossier du domaine pour
`stats/bayesien`, `math/information` et `math/theorie-apprentissage`, trois valeurs déjà
promues, et ratait la promotion de `data/catalogue` :

- **Mêmes règles que `check_arbo.py`.** Les rôles qui pèsent sur le seuil sont lus dans le manifeste : aujourd'hui **brique et notion** ; ni comparatif, ni hub, ni pattern, ni rule. Aucune liste n'est recopiée dans le script, et il refuse de répondre (code 5) si son calcul diverge de celui du kit.
- **Population lue dans les fichiers**, pas dans `brain-index.json` : l'index n'est régénéré qu'à la clôture, une page écrite plus tôt dans la même session lui est invisible.
- **La page à insérer compte**, avec son rôle (`--role`, défaut `brique`) : un comparatif inséré ne fait franchir aucun seuil, une notion oui.
- **Il signale les effets de bord** : lever le plafond d'un domaine peut promouvoir une *autre* valeur (essayer `automation/autre`), et le hub d'un dossier promu ne peut pas reprendre le nom d'un fichier existant.

Les sorties à connaître (le code de retour les distingue) :

| Code | Sens | Que faire |
|---|---|---|
| 0 | dérivation sûre — l'issue dit *déjà promue*, *sous le seuil*, *plafond* ou *franchit le seuil* | lire la ligne `issue` : **jamais supposer** |
| 2 | **préfixe inconnu**, ou rôle inconnu — stdout vide | pas un bug à contourner : catégorie à arbitrer. **Demander** (procédure *nouvelle valeur de catégorie*) |
| 3 | préfixe connu, **valeur non déclarée** dans `brain.yml` — le dossier affiché est *hypothétique* | `check_brain` la refuserait en dur (R14). **Demander**, puis procédure *nouvelle valeur de catégorie* |
| 4 | le seuil est franchi **sans `libelle:` déclaré** — la dérivation refuse d'inventer un nom | libellé à déclarer dans `brain.yml`, avec l'accord de floSa (même procédure) |
| 5 | ce script et le kit ne calculent plus la même chose | ne pas se fier au script ; le signaler |

Quand l'issue est **FRANCHIT LE SEUIL** : l'insertion fait passer un sous-domaine à 5 pages
pesantes et **promeut** un dossier. Ce n'est plus une insertion, c'est une réorganisation : le
dossier se crée, ses pages y descendent par `git mv`, il prend un hub à son nom (`<Libellé>.md`,
nom unique dans le vault). Le libellé est déjà lu dans `brain.yml`,
`axes.rangement.prefixes[<préfixe>].sous.<valeur>.libelle` — **il ne se cherche plus dans
`SUB_LABEL`, qui n'existe plus**. **Le signaler à floSa avant de le faire.** Le plafond
(`plafond_promotion`) est déjà appliqué par le script : un sous-domaine ne se promeut pas s'il
ne laisse aucune page au niveau du domaine.

### Lister le rayon — une commande, une liste fermée

```bash
D=$(uv run .claude/skills/enrichir-brain/ou.py "database/vecteur" 2>/dev/null)   # stdout = le dossier, seul
                                        # (relancer une fois SANS 2>/dev/null : le diagnostic est sur stderr)
ls -1 "$D"                              # P3, P4, P5 : le rayon, en clair
dirname "$D"                            # P2 : le parent ; remonter jusqu'à la racine
```

Ce que `ls` rend, ligne par ligne : le hub du dossier (`<Dossier>.md`), le ou les
comparatifs — **deux fichiers de même nom**, `Comparatif - <thème>.md` et son `.base`
(P3) —, et les autres `.md` : les pairs (P5). Il n'y a rien d'autre à chercher, et c'est
tout l'intérêt de l'arbre : **plus rien à déduire des tags.**

### L'exception notion — levée le 2026-09-05

P4 était la seule ligne que `ls` ne rendait pas : les 297 notions vivaient sous
`Wiki/Concepts/`, hors de l'arbre, et il fallait les chercher par l'index. **Le lot 4 les a
toutes descendues** — une notion se range désormais par son domaine, comme une brique, et le
`ls` du dossier la rend au même titre que ses pairs. Il n'y a plus d'exception.

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
- `AI/scripts/arbo.py` — la dérivation `categorie:` → chemin, écrite une fois. Depuis le lot 9 c'est un **pont** vers le kit (`AI/scripts/brainkit/`, instance figée le 2026-09-29) ; ses tables ne sont plus dans le code. Ne pas la réimplémenter de tête : `ou.py` l'appelle.
- `brain.yml` — le **manifeste**, source machine de tout ce que le validateur sait : rôles (`pese_sur_le_seuil`, `range_par`), axe de rangement (`axes.rangement` : `prefixes`, `rattachements`, `seuil_promotion`, `plafond_promotion`, et pour chaque sous-valeur son `libelle:`, son `motif:`, sa `frontiere:`), axe de nature, règles et sévérités (`regles`), vocabulaires. **Les valeurs légales de `categorie:` et de `famille:` sont lues ici**, pas dans `taxonomie.md`. Fichier long : le lire par tranche (`grep -n`, `sed -n`).
- `Documentation/general/taxonomie.md` — les **deux axes** de rangement : `categorie:` (le domaine, arbre D1→D14 ; le nombre de valeurs est en tête du fichier, ne pas le recopier) et `famille:` (la nature technique, 9 valeurs fermées, arbre F1→F9). Les deux se **dérivent** par arbre de décision, ils ne se choisissent pas à l'intuition. La section *Axe `role:`* y donne le vocabulaire des rôles. **C'est de la documentation, plus la source machine** : `brain.yml` déclare `vocabulaires.taxonomie.genere: true`, le validateur ne la relit pas. Une valeur ajoutée ici et pas dans `brain.yml` est refusée en dur ; une valeur ajoutée dans `brain.yml` et pas ici passe le validateur et laisse la documentation mentir (cf. *Procédure — nouvelle valeur de catégorie*).
- `Documentation/general/tags.md` — vocabulaire de tags **fermé**. Piocher ici, ne jamais inventer.
- `Documentation/general/themes.md` — vocabulaire `domaines:`.
- `Templates/Service-Dev.md`, `Templates/Concept-Wiki.md` — gabarits stricts.
- `AI/design/brain-v3.md` §5 à §9 — les gabarits de page par `role:`.

## Conventions v3 non négociables

- **Le dossier se dérive, il ne se choisit pas.** `categorie:` donne le domaine, `arbo.py` donne le chemin. Un fichier posé « là où ça semble logique » fait échouer `check_arbo.py`.
- **Trois champs, trois questions distinctes.** `categorie:` = de quoi ça parle (le domaine) · `famille:` = ce que c'est techniquement (paquet ? plateforme ?) · `role:` = ce que la page **est** éditorialement (`brique`, `notion`, `comparatif`, `pattern`, `rule`, `hub`). Un `role: hub`, `pattern` ou `rule` ne porte **pas** de `categorie:` : un hub *est* le rangement, un pattern enjambe les domaines par construction, une règle est transverse par définition.
- **Ton impersonnel** partout : ni « tu » ni « vous ». Phrases courtes, parties + bullets.
- **Frontmatter exact** selon le gabarit du `role:` : ni plus, ni moins de champs. C'est `role:` qui choisit le gabarit que `check_brain.py` applique.
- **Pitch unique, une seule convention de réinjection** : chaque page porte SON `pitch:` (une ligne), écrit une seule fois. Une donnée, trois usages (frontmatter, sections `### Alternatives` et `### Compléments` des autres pages — sous `## Écosystème` depuis le lot 6 —, propositions de `planifier-projet`). La convention, en trois clauses :
  1. cible listée dans le frontmatter `alternatives:` → la ligne **commence par** le `pitch:` courant de la cible, à la normalisation près (`**` retirés, espaces réduits, casse ignorée) ; **suffixe libre autorisé après**. **Contrôlé, en dur** (R1·R22, règle `reinjection_du_resume`) ;
  2. cible absente du frontmatter `alternatives:` → mention de voisinage, ligne libre mais **préfixée de `voisin :`**. Le validateur **exempte** une puce dont l'entrée n'est pas une cible du champ : le marqueur n'est plus contrôlé par rien, il reste une convention de lisibilité ;
  3. jamais de prose à la place du pitch d'une cible listée en `alternatives:` — soit la prose devient le suffixe (clause 1), soit la cible sort du frontmatter (clause 2). C'est ce que R1·R22 refuse dès que la cible est dans le champ.

  Le pitch se **copie** depuis la cible, il ne se retape jamais.
- **Liens nus, toujours** : `[[Qdrant]]`, jamais `[[Bases de données/Vectoriel/Qdrant|Qdrant]]`. Le pipe ne sert qu'à changer le texte affiché (`[[Qdrant|la base vectorielle]]`), jamais à porter un chemin — un chemin casse au premier `git mv`, et le lot 3 en a fait 682 sans toucher un lien. Contrepartie : **le nom de fichier d'une page nouvelle doit être unique dans le vault**, à la casse près (le système de fichiers de floSa est insensible à la casse). Vérifier avant de créer, y compris pour un hub à créer.
- **Catégorie ou tag manquant → demander**, jamais inventer. Une valeur de catégorie se pose par la *Procédure — nouvelle valeur de catégorie* (trois fichiers de vocabulaire, dont `brain.yml`), un tag dans `Documentation/general/tags.md`. **Aucune valeur n'est créée sans l'accord de floSa.**
- **Faits vérifiés sur le web, d'office (sans demander la permission)** : avant d'écrire une fiche, vérifier en ligne (WebSearch / WebFetch) les champs factuels — `licence_type`, `langage`, `maturite`, `hosted`, `scaling`, `url_docs` / `url_repo`, statut actuel (actif / déprécié / racheté). Ne jamais demander l'autorisation de vérifier : le faire directement. Info introuvable ou ambiguë → laisser le champ vide, ne pas inventer.
- **Le corps d'une page ne s'écrit pas de mémoire — brique comme notion (d'office, sans demander)** : le modèle qui écrit peut avoir une connaissance périmée, et une page qui la recopie est fausse le jour où elle est écrite. Avant de rédiger le **contenu** (définition, fonctionnement, fonctionnalités, versions, limites, état de l'art), le chercher en ligne et écrire **depuis ce qu'on a lu**, pas depuis ce qu'on croit savoir :
  - **Brique** : la doc officielle et le dépôt (README, releases, changelog) pour ce que l'outil fait *aujourd'hui* ; les faits qui datent (version, fonctionnalités récentes, dépréciation) portent leur source.
  - **Notion** : des **sources primaires**, pas les premiers résultats d'un moteur — articles de recherche (arXiv, ACL, NeurIPS, ICLR…), documentation officielle, billets techniques des équipes qui ont construit la méthode ; pour un domaine actif, aussi les travaux des ~12 derniers mois et les **critiques ou limites connues**, pas seulement la version canonique. Chaque papier retenu est ouvert et vérifié (titre, auteurs, année, résultat annoncé) avant d'être cité, avec son lien.
  - **Désaccord** entre deux sources : l'écrire tel quel, ne pas trancher. **Rien de trouvé** : ne pas l'écrire, et le dire à floSa en fin de capture.
  - **Confronter à l'existant** : si une notion ou une brique voisine du vault dit autre chose que la source, ne pas la réécrire (une notion se propose, cf. plus bas) — le signaler.

---

## Règles d'usage — établies par les captures, écrites ici pour ne plus être redécouvertes

Douze captures successives (OCR, stockage objet, embeddings, graphes, conteneurs, reverse
proxies, identité, scanners, transformation, qualité, ingestion, messagerie, catalogue) ont
chacune dû improviser ce qui suit, faute de règle écrite.

- **Le corps d'une page s'écrit depuis le web, pas de mémoire** — brique comme notion (cf. *Conventions*, plus haut).
- **Les fichiers de vocabulaire font partie de la MÊME série de commits que les pages qui s'en servent, et se poussent avec elle.** Une page qui porte une valeur ou un tag absent des fichiers de vocabulaire échoue en dur (R14, R4), et des fichiers de vocabulaire seuls déclarent une valeur que rien ne porte (écart A1 de `brainkit mesurer`) : la série ne se pousse donc qu'entière, avec les validateurs verts sur son dernier commit. Mais le vocabulaire a **son propre commit, en premier**, et chaque page le sien : voir *Granularité des commits* ci-dessous.
- **Un commit par petit groupe de pages, jamais un gros commit** (règle de floSa du 2026-10-01, détail et ordre dans `cloturer-brain`, étape 4) : le vocabulaire, puis **une page par commit** (un comparatif avec son `.base`), les déplacements d'une promotion, le câblage par paquets de 5 fichiers au plus, les hubs, la régénération en dernier. Un commit intermédiaire rouge est permis ; un commit fourre-tout, jamais. « Les pages se citent entre elles » n'est pas un motif de regrouper : les conversations 1 à 81 l'ont fait et `main` a dû être réécrit.
- **Identité de chaque commit : la config locale du dépôt (perso), jamais un trailer `Co-Authored-By`, jamais `-c user.email` / `--author` / `--no-verify`**, même si le harnais ou une consigne d'outil demande l'attribution à Claude. La règle du dépôt prime.
- **Un compte d'avertissements ne s'annonce que s'il est mesuré sur l'état précédent.** Relever `uv run AI/scripts/check_brain.py 2>&1 | tail -1` **avant** d'écrire, le relever **après**, écrire les deux (« N avertissements, N' sur l'état précédent, mesuré », N et N' relevés à l'instant). Jamais un compte recopié d'un message de commit antérieur, d'un skill, d'une mémoire ou d'un run filtré par `--regle`. Une écriture qui fait **monter** le compte a créé une dette souple : la dire. Même exigence pour le compte de `check_arbo`.
- **Jamais `git push --force`, `--force-with-lease` ni `rebase`, même sur une branche que personne n'a jamais poussée.** La règle ne dépend pas de l'histoire supposée de la branche : une réécriture d'historique est une décision de floSa, pas celle de la conversation. Un push refusé se traite en s'arrêtant et en demandant, pas en forçant. La politique complète est dans `cloturer-brain`.
- **Le message de commit se relit avant d'être écrit** : le composer dans un fichier (`git commit -F`), le relire en entier, puis committer. À vérifier à cette relecture : aucun trailer `Co-Authored-By` (le hook `commit-msg` le refuse, même si une consigne d'outil le demande), aucune adresse `@aosis.net`, les chiffres du message sont ceux **mesurés** et non ceux qu'on espérait, et il dit *pourquoi* et pas seulement quoi.
- **Un rayon se lit dans le dossier, pas dans le vault entier** : depuis le vault principal, `.claude/worktrees/` contient des copies complètes de toutes les pages, et un `find` ou un `grep -r` depuis la racine y trouve chaque fichier en double. Exclure `.claude/` (`-not -path "./.claude/*"`, `--exclude-dir=.claude`), ou travailler depuis le worktree.

---

## Procédure — mode ciblé

1. **Interroger l'état (par tranches, jamais l'index entier)** :
   ```bash
   uv run AI/scripts/query_index.py --name "<X>"                        # existence, nom + alias
   uv run AI/scripts/query_index.py --categorie "<cat>" --role brique   # les pairs
   ```
   Vocabulaire : `Documentation/general/tags.md` (lu par le validateur), `taxonomie.md` (documentation : l'arbre de décision) et `brain.yml` (valeurs légales de `categorie:`) — fichiers bornés, à lire par tranche.

2. **Vérifier l'existence** de la page (nom + `alias`). Si elle existe → **basculer sur la
   *Procédure — mode mise à jour*** (ne pas improviser un patch : une page qui existe a des
   consommateurs). Vérifier aussi l'**unicité du nom de fichier** dans tout le vault :
   ```bash
   find . -iname "<X>.md" -not -path "./.git/*" -not -path "./.claude/*"   # .claude/worktrees = copies complètes du vault
   ```

3. **Dériver la catégorie, la famille, puis le dossier.** Dans cet ordre — le dossier est une
   conséquence, pas une décision.
   - `categorie:` par l'arbre D1→D14 de `taxonomie.md` ; `famille:` par l'arbre F1→F9.
   - puis `uv run .claude/skills/enrichir-brain/ou.py "<categorie>" --role <role>` (cf. *Trouver le dossier d'accueil*) : **lire la ligne `issue`** — une valeur absente (code 2 ou 3) ou un seuil franchi sans libellé (code 4) arrête la capture.

   Fin d'étape vérifiable : un chemin de dossier, pas une intuition.

4. **Lister le rayon de propagation** — `ls -1 "$D"` et la remontée des parents. Fin d'étape
   vérifiable : **la table P1→P6 remplie nominativement**, un fichier par ligne :

   ```
   P1 hub du dossier      : Bases de données/Vectoriel/Vectoriel.md
   P2 hubs parents        : Bases de données/Bases de données.md
   P3 comparatif          : Bases de données/Vectoriel/Comparatif - Bases vectorielles.md
                            (+ son `.base`, embarqué par la page)
   P4 notion              : Bases de données/Vectoriel/Bases de données vectorielles.md
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

     > **P2 ne bouge pas toujours, et c'est normal.** Si la brique atterrit dans un
     > **sous-dossier promu**, la zone AUTO du hub de domaine liste les **sous-hubs**, pas les
     > feuilles : elle ne change pas. Mesuré en insérant `USearch` dans
     > `Bases de données/Vectoriel/` — `Vectoriel.md` bouge, `Bases de données.md` reste
     > identique au bit près. C'est le cas type de la « ligne sans objet » : la **déclarer**
     > sans objet, ne pas la taire, et regarder quand même le **corps** du hub parent, qui peut
     > décrire le sous-domaine en une phrase à rafraîchir. Si la brique atterrit **directement
     > dans le dossier de domaine**, P1 et P2 désignent la même page.
   - **P3 — le comparatif.** Depuis le lot 5 il est en **deux fichiers de même nom** : la
     page `role: comparatif`, qui porte le corps et les liens, et le `.base` qu'elle embarque,
     qui ne porte que la requête. Les deux se traitent, et pas de la même façon.

     - **Le `.base` — automatique.** S'il filtre par `categorie` (le cas normal), la nouvelle
       brique **entre toute seule** dans la vue : rien à faire, le vérifier suffit. S'il filtre
       par liste de noms codée en dur ou par chemin, **elle n'entrera jamais** : le signaler
       (`check_brain` le sort en `[WARN] R8d`). Ne jamais ajouter un nom à la main dans un
       filtre par catégorie.
     - **La page — à écrire.** Une brique entrée dans la vue sans puce dans `## Ce qui
       départage` est une ligne du tableau que rien n'explique. Ajouter **une** puce
       `- [[<Brique>]] — <ce qui la distingue des autres membres>` : pas son pitch, qui est
       déjà dans la colonne du tableau, et **rien qui ne se lise pas dans sa fiche** (au lot 5,
       les 45 puces du pilote sortent toutes de `## Pourquoi`, et 38 sur 45 de `## Pièges`).
       Relire aussi la ligne « On tranche sur : … » : une brique qui ouvre un critère neuf
       peut la périmer.
     - **Le lien, lui, ne se touche pas.** Une fiche qui cite `[[Comparatif - <thème>]]` en
       lien **nu** vise la page, jamais le `.base` — la page a le même stem. Repointer vers
       `[[<thème>.base]]` serait une régression (lot 5, remontée 2).

     Aucun comparatif dans le dossier et ≥ 2 briques de la catégorie → en proposer un, page
     **et** `.base` (`check_brain` le réclame déjà en `[WARN] R8a`). **Un comparatif créé a un
     consommateur que le dossier ne rend pas** — le seul de toute la table : le hub
     `Comparatifs/Comparatifs.md`, qui réunit les 47 et n'est dans le rayon d'aucune
     insertion, puisqu'il vit à la racine.

     - **Le hub — généré.** Sa zone AUTO se remplit depuis `role: comparatif` : `cloturer-brain`
       la régénère, rien à écrire à la main. Une liste tenue à la main mentirait dès ce
       comparatif-ci.
     - **Le lien retour — à écrire, et c'est lui qui compte.** La nouvelle page se clôt par :

       ```markdown
       ## Voir aussi

       - [[Comparatifs]] — le hub qui réunit tous les comparatifs du brain, groupés par domaine.
       ```

       Sans lui, le hub cite le nouveau comparatif et le nouveau comparatif ne cite personne :
       il reste un nœud rouge isolé dans la grappe de son domaine, exactement l'état que le
       hub a corrigé le 2026-09-06. C'est le **lien retour** qui fait la galaxie, pas la liste.
   - **P4 — la notion.** La brique cite sa notion dans `## Voir aussi` (la section `## Liens` n'existe plus
     dans le gabarit brique) ; la notion cite la brique dans `## Approches voisines & alternatives`
     (le titre réel des pages ; la spec `brain-v3.md` §7 dit « Approches voisines », en retard sur elles). Les **deux** sens. Un seul est contrôlé : R15 (**dure**, plus un avertissement) exige de toute brique au moins un lien vers une notion ou un hub ; le sens notion → brique n'est vérifié par rien, il se tient à la main.
     Notion absente → la créer (c'est une capture, pas une incursion). Notion existante à
     modifier → **demander** (cf. *Pré-requis*).
   - **P5 — les briques pairs.** Choisir parmi les pairs listés à l'étape 4 celles qui sont
     de vraies alternatives. Pour chacune : `alternatives:` **des deux côtés** (si A cite B,
     B cite A — `check_brain` R12 est dur là-dessus), **et** la section `### Alternatives` (sous
     `## Écosystème`) des deux pages (R11). Un pair écarté est un choix, pas un oubli : le dire.
   - **P6 — les pitchs.** Chaque puce ajoutée réinjecte le `pitch:` **courant** de sa cible,
     copié depuis la cible (R1). Vérifier avec la règle `reinjection_du_resume` (*Vérifier la réinjection du pitch*, ci-dessous) avant de passer à l'étape 8.

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
   | Fichier touché **hors du dossier** | légitime pour P2 (hubs parents), P4 (notion) et, si un comparatif a été **créé**, `Comparatifs/Comparatifs.md` (P3) ; **suspect** partout ailleurs — l'expliquer ou le défaire |

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
   uv run AI/scripts/build_index.py && uv run AI/scripts/build_mocs.py && uv run AI/scripts/build_bandeau.py && uv run AI/scripts/build_links.py && uv run AI/scripts/build_carte.py   # l'ordre de cloturer-brain
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
| `pitch:` | P5, P6 | **[M]** puces `### Alternatives` / `### Compléments` des pages qui citent la cible · **[G]** zones AUTO des hubs · **[G]** `brain-index.json/.md` · vues `.base` : lecture directe, rien à faire | modifier le `pitch:`, puis `uv run AI/scripts/check_brain.py --regle reinjection_du_resume \| grep "<X>"` : chaque `[FAIL]` est une puce à recopier, et elles seules — un `grep` sur le nom ratisse trop large (corps et `## Voir aussi` compris) | la même commande ne renvoie **rien** (voir *Vérifier la réinjection du pitch*) |
| `nom:` ou renommage du fichier | P1→P6 | **[M]** nom du fichier et champ `nom:` · **[D]** wikilinks du corps (R2) · **[D]** wikilinks du **frontmatter** `alternatives:` / `complements:` (une cible absente de l'index sort en dur, R12·R18) · **[!]** les autres champs à wikilinks · **[M]** libellés des puces `## Alternatives` · **[!]** listes de noms codées en dur dans les `.base` · **[G]** index, hubs, liens | `grep -rn "<Ancien nom>" --include="*.md" --include="*.base" . \| grep -v "^\./\.git/"` | la même commande renvoie **0 ligne** ; puis `grep -rn "file.name ==" --include="*.base" .` et les deux validateurs |
| `categorie:` | **change de rayon** | **[D]** valeur déclarée dans `brain.yml` (`axes.rangement.prefixes[].sous`, R14) — et, à la main, dans `taxonomie.md` · **[D]** le chemin doit suivre : la page **déménage**, par `git mv` (jamais un copier-supprimer : l'historique se perd) · **[!]** entrée/sortie des comparatifs `.base` filtrés par catégorie · **[G]** hub quitté et hub d'accueil · **[M]** jeu d'alternatives pertinentes : les pairs de la **nouvelle** catégorie, et le retrait chez ceux de l'ancienne | `uv run .claude/skills/enrichir-brain/ou.py "<ancienne>" --role <role>` puis `"<nouvelle>"` — les deux dossiers, donc les deux rayons (la page comptait dans l'ancienne : lire les deux lignes `issue`, un départ peut faire redescendre une valeur sous le seuil) ; `grep -rl 'categorie == "<ancienne>"' --include="*.base" .` | `uv run AI/scripts/check_arbo.py` (concordance chemin ↔ catégorie, **dure**) ; `check_brain.py` valide l'appartenance au vocabulaire — les valeurs légales viennent de `brain.yml`, ni de `taxonomie.md` ni d'un `grep` de ses puces ; le comparatif quitté garde **≥ 2 membres** (0 ou 1 = comparatif à vider ou refiltrer, `[WARN] R8b`) |
| `famille:` | — | **[D]** valeur ∈ énumération fermée de `brain.yml` (`axes.nature`, R14) · **[D]** conditionne `hosted:` et `scaling:` (R16) : les retirer si la famille cesse d'être `plateforme` / `saas` / `application` · **[D]** champ indexé, un consommateur machine filtre dessus | `uv run AI/scripts/query_index.py --famille <valeur> --fields nom,path` | `check_brain.py` ; la famille doit être **dérivée** de l'arbre F1→F9 (première réponse positive gagne), pas choisie — si deux branches conviennent, une règle de départage R1-R6 tranche ; si aucune ne tranche, laisser vide et demander |
| `tags:` | — | **[D]** tags présents dans `tags.md` · **[!]** entrée/sortie des comparatifs `.base` filtrés par tag · **[G]** index des tags de `liens.md` | `grep -rl '"<tag>"' --include="*.base" .` | `grep -c "<tag>" Documentation/general/tags.md` → ≥ 1 ; `check_brain.py` |
| `role:` | P1→P6 | **[D]** enum fermée, **six** valeurs (`brique`, `notion`, `comparatif`, `pattern`, `rule`, `hub`) · **[D]** il choisit le **gabarit** que le validateur applique : changer `role:` change la liste des champs autorisés · **[D]** `pattern` et `rule` n'ont **pas** de `categorie:` et vivent dans `Patterns/` et `Rules/` — changer de rôle peut donc déménager la page · **[G]** index, hubs, liens, couleur du graphe | `uv run AI/scripts/query_index.py --role brique --categorie <cat>` | les deux validateurs — un champ hors gabarit sort en dur (R3) |
| `maturite:` | P3 | **[D]** enum fermée · **[!]** plusieurs `.base` filtrent `maturite != "deprecated"` ou `== "production"` — une page qui bascule sort de la vue sans bruit · **[D]** **indexé**, et c'est le SEUL critère éliminatoire depuis la suppression de `status:` : `planifier-projet` n'ouvre pas la fiche · **[M]** si `deprecated` : renseigner `alternatives:` (c'est lui qui dit quoi proposer à la place) **et** nommer le successeur dans le corps, pour le lecteur humain | `grep -rl 'maturite' --include="*.base" .` | `sed -n '/^maturite:/p;/^alternatives:/p' "<chemin>"` → une brique `deprecated` nomme ses successeurs ; `uv run AI/scripts/verifier_fraicheur.py` signale le contraire |
| `complements:` | P5 | **[D]** réciprocité, comme `alternatives:` : si A cite B, B cite A · **[M]** la section `### Compléments` (sous `## Écosystème`) liste les mêmes cibles, avec le pitch courant de chacune (R1·R22, dure) — `### Alternatives` ne le couvre pas · **[G]** index | `grep -rn "complements:" --include="*.md" . \| grep -v "^\./\.git/"` | `check_brain.py` |
| `alias:` | — | **[!]** résolution des liens `[[alias]]` · **[!]** détection d'existence à l'étape 1 de la procédure ciblée · **[D]** unicité du nom de fichier (dure) · **[!]** collisions d'alias : avertissement R5 (`collision_alias`), compte à lire dans `check_brain`, pas ici | `uv run AI/scripts/query_index.py --name "<alias>" --fields nom,path` | la même commande, après `build_index`, renvoie `"count": 1` |
| `domaines:` | P2 | **[G]** les 6 hubs de `Métiers/`, générés depuis ce champ · **[!]** appartenance au vocabulaire `themes.md` | `grep -c "<valeur>" Documentation/general/themes.md` | cette commande renvoie ≥ 1 ; `grep -rl "<X>" "Métiers/"` après `build_mocs` |
| `alternatives:` | P5, P6 | **[D]** réciprocité — si A cite B, B cite A (R12) · **[M]** la section `### Alternatives` liste les mêmes cibles (R11) · **[M]** la puce de chaque cible suit la convention de réinjection (R1·R22, dure) | `grep -n "alternatives:" "<chemin>"` | `check_brain.py` (réciprocité **et** réinjection : les deux sont dures) |
| `licence_type:`, `hosted:`, `scaling:`, `langage:` | — | **[D]** enums fermées, sauf `langage` · **[D]** `hosted:` et `scaling:` sont **conditionnels à `famille:`** : ils n'existent que pour `plateforme`, `saas`, `application` — les poser ailleurs sort en dur (R16) · **[!]** `hosted:` est une **liste** (`[self]`, `[managed]`, `[self, managed]`), jamais un scalaire · lus en direct par les vues `.base`, rien à propager | — | `check_brain.py` |
| `url_docs:`, `url_repo:` | — | **[!]** joignabilité, aucun contrôle en place | — | `curl -sS -o /dev/null -w '%{http_code}\n' -L --max-time 10 "<url>"` → 2xx/3xx ; 403 et 429 tolérés, 404 et NXDOMAIN non |
| **Suppression d'une page** | P1→P6 | **[D]** liens morts dans le corps des citeurs (R2) · **[!]** liens morts en **frontmatter** · **[D]** cible d'alternative absente de l'index → échec explicite (R12) · **[!]** un `.base` peut tomber à 0 membre · **[G]** index, hubs, liens | `grep -rn "<X>" --include="*.md" --include="*.base" . \| grep -v "^\./\.git/"` | la même commande renvoie **0 ligne** ; le `.base` du dossier garde **≥ 2 membres** ; les deux validateurs. **Une suppression de page se demande** ; un déplacement passe par `git mv` |

### Vérifier la réinjection du pitch — la règle `reinjection_du_resume` (ex-`[V1]`)

Le script `[V1]` de ce skill est **retiré**. Il cherchait `## Alternatives` (niveau 2) alors que
ces sections sont des `### Alternatives` sous `## Écosystème` depuis le lot 6 : il ne trouvait
aucune section, répondait « 0 ligne à traiter » sur tout le vault **quel que soit l'état des
pitchs**, et cette réponse valait vérification dans la table. (Corrigé pour lire le niveau 3, il
signale 23 lignes, toutes des puces d'explication « Aucune alternative déclarée : … » que le
validateur exempte à raison : il ne valait plus la peine d'être maintenu.)

Le contrôle est **dur et dans le kit** : R1·R22, règle `reinjection_du_resume`. Il lit les
sections `Alternatives` et `Compléments`, et toute puce dont l'entrée est une cible du champ
`alternatives:` / `complements:` doit **commencer par** le `pitch:` courant de cette cible
(`**` et espaces normalisés, suffixe libre). Une puce dont l'entrée n'est pas une cible du
champ est exemptée. Sortie non nulle (code 1) s'il reste une puce à traiter.

```bash
uv run AI/scripts/check_brain.py --regle reinjection_du_resume | grep "<Cible>"   # vide = tout est à jour
```

- **`--regle` filtre l'affichage, pas le verdict à retenir.** La ligne finale d'un run filtré peut dire `OK — aucune violation dure` alors qu'une autre règle échoue (mesuré : une page au frontmatter illisible, hors de la règle demandée). `--regle` sert à **lire** un sous-ensemble ; le verdict est celui du run complet de `cloturer-brain`.
- **Vérifié sur une copie jetable du vault** : ajouter `, MODIFIE` à la fin du `pitch:` de Qdrant fait sortir `[FAIL] reinjection_du_resume` pour Milvus, Pinecone, Weaviate, pgvector (`### Alternatives`) et FastEmbed (`### Compléments`), avec le code de retour 1. La liste des `[FAIL]` **est** l'inventaire des puces à recopier — c'est ce que `[V1] <X>` donnait *avant* l'édition, et qu'on obtient maintenant *après*.
- La règle est à **0 violation** depuis le lot 8 : il n'y a plus de compte de référence à ne pas dépasser, le seuil est zéro.

### Cas particulier — retour d'expérience daté

Un bug rencontré n'est pas une modification de champ : il s'écrit dans la section
`## Retours` de la fiche concernée — **créée à cette occasion si elle n'existe pas** — et
**ne déclenche aucune propagation** — rayon nul. La section `## Pièges` qui l'accueillait a été
dissoute au lot 6 : elle ne contenait aucun retour, rien que des bornes de conception.

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

## Procédure — nouvelle valeur de catégorie

Déclencheur : `ou.py` sort en **code 2 ou 3**, ou l'arbre D1→D14 de `taxonomie.md` ne range pas
le sujet. **Ne jamais créer une valeur de catégorie sans l'accord de floSa** : elle change la
forme de l'arbre, et les trois valeurs les plus récentes (`data/messagerie`, `security/analyse`,
`data/catalogue`) portent toutes « sur arbitrage de floSa » dans leur message de commit.

1. **Proposer, puis attendre.** Une proposition tient en quatre lignes : la valeur (`<préfixe>/<sous>`, préfixe existant — un **nouveau préfixe** est un nouveau dossier racine, hors de cette procédure : le signaler et demander) ; la **frontière** (ce qui la distingue de chaque valeur voisine, avec la règle D-Rn qui tranche) ; le **libellé** du sous-dossier ; les tags. Préférer un sous-domaine sous un préfixe existant à un préfixe neuf (`data/messagerie`, `data/catalogue`).
2. **Poser le libellé.** Il ne sert que si le seuil est franchi, mais il se déclare dès l'ouverture : un seuil franchi sans libellé fait échouer la dérivation (`ou.py` code 4). Il ne redouble ni le nom du domaine parent (« Analyse de vulnérabilités » et non « Analyse de sécurité »), ni le nom d'une notion ou d'une page existante — le hub du dossier sera `<Libellé>.md`, nom unique dans le vault à la casse près :
   ```bash
   find . -iname "<Libellé>.md" -not -path "./.git/*" -not -path "./.claude/*"   # doit ne rien rendre
   ```
3. **Écrire les fichiers de vocabulaire — tous, ils bougent ensemble.**

   | Fichier | Rôle | Ce qu'on y écrit |
   |---|---|---|
   | `brain.yml` | **source machine** : c'est lui qui rend la valeur légale (R14, dure) | `axes.rangement.prefixes[<préfixe>].sous.<sous>` avec `libelle:`, `motif:` (date, arbitrage, collision évitée) et `frontiere:`. Rien ne contrôle le `motif:`, mais toutes les valeurs ouvertes récemment le portent : sans lui, le choix d'un libellé ne se relit pas |
   | `Documentation/general/taxonomie.md` | documentation lue par floSa, **non lue par le validateur** | la valeur dans le bloc de code ` ```domaine `, à sa place dans l'ordre du préfixe ; **le compte** en tête de fichier (« 110 valeurs ») et dans le titre de la section *Axe `categorie:`* ; la frontière, dans *Sous-domaines qui prêtent à confusion* |
   | `Documentation/general/tags.md` | vocabulaire fermé, lu par le validateur (R4) | seulement si de nouveaux tags : une ligne (tag en backticks, puis son sens et sa frontière) dans l'unique tableau *Vocabulaire*, à côté des tags du même sujet (colonne 1 en backticks, kebab-case, anglais, singulier). Un tag se **propose** à floSa, il ne s'invente pas |

   Piège mesuré : oublier `taxonomie.md` **ne casse aucun validateur** (`vocabulaires.taxonomie.genere: true`), donc la documentation ment sans que rien ne le dise. Le contrôle est humain : `grep -c "<valeur>" Documentation/general/taxonomie.md` doit rendre ≥ 1, et le compte doit avoir bougé de 1.
4. **Vérifier la dérivation** : `uv run .claude/skills/enrichir-brain/ou.py "<valeur>"` sort en code 0, et sa ligne `issue` dit ce qu'on attend (sous le seuil, ou promotion à signaler).
5. **Ne pas toucher au bloc `axes.rangement.mesure:`.** C'est un relevé daté écrit à la main (dernière mise à jour 2026-09-10) : `valeurs_declarees`, `sous_libelles_declares`, `sous_domaines_promus`… **Aucun script ne le régénère et aucun ne le lit** (recherché dans le kit figé : seules les mesures *par règle* sont exploitées, par `brainkit mesurer`). Il est périmé — au 2026-09-30 le manifeste déclare 116 valeurs quand le bloc en annonce 110 — et le corriger est un travail à part, pas un effet de bord d'une capture. Ne pas s'y fier pour un compte.
6. **Série de commits, vocabulaire en premier.** Les trois fichiers de vocabulaire ont leur commit, qui précède les pages qui portent la valeur ; la série se pousse d'un bloc (cf. *Règles d'usage* et `cloturer-brain`, étape 4). Message : la valeur, la frontière, le libellé et son motif, l'arbitrage de floSa, et le compte d'avertissements **mesuré sur l'état précédent**.

## Anti-patterns

- **Écrire la page et s'arrêter là.** Le rayon n'est pas optionnel : une brique insérée sans P1→P6 dégrade la structure au lieu de l'enrichir, et c'est précisément ce que le lot 7 corrige.
- **Sauter une ligne de P1→P6 en silence.** Une ligne sans objet se déclare sans objet.
- **Deviner le dossier au lieu de le dériver.** `categorie:` → `arbo.py` → chemin. Un fichier posé à vue fait échouer `check_arbo.py`, et il le fait après coup.
- **Sauter le contrôle de l'étape 8.** Confronter `git status` au `ls` du dossier est ce qui transforme une intention en fait vérifié.
- Créer la page demandée mais oublier la notion (P4) ou la réciprocité des alternatives (P5).
- **Rédiger le corps d'une page de mémoire**, sans recherche en ligne : le modèle peut être périmé, et une notion écrite de mémoire n'a ni source ni état de l'art.
- Inventer une catégorie, un tag, une famille ou un score (le score n'existe plus).
- Recopier un pitch divergent au lieu de réinjecter le `pitch:` de la cible.
- **Modifier un champ d'une page existante sans dérouler la table des effets de bord** : c'est l'origine mesurée des pitchs périmés du vault (constat C1 de l'audit axe 2).
- Substituer une prose comparative au pitch d'une cible listée en `alternatives:` (clause 3) — ou omettre le marqueur `voisin :` sur une puce dont la cible n'est pas dans `alternatives:`.
- Clore une mise à jour sur un `[FAIL] reinjection_du_resume` restant, ou croire une vérification qui répond « 0 » sans avoir vu qu'elle **cherche quelque chose** : `[V1]` répondait « 0 ligne » sur un vault entier parce que son motif ne trouvait aucune section.
- **Recopier de mémoire, dans un message ou une synthèse, un compte d'avertissements** : il n'est annoncé que s'il a été relevé sur l'état précédent *et* sur l'état final (cf. *Règles d'usage*).
- **Créer une valeur de catégorie sans l'accord de floSa**, ou la poser dans `taxonomie.md` sans `brain.yml` (ou l'inverse) : la moitié de la procédure ne compte pas.
- **`git push --force`, y compris sur une branche jamais poussée**, et `--no-verify`.
- Éditer une zone `<!-- AUTO -->` de hub à la main : elle sera écrasée à la clôture.
- Écrire un wikilink qualifié par chemin : il casse au prochain `git mv`, et les lots 4 à 6 en feront encore.
- Réécrire une notion existante sans que floSa l'ait demandé.
- Dupliquer une entrée d'expérience datée sur les deux briques d'un incident inter-briques.
- Oublier d'invoquer `cloturer-brain`, ou clore soi-même à sa place : la régénération, la validation, la vérification de divergence et le commit y sont écrits une seule fois.

## Voir aussi

- `cloturer-brain` — la clôture mécanique, appelée en fin de chaque procédure. **Seul endroit du vault où la politique git est écrite**, à l'exception de la règle d'identité, qui est dans `CLAUDE.md` parce qu'elle doit être lue à chaque conversation.
- `planifier-projet` — consomme l'index produit par la clôture.
- `AI/design/brain-v3.md` §10 (la règle de propagation), §12 (l'impact sur ce skill), §5 à §9 (les gabarits par rôle).
- `.claude/skills/enrichir-brain/ou.py` — le calcul du dossier d'accueil (versionné avec ce skill).
- `AI/migration/lot-7-skills.md` — le lot qui a écrit cette version.
